# The Stupid Things bank: how it refills itself

The **Stupid Things Realtors Do** lane pulls from [`../../data/stupid-things.json`](../../data/stupid-things.json).
This is how that bank stays full without D.J. thinking about it.

Charter, qualifying test, and heat rules: [`../../data/stupid-things.md`](../../data/stupid-things.md).

---

## The contract

**Availability is counted in open angles, not practices.** D.J.'s rule, 2026-08-13: the same
topic runs again as long as the angle on the *solution* is new. So a practice with every angle
spent is not gone, it is waiting for a new angle.

```
available = practices with at least one angle whose status is "open"
```

- **Target: 20 available.**
- **Refill trigger: 5.**
- The bank gets worked down to 5, then topped back to 20. Not a weekly quota.

## The chain

```text
Weekly (Sun 6:00am CT)   Stupid Things Bank Check routine
                           |
                           |  1. git pull
                           |  2. python3 scripts/stupid_things.py health
                           |
                           +-- exit 0  -> post nothing, do nothing, stop.
                           |             This is the normal outcome most weeks.
                           |
                           +-- exit 10 -> REFILL. Scour, draft candidates, then:
                                            3. pipe JSON into `intake --stdin`
                                            4. commit + push
                                            5. ONE Gmail draft: what got added
                           v
              data/stupid-things.json  (+ regenerated data/stupid-things.md)
                           |
                           v
Any time                 D.J.: "stupid things"    -> Claude lists the shortlist
                         D.J.: "stupid things 2"  -> Claude builds the full script
                                                     then logs the angle as used
Daily 5:30am CT          Morning Walk & Talk Research runs `pick --count 6` and leads the
                         email with 2-3 [TIP] options (2026-09-09). A pick built by the Apps
                         Script generator carries bank_id + bank_angle in its frontmatter.
Hourly (weekdays)        Walk & Talk Reply -> Content Board posts each Apps-Script-built script
                         to the Notion board as a Picked row and runs `log` for a [TIP] right
                         then (trig_01WJretURg6XmPzY58xkuX9n).
Weekly (Sun 6:00am CT)   Backstop. Before the health check, the Bank Check routine reads the week's
                         "Walk & Talk Options" threads, finds generated tip scripts by their
                         bank_id line, and runs `log` for each, so email-built tips leave the
                         pool. Then `board-check` (exit 12 = the bank disagrees with what has
                         actually been built), then health, then the refill branch as before.
```

## board-check: the bank against the artifacts (2026-09-10)

```
python3 scripts/stupid_things.py board-check     # exit 0 = agrees, exit 12 = does not
python3 scripts/stupid_things.py board-check --json
python3 scripts/tests/test_board_check.py        # 18 cases, offline, no deps
```

See also `receipt-check` below, which asks the other question: not "was this
angle already built" but "is this receipt something Rule 1 would accept today."

The Sunday log step above only covers tips built by the **email** path, because Gmail is the
only place it looks. A tip built in Claude Code, or one whose script was written straight onto
the Content Board, leaves no trace it can see. `board-check` closes that by reading the bank
next to the two places a finished script actually lands: the committed board cache
(`data/content-board-state.json`) and `scripts/stupid-things/`. It is offline and
deterministic like the rest of the engine -- no Notion call, and the routine only needs the
exit code.

Three disagreements, all of which had already happened when it was written:

| It finds | What it means | Why it matters |
|---|---|---|
| **BUILT BUT STILL OPEN** | A board row or repo script exists for an angle the bank still offers | The brief offers it again and it gets built twice |
| **RECEIPT SAYS CONFIRMED, THE SCRIPT SAYS OTHERWISE** | A build re-verified the receipt, found it did not hold, and the finding never reached the bank | The brief keeps printing a claim that a build already disproved |
| **LOGGED BUT THE SCRIPT IS NOT THERE** | An angle is marked spent and its script path does not exist | The angle is gone and so is the work |

**The morning that produced it.** ST-0002 was built on 2026-08-23, posted to the board, and
never logged, so the 2026-09-10 brief offered it again and D.J. picked it. That same 2026-08-23
build had *also* re-verified the receipt and found the cited NAR page was from April 2024 and
said nothing about a responsiveness ranking -- and that finding sat in the script for eighteen
days while the brief kept printing `receipt: confirmed (NAR, 2026)`. Neither fault is visible
from inside the bank. Both are obvious the moment the bank is read next to the artifacts.

