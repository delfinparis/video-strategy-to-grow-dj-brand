#!/usr/bin/env python3
"""
Weekly planner for the Broker Problems lane (docs/series/broker-problems-standard.md).

Three scripts a week since 2026-09-08 (Tue / Thu / Fri). This script reads the
bank (data/brokerage-pain.md) and its rotation table, drops anything used inside
the 8-week window, applies the lane's rotation rules, and writes a brief with one
primary entry and two alternates per slot to data/broker-problem-briefs/.

It is DETERMINISTIC AND OFFLINE, on purpose, and it owns exactly the half a model
should not be trusted with:

  - the 8-week no-repeat on entries (dated rotation rows only; a script that was
    written and never aired does not spend the entry)
  - no flavor twice in a week, and never the same flavor as the last aired post
  - the weekly brand-tax minimum (2 of 3, D.J.'s 2026-09-08 direction)
  - the Silence quota (at least 2 in any trailing 28 days) and the Permission
    Slip cadence (about monthly), and which one yields when they collide
  - the rung mix (rung 2 at least half of the trailing four weeks, rung 3 at
    most one in four)
  - refusing entries the bank marks parked, blocked, or sign-off-required
  - never letting an unverified receipt read as a verified one

The judgment half -- writing the hook, re-verifying the receipt, running the
four passes and the council -- belongs to the Sunday routine and to the
on-demand build in Claude Code. See docs/automation/broker-problems-engine.md.

Nothing in this chain may invent a figure. An entry marked `Receipt: NEEDED`
ships only in a shape that needs no number, and the brief says so on the option.

Usage:
  python3 scripts/broker_problems.py plan
      Write this week's brief (three slots, alternates, audit lines).
  python3 scripts/broker_problems.py plan --week 2026-09-14 --stdout
  python3 scripts/broker_problems.py pick --count 6 --stdout
      A flat shortlist for when D.J. says "broker problems" off-cycle.
  python3 scripts/broker_problems.py log --entry F1 --script scripts/broker-problems/BP-006-x.md \
      --date 2026-09-08 [--rung 2] [--surface video]
      Append a rotation row. Flavor and rung default to the bank entry's.
  python3 scripts/broker_problems.py health
      Bank status. EXIT CODE 10 means a refill is due.

Dependencies: none (standard library only).
"""

import argparse
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
BANK = REPO_ROOT / "data" / "brokerage-pain.md"
OUT_DIR = REPO_ROOT / "data" / "broker-problem-briefs"

ROTATION_WEEKS = 8
SLOTS = ["Tue", "Thu", "Fri"]
SLOT_OFFSET = {"Tue": 1, "Thu": 3, "Fri": 4}      # days after the week's Monday
BRAND_TAX_MIN_PER_WEEK = 2                        # D.J., 2026-09-08
SILENCE_MIN_PER_28_DAYS = 2                       # standard: "at least twice a month"
PERMISSION_SLIP_EVERY_DAYS = 28                   # standard: "about monthly"
PERMISSION_SLIP_AFTER_AIRED = 3                   # strategy: only once the lane has named problems without selling
RUNG2_MIN_SHARE = 0.5                             # trailing four weeks
RUNG3_MAX_SHARE = 0.25
REFILL_THRESHOLD = 6                              # available entries; below this, exit 10
EXIT_REFILL_DUE = 10

# Flavor letter -> (display name, default heat, suggested hook families)
# Heat floor is 4 everywhere since 2026-08-20 (Rule 9.2). The Silence and the
# Permission Slip used to run at 3; they now have to name the wrong default in
# the hook to earn 4. The brief says so on those options.
FLAVORS = {
    "A": ("The Slow Leak", 4.0, "6 (Named Stakes) or 4 (System Indictment)"),
    "B": ("The Thing That Doesn't Make Sense", 4.0, "4 (System Indictment) or 7 (Forbidden)"),
    "C": ("The Silence", 4.0, "1 (Mirror) or 5 (Confession), with the wrong default named in the hook"),
    "D": ("The Permission Slip", 4.0, "5 (Confession) or 3 (Defector), with the wrong default named in the hook"),
    "E": ("Run The Math With Me", 4.0, "3 (Defector) or 6 (Named Stakes)"),
    "F": ("The Brand Tax", 4.5, "4 (System Indictment), 7 (Forbidden) or 6 (Named Stakes)"),
}

