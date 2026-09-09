# Realtor Tips (Stupid Things Realtors Do) - Series Standard

Per-series rules for the **realtor tip** lane: *mistakes agents make, and what to do instead.*
On the Content Board and in the bank this lane is called **Stupid Things Realtors Do**; D.J.
calls them "do this, don't do that" tips and, since 2026-09-09, "realtor tips." Same lane,
same bank. Builds on [`../editorial-standards.md`](../editorial-standards.md), the universal
standard. Everything there applies here. This document only adds what is specific to the lane.

**If this document and the universal standard ever conflict, the universal standard wins.**

Charter, qualifying test, target rule, heat rules, and the bank:
[`../../data/stupid-things.md`](../../data/stupid-things.md). Refill contract:
[`../automation/stupid-things-bank.md`](../automation/stupid-things-bank.md). Why this lane is
now 3-4 a week and the daily brief leads with it:
[`../strategy/2026-09-09-weekly-mix-and-tips-engine.md`](../strategy/2026-09-09-weekly-mix-and-tips-engine.md).

---

## What a realtor tip is

A 30-35 second walk-and-talk where D.J. names one specific thing agents do that costs a client,
a deal, or the agent on the other side, and hands over the exact thing to do instead.

**Core promise to the viewer:** *You've seen this. Here's what it actually costs, and here's
the move.*

Three things separate it from its neighbors:

| | Realtor tip (this lane) | The Take | Broker Problem |
|---|---|---|---|
| Subject | A **behavior** agents perform | A **belief** agents were taught | The **arrangement** with their brokerage |
| Beat 2 | Who pays for the behavior | Who profits from the belief | What the premium was supposed to buy |
| Close | The swap: do this instead | The swap | A look, never a leave |
| Bank | `data/stupid-things.json` | `data/sacred-cows.md` | `data/brokerage-pain.md` |

Since 2026-09-09 the Take is a **source** for this lane, not a slot of its own: a take is a
realtor tip that happens to carry a who-profits beat. When the daily brief offers a take, it is
labelled `[TIP]` like the rest and built to this standard with the who-profits line living
inside TENSION. Brokerage economics (splits, fees, support, coaching, tools) stays out of this
lane entirely; that is a Broker Problem.

---

## The four beats on the universal clock

The bank pre-writes one sentence per beat. The build sharpens them; it does not start over.

| Clock beat | Seconds | Words | This lane's beat | Comes from |
|---|---|---|---|---|
| **HOOK** | 0:00-0:01.5 | 5-8 | **THE STUPID THING**, named flat, with the cost in it | the angle's `hook`, sharpened |
| **TENSION** | 0:01.5-0:06.5 | 11-14 | **LOOKS LIKE**: the recognizable scene | the entry's `looks_like`, cut to one sentence |
| **THE POINT** | 0:06.5-0:21.5 | 34-40 | **WHY IT COSTS**: the receipt, said once, then the turn | the entry's `receipt` + the angle's `angle` |
| **PAYOFF** | 0:21.5-0:30 | 18-22 | **THE FIX**: the swap, physical and do-it-Monday, then the loop-back | the angle's `swap` |

**68-84 spoken words, hard cap 88, floor 68.** Count them. STUPID-001 was written at 157 words
to the retired 45-75s spec; it is a re-cut candidate, not a format model. The format models are
BP-006 through BP-008 (structure) and the beat mapping above (content).

**The swap is never what gets cut.** An indictment with no fix is a rant, and the lane's whole
job is the fix. If the script is over, cut the scene to its shortest recognizable form, then
shorten the receipt to the number and its owner. Touch the swap last.

**The receipt is one number, said once, with its limit.** "NAR, twenty twenty-six" is enough on
camera; the full citation lives in Data Source. An entry marked `receipt: needed` ships with no
number: run it as the scene and the swap, and say nothing a commenter can check and beat.

---

## Heat and target

