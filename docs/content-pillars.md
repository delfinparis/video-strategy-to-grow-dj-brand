# Content Pillars

This document defines the strategic structure of D.J. Paris's **short-form video** content. It was reset on 2026-07-21 alongside the goal reset and gate layer, and the pillar definitions were refined on 2026-07-22 against a single test question (below). Read [`strategy/2026-07-21-goal-reset-and-gate-layer.md`](strategy/2026-07-21-goal-reset-and-gate-layer.md) first; this file is the pillar-level detail under that decision.

Carousels are a parallel surface with their own standard ([`series/carousel-standard.md`](series/carousel-standard.md)); they are not pillars and are not covered here.

## The one thing (brand spine)

> **D.J. Paris tells real estate agents exactly what to do and say to grow their business.**

Every pillar ladders under that one promise instead of competing with it. The "do and say" content (scripts, tools, prompts) *is* the promise. News and KIRP are the credibility that makes it believable, not co-equal pillars. Broker Problems is the recruiting edge. When a pillar or a script does not obviously serve "what to do and say to grow," question whether it belongs.

The April 2026 four-pillar model (AI Agent Minute, Agent Tip of the Day, The Playbook, Inside the Industry) is retired. What replaces it is below. The legacy model is preserved at the end for reference.

---

## The test question every video pillar has to pass

> "What is the most useful short-form video I can make with little or no editing, walking down a street, that gives a real estate agent something of value they can actually get excited about and become hooked on, so they watch more?"

Five criteria are baked in: **cheap to make** (one take, selfie stick, no edit), **genuinely useful**, **exciting** (fear-removal or money-found, not just "informative"), **serializes** (there is always a next one), and it **feeds a business goal**. Every gated and news pillar below is here because it passes this test. The one pillar that does not pass it (Spotlight) is deliberately a substitute, not a fixed slot, and is judged on recruiting reach instead of viewer value.

---

## The pillars at a glance

| Pillar | Weekly | Gate | Core job |
|---|---|---|---|
| **Value Giveaways** | 6 | Gated (IG/FB) | Generate leads. The only gated video pillar |
| **News / Inside the Industry** | 2 | Ungated | Reach, authority, NAR recognition |
| **Broker Problems** | 2 | Ungated | Recruiting wedge + reach |
| **KIRP Promos** | 2 | Ungated | Podcast listeners + reach |
| **The Take** | 3 | Ungated | Reach + authority via defensible contrarian positions |
| **Chicago Agent Spotlight** | substitute | Ungated | Recruiting signal (subs into a News/Broker slot) |

**15 videos per week** (12 plus the 3 takes added 2026-08-10). With 14 carousels (2 gated) that is **29 posts, 5 gated, 24 open** — the open side carries the large majority, which is the intended trade: the gate layer converts, the open layer feeds it. Gated videos went 6 → 3 on 2026-08-19; the grid and the tradeoff live in [`../schedule/master-calendar.md`](../schedule/master-calendar.md), and 12 of the 15 videos are now fed by the [Content Board](automation/content-board.md).

Each goal-reset objective has a carrier: reach and followers (News + Broker Problems + Spotlight), engagement and leads (Value Giveaways), value to realtors (all), KIRP listeners (KIRP promos + the national route out of the gate DM), NAR and institutional recognition (News + the tool-launch cadence inside Giveaways).

D.J. films daily, so 12 videos is real rather than aspirational. KIRP promos ride on top of the other 10; the promo engine already runs ahead of the calendar.

---

## Pillar 1: Value Giveaways (the lead engine)

**Series role:** the only gated video pillar. This is where leads come from.
**Format:** talking-head walk-and-talk, 45-75s, teaching one thing on camera and gating a deeper artifact.
**Gate:** a single spoken keyword ask on Instagram and Facebook, delivered by ManyChat auto-DM. Never on LinkedIn. Governed by the Rule 4 value-exchange exception in [`editorial-standards.md`](editorial-standards.md).

