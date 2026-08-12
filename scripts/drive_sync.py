#!/usr/bin/env python3
"""
Mirror rendered carousel slides to Google Drive.

Runs in CI after a routine pushes new slides. Every deck folder under
graphics/carousels/ becomes a folder of the same name inside the Drive
`carousels` folder, so Jennica picks them up without touching GitHub.

Uploads are idempotent: a file that already exists by name in the target folder
is updated in place rather than duplicated, because decks get re-rendered
whenever their copy changes.

Auth is an OAuth refresh token, acting as D.J. himself, NOT a service account.
Service accounts have no Drive storage quota of their own, so anything they
upload to a personal My Drive is rejected with storageQuotaExceeded. Google's
workarounds for that are shared drives or domain-wide delegation, and both need
Google Workspace. This is a personal Gmail account, so the script authenticates
as the user and the files land against his own quota.

Get the token once with scripts/drive_auth.py.

GBP post cards ride the same pipe. They are flat files in graphics/gbp/ rather
than a folder per deck, so that whole directory syncs as one unit.

Env:
    GOOGLE_OAUTH_CLIENT_ID
    GOOGLE_OAUTH_CLIENT_SECRET
    GOOGLE_OAUTH_REFRESH_TOKEN
    DRIVE_CAROUSELS_FOLDER_ID     the parent folder id in Drive
    DRIVE_GBP_FOLDER_ID           optional. Where GBP cards go. Unset, they
                                  land in a `gbp` subfolder beside the decks.

Usage:
    python3 scripts/drive_sync.py <dir> [<dir> ...]
    python3 scripts/drive_sync.py graphics/gbp
    python3 scripts/drive_sync.py --all
"""

import json
import mimetypes
import os
import re
import sys

from google.auth.transport.requests import Request

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAROUSEL_ROOT = os.path.join(BASE_DIR, "graphics", "carousels")
# GBP post cards are flat files in one folder, not a folder per deck, so they
# sync as a single directory rather than one Drive folder per card.
GBP_ROOT = os.path.join(BASE_DIR, "graphics", "gbp")
SCOPES = ["https://www.googleapis.com/auth/drive"]

# Kale and the podcast are different audiences with different footers, so their
# decks are different deliverables and live in different Drive folders.
KR_FOLDER_NAME = "KR Carousels"
KIRP_FOLDER_NAME = "KIRP Carousels"

# Zips are gitignored, so they never reach CI. Everything else in a deck folder
# is something Jennica or LinkedIn needs.
UPLOAD_EXT = {".png", ".pdf", ".txt"}


