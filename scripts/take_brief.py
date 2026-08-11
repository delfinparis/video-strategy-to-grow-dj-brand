#!/usr/bin/env python3
"""
Weekly take brief generator for The Take (docs/series/take-standard.md).

Reads the sacred-cows bank, drops anything used inside the 8-week rotation
window, balances what's left across sections and the three weekly slots, and
writes 5-7 numbered options to data/take-briefs/YYYY-MM-DD.md.

This script is deliberately DETERMINISTIC AND OFFLINE. It does the half a model
should not be trusted with -- counting the 8-week rotation window, spreading
candidates across sections, flagging which entries still have no verified number
-- and writes a brief skeleton with a blank Hook / Swap / Loop-back on each
option.

The judgment half is the Sunday cloud routine's job, and it lives there for one
concrete reason: 19 of the 42 bank entries are marked `Evidence: research`,
meaning the belief is real but no number has been sourced yet. Sourcing those
needs web search. An API call from this script would not have it, so it would
produce confident hooks resting on numbers nobody checked. The routine has web
search, so it fills the hooks in and clears the VERIFY blocks.

Nothing in this chain may invent a figure. A take whose receipt turns out to be
wrong does more damage than the reach was worth (take-standard.md, "Source
rigor"). An option whose number cannot be sourced gets dropped, not softened.

Usage:
  python3 scripts/take_brief.py
  # 6 options for the upcoming week -> data/take-briefs/YYYY-MM-DD.md

  python3 scripts/take_brief.py --count 7
  # 5-7 allowed; it is a shortlist, not a catalog

  python3 scripts/take_brief.py --verified-only
  # only candidates whose evidence already exists in-repo, so nothing in the
  # brief needs sourcing. Useful on a week with no research time.

  python3 scripts/take_brief.py --stdout
  # print instead of writing

Dependencies: none (standard library only).
"""

import argparse
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
BANK = REPO_ROOT / "data" / "sacred-cows.md"
OUT_DIR = REPO_ROOT / "data" / "take-briefs"

ROTATION_WEEKS = 8
REFILL_THRESHOLD = 24          # bank doc's own refill trigger

# Slot -> (heat, allowed hook families). Mirrors the table in take-standard.md.
SLOTS = {
    "Mon": ("3.5", "9 (Swap / List)"),
    "Wed": ("4", "2 (Sacred Cow) or 4 (System Indictment)"),
    "Fri": ("3-3.5", "5 (Confession), 7 (Forbidden), or 8 (Cohort Callout)"),
}

# Sections whose turn indicts an incentive or a system read naturally as the
# Wednesday heat-4 slot. Advisory only -- stage 2 can move a candidate, and the
# brief prints the reasoning either way.
WED_LEANING = {"Brokerage economics", "Career and identity"}


# ---------------------------------------------------------------------------
# Bank parsing
# ---------------------------------------------------------------------------
def normalize(belief):
    """Rotation rows and bank headings quote the same belief with drifting
    punctuation. Compare on a flattened form so a stray period never lets a
    used entry back into rotation."""
    s = belief.strip().strip('"').strip().lower()
    s = re.sub(r"[^a-z0-9 ]+", "", s)
    return re.sub(r"\s+", " ", s).strip()


def parse_bank(text):
    """Returns (entries, sections_in_order).

    An entry is a `**"belief."**` heading plus the prose beneath it, under the
    most recent `### Section`.
    """
    entries = []
    sections = []
    section = None
    lines = text.splitlines()
    i = 0
    # Only parse inside the "## Bank" region; the qualifying test and the
    # rotation notes above it contain bold text that would otherwise match.
    start = 0
    for n, ln in enumerate(lines):
        if ln.strip() == "## Bank":
            start = n
            break
    for ln in lines[start:]:
        i += 1
        if ln.startswith("### "):
            section = ln[4:].strip()
            if section not in sections:
                sections.append(section)
            continue
        m = re.match(r'^\*\*"(.+)"\*\*\s*$', ln.strip())
        if m and section:
            entries.append({
                "belief": m.group(1).strip(),
                "section": section,
                "body_lines": [],
                "_line": i,
            })
            continue
        if ln.startswith("## ") and not ln.startswith("### "):
            section = None
            continue
        # A horizontal rule closes the Bank section. Without this the trailing
        # "---" lands in the last entry's body and shows up as evidence text.
        if re.match(r"^-{3,}\s*$", ln.strip()):
            section = None
            continue
        if entries and section and ln.strip():
            entries[-1]["body_lines"].append(ln.strip())

    for e in entries:
        body = " ".join(e.pop("body_lines"))
        e["body"] = re.sub(r"\s+", " ", body).strip()
        e["profits"] = _field(body, "Profits:", ("Turn:", "Evidence:"))
        e["turn"] = _field(body, "Turn:", ("Evidence:",))
        e["evidence"] = _field(body, "Evidence:", ("Heat check:", "**Heat check:**", "Flag:"))
        low = body.lower()
        e["verified"] = "evidence: in-repo" in low
        e["needs_research"] = "evidence: research" in low
        e["heat_check"] = "heat check" in low
        e["flagged"] = "flag:" in low
        e["key"] = normalize(e["belief"])
    return entries, sections


