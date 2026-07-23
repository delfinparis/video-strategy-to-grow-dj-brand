# Carousel + Static Post Standard

The format spec for D.J.'s **static and carousel Instagram posts** -- the saveable, swipeable
format that sits alongside the 45-75s walk-and-talk videos. Sourced from the best realtor
carousel accounts (see [`docs/strategy/realtor-instagram-watchlist.md`](../strategy/realtor-instagram-watchlist.md))
and built on the repo's existing [Viral 3-Act Spine](viral-3-act-spine.md) and
[caption-and-hashtag-strategy](../caption-and-hashtag-strategy.md).

Reference implementation already in the repo:
[`scripts/carousels/NF-058-reffkin-jensen-testimony-carousel.md`](../../scripts/carousels/NF-058-reffkin-jensen-testimony-carousel.md).

---

## What a carousel is for here

> **UPDATED 2026-07-22.** Carousels were promoted from a saves layer to **the lead surface that
> runs alongside video**. The week is now **5 carousels: 2 gated + 3 open**, the KPI is split by
> type (gated = leads, open = saves/sends), and gated carousels ship in **two variants** (IG/FB
> keyword gate, LinkedIn link-in-first-comment). See [The 5-carousel week](#the-5-carousel-week-2026-07-22)
> and [Loomly handoff](#loomly-handoff-what-jennica-receives) below; they govern where they
> conflict with older text. Strategy: [`../strategy/2026-07-21-goal-reset-and-gate-layer.md`](../strategy/2026-07-21-goal-reset-and-gate-layer.md).
>
> **What carousels are for (the test question):** video carries what wants to be *watched*;
> carousels carry what wants to be **saved and sent**. Ask: "would an agent screenshot this,
> save it to a folder, or text it to another agent?" Reference material (scripts, checklists,
> comparison tables, data cards) passes. Opinion and narrative do not -- that is video's job.
> The 0-1 saves the format was getting came from putting video's content on a surface that
> rewards something else.

**Primary job (superseded, see the update box above): reach and saves** (set 2026-07-07). A carousel earns its slot when an agent
would *save* it to act on later or *send* it to another agent. That is a different job than the
walk-and-talk videos, which carry the recruiting-first load. Carousels grow follows and
authority; recruiting is the soft secondary.

**Two lanes, run roughly evenly:**

- **News-repurpose:** turn an existing Inside-the-Industry (NF/IS/IA) script into a carousel.
  Same facts, same sourcing, no new claims. Lowest new effort. Model: the NF-058 example.
- **Evergreen tip:** net-new saveable how-to (scripts, objection handling, marketing tactics,
  data cards) modeled on Coffee & Contracts / Jimmy Mackin / Chelsea Peitz. Not tied to a script.

---

## Stat sourcing (the same engine the walk-and-talks use)

A carousel does not get a looser stat standard because it is "just an image." Every number on
a slide obeys **[editorial-standards.md](../editorial-standards.md) Rule 1 (Never Fabricate
Statistics)** exactly like a spoken script: a named source, a publication year, and a
`## Data Source` block in the carousel file. No rounding, no "roughly," no plausible-but-invented
specifics. A data slide with an unsourceable number gets pulled, not shipped.

Pull stats from the **same three sources** the video series already draws on, so a carousel is
just another surface for stats D.J. has already vetted:

| Stat source | Where it lives | Feeds which carousels |
|---|---|---|
| **Evergreen stat bank** (walk-and-talk engine) | `data/news-briefs/stat-bank.json`, maintained by [`scripts/stat_bank.py`](../../scripts/stat_bank.py) | Evergreen data-card carousels. The bank already holds sourced NAR/Zillow/Redfin/HousingWire stats with a named source + year; `news_brief.py` surfaces the best-fit one each morning. A stat good enough to film is good enough to make a carousel. |
| **Today's news brief** | `data/news-briefs/YYYY-MM-DD.md` (from [`scripts/news_brief.py`](../../scripts/news_brief.py)) | News-repurpose carousels. Same story, same sourcing as the NF script it repackages. |
| **Coffee Talk aired scripts** | `coffeetalk-episode-registry` repo (the Coffee Talk system prompt is also the origin of this repo's stat-integrity rules) | Coffee Talk-derived tip/stat carousels. Every number traces to the aired script. |
| **KIR episode analysis** | `keeping-it-real-content-system/data/analysis/<episode>_analysis.json` (the source [`scripts/podcast-promos/build_promo_brief.py`](../../scripts/podcast-promos/build_promo_brief.py) already uses) | Podcast-tie-in carousels. Every number traces to the analysis JSON, never invented. |

The last two repos live beside this one on D.J.'s home Mac (`~/GitHub Projects/`). They are not
cloned into every cloud session, so when a carousel needs a Coffee Talk or KIR stat and those
repos are not present, mark it `[STAT NEEDED: ...]` per Rule 1 and fill it on the machine that
has them. Never fabricate to fill the gap.

**Reuse rule carries over:** a stat that was right in April may be wrong by July. Re-verify
every stat at carousel-build time, even one lifted from a script that already shipped.

---

## Slide architecture

Carousels are the 3-Act Spine expressed across slides instead of across 60 seconds. The
retention problem is the same (people leave in the middle), and the fix is the same (open a
loop, make each slide earn the next swipe).

| Slide | Job | Rule |
|---|---|---|
| **1 -- Hook** | Stop the scroll AND promise the payoff | Carries ~80% of the weight. One idea, biggest type. Name the reward for swiping. |
| **2 -- Standalone second hook** | Re-hook the swipers | Instagram re-serves slide 2 to people who did not swipe past slide 1. It must work with zero context. Never "continued from slide 1." |
| **3 to N-2 -- The body** | One idea per slide, earn each swipe | After slide 3, tighten: one idea, one line of body where possible. This is the story/tactic middle. |
| **N-1 -- Screenshot payload** | The slide people save on their own | The numbered list, the checklist, the scripts. This is the slide people screenshot. Make it so self-contained the save is automatic. The payload earns the save; the deck never asks for it. |
| **N -- Close** | "Here's what you do now" action | Close on one specific action at the agent's own business, tied to the payload (editorial-standards Rule 4). Then, optionally, one loop-back line that echoes the hook. No "save this," no "follow for," no engagement ask of any kind. |

**Gate exception (2026-07-22):** the **2 gated carousels** each week close on a value-exchange gate instead -- a single keyword ask delivering a real artifact, per the Rule 4 exception in [editorial-standards.md](../editorial-standards.md). That is permitted on **Instagram and Facebook only**. The **3 open carousels** keep the rule below exactly as written, and *no* carousel on **LinkedIn** ever carries a keyword ask. Hollow bait ("save this," "follow for," "tag") stays banned on all five, on every platform, gated or not.

**Reach and saves is the goal, not a line you say.** This format's goal is saves and reach, but "save this" and "follow for more" are still banned here exactly as in every other series (editorial-standards Rule 4; they appear by name in the pre-commit checklist). The resolution is not a loophole for carousels: you *earn* the save with a screenshot-worthy N-1 payload and a close that hands the agent something to do, the same way the walk-and-talks earn it. The watchlist's scoring lens uses "save-worthiness" and "send-worthiness" as internal quality tests for picking which idea to build; that is a private yardstick, never viewer-facing copy. If a draft slide or caption contains "save this," "save it," "save the carousel," "follow for," "tag," or "bookmark," it is not done.

**Slide count:** 6-10. Under 6 rarely justifies the swipe format; over 10 loses people. NF-058
ran 9 and that is a good default ceiling for a news carousel. Evergreen tip carousels often
land at 6-8.

**Format families for slide 1** (pick on purpose, log it):
- One-tactic breakdown ("The one caption change that doubled saves")
- Listicle / scripts ("5 things to say when a seller says 'let's just try Zillow'")
- Data card ("$1.3B a year. That is what one company offered to end private listings.")
- Myth-bust ("You do not need 10,000 followers to get a listing from Instagram.")
- POV / relatable ("POV: the lead who ghosted you for 6 months just liked your story.")

---

## Building it in Canva

**Do not use one AI prompt to author the deck.** Canva's Magic Design (text-to-design) paraphrases
copy to fit a layout, and a paraphrased number is a Rule 1 fabrication: feed it "$2,165" and it
will happily render "$2K+" or "over $2,000." The exact, sourced figure is the entire point of a
data carousel. So the copy is always **typed from the carousel file, never generated**. Canva's AI
is used only for imagery (Magic Media) and, at most, as a rough scaffold you immediately correct.

### Step 1 -- Build the two Brand Templates (once)

Create two reusable Canva **Brand Templates** at 1080x1350, one per lane, so every carousel is a
fill-in job, not a design job:

| Template | Lane | Locks |
|---|---|---|
| **IIR News (dark editorial)** | news-repurpose | Charcoal-to-near-black background, one accent color, bold condensed headline font, D.J. / Inside the Industry mark in a bottom corner. The "Bloomberg-courtroom-explainer" look the NF scripts call for. |
| **Evergreen (light clean)** | evergreen | Warm off-white background, dark text, one accent, same mark. Lighter and calmer than the news look. |

Each template holds the five slide *roles* as pages: Hook, Second hook, Body (duplicate as many
as the deck needs), Screenshot payload, Close. Size the text placeholders so the hook is the
biggest type on the page and body slides are one to two lines.

### Step 2 -- Fill the copy (exact, from the file)

Two ways, both keep the numbers verbatim:

- **Manual:** paste each slide block's copy into the matching template page.
- **Bulk Create (faster, still exact):** Canva's **Bulk Create** app auto-generates one page per
  row of a data table. Connect the template's text fields to the table columns, hit generate, and
  the whole deck builds in one pass. Because the table holds *your* typed copy, there is no
  paraphrase risk. Table format:

  | Column | Holds |
  |---|---|
  | `slide` | slide number (1, 2, 3 ...) |
  | `role` | hook / second-hook / body / payload / close |
  | `headline` | the slide's big line |
  | `body` | the supporting line(s); use line breaks for a numbered payload or the two close lines |

  A carousel file may end with a ready-to-paste Bulk Create table in this shape. If it does, it is
  a convenience copy of the slide blocks above it, not a second source of truth: if the two ever
  disagree, the slide blocks win.

### Step 3 -- Imagery via Magic Media (the only safe AI step)

Backgrounds and accent visuals only. Each carousel file carries a `## Canva Magic Media Prompts`
section. The rules:

- **Imagery only. Never ask Magic Media to render text, numbers, charts, or a logo.** AI image
  tools mangle glyphs, and a mangled stat on a slide is a fabrication. Text comes from the template
  layer; the mark comes from the Brand Template.
- **Keep it subtle behind data slides** so the figure stays legible: a low-contrast texture or
  gradient, not a busy photo.
- **Match the lane look** (dark editorial vs light clean) so a deck reads as one system.
- Generate at the deck's vertical ratio (1080x1350) and set it as a background layer, text on top.

---

## Frontmatter

Every carousel file in `scripts/carousels/` starts with:

```yaml
---
lane: "news-repurpose"            # or "evergreen"
source_script: "scripts/inside-the-industry/NF-0XX-slug.md"   # omit for evergreen
carousel_for: "Working title of the post"
hook_family: "data-card"          # the slide-1 family, per the list above
platform_primary: "Instagram (carousel)"
platform_secondary: "LinkedIn (PDF/document carousel)"
slide_count: 8
goal: "reach-and-saves"
generated: "YYYY-MM-DD"
---
```

`hook_family` and `goal` are new to this format; the rest mirrors the NF-058 example. Do not
repeat the same `hook_family` two carousels in a row (same discipline as the video Hook Matrix).

---

## The 5-carousel week (2026-07-22)

**5 carousels per week: 2 gated + 3 open**, alongside the 12 videos. Claude builds them; Jennica loads them into Loomly. The lineup maps to the video pillars so most of the work is repurpose, not net-new.

| # | Carousel | Gate | What is on the slides | Judged on |
|---|---|---|---|---|
| 1 | **"Say this, not that" script card** | Gated | The exact word-for-word responses. The screenshot format | Leads |
| 2 | **Tool / prompt use-case** | Gated | The use case + a taste of the output | Leads |
| 3 | **Broker-problem comparison** | Open | "What your brokerage should give you vs what most do" -- a table agents save AND send | Saves + sends |
| 4 | **News explainer card** | Open | The week's biggest story as a saveable data/timeline card | Saves + reach |
| 5 | **Evergreen checklist** | Open | Net-new saveable how-to (Coffee & Contracts model) | Saves |

**#3 is the sleeper.** The broker-problem comparison table is the most *sendable* thing on the list: an agent screenshots "here's what you're missing" and texts it to a friend at another brokerage. That is the recruiting wedge spreading peer-to-peer on the surface built for it. It stays open (ungated) for the same reason the broker-problem videos do -- overt Kale content gets throttled on FB (-5.3x), and gating it would cost reach and read as a pitch.

**The 2 gated carousels reinforce that week's video offers.** Same asset, same keyword as one of the week's giveaway videos. The agent sees the tip as a video and again as a saveable carousel: two shots at one conversion, one keyword to remember, no extra ManyChat flow. Do not mint separate carousel-only offers.

### Two variants for every gated carousel

The same deck ships twice, because the gate mechanic does not exist on LinkedIn (ManyChat has no LinkedIn channel, and LinkedIn bans comment-to-DM automation *and* downranks "comment X" asks):

| Platform | Capture mechanic | Close source |
|---|---|---|
| **Instagram + Facebook** | Keyword gate: "comment SCRIPTS and I'll send it" | `IG Gate - <keyword>` |
| **LinkedIn** | Identical slides, **resource link in the FIRST COMMENT** (never the post body -- LinkedIn downranks body links). The tapthis page asks for the email | `LinkedIn - <asset>` |

Both roads end in a Close lead. Only the door changes. Links and their source tags live in [`../../data/keyword-registry.md`](../../data/keyword-registry.md).

**The 3 open carousels should all go to LinkedIn.** Documents and carousels out-engage video there (~6.6-6.8%) and it is the most agent-dense audience. This is finally using LinkedIn's one genuine strength.

### KPI split

The old single "reach and saves" KPI is retired -- it was failing on its own terms (saves running 0-1). Judge by type:

- **Gated (1, 2):** leads captured. Saves are a nice-to-have.
- **Open (3, 4, 5):** saves + sends, and for #3, comment-mined Chicago signals.

---

## Loomly handoff: what Jennica receives

Claude builds the carousel; **Jennica inputs it into Loomly**. She is loading, not interpreting, so every carousel file ends with a paste-ready handoff block. Nothing in it should require a judgment call.

The block contains, in order:

1. **Slide-by-slide copy** -- numbered, exact, paste-per-slide. (The Canva Bulk Create table above serves this.)
2. **The caption**, per platform, final. No "pick one."
3. **The hashtag block**, already capped per [caption-and-hashtag-strategy](../caption-and-hashtag-strategy.md).
4. **The ManyChat keyword** (gated only) -- flagged VERBATIM.
5. **The LinkedIn first-comment link** (gated only), with its `?src=` tag.
6. **The pinned first comment** (open carousels) -- value-extending, never a "follow me."
7. **Platform routing** -- which of IG / FB / LinkedIn this deck goes to.

> **The keyword is copied exactly, never reworded.** "Comment SCRIPT" instead of "comment SCRIPTS" silently breaks the ManyChat trigger. There is no error message; the leads simply never arrive. Same for the `?src=` tag on LinkedIn links.

### Carousel QA checklist (the lighter-than-video bar, still a bar)

Run before handing to Loomly. "Lighter than a walk-and-talk" never means sloppy (see the quality floor in [content-pillars.md](../content-pillars.md)):

- [ ] Every stat has a named source + year and a `## Data Source` block (Rule 1 applies to slides exactly as to scripts)
- [ ] Slide 1 carries one idea and names the reward for swiping
- [ ] Slide 2 stands alone with zero context (IG re-serves it to non-swipers)
- [ ] The N-1 payload is self-contained enough to screenshot
- [ ] No em dashes, no AI-speak, hashtag caps respected
- [ ] No hollow bait anywhere ("save this," "follow for," "tag a friend") -- gated or open
- [ ] Gated only: keyword matches the registry exactly, and a flow exists for it
- [ ] LinkedIn variant: link is in the first comment, carries its `?src=` tag, and no keyword ask appears anywhere

---

## Cadence: superseded background

*The 3/week recommendation below is superseded by the 5-carousel week above. The reasoning is kept because the format-vs-video logic still holds.*

**The original recommendation: 3 carousels per week once ramped, added *alongside* the daily videos, not
in place of them.** Roughly 2 evergreen tips + 1 news-repurpose (the "both lanes, evenly-ish"
split). Ramp there over the first three weeks so the format and templates settle: **week 1 = 1,
week 2 = 2, week 3+ = 3.** Then hold and let the data decide whether to push higher.

**Why 3, and why alongside:**

- Carousels do a **different job** than D.J.'s videos, so they add rather than compete. Reels
  are the reach/discovery format; carousels are the **saves and engagement** format. 2026 data:
  carousels average a ~1.92% engagement rate vs ~0.50% for Reels, and carousels get on the order
  of 9x the saves of a single image (this repo's own [platform-strategy.md](../platform-strategy.md)
  and the 2026 Metricool/Socialinsider studies). Past ~50K followers, carousels also start to
  *out-reach* Reels. This format's stated goal is reach-and-saves, so carousels are the right tool.
- **3/week is the researched sweet spot.** The consensus optimal mix for a business account is
  ~2-3 carousels/week; Mosseri's public guidance is consistency over raw volume. Total output
  past ~10 pieces/week hits diminishing returns and burnout, so 3 carousels layered onto the
  existing 6 video slots keeps the week productive without tipping into spam.
- **1 of the 3 is nearly free.** The news-repurpose carousel repackages an NF script D.J. already
  filmed that week (same facts, same Data Source). Only the ~2 evergreen tips are net-new work.

**Weekly grid (carousels ride as a second post on news days, spaced a few hours off the video):**

| Day | Existing video slot | Add |
|---|---|---|
| Mon | KIR Podcast Promo | - |
| Tue | IIR News (NF) | **Evergreen tip carousel** (net-new) |
| Wed | IIR News (NF) / Playbook | - |
| Thu | IIR News (NF) | **News-repurpose carousel** (repackages the week's strongest NF) |
| Fri | AI Tip of the Week | - |
| Sat | IIR News (NF) | **Evergreen tip carousel** (net-new) |
| Sun | off | *optional: the still-text-video A/B test (see below)* |

Post the carousel several hours apart from that day's Reel (do not stack two posts back to back).
On a light news week, drop to 2 carousels rather than force a third -- the [WOW gate](../editorial-standards.md)
applies here too.

**The still-text-video test (text over moving b-roll):** run it as an **A/B experiment for the
first month, ~1/week**, not as a separate third format. Take one evergreen tip and build it both
ways -- static carousel and text-on-video -- and compare saves and sends. Keep whichever your
audience saves more, then fold the winner into the 3/week. Do not commit to producing both
formats forever; the point is to learn which one this audience rewards. A still-text-video is a
walk-and-talk-adjacent asset, so it needs an `## AI Music Prompt` block (see the music note below).

Revisit this number after four weeks against the saves/sends data, the same way the pillar pivot
gets reviewed.

---

## Body format (Canva-ready)

Write one slide per block, headline + body, exactly like NF-058. The file is a build spec a
human or a VA drops into Canva -- it is copy, not design. Keep design notes at the bottom.

```markdown
## SLIDE 1 -- HOOK
**Headline (large, top third):**
[the hook]
**Subhead (smaller, below):**
[the payoff promise]
```

**Design notes block** at the end covers: which slides carry text weight, the recap slide's
repeatable visual pattern, and the color/logo treatment (default to the brand's dark editorial
look for news carousels; a lighter, cleaner look is fine for evergreen tips).

---

## Captions

Carousels get the same five captions as every post (LinkedIn, Instagram, TikTok as a static/
video crosspost, YouTube Community, Facebook) under the **same rules** as the rest of the repo:

- **Zero em dashes, zero AI-speak, zero engagement-asks** (CLAUDE.md social-caption rule).
- **Front-load one real search phrase** in the first 125 characters (caption-and-hashtag Rule 2).
- **3-5 hashtags**, realtor-first (caption-and-hashtag Rule 1).
- **Optimize for the save and the send**, never for the comment (Rule 3).

The first line of the Instagram caption should echo slide 1's promise so the post reads as one
thing whether someone swipes the images or reads the caption.

---

## Music prompt: only if it ships as video

A **static image carousel needs no music** -- omit the `## AI Music Prompt` block (the NF-058
carousel correctly has none). If the carousel is delivered instead as a **text-on-moving-video**
post (one of the formats D.J. is exploring), it becomes a walk-and-talk-adjacent asset and DOES
need an `## AI Music Prompt` block per CLAUDE.md, tuned per [`docs/ai-music-prompts.md`](../ai-music-prompts.md).
Decide the delivery format up front and follow the matching rule.

---

## Pre-ship checklist

- [ ] Slide 1 names the payoff, not just the topic.
- [ ] Slide 2 works with zero context (re-serve test).
- [ ] Recap slide is self-contained and screenshot-worthy.
- [ ] Close leads with a save reason; any follow ask is small and below it.
- [ ] News-repurpose only: every fact traces to the source script. No new claims.
- [ ] Captions scrubbed for em dashes, AI-speak, engagement-asks (CLAUDE.md).
- [ ] Keyword in the first 125 characters of the IG caption; 3-5 hashtags.
- [ ] `hook_family` differs from the previous carousel.
- [ ] Anti-plagiarism: idea and format borrowed, copy and creative are original.
