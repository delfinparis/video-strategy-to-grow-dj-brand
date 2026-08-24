#!/usr/bin/env python3
"""
Fail loudly when the carousel watchdog stops reporting.

This is the alarm for the alarm. The watchdog checks that the morning's decks
reached Drive and emails D.J. when they did not, but nothing was watching the
watchdog: if it stopped firing, or the Claude Gmail connector lost its
authorization, a broken morning and a perfect one both produced total silence.
That exact failure mode already cost five days of walk-and-talk briefs in June
2026 (docs/automation/walk-and-talk-delivery.md).

So the watchdog now writes data/carousel-heartbeat.json on every run, pass or
fail, and this script is run by a GitHub Action that FAILS when the heartbeat is
stale or reports a bad morning. GitHub emails on a failed scheduled workflow,
which is the point: that notification comes from GitHub's own infrastructure and
does not touch the Gmail connector, the routine scheduler, or Make. Everything
upstream can be dead at once and this still reaches him.

Exit codes:
    0   heartbeat is today's and says ok
    1   heartbeat is stale, missing, malformed, or says failed

Usage:
    python3 scripts/check_heartbeat.py
    python3 scripts/check_heartbeat.py --today 2026-08-14   # for testing
"""

import argparse
import datetime
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEARTBEAT = os.path.join(BASE_DIR, "data", "carousel-heartbeat.json")

# The watchdog runs at 14:00 UTC and this check at 16:30 UTC, so on a healthy
# day the stamp is always today's. One day of slack would delay detection by a
# whole day, and a carousel morning that silently vanished is exactly what this
# exists to catch, so the window is deliberately tight.
FIX_HINTS = """
WHAT TO CHECK, in order:

1. Did the watchdog routine run at all?
   https://claude.ai/code/routines  ->  "Carousel watchdog"
   A paused or errored routine writes no heartbeat.

2. Did the daily carousel engine run? (6:30am CT)
   Same page. If the engine died, the watchdog should have emailed already.
   If you got no email either, suspect the Gmail connector, see 3.

3. Is the Claude Gmail connector still authorized?
   https://claude.ai/customize/connectors
   This is the failure that makes a broken morning look identical to a good
   one, because it kills the watchdog's email without killing the watchdog.
   It is also why you are reading this message instead of nothing at all.

4. Could the watchdog not push? A heartbeat it wrote but failed to push
   never reaches this check. Look for push errors in the run log.
"""


def load():
    if not os.path.exists(HEARTBEAT):
        return None, f"No heartbeat file at {os.path.relpath(HEARTBEAT, BASE_DIR)}"
    try:
        with open(HEARTBEAT, encoding="utf-8") as fh:
            return json.load(fh), None
    except (OSError, ValueError) as e:
        return None, f"Heartbeat file is unreadable: {e}"


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--today", help="override today's date, for testing")
    args = ap.parse_args()

    today = args.today or datetime.datetime.now(datetime.timezone.utc).date().isoformat()

    beat, err = load()
    if err:
        print(f"CAROUSEL HEARTBEAT MISSING\n\n{err}\n{FIX_HINTS}", file=sys.stderr)
        return 1

    stamped = str(beat.get("date", "")).strip()
    status = str(beat.get("status", "")).strip().lower()
    missing = beat.get("missing") or []

    if stamped != today:
        print(
            f"CAROUSEL HEARTBEAT STALE\n\n"
            f"Expected today ({today}), the watchdog last reported {stamped or 'never'}.\n"
            f"Nobody checked whether this morning's carousels reached Drive.\n{FIX_HINTS}",
            file=sys.stderr,
        )
        return 1

    if status != "ok":
        detail = "\n".join(f"  - {m}" for m in missing) or "  (the watchdog did not say which)"
        print(
            f"CAROUSEL DELIVERY FAILED ({today})\n\n"
            f"The watchdog ran and reported status '{status or 'unknown'}'.\n"
            f"Missing:\n{detail}\n\n"
            f"It should also have drafted you an email with the full diagnosis.\n"
            f"If no email arrived, the Gmail connector is the next thing to check.\n",
            file=sys.stderr,
        )
        return 1

    print(f"Carousel heartbeat OK for {today}. Watchdog ran and found all eight delivered.")
    print(
        "This only reports what the watchdog said about itself. The independent "
        "check is `drive_audit.py --date <today>`, which reads Drive."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
