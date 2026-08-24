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

**A deck that is gone from Drive has usually been posted.** D.J. and Jennica delete
a deck's folder once it goes out, so an empty space is how they track what has
shipped. That makes absence ambiguous rather than bad, and the ambiguity is only
resolvable by date:

  - Auditing the whole library, a deck in neither folder is assumed posted and
    cleared. Failing on those would mean an alarm that rings for every deck ever
    published, which is an alarm nobody reads.
  - Auditing one day (`--date`, what the heartbeat runs), a deck in neither folder
    is a real failure, because this morning's decks should still be sitting there
    unposted. If one was posted and cleared before the check ran, Drive's trash
    still holds the folder, and a deck found there counts as delivered.

Verdicts:
    ok          in the right folder
    misfiled    in Drive, in the wrong folder                       fails
    duplicate   in both folders, one copy goes stale on re-render   fails
    posted      gone from Drive, or trashed on the audited day      passes
    missing     gone, nothing trashed that day, and dated today     fails

Drive folders with no matching deck in the repo are printed as a note, never a
failure: retired decks are allowed to stay in Drive.

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
    GBP_FOLDER_NAME,
    GBP_ROOT,
    KIRP_FOLDER_NAME,
    KR_FOLDER_NAME,
    drive_client,
    ensure_folder,
    is_kirp,
    kirp_folder,
)


# A deck that is where it belongs and one that was posted and cleared are both
# fine mornings. Only a wrong folder or a deck that never arrived is a fault.
PASSING = {"ok", "posted"}

# D.J. raised GBP from one card a day to two on 2026-08-20. This is the only
# place that number is CHECKED rather than merely instructed: check_heartbeat.py
# reads the routine's own report of itself, and a routine that quietly produced
# one card would report one card and pass. The GBP cards spent a week landing in
# the wrong Drive folder precisely because nothing independent counted them.
GBP_CARDS_PER_DAY = 2


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