**Design rule (non-negotiable):** the video must be worth watching even if nobody comments. Teach the thing on camera; gate the doc/tool that goes deeper. Six ungated-feeling value videos a week is a content brand. Six "watch the rest in the DM" videos a week is six ads, and the reach dies. Enforce this on every giveaway.

**The 6 weekly giveaways, three flavors:**

| Flavor | # / wk | Artifact gated | Why it passes the test |
|---|:--:|---|---|
| **"Say this, not that"** | 3 | A full doc built for that tip (make one per tip; endless supply) | The strongest answer to the test question. D.J. says the exact words walking down the street (zero edit), it removes a specific fear the agent has this week (the excitement), and "what do I say when..." serializes forever |
| **Tool use-case** | 2 | Access to an existing tool/doc (webinar toolkit, prompt stacks, etc.) | Framed by the use case, NOT the tool. "Here's how to handle the low-appraisal call, comment for the Objection Vault," never "here's the Objection Vault" three times |
| **AI prompt idea** | 1 | The 700-prompt vault (tapthis.co) | One vivid prompt result per week; the vault is the deeper artifact |

**The offer unit is the use case, not the tool or the doc.** There are only ~5 tools; at 2 tool videos a week, framing by tool burns the whole shelf in under three weeks. Framing by use case makes the same tool a fresh offer every time. Same logic protects the "say this" flavor: each is a distinct high-stakes moment, so the supply is bottomless as long as new docs get built.

**This pillar absorbs two retired series.** The Playbook ("here's the play" script cards) and AI Tip of the Week (a prompt) were always giveaways without a gate. They are now the "say this, not that" and "AI prompt" flavors, with a hand-raise finally attached.

**Keyword discipline:** every offer's keyword is registered in [`../data/keyword-registry.md`](../data/keyword-registry.md) so offers do not silently repeat and keywords do not collide. Keep the active set small and repeated. On carousels and in Loomly, the keyword is passed verbatim; a reworded keyword silently destroys that post's leads.

---

## Pillar 2: News / Inside the Industry

**Series role:** reach, authority, and the NAR/institutional signal.
**Format:** the Inside the Industry NF (news flash) and IS (synthesis) sub-types, 45-75s, sharp take on real estate industry news within 24 hours, Chicago angle where possible. 2 of the best stories per week, not every story.
**Gate:** none, on any platform. A serious industry take with a keyword ask stapled to it cheapens the credibility that makes it work. D.J.'s explicit decision.

**Why it stays ungated and central:** this is the pillar the 2026 LinkedIn feed is built to distribute (news-first, topical), and it is the credibility layer that makes NAR and sponsors take calls. Measured on reach and authority, never on leads.

**Feeding it:** `python3 scripts/news_brief.py` each morning, the Feedly real estate feeds, and D.J.'s NAR + Kale operational view. IS drafts pull from the 700-episode podcast archive on quiet news weeks.

---

## Pillar 3: Broker Problems

**Series role:** the recruiting wedge. Content that names the pain an agent has with their *current* brokerage.
**Format:** talking-head walk-and-talk, 45-75s. One specific broker-side pain: bad splits, junk fees, no support, dead company leads, no training, no tech. Name the math, name the fix.
**Gate:** none. D.J.'s call, and his own Facebook data backs it: overt Kale/recruiting content gets throttled (-5.3x on "Kale coaches," -10.5x on webinar promo). Gating these would cost reach AND read as a pitch. Keep them open.

**The recruiting mechanic is the comment section, not a gate.** When D.J. posts "if your brokerage takes 30% and hands you nothing, here's the math," Chicago agents out themselves in the replies ("that's exactly my split"). That is a live, unforced recruiting signal. **Operating rule: someone reads every comment on a Broker Problems video and flags Chicago complainers into Close** for Ana/Jennica to work. The video does reach; the comments do recruiting.

**Why it passes the test where Spotlight doesn't:** a broker-problem video is genuinely useful and exciting to the person watching (it validates a frustration and hands them a fix), and it serializes (there is always another brokerage pain). It is the recruiting-signal job Spotlight was reaching for, but pointed at the viewer instead of at a third party.

