# The Notion Content Board

The board is at **[Content Board](https://www.notion.so/35037694472d47d9a5c8c34cfa95d9e4)**,
a database inside the **Kale Recruitment Hub** page in Notion (moved there from
*DJ's Daily Operating System* on 2026-08-20; the id and URL are unchanged).

**What it is for, in one line:** D.J. opens a row and the finished script is
already sitting there, ready to film. Not a hook to build from later — the
whole thing.

That is the standard this doc exists to hold. A row with a good hook and an
empty body is a **failure**, not a partial success, and
`scripts/content_board.py health` fails the board for exactly that reason.

---

## Why the board is not just the briefs

The morning walk-and-talk brief is a *daily* surface: it rots by dinner, and if
D.J. is busy that day the options are gone. The lanes that are not news —
Takes, Broker Problems, Stupid Things, KIRP — have no reason to rot, and used to
have nowhere to wait. The board is the shelf they wait on.

It does not replace the walk-and-talk email chain
([`walk-and-talk-delivery.md`](walk-and-talk-delivery.md)). News still arrives
by email each morning and still gets built on demand. The board is where the
evergreen lanes accumulate, and where **every** lane ends up with a finished
script attached.

---

## Schema

| Column | What it holds |
|---|---|
| **Hook** (title) | The spoken scroll-stop line. This is what D.J. picks between. |
| **Lane** | News, Agent Tip, Agent Spotlight, Stupid Things Realtors Do, Broker Problems, Take, KIRP Episode |
| **Angle** | The reframe in one or two sentences — enough to pick from without opening the page. |
| **Heat** | Friction 1-5. Rule 9.2 allows one heat-4/5 video per week. |
| **Status** | Open → Picked → Filmed → Posted. Dead = expired or rejected, never deleted. |
| **Added** | When the row landed. |
| **Expires** | News and Agent Tip only. Evergreen lanes leave it empty and wait on the shelf. |

| **Last edited** | Auto-maintained by Notion, and **hidden from the default view**. Added 2026-08-20 so `week` can tell which slot a Picked/Filmed/Posted row spent. It is for the engine, not for picking. |

**There is deliberately no Source column and no Bank ref column.** D.J. removed
both on 2026-08-20: the board is a picking surface, and a picking surface with
seven columns is not one. Neither piece of information was lost — both moved
into the page body:

- the receipt lives under `## Data Source`, which is where the repo standard
  puts it anyway, and where the claim it backs is actually visible;
- the bank pointer lives in the one-line footer at the bottom of the body,
  emitted and parsed by `scripts/content_board.py footer`.

Do not add either column back. If you need them programmatically, read the body.

---

## The weekly grid: what the board owes each week

`TARGETS` is **shelf depth** -- how many rows wait in a lane. This is the other
question: how many of the week's videos each lane is allowed to become.

[`schedule/master-calendar.md`](../../schedule/master-calendar.md) carries 15
videos a week. D.J. cut gated Value Giveaways from 6 to 3 on 2026-08-19 to make
room for the three lanes that had no slot at all, so:

```
15 videos - 3 giveaways = 12 board-fed video slots a week
```

| Lane | Min/wk | Max/wk | Shelf target |
|---|---:|---:|---:|
| News | 2 | 2 | 3 |
| Agent Tip | 1 | 3 | 4 |
| Agent Spotlight | 1 | 2 | 2 |
| Stupid Things Realtors Do | 1 | 3 | 6 |
| Broker Problems | 1 | 3 | 4 |
| Take | 2 | 4 | 6 |
| KIRP Episode | 1 | 2 | 4 |
| **Sum** | **9** | **19** | |

**The maximums oversubscribe the week on purpose.** They sum to 19 against 12
slots. A range says what a lane is *allowed* to do in a good week, never what it
is entitled to. Minimums sum to 9, so **3 slots a week are genuinely
discretionary** -- and that number is why this is arithmetic in a script rather
than a judgment call at 5:30am.

```bash
python3 scripts/content_board.py week --board board.json
python3 scripts/content_board.py check-heat --board board.json --heat 4
```

`check-heat` is the Rule 9.2 guard: one heat-4-or-higher video across the whole
week. It exits **12** when the slot is already spent. A row under heat 4 always
exits 0, so the routine can call it unconditionally.

**Two changes came with the grid, and both are in the calendar file:** Agent
Spotlight was promoted out of substitute status and now owes 1 a week like
everything else, and Stupid Things and Agent Tip got the other two freed slots.
The tradeoff D.J. accepted, stated plainly: **the gate layer is the only thing on
the grid that asks a viewer to raise a hand**, so cutting giveaways 6 to 3 buys
variety with recruiting signal. Watch keyword volume for two cycles.

### Dating a spent slot, and why it is approximate

There is no "picked on" column, because D.J. stripped the board back to seven
columns on 2026-08-20 and adding one would walk that straight back. So `week`
reads `picked_on` if the snapshot carries one, and otherwise falls back to
Notion's **Last edited**, which is the hidden column added for exactly this.

**That fallback is an approximation and it is labelled as one in the output.** It
is right unless a row was edited again for some other reason after being picked,
which would move it into the wrong week. Two things follow:

- **`check-heat` is advisory**, and says so when it blocks. It never silently
  refuses work on the strength of a guess.
- **A row that has left Open with no date at all is NOT counted**, and `week`
  reports how many it skipped rather than quietly reporting a smaller number.
  Silence would make an under-filled week look like an on-track one, which is
  the same failure the walk-and-talk chain has already paid for twice.

### Exporting the snapshot

`week` and `check-heat` need `heat` and `last_edited`, which the older export
query did not select. The full one:

```sql
SELECT url,
       "Lane"   AS lane,
       "Status" AS status,
       "Hook"   AS hook,
       "Heat"   AS heat,
       "date:Expires:start" AS expires,
       substr("Last edited", 1, 10) AS last_edited
FROM "collection://6d781813-77d2-48b6-bb7b-a7bce63bcd29"
```

Both fields are optional in `load_board`, so an old snapshot still runs `plan`
and `health` unchanged -- it just degrades the week accounting, loudly.

## The split: what the script owns, what the routine owns

Same split as the Stupid Things bank
([`stupid-things-bank.md`](stupid-things-bank.md)), for the same reason.

`scripts/content_board.py` is **deterministic and offline**. It owns the
counting and the refusing:

- how many Open rows each lane has, and whether a refill is due
- which rows have passed their `Expires` date and must go Dead
- which live rows are missing a script body and must be filled
- whether a proposed hook is a reword of one already on the board

The **cloud routine** owns the judgment: researching the story, verifying the
receipt, and writing the four-pass v3. It has web search and the repo. It never
decides whether a refill is due — it reads the exit code.

```
python3 scripts/content_board.py health --board board.json
    Exit 0  = board stocked, every live row has a body. STOP.
    Exit 10 = work due. Continue.

python3 scripts/content_board.py plan --board board.json
    The work order as JSON: kill[], fill[], need{}, counts{}, seen_hooks[].

python3 scripts/content_board.py check-hook --board board.json --hook "..."
    Exit 0 = novel. Exit 11 = reword of a hook already live. Never bank it.

python3 scripts/content_board.py footer --lane Take --ref "sacred-cows.md #2"
    The exact footer line for the bottom of the page body.

python3 scripts/content_board.py cache-known
    Rows already known to have a body, so those pages are not fetched again.

python3 scripts/content_board.py cache-update --board board.json
    Fold the post-run snapshot back into the cache. Commit the result.
```

### Open vs Picked

Lane inventory counts **Open only**. A `Picked` row is still live — it can be
killed, and it still needs a body — but D.J. has already claimed it, so it is not
something he can choose. Counting Picked as inventory would let a lane where he
has claimed everything read as full and never refill, leaving him a board with
six Takes on it and nothing to pick.

### The body cache

Whether a page has a script can only be learned by fetching the page, and a
filled page never empties itself. `data/content-board-state.json` remembers the
answer, which turns roughly thirty full-script page fetches per run into zero.

The routine reads `cache-known` first and only fetches the pages it does not
already know about. After the run it calls `cache-update` and commits the file.

Two rules keep the cache honest:

- **Only a `true` is ever cached.** Caching a `false` would let a run that died
  halfway teach the cache that a row is permanently empty.
- **It expires after 7 days.** The one way this cache can be wrong is a body
  deleted by hand in Notion, which still reads as filled. A weekly full re-read
  catches it. A stale cache returns nothing rather than a stale yes: a slower
  run is fine, a blank row D.J. opens on set is not.

The file is also the only record of board state that lives outside Notion.

`board.json` is the snapshot the routine exports from Notion before planning:

```json
[{"url": "...", "lane": "News", "status": "Open", "hook": "...",
  "expires": "2026-08-22", "has_body": false, "ref": "news-briefs/2026-08-20.md #1"}]
```

`ref` is the bank pointer read back out of the page footer, or `null`. It is how
the mirror lanes below know a committed script is already on the board.

`has_body` is true when the page carries **any** heading from
`python3 scripts/content_board.py body-markers`:

```
## Script            board-native rows
## Spoken Script     podcast promos
## Full Script       Chicago spotlights
```

The series have never agreed on one heading. Checking only for `## Script` would
mark every mirrored row empty and rewrite a good script on top of itself.

---

## Lane targets

Sized off the 15-videos-a-week plan in `CLAUDE.md`, so the board holds roughly
two weeks of runway. News is deliberately shallow, because it rots.

| Lane | Target Open | Refill at | Expires after |
|---|---|---|---|
| News | 3 | ≤2 | 3 days |
| Agent Tip | 4 | ≤2 | 7 days |
| Take | 6 | ≤3 | never |
| Broker Problems | 4 | ≤2 | never |
| Stupid Things Realtors Do | 6 | ≤3 | never |
| Agent Spotlight | 2 | ≤1 | never |
| KIRP Episode | 4 | ≤2 | never |

Where candidates come from:

| Lane | Source |
|---|---|
| News, Agent Tip | `data/news-briefs/<today>.md` |
| Take | `data/take-briefs/<latest>.md`, `data/sacred-cows.md` |
| Broker Problems | `data/brokerage-pain.md` (22 entries), plus a re-verified receipt |
| Stupid Things | `python3 scripts/stupid_things.py pick --count N` |
| Agent Spotlight | **mirrored** from `scripts/chicago-agent-spotlight/` — see below |
| KIRP Episode | **mirrored** from `scripts/podcast-promos/kir-*.md` — see below |

> **Correction, 2026-08-20. The Broker Problems bank is real.** An earlier
> version of this note said `brokerage-pain.md` "does not exist in this repo and
> never did" and called the pointers phantom. It exists: 22 entries, written
> 2026-08-18 alongside
> [`../series/broker-problems-standard.md`](../series/broker-problems-standard.md)
> and [`../strategy/2026-08-18-why-agents-leave.md`](../strategy/2026-08-18-why-agents-leave.md).
> All three sat **uncommitted** in one machine's working tree for two days, so a
> second machine could not see them and read the absence as a fact. They are
> committed now.
>
> The lesson is the one this repo keeps relearning from the other direction: **a
> file you cannot see is not a file that does not exist.** Across three machines,
> `git fetch` and a look at the other device's working state come before
> concluding anything is missing. The original note was right about one thing and
> it still stands: a row whose number cannot be sourced ships with the claim
> removed, never with the number and a shrug.
>
> Build rules for the lane live in the standard, and the seed that converts is
> **"I have never once checked whether this is normal,"** never "my brokerage is
> bad." Never mention Kale. Heat 5 is banned outright.

---

## The two mirror lanes: Agent Spotlight and KIRP Episode

These two lanes are **not researched here**, and adding research for them would
be a mistake. Both already have a producing routine that does the scouting and
commits a finished walk-and-talk to this repo:

| Lane | Producing routine | Lands in |
|---|---|---|
| Agent Spotlight | `trig_01Fr5tCSZnfhxSXtSPEcCVhe` — Weekly Chicago Agent Spotlight, Mon 6am CT | `scripts/chicago-agent-spotlight/<agent>-<date>.md` |
| KIRP Episode | `trig_01S1nWLHuJ3jYLg7BzyC9Kaf` — Daily KIR episode → walk-and-talk promo, 7am CT | `scripts/podcast-promos/kir-<guest>-<date>.md` |

So the board **mirrors the committed file** rather than scouting the same agent
or guest a second time. If the board did its own research here, two routines
would pick two different Chicago agents in the same week and D.J. would have to
work out which one was real.

```
python3 scripts/content_board.py mirror --board board.json
```

For each mirror lane it reports what is on the board, how much room is left to
target, how many committed scripts are not on the board yet, the parsed rows to
post (newest first, by the date in the filename), and how many it held back.

Each parsed row gives you the whole thing:

- **Hook** — the first line D.J. actually says, taken from under the script
  heading, past any `**HOOK (0:00-0:08)**` beat label. Not the frontmatter title
  and not the H1: neither of those is what stops a scroll.
- **Angle** — the file's `> **WOW:**` note, which is already a one-line statement
  of why the script exists.
- **Heat** — 2. Both lanes are amplification plays, not friction plays.
- **Body** — the file at `body_path`, posted as the page body.
- **Expires** — empty. A promo and a spotlight both keep.

**The repo path is the dedupe key**, not the hook text, and it is matched against
rows at *every* status — on **basename**, not the full path. The ref is read back
out of a footer a model wrote, and one that says `podcast-promos/x.md` instead of
`scripts/podcast-promos/x.md` is not a new episode. Exact path matching would
call it one and post a duplicate. An episode already Posted can never reappear as a new
row. This is stronger than `check-hook`, so mirror rows skip that check.

**Post the file as-is.** Do not re-run the four passes on a mirrored script —
its producing routine already ran its own standard, the spotlight carries
`## Verified Tags` and a post-publish DM that the board template has no slot for,
and rewriting it would silently fork the script from the file D.J.'s other
tooling reads. Mirror lanes are the one exception to the body template below.

**A held-back script is not a lost one.** It waits in the repo and gets mirrored
when a row ahead of it goes Posted. That is the point of the shelf.

## The page body: what "ready to film" means

Every row's body is the **final v3**, built through the same four passes as any
walk-and-talk ([`walk-and-talk-on-demand.md`](walk-and-talk-on-demand.md)):
draft → stress-test (Story Pass first) → EP-polish → council review. The passes
run silently. Only v3 lands on the page.

The body is, in order:

1. A callout line carrying `hook_family`, `pattern_interrupt`, `story_format`,
   and target length. (Notion has no frontmatter; this is the frontmatter.)
2. `## Script` — `### HOOK (0:00-0:03)`, `### STORY`, `### PAYOFF`, each with
   its production note. The HOOK opens with the standalone **spoken**
   scroll-stop line, per CLAUDE.md. Never a manual text overlay.
3. `## Data Source` — every claim with a named source, a date, and a URL. This
   is the receipt, and it is the reason there is no Source column.
4. `## AI Music Prompt` — `**Vibe:**` plus the CapCut prompt, ≤300 characters.
5. `## Social Media` — all five captions with hashtags at the per-platform caps
   from `docs/caption-and-hashtag-strategy.md`. No em dashes, no AI-speak.
6. `## Council Review` — 2-3 tested spoken scroll-stop variants mapped to hook
   families, the one-line why-it-works, and the single dissent to A/B next.
7. The footer line from `content_board.py footer`.

**A news row's claims are re-verified at write time, every time.** A body
written three days ago against a number that has since been revised is worse
than an empty page, because it reads as checked.

**Never invent a figure.** If a receipt cannot be found, the claim comes out of
the script. `receipt.status = "needed"` is a valid outcome in the Stupid Things
bank and the same rule applies here.

---

## The routine

**Content Board refill** runs daily at 8:10am CT (`10 13 * * *` UTC). It has the
Notion connector and this repo.

1. `git pull`, export the board snapshot from Notion to `board.json`.
2. `python3 scripts/content_board.py health --board board.json`. **Branch on the
   exit code, not the prose.** Exit 0 = stop, report one line, no writes.
3. On exit 10, run `plan`, then in this order:
   - **kill** — set every row in `kill[]` to Status `Dead`. Never delete a row.
   - **fill** — for every row in `fill[]`, write the full v3 body. This comes
     first among the writes: a row already on the board that D.J. might open
     today matters more than a row that does not exist yet.
   - **mirror** — run `content_board.py mirror` and post every row in each
     lane's `post[]`, using the file at `body_path` as the page body, unchanged.
     This runs before `need`, because it costs no research.
   - **need** — `check-hook` scans **every** status, not just the live ones, so
     a hook D.J. already Posted cannot come back as a fresh row. It is tuned to
     over-reject: a false DUPE costs one candidate the routine can replace, a
     false NOVEL puts a repeat in front of D.J. Log every dropped candidate.
   - **need** — add new rows per lane, each one created *with its body already
     written*. Run `check-hook` on every candidate hook before creating it; an
     exit 11 candidate is dropped, not reworded. Agent Spotlight and KIRP
     Episode never appear here — `mirror` owns them.
4. Report what changed in one short block. Email only on failure.

**The failure mode this system is built against:** a check confirms rows exist
and nothing confirms D.J. can actually film them. `health` returning 0 while a
row sits with an empty body is precisely that bug, which is why `has_body` is
part of the health check and not a separate nicety.