The first run found **five** more built-but-open angles, so this was never a one-off.

**It reports what it cannot check rather than skipping it.** A board row whose ref carries no
bank id, or whose angle number and angle text point at different angles, comes back under
COULD NOT BE CHECKED. Guessing which angle a script belongs to would spend the wrong one, and a
silent skip is how the thing this check exists to catch would slip past the check itself.

**Why the Sunday log step exists.** The Apps Script generator is one API call with no
filesystem, so a tip it builds cannot mark its own angle used. Without the Sunday step the
same angle stays open and gets offered again. `log` refuses an angle that is already spent, so
the step is safe to re-run.

**The cheap check is the point.** Most weeks the routine runs one offline command, gets exit 0,
and stops. It costs almost nothing. The expensive scouring only happens when the bank has
actually been worked down, which is the shape D.J. asked for: *run this automatically when it
gets low.*

**Exit code 10 is the whole interface.** The routine does not parse output to decide whether to
refill. `scripts/stupid_things.py health` returns 10 when a refill is due and 0 when it is not.
If that contract ever changes, this doc and the routine change together.

## The split, and why it is where it is

| Half | Runs where | Why |
|---|---|---|
| Counting availability, deciding a refill is due | `scripts/stupid_things.py`, offline | Counting is arithmetic. A model asked to count gets it wrong eventually, and gets it wrong *silently* |
| Refusing duplicates and rewords | same script | The reuse rule lives or dies on this. See below |
| Honoring the rejected list | same script | Fails closed. A killed candidate must not come back because a refill phrased it differently |
| Finding practices, sourcing receipts, writing angles | the routine | Needs web search and judgment. A script-side call would have neither |

### The dedupe is the load-bearing part

Reuse is only a feature while the angles are genuinely different. The moment a refill can bank
"say the honest number first" on top of "lead with the real price," the bank quietly turns into
the same video over and over and nobody notices for a month.

So `intake` refuses three things, and each was tested against a real failure before shipping:

1. **A reworded angle** on a practice already in the bank, whether the original is open or
   already used. Matched on the max of Jaccard and the overlap coefficient over content words,
   at 0.50. Refused with the angle it collided with, so the routine can try again. This is the
   check the reuse rule depends on.
2. **Anything on the rejected list**, matched on `match_terms` rather than similarity. This one
   is deliberately not lexical: "Agents who are terrible because they just got licensed" shares
   two content words with "agents who are bad at their job because they are new or
   inexperienced," and no similarity measure will ever join them. Term matching catches it.
   **This is the punching-down guardrail and it fails closed.**
3. **A near-certain duplicate practice**, at 0.75 and above. Only near-certainty auto-merges.

### The limit, stated plainly: the script cannot find semantic duplicates

**It catches rewords. It does not catch the same practice described in different words, and no
amount of threshold tuning will change that.** Both failure directions shipped during the first
real intake, which is why the design is what it is:

- At 0.55 it **missed** "the pre-contract superstar who disappears after the client signs"
  against "going radio silent after the contract is signed." Same practice, scored 0.29.
- At 0.55 it **wrongly merged** "leaking your own client's bottom line to the other side" into
  "running down the agent on the other side of the deal." Different practices, scored 0.571,
  because both are short and share "own," "client," "other," "side."

Lowering the bar to catch the first makes the second worse. Raising it to stop the second makes
the first worse. And the genuinely hard cases score at **noise level**: "Photographing a
client's largest asset on a phone" against "Dark, blurry, badly composed iPhone photos on the
MLS" scores **0.14**, as does "Overpricing to win the listing" against "Taking a listing at a
price the comps don't support." Nothing distinguishes those from thousands of unrelated pairs.

So the script does the half it can prove and escalates the rest:

| Score | What happens |
|---|---|
| **>= 0.75** | Auto-merge. Near-certain |
| **0.30 - 0.75** | Entry is **created**, and the intake report flags it: `? ST-00XX resembles ST-00YY` |
| **< 0.30** | Created silently. Below this, review noise drowns the signal |