# Hook family -> the selfie-stick move that pairs with it (pattern-interrupt-cheatsheet.md)
PATTERN_FOR_FAMILY = {
    "1": "4 (Walk-Toward)", "2": "1 (The Stop)", "3": "6 (Location Cold-Open) or 2 (Push-In)",
    "4": "1 (The Stop)", "5": "2 (Push-In)", "6": "5 (One Prop)", "7": "3 (The Whip) or 7 (Gesture-On-Beat)",
    "8": "4 (Walk-Toward)", "9": "5 (One Prop) or 7 (Gesture-On-Beat)",
}

UNAVAILABLE_STATUS = re.compile(r"parked|blocked|sign-off required", re.I)


# ---------------------------------------------------------------------------
# Bank parsing
# ---------------------------------------------------------------------------
def parse_bank(text):
    """Returns (entries, rotation_rows).

    An entry is a `### ID. Title` heading under the most recent `## Flavor X:`
    heading, plus the bold fields beneath it. IDs like `E1 / A6` keep the first
    code as the canonical one and the second as an alias.
    """
    entries, flavor = [], None
    current = None
    for raw in text.splitlines():
        line = raw.rstrip()
        m = re.match(r"^## Flavor ([A-Z]): (.+?)(?: \(.*\))?$", line)
        if m:
            flavor = m.group(1)
            current = None
            continue
        if line.startswith("## "):
            flavor = None
            current = None
            continue
        m = re.match(r"^### ([A-Z]\d+)(?: / ([A-Z]\d+))?\. (.+)$", line)
        if m and flavor:
            current = {
                "id": m.group(1), "alias": m.group(2), "title": m.group(3).strip(),
                "flavor": flavor, "register": "", "receipt": "", "rung": [], "status": "",
                "body": [],
            }
            entries.append(current)
            continue
        if current is None:
            continue
        current["body"].append(line)
        m = re.match(r"^\*\*Register:\*\*\s*(.+?)\.?\s*$", line)
        if m:
            current["register"] = m.group(1).strip().lower()
        m = re.match(r"^\*\*Receipt:\s*(.+?)\*\*", line)
        if m:
            current["receipt"] = m.group(1).strip().rstrip(".")
        m = re.match(r"^\*\*Rung:\*\*\s*(.+)$", line)
        if m:
            current["rung"] = [int(d) for d in re.findall(r"\b([123])\b", m.group(1))] or []
        m = re.match(r"^\*\*Status:\*\*\s*(.+)$", line)
        if m:
            current["status"] = m.group(1).strip()

    rows = []
    in_table = False
    for line in text.splitlines():
        if line.startswith("## Rotation table"):
            in_table = True
            continue
        if in_table and line.startswith("## "):
            break
        if in_table and line.startswith("|") and not line.startswith("|---") and "Date" not in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 6:
                continue
            d = None
            try:
                d = datetime.strptime(cells[0], "%Y-%m-%d").date()
            except ValueError:
                pass
            codes = re.findall(r"\b([A-Z]\d+)\b", cells[1])
            rows.append({
                "date": d, "codes": codes, "flavor": cells[2], "rung": cells[3],
                "script": cells[4], "surface": cells[5],
            })
    return entries, rows


def receipt_kind(entry):
    r = entry["receipt"].lower()
    if r.startswith("needed"):
        return "NEEDED"
    if r.startswith("not needed"):
        return "not needed"
    if "unusable" in r:
        return "verified quote, name-stripped only"
    if r.startswith("verified") or r.startswith("first-party"):
        return "verified"
    return entry["receipt"] or "unstated"


def entry_codes(entry):
    return {entry["id"]} | ({entry["alias"]} if entry["alias"] else set())


def flavor_of_row(row, entries):
    """Rotation rows spell the flavor loosely. Resolve through the entry code."""
    for e in entries:
        if entry_codes(e) & set(row["codes"]):
            return e["flavor"]
    f = row["flavor"].lower()
    for letter, (name, _, _) in FLAVORS.items():
        if name.lower().split()[-1] in f or name.lower() in f:
            return letter
    if "silence" in f:
        return "C"
    if "permission" in f:
        return "D"
    if "math" in f:
        return "E"
    if "brand" in f:
        return "F"
    return None


# ---------------------------------------------------------------------------
# Planning
# ---------------------------------------------------------------------------
def week_monday(today, override):
    if override:
        d = datetime.strptime(override, "%Y-%m-%d").date()
        return d - timedelta(days=d.weekday())
    if today.weekday() >= 5:                      # Sat/Sun: plan the coming week
        return today + timedelta(days=7 - today.weekday())
    return today - timedelta(days=today.weekday())


