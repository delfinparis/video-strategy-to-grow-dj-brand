#!/usr/bin/env python3
"""
One-time Drive reorg: split the single `carousels` folder into Kale and KIRP.

The folder started life holding everything. It is now 27 Kale decks and 3
podcast decks, so it is renamed to what it mostly already is, and the three
podcast decks move out to a sibling folder.

    carousels/                 ->  KR Carousels/
      KIRP-*-carousel/         ->    KIRP Carousels/KIRP-*-carousel/
      gbp/                     ->    KR Carousels/gbp/   (stays put)

Which decks are KIRP is not decided by the folder name. It comes from the
`lane: "podcast"` frontmatter on each deck's source markdown, the same field
that already decides whether a slide gets the podcast wordmark and the
keepingitrealpod.com footer instead of Kale's. Naming and routing cannot drift
apart that way.

Safe to re-run. Renaming a folder that is already named right is a no-op, and a
deck already in the KIRP folder is left alone.

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
    deck_lane,
    drive_client,
    ensure_folder,
    find_child,
)


def parent_of(svc, folder_id):
    parents = (
        svc.files()
        .get(fileId=folder_id, fields="parents", supportsAllDrives=True)
        .execute()
        .get("parents")
    )
    return parents[0] if parents else "root"


def local_kirp_decks():
    """Deck slugs whose source markdown declares the podcast lane."""
    if not os.path.isdir(CAROUSEL_ROOT):
        return []
    return sorted(
        d
        for d in os.listdir(CAROUSEL_ROOT)
        if os.path.isdir(os.path.join(CAROUSEL_ROOT, d))
        and deck_lane(os.path.join(CAROUSEL_ROOT, d)) == "podcast"
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

    decks = local_kirp_decks()
    if not decks:
        print(
            "No podcast-lane decks found locally. Nothing would move.\n"
            "Check that scripts/carousels/*.md still carry lane: \"podcast\".",
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

    print(f"\nPodcast-lane decks to move ({len(decks)}):")
    moved = missing = already = 0
    for slug in decks:
        src_id = find_child(svc, kr_id, slug, folder=True)
        if not src_id:
            if kirp_id and find_child(svc, kirp_id, slug, folder=True):
                print(f"  {slug}: already in KIRP Carousels")
                already += 1
            else:
                print(f"  {slug}: not in Drive yet, will land there on next sync")
                missing += 1
            continue
        print(f"  {slug}: move -> {KIRP_FOLDER_NAME}")
        if args.apply:
            svc.files().update(
                fileId=src_id,
                addParents=kirp_id,
                removeParents=kr_id,
                fields="id, parents",
                supportsAllDrives=True,
            ).execute()
        moved += 1

    print(
        f"\n{moved} to move, {already} already there, {missing} not yet in Drive."
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
