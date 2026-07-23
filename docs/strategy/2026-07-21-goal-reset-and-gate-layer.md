# Goal Reset and the Gate Layer

**Date:** 2026-07-21
**Decided by:** D.J. Paris
**Status:** Decisions locked. Build not yet executed (see [Build queue](#build-queue)).
**Supersedes:** the goal list in `README.md`, the cadence in `docs/content-pillars.md`, and the KPI in `docs/series/carousel-standard.md`.
**Also closes:** the overdue 2026-07-19 end-of-test review from [`2026-04-18-pillar-pivot-decision.md`](2026-04-18-pillar-pivot-decision.md).

This is the working document. If you are picking this up on another machine, read it top to bottom before touching anything else. Everything below was decided in a strategy session on 2026-07-21; nothing here is a proposal awaiting approval unless it says so explicitly.

---

## Why this exists

The 90-day pivot test (Apr 20 to Jul 18) ended without a review being written. This document is that review plus the decision that follows from it.

**What the test produced:** a reliable content machine. Every post organically reaches a few hundred to low thousands per surface, roughly 1,000 to 1,600 cross-surface per script. Production quality is high and the editorial system works.

**What the test did not produce:** a single recruiting conversation. D.J. confirmed this directly. Many people say they love the content. Nobody has said it brought them to Kale.

**Root cause, and it is not the content:** there was no capture layer. Not one post in 90 days asked a viewer to raise a hand. Content produced followers because followers were the only thing it was structurally capable of producing.

Two supporting findings from the same session:

1. **The one capture mechanism that exists has produced one real lead, ever.** tapthis.co has a working stack in `kale-ai-prompts/app/api/capture-email/route.ts` that creates a Close lead, fires Meta CAPI, and emails the asset. Close contains 4 records from it. Three are D.J.'s own tests. It also writes to the wrong custom field (see [Close field bug](#8-close-field-bug-kale-ai-prompts)).
2. **The primary goal is currently unmeasurable.** Roster syncs and genuine new recruits share the "Kale Agent" status in Close, so a 2026 query returns 545. Recruits attributable to content cannot be counted today.

**The decision:** keep the content machine. Add the gate layer. Do not reverse the pivot.

---

## The goals, in D.J.'s words

Recorded verbatim from the session. The short-form video and carousel content exists to:

- add more reach and followers
- increase engagement with content
- generate actual leads via offers ("comment X for a free Y") that ultimately join Kale (Chicago agents); for outside Chicago, still generate the leads and promote KIRP
- add value to realtors who want the news content or tip content
- get more listeners to KIRP
- build the brand with NAR and other real estate institutions (increased recognition)

These are not six competing goals. They are one machine:

```
VALUE CONTENT (news + tips + tools)
        |
     REACH + FOLLOWERS
        |
     ENGAGEMENT
        |
     OFFER: "comment X for free Y"        <- the capture, the only genuinely new piece
        |
        +-- Chicago agent   -> Kale recruiting lead
        +-- Everywhere else -> KIRP listener + tool user
        |
NAR + INSTITUTIONAL RECOGNITION           <- byproduct of running the above at volume
```

Every objective has a carrier. Nothing on the list is orphaned, and nothing gets deleted.

### What changed from the April goal list

The old README list ("1. Kale recruiting, 2. NAR, 3. KIRP growth, 4. National reach") failed as a goal set for five reasons, all of which the new structure fixes: they were territories rather than goals with numbers, four ranked priorities behaved as four coequal ones, the measured metrics were vanity while the wanted outcomes went unmeasured, nothing on the list was an asset D.J. owns, and "national thought leader reach" was an input promoted to a goal, which is why four of six weekly slots were making national-generic news.

**National reach is now explicitly a byproduct, not a goal.** It is what makes NAR return calls and what makes sponsors amplify. It is harvested, not optimized.

---

## The architecture

### Video carries the brand. Carousels carry the offers.

|  | Video | Carousel |
|---|---|---|
| Job | Reach, authority, podcast, NAR | Saves, offers, leads |
| Gate | Only on giveaway videos, tool launches, and event promos | 2 of 5 gated |
| Editorial | No-engagement-ask rule stays fully intact | Value-exchange gate permitted |

D.J.'s call, and it is the right one: news walk-and-talks and KIRP promos get **no gate**. A serious NAR settlement take with "comment BRIEF below" attached would cheapen the exact thing that makes it credible. This keeps the no-engagement-ask rule intact everywhere the editorial machinery lives, and confines the amendment to carousels and offer videos.

### The offer unit is the use case, not the tool

This is the single most important design rule in this document.

There are 5 tools on tapthis.co. If the offer unit is "a tool," then 4 to 5 giveaway videos a week means re-promoting the same five things every week forever, and comment volume collapses inside a month from offer fatigue.

| Offer unit | Inventory | Runway at 5/week |
|---|---|---|
| The tool | 5 | One week |
| The use case | 620 prompts + 4 prospecting plays + 4 webinar tools | Over two years |

"Comment LISTING and I'll send you the prompt that writes your listing description" is a distinct offer from "comment FOLLOWUP for the ghosted-lead sequence," even though both live inside tapthis.

**Corollary design rule: the video must be worth watching even if nobody comments.** Teach the use case on camera, gate only the artifact. Done right, giveaway videos generate reach too, which protects the top of the funnel. Done wrong, half the output becomes ads.

### Existing tool inventory (all built, none ever launched)

| Tool | Route | What it is |
|---|---|---|
| Sound Like You | `/sound-like-you` | Make AI sound exactly like you (voice print builder) |
| Prospecting | `/prospecting` | Pre-Listing Intelligence Dossier, Database Triage, Ghost Notes Reactivation, Business Entity Unmasking |
| Webinar tools | `/webinar` | Midnight Sales Coach, Context-Loaded Client Brief, Objection Vault, AI Open House Machine |
| Stacks | `/stacks` | Multi-step prompt chains |
| Heartland | `/heartland` | "You're Doing AI 100% Wrong" five strategies |
| The vault | root | 620 prompts |

**Launch order decided: `/sound-like-you` first** (most distinctive, least replicable by a competitor), then `/prospecting`, then `/stacks`. The first three cycles need no build work, which buys 18 weeks to build tool number six properly.

D.J. intends to keep building new tools on an ongoing basis so there is always something new to offer. That is correct and is what keeps the gate fresh; each launch is a legitimately new reason to ask, it reactivates prior converts, and every launched tool stays in the evergreen keyword rotation permanently.

---

## The weekly cadence

**15 posts per week: 10 videos, 5 carousels.** D.J. films daily, so video volume is real rather than aspirational.

### Videos (10/week)

| Type | Count | Gate |
|---|---|---|
| KIRP promos | 2-3 | none |
| News walk-and-talks | 2-3 | none |
| Use-case giveaways | 4-5 | gated |

KIRP publishes 2 to 3 episodes a week and D.J. wants a walk-and-talk for every episode, so promos flex to actual episode drops rather than sitting on fixed days. The promo engine is already built (`scripts/podcast-promos/build_promo_brief.py` plus the Hype Machine spec) and is currently outrunning the calendar: 14 promos exist in the repo, only 8 ever posted.

### Carousels (5/week)

| Type | Count | Gate |
|---|---|---|
| Gated offer carousels | 2 | gated |
| Engagement carousels | 3 | none |

**Production split:** Claude builds the carousels. Jennica inputs them into **Loomly**. D.J.'s marginal cost is near zero, which is why 5 is sustainable.

This requires a **Loomly-ready handoff format** in the carousel standard, because Jennica is inputting rather than interpreting: slide-by-slide copy she can paste, the caption, the hashtag block, the ManyChat keyword, and the pinned first comment. The format must state explicitly that **the keyword is never to be reworded**. A paraphrased keyword silently destroys that post's leads.

---

## The six-week cycle

The tool launch and the event are two phases of one cycle. The new tool is the webinar's hook.

| Week | Gated campaign | Giveaway slots |
|---|---|---|
| 1 | **Tool launch** (`VOICE` first, then next tool) | evergreen use cases |
| 2-3 | none | evergreen use cases |
| 4 | **Event announce** (`WEBINAR`) | evergreen use cases |
| 5 | Event: teach one piece of it, gate the seat | reduced |
| 6 | Event: last call, then the webinar runs | reduced |

**Event promos come out of the giveaway slots during weeks 4 to 6, not on top of them.** Volume stays at 10 videos and 5 carousels. Three event posts across three weeks is a real runway; one post every six weeks would not fill a webinar.

**The gate is the fix for event throttling.** Facebook distributes webinar promos at **-10.5x**, the worst number in the entire dataset, and the outbound registration link is a large part of that. "Comment WEBINAR and I'll send you the link" removes the link from the post entirely.

Non-Chicago registrants are welcome. The content is AI strategy and is valuable to anyone; the DM routing splits them to the podcast and tool track afterward.

---

## The gate mechanism

**ManyChat, to be purchased.** Approved by D.J.

```
Post ends with a spoken keyword ask
        |
Viewer comments the keyword
        |
ManyChat auto-DMs the asset
        |
DM asks ONE qualifying question: "are you licensed in Illinois?"
        |
        +-- Yes -> email capture -> Close, source "IG Offer - <keyword>"
        +-- No  -> email capture -> Close, tagged national -> KIRP + tools nurture
```

The Illinois question is the entire routing mechanism and must land as helpfulness, not screening. Working draft: *"Sending it now. And so I point you at the right stuff, are you licensed in Illinois?"*

**Platforms:** Instagram and Facebook only. LinkedIn keeps the no-engagement-ask rule untouched; LinkedIn actively downranks engagement bait per the June stress test, and its audience is the wrong one for this mechanic.

### Close fields the flow writes to

These already exist. No new field creation needed for events.

| Purpose | Field |
|---|---|
| Lead source | `cf_U9j9E5v9LuS4SMLZfI854gU88tmhi0GLVlxtzbZp1yD` (Kale Lead Source) |
| Event registration | `cf_1gvyQgunZuym2LgHYQmy0RnCz5KIvL9gqRLMpcYlpNY` (Registered for Webinar) |
| Event attendance | `cf_Z6ZcMb3eocGGwB2ZKnvH110LCV5cK5WdVFtS49xfKeU` (Attended Webinar) |
| Which event | `cf_pBU4ck6PIdkVbBJDutSxlWbRO7GqTYCZgubIRf1AH7r` (Last Webinar Registered) |
| Pipeline | `cf_v8hykgKmpI4sXeaJ6tOO90V7h1Sumi7o88xXGKQKlbx` -> "Webinar Registered" |

### Keyword map (starting set)

Keep the set small and repeated. Five keywords the audience learns beats twenty they do not. Full allocation tracked in `data/keyword-registry.md` (to be built).

| Content | Offer | Keyword |
|---|---|---|
| Giveaway video | The single prompt or play taught in the video | one per use case, registry-tracked |
| Gated carousel | The checklist or template from the payload slide | `LIST` |
| Tool launch | The tool | tool-specific (`VOICE` for Sound Like You) |
| Event promo | The registration link | `WEBINAR` |

---

## The week-4 checkpoint

Full volume starts immediately (capacity exists). What does not get skipped is a hard checkpoint at week 4, with the numbers named in advance so the scale decision is data-driven:

- comments per gated post, split by video vs carousel
- DM open rate
- email capture rate (DM opened to email submitted)
- the Illinois split (what fraction of captured leads are actually recruitable)

If gated carousels pull a fraction of what gated videos do, shift the mix rather than guessing. If the whole loop converts poorly, fix the offer or the ask before multiplying the work.

---

## Build queue

Nothing below has been executed yet. This document is the spec.

### Video repo

1. ~~`docs/strategy/2026-07-21-goal-reset-and-gate-layer.md`~~ **done, this file**
2. `docs/analytics/2026-07-19-pivot-results.md`. Formal close of the 90-day review against the five success criteria in the April pivot decision. Verdict: criteria 1-3 (engagement, reach, followers) held or passed; criteria 4-5 (industry conversations, recruiting conversation) failed. Root cause: no capture layer. Decision: keep content, add gate. Do not reverse the pivot.
3. `docs/series/carousel-standard.md`, **rewritten.** KPI moves from saves to gated leads. Gate becomes mandatory on 2 of 5. Remove the blanket engagement-ask ban. Add the Loomly handoff format for Jennica.
4. `docs/editorial-standards.md` and `CLAUDE.md`, **amended.** See exact amendment text below.
5. `docs/content-pillars.md`, **rewritten.** Still documents the four-pillar cadence retired in April 2026.
6. `data/keyword-registry.md`, **new.** Which use case maps to which keyword, which have aired, and when. Same pattern as `scripts/podcast-promos/promo-registry.md`, and for the same reason: at 4-5 giveaways a week the offers will start repeating without a registry.
7. `docs/automation/manychat-flows.md`, **new.** DM scripts, the Illinois question, Close routing, per-keyword branches. A spec for D.J. to build in the ManyChat UI; it cannot be wired up from here.

### kale-ai-prompts

8. See [Close field bug](#8-close-field-bug-kale-ai-prompts) below.

### The exact editorial amendment (approved, not yet applied)

The current rule bans engagement asks universally. `CLAUDE.md` Rule 4, the carousel standard ("no engagement ask of any kind"), and a commit literally titled "Strip engagement asks from carousels" all enforce it. **As written, the build process will delete every gate specified in this document.** The amendment must land before any gated content is drafted.

Replace the universal ban with a three-part rule:

- **Hollow engagement bait stays banned everywhere.** "Comment YES if you agree," "double tap if," "save this," "follow for more." These manufacture a signal without delivering anything. This is the rule's original purpose and it is unchanged.
- **LinkedIn keeps the total ban.** No gates, no keyword asks, no exceptions. LinkedIn downranks engagement bait explicitly and the mechanic does not fit that audience.
- **Value-exchange gates are permitted on Instagram and Facebook**, and only on gated carousels, giveaway videos, tool launches, and event promos. A value-exchange gate delivers a real artifact the viewer asked for. "Comment PROMPTS for my 620-prompt library" is a delivery mechanism, not bait.

News walk-and-talks and KIRP promos remain ungated on every platform, by D.J.'s decision.

### 8. Close field bug (kale-ai-prompts)

`app/api/capture-email/route.ts` stamps `"Copy That"` into `cf_c09clx40GuQEME4aFK13bHwS57NdQOUTMWI5KAq9EfY`, which is **Lead Type** (the A/B/C field). It should write to `cf_U9j9E5v9LuS4SMLZfI854gU88tmhi0GLVlxtzbZp1yD`, **Kale Lead Source**.

Consequences today: every tapthis lead is invisible to source reporting, and Lead Type is being quietly corrupted. One-line fix, and worth verifying in Close afterward.

A second, larger issue in the same file: the capture modal fires 1.2 seconds **after** the prompt is copied, and a dismissal writes to `localStorage` so it never asks that device again. The visitor already has the thing being traded for. Under the new architecture tapthis capture matters less (ManyChat is the primary gate), but the modal timing should be revisited rather than left as is.

---

## Open items

- **Recruiting baseline is still unknown.** How many Chicago agents join Kale in a typical month, and how many would make this worth the hours. Needed before any outcome target can be set honestly.
- **Making recruits countable in Close.** Roster syncs and real recruits share the "Kale Agent" status. Until they are separable, the primary goal cannot be measured. Blocking for any attribution reporting.
- **Publishing log has been dark since 2026-07-02.** Nineteen days as of this session. Either posting slipped or the YouTube auto-sync routine broke. Unresolved.
- **ManyChat not yet purchased.**
- **Whether the Zillow/NAR paid amplification is a repeatable channel.** A partner who can put a million views behind a take outweighs any cadence change in this document. Never investigated.

---

## 2026-07-22 addendum: pillar refinement + council review

The 2026-07-21 session set the architecture. The 2026-07-22 session refined the pillars against a test question, then ran the whole plan past an adversarial council and fixed what it found. Both are folded into the docs; this section records what changed and why.

### The test question that refined the pillars

> "What is the most useful short-form video I can make with little or no editing, walking down a street, that gives a real estate agent something of value they can actually get excited about and become hooked on, so they watch more?"

Scoring the candidate formats against it produced one decisive finding: **the exact-script ("what do I say when...") video wins on every axis** -- zero editing, removes a specific fear (that is the *excitement*, where most tips are merely useful), and serializes forever. Prompts scored lower because **the value lives off-screen**: you cannot feel a prompt walking down a street. So the Giveaway pillar is anchored on "say this, not that" scripts, with prompts as a secondary flavor.

The same test exposed that **Chicago Agent Spotlight fails on viewer value** -- a spotlight is about someone else. It keeps a role (best FB distribution in the dataset, +6.0x; real recruiting reach) but as a **substitute**, never a fixed slot, judged on reshares and Chicago follows rather than viewer value.

### The one thing (brand spine)

> **D.J. Paris tells real estate agents exactly what to do and say to grow their business.**

News and KIRP are credibility *under* that promise, not co-equal pillars. Broker Problems is the recruiting edge. This resolves the council's "five pillars is five things to be known for" finding.

### Final structure

**17 posts/week: 12 videos + 5 carousels, 8 gated.** Detail in [`../content-pillars.md`](../content-pillars.md) and [`../series/carousel-standard.md`](../series/carousel-standard.md).

| Pillar | Weekly | Gate |
|---|---|---|
| Value Giveaways (3 say-this + 2 tool use-case + 1 prompt) | 6 | Gated IG/FB |
| News / Inside the Industry | 2 | Open |
| **Broker Problems** (new pillar) | 2 | Open; comments mined for Chicago signals |
| KIRP Promos | 2 | Open |
| Chicago Agent Spotlight | substitute | Open |
| Carousels | 5 (2 gated) | 2 gated IG/FB + LinkedIn link variant |

**Broker Problems** is the significant addition: content naming the pain an agent has with their *current* brokerage. It passes the test question (useful and exciting to the viewer, serializes) where Spotlight did not, and it does the recruiting-signal job better. Ungated on purpose -- FB throttles overt Kale content (-5.3x) -- with the recruiting mechanic being **comment mining**, not a gate.

### The council review and the five fixes

Five adversarial lenses (direct-response marketer, positioning strategist, algorithm realist, recruiting operator, COO) reviewed the plan. All five findings were adopted:

| # | Finding | Fix | Where it lives |
|---|---|---|---|
| 1 | **Lead quality inverted** -- 6 low-intent slots vs 2 high-intent; the DM filtered geography, never intent. A prompt-downloader is a content fan, not a mover | **Q2 intent question** in every gated DM: "what's the ONE thing you'd change about your brokerage?" -> new Close field *Brokerage Pain* -> four-way routing | [`../automation/manychat-flows.md`](../automation/manychat-flows.md) |
| 2 | **Capture ends in a dead list** -- no nurture defined, and the gated docs did not exist | 3 nurture sequences (HOT Chicago / Warm Chicago / National) + **the Objection Response Vault** as the one net-new flagship doc. Both are launch prerequisites | manychat-flows.md; Vault still to build |
| 3 | **Quality-at-volume risk** -- 17 posts/week vs the 3-pass bar | Explicit **quality floor** (ship fewer rather than drop the bar) + **minimum-viable week** (2 News + 2 Giveaways) + batch-filming buffer | [`../content-pillars.md`](../content-pillars.md) |
| 4 | **Five co-equal pillars, no one sentence** | The one thing (above); News/KIRP subordinated to credibility | content-pillars.md, README |
| 5 | **Operating rules unowned** | Owner table below | this doc |

### Ownership

| Job | Owner |
|---|---|
| Film all 12 videos | D.J. (buffered by batch-filming, 2-3 sessions/wk, 1 week of evergreen in the can) |
| Build carousels | Claude |
| Load Loomly | Jennica |
| Broker-problem comment mining -> flag Chicago into Close | **Jennica** (confirmed 2026-07-22) |
| Build + maintain ManyChat flows | D.J. sets up; Jennica swaps keywords per the registry |
| Work HOT Chicago leads + nurture sequences | Ana |
| Week-4 checkpoint | Claude compiles, D.J. decides |

### Launch prerequisites (nothing gates until these are true)

- [ ] ManyChat purchased; IG + FB connected
- [ ] **Objection Response Vault built** and genuinely worth an email (the one net-new flagship doc)
- [ ] *Brokerage Pain* field created in Close
- [ ] The 3 nurture sequences built in Close
- [ ] One flow tested end-to-end (comment -> DM -> asset -> Q1 -> Q2 -> email -> correctly-sourced Close record)
- [ ] Close field bug fixed in `kale-ai-prompts` (Kale Lead Source, not Lead Type) + `?src=` tag handling for LinkedIn capture

---

## Session context

Decisions in this document came from a strategy session on 2026-07-21 in which D.J. explicitly reset the goals from scratch rather than amending the April list. Two framings were proposed and rejected along the way, recorded here so they do not get re-litigated:

- **"Content as assist to outbound"** (content makes cold calls convert rather than sourcing leads). D.J. initially selected this, then described a sourcing model in his own words. Sourcing won.
- **"National audience is a dead end."** Wrong. D.J.'s routing solves it: capture everyone, route by geography, Chicago to Kale and everywhere else to KIRP and the tools. One mechanic, two destinations.