def child_files(svc, parent_id):
    """Every non-trashed FILE directly inside parent_id, as {name: id}."""
    out = {}
    token = None
    while True:
        res = (
            svc.files()
            .list(
                q=(
                    f"'{parent_id}' in parents and trashed = false "
                    "and mimeType != 'application/vnd.google-apps.folder'"
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


def local_gbp(date=None):
    """The GBP cards in the repo, as {slug: {"image": name, "caption": name}}.

    A card is an image plus its caption. They live in two folders locally and
    mirror to two folders in Drive, so a card is only delivered when BOTH have
    arrived. Keyed by slug so a half-card is visible as a half-card rather than
    as two unrelated files.
    """
    cards = {}
    for kind in ("image", "caption"):
        d = os.path.join(GBP_ROOT, kind)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            stem, ext = os.path.splitext(name)
            if not ext or ext.lower() not in (".png", ".jpg", ".jpeg", ".txt"):
                continue
            if date and not stem.startswith(date):
                continue
            cards.setdefault(stem, {})[kind] = name
    return cards


def audit_gbp(svc, kr_id, date, results):
    """Audit GBP cards the same way decks are audited: by folder, not existence.

    GBP was carved out of this audit when it was written -- the orphan scan
    still skips the `gbp` folder by name -- so from 2026-08-14 the cards were
    the one thing the morning check could not see. That is exactly how every
    card ended up somewhere other than `gbp > image` and `gbp > caption` with
    the heartbeat reporting ok every single day.
    """
    cards = local_gbp(date)
    if not cards:
        if date:
            results.append({"deck": "gbp/<none>", "verdict": "missing",
                            "expected": GBP_FOLDER_NAME})
            print(f"\nGBP cards checked (0):")
            print(f"! missing   no GBP card rendered for {date} at all. "
                  f"Expected {GBP_CARDS_PER_DAY}.")
        return

    gbp_id = ensure_folder(svc, kr_id, GBP_FOLDER_NAME)
    subs = child_folders(svc, gbp_id)
    present = {
        kind: (child_files(svc, subs[kind]) if kind in subs else {})
        for kind in ("image", "caption")
    }

    print(f"\nGBP cards checked ({len(cards)}):")
    for slug in sorted(cards):
        want = cards[slug]
        halves, missing = [], []
        for kind in ("image", "caption"):
            name = want.get(kind)
            if not name:
                missing.append(f"no {kind} rendered in the repo")
            elif name in present[kind]:
                halves.append(kind)
            else:
                missing.append(f"{kind} not in '{GBP_FOLDER_NAME} > {kind}'")

        if not missing:
            verdict, detail = "ok", "image and caption both filed"
        elif halves:
            verdict, detail = "half-card", "; ".join(missing)
        else:
            verdict, detail = "missing", "; ".join(missing)

        results.append({"deck": f"gbp/{slug}", "verdict": verdict,
                        "expected": GBP_FOLDER_NAME})
        mark = " " if verdict in PASSING else "!"
        print(f"{mark} {verdict:9} {slug}: {detail}")

    # The daily quota, checked against what is actually on disk for that date.
    # Only meaningful for a dated audit: the whole library has no daily shape.
    if date and len(cards) < GBP_CARDS_PER_DAY:
        results.append({"deck": f"gbp/{date}-quota", "verdict": "short",
                        "expected": f"{GBP_CARDS_PER_DAY} cards"})
        print(f"! short     {len(cards)} card(s) for {date}, expected "
              f"{GBP_CARDS_PER_DAY}. Either the routine produced one, or it "
              f"found only one honest angle and should have said so in its "
              f"run summary.")
    elif date and len(cards) > GBP_CARDS_PER_DAY:
        print(f"  note      {len(cards)} cards for {date}, more than the "
              f"{GBP_CARDS_PER_DAY} expected. Not a failure.")

    stray = sorted(
        (set(present["image"]) | set(present["caption"]))
        - {n for c in local_gbp().values() for n in c.values()}
    )
    if stray:
        print(f"\n  In '{GBP_FOLDER_NAME}' with no card in the repo "
              f"({len(stray)}), left alone:")
        for name in stray:
            print(f"    {name}")


def in_trash(svc, slug, date):
    """True if this deck was trashed ON the day being audited.

    Deleting a posted deck is how the folder empties out, so the trash is the
    receipt: it says the folder existed and was cleared on purpose, which is the
    one thing that distinguishes a posted deck from one that never arrived.

    The day matters. The trash also holds old copies cleared during the
    2026-08-15 cleanup, and a name match against one of those would let a deck
    that never arrived this morning pass as posted. That is the false all-clear
    this whole check exists to stop, so only a same-day trashing counts.
    Emptying the trash loses the receipt and the deck reads as missing.
    """
    safe = slug.replace("'", "\\'")
    res = (
        svc.files()
        .list(
            q=(
                f"name = '{safe}' and trashed = true "
                "and mimeType = 'application/vnd.google-apps.folder'"
            ),
            fields="files(id, trashedTime)",
            pageSize=10,
            supportsAllDrives=True,
            includeItemsFromAllDrives=True,
        )
        .execute()
    )
    return any(
        str(f.get("trashedTime", "")).startswith(date) for f in res.get("files", [])
    )


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
        elif not args.date:
            verdict, detail = "posted", "gone from Drive, so it went out"
        elif in_trash(svc, slug, args.date):
            verdict, detail = "posted", "trashed today, so it went out and was cleared"
        else:
            verdict, detail = (
                "missing",
                f"not in '{want}', '{other}', or the trash. It never arrived",
            )

        results.append({"deck": slug, "verdict": verdict, "expected": want})
        mark = " " if verdict in PASSING else "!"
        print(f"{mark} {verdict:9} {slug}: {detail}")

    audit_gbp(svc, kr_id, args.date, results)

    known = set(decks) if not args.date else set(local_decks())
    # `gbp` is a real folder that holds cards, not a stray deck, so it is not an
    # orphan. It is audited by audit_gbp above rather than skipped, which is the
    # difference between excluding something and ignoring it.
    orphans = sorted((set(in_kr) | set(in_kirp)) - known - {GBP_FOLDER_NAME})
    if orphans:
        print(f"\nIn Drive with no deck in the repo ({len(orphans)}), left alone:")
        for name in orphans:
            where = KR_FOLDER_NAME if name in in_kr else KIRP_FOLDER_NAME
            print(f"  {name} ({where})")

    bad = [r for r in results if r["verdict"] not in PASSING]
    gbp_n = sum(1 for r in results if r["deck"].startswith("gbp/"))
    posted = [r for r in results if r["verdict"] == "posted"]
    print(
        f"\n{len(results) - len(bad) - len(posted)} ok, {len(posted)} already posted, "
        f"{len(bad)} not ok  ({len(results) - gbp_n} deck(s), {gbp_n} GBP card(s))."
    )
    if bad:
        print(
            "\nFix a misfiled or duplicated deck with the Drive reorg Action "
            "(dry run first). A missing deck needs the Graphics to Drive Action "
            "re-run for that folder. Re-syncing a deck that was posted and cleared "
            "puts it back in Drive looking unposted, so check before re-running."
        )
    if args.json:
        print("\n" + json.dumps({"decks": results, "orphans": orphans}, indent=2))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
