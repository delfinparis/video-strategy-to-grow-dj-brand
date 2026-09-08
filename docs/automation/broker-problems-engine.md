# The Broker Problems engine: three finished scripts a week

The Broker Problems lane ([`../series/broker-problems-standard.md`](../series/broker-problems-standard.md))
needs three recording-ready scripts a week, Tuesday, Thursday and Friday. This is how they get
made. Register and strategy: [`../strategy/2026-09-08-brand-tax-register.md`](../strategy/2026-09-08-brand-tax-register.md).

Built like the take brief ([`take-brief.md`](take-brief.md)), not like the walk-and-talk chain:
a weekly planning artifact lands in the repo, the routine writes the scripts, and the Content
Board mirrors them. No email, no reply watcher, no second copy of the walk-and-talk chain's
failure modes.

**The difference from the take brief:** the take routine writes *options* and D.J. picks. This
routine writes *finished scripts*. D.J. asked for three a week he can film, and the Content
Board standard already says a row with a hook and no body is a failure. So the Sunday output is
three complete four-pass scripts, council review included, committed to `scripts/broker-problems/`.

## The chain

```text
Sunday 8:00am CT   Broker Problems routine
                     |
                     |  1. git pull
                     |  2. python3 scripts/broker_problems.py plan
                     |       (deterministic: rotation, flavor rules, brand-tax minimum,
                     |        Silence quota, Permission Slip cadence, rung mix, receipt status)
                     |  3. for each of the three primaries:
                     |       re-verify the receipt (web) -> draft -> stress test -> EP polish
                     |       -> council review -> scripts/broker-problems/BP-###-slug.md
                     |       (if the option says "Existing script", re-cut it instead)
                     |  4. python3 scripts/broker_problems.py log --entry <id> --script <path> --date <slot date>
                     |  5. python3 scripts/broker_problems.py health   (exit 10 = refill due, say so loudly)
                     |  6. commit + push
                     v
       data/broker-problem-briefs/<monday>.md   +   three BP-###.md files   +   rotation rows
                     |
                     v
Daily              Content Board routine: `content_board.py mirror` picks up the new files,
                   posts them as rows with the full body. D.J. films off the board.
                     |
                     v
Any time           D.J.: "broker problems"  ->  Claude shows the three slots
                   D.J.: "broker problems 2" -> Claude builds or re-cuts that slot on demand
```

## The split, and why it is where it is

| Half | Runs where | Why |
|---|---|---|
| Rotation math, flavor rules, quotas, receipt status, the brief skeleton | `scripts/broker_problems.py`, offline, standard library | These are the things a model gets wrong at 8am: counting an eight-week window, remembering that Thursday was a Silence, noticing the bank is four entries from empty. A script does them the same way every time. |
| Receipt verification, the hook, the four passes, the council | The Sunday routine (web search) or the on-demand build in Claude Code | Judgment, and sourcing. Half the bank is `Receipt: NEEDED` on purpose. |

Nothing in this chain may invent a figure. An entry marked NEEDED ships only in a shape that
needs no number (the viewer's own figure, a scene, a question). The brief prints that constraint
on the option so the routine cannot miss it.

## What `plan` enforces

- **Eight-week no-repeat on entries.** Only dated rotation rows count. BP-001 through BP-005
  were written and never aired, so their entries are still available and the brief offers them
  as re-cuts.
- **No flavor twice in a week, and never the same flavor as the last aired post.**
- **Brand-tax minimum: two of three.** D.J.'s 2026-09-08 direction. Flavor F leads Tuesday.
- **The Silence at least twice per 28 days.** It converts, and it is the flavor a fee lane
  quietly stops making. It yields to nothing except an empty Flavor C.
- **The Permission Slip about monthly, and only after three posts have aired.** It yields to
  the brand-tax minimum in a collision, and the brief says so.
- **Rung 2 at least half of the trailing four weeks, rung 3 at most one in four.**
- **Parked, blocked, and sign-off-required entries are held out** and listed under "Held out
  this week" so nobody wonders where D2 went.
- **Rows already logged for the week are honored, not re-planned.** Running `plan` after `log`
  shows the week as it is.

## Commands

```bash
python3 scripts/broker_problems.py plan                 # this week's brief -> data/broker-problem-briefs/
python3 scripts/broker_problems.py plan --week 2026-09-14 --stdout
python3 scripts/broker_problems.py pick --count 6 --stdout   # flat shortlist, off-cycle
python3 scripts/broker_problems.py log --entry F1 --script scripts/broker-problems/BP-006-x.md --date 2026-09-08
python3 scripts/broker_problems.py health               # exit 10 = refill due
```

## Refill

`health` exits 10 when fewer than six entries are available after rotation, or fewer than four
brand-tax entries. At three a week the bank of 28 runs thin around late October 2026. The refill
is not automated on purpose: the two best sources are D.J.'s recruiting-call notes and Kale's own
departures, and both need his hand. The routine reports the exit code in its summary and stops
short of inventing entries.

## What can go wrong

- **The routine writes a script with a number the bank marks NEEDED.** The brief prints "No
  number on camera" on those options. If a script ships one anyway, the receipt was invented.
  Kill the script, not the entry.
- **A script names a firm, a franchise, or a product.** Ship test in the standard's pre-flight.
  C4's source quote names a product; the bank marks it a hard block. Strip to the category.
- **A script mentions Kale.** Never, in any form, including the captions and the pinned comment.
- **The plan and the board disagree.** The board mirrors files by basename; a renamed file is a
  new row. Do not rename a BP file after it is on the board.
- **The Friday slot.** The calendar carries 16 videos as of 2026-09-08 pending D.J.'s call on
  whether the third Broker Problem is added or displaces something. Until he rules, the engine
  plans three.
