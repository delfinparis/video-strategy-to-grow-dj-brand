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

  python3 scripts/content_board.py mirror --board board.json
      The two lanes that are NOT researched here. Agent Spotlight and KIRP
      Episode already have their own producing routines, which commit finished
      scripts to the repo. This lists the committed scripts that are not on the
      board yet, parsed and ready to post, newest first.

  python3 scripts/content_board.py cache-known
      Rows already known to have a body, so the routine can skip fetching those
      pages. Returns nothing at all once the cache is a week old, forcing a full
      re-read. Pair with cache-update after the run.

  python3 scripts/content_board.py body-markers
      The headings that count as "this page has a script". Series differ:
      podcast promos head it `## Spoken Script`, spotlights `## Full Script`.

board.json is the snapshot the routine exports from Notion before planning:
  [{"url": "...", "lane": "News", "status": "Open", "hook": "...",
    "expires": "2026-08-22", "has_body": false, "ref": "news-briefs/..."}, ...]

`ref` is the bank pointer read back out of the page footer, or null. It is how
the mirror lanes know a committed script is already on the board.

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

# Whether a page has a script body can only be learned by fetching the page,
# and a filled page never empties itself. Remembering the answer turns roughly
# thirty full-script page fetches per run into zero, and it is also a record of
# the board that lives somewhere other than Notion.
STATE_PATH = os.path.join(DATA, "content-board-state.json")

# How long the cache is trusted before the routine re-reads every page anyway.
# The cache can only go wrong one way -- a body deleted by hand in Notion still
# reads as filled -- and a weekly full check is what catches that.
STATE_MAX_AGE_DAYS = 7

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
    # Mirror lanes: never researched here, only mirrored. See `mirror`.
    "Agent Spotlight": ["MIRROR scripts/chicago-agent-spotlight/"],
    "KIRP Episode": ["MIRROR scripts/podcast-promos/kir-*.md"],
}

# Lanes whose rows rot. Everything else waits on the shelf indefinitely.
PERISHABLE = {"News": 3, "Agent Tip": 7}

# A row is LIVE for the purposes of killing it and filling its body -- a Picked
# row still needs a script. It is only AVAILABLE if D.J. can still choose it.
# Counting Picked as inventory means a lane where he has claimed everything
# reads as full and never refills, leaving him nothing to pick from.
LIVE_STATUSES = {"Open", "Picked"}
AVAILABLE_STATUSES = {"Open"}
FOOTER_PREFIX = "Bank ref:"

# A page counts as having a script if it carries any of these. The series do not
# agree on one heading and never have: podcast promos head it `## Spoken Script`,
# Chicago spotlights `## Full Script (Spoken)`, board-native rows `## Script`.
# Checking only for `## Script` would mark every mirrored row empty and rewrite a
# perfectly good script on top of itself.
SCRIPT_HEADINGS = ("## Script", "## Spoken Script", "## Full Script")

# The two lanes this board does NOT research. Both already have a producing
# routine that commits a finished walk-and-talk to the repo, so the board mirrors
# the committed file instead of scouting the same guest or agent a second time.
# The repo path is the dedupe key, which is stronger than hook text: an episode
# already Posted can never come back as a new row.
MIRROR_LANES = {
    "KIRP Episode": {
        "dir": "scripts/podcast-promos",
        "pattern": r"^kir-.+\.md$",
        "heat": 2,
        "producer": "trig_01S1nWLHuJ3jYLg7BzyC9Kaf (Daily KIR episode -> walk-and-talk promo)",
    },
    "Agent Spotlight": {
        "dir": "scripts/chicago-agent-spotlight",
        "pattern": r"^(?!README).+\.md$",
        "heat": 2,
        "producer": "trig_01Fr5tCSZnfhxSXtSPEcCVhe (Weekly Chicago Agent Spotlight)",
    },
}

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
    """Content words only, so 'Your cap you never hit' collides with 'The cap you have never once hit'.

    Apostrophes are closed up rather than split on, because splitting turns
    "you're" into the tokens "re" and "don't" into "don" + "t", and those
    fragments then read as shared content between two unrelated hooks.
    """
    text = (text or "").lower().replace("'", "").replace("\u2019", "")
    words = re.findall(r"[a-z0-9]+", text)
    return [w for w in words if w not in STOPWORDS]


def similarity(a, b):
    """Jaccard over content words. Cheap, offline, and good enough to catch a reword."""
    sa, sb = set(normalize(a)), set(normalize(b))
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


