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
```

`board.json` is the snapshot the routine exports from Notion before planning:

```json
[{"url": "...", "lane": "News", "status": "Open",
  "hook": "...", "expires": "2026-08-22", "has_body": false}]
```

`has_body` is true only when the page already contains a `## Script` heading.
An empty page, or a page holding only an angle, is `false`.

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
| Agent Spotlight | scout live per `docs/series/chicago-agent-spotlight-standard.md` |
| KIRP Episode | `python3 scripts/kirp_source.py --peek` |

> **Broker Problems has no bank file.** The rows loaded on 2026-08-19 cite
> `brokerage-pain.md`, which does not exist in this repo and never did. Those
> pointers are phantom. Until a real bank exists, Broker Problems candidates
> must be sourced from `docs/content-pillars.md` plus a verified live receipt,
> and a row whose number cannot be sourced ships with the claim removed — not
> with the number and a shrug.

---

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
   - **need** — add new rows per lane, each one created *with its body already
     written*. Run `check-hook` on every candidate hook before creating it; an
     exit 11 candidate is dropped, not reworded.
4. Report what changed in one short block. Email only on failure.

**The failure mode this system is built against:** a check confirms rows exist
and nothing confirms D.J. can actually film them. `health` returning 0 while a
row sits with an empty body is precisely that bug, which is why `has_body` is
part of the health check and not a separate nicety.
