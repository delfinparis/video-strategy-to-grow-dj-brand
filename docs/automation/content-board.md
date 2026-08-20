# The Notion Content Board

The board is at **[Content Board](https://www.notion.so/35037694472d47d9a5c8c34cfa95d9e4)**,
a database inside D.J.'s *DJ's Daily Operating System* page in Notion.

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
| Broker Problems | `docs/content-pillars.md` + a live receipt from web search |
| Stupid Things | `python3 scripts/stupid_things.py pick --count N` |
| Agent Spotlight | **mirrored** from `scripts/chicago-agent-spotlight/` — see below |
| KIRP Episode | **mirrored** from `scripts/podcast-promos/kir-*.md` — see below |

> **Broker Problems has no bank file.** The rows loaded on 2026-08-19 cite
> `brokerage-pain.md`, which does not exist in this repo and never did. Those
> pointers are phantom. Until a real bank exists, Broker Problems candidates
> must be sourced from `docs/content-pillars.md` plus a verified live receipt,
> and a row whose number cannot be sourced ships with the claim removed — not
> with the number and a shrug.

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
