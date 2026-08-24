# The weekly take brief: how it gets produced

The take lane ([`../series/take-standard.md`](../series/take-standard.md)) needs 3 scripts a
week. This is how D.J. gets 5-7 vetted options to pick them from, every Sunday.

Deliberately **not** built like the walk-and-talk chain. That one is a daily 5:30am research
routine feeding a Gmail draft, an Apps Script sender, an alarm, and a reply watcher, and
[`walk-and-talk-delivery.md`](walk-and-talk-delivery.md) is a post-mortem of what happens when
one link in it goes quiet. A weekly planning artifact does not need to beat D.J. to the alarm
clock, so it does not buy a second copy of that risk. The brief lands in the repo, a Gmail
draft nudges him, and he picks from it in Claude Code whenever he sits down.

## The chain

```text
Sunday 7:00am CT   Take Brief routine
                     |
                     |  1. git pull
                     |  2. python3 scripts/take_brief.py --count 6
                     |       (deterministic: rotation, section spread, receipt status)
                     |  3. web-verify every NEEDS RECEIPT option
                     |  4. write Hook / Swap / Loop-back into each option
                     |  5. commit + push
                     |  6. create ONE Gmail draft (unsent)
                     v
       data/take-briefs/YYYY-MM-DD.md   +   draft "Take options - week of <Mon date>"
                     |
                     v
Any time that week   D.J.: "takes"  ->  Claude lists the options
                     D.J.: "takes 2" ->  Claude builds the full script
```

## The email is a DRAFT, and a draft is not a delivery

D.J.'s call, 2026-08-12, matching what the take-carousel, KIRP, and news/tip routines already
do. Read this before assuming he has seen a brief.

**The Gmail connector cannot send.** It only creates drafts. That is the whole reason the
walk-and-talk chain needs an Apps Script sender at all. So this brief produces a draft sitting
in D.J.'s drafts folder, titled `Take options - week of <Mon date>`, and nothing moves it to
his inbox.

That is a deliberate trade, not an oversight. A real sent email would need a second
subject-line contract in the Apps Script, and that contract is exactly what caused the
five-day outage in June 2026 when a routine switched an em dash to a hyphen. For a weekly
planning doc the draft is enough of a nudge, and the repo file is the real artifact.

**What follows from that:**

- **A created draft is not proof D.J. read it.** The walk-and-talk doc's rule ("never treat
  file existence as delivery") applies here with one more step removed. Do not report a brief
  as delivered because a draft exists.
- **The draft is written to be pickable from a phone.** Spoken hook first on every option,
  because that is what he is actually choosing between, then slot, swap, and receipt. He should
  not need to open the repo to choose.
- **Replying to it does nothing.** There is no reply watcher on this routine, unlike the
  walk-and-talk chain. The draft says so in its last line. If a reply-to-build flow is ever
  wanted here, it needs building; do not assume it works because the daily one does.
- **A failed draft must be reported, never silent.** The routine is instructed to say so
  loudly in its summary if the Gmail connector is down, because a silent fallback is a bug
  (same rule as the walk-and-talk chain). The connector losing OAuth is the single most common
  failure across these routines.

**Upgrade path if the draft turns out to be too easy to miss:** extend
`scripts/apps-script/walk-and-talk-project.gs` with a second sender keyed to the
`Take options` subject prefix. Change the subject in one place, change it in both.

## The split, and why it is where it is

| Half | Runs where | Why |
|---|---|---|
| Rotation math, section spread, receipt status | `scripts/take_brief.py`, offline, no dependencies | The 8-week window is arithmetic. A model asked to count weeks gets it wrong eventually, and gets it wrong *silently* |
| Sourcing numbers, writing hooks | The routine | 19 of 42 bank entries have no verified number. Sourcing needs web search, which a script-side API call would not have |

The script writes a **skeleton** with `_[routine fills in]_` where the hook, swap, and loop-back
go. That is on purpose: a half-run routine should look obviously broken rather than look
finished. If D.J. opens a brief and sees those placeholders, step 3 or 4 did not happen.