def aired_rows(rows):
    return [r for r in rows if r["date"] and r["surface"].lower().startswith("video")]


def availability(entries, rows, monday):
    """Which entries may run this week, and why the rest may not."""
    window_start = monday - timedelta(weeks=ROTATION_WEEKS)
    used = {}
    drafted = {}
    for r in rows:
        for c in r["codes"]:
            if r["date"] and r["date"] >= window_start:
                used[c] = r
            elif not r["date"] and r["script"]:
                drafted[c] = r["script"]
    avail, dropped = [], []
    for e in entries:
        codes = entry_codes(e)
        hit = [used[c] for c in codes if c in used]
        if hit:
            dropped.append((e, f"used {hit[0]['date']} in {hit[0]['script']}"))
            continue
        if UNAVAILABLE_STATUS.search(e["status"]):
            dropped.append((e, f"status: {e['status']}"))
            continue
        e["drafted"] = next((drafted[c] for c in codes if c in drafted), "")
        avail.append(e)
    return avail, dropped


def trailing(rows, entries, monday, days):
    start = monday - timedelta(days=days)
    out = []
    for r in aired_rows(rows):
        if start <= r["date"] < monday:
            out.append((r, flavor_of_row(r, entries)))
    return out


def preferred_rung(entry):
    return 2 if 2 in entry["rung"] else (entry["rung"][0] if entry["rung"] else 2)