---

## Pillar 4: KIRP Promos

**Series role:** drive podcast listeners and carry reach, using the episode engine already built.
**Format:** walk-and-talk promo, built through the Hype Machine (`scripts/podcast-promos/build_promo_brief.py` + [`series/podcast-promo-hype-machine.md`](series/podcast-promo-hype-machine.md)).
**Gate:** none. D.J.'s decision: the ask is simply "go check out the episode."
**Cadence:** 2 per week, promoting the show's best recent episodes. The engine outruns the calendar (14 promos built, 8 posted), so slotting is the constraint, not supply.

---

## Pillar 5: The Take (added 2026-08-10)

**Series role:** reach and authority through defensible contrarian positions. The lane that gets argued with.
**Format:** talking-head walk-and-talk, 45-60s, Mon/Wed/Fri. Full standard: [`series/take-standard.md`](series/take-standard.md).
**Gate:** none, on any platform. A take with a keyword stapled to it reads as bait, and bait is what turns a defensible position into a pile-on.

**The shape:** *realtors shouldn't do X, do Y instead.* Five beats: THE COW (the wrong default) → WHO PROFITS (the turn) → THE RECEIPT (one real number) → THE SWAP (do Y) → LOOP-BACK.

**Beat 2 is why this is a pillar and not a hook style.** Naming who makes money from a belief surviving is what separates a take from a tip, and it is what keeps friction pointed outward at an incentive instead of down at the agent who believed it. Candidates live in [`../data/sacred-cows.md`](../data/sacred-cows.md), which records a `Profits:` line for every entry so that beat is never improvised.

**Heat discipline is the whole design constraint.** 3.5 on Monday and Friday, exactly one heat 4 on Wednesday. Rule 9.2 caps heat 4-5 at one post per week across the *entire* schedule, so the Wednesday take spends the brand's only friction slot. Heat 5 (naming a person, brokerage, coach, or product) is banned outright in this lane.

**Each take pairs with the take carousel already scheduled that day.** Same bank entry, one verification pass, two surfaces: the video argues it, the carousel hands over the receipt in saveable form. That pairing is the only reason 3 more videos a week is affordable at the quality floor.

**Why it passes the test question:** a take is cheap to make (one take, no edit, the argument is the whole production), genuinely useful (it names a thing the agent is wasting money or Sundays on and hands over the replacement), exciting in the fear-removal sense, and it serializes without limit as long as the bank stays fed. It feeds recruiting the same way Broker Problems does: **someone reads the comments on every take** and flags Chicago agents who out themselves into Close.

**Distinguish it from two neighbors.** Against the "say this, not that" giveaway: that one is gated and helpful, this one is open and contrarian, and the difference is beat 2. Against Broker Problems: that one points at the viewer's brokerage, this one points at a practice or incentive anywhere in the business.

---

## Pillar 6 (substitute): Chicago Agent Spotlight

**Series role:** recruiting signal via generosity. Not a fixed slot.
**Format:** per [`series/chicago-agent-spotlight-standard.md`](series/chicago-agent-spotlight-standard.md). Scout a fresh Chicago agent in the news, verify the handle before tagging, verify every fact, never AI-generate the person's face, frame on the person and the lesson.
**Gate:** none.

**Why substitute, not fixed:** it fails the test question — a spotlight gives the *viewer* little they get excited about, because it is about someone else. It still does real work (the best FB distribution in the dataset, +6.0x on a guest feature; tags recruitable Chicago agents; feeds the IG attract play), so it substitutes into a News or Broker Problems slot whenever a worthy Chicago subject exists, and is skipped when one does not. Judge on reshares and new Chicago followers, never on saves or viewer value.

---

## Weekly shape (target)

