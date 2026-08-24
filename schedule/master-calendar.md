# Master Content Calendar

**Current as of 2026-08-19.** This is the day-by-day grid that [`../docs/content-pillars.md`](../docs/content-pillars.md) points at. It assigns every weekly slot to a day, names the category, and states the gate. It does **not** name scripts -- scripts get picked into these slots each week from the briefs and banks listed in [What feeds each slot](#what-feeds-each-slot).

Governing docs, in precedence order when they conflict:

1. [`../docs/strategy/2026-07-21-goal-reset-and-gate-layer.md`](../docs/strategy/2026-07-21-goal-reset-and-gate-layer.md) -- goals and the gate layer
2. [`../docs/content-pillars.md`](../docs/content-pillars.md) -- pillar definitions
3. [`../docs/series/take-standard.md`](../docs/series/take-standard.md) and [`../docs/series/carousel-standard.md`](../docs/series/carousel-standard.md) -- per-series rules
4. This file -- which day each slot lands on

---

## The cadence: 29 posts a week

**15 videos + 14 carousels. 5 gated, 24 open. Sunday is carousel-only.**

| Surface | Per week | Gated |
|---|---:|---:|
| Videos | 15 | 3 |
| Carousels | 14 | 2 |
| **Total** | **29** | **5** |

> **Changed 2026-08-19.** Gated Value Giveaways went from 6 videos a week to 3, and the
> three freed slots went to the lanes that had no slot at all: Stupid Things Realtors Do,
> Agent Tip, and Chicago Agent Spotlight (promoted out of substitute status). D.J.'s call,
> made with the tradeoff stated: **the gate layer is the only thing on the grid that asks a
> viewer to raise a hand**, so this buys variety with recruiting signal. Watch keyword
> volume in [`../data/keyword-registry.md`](../data/keyword-registry.md) for two cycles; if
> hand-raises fall off a cliff, the fourth giveaway comes back out of the discretionary pool.
>
> Which slot each of those categories fills is now decided by the
> [Content Board](../docs/automation/content-board.md), not by this file. The calendar names
> the category; the board names the row.

> **Note on the carousel number.** [`../docs/content-pillars.md`](../docs/content-pillars.md) still says 5 carousels and a 20-post week. That figure predates the 2026-08-07 move to a 14-a-week, two-a-day carousel grid (`d82abb7`), which [`../docs/series/carousel-standard.md`](../docs/series/carousel-standard.md) documents and the four carousel routines already run. 14 is what is actually shipping; content-pillars needs the correction.

---

## The week at a glance

| Day | Video 1 | Video 2 | Video 3 | Carousel 1 | Carousel 2 | Posts |
|---|---|---|---|---|---|:--:|
| **Mon** | Take | KIRP promo | Giveaway: say this 🔒 | KIRP episode | Take 🔒 | 5 |
| **Tue** | News / IIR | Broker Problem | Stupid Things | Broker-problem compare | News / tip | 5 |
| **Wed** | Take (heat 4.5-5) | News / IIR | Agent Tip | KIRP episode | Take | 5 |
| **Thu** | Broker Problem | KIRP promo | Agent Spotlight | News / tip | News / tip 🔒 | 5 |
| **Fri** | Take | Giveaway: AI prompt 🔒 | -- | KIRP episode | Take | 4 |
| **Sat** | Giveaway: tool use-case 🔒 | -- | -- | News / tip | News / tip | 3 |
| **Sun** | -- | -- | -- | News / tip | News / tip | 2 |

🔒 = gated (ManyChat keyword on Instagram and Facebook only, never LinkedIn)

**Weekly totals check:** Takes 3 · News 2 · Broker Problems 2 · KIRP promos 2 · Giveaways 3 (1 say-this + 1 tool + 1 prompt) · Stupid Things 1 · Agent Tip 1 · Agent Spotlight 1 = **15 videos**. KIRP carousels 3 · Take carousels 3 · Broker-problem carousel 1 · News/tip carousels 7 = **14 carousels**.

Twelve of those 15 videos are **fed by the board**; the 3 giveaways are not. Lane minimums
account for 9 of the 12, which leaves **3 discretionary slots a week**. Run
`python3 scripts/content_board.py week --board board.json` for the live count — that arithmetic lives in the
script, not in this table, because a number maintained in two places drifts.

---

## Day by day

### Monday -- 5 posts

| Slot | Category | Gate | Fed by | Post window (CT) |
|---|---|---|---|---|
| Video | **The Take** (heat 4-4.3) | none | Sunday take brief, `data/take-briefs/` | LI 2-5pm, IG 12-6pm, FB 5-8pm |
| Video | **KIRP promo** | none | Hype Machine, `scripts/podcast-promos/` | midday |
| Video | **Giveaway: "say this, not that"** | 🔒 keyword | purpose-built doc per tip | IG/FB midday-evening |
| Carousel | **KIRP episode** | none | 8:00am routine | mid-morning |
| Carousel | **Take** | 🔒 keyword | 9:00am routine, same bank entry as the take video | afternoon |

Monday's take and take carousel work the **same** [`sacred-cows.md`](../data/sacred-cows.md) entry -- one verification pass, two surfaces, different hook families. The video claims its hook family first.

### Tuesday -- 5 posts

| Slot | Category | Gate | Fed by | Post window (CT) |
|---|---|---|---|---|
| Video | **News / Inside the Industry** | none | 5:30am walk-and-talk brief | LI 2-5pm (strongest day of the week) |
| Video | **Broker Problem** | none | [brokerage-pain bank](../data/brokerage-pain.md) | FB 5-8pm (74% Chicago) |
| Video | **Stupid Things Realtors Do** | none | [Content Board](../docs/automation/content-board.md), **Stupid Things Realtors Do** lane | IG/FB midday |
| Carousel | **Broker-problem comparison** | none | Tue 8:00am routine | mid-morning |
| Carousel | **News / tip** | none | Tue 7:05am routine (1 on Tuesdays) | early |

**Comment duty:** someone reads every comment on the Broker Problem video and flags Chicago complainers into Close for Ana/Jennica. That is the recruiting mechanic for this pillar -- the video does reach, the comments do recruiting.

### Wednesday -- 5 posts

| Slot | Category | Gate | Fed by | Post window (CT) |
|---|---|---|---|---|
| Video | **The Take -- heat 4.5-5** | none | Sunday take brief | LI 2-5pm |
| Video | **News / Inside the Industry** | none | 5:30am walk-and-talk brief | midday |
| Video | **Agent Tip** | none | [Content Board](../docs/automation/content-board.md), **Agent Tip** lane | IG/FB midday-evening |
| Carousel | **KIRP episode** | none | 8:00am routine | mid-morning |
| Carousel | **Take** | none | 9:00am routine | afternoon |

**Wednesday is the week's hardest swing, not its only hot one.** D.J. raised the floor and then opened the ceiling on 2026-08-20: Rule 9.2 is a **band of 4 to 5** across the whole schedule with the body of work **averaging 4.3-4.5**, so there is no single friction slot left for series to compete over. Wednesday runs 4.5-5; Monday and Friday run 4 to 4.3.

**Heat 5 (naming a person, brokerage, coach, or product) is permitted and priced, not banned.** The governing number is the average, so a 5 needs 4.0s around it. Run `python3 scripts/content_board.py check-heat --board board.json` to see where the week actually sits — it says plainly when the schedule is running hot.

### Thursday -- 5 posts

| Slot | Category | Gate | Fed by | Post window (CT) |
|---|---|---|---|---|
| Video | **Broker Problem** | none | [brokerage-pain bank](../data/brokerage-pain.md) | FB 5-8pm |
| Video | **KIRP promo** | none | Hype Machine | midday |
| Video | **Chicago Agent Spotlight** | none | [Content Board](../docs/automation/content-board.md), **Agent Spotlight** lane (mirrored from `scripts/chicago-agent-spotlight/`) | IG/FB midday-evening |
| Carousel | **News / tip** | none | 7:05am routine | early |
| Carousel | **News / tip** | 🔒 keyword | 7:05am routine, keyword matched to **Friday's** AI-prompt giveaway (Thursday no longer carries a giveaway video) | afternoon |

Same comment duty as Tuesday on the Broker Problem video.

### Friday -- 4 posts

| Slot | Category | Gate | Fed by | Post window (CT) |
|---|---|---|---|---|
| Video | **The Take** (heat 4-4.3) | none | Sunday take brief | LI 2-5pm |
| Video | **Giveaway: AI prompt** | 🔒 keyword | the 700-prompt vault, tapthis.co | IG/FB midday |
| Carousel | **KIRP episode** | none | 8:00am routine | mid-morning |
| Carousel | **Take** | none | 9:00am routine | afternoon |

### Saturday -- 3 posts

| Slot | Category | Gate | Fed by | Post window (CT) |
|---|---|---|---|---|
| Video | **Giveaway: tool use-case** | 🔒 keyword | evergreen, pulled from the can | IG/FB midday |
| Carousel | **News / tip** | none | 7:05am routine | morning |
| Carousel | **News / tip** | none | 7:05am routine | afternoon |

Saturday's video is deliberately the **evergreen** giveaway, filmed in a weekday batch session. No filming happens at the weekend, so this slot must always come out of the buffer.

### Sunday -- 2 posts

| Slot | Category | Gate | Fed by | Post window (CT) |
|---|---|---|---|---|
| Carousel | **News / tip** | none | 7:05am routine | morning |
| Carousel | **News / tip** | none | 7:05am routine | afternoon |

**No video on Sunday.** Sunday is the planning day: the 7:00am take-brief routine writes next week's take options, and the week's slots below get filled in.

---

## What you film

Of the 29 posts, **D.J. is on camera for 15**. All 14 carousels are built by routines before he wakes up. Only the two news videos are genuinely same-day; everything else batches.

| Session | When | Count | What |
|---|---|:--:|---|
| **Batch A** | Mon | 9 | The week's 3 takes, 2 broker problems, 2 KIRP promos, 1 Stupid Things, 1 Agent Tip. All pulled off the [Content Board](../docs/automation/content-board.md) Monday morning. Nothing time-sensitive, so one session covers Mon-Fri |
| **Batch B** | Wed or Thu | 3 | The three giveaways for **next** week. This is the batch that keeps the can full, and the only reason Saturday has a post and a bad week still ships |
| **Same-day** | Tue, Wed, Thu | 3 | Two news walk-and-talks off that morning's 5:30am brief, plus Thursday's Spotlight. These cannot be filmed ahead: news has to land inside 24 hours, and a Spotlight is only worth posting while its subject is actually in the news |

**Total filming is unchanged at 15**, and Batch B got smaller. Batch A absorbed the two new
evergreen lanes because they come off a shelf that is already stocked on Monday.

| Day | On camera | Posts | Already built |
|---|---|---|---|
| **Mon** | Batch A, 9 videos for the week | Take, KIRP promo, giveaway | KIRP deck 8:00a, take deck 9:00a |
| **Tue** | News, same day off the 5:30a brief | News, broker problem, Stupid Things | News deck 7:05a, broker deck 8:00a |
| **Wed** | News, same day. Batch B if not Thu | Take (heat 4.5-5), news, Agent Tip | KIRP deck 8:00a, take deck 9:00a |
| **Thu** | Spotlight, same week. Batch B, next week's 3 giveaways | Broker problem, KIRP promo, Spotlight | Two news decks 7:05a |
| **Fri** | nothing | Take, giveaway | KIRP deck 8:00a, take deck 9:00a |
| **Sat** | nothing | Giveaway, from the can | Two news decks 7:05a |
| **Sun** | nothing | nothing | Two news decks 7:05a. Take brief lands 7:00a -- pick next week's three |

**First hour on every post:** reply to every comment, and pin a value-extending first comment (the script, the next step, the receipt). Never a "follow me." Creator replies are weighted for distribution; this is Rule 10.4-10.6 and it outperforms anything in the script.

---

## The categories

| Category | What it is | Gate | Judged on | Standard |
|---|---|---|---|---|
| **Giveaway: "say this, not that"** | The exact words for one high-stakes moment, said on camera; the deeper doc is gated | 🔒 IG/FB | Leads (comments → Close) | [content-pillars](../docs/content-pillars.md#pillar-1-value-giveaways-the-lead-engine) |
| **Giveaway: tool use-case** | One use case for an existing tapthis.co tool, framed by the *use case* never the tool | 🔒 IG/FB | Leads | same |
| **Giveaway: AI prompt** | One vivid prompt result; the 700-prompt vault is the artifact | 🔒 IG/FB | Leads | same |
| **The Take** | "Realtors shouldn't do X, do Y instead." Five beats: the cow → who profits → the receipt → the swap → loop-back | never | Reach + argument in the comments | [take-standard](../docs/series/take-standard.md) |
| **News / Inside the Industry** | Sharp take on industry news within 24h, Chicago angle where possible. The 2 best stories, not every story | never | Reach + authority | [inside-the-industry-standard](../docs/series/inside-the-industry-standard.md) |
| **Broker Problem** | One normalized pain in the agent's arrangement with their *current* brokerage. Three rotating flavors: Slow Leak, Doesn't Make Sense, the Silence. Close hands over a look, never a leave. Never mentions Kale | never | Reach + Chicago comment signal | [broker-problems-standard](../docs/series/broker-problems-standard.md) |
| **KIRP promo** | Walk-and-talk promo for a recent episode | never | Podcast listeners | [podcast-promo-hype-machine](../docs/series/podcast-promo-hype-machine.md) |
| **Stupid Things Realtors Do** | One named bad behavior and the exact fix. Runs again on a genuinely new angle on the *solution*, never a reworded one | never | Reach + comment argument | [stupid-things bank](../data/stupid-things.md) |
| **Agent Tip** | One usable number or move, said plainly. The `[STAT]` track in the morning brief, finally named as its own lane | never | Saves + sends | [content-pillars](../docs/content-pillars.md) |
| **Chicago Agent Spotlight** | One Chicago agent currently in the news, tagged with a verified handle and an IG Collab. Promoted out of substitute status 2026-08-19 and now owes 1 a week | never | **Reshares + new Chicago followers, never saves** | [spotlight-standard](../docs/series/chicago-agent-spotlight-standard.md) |
| **Carousel: KIRP episode** | Saveable takeaways from an episode | never | Saves + sends | [carousel-standard](../docs/series/carousel-standard.md) |
| **Carousel: Take** | The receipt for that day's take, laid out to be saved | varies | Saves + sends | same |
| **Carousel: Broker-problem compare** | Side-by-side brokerage-economics comparison | never | Saves + sends | same |
| **Carousel: News / tip** | News repurpose or evergreen tip / checklist / data card | varies | Saves + sends | same |

---

## Surfaces

Videos crosspost to all six retained surfaces: **LinkedIn personal, Facebook personal, Facebook business, Instagram personal, TikTok business, YouTube business.** Carousels run **Instagram and Facebook**, plus LinkedIn with the tagged joinkale link in the first comment.

**LinkedIn caps at roughly one post per 12 hours.** On a 5-post day that means LinkedIn takes the day's strongest video plus at most one carousel. Everything else still ships to the other surfaces. Do not stack three LinkedIn posts in a day to hit a number.

Gated posts carry a ManyChat keyword on **Instagram and Facebook only**. Never on LinkedIn -- LinkedIn downranks comment-bait and bans comment-to-DM automation. Every keyword is registered in [`../data/keyword-registry.md`](../data/keyword-registry.md) and is **passed to Loomly verbatim**; a reworded keyword silently destroys that post's leads.

---

## The six-week cycle overlay

Tool launches and event promos come **out of** the giveaway slots, not on top of them. Volume stays at 15 and 14.

> **Tighter since 2026-08-19.** With 3 giveaway slots instead of 6, a launch week and an
> event week now consume most of the gated inventory rather than a third of it. On weeks 5-6
> the event *is* the giveaway layer. If a cycle needs more gated surface than 3 slots hold,
> take it from the **discretionary** board slots and say which lane gave way -- do not quietly
> run 16 videos.

| Week | What changes | Giveaway slots |
|---|---|---|
| 1 | **Tool launch** (`/sound-like-you` first, then `/prospecting`, then `/stacks`) | evergreen use cases |
| 2-3 | nothing | evergreen use cases |
| 4 | **Event announce** (`WEBINAR` keyword) | evergreen use cases |
| 5 | Event: teach one piece, gate the seat | reduced |
| 6 | Event: last call, webinar runs | reduced |

---

## Substitutions and the cut order

**Chicago Agent Spotlight now holds Thursday's third slot** rather than substituting into
someone else's. As a substitute it ran rarely and unpredictably, which is a poor way to run
the one category judged on reshares and new followers. If no worthy Chicago subject exists in
a given week, the slot goes back to the discretionary pool -- run
`content_board.py week --board board.json` and spend it on whichever lane has room above its minimum. **Do not
film a Spotlight about a thin subject to fill the slot.** An empty slot is reported as empty;
this grid has never invented a post to fill itself.

**When the week is too heavy, cut in this order:**

0. The three discretionary slots go first -- that is what they are for. `content_board.py week --board board.json`
   names them, and cutting them costs nothing, because every lane still clears its minimum
1. Takes drop from 3 to 1 -- **keep Wednesday**, the 4.5-5 slot doing the distinctive work
2. Carousels 14 → 7 (one a day)
3. Videos 15 → 12

Takes cut first because they are the newest lane and the least attributable, not the least valuable. **A half-researched take is worse than no take** -- the receipt is the whole defense when the comments arrive.

**The 3-pass rigor (draft → stress-test → EP-polish) is non-negotiable on every video.** If a week cannot clear 29 posts at that bar, ship fewer. A skipped slot costs nothing; a 2-pass filler post costs brand.

### Minimum-viable week

When D.J. is travelling, sick, or slammed, **four posts always ship: 2 News + 2 Giveaways.** Everything else is optional that week.

---

## What feeds each slot

| Input | When | Output | Feeds |
|---|---|---|---|
| Morning Walk & Talk Research routine | 5:30am CT daily | Gmail draft → sent ~6:15am by Apps Script | News videos, Broker Problems, giveaway ideas |
| `scripts/news_brief.py` | daily | `data/news-briefs/YYYY-MM-DD.md` | News videos, news-repurpose carousels |
| Walk & Talk Watchdog | 6:50am CT daily | alarm if no brief was **delivered** | reliability of the above |
| Take Brief routine | **Sun 7:00am CT** | `data/take-briefs/YYYY-MM-DD.md`, 5-7 vetted options | all 3 takes + all 3 take carousels |
| News / tip carousel routine | Tue/Thu/Sat/Sun 7:05am | 2 decks (1 on Tue) | 7 news/tip carousels |
| KIRP episode carousel routine | Mon/Wed/Fri 8:00am | 1 deck | 3 KIRP carousels |
| Broker-problem carousel routine | Tue 8:00am | 1 deck | 1 broker carousel |
| Take carousel routine | Mon/Wed/Fri 9:00am | 1 deck | 3 take carousels |
| `scripts/podcast-promos/build_promo_brief.py` | on episode drop | promo brief | 2 KIRP promo videos |
| `scripts/growth_digest.py` | weekly | `data/growth-digests/YYYY-Www.md` | how to make and distribute better, not what to post |

**Filming reality:** D.J. films on weekdays, in 2-3 batch sessions, and keeps **one week of evergreen giveaways in the can**. That buffer is what makes Saturday's slot and the minimum-viable week possible without D.J. being a single point of failure.

**Sunday ritual:** take brief lands at 7:00am, then fill next week's slots, then run the recruiting-funnel review in [`../docs/analytics/recruiting-funnel-dashboard.md`](../docs/analytics/recruiting-funnel-dashboard.md).

**Everything logs to [`../data/publishing-log.csv`](../data/publishing-log.csv).** The YouTube auto-sync backfills it, but auto-match failures land as `REVIEW-no-match` rows and need a human pass.

---

## History

- **Feb 23 - Apr 18, 2026:** 6 posts/week. AI Agent Minute (M/W/F) + Agent Tip of the Day (T/Th/Sa). Both series now frozen.
- **Apr 20 - Jul 18, 2026:** 6 posts/week, Inside the Industry primary. Reliable machine, **zero** recruiting conversations, because nothing asked for a hand-raise. See [`../docs/analytics/2026-07-19-pivot-results.md`](../docs/analytics/2026-07-19-pivot-results.md).
- **Jul 22, 2026:** goal reset and the gate layer. 12 videos + 5 carousels.
- **Aug 7, 2026:** carousels to a 14-a-week, two-a-day grid.
- **Aug 10, 2026:** The Take added, 3 videos a week, paired to the existing take carousels.

The pre-pivot week-by-week record is in [`weekly-breakdown.md`](weekly-breakdown.md) (historical only).

---

*Grid written 2026-08-11 | Cadence: 15 videos + 14 carousels | Next review: week-4 quality checkpoint*