def plan_week(entries, rows, monday):
    """Plan the three slots. Rows already logged for this week are honored as
    picks, not re-planned, so running `plan` after `log` shows the week as it
    actually is instead of overwriting the brief with a different set."""
    week_end = monday + timedelta(days=6)
    aired = aired_rows(rows)
    prior = [r for r in aired if r["date"] < monday]
    this_week = [r for r in aired if monday <= r["date"] <= week_end]
    # this week's rows must not count as "used" against themselves
    avail, dropped = availability(entries, [r for r in rows if r not in this_week], monday)
    last = prior
    last_flavor = flavor_of_row(last[-1], entries) if last else None

    recent28 = trailing(rows, entries, monday, 28)
    silence_recent = sum(1 for _, f in recent28 if f == "C")
    permission_recent = sum(1 for _, f in recent28 if f == "D")
    rungs_recent = [int(r["rung"]) for r, _ in recent28 if r["rung"].isdigit()]

    silence_due = silence_recent < SILENCE_MIN_PER_28_DAYS
    permission_due = permission_recent == 0 and len(last) >= PERMISSION_SLIP_AFTER_AIRED

    notes = []
    picks = []          # (slot, entry, reason)
    taken_flavors = set()
    taken_ids = set()
    logged_slots = set()
    for r in this_week:
        slot = next((s for s, off in SLOT_OFFSET.items() if monday + timedelta(days=off) == r["date"]), None)
        entry = next((e for e in entries if entry_codes(e) & set(r["codes"])), None)
        if slot and entry and slot not in logged_slots:
            picks.append((slot, entry, f"already logged: `{r['script']}`"))
            taken_ids.add(entry["id"])
            taken_flavors.add(entry["flavor"])
            logged_slots.add(slot)

    def take(slot, pool, reason):
        for e in pool:
            if e["id"] in taken_ids or e["flavor"] in taken_flavors:
                continue
            if not picks and last_flavor and e["flavor"] == last_flavor:
                continue
            picks.append((slot, e, reason))
            taken_ids.add(e["id"])
            taken_flavors.add(e["flavor"])
            return e
        return None

    def rung2_first(pool):
        # rung 2 first, then entries that need no sourcing, then bank order
        return sorted(pool, key=lambda e: (0 if 2 in e["rung"] else 1,
                                           1 if receipt_kind(e) == "NEEDED" else 0,
                                           0 if "recommended" in e["status"].lower() else 1,
                                           e["flavor"], e["id"]))

    brand = rung2_first([e for e in avail if e["register"] == "brand tax"])
    brand_F = [e for e in brand if e["flavor"] == "F"]
    silence = rung2_first([e for e in avail if e["flavor"] == "C"])
    permission = rung2_first([e for e in avail if e["flavor"] == "D"])
    rest = rung2_first([e for e in avail if e["register"] != "brand tax" and e["flavor"] not in ("C", "D")])

    def open_slot(slot):
        return slot not in logged_slots and not any(s == slot for s, _, _ in picks)

    # Tue: the direct one. Flavor F leads; if F is exhausted, any brand-tax entry.
    if open_slot("Tue"):
        if not take("Tue", brand_F + brand, "brand-tax lead (Flavor F first, D.J. 2026-09-08)"):
            notes.append("No brand-tax entry available for Tuesday. Refill Flavor F.")
            take("Tue", rest, "fallback: nothing brand-tax was available")

    # Thu: the Silence, when it is due. It converts, and it is the flavor a fee lane stops making.
    if open_slot("Thu"):
        if silence_due:
            s = take("Thu", [e for e in silence if e["register"] == "brand tax"] + silence,
                     f"Silence due ({silence_recent} in the trailing 28 days, minimum {SILENCE_MIN_PER_28_DAYS})")
            if not s:
                notes.append("Silence is due and no Silence entry is available. Refill Flavor C.")
        if open_slot("Thu"):
            take("Thu", brand, "second brand-tax entry (weekly minimum 2 of 3)")

    # Fri: whatever the week still owes, in this order.
    if open_slot("Fri"):
        brand_count = sum(1 for _, e, _ in picks if e["register"] == "brand tax")
        if brand_count < BRAND_TAX_MIN_PER_WEEK:
            if not take("Fri", brand, "second brand-tax entry (weekly minimum 2 of 3)"):
                notes.append("Could not reach 2 brand-tax entries this week without repeating a flavor.")
        if open_slot("Fri") and permission_due:
            take("Fri", permission, f"Permission Slip due (none in the trailing {PERMISSION_SLIP_EVERY_DAYS} days)")
        if open_slot("Fri"):
            take("Fri", brand + rest + silence + permission, "rotation: brand-tax register preferred, distinct flavor, rung 2 preferred")
    picks.sort(key=lambda p: SLOTS.index(p[0]))

    if permission_due and not any(e["flavor"] == "D" for _, e, _ in picks):
        notes.append("Permission Slip is due but yielded to the brand-tax minimum this week. Run it next week.")
    if len(last) < PERMISSION_SLIP_AFTER_AIRED:
        notes.append(f"Permission Slip held back until {PERMISSION_SLIP_AFTER_AIRED} posts have aired ({len(last)} so far). The lane earns the right to say looking is allowed by naming problems without selling first.")
    if silence_due and not any(e["flavor"] == "C" for _, e, _ in picks):
        notes.append("Silence quota is short and this week does not fix it. Next week's Thursday must.")

    # Rung audit over the trailing four weeks plus this plan.
    planned_rungs = rungs_recent + [preferred_rung(e) for _, e, _ in picks]
    if planned_rungs:
        r2 = planned_rungs.count(2) / len(planned_rungs)
        r3 = planned_rungs.count(3) / len(planned_rungs)
        if r2 < RUNG2_MIN_SHARE:
            notes.append(f"Rung 2 share would be {r2:.0%} (minimum 50%). Write the closes on rung 2.")
        if r3 > RUNG3_MAX_SHARE:
            notes.append(f"Rung 3 share would be {r3:.0%} (maximum 25%). Pull one close down to rung 2.")

    alternates = {}
    for slot, e, _ in picks:
        pool = [a for a in avail if a["id"] not in taken_ids and a["flavor"] not in taken_flavors - {e["flavor"]}]
        same_flavor = [a for a in pool if a["flavor"] == e["flavor"]]
        same_register = [a for a in pool if a not in same_flavor and a["register"] == e["register"]]
        others = [a for a in pool if a not in same_flavor and a not in same_register]
        alternates[slot] = (same_flavor + same_register + others)[:2]

    heats = [FLAVORS[e["flavor"]][1] for _, e, _ in picks]
    return {
        "monday": monday, "picks": picks, "alternates": alternates, "dropped": dropped,
        "notes": notes, "available": avail, "last_flavor": last_flavor,
        "silence_recent": silence_recent, "permission_recent": permission_recent,
        "heat_avg": sum(heats) / len(heats) if heats else 0,
    }


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
def option_block(e, slot=None, monday=None, reason=None):
    fname = FLAVORS[e["flavor"]][0]
    heat = FLAVORS[e["flavor"]][1]
    fam = FLAVORS[e["flavor"]][2]
    first_family = re.match(r"(\d)", fam).group(1)
    lines = []
    head = f"**{e['id']}. {e['title']}**"
    if slot and monday:
        d = monday + timedelta(days=SLOT_OFFSET[slot])
        head = f"### {slot} {d.isoformat()}: {head}"
    lines.append(head)
    lines.append(f"- Flavor: {fname} ({e['flavor']})" + (f" | Register: {e['register']}" if e["register"] else ""))
    lines.append(f"- Rung: {preferred_rung(e)}" + (f" (bank allows {', '.join(map(str, e['rung']))})" if len(e["rung"]) > 1 else ""))
    lines.append(f"- Receipt: {receipt_kind(e)}")
    if receipt_kind(e) == "NEEDED":
        lines.append("  - **No number on camera.** Run it on the viewer's own figure, or as a scene or a question.")
    lines.append(f"- Heat target: {heat} (floor 4; the flavor's old default no longer ships)")
    lines.append(f"- Hook family: {fam} | Pattern interrupt: {PATTERN_FOR_FAMILY[first_family]} (no repeat of the previous post's move)")
    if e.get("drafted"):
        lines.append(f"- Existing script: `{e['drafted']}` -- written before the 30-35s rule and the heat-4 floor. **Re-cut to 68-84 words and lift the hook to heat 4+, do not re-draft from scratch.**")
    if reason:
        lines.append(f"- Why this slot: {reason}")
    lines.append("- Spoken hook: _[routine fills in]_")
    lines.append("- The look (close): _[routine fills in, on the rung above]_")
    return "\n".join(lines)


