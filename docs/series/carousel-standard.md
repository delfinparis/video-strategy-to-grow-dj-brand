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

**Primary job: reach and saves** (set 2026-07-07). A carousel earns its slot when an agent
would *save* it to act on later or *send* it to another agent. That is a different job than the
walk-and-talk videos, which carry the recruiting-first load. Carousels grow follows and
authority; recruiting is the soft secondary.

**Two lanes, run roughly evenly:**

- **News-repurpose:** turn an existing Inside-the-Industry (NF/IS/IA) script into a carousel.
  Same facts, same sourcing, no new claims. Lowest new effort. Model: the NF-058 example.
- **Evergreen tip:** net-new saveable how-to (scripts, objection handling, marketing tactics,
  data cards) modeled on Coffee & Contracts / Jimmy Mackin / Chelsea Peitz. Not tied to a script.

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
| **N-1 -- Saveable recap** | The "save this" payload | The numbered list, the checklist, the scripts. This is the slide people screenshot. Make it self-contained. |
| **N -- Close** | Save prompt first, soft CTA second | Lead with a reason to save ("save this for the next time..."). The follow ask is small and below it. Never an engagement-bait CTA. |

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