def _field(body, label, stops):
    """Pull `Label: ... ` out of the run-on prose, ending at the next label."""
    idx = body.find(label)
    if idx < 0:
        return ""
    rest = body[idx + len(label):]
    cut = len(rest)
    for s in stops:
        j = rest.find(s)
        if 0 <= j < cut:
            cut = j
    return re.sub(r"\s+", " ", rest[:cut]).strip(" .,")


def parse_rotation(text):
    """Returns [{date, key, raw}] from the rotation table at the bottom."""
    rows = []
    tail = text.split("## Rotation", 1)
    if len(tail) < 2:
        return rows
    for ln in tail[1].splitlines():
        ln = ln.strip()
        if not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if len(cells) < 2:
            continue
        m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", cells[0])
        if not m:
            continue                      # header and separator rows
        entry = cells[1]
        qm = re.search(r'"(.+?)"', entry)
        belief = qm.group(1) if qm else re.sub(r"\(.*?\)", "", entry)
        rows.append({
            "date": datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)),
                             tzinfo=timezone.utc),
            "key": normalize(belief),
            "raw": entry,
        })
    return rows


# ---------------------------------------------------------------------------
# Eligibility + selection
# ---------------------------------------------------------------------------
def select(entries, rotation, now, count, verified_only):
    """Deterministic. Returns (chosen, report)."""
    cutoff = now - timedelta(weeks=ROTATION_WEEKS)
    used = {}
    for r in rotation:
        if r["date"] >= cutoff:
            used[r["key"]] = max(used.get(r["key"], r["date"]), r["date"])

    pool, blocked = [], []
    for e in entries:
        if e["key"] in used:
            e["blocked_until"] = used[e["key"]] + timedelta(weeks=ROTATION_WEEKS)
            blocked.append(e)
            continue
        if verified_only and not e["verified"]:
            continue
        pool.append(e)

    # Most-recent section first, so we can spread away from it.
    recent_sections = []
    for r in sorted(rotation, key=lambda x: x["date"], reverse=True):
        for e in entries:
            if e["key"] == r["key"] and e["section"] not in recent_sections:
                recent_sections.append(e["section"])

    def rank(e):
        return (
            0 if e["verified"] else 1,               # ship-ready first
            recent_sections.index(e["section"]) * -1 # away from what just ran
            if e["section"] in recent_sections else -99,
            0 if not e["flagged"] else 1,            # flagged entries last
            e["_line"],                              # stable tiebreak
        )

    ranked = sorted(pool, key=rank)

    # Round-robin across sections so one section can't fill the whole brief.
    by_section = {}
    for e in ranked:
        by_section.setdefault(e["section"], []).append(e)
    order = sorted(by_section, key=lambda s: (
        recent_sections.index(s) * -1 if s in recent_sections else -99,
        s,
    ))
    chosen = []
    while len(chosen) < count and any(by_section.values()):
        for s in order:
            if not by_section.get(s):
                continue
            chosen.append(by_section[s].pop(0))
            if len(chosen) >= count:
                break

    for e in chosen:
        e["slot_hint"] = "Wed" if e["section"] in WED_LEANING else "Mon/Fri"

    return chosen, {
        "total": len(entries),
        "blocked": blocked,
        "eligible": len(pool),
        "verified_eligible": sum(1 for e in pool if e["verified"]),
        "research_eligible": sum(1 for e in pool if e["needs_research"]),
    }