def render_brief(plan, entries):
    monday = plan["monday"]
    out = [
        f"# Broker Problems: week of {monday.isoformat()}",
        "",
        f"Generated {date.today().isoformat()} by `scripts/broker_problems.py plan`. Three slots, one",
        "primary and two alternates each. Rules applied: 8-week entry rotation, no flavor twice in a",
        f"week, brand-tax minimum {BRAND_TAX_MIN_PER_WEEK} of 3, Silence at least {SILENCE_MIN_PER_28_DAYS} per 28 days,",
        "Permission Slip about monthly, rung 2 at least half. Standard:",
        "[`../../docs/series/broker-problems-standard.md`](../../docs/series/broker-problems-standard.md).",
        "",
        "**A brief is a shortlist, not a clearance.** Re-verify every receipt before drafting, and",
        "never put a number on camera that the bank marks NEEDED. Kale is never mentioned. No firm",
        "is ever identifiable. The close hands over a look, never a leave.",
        "",
        "## The week",
        "",
    ]
    for slot, e, reason in plan["picks"]:
        out.append(option_block(e, slot, monday, reason))
        alts = plan["alternates"].get(slot, [])
        if alts:
            out.append("")
            out.append("Alternates:")
            for a in alts:
                out.append(f"- {a['id']}. {a['title']} ({FLAVORS[a['flavor']][0]}, rung {preferred_rung(a)}, receipt {receipt_kind(a)})")
        out.append("")
    out += [
        "## Audit",
        "",
        f"- Last aired flavor: {FLAVORS[plan['last_flavor']][0] if plan['last_flavor'] else 'none aired yet'}",
        f"- Silence in trailing 28 days: {plan['silence_recent']} (minimum {SILENCE_MIN_PER_28_DAYS})",
        f"- Permission Slip in trailing 28 days: {plan['permission_recent']} (about 1)",
        f"- Brand-tax entries this week: {sum(1 for _, e, _ in plan['picks'] if e['register'] == 'brand tax')} of 3 (minimum {BRAND_TAX_MIN_PER_WEEK})",
        f"- Planned heat average for the lane this week: {plan['heat_avg']:.2f} (schedule-wide band 4.3-4.5 is measured by `content_board.py check-heat`)",
        f"- Entries available after rotation: {len(plan['available'])} (refill below {REFILL_THRESHOLD})",
    ]
    for n in plan["notes"]:
        out.append(f"- **{n}**")
    if plan["dropped"]:
        out += ["", "## Held out this week", ""]
        for e, why in plan["dropped"]:
            out.append(f"- {e['id']}. {e['title']}: {why}")
    out += [
        "",
        "## What happens next",
        "",
        "1. The routine (or the on-demand build when D.J. says \"broker problems\") writes each primary",
        "   through draft, stress test, EP polish, and council review, to `scripts/broker-problems/BP-###-slug.md`.",
        "2. `python3 scripts/broker_problems.py log --entry <id> --script <path> --date <post date>` for each.",
        "3. The Content Board mirrors `scripts/broker-problems/` on its next run; D.J. films off the board.",
        "",
    ]
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------
def load():
    text = BANK.read_text()
    entries, rows = parse_bank(text)
    return text, entries, rows


