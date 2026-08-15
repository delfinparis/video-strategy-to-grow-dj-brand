#!/usr/bin/env python3
"""
Check that every deck in the repo is in the RIGHT Drive folder, not just in Drive.

The watchdog used to ask "is this deck in Drive?" and a deck filed under the wrong
brand answered yes. That is how four KIRP decks sat in `KR Carousels` for two days
while the 2026-08-14 heartbeat reported ok (docs/automation/carousel-drive-sync.md).
Existence is not delivery. Jennica opens one folder, and a deck in the other one is
missing as far as the morning is concerned.

So this asks the harder question, per deck: is it in the folder that
drive_sync.is_kirp() says it belongs in, and is it in only that folder?

Verdicts:
    ok          in the right folder
    misfiled    in Drive, in the wrong folder
    duplicate   in both folders, so one copy is stale the moment a deck re-renders
    missing     not in either folder

Anything but ok exits 1, so a GitHub Action can fail on it and mail D.J. Drive
folders with no matching deck in the repo are printed as a note, never a failure:
retired decks are allowed to stay in Drive.

Env: same as drive_sync.py.

Usage:
    python3 scripts/drive_audit.py                  # every deck in the repo
    python3 scripts/drive_audit.py --date 2026-08-15  # only that day's decks
    python3 scripts/drive_audit.py --json           # machine-readable summary
"""

import argparse
import json
import os
import sys

from drive_sync import (
    CAROUSEL_ROOT,
    KIRP_FOLDER_NAME,
    KR_FOLDER_NAME,
    drive_client,
    is_kirp,
    kirp_folder,
)


def child_folders(svc, parent_id):
    """Every non-trashed subfolder of parent_id, as {name: id}.

    Paginated on purpose. The default page size would quietly truncate a folder
    that is already past 30 decks, and a truncated listing reads exactly like a
    missing deck.
    """
    out = {}
    token = None
    while True:
        res = (
            svc.files()
            .list(
                q=(
                    f"'{parent_id}' in parents and trashed = false "
                    "and mimeType = 'application/vnd.google-apps.folder'"
                ),
                fields="nextPageToken, files(id, name)",
                pageSize=200,
                pageToken=token,
                supportsAllDrives=True,
                includeItemsFromAllDrives=True,
            )
            .execute()
        )
        for f in res.get("files", []):
            out[f["name"]] = f["id"]
        token = res.get("nextPageToken")
        if not token:
            return out


def local_decks(date=None):
    """Deck slugs in the repo, optionally only those built on one date.

    The date is matched against the slug (`KIRP-2026-08-15-...`) rather than the
    source frontmatter, because the daily engine puts it there and a deck that
    never got a source file is exactly the kind this should still audit.
    """
    if not os.path.isdir(CAROUSEL_ROOT):
        return []
    decks = sorted(
        d
        for d in os.listdir(CAROUSEL_ROOT)
        if os.path.isdir(os.path.join(CAROUSEL_ROOT, d))
    )
    if date:
        decks = [d for d in decks if date in d]
    return decks


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--date", help="only audit decks whose slug carries this date")
    ap.add_argument("--json", action="store_true", help="print a JSON summary too")
    args = ap.parse_args()

    kr_id = os.environ.get("DRIVE_CAROUSELS_FOLDER_ID", "").strip()
    if not kr_id:
        sys.exit("DRIVE_CAROUSELS_FOLDER_ID is not set")

    decks = local_decks(args.date)
    if not decks:
        print(f"No decks in the repo{' for ' + args.date if args.date else ''}.")
        return 1 if args.date else 0

    svc = drive_client()
    kirp_id = kirp_folder(svc, kr_id)
    in_kr = child_folders(svc, kr_id)
    in_kirp = child_folders(svc, kirp_id)

    print(f"{KR_FOLDER_NAME}: {len(in_kr)} folders")
    print(f"{KIRP_FOLDER_NAME}: {len(in_kirp)} folders\n")

    results = []
    for slug in decks:
        want_kirp = is_kirp(os.path.join(CAROUSEL_ROOT, slug))
        want, other = (
            (KIRP_FOLDER_NAME, KR_FOLDER_NAME)
            if want_kirp
            else (KR_FOLDER_NAME, KIRP_FOLDER_NAME)
        )
        here, there = (in_kirp, in_kr) if want_kirp else (in_kr, in_kirp)

        if slug in here and slug in there:
            verdict, detail = "duplicate", f"in both, extra copy in '{other}'"
        elif slug in here:
            verdict, detail = "ok", f"in '{want}'"
        elif slug in there:
            verdict, detail = "misfiled", f"in '{other}', belongs in '{want}'"
        else:
            verdict, detail = "missing", f"not in '{want}' or '{other}'"

        results.append({"deck": slug, "verdict": verdict, "expected": want})
        mark = " " if verdict == "ok" else "!"
        print(f"{mark} {verdict:9} {slug}: {detail}")

    known = set(decks) if not args.date else set(local_decks())
    orphans = sorted((set(in_kr) | set(in_kirp)) - known - {"gbp"})
    if orphans:
        print(f"\nIn Drive with no deck in the repo ({len(orphans)}), left alone:")
        for name in orphans:
            where = KR_FOLDER_NAME if name in in_kr else KIRP_FOLDER_NAME
            print(f"  {name} ({where})")

    bad = [r for r in results if r["verdict"] != "ok"]
    print(f"\n{len(results) - len(bad)} ok, {len(bad)} not ok.")
    if bad:
        print(
            "\nFix a misfiled or duplicated deck with the Drive reorg Action "
            "(dry run first). A missing deck needs the Graphics to Drive Action "
            "re-run for that folder."
        )
    if args.json:
        print("\n" + json.dumps({"decks": results, "orphans": orphans}, indent=2))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