# Jaccard cannot separate every case, and the two error directions are not
# equally bad. A false DUPE costs one candidate the routine can simply replace.
# A false NOVEL puts a repeat in front of D.J. and makes the board look broken.
# So this stays deliberately aggressive, and the near band exists to make the
# borderline calls visible in the run log instead of silently dropped.
#
# Known false positive: "Your BUYERS are about to ask if rates drop" scores
# 0.71 against "Your SELLERS are about to ask if rates drop". Same shape, real
# difference, and word overlap cannot see it. Rejecting is the safer miss.
DUPE_THRESHOLD = 0.6
NEAR_THRESHOLD = 0.45


def load_board(path):
    with open(path) as fh:
        rows = json.load(fh)
    if not isinstance(rows, list):
        sys.exit("board.json must be a list of row objects")
    for i, row in enumerate(rows):
        if not isinstance(row, dict) or not row.get("url"):
            sys.exit(f"board.json row {i} has no url -- the snapshot is broken, "
                     f"not the board. Re-export it before planning.")
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
        if row["lane"] in counts and row["status"] in AVAILABLE_STATUSES:
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
    # Deliberately every status, not just the live ones. A hook D.J. already
    # Posted coming back as a fresh row is the most embarrassing failure this
    # board can have, and it is the one a live-only scan would allow.
    rows = load_board(args.board)
    worst = (0.0, None, None)
    for row in rows:
        score = similarity(args.hook, row["hook"])
        if score > worst[0]:
            worst = (score, row["hook"], row["status"])
    if worst[0] >= DUPE_THRESHOLD:
        print(f"DUPE {worst[0]:.2f} vs [{worst[2]}]: {worst[1]}")
        return 11
    if worst[0] >= NEAR_THRESHOLD:
        print(f"NEAR {worst[0]:.2f} vs [{worst[2]}]: {worst[1]}")
        return 0
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



def split_sentences(text):
    return [t.strip() for t in re.split(r"(?<=[.!?])\s+", text.strip()) if t.strip()]


def parse_script_file(path, lane, heat):
    """Pull the board row out of a finished script file.

    The hook is the first thing D.J. actually says, which is not in the
    frontmatter and not the H1 -- it is the first prose line under the script
    heading, past any `**HOOK (0:00-0:08)**` beat label.
    """
    with open(path) as fh:
        body = fh.read()

    lines = body.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.startswith(SCRIPT_HEADINGS):
            start = i + 1
            break
    if start is None:
        return None  # not a script file (a registry, a README, a brief)

    spoken = ""
    for line in lines[start:]:
        stripped = line.strip()
        if not stripped or stripped.startswith(("#", ">", "*Production", "|")):
            continue
        if re.fullmatch(r"\*\*[A-Z][A-Za-z ]*\(?[0-9:\-\. ]*\)?\*\*", stripped):
            continue  # a beat label, not a spoken line
        if stripped.startswith("---"):
            break
        spoken = stripped
        break
    if not spoken:
        return None

    sentences = split_sentences(spoken)
    hook = sentences[0] if sentences else spoken
    if len(hook) < 60 and len(sentences) > 1:
        hook = f"{hook} {sentences[1]}"

    # The WOW note is the one-line reason this script exists, which is exactly
    # what the Angle column wants. Take the WHOLE blockquote, not the bolded
    # head of it -- spotlights bold only a two-word label ("Person + lesson.")
    # and put the substance after the closing asterisks.
    angle = ""
    for i, line in enumerate(lines):
        if re.match(r"^>\s*\*\*WOW", line):
            quote = []
            for follow in lines[i:]:
                if not follow.startswith(">"):
                    break
                quote.append(follow.lstrip("> ").strip())
            text = " ".join(quote)
            text = text.replace("**", "")
            text = re.sub(r"^WOW:?\s*", "", text)
            angle = " ".join(split_sentences(text)[:2])
            break
    if not angle:
        title = re.search(r'^title:\s*"(.+?)"', body, re.M)
        angle = title.group(1) if title else hook

    return {
        "ref": os.path.relpath(path, BASE_DIR),
        "lane": lane,
        "hook": re.sub(r"\s+", " ", hook).strip(),
        "angle": re.sub(r"\s+", " ", angle).strip()[:400],
        "heat": heat,
        "body_path": os.path.relpath(path, BASE_DIR),
    }


