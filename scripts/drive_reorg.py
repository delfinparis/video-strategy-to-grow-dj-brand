#!/usr/bin/env python3
"""
Put every deck in the Drive folder it belongs in.

It started as the one-time split of the single `carousels` folder into Kale and
KIRP, and it is now the standing repair tool for whatever
[`drive_audit.py`](drive_audit.py) finds:

    carousels/                 ->  KR Carousels/
      KIRP-*-carousel/         ->    KIRP Carousels/KIRP-*-carousel/
      gbp/                     ->    KR Carousels/gbp/   (stays put)

It moves in **both** directions. A KIRP deck in KR goes to KIRP, and a Kale deck
in KIRP goes back to KR: on 2026-08-14 twenty-one older Kale decks turned up
inside KIRP Carousels, having been moved there by hand after the 08-12 sync put
them in KR, and a one-way tool could not put them back.

Which decks are KIRP comes from drive_sync.is_kirp(), so this script and the
sync can never disagree about where a deck belongs. It is the `KIRP-` slug
prefix, with `lane: "podcast"` as the fallback for anything unprefixed.

Safe to re-run: renaming a folder that is already named right is a no-op, and a
deck already in the right folder is left alone. It only ever moves a folder
between those two, never deletes, and never touches a deck it cannot find in
either.

Dry run by default. Nothing changes in Drive without --apply.

Env: same as drive_sync.py.

Usage:
    python3 scripts/drive_reorg.py
    python3 scripts/drive_reorg.py --apply
"""

import argparse
import os
import sys

from drive_sync import (
    CAROUSEL_ROOT,
    KIRP_FOLDER_NAME,
    KR_FOLDER_NAME,
    drive_client,
    ensure_folder,
    find_child,
    is_kirp,
)


def parent_of(svc, folder_id):
    parents = (
        svc.files()
        .get(fileId=folder_id, fields="parents", supportsAllDrives=True)
        .execute()
        .get("parents")
    )
    return parents[0] if parents else "root"


def local_decks():
    """Every deck in the repo, as (slug, belongs_in_kirp).

    Sharing is_kirp() with drive_sync is the point: if the two ever disagreed,
    this script would faithfully move decks the next sync would file back.
    """
    if not os.path.isdir(CAROUSEL_ROOT):
        return []
    return sorted(
        (d, is_kirp(os.path.join(CAROUSEL_ROOT, d)))
        for d in os.listdir(CAROUSEL_ROOT)
        if os.path.isdir(os.path.join(CAROUSEL_ROOT, d))
    )


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "--apply", action="store_true", help="actually change Drive (default: dry run)"
    )
    args = ap.parse_args()

    kr_id = os.environ.get("DRIVE_CAROUSELS_FOLDER_ID", "").strip()
    if not kr_id:
        sys.exit("DRIVE_CAROUSELS_FOLDER_ID is not set")

    decks = local_decks()
    if not decks:
        print(
            "No decks found locally. Nothing would move.\n"
            "Expected deck folders under graphics/carousels/.",
            file=sys.stderr,
        )

    mode = "APPLY" if args.apply else "DRY RUN, nothing will change"
    print(f"Drive reorg ({mode})\n")

    svc = drive_client()

    current = svc.files().get(
        fileId=kr_id, fields="id, name", supportsAllDrives=True
    ).execute()
    print(f"Kale folder: '{current['name']}' ({kr_id})")

    if current["name"] == KR_FOLDER_NAME:
        print(f"  already named '{KR_FOLDER_NAME}', leaving it")
    else:
        print(f"  rename '{current['name']}' -> '{KR_FOLDER_NAME}'")
        if args.apply:
            svc.files().update(
                fileId=kr_id, body={"name": KR_FOLDER_NAME}, supportsAllDrives=True
            ).execute()

    root = parent_of(svc, kr_id)
    existing_kirp = find_child(svc, root, KIRP_FOLDER_NAME, folder=True)
    if existing_kirp:
        kirp_id = existing_kirp
        print(f"\nKIRP folder: exists ({kirp_id})")
    elif args.apply:
        kirp_id = ensure_folder(svc, root, KIRP_FOLDER_NAME)
        print(f"\nKIRP folder: created ({kirp_id})")
    else:
        kirp_id = None
        print(f"\nKIRP folder: would create '{KIRP_FOLDER_NAME}' beside the Kale one")

    print(f"\nDecks checked ({len(decks)}):")
    moved = missing = already = 0
    for slug, want_kirp in decks:
        want_id, want_name = (
            (kirp_id, KIRP_FOLDER_NAME) if want_kirp else (kr_id, KR_FOLDER_NAME)
        )
        from_id, from_name = (
            (kr_id, KR_FOLDER_NAME) if want_kirp else (kirp_id, KIRP_FOLDER_NAME)
        )

        if want_id and find_child(svc, want_id, slug, folder=True):
            already += 1
            continue

        src_id = find_child(svc, from_id, slug, folder=True) if from_id else None
        if not src_id:
            # In neither folder, which usually means it was posted and the folder
            # deleted. Never re-upload on a hunch: that puts a published deck back
            # in Drive looking like it still needs posting. Name it and stop.
            print(f"  {slug}: in neither folder, most likely posted and cleared")
            missing += 1
            continue

        print(f"  {slug}: move '{from_name}' -> '{want_name}'")
        if args.apply:
            svc.files().update(
                fileId=src_id,
                addParents=want_id,
                removeParents=from_id,
                fields="id, parents",
                supportsAllDrives=True,
            ).execute()
        moved += 1

    print(
        f"\n{moved} to move, {already} already in the right folder, "
        f"{missing} gone from Drive (posted)."
    )
    if not args.apply:
        print("\nDry run. Re-run with --apply to make these changes.")
    elif kirp_id:
        print(
            f"\nDone. Optionally pin the folder by adding a DRIVE_KIRP_FOLDER_ID "
            f"secret set to {kirp_id}. The sync finds it by name without one."
        )


if __name__ == "__main__":
    main()
