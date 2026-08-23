# Podcast Promo: The Hype Machine — Series Format Guide

The operating manual for turning **any podcast episode into a walk-and-talk promo**. One repeatable engine, two shows: **Keeping It Real** (guest interviews) and **Coffee Talk with Tim & D.J.** (stat-driven, no guest). Built to be portable — a third show plugs in by adding one source adapter (see [Source Adapters](#source-adapters)).

**Before writing any promo, read [`../editorial-standards.md`](../editorial-standards.md).** Universal rules win over anything here: no fabricated stats, no em dashes (use `--`), straight quotes, contractions in every spoken line, "D.J. Paris" with periods. Music rules live in [`../ai-music-prompts.md`](../ai-music-prompts.md) (Podcast promo preset). This file only defines what's specific to the hype-machine format.

---

## What This Series Is

**A 22-30 second talking-head promo that makes an agent feel they cannot afford to skip this episode.** Hard cap 35s / 85 spoken words. Set 2026-08-15, replacing the old 60-70 second target.

**This is the series the new length hurts most, and here is how it survives.** The old five-beat arc named three topics *and* delivered a tip in 65 seconds. At 60 words that does not fit. The resolution: **name one topic, not three, and keep the tip.** The tip is what makes the promo useful rather than promotional, so it never gets cut. The X-Y-Z beat collapses from three topics to the single most surprising one, and the episode's breadth is sold in the caption, where it costs nothing. It is not a recap. It is a hype machine. The job is to take the episode's raw intelligence and compress it into one irresistible pitch:

> "On this episode, [we / guest and I] got into X, Y, and Z. Here's what we actually solved for agents. And here's the one tip that'll help you with your next client."

The promo lives or dies on **specificity stolen from the episode** — a real number, a real tactic, a real quote. Generic ("great conversation about mindset") is failure. The episode already did the work; the promo's only job is to pick the sharpest three things and frame them as a reason to listen tonight.

## What This Series Is NOT

- Not a full recap or summary. Pick the three sharpest beats, leave the rest.
- Not a guest bio reel. The guest's credibility is a credibility *token*, not the subject.
- Not generic. "We talked about social media" is dead on arrival. "She keeps a white duvet in her trunk and it's worth thirty grand a listing" is the bar.
- Not a follow-beg. The CTA is "go listen, then do this one thing" — a real offer, not an engagement ask (editorial Rule 4).

---

## The Arc (5 beats, ~25 seconds)

**3-act spine: compressed, like every other series since 2026-08-15.** A promo is a trailer, and a trailer is a story, so it still runs the [Viral 3-Act Spine](viral-3-act-spine.md) -- but the full narrative version this series used to claim is gone. Act 2 is one sentence. Each of the five beats below is now **one sentence, and beats 2 and 3 usually merge into one**: the single topic and the problem it solves are the same sentence. The episode is the story; the promo's job is to make the viewer feel they cannot miss it. The five beats map onto the three acts: **The Hook** = Act 1 (stop the scroll + promise the payoff, the one irresistible thing). **The X-Y-Z + What We Solved** = Act 2 (the story of what the episode actually opened up, with the "what we solved" turn -- the moment it stops being topics and becomes a fix the viewer needs). **The Tip + The Close** = Act 3 (resolve: hand over the one usable tip -> the "go listen, then do this" action -> a loop-back to the hook). Steal the story from the episode; never invent one (universal Rule 1 -- every claim traces to the analysis JSON or the aired script).

Every promo, both shows, hits these five beats in order. The scroll-stopper is the **first spoken line** (captions.ai renders audio only — no on-screen-text-only hooks).

| # | Beat | Job | Source field (KIR) | Source field (Coffee Talk) |
|---|------|-----|--------------------|----------------------------|
| 1 | **The Hook** | One spoken line that stops the scroll. Steal the single most surprising number, tactic, or contradiction in the episode. | sharpest of `clip_worthy_moments.quote` / `quotable_insights` / a `key_tactics` line | the central hook stat |
| 2 | **The X-Y-Z** | "On this episode, [guest and I / Tim and I] got into..." Name **ONE** topic in plain agent language, the most surprising one, not the show's words. (Was three topics; cut to one 2026-08-15 for the 25s runtime. Sell the breadth in the caption, where it is free.) | strongest of `main_topics` | `Topic Category` |
| 3 | **What We Solved** | The proof beat. Name 1-2 *problems agents actually have* and that the episode answers. This is the "solved these problems for agents" line. | 1-2 `problems_addressed.specific_problem` + the gist of `solution_summary` | the agent problem the stat exposes |
| 4 | **The Tip** | "Here's the one thing you can use with your next client." Lift ONE concrete, do-it-tomorrow tactic from the episode. Must be specific enough to act on without listening. | best `key_tactics.tactic` or the tactical `clip_worthy_moments` | the episode's "3 action steps" — pick the most portable one |
| 5 | **The Close** | "Here's what you do now": go listen (where), and apply the tip. A real CTA, never a follow-beg. | episode link / "this week's KIR" | "this week's Coffee Talk" |

**The tip is the payload, and at 60 words it is the beat that never gets cut.** An agent should be able to skip the episode, do only the tip, and still win — and feel guilty enough about skipping that they listen anyway. If the tip is vague, the promo failed. When the script runs long, cut in this order: the second topic (already gone), the guest's credential stack, the problem beat's second problem, the close's wind-up. The tip stands last. Pull the most *physical, specific* tactic available (the duvet, the exact text script, the 5-minute callback), not the abstraction ("stay in touch").

---

## Source Adapters

The engine is show-agnostic. Each show is just a different way of filling the five beats. The brief-builder ([`../../scripts/podcast-promos/build_promo_brief.py`](../../scripts/podcast-promos/build_promo_brief.py)) reads the source and emits a filled brief.

### KIR adapter (guest interviews)
- **Source:** `~/GitHub Projects/keeping-it-real-content-system/data/analysis/<episode>_analysis.json`
- **Frame:** "[Guest], [credential], came on the show and..." The guest is the authority; D.J. is the host who pulled the value out.
- **Credibility token:** Use `guest_info.title` / `company` / `production_level` in ONE compressed line (beat 2 or 3). Trim hard.
- **Tip source priority:** `key_tactics` > tactical `clip_worthy_moments` > `problems_addressed.solution_summary`.

### Coffee Talk adapter (Tim & D.J., stat-driven, no guest)
- **Source:** the aired script in `~/GitHub Projects/coffeetalk-episode-registry/scripts/<episode>.md` + its row in `registry.md`.
- **Frame:** "Tim and I opened this week's Coffee Talk with [stat], and here's why it should scare you / change what you do Monday."
- **Tip source:** the episode's 3 required action steps — pick the single most portable one for beat 4.
- **Stat discipline:** every stat in the promo must already exist in the aired episode. Do NOT introduce a new stat the episode didn't make. Cross-check against `registry.md` like the generator does.

### Adding a third show
Add an adapter section here + a loader branch in the brief-builder. The arc and output spec do not change.

---

## Output: The Full Package

Every promo is a single `.md` in [`../../scripts/podcast-promos/`](../../scripts/podcast-promos/), named `<show>-<guest-or-slug>-<date>.md` (e.g. `kir-amanda-pendleton-2026-01-30.md`). It contains, in order:

1. **Frontmatter** — `type`, `show`, `episode`, `source_analysis` (path), `cta`, `listen_url`, `target_duration: "22-30 seconds"`, `word_count`, `placement`.
2. **The WOW line** — one blockquote at the top: the promo's whole reason to exist, for the editor/D.J. to gut-check before filming.
3. **`## Spoken Script (D.J. — to camera, walking)`** — the five beats as natural spoken paragraphs. Contractions everywhere. No stage directions inside the spoken lines.
4. **`## B-Roll Cues (for the editor)`** — a beat-by-beat table. For KIR, cue the episode's video / guest clip if assets exist; otherwise D.J. talking-head + episode cover. Music ducks under any clip audio.
5. **`## Data Source`** — every field pulled, with the analysis-JSON path and timestamps so claims are auditable (editorial source-rigor rule).
6. **`## AI Music Prompt`** — Podcast promo preset from [`../ai-music-prompts.md`](../ai-music-prompts.md), tuned to the episode's energy (warm/major for an upbeat guest; a touch more grounded for a heavy topic). Single CapCut prompt (D.J. edits only in CapCut, no Suno/Udio), `no vocals` first, BPM as a number, ≤300 chars.
7. **`## Social Descriptions`** — IG, TikTok, YouTube Shorts, Facebook, LinkedIn, each tuned to its platform's passive signal and link-delivery rule (IG/TikTok = link in bio, YT = pinned comment, FB/LinkedIn = link in post). Plus a hashtag quick-reference.

Match the structure of the reference promo: [`../../scripts/podcast-promos/breakthrough-with-michael-ep1-emma-cta.md`](../../scripts/podcast-promos/breakthrough-with-michael-ep1-emma-cta.md).

---

## Dedup Protocol (non-negotiable)

The KIR catalog is 700+ episodes. Across that many promos, the same takeaway ("stay in touch with past clients") will surface again and again and the feed goes stale. Before finalizing any promo:

1. Read [`../../scripts/podcast-promos/promo-registry.md`](../../scripts/podcast-promos/promo-registry.md).
2. Check your planned **hook** and **tip** against the `Hook Used` and `Tip Used` columns.
3. If the tip already aired in another promo, pick a *different* tactic from the same episode. If the episode only has one usable tip and it's taken, flag it in the promo's notes and lead with a different angle (a quote or a contradiction).
4. After finalizing, add a row to the registry: date, show, episode, hook, tip, topic.

For Coffee Talk, this stacks on top of the existing stat registry — the stat dedup still applies first.

---

## Quick Checklist (before delivering)

- [ ] Hook is the **first spoken line** and steals the episode's single most surprising thing.
- [ ] X-Y-Z names three real topics in agent language, not the show's words.
- [ ] "What we solved" names a real agent problem, not a category.
- [ ] The tip is **physical and specific** — actionable without listening.
- [ ] Close is "here's what you do now" (listen + apply), not a follow-beg.
- [ ] Hook and tip checked against `promo-registry.md`, and a new row added.
- [ ] Zero em dashes / en dashes. Straight quotes. Contractions in every spoken line.
- [ ] Every number/claim traces to the episode (KIR analysis JSON or aired Coffee Talk script). No new stats.
- [ ] AI Music Prompt block present, tuned, `[no vocals]` first.
- [ ] All five social descriptions present with correct link-delivery per platform.