- **Band 4 to 4.7.** Every script names the wrong default flatly and puts the cost in the first
  ten seconds. Softeners ("a lot of agents," "this might be," "I could be wrong") come out.
- **`target: sideways` carries full heat.** The wronged party is the good agent watching.
- **`target: self` caps at 4.3.** The viewer is the one doing it and Rule 9.4 does not let the
  friction point at them. Those scripts reach the band through specificity about the cost,
  never through a harder verdict about the person.
- **Alternate targets.** `pick` already does this; the daily brief keeps the alternation across
  its `[TIP]` options and the week should not run three `self` tips in a row.
- **Heat 5 never.** No brokerage, franchise, team, coach, program, product-as-villain, or
  identifiable agent. Ship test: could a viewer name one company with confidence?
- **Legal-exposure entries carry the highest evidence burden.** Say the exposure (the statute,
  the docket), never predict the verdict.

## Hook family and visual open

- Default families: **9 Swap/List** ("stop doing X, do Y"), **8 Cohort Callout** ("listing
  agents, ..."), **1 Mirror** with the cost named, **4 System Indictment** when the behavior is
  industry-wide. Rotate; never the same family as the previous post.
- Family 9 is the save magnet and this lane's natural shape. It still has to open on a cost or a
  wrong default to clear heat 4: "Stop saying 'I'll get you top dollar.' It costs you the
  listing" clears; "Here's a better way to say it" does not.
- Pattern interrupt: One Prop and Gesture-On-Beat pair with Swap/List; Walk-Toward with Cohort
  Callout and Mirror; Location Cold-Open when the scene is on-site (a stale sign, a lockbox).

## The close

Rule 4: a "here's what you do now" close, no engagement asks. In this lane the close is the
swap itself, physical enough to do Monday: the sentence to say at the signing table, the task
to put in the phone, the question to ask before the disclosure goes out. Then the loop-back
reloads the hook (Rule 9.1). Never a moral.

---

## How a tip gets built (three paths, one standard)

1. **The daily brief (primary).** The 5:30am routine runs `python3 scripts/stupid_things.py pick`
   and leads the email with 2-3 `[TIP]` options, each carrying the bank id, the target class,
   the pre-written scene, the swap, and the receipt status. D.J. replies with a number; the
   Apps Script generator builds it to this standard. The generated script carries `bank_id` and
   `bank_angle` in frontmatter. Within the hour the Walk & Talk Reply → Content Board routine
   posts it to the Content Board as a Picked row and logs the angle; the Sunday bank check is
   the backstop.
2. **On demand.** D.J. says **"stupid things"** or **"realtor tips"** in Claude Code: show
   `pick --count 5`, build the pick through the four passes to
   `scripts/stupid-things/STUPID-###-slug.md`, then
   `python3 scripts/stupid_things.py log --id ST-#### --script <path>`.
3. **The local brief.** `scripts/news_brief.py` writes the same 2-3 tip options into
   `data/news-briefs/<today>.md` above the news candidates, for the "walk and talk" on-demand
   path on any machine.

**Re-verify the receipt at build time, every path.** The bank is a shortlist, not a clearance.

---

## Pre-flight (in addition to the universal checklist)

- [ ] The entry is a behavior, not a belief (else it is a take) and not brokerage economics (else
      it is a Broker Problem)
- [ ] `bank_id` and `bank_angle` in frontmatter; the angle is still open in the bank
- [ ] Receipt re-verified, or no number spoken
- [ ] Hook names the cost in 5-8 words; family rotated from the previous post
- [ ] `target` declared; `self` scripts sit at or under 4.3
- [ ] The swap is physical, one move, and survives the cut
- [ ] No identifiable firm, product, or agent
- [ ] 68-84 spoken words, counted
- [ ] Five captions, YouTube Shorts `**Title:**` present, hashtag caps, one brand tag
- [ ] Logged with `stupid_things.py log` once the script exists (on-demand path), or carries
      `bank_id` so the Sunday check can log it (email path)
