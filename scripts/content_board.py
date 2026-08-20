#!/usr/bin/env python3
"""
Engine for the Notion Content Board.

The board is the picking surface D.J. actually uses: he opens a row and the
whole finished script is sitting there, ready to film. This script owns the
half a model should not be trusted with, exactly like scripts/stupid_things.py
owns it for the Stupid Things bank:

  - counting what is Open per lane and deciding whether a refill is due
  - deciding which rows have EXPIRED and must be killed
  - deciding which rows are missing their script body and must be filled
  - refusing a hook that is a reword of one already on the board

The judgment half -- researching the story, writing the four-pass v3, checking
the receipt -- belongs to the cloud routine, which has web search and the repo.
See docs/automation/content-board.md.

The board carries NO source column and NO bank ref column (D.J., 2026-08-20:
"I don't need the source column, or the bank ref"). Both still exist, inside
the page body: the receipt lives under `## Data Source` where the repo standard
already puts it, and the bank pointer lives in the one-line footer this script
emits and parses. Dropping them from the board did not drop them from the
system.

Usage:
  python3 scripts/content_board.py health --board board.json
      Exit 0 = board is stocked and every row has a body. Exit 10 = work due.
      The exit code is the whole interface the routine needs.

  python3 scripts/content_board.py plan --board board.json
      The work order as JSON: what to kill, what to fill, what to add.

  python3 scripts/content_board.py check-hook --board board.json --hook "..."
      Exit 0 = novel. Exit 11 = too close to a hook already on the board.

  python3 scripts/content_board.py footer --lane News --ref "news-briefs/2026-08-20.md #1"
      The exact footer line to paste at the bottom of a page body.

board.json is the snapshot the routine exports from Notion before planning:
  [{"url": "...", "lane": "News", "status": "Open",
    "hook": "...", "expires": "2026-08-22", "has_body": false}, ...]

Dependencies: none (standard library only).
"""

import argparse
import json
import os
import re
import sys
from datetime import date, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE_DIR, "data")

# How many Open rows each lane should carry. Sized off the weekly plan in
# CLAUDE.md (15 videos/week) so the board holds roughly two weeks of runway,
# except News, which is deliberately shallow because it rots.
TARGETS = {
    "News": 3,
    "Agent Tip": 4,
    "Take": 6,
    "Broker Problems": 4,
    "Stupid Things Realtors Do": 6,
    "Agent Spotlight": 2,
    "KIRP Episode": 4,
}

# Refill when a lane drops to or below this. Prevents a one-row top-up every
# single day, which is how a bank fills with filler.
REFILL_TRIGGER = {
    "News": 2,
    "Agent Tip": 2,
    "Take": 3,
    "Broker Problems": 2,
    "Stupid Things Realtors Do": 3,
    "Agent Spotlight": 1,
    "KIRP Episode": 2,
}

# Where the routine goes to find new candidates for each lane. These are read
# by the routine, not by this script -- it only reports which ones are present,
# so a refill can never quietly source a lane from nothing.
SOURCES = {
    "News": ["data/news-briefs/<today>.md"],
    "Agent Tip": ["data/news-briefs/<today>.md"],
    "Take": ["data/take-briefs/<latest>.md", "data/sacred-cows.md"],
    "Broker Problems": ["docs/content-pillars.md", "web search for the receipt"],
    "Stupid Things Realtors Do": ["python3 scripts/stupid_things.py pick --count N"],
    "Agent Spotlight": ["docs/series/chicago-agent-spotlight-standard.md (scout live)"],
    "KIRP Episode": ["python3 scripts/kirp_source.py --peek"],
}

# Lanes whose rows rot. Everything else waits on the shelf indefinitely.
PERISHABLE = {"News": 3, "Agent Tip": 7}

LIVE_STATUSES = {"Open", "Picked"}
FOOTER_PREFIX = "Bank ref:"

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "because", "but", "by", "for",
    "from", "has", "have", "here", "how", "in", "is", "it", "its", "just",
    "not", "of", "on", "or", "s", "so", "that", "the", "their", "then",
    "there", "they", "this", "to", "was", "what", "when", "who", "why",
    "will", "with", "you", "your", "youre",
}


def today():
    """Overridable for tests, and for a routine that runs either side of UTC midnight."""
    stamp = os.environ.get("CONTENT_BOARD_TODAY")
    return date.fromisoformat(stamp) if stamp else date.today()


def normalize(text):
    """Content words only, so 'Your cap you never hit' collides with 'The cap you have never once hit'."""
    words = re.findall(r"[a-z0-9]+", (text or "").lower())
    return [w for w in words if w not in STOPWORDS]


def similarity(a, b):
    """Jaccard over content words. Cheap, offline, and good enough to catch a reword."""
    sa, sb = set(normalize(a)), set(normalize(b))
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


DUPE_THRESHOLD = 0.6


