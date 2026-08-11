# Weekly Take Briefs

One brief per week, produced Sunday morning, holding 5-7 vetted options for the three take
videos that ship Mon/Wed/Fri. Feeds The Take
([`../../docs/series/take-standard.md`](../../docs/series/take-standard.md)).

Each option is a candidate from the sacred-cows bank that has cleared the 8-week rotation
window, plus a spoken hook, the who-profits turn, the swap, and a sourced receipt.

## The pipeline

1. **Parse the bank.** [`../sacred-cows.md`](../sacred-cows.md) holds 42 candidate beliefs
   across six sections, each with a `Profits:` line, a `Turn:`, and an evidence status.
2. **Enforce rotation.** Anything used inside 8 weeks is dropped, counted off the rotation
   table at the bottom of the bank. Video and carousel share one row per entry, so a paired
   pair blocks once, not twice.
3. **Spread by section.** Round-robin across sections so one section cannot fill the brief,
   biased away from whatever ran most recently.
4. **Rank ship-ready first.** Entries whose evidence already exists in-repo outrank entries
   still needing a number sourced. Flagged entries sort last.
5. **Write the skeleton.** Steps 1-4 are deterministic and run offline in
   [`../../scripts/take_brief.py`](../../scripts/take_brief.py) with no dependencies. Hook,
   swap, and loop-back are left as `_[routine fills in]_`.
6. **Source and fill (the routine).** The Sunday routine web-verifies every option marked
   NEEDS RECEIPT, drops any whose number cannot be found, and writes the hooks. This half
   lives in the routine because 19 of the 42 entries have no verified number yet and sourcing
   them needs web search.
7. **Commit.** The brief lands here; D.J. says "takes" in Claude Code to pick.

Full chain and failure modes:
[`../../docs/automation/take-brief.md`](../../docs/automation/take-brief.md).

## Reading one

- **NEEDS RECEIPT** on an option means no sourced number exists for it yet. If it survived into
  a finished brief, the routine found one. If the brief still shows the marker, the routine
  died before step 6.
- **`_[routine fills in]_`** anywhere means the same thing. Do not post from a skeleton; say
  "takes" and Claude fills it in live.
- **Heat check / Flagged** callouts are lifted from the bank. Read the bank note before
  drafting; those entries sit near a line the lane does not cross.
- **Bank health** at the bottom lists what is blocked by rotation and until when, and warns
  when eligible entries drop under 24.

## Rebuilding one by hand

```bash
python3 scripts/take_brief.py            # 6 options for the coming week
python3 scripts/take_brief.py --count 7  # 5-7 allowed
python3 scripts/take_brief.py --verified-only   # nothing needing research
```

Standard library only, no API key, no network. The recovery path is as good as the happy path,
which is why this lane has no alarm.