**A wrong auto-merge is the more expensive error**, because it buries an entry somewhere nobody
looks again. Creating a duplicate is visible and fixable; a bad merge is neither.

### So every refill has a mandatory human dedupe step

After `intake`, the routine **must**:

```bash
python3 scripts/stupid_things.py dupes            # suspects, not verdicts
python3 scripts/stupid_things.py merge --from ST-00XX --into ST-00YY
```

and then **read the new entries against the bank itself**, not just the `dupes` output, because
the hardest duplicates score below the reporting floor. This is judgment work and it is exactly
why it lives in the routine rather than the script. The first bulk intake produced **eight**
real duplicates; `dupes` surfaced four of them and the other four had to be caught by reading.

## What the routine does on a refill

### 1. Scour

Where to look, in priority order. **This list is built from what actually returns, not from
where the complaints feel like they live.**

**Reddit is not directly reachable.** `WebFetch` is blocked on reddit.com and `WebSearch`
barely indexes subreddit threads; a `site:reddit.com` query returns Wikipedia and Trustpilot.
Do not write a refill that depends on it. Reddit-style material arrives indirectly, through
Google-indexed forum threads (BiggerPockets, ActiveRain) and through press that quotes them.

| Priority | Source | What it yields | Receipt grade |
|---|---|---|---|
| 1 | **State license enforcement dockets** (IDFPR monthly reports, NV RED, CA DRE, CO DRE) | Adjudicated bad practice with case numbers and dates | Highest. Already proven |
| 2 | **Regulator guidance and bulletins** (TREC articles, SC LLR, CO DRE notifications) | The behavior a regulator felt the need to warn licensees about | High |
| 3 | **E&O carriers and real estate attorneys** (CRES, firm blogs) | The complaint categories that most often become litigation | Medium. Named category, rarely a number |
| 4 | **Consumer press and advice columns** | What the public is being told to watch out for | Medium |
| 5 | **Consumer agent reviews** (Redfin agent pages, Trustpilot) | Verbatim client complaints, unfiltered | Low as receipt, high as sighting |
| 6 | **Industry commentary and forums** (Substack, BAM, Inman, BiggerPockets via Google) | Agent-on-agent critique, which is the `sideways` vein | Low as receipt, high as sighting |

Bias the search toward **`target: sideways`** candidates (the agent on the other side of the
deal), because that is the lane's default and the bank currently skews that way for a reason:
the good agent watching is the wronged party rather than the accused.

### 2. Write candidates

Output a JSON array. New practices need `practice`, `category`, `target`, and `angles`. A new
angle on an existing practice needs only `practice` (any phrasing that matches) and `angles`.

```json
[
  {
    "practice": "Going radio silent after the contract is signed",
    "angles": [
      {"angle": "Escalate to the managing broker on day two, not day seven",
       "swap": "No answer in 24 hours, call the managing broker directly. Not the agent again."}
    ],
    "sightings": [{"date": "2026-10-05", "where": "IDFPR Sept 2026 report",
                   "url": "https://...", "gist": "..."}]
  },
  {
    "practice": "A practice not yet in the bank",
    "category": "Duty and disclosure",
    "who_complains": "Buyers, and the E&O carrier",
    "target": "sideways",
    "heat_ceiling": 3.5,
    "receipt": {"status": "needed"},
    "sightings": [{"date": "...", "where": "...", "url": "...", "gist": "..."}],
    "angles": [{"angle": "...", "swap": "..."}]
  }
]
```

Rules the routine owns, because the script cannot check them:

- **A swap is mandatory and it is physical.** One thing, at the agent's own business, doable
  tomorrow. An indictment with no fix is a rant, and it is this lane's likeliest failure.
- **Never invent a receipt.** Ship `{"status": "needed"}` and let the build pass source it.
  Never write an angle that implies a figure nobody has checked.
- **A sighting is not a receipt.** Sightings prove the complaint recurs. That is all.
- **Vendor blogs are a trap.** Numbers about listing photos are mostly published by companies
  selling listing photos. If the only source sells the solution, set a `flag` and leave the
  receipt needed.
- **Never name** a brokerage, franchise, team, coach, program, product-as-villain, or an
  identifiable agent. Heat 5, banned outright.