| | Count | Gate |
|---|---|---|
| Value Giveaways (3 "say this" + 2 tool + 1 prompt) | 6 | gated |
| The Take (Mon/Wed/Fri) | 3 | none |
| News / Inside the Industry | 2 | none |
| Broker Problems | 2 | none |
| KIRP promos | 2 | none |
| Chicago Agent Spotlight | substitutes into a News/Broker slot | none |
| **Video total** | **15** | 6 gated |
| Carousels | 5 (2 gated, 3 not) | see carousel standard |
| **Week total** | **20** | 8 gated |

**Heat budget across the whole week: one post at heat 4-5, and it is the Wednesday take.** Rule 9.2 counts posts, not series. If a News or Broker Problems script wants heat 4 in a given week, one of them gives way. The `news_brief.py` hook-cadence banner reports whether the slot is still open.

The day-by-day grid lives in [`../schedule/master-calendar.md`](../schedule/master-calendar.md). Every sixth week, one Giveaway slot becomes a **tool launch**, and the six-week cycle also runs the event-promo runway (weeks 4-6) out of Giveaway slots. See the goal-reset doc for the cycle.

### Quality floor (never negotiable)

29 posts a week is a volume that can quietly erode the standard the whole brand was built on. It does not get to. The take lane added 3 videos on 2026-08-10 and is the newest, least proven load on the system, so it is named explicitly in the cut order below.

- **The 3-pass rigor (draft → stress-test → EP-polish) is non-negotiable on every video.** If a week cannot clear 29 posts at that bar, ship fewer. A skipped slot costs nothing; a 2-pass filler post costs brand. Volume is never the goal -- recruits are.
- **Cut order when the week is too heavy:** takes drop from 3 to 1 (keep Wednesday, the heat-4 slot, since that is the one doing the distinctive work), then carousels 5 → 3, then videos back to 12. Takes are cut first because they are the newest lane and the least attributable, not because they are the least valuable. **A half-researched take is worse than no take** -- the receipt is the whole defense when the comments arrive.
- **Carousels get their own defined QA** (the checklist in the Loomly handoff, [`series/carousel-standard.md`](series/carousel-standard.md)), so "lighter than a video" never means "sloppy."
- **The week-4 checkpoint tests this explicitly:** is production quality holding at 17/week? If it is slipping, cut to 12 videos or drop carousels to 3 before cutting anything else. Reach and leads are worthless if the content that earns them stops being good.

### Minimum-viable week (bad weeks)

When D.J. is traveling, sick, or slammed, the system degrades gracefully instead of collapsing. **Four posts always ship, no matter what: 2 News + 2 Giveaways.** Everything else is optional that week. A batch-filming buffer (film in 2-3 sessions a week, keep one week of evergreen giveaways in the can) exists so D.J. filming every video is not a single point of failure.

---

## Retired: the April 2026 four-pillar model

The prior model organized around AI Agent Minute (educator), Agent Tip of the Day (connector), The Playbook (practitioner), and Inside the Industry (thought leader), at 6 posts/week.

What happened to each:

- **AI Agent Minute** (100 scripts): frozen at the April pivot; underperformed its investment. Its AI-tool use-cases now feed the AI-prompt giveaway flavor.
- **Agent Tip of the Day** (62 scripts): frozen; the podcast-wisdom job moved to KIRP promos and IS synthesis.
- **The Playbook** (8 pilot): absorbed into Value Giveaways as the "say this, not that" flavor. The script card is now a gated doc.
- **Inside the Industry**: survives and split. NF/IS became the News pillar; the IA (access) sub-type evolved into Chicago Agent Spotlight.

The deeper reason for the reset: the April model had no capture layer. Every pillar produced followers because none asked for a hand-raise. The 90-day test (Apr 20 - Jul 18) produced zero recruiting conversations. The new structure keeps what reached people and adds the gate that converts them, plus a Broker Problems pillar that turns the recruiting wedge into viewer value. Full analysis: [`analytics/2026-07-19-pivot-results.md`](analytics/2026-07-19-pivot-results.md).

The legacy five-theme model (The AI Agent, Top Producer Secrets, Real Talk, Market Intelligence, Systems That Scale) that preceded the four pillars is fully retired and no longer referenced.