## The script

```bash
python3 scripts/take_brief.py               # 6 options -> data/take-briefs/<today>.md
python3 scripts/take_brief.py --count 7     # 5-7 allowed
python3 scripts/take_brief.py --verified-only   # only entries that already have a receipt
python3 scripts/take_brief.py --stdout      # print, don't write
```

Standard library only. It reads [`../../data/sacred-cows.md`](../../data/sacred-cows.md) and
nothing else, so it runs anywhere the repo is checked out.

What it guarantees:

- **No entry used inside 8 weeks**, counted off the rotation table at the bottom of the bank.
- **Section spread** by round-robin, so one section cannot fill the brief.
- **Ship-ready first.** Entries with in-repo evidence outrank entries still needing research.
- **Bank health footer** listing what is blocked and until when, plus a refill warning when
  eligible entries drop under 24.

What it refuses to do: invent a number, or write a hook that implies one.

## The routine's job

Beyond running the script, the routine owns the part that needs judgment and the web:

1. **Clear every NEEDS RECEIPT block.** Find a real figure with a named publisher and a year.
   If one cannot be found, **drop that option and note it** rather than softening the claim
   into something unfalsifiable. Six honest options beat seven with a soft one.
2. **Re-check in-repo receipts that carry a caveat.** Several bank entries say things like
   "needs the current NAR Profile citation." A stat that was right in April may be wrong now.
3. **Write the hook, swap, and loop-back** per the take standard: spoken scroll-stop, tension
   in the first 3-5 words, friction outward at the incentive, swap physical and doable
   tomorrow.
4. **Assign slots.** One pick each for Mon, Wed and Fri. Wednesday is the week's hardest swing
   (4.5-5, top of the Rule 9.2 band); Mon and Fri run 4 to 4.3. With heat no longer rationed,
   the family rotation is the only thing preventing three takes from reading as one repeated
   move, so it matters more than it used to. Rotate hook families per the standard.
5. **Never name** a brokerage, coach, product, or individual agent. That is heat 5 and banned
   outright in this lane.

## Picking and building

In Claude Code, on any device:

- **"takes"** reads the newest `data/take-briefs/*.md` and lists the options.
- **"takes 2"** (or several numbers) builds the full script through the four passes, out to
  `scripts/takes/TAKE-###-slug.md`.

Claude re-verifies the receipt at build time regardless of what the brief says. The brief is a
shortlist, not a clearance.

After building, the chosen entries get logged in the rotation table in
[`../../data/sacred-cows.md`](../../data/sacred-cows.md) so the 9:00am take-carousel routine
does not re-pick them.

## When the brief does not show up

There is no alarm on this one, by design: a missing weekly planning doc is a mild
inconvenience, not a missed post, and an alarm nobody needs is how real alarms get ignored.
The Gmail draft is a nudge, not a watchdog. No draft means no alarm fires, so silence here
means nothing either way.

1. `git pull`, then check whether `data/take-briefs/<sunday>.md` exists.
2. If it does not, just run `python3 scripts/take_brief.py` yourself. It needs no API key and
   no network, and it produces the skeleton in under a second. Then say "takes" and Claude
   fills in the rest live, which is the same work the routine would have done.
3. Check the routine at <https://claude.ai/code/routines> if it keeps missing.

The recovery path is genuinely as good as the happy path here, which is the main reason this
lane does not need the walk-and-talk chain's machinery.

## Failure mode worth knowing

**The brief exists but is full of `_[routine fills in]_`.** The script ran and the routine
died before step 4. The options are still real and the rotation math is still correct, so say
"takes" and Claude fills them in live. Do not post from a skeleton.

**The draft arrived but the repo file did not, or vice versa.** These are steps 5 and 6 and
either can fail alone. The repo file is the authoritative artifact; the draft is a copy for
reading on a phone. If they disagree, trust the file. If only the draft exists, the commit
failed and the brief will be missing from the repo for anyone on another device.
