# The weekly mix, and the realtor-tip engine: tips over news

Decision doc, 2026-09-09. Follows [`2026-09-08-brand-tax-register.md`](2026-09-08-brand-tax-register.md)
by one day and resolves the open Friday-slot question it left.

---

## What D.J. asked for, in his words

> "I also want to build a 'do this, don't do that' real estate agent tip engine. I'm getting the
> similar walk and talk news stories every day and want to adjust that. Let's do more realtor
> tips (mistakes agents make - do X instead) and less news."

And, an hour later, the weekly recipe:

> "Let's do 2-3 podcast episode promos, 3-4 realtor tips, 2-4 news stories, and 3 'seeding doubt
> about their current brokerage.'"

---

## The finding: the tip engine already existed and nothing was drawing from it

The **Stupid Things Realtors Do** lane is, by its own charter, "a specific thing agents do that
is bad for the client or the deal, and the exact thing to do instead." That is the tip engine.
On 2026-09-09 its bank held **69 practices, 60 available, 33 with a confirmed receipt**, each
carrying a pre-written scene, a swap, and in many cases a spoken hook. One script had ever been
built from it (STUPID-001), and the lane had one slot a week.

Meanwhile the daily walk-and-talk brief, the thing D.J. actually films from, was news by
construction: the 5:30am routine researched the last 48 hours and offered 5-8 news options, with
a stat as the fallback and a take on Mon/Wed/Fri. Nothing in the daily path ever touched the tip
bank. So D.J. saw the same kind of news option every morning and a bank of sixty tips sat unread.

**The fix is a re-pointing, not a new lane.** The daily brief now leads with tips from that bank.
The reply-to-script generator learns to build one. The weekly grid carries the mix D.J. named.

---

## The weekly mix (D.J., 2026-09-09)

| Lane | Per week | Fed by |
|---|---|---|
| **Podcast episode promos** (KIRP) | **2-3** | Daily KIR routine, mirrored to the board |
| **Realtor tips** (Stupid Things bank; takes and guest tips count) | **3-4** | Daily brief `[TIP]` options, on-demand "stupid things" |
| **News** | **2-4** | Daily brief `[NEWS]` options, at most 2 a day |
| **Broker Problems** | **3** | Sunday engine, Tue/Thu/Fri |

That is **10-14 board-fed videos a week.** The gated Value Giveaways were not in D.J.'s list;
asked, he said "let's still offer them, maybe 1-2 a week" (2026-09-09). So they drop from 3 to
1-2 (Monday say-this, Friday alternating AI prompt and tool use-case) and the week is 11-16
videos, written to 14.

**What gave way.** The Take lane's three standalone slots. A take is a realtor tip with a
who-profits beat, so takes now arrive as `[TIP]` options and count toward the 3-4. The Sunday
take-brief routine keeps running as a source; its slots are gone. That also closes the question
the brand-tax doc left open: the third Broker Problem on Friday does not need a 16th video, it
takes one of the take's old slots. **The week is back to 15.**

**What was not touched.** Agent Tip of the Day (guest-sourced) counts toward the tip quota when
one runs, and Chicago Agent Spotlight stays a substitute.

## The grid

| Day | Video 1 | Video 2 | Video 3 |
|---|---|---|---|
| **Mon** | Realtor tip | KIRP promo | Giveaway: say this 🔒 |
| **Tue** | News | Broker Problem | Realtor tip |
| **Wed** | Realtor tip | News | -- |
| **Thu** | Broker Problem | KIRP promo | News (optional) |
| **Fri** | Broker Problem | Realtor tip (optional 4th) | Giveaway: AI prompt or tool use-case 🔒 (optional 2nd) |
| **Sat** | KIRP promo (optional 3rd) | -- | -- |
| **Sun** | News (optional 4th) | -- | -- |

Minimums: tips 3, news 2, KIRP 2, BP 3 = 10 board-fed. Maximums 14. `content_board.py week`
carries the same numbers and says which minimums are still owed.

---

## What changed in the machine

1. **The daily brief leads with tips.** The Morning Walk & Talk Research routine now runs
   `python3 scripts/stupid_things.py pick --count 6 --stdout` first and offers **2-3 `[TIP]`
   options at the top of the email**, then **at most 2 `[NEWS]` options** that clear the 48-hour
   rule, then the `[STAT]` fallback if needed. The Mon/Wed/Fri take is a `[TIP]` with a
   who-profits line. Five to six options total, tips first.
2. **The reply generator builds tips.** `scripts/apps-script/walk-and-talk-project.gs` detects a
   `[TIP]` pick and builds to the realtor-tip standard: series `Stupid Things Realtors Do`, the
   four beats mapped onto the clock, `bank_id` and `bank_angle` in frontmatter. D.J. pasted the
   updated file into the Apps Script project on 2026-09-09.
3. **The local brief carries the same tips.** `scripts/news_brief.py` writes a "Realtor tips"
   section above the news candidates and defaults to three news takes instead of five.
4. **The bank gets logged from the email path.** The Sunday Stupid Things Bank Check routine now
   reads the week's Walk & Talk threads, finds generated scripts carrying `bank_id`, and runs
   `stupid_things.py log` for each, so an angle built by email leaves the pool.
5. **The series standard exists.** [`../series/stupid-things-standard.md`](../series/stupid-things-standard.md),
   which the lane never had.
6. **The grid.** `schedule/master-calendar.md`, `scripts/content_board.py`, `CLAUDE.md`, and
   `docs/content-pillars.md` carry the mix above.

## Two flags for D.J.

- **The gated giveaways.** Resolved same day: 1-2 a week, not 3.
- **Two reply generators are live.** The Apps Script builds the script when D.J. replies and
  labels the thread `WT-Scripted`. A separate hourly cloud routine ("Walk & Talk Reply → Script")
  also watches the same threads with its own label and an older three-pass prompt. It now stops
  when it sees the Apps Script's label, so it cannot double-reply; the cleaner fix is to disable
  it at https://claude.ai/code/routines once the Apps Script path is trusted.