# ---------------------------------------------------------------------------
# Brief
# ---------------------------------------------------------------------------
def format_brief(chosen, report, now, week_of):
    """Writes the SKELETON. Hook / Who profits / Swap / Loop-back are left blank
    on purpose: the Sunday routine fills them in after it has sourced the
    numbers. A skeleton that arrives unfilled is obvious at a glance, which is
    the point -- a half-run routine should look broken, not look finished."""
    L = []
    L.append(f"# Take Options, week of {week_of:%a %b %-d, %Y}")
    L.append("")
    L.append(f"> Generated {now:%Y-%m-%d} by `scripts/take_brief.py`. "
             "Pick 3: one Mon, one Wed (the heat-4 slot), one Fri.")
    L.append("> Build with `takes <n>` in Claude Code. "
             "Standard: `docs/series/take-standard.md`.")
    L.append("")

    needs = [e for e in chosen if not e["verified"]]
    if needs:
        L.append(f"**{len(needs)} of {len(chosen)} options need a number sourced before they "
                 "can ship.** Marked NEEDS RECEIPT below. A take without a receipt does not "
                 "run, and the number is never estimated to fill the gap.")
        L.append("")

    L.append("---")
    L.append("")

    for i, e in enumerate(chosen, 1):
        L.append(f"## {i}. {e['belief']}")
        L.append("")
        L.append(f"**Section:** {e['section']} | **Slot hint:** {e['slot_hint']} | "
                 f"**Receipt:** {'in-repo' if e['verified'] else '**NEEDS RECEIPT**'}")
        L.append("")
        L.append(f"**Who profits (from the bank):** {e['profits']}")
        L.append("")
        L.append(f"**The turn (from the bank):** {e['turn']}")
        L.append("")
        L.append(f"**Evidence note:** {e['evidence']}")
        L.append("")
        L.append("**Hook (spoken):** _[routine fills in]_")
        L.append("")
        L.append("**The swap:** _[routine fills in]_")
        L.append("")
        L.append("**Loop-back:** _[routine fills in]_")
        L.append("")
        if not e["verified"]:
            L.append("> **NEEDS RECEIPT.** No sourced number exists for this entry yet. "
                     "Source it with a named publisher and year, or drop the option. "
                     "Do not write a hook that implies a figure you have not verified.")
            L.append("")
        if e["heat_check"]:
            L.append("> **Heat check on this entry in the bank.** Read the bank note before "
                     "drafting; it sits near a line the lane does not cross.")
            L.append("")
        if e["flagged"]:
            L.append("> **Flagged in the bank.** It carries a do-not-ship-unless condition. "
                     "Check it before this option is offered at all.")
            L.append("")
        L.append("---")
        L.append("")

    L.append("## Slots this brief has to fill")
    L.append("")
    L.append("| Day | Heat | Hook family |")
    L.append("|---|---|---|")
    for day, (heat, fam) in SLOTS.items():
        L.append(f"| {day} | {heat} | {fam} |")
    L.append("")
    L.append("Exactly one Wednesday pick. That slot is the whole week's only heat-4 post "
             "under Rule 9.2, not just this series'.")
    L.append("")

    L.append("## Bank health")
    L.append("")
    L.append(f"- **{report['eligible']} of {report['total']} entries eligible** "
             f"({ROTATION_WEEKS}-week rotation applied).")
    L.append(f"- {report['verified_eligible']} have in-repo evidence, "
             f"{report['research_eligible']} still need a number sourced.")
    if report["blocked"]:
        L.append(f"- {len(report['blocked'])} blocked by rotation:")
        for e in sorted(report["blocked"], key=lambda x: x["blocked_until"]):
            L.append(f"  - \"{e['belief']}\" free again {e['blocked_until']:%b %-d}")
    if report["eligible"] < REFILL_THRESHOLD:
        L.append("")
        L.append(f"> **Refill the bank.** Under {REFILL_THRESHOLD} eligible entries is the "
                 "threshold in `data/sacred-cows.md`. Below this the rotation starts forcing "
                 "repeats.")
    L.append("")
    L.append("## After you pick")
    L.append("")
    L.append("1. Say `takes 2` (or several numbers) in Claude Code.")
    L.append("2. Claude re-verifies the receipt before drafting. If the number cannot be "
             "sourced, the option is dropped, not softened.")
    L.append("3. Log the chosen entries in the rotation table in `data/sacred-cows.md` so "
             "the carousel routine does not re-pick them.")
    L.append("")
    return "\n".join(L)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--count", type=int, default=6, help="How many options (5-7, default 6)")
    p.add_argument("--verified-only", action="store_true",
                   help="Only candidates whose evidence already exists in-repo")
    p.add_argument("--out", default=None, help="Override output path")
    p.add_argument("--stdout", action="store_true", help="Print instead of writing")
    args = p.parse_args()

    if not 5 <= args.count <= 7:
        print("error: --count must be 5-7 (the brief is a shortlist, not a catalog).",
              file=sys.stderr)
        return 2
    if not BANK.exists():
        print(f"error: bank not found at {BANK}", file=sys.stderr)
        return 1

    text = BANK.read_text()
    entries, _ = parse_bank(text)
    rotation = parse_rotation(text)
    if not entries:
        print("error: parsed 0 entries from the bank. Has its format changed?", file=sys.stderr)
        return 1

    now = datetime.now(timezone.utc)
    # The brief is for the week starting the next Monday.
    week_of = now + timedelta(days=(7 - now.weekday()) % 7 or 7)

    chosen, report = select(entries, rotation, now, args.count, args.verified_only)
    if not chosen:
        print("error: no eligible entries. The rotation window has blocked everything; "
              "refill data/sacred-cows.md.", file=sys.stderr)
        return 1
    if len(chosen) < args.count:
        print(f"warning: only {len(chosen)} eligible entries, asked for {args.count}.",
              file=sys.stderr)

    brief = format_brief(chosen, report, now, week_of)

    if args.stdout:
        print(brief)
        return 0
    out = Path(args.out) if args.out else OUT_DIR / f"{now:%Y-%m-%d}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(brief)
    print(f"Wrote {out} ({len(chosen)} options, "
          f"{report['eligible']}/{report['total']} eligible, "
          f"{sum(1 for e in chosen if not e['verified'])} needing a receipt)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
