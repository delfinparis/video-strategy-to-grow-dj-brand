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
    creds = service_account.Credentials.from_service_account_info(
        json.loads(raw), scopes=SCOPES
    )
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
    print(f"Syncing {len(decks)} deck(s) to Drive:")
    for deck in decks:
        sync_deck(svc, parent_id, deck)


if __name__ == "__main__":
    main()