- **Never bank a character judgment.** "Lazy agents," "new agents who don't know what they're
  doing." The script blocks the phrasings it knows; the routine must not try new ones.

### 3. Intake and report

```bash
python3 scripts/stupid_things.py intake --stdin < candidates.json
```

It prints what it added, what angles it took, what sightings it merged, and **what it refused
and why**. Read the refusals. A refill that produced eight candidates and had six refused as
rewords is a signal the scour went shallow, not a signal the script is broken.

Then commit, push, and create **one** Gmail draft summarizing what went in.

### 4. If the refill cannot reach 20

**Say so. Do not pad.** Ten honest entries beat twenty with filler, and filler in a bank is
worse than an empty slot because it looks like inventory. Report the real number and what was
searched. The next run picks it up.

## The email is a DRAFT, and a draft is not a delivery

Same as the take brief. The Gmail connector cannot send, only draft. So a refill leaves a draft
titled `Stupid Things bank refilled` sitting in D.J.'s drafts folder and nothing moves it to his
inbox.

- **A created draft is not proof D.J. read it.** The repo file is the artifact.
- **Replying to it does nothing.** There is no reply watcher on this routine.
- **A failed draft must be reported loudly**, never silently swallowed. The Gmail connector
  losing OAuth is the single most common failure across these routines, and it is exactly what
  caused the August 2026 walk-and-talk outage.

## When the routine does not run

No alarm on this one, by design. A bank that refills a week late costs nothing, and an alarm
nobody needs is how real alarms get ignored. Recovery is genuinely as good as the happy path:

1. `git pull`, then `python3 scripts/stupid_things.py health`.
2. If it says REFILL DUE, say **"stupid things refill"** in Claude Code and it does the same
   work the routine would have, live.
3. Check <https://claude.ai/code/routines> if it keeps missing.

## Failure modes worth knowing

**The bank says 20 available but half have `receipt: needed`.** That is normal and it is not a
bug. Availability counts angles, not readiness. `health` reports the split, and `pick` marks
every unsourced entry NEEDS RECEIPT. Sourcing happens at build time, where the number is fresh.

**Everything refused as a reword.** The scour found the same practices already in the bank. That
is what a mature bank looks like. The fix is not to loosen the threshold, it is to go looking
for new *angles* on entries already there, which is half the refill's job and the half that
gets skipped.

**An entry keeps getting picked and never built.** Probably `receipt: needed` on a practice
where no neutral source exists. Either retire it (`"status": "retired"`) or accept it ships
without a number, on the strength of the behavior alone.

## receipt-check: the gate, pointed backwards (2026-09-10)

```
python3 scripts/stupid_things.py receipt-check    # exit 0 = clean, exit 13 = a banked receipt would be refused
python3 scripts/tests/test_receipt_gate.py        # 25 cases, offline, no deps
```

On 2026-09-10 all 39 confirmed receipts were re-checked against their own cited
pages. **19 were false, 11 were partly wrong, 8 held.** Full findings:
[`../audits/2026-09-10-stupid-things-receipt-audit.md`](../audits/2026-09-10-stupid-things-receipt-audit.md).

Every failure was one of two moves, and both are now refused at intake by
`screen_receipt()`:

1. **The number came from someone selling something.** A receipt may only be born
   `confirmed` if its host is on `RECEIPT_SOURCE_ALLOW` -- associations,
   regulators, courts, statute, the portals' research desks, trade press, real
   research. Vendor and aggregator pages cannot carry a confirmed receipt. A host
   can be added deliberately (that is how the IRC got in), never by accident.
2. **The year was the year it was banked, not the year it was published.** A
   confirmed receipt must record `published`, the source's real publication date,
   and it must agree with `year`. A 2019 article banked as 2026 is refused.

A downgrade never deletes the number. The entry keeps it in `original_claim` with
the reason in `caution`, so the writer still knows the claim exists and still knows
exactly why it cannot be said flat.

**The caution list needs the same scepticism as the bank.** Five of the seven
`receipt_cautions` were recommending replacement figures that this audit
disproved. A list of known-bad numbers is only as good as the numbers it
recommends instead; re-check the `say_instead` fields whenever a receipt dies.