def cmd_mirror(args):
    rows = load_board(args.board)
    # Every ref ever seen, at ANY status. A Posted episode must not come back.
    #
    # Matched on BASENAME, not the whole path. The ref is read back out of a
    # page footer written by a model, and one that says "podcast-promos/x.md"
    # instead of "scripts/podcast-promos/x.md" is not a new episode -- but exact
    # path matching would call it one and post a duplicate. The basenames carry
    # their own date and are unique.
    claimed = {os.path.basename(r["ref"]) for r in rows if r.get("ref")}
    live_counts = {}
    for row in rows:
        if row["status"] in LIVE_STATUSES:
            live_counts[row["lane"]] = live_counts.get(row["lane"], 0) + 1

    out = {}
    for lane, cfg in MIRROR_LANES.items():
        directory = os.path.join(BASE_DIR, cfg["dir"])
        candidates = []
        if os.path.isdir(directory):
            # Names are `<guest-or-agent>-<YYYY-MM-DD>.md`, so a plain reverse
            # sort orders by guest name and buries the newest episode. Sort on
            # the date the filename actually carries.
            def file_date(name):
                found = re.search(r"(\d{4}-\d{2}-\d{2})", name)
                return found.group(1) if found else "0000-00-00"

            names = sorted(os.listdir(directory), key=file_date, reverse=True)
            for name in names:
                if not re.match(cfg["pattern"], name):
                    continue
                if name in claimed:
                    continue
                parsed = parse_script_file(os.path.join(directory, name), lane, cfg["heat"])
                if parsed:
                    candidates.append(parsed)
        room = max(0, TARGETS[lane] - live_counts.get(lane, 0))
        out[lane] = {
            "producer": cfg["producer"],
            "on_board": live_counts.get(lane, 0),
            "target": TARGETS[lane],
            "room": room,
            "available": len(candidates),
            "post": candidates[:room],
            "held_back": max(0, len(candidates) - room),
        }
    print(json.dumps(out, indent=2))
    return 0


def cmd_body_markers(args):
    for heading in SCRIPT_HEADINGS:
        print(heading)
    return 0



def load_state():
    if not os.path.exists(STATE_PATH):
        return {"updated": None, "rows": {}}
    try:
        with open(STATE_PATH) as fh:
            state = json.load(fh)
    except (json.JSONDecodeError, OSError):
        return {"updated": None, "rows": {}}   # a corrupt cache is a slow run, not a wrong one
    state.setdefault("rows", {})
    return state


def state_is_fresh(state):
    if not state.get("updated"):
        return False
    try:
        age = (today() - date.fromisoformat(state["updated"])).days
    except ValueError:
        return False
    return 0 <= age < STATE_MAX_AGE_DAYS


def cmd_cache_known(args):
    """The rows whose page body the routine can skip fetching."""
    state = load_state()
    if not state_is_fresh(state):
        # Deliberately hand back nothing rather than a stale yes. A full re-read
        # is a slower run; a wrong yes is a blank row D.J. opens on set.
        print(json.dumps({"fresh": False, "reason": "cache stale or missing", "known": {}}, indent=2))
        return 0
    known = {
        url: {"ref": row.get("ref")}
        for url, row in state["rows"].items()
        if row.get("has_body")
    }
    print(json.dumps({"fresh": True, "updated": state["updated"], "known": known}, indent=2))
    return 0


def cmd_cache_update(args):
    """Fold the post-run board snapshot back into the cache."""
    rows = load_board(args.board)
    state = load_state()
    for row in rows:
        # Only ever remember a body that exists. Never cache a false, or a run
        # that failed halfway would teach the cache the row is permanently empty.
        if row.get("has_body"):
            state["rows"][row["url"]] = {
                "has_body": True,
                "ref": row.get("ref"),
                "lane": row.get("lane"),
            }
    state["updated"] = today().isoformat()
    os.makedirs(DATA, exist_ok=True)
    with open(STATE_PATH, "w") as fh:
        json.dump(state, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print(f"Cached {len(state['rows'])} filled rows -> {os.path.relpath(STATE_PATH, BASE_DIR)}")
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

    p = sub.add_parser("mirror")
    p.add_argument("--board", required=True)
    p.set_defaults(fn=cmd_mirror)

    p = sub.add_parser("cache-known")
    p.set_defaults(fn=cmd_cache_known)

    p = sub.add_parser("cache-update")
    p.add_argument("--board", required=True)
    p.set_defaults(fn=cmd_cache_update)

    p = sub.add_parser("body-markers")
    p.set_defaults(fn=cmd_body_markers)

    p = sub.add_parser("footer")
    p.add_argument("--lane", required=True)
    p.add_argument("--ref", required=True)
    p.set_defaults(fn=cmd_footer)

    args = parser.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
