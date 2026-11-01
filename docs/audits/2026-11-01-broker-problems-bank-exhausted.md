# Broker Problems: the bank is exhausted, and it is arithmetic, not a bug

Audit written 2026-11-01 by the Sunday Broker Problems routine, which produced **zero scripts**
for the week of 2026-11-02 because `plan` returned zero slots.

## What happened

```
$ python3 scripts/broker_problems.py health
bank entries 28, available 0, held out 28
  brand-tax register available: 0
REFILL DUE (available 0 < 6, or brand-tax 0 < 4)   # exit 10
```

`plan` wrote `data/broker-problem-briefs/2026-11-02.md` with an empty "## The week" section and
two notes: no brand-tax entry available for Tuesday, and the brand-tax minimum of 2 could not be
reached. The rotation math is correct. There was nothing to build.

## Why, in one line

**24 usable entries against a 24-slot rotation window. The lane has zero slack by construction.**

- The bank holds 28 entries.
- Four are permanently held and have been for weeks: **B4** parked pending a receipt, **C5** open
  pending D.J. sign-off, **D2** open pending D.J. sign-off, **D3** blocked pending D.J.'s
  material. That leaves **24 usable**.
- `ROTATION_WEEKS = 8`, and the lane ships **3 a week**. The no-repeat window therefore holds
  **8 x 3 = 24 posts** at any moment.
- 24 usable entries filling a 24-post window means every usable entry is always inside the
  window. Each week three entries age out and three get consumed. Net change: zero.

This is why `health` has been reporting refill due and why availability now sits at 0. The engine
doc predicted the date ("the bank of 28 runs thin around late October 2026"); this is that date
arriving. It will not clear itself.

## What the next few weeks actually look like

Running `plan` for future weeks shows availability of 3, 6, then 9, which is **misleading** -- no
posts are logged for November yet, so those weeks retire old entries without consuming new ones.
Once a week's three posts are logged, the following week drops back by three. The steady state is
0 to 3 available.

Concretely, if the lane resumes:

- **Week of 2026-11-09:** 3 entries come back (F1, C4, A2). Exactly enough for three slots, with
  **no alternates** and only one brand-tax entry, so the brand-tax minimum of 2 fails again.
- **Every week after:** the same knife edge. One parked receipt or one flavor collision and the
  week comes up short.

So the lane can limp, but it cannot be planned, and the first failed receipt re-verification has
nowhere to fall back to.

## What unblocks it

Nothing in this chain may invent entries, so the routine stopped. Two kinds of fix:

**Immediate, and already owed (would return 3 usable entries this week):**

1. **D2 sign-off** -- "I run a brokerage and my agents should be looking too." The strongest
   Permission Slip in the bank. It is a real public commitment agents will hold D.J. to, which is
   exactly why it needs his word and not a routine's.
2. **C5 sign-off** -- "You left, and nobody called."
3. **B4's receipt** -- "Their revenue from you goes up as their time to you goes down," parked for
   want of a number.

**Structural, and the actual answer:** the refill the 2026-09-08 register doc asked for and that
has not landed. The two best sources are both D.J.'s hand and neither is automatable:

- **His recruiting-call notes.** Thirty calls a day, the best Chicago-specific brand-tax material
  there is, and none of it is in the bank. Raw dumps are fine; entries get written with
  `receipt: first-party, unquantified`.
- **Kale's own departures.** Whether any of why agents left Kale becomes an entry. The most honest
  material available and the most exposed. Not started.

**Sizing the refill:** holding 3 a week with real planning slack needs roughly **32 to 34 usable**
entries, not 24 -- the 24-slot window plus two alternates a slot. Flavor F (brand tax) needs the
most, since the minimum of 2 of 3 a week means the register alone wants about 16 entries in
rotation and has 6.

The alternative, if the refill is not coming, is to drop the lane to **2 a week**, which turns the
window into 16 slots against 24 usable entries and restores 8 entries of slack immediately. That
is D.J.'s call, not the routine's, and CLAUDE.md's quality floor points the same way: *if a week
cannot clear that bar, ship fewer posts. Volume is never the goal.*
