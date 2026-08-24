# Chicago Agent Spotlight — Series Standard

Feature one Chicago real estate agent who is currently in the news, on a podcast, or on an award list. D.J. makes a short video celebrating them (a video they are not expecting), tags them, sets it up as a collab, and sends a DM after posting. **Realtors follow realtors**, so a genuine, ego-first spotlight borrows their audience and earns new realtor followers for D.J.

**This is a daily option** in the walk-and-talk brief. Say **"spotlight"** and Claude scouts, verifies, and builds the full unit.

---

## Why it works (two goals, one post)

1. **Amplification / follower growth (primary).** The featured agent and their brokerage reshare, putting D.J. in front of a warm realtor audience. Judge every spotlight on **reshares + new followers, NOT saves** (saves are the tip-carousel metric — see [`../../docs/series/carousel-standard.md`](carousel-standard.md) if present, and the carousel/image strategy).
2. **Warm recruiting touch (secondary).** Each spotlight is a permission-based, ego-first first touch on an agent D.J. could later recruit to Kale. The post-publish DM is what triggers the reshare AND opens the relationship (KIR guest invite first; a flat-fee conversation only much later, warm).

---

## Guardrails (non-negotiable)

- **Never guess a social handle.** Verify the exact Instagram/LinkedIn/Facebook handle before tagging. Tagging the wrong account backfires publicly. If a handle can't be verified, mark it "VERIFY before posting" and do not tag it.
- **Verify the facts.** D.J. gives real, attributable praise. Every claim traces to a named source in the Data Source block (their site, the magazine feature, the award page). No invented stats or quotes.
- **Do not AI-generate the person's face.** Use D.J. talking-head, or screen-record their own public feature/posts WITH on-screen credit. Never fabricate their likeness.
- **Frame on the person + the lesson, never the competitor brokerage's greatness.** Celebrate what the agent does; do not promote the rival brand.
- **No hostile-poaching tone.** This is celebratory. It is not "come to Kale." The recruiting value is the warm relationship, not a pitch in the post.

---

## Scouting sources

Look for a fresh Chicago agent (not one recently featured) in:
- Chicago Agent Magazine (features, Who's Who, top-producer cover stories, Agents' Choice)
- Chicago REALTOR® Magazine (member spotlights, CAR leadership)
- Inman (Chicago hires/moves, Future Leaders, Power Players)
- The Real Deal Chicago
- Award / recognition lists (CAR Rising Star, Chicago Magazine top agents, Five Star)
- Recent podcast guests (including KIR's own archive for a re-feature)

Prefer individual producers (better reshare + a real recruiting angle) but association leaders and newsworthy moves are strong pure-amplification picks. De-dup against past spotlights before choosing.

---

## The unit (what "build the spotlight" produces)

A single file in `scripts/chicago-agent-spotlight/<agent-slug>-<date>.md` containing:

1. **Walk-and-talk script** — the [Viral 3-Act Spine](viral-3-act-spine.md): HOOK (a lesson the audience feels + the reveal) → STORY (the agent's real arc, one turn) → PAYOFF (the lesson for the viewer + the tag/credit). D.J. teaches the lesson the agent embodies; no image of them required. **Target 22-30s, 48-72 spoken words, hard cap 35s / 85 words** (set 2026-08-15, replacing the old 45-60s / 135-word target). At this length the agent's arc is one sentence with one turn, and the lesson is one sentence. The credit and the handle go in the caption and the Verified Tags block, not the spoken script, so tagging costs you no runtime. This series is the one place where **heat stays at 3**, not the default 4: a spotlight points warmth at a person, and friction has no place in it. Follow [`editorial-standards.md`](../editorial-standards.md) and the [AI-tells field guide](../ai-tells-field-guide.md).
2. **`## AI Music Prompt`** — a single **CapCut** prompt (≤300 chars, no Suno/Udio), warm/major-key tribute energy. Per [`../ai-music-prompts.md`](../ai-music-prompts.md).
3. **Five social captions** — LinkedIn (PRIMARY; the relationship/community surface), Instagram Reels, TikTok, YouTube Shorts, Facebook. **No X/Twitter.** No em dashes, no engagement asks, keyword front-loaded (per [`../caption-and-hashtag-strategy.md`](../caption-and-hashtag-strategy.md)).
4. **Verified Tags block** — the confirmed handles + an **IG Collab invite** instruction (the Collab is what surfaces the video to their audience).
5. **Post-publish DM** — the message D.J. sends after posting. This is the reshare trigger and the warm-relationship open. No ask, no pitch.
6. **Companion carousel** — a file in `scripts/carousels/spotlight-<agent-slug>-<date>-carousel.md` repurposed from the same facts (goal: reshares + followers).

**Reference example:** [`../../scripts/chicago-agent-spotlight/dawn-bremer-2026-07-08.md`](../../scripts/chicago-agent-spotlight/dawn-bremer-2026-07-08.md) + its carousel.

---

## Log the carousel to Notion

After building, add a row to the **Daily Carousels** Notion database (https://app.notion.com/p/27267ba77da64ef5a5033fc1dd992a0a) so D.J. can review it on his phone:
- **Carousel** = title, **Date** = today, **Series** = "Chicago Agent Spotlight", **Status** = "Ready", **Slides** = count, **Tag / Collab** = the verified handles + collab note, **Source script** = GitHub link to the carousel file.
- Put the full slide copy in the page body so it reads on mobile without opening GitHub.

---

## 3-pass workflow

Same as every walk-and-talk: draft → stress test (Story Pass first) → EP polish. Deliver only the final. The Story Pass check "no fabricated story" is doubly important here — every specific about a real person must trace to a source.

*Created 2026-07-08. First unit: Dawn Bremer.*