def cmd_plan(args):
    _, entries, rows = load()
    monday = week_monday(date.today(), args.week)
    plan = plan_week(entries, rows, monday)
    brief = render_brief(plan, entries)
    if args.stdout:
        print(brief)
        return 0
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / f"{monday.isoformat()}.md"
    path.write_text(brief)
    print(f"wrote {path.relative_to(REPO_ROOT)}")
    for n in plan["notes"]:
        print(f"note: {n}")
    return 0


def cmd_pick(args):
    _, entries, rows = load()
    monday = week_monday(date.today(), None)
    avail, _ = availability(entries, rows, monday)
    ordered = sorted(avail, key=lambda e: (0 if e["register"] == "brand tax" else 1,
                                           0 if e["flavor"] == "F" else 1,
                                           0 if 2 in e["rung"] else 1,
                                           1 if receipt_kind(e) == "NEEDED" else 0,
                                           e["flavor"], e["id"]))
    lines = []
    for i, e in enumerate(ordered[:args.count], 1):
        lines.append(f"{i}. {e['id']}. {e['title']} -- {FLAVORS[e['flavor']][0]}, rung {preferred_rung(e)}, receipt {receipt_kind(e)}"
                     + (f", existing script {e['drafted']}" if e.get("drafted") else ""))
    print("\n".join(lines))
    return 0


def cmd_log(args):
    text, entries, rows = load()
    entry = next((e for e in entries if args.entry in entry_codes(e)), None)
    if entry is None:
        print(f"no bank entry {args.entry}", file=sys.stderr)
        return 2
    flavor = FLAVORS[entry["flavor"]][0]
    rung = args.rung or preferred_rung(entry)
    d = args.date or date.today().isoformat()
    datetime.strptime(d, "%Y-%m-%d")
    code = entry["id"] + (f"/{entry['alias']}" if entry["alias"] else "")
    row = f"| {d} | {code} | {flavor} | {rung} | {args.script} | {args.surface} |"
    lines = text.splitlines()
    idx = None
    for i, line in enumerate(lines):
        if line.startswith("## Rotation table"):
            idx = i
        elif idx is not None and i > idx and line.startswith("## "):
            end = i
            break
    else:
        end = len(lines)
    # insert before the blank line(s) that precede the next section
    insert_at = end
    while insert_at > idx and not lines[insert_at - 1].startswith("|"):
        insert_at -= 1
    # replace a placeholder `_(unused)_` row for the same script, if one exists
    for i in range(idx, insert_at):
        if lines[i].startswith("| _(unused)_") and args.script.split("/")[-1].split("-")[1] in lines[i]:
            lines[i] = row
            break
    else:
        lines.insert(insert_at, row)
    BANK.write_text("\n".join(lines) + "\n")
    print(f"logged {row}")
    return 0


def cmd_health(args):
    _, entries, rows = load()
    monday = week_monday(date.today(), None)
    avail, dropped = availability(entries, rows, monday)
    by_flavor = {}
    for e in avail:
        by_flavor.setdefault(e["flavor"], []).append(e["id"])
    print(f"bank entries {len(entries)}, available {len(avail)}, held out {len(dropped)}")
    for f, ids in sorted(by_flavor.items()):
        print(f"  {f} {FLAVORS[f][0]:<36} {len(ids)}  {' '.join(ids)}")
    brand = sum(1 for e in avail if e["register"] == "brand tax")
    print(f"  brand-tax register available: {brand}")
    if len(avail) < REFILL_THRESHOLD or brand < BRAND_TAX_MIN_PER_WEEK * 2:
        print(f"REFILL DUE (available {len(avail)} < {REFILL_THRESHOLD}, or brand-tax {brand} < {BRAND_TAX_MIN_PER_WEEK * 2})")
        return EXIT_REFILL_DUE
    print("ok")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan")
    p.add_argument("--week", help="any date in the target week, YYYY-MM-DD")
    p.add_argument("--stdout", action="store_true")
    p.set_defaults(fn=cmd_plan)
    p = sub.add_parser("pick")
    p.add_argument("--count", type=int, default=6)
    p.add_argument("--stdout", action="store_true")
    p.set_defaults(fn=cmd_pick)
    p = sub.add_parser("log")
    p.add_argument("--entry", required=True)
    p.add_argument("--script", required=True)
    p.add_argument("--date")
    p.add_argument("--rung", type=int)
    p.add_argument("--surface", default="video")
    p.set_defaults(fn=cmd_log)
    p = sub.add_parser("health")
    p.set_defaults(fn=cmd_health)
    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