def load_board(path):
    with open(path) as fh:
        rows = json.load(fh)
    if not isinstance(rows, list):
        sys.exit("board.json must be a list of row objects")
    for row in rows:
        row.setdefault("status", "Open")
        row.setdefault("lane", "")
        row.setdefault("hook", "")
        row.setdefault("expires", None)
        row.setdefault("has_body", False)
    return rows


def source_status():
    """Report which candidate sources actually exist right now."""
    stamp = today().isoformat()
    present = {}
    news = os.path.join(DATA, "news-briefs", f"{stamp}.md")
    present["news_brief_today"] = (
        f"data/news-briefs/{stamp}.md" if os.path.exists(news) else None
    )

    takes = sorted(
        f for f in os.listdir(os.path.join(DATA, "take-briefs"))
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}\.md", f)
    ) if os.path.isdir(os.path.join(DATA, "take-briefs")) else []
    present["take_brief_latest"] = (
        os.path.join("data/take-briefs", takes[-1]) if takes else None
    )
    present["sacred_cows"] = (
        "data/sacred-cows.md" if os.path.exists(os.path.join(DATA, "sacred-cows.md")) else None
    )
    present["stupid_things_bank"] = (
        "data/stupid-things.json" if os.path.exists(os.path.join(DATA, "stupid-things.json")) else None
    )
    return present


def build_plan(rows):
    stamp = today()
    kill, fill = [], []

    for row in rows:
        if row["status"] not in LIVE_STATUSES:
            continue
        expires = row.get("expires")
        if expires:
            try:
                if date.fromisoformat(expires) < stamp:
                    kill.append({
                        "url": row["url"],
                        "hook": row["hook"],
                        "lane": row["lane"],
                        "reason": f"expired {expires}",
                    })
                    continue
            except ValueError:
                pass  # a malformed date is not a reason to kill a good row
        if not row.get("has_body"):
            fill.append({"url": row["url"], "hook": row["hook"], "lane": row["lane"]})

    killed = {k["url"] for k in kill}
    live = [r for r in rows if r["status"] in LIVE_STATUSES and r["url"] not in killed]

    counts = {lane: 0 for lane in TARGETS}
    for row in live:
        if row["lane"] in counts:
            counts[row["lane"]] += 1

    need = {}
    for lane, target in TARGETS.items():
        have = counts[lane]
        if have <= REFILL_TRIGGER[lane]:
            need[lane] = target - have

    return {
        "date": stamp.isoformat(),
        "counts": counts,
        "targets": TARGETS,
        "kill": kill,
        "fill": fill,
        "need": need,
        "expiry_days": PERISHABLE,
        "sources": {lane: SOURCES[lane] for lane in need},
        "sources_present": source_status(),
        "seen_hooks": [r["hook"] for r in live],
        "work_due": bool(kill or fill or need),
    }


def cmd_plan(args):
    plan = build_plan(load_board(args.board))
    print(json.dumps(plan, indent=2))
    return 0


def cmd_health(args):
    plan = build_plan(load_board(args.board))
    parts = [f"{lane} {plan['counts'][lane]}/{TARGETS[lane]}" for lane in TARGETS]
    print("Board: " + ", ".join(parts))
    print(
        f"kill {len(plan['kill'])}, fill {len(plan['fill'])}, "
        f"lanes needing rows {len(plan['need'])}"
    )
    if plan["work_due"]:
        print("REFILL DUE")
        return 10
    print("Board is stocked and every live row has a script body.")
    return 0


def cmd_check_hook(args):
    rows = load_board(args.board)
    live = [r for r in rows if r["status"] in LIVE_STATUSES]
    worst = (0.0, None)
    for row in live:
        score = similarity(args.hook, row["hook"])
        if score > worst[0]:
            worst = (score, row["hook"])
    if worst[0] >= DUPE_THRESHOLD:
        print(f"DUPE {worst[0]:.2f} vs: {worst[1]}")
        return 11
    print(f"NOVEL (closest {worst[0]:.2f})")
    return 0


def cmd_footer(args):
    stamp = today()
    line = f"{FOOTER_PREFIX} {args.ref} | lane: {args.lane} | added: {stamp.isoformat()}"
    if args.lane in PERISHABLE:
        expires = stamp + timedelta(days=PERISHABLE[args.lane])
        line += f" | expires: {expires.isoformat()}"
    print(line)
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    for name, fn in (("plan", cmd_plan), ("health", cmd_health)):
        p = sub.add_parser(name)
        p.add_argument("--board", required=True)
        p.set_defaults(fn=fn)

    p = sub.add_parser("check-hook")
    p.add_argument("--board", required=True)
    p.add_argument("--hook", required=True)
    p.set_defaults(fn=cmd_check_hook)

    p = sub.add_parser("footer")
    p.add_argument("--lane", required=True)
    p.add_argument("--ref", required=True)
    p.set_defaults(fn=cmd_footer)

    args = parser.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
