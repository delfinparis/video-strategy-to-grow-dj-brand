# YouTube Archive Clip Play (Plan)

An execution-ready plan to mine the 700+ episode Keeping It Real video archive for short and long clips, the "Bartlett play" that [`docs/platform-strategy.md`](../platform-strategy.md) has flagged as the brand's biggest unleveraged asset. Source material confirmed: most episodes have video recordings, so this is real talking-head/interview clipping, not audiograms. Ramp decision at the July 19 review.

---

## The opportunity

Steven Bartlett built Diary of a CEO by clipping the most explosive 45-90 seconds of each interview as standalone content. D.J. has 700+ recorded interviews with top-producing agents sitting unused. The archive is a content library most creators would pay for and D.J. already owns.

Two output types, two jobs:

- **Shorts (45-90s vertical):** hook-first clips of the single best moment per episode. Distribution play. Posts to YouTube Shorts and cross-posts to Instagram, TikTok, Facebook, and LinkedIn (native). Feeds reach and the recruiting funnel.
- **Long clips (5-12 min, 16:9):** standalone segments on the main YouTube channel. The Bartlett core. Builds the 700-episode archive into a searchable, evergreen YouTube presence and grows the brand's largest raw audience.

---

## Reuse what already exists (do not build from scratch)

This workstream plugs into systems the repo already has:

- **Episode intelligence + the Hype Machine engine.** [`scripts/podcast-promos/build_promo_brief.py`](../../scripts/podcast-promos/build_promo_brief.py) already pulls an episode's own intelligence (the KIR analysis JSON) into a structured arc, and the format spec lives in [`docs/series/podcast-promo-hype-machine.md`](../series/podcast-promo-hype-machine.md). The same intelligence that finds a promo's "tip payload" can surface clip candidates: the moment in the interview where the guest says the one thing worth clipping. Start clip selection from that intelligence, not by re-watching episodes cold.
- **The CapCut workflow.** [`docs/capcut-editing-playbook.md`](../capcut-editing-playbook.md) (captions, the 10-15% music bed) and the AI music presets already define how a clip gets cut. Clips use the same pipeline.
- **The caption/hashtag standard.** [`docs/caption-and-hashtag-strategy.md`](../caption-and-hashtag-strategy.md) governs every title, description, and hashtag set. YouTube titles and descriptions are keyword-first (D.J.'s existing YouTube descriptions are already the model).

---

## Phase 1: prove the workflow (beachhead, ~3-4 weeks to July 19)

Do not start by processing 700 episodes. Prove the pipeline on a small, high-value batch first.

1. **Pick 8-12 beachhead episodes.** Selection priority: highest-download episodes, biggest-name guests, and evergreen tactical interviews (a concrete agent tactic dates slowly). Avoid news-pegged episodes that have aged out.
2. **Surface clip candidates per episode** using the episode intelligence (the same source `build_promo_brief.py` reads). Target 1 Short candidate and 1 long-clip candidate per episode. The Short candidate is the single most clip-worthy 45-90s moment (a surprising number, a contrarian take, a permission-slip line, a named tactic). The long-clip candidate is a 5-12 min self-contained segment with a clear question and payoff.
3. **Cut in CapCut** per the playbook: captions burned in, music bed at 10-15%, hook in the first 2 seconds.
4. **Title + describe per the caption standard:** keyword-first title under 70 chars, description that names the guest, the topic, and the searchable phrase, 3-5 hashtags including #shorts on the Shorts.
5. **Publish on a fixed cadence:** start at 1 Short + 1 long clip per week. Shorts cross-post to IG/TikTok/FB/LinkedIn (native uploads, not links).

---

## What to measure

Per clip, logged with the weekly metrics:

- **Shorts:** views, average view duration / completion, swipe-away rate, subscribers gained, cross-platform reach.
- **Long clips:** views, average view duration (the YouTube signal that matters most), watch-time hours, subscribers gained.
- **Funnel tie-in:** any profile/channel-driven movement toward the recruiting funnel (tapthis.co, channel subscribes that convert to podcast listeners).

---

## Decision criteria (July 19 ramp review)

- **Ramp up** (scale the cadence, work deeper into the archive, consider a VA or editor for volume) if the beachhead clips show meaningful watch-time and subscriber growth versus the channel's current baseline, at an effort cost that's sustainable.
- **Hold at low cadence** if clips perform but the per-clip effort is too high to scale without help.
- **Reprioritize** if Shorts and long clips both underperform the existing IIR distribution, the archive stays a someday-asset and effort goes back to LinkedIn-first IIR.

---

## Open decisions for D.J. (gate the build, not the plan)

1. **Who edits at volume?** D.J., or a VA/editor handed a repeatable spec. The pipeline above is designed to be handed off; phase 2 scale likely needs an editor.
2. **Where do the archive video files live, and how accessible are they?** Phase 1's first task is confirming the 8-12 beachhead episodes' video files are retrievable and in usable quality.
3. **Helper tooling.** If phase 1 proves out, a small `clip_candidates.py` (reusing the episode-intelligence reader from `build_promo_brief.py`) could auto-surface the top clip moment per episode and scaffold the title/description. Worth building only after the manual workflow proves the clips perform.

---

## Owner and timeline

- **Owner:** D.J. for phase 1 selection + editing; revisit staffing at July 19.
- **Start:** pick the 8-12 beachhead episodes this week; first clip out within the test window.
- **Read-out:** July 19 pivot review, as the ramp/hold/reprioritize decision.

*Plan written 2026-06-14. Phase 1 is a proof, not a launch. The 700-episode scale is earned by the beachhead clips performing, not assumed.*
