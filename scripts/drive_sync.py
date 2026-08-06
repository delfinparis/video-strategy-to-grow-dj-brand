#!/usr/bin/env python3
"""
Mirror rendered carousel slides to Google Drive.

Runs in CI after a routine pushes new slides. Every deck folder under
graphics/carousels/ becomes a folder of the same name inside the Drive
`carousels` folder, so Jennica picks them up without touching GitHub.

Uploads are idempotent: a file that already exists by name in the target folder
is updated in place rather than duplicated, because decks get re-rendered
whenever their copy changes.

Auth is a Google service account. The `carousels` Drive folder has to be shared
with the service account's email as Editor, or it cannot see the folder at all.

Env:
    GOOGLE_SERVICE_ACCOUNT_JSON   the service account key, as JSON
    DRIVE_CAROUSELS_FOLDER_ID     the parent folder id in Drive

Usage:
    python3 scripts/drive_sync.py <deck-dir> [<deck-dir> ...]
    python3 scripts/drive_sync.py --all
"""

import json
import mimetypes
import os
import sys

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAROUSEL_ROOT = os.path.join(BASE_DIR, "graphics", "carousels")
SCOPES = ["https://www.googleapis.com/auth/drive"]

# Zips are gitignored, so they never reach CI. Everything else in a deck folder
# is something Jennica or LinkedIn needs.
UPLOAD_EXT = {".png", ".pdf", ".txt"}


def drive_client():
    raw = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "").strip()
    if not raw:
        sys.exit("GOOGLE_SERVICE_ACCOUNT_JSON is not set")

    # Diagnose a bad secret without ever printing it. A truncated or partial
    # paste is the usual cause, and the raw JSONDecodeError says nothing useful.
    try:
        info = json.loads(raw)
    except json.JSONDecodeError as e:
        sys.exit(
            "GOOGLE_SERVICE_ACCOUNT_JSON is not valid JSON "
            f"({e.msg} at char {e.pos}). Length is {len(raw)} chars and it starts "
            f"with {raw[:1]!r}. A real key is ~2300 chars and starts with '{{'. "
            "Re-set it straight from the file so nothing is lost in a paste:\n"
            "  gh secret set GOOGLE_SERVICE_ACCOUNT_JSON < /path/to/key.json"
        )

    if not isinstance(info, dict) or info.get("type") != "service_account":
        sys.exit(
            "GOOGLE_SERVICE_ACCOUNT_JSON parsed but is not a service account key. "
            "Download a fresh JSON key from the service account's Keys tab."
        )
    missing = [k for k in ("client_email", "private_key", "token_uri") if not info.get(k)]
    if missing:
        sys.exit(f"Service account key is missing required field(s): {', '.join(missing)}")

    print(f"Authenticating as {info['client_email']}")
    creds = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def find_child(svc, parent_id, name, folder=False):
    q = [
        f"'{parent_id}' in parents",
        f"name = '{name.replace(chr(39), chr(92) + chr(39))}'",
        "trashed = false",
    ]
    if folder:
        q.append("mimeType = 'application/vnd.google-apps.folder'")
    res = (
        svc.files()
        .list(
            q=" and ".join(q),
            fields="files(id, name)",
            pageSize=1,
            supportsAllDrives=True,
            includeItemsFromAllDrives=True,
        )
        .execute()
    )
    files = res.get("files", [])
    return files[0]["id"] if files else None


def ensure_folder(svc, parent_id, name):
    existing = find_child(svc, parent_id, name, folder=True)
    if existing:
        return existing
    meta = {
        "name": name,
        "mimeType": "application/vnd.google-apps.folder",
        "parents": [parent_id],
    }
    return svc.files().create(body=meta, fields="id", supportsAllDrives=True).execute()["id"]


def upload(svc, folder_id, path):
    name = os.path.basename(path)
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    media = MediaFileUpload(path, mimetype=mime, resumable=False)
    existing = find_child(svc, folder_id, name)
    if existing:
        svc.files().update(fileId=existing, media_body=media, supportsAllDrives=True).execute()
        return "updated"
    svc.files().create(
        body={"name": name, "parents": [folder_id]},
        media_body=media,
        fields="id",
        supportsAllDrives=True,
    ).execute()
    return "created"


def check_parent(svc, parent_id):
    """Confirm the service account can actually see the target folder.

    A service account sees nothing in Drive until the folder is explicitly
    shared with its email, and the API's 404 for that case reads identically to
    a wrong folder id. Say which it is.
    """
    try:
        f = svc.files().get(fileId=parent_id, fields="id, name", supportsAllDrives=True).execute()
        print(f"Target folder: {f['name']}")
    except Exception as e:
        sys.exit(
            f"Cannot open Drive folder {parent_id}: {e}\n"
            "If this is a 404, the folder is almost certainly not shared with the "
            "service account. Open the folder in Drive, Share, add the "
            "client_email printed above as Editor."
        )


def sync_deck(svc, parent_id, deck_dir):
    slug = os.path.basename(deck_dir.rstrip("/"))
    files = sorted(
        os.path.join(deck_dir, f)
        for f in os.listdir(deck_dir)
        if os.path.splitext(f)[1].lower() in UPLOAD_EXT
    )
    if not files:
        print(f"  {slug}: nothing to upload")
        return
    folder_id = ensure_folder(svc, parent_id, slug)
    counts = {"created": 0, "updated": 0}
    for path in files:
        counts[upload(svc, folder_id, path)] += 1
    print(f"  {slug}: {counts['created']} new, {counts['updated']} updated")


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)

    parent_id = os.environ.get("DRIVE_CAROUSELS_FOLDER_ID", "").strip()
    if not parent_id:
        sys.exit("DRIVE_CAROUSELS_FOLDER_ID is not set")

    if args == ["--all"]:
        decks = [
            os.path.join(CAROUSEL_ROOT, d)
            for d in sorted(os.listdir(CAROUSEL_ROOT))
            if os.path.isdir(os.path.join(CAROUSEL_ROOT, d))
        ]
    else:
        decks = [d for d in args if os.path.isdir(d)]

    if not decks:
        print("No deck folders to sync.")
        return

    svc = drive_client()
    check_parent(svc, parent_id)
    print(f"Syncing {len(decks)} deck(s) to Drive:")
    for deck in decks:
        sync_deck(svc, parent_id, deck)


if __name__ == "__main__":
    main()