def drive_client():
    """Build a Drive client from a stored refresh token."""
    missing = [
        k
        for k in (
            "GOOGLE_OAUTH_CLIENT_ID",
            "GOOGLE_OAUTH_CLIENT_SECRET",
            "GOOGLE_OAUTH_REFRESH_TOKEN",
        )
        if not os.environ.get(k, "").strip()
    ]
    if missing:
        sys.exit(
            "Missing OAuth secret(s): "
            + ", ".join(missing)
            + "\nRun scripts/drive_auth.py once to mint them, then add them as repo "
            "secrets. See docs/automation/carousel-drive-sync.md."
        )

    creds = Credentials(
        None,
        refresh_token=os.environ["GOOGLE_OAUTH_REFRESH_TOKEN"].strip(),
        client_id=os.environ["GOOGLE_OAUTH_CLIENT_ID"].strip(),
        client_secret=os.environ["GOOGLE_OAUTH_CLIENT_SECRET"].strip(),
        token_uri="https://oauth2.googleapis.com/token",
        scopes=SCOPES,
    )
    try:
        creds.refresh(Request())
    except Exception as e:
        sys.exit(
            f"Could not refresh the OAuth token: {e}\n"
            "If this says invalid_grant, the refresh token has been revoked or "
            "expired. That happens when the OAuth consent screen is still in "
            "Testing status, where Google expires refresh tokens after 7 days. "
            "Set the consent screen to In production, then re-run "
            "scripts/drive_auth.py and update the GOOGLE_OAUTH_REFRESH_TOKEN secret."
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


def sync_dir(svc, parent_id, src_dir, nest=True):
    """Mirror one local directory into Drive.

    nest=True puts the files in a Drive subfolder named after the directory,
    which is what every deck wants. nest=False uploads straight into parent_id,
    for when the target folder in Drive already is the destination.
    """
    slug = os.path.basename(src_dir.rstrip("/"))
    files = sorted(
        os.path.join(src_dir, f)
        for f in os.listdir(src_dir)
        if os.path.splitext(f)[1].lower() in UPLOAD_EXT
    )
    if not files:
        print(f"  {slug}: nothing to upload")
        return
    folder_id = ensure_folder(svc, parent_id, slug) if nest else parent_id
    counts = {"created": 0, "updated": 0}
    for path in files:
        counts[upload(svc, folder_id, path)] += 1
    print(f"  {slug}: {counts['created']} new, {counts['updated']} updated")


def is_gbp(path):
    return os.path.abspath(path).rstrip("/") == GBP_ROOT


LANE_RE = re.compile(r'^lane:\s*"?([\w-]+)')


def deck_lane(deck_dir):
    """Read the lane out of the deck's source markdown frontmatter.

    A rendered deck folder carries no metadata of its own, but it is named for
    the same slug as its source file, so the lane is one read away. Anything
    unreadable falls back to the Kale side, which is where 27 of 30 decks
    belong: a misfiled Kale deck is a smaller problem than a KIRP folder that
    silently stops receiving decks.
    """
    slug = os.path.basename(deck_dir.rstrip("/"))
    src = os.path.join(BASE_DIR, "scripts", "carousels", slug + ".md")
    try:
        with open(src, encoding="utf-8") as fh:
            for _ in range(30):
                line = fh.readline()
                if not line:
                    break
                match = LANE_RE.match(line)
                if match:
                    return match.group(1)
    except OSError:
        pass
    return ""


def is_kirp(deck_dir):
    return deck_lane(deck_dir) == "podcast"


def kirp_folder(svc, kr_id):
    """The KIRP folder, resolved as a sibling of the Kale one.

    Pinning it to a secret is supported but not required. Without one the
    folder is found (or created) by name next to the Kale folder, so the split
    works the moment the code lands, with no secret to mint first.
    """
    pinned = os.environ.get("DRIVE_KIRP_FOLDER_ID", "").strip()
    if pinned:
        return pinned
    parents = (
        svc.files()
        .get(fileId=kr_id, fields="parents", supportsAllDrives=True)
        .execute()
        .get("parents")
        or ["root"]
    )
    return ensure_folder(svc, parents[0], KIRP_FOLDER_NAME)


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)

    carousels_id = os.environ.get("DRIVE_CAROUSELS_FOLDER_ID", "").strip()
    if not carousels_id:
        sys.exit("DRIVE_CAROUSELS_FOLDER_ID is not set")
    # Optional. Without it the GBP cards land in a `gbp` subfolder beside the
    # decks, which still gets them to Jennica. Set it to give them their own
    # top-level folder, and they upload straight into it.
    gbp_id = os.environ.get("DRIVE_GBP_FOLDER_ID", "").strip()

    if args == ["--all"]:
        dirs = [
            os.path.join(CAROUSEL_ROOT, d)
            for d in sorted(os.listdir(CAROUSEL_ROOT))
            if os.path.isdir(os.path.join(CAROUSEL_ROOT, d))
        ]
        if os.path.isdir(GBP_ROOT):
            dirs.append(GBP_ROOT)
    else:
        dirs = [d for d in args if os.path.isdir(d)]

    if not dirs:
        print("Nothing to sync.")
        return

    svc = drive_client()
    check_parent(svc, carousels_id)
    if gbp_id and any(is_gbp(d) for d in dirs):
        check_parent(svc, gbp_id)

    # Resolved once, and only when a podcast deck is actually in this run.
    kirp_id = None

    print(f"Syncing {len(dirs)} folder(s) to Drive:")
    for path in dirs:
        if is_gbp(path):
            sync_dir(svc, gbp_id or carousels_id, path, nest=not gbp_id)
        elif is_kirp(path):
            if kirp_id is None:
                kirp_id = kirp_folder(svc, carousels_id)
            sync_dir(svc, kirp_id, path)
        else:
            sync_dir(svc, carousels_id, path)


if __name__ == "__main__":
    main()
