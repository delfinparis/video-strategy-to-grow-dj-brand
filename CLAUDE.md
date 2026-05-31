# Claude Instructions — video-strategy-to-grow-dj-brand

Project-specific operating rules for Claude when working in this repo. Universal editorial rules live in [`docs/editorial-standards.md`](docs/editorial-standards.md); series rules live in `docs/series/`. This file captures workflow defaults that aren't editorial — things Claude should *do every time* without being reminded.

---

## Always include an AI Music Prompt with every walk-and-talk script

**Scope:** Any 45-75s talking-head script in this repo. Specifically:
- All `scripts/inside-the-industry/` scripts (NF, IS, IA)
- All `scripts/the-playbook/` scripts
- All `scripts/ai-tip-of-the-week/` scripts
- All `scripts/podcast-promos/` scripts
- Any new short-form talking-head series we add

D.J. calls these "walk-and-talks." They get cut in CapCut and need a music bed at 10-15% volume per [`docs/capcut-editing-playbook.md`](docs/capcut-editing-playbook.md) Part 6.

**The rule:** Every walk-and-talk script must end with an `## AI Music Prompt` section *beneath* the `## Data Source` section. Format:

```markdown
## AI Music Prompt

**Vibe:** [one-line description tuned to this specific script's energy]

**Suno / Udio:**
> [calibrated prompt — start from the matching preset in docs/ai-music-prompts.md, then tune BPM/energy/key descriptors to the actual script content]

**CapCut AI Music:**
> [short version of the same prompt — 1-2 sentences, same DNA]
```

**Where to pull the templates from:** [`docs/ai-music-prompts.md`](docs/ai-music-prompts.md) has presets for each sub-type (NF default, NF big-number, IS, IA, Playbook, AI Tip of the Week, podcast promo) plus the master template and the troubleshooting table.

**Don't just paste the preset verbatim.** Tune it:
- **BPM:** 90 for sober/legal news, 95 default NF, 100 for big-number / scoreboard moments, 105-108 for tactical/upbeat, 90 for reflective synthesis.
- **Energy descriptor:** Match the script's emotional register. A $52M settlement is "urgent but controlled." A "five brokerages in three months" scoreboard is "confident with forward momentum." A reflective IS about top producers is "warm and authoritative."
- **Key feel:** Default minor-key-but-hopeful. Major-leaning for Playbook/AI Tip/Podcast Promo. Avoid pure-dark minor unless the news genuinely warrants it (it almost never does).

**Non-negotiables in every prompt** (these are what make tracks voiceover-safe):
- `[no vocals]` or `instrumental only` at the **start** of the style prompt
- `no melodic hook, no vocal chops, no risers, no whooshes`
- `unobtrusive background for voiceover` or `doesn't compete with speech`
- `loopable`
- Specify BPM as a number

**When in doubt:** Use the NF default preset from [`docs/ai-music-prompts.md`](docs/ai-music-prompts.md) and tune from there.

---

## When updating older scripts

If you're editing a script that doesn't have an `## AI Music Prompt` section yet, add one. Don't ask first — it's a known gap from before this rule existed.

---

## What walk-and-talk does NOT include

These series don't need an AI Music Prompt block (different format or already-set audio):
- `scripts/agent-tip-of-the-day/` — frozen / curation-pending, don't touch
- `scripts/ai-agent-minute/` — frozen, don't touch
- `scripts/reels/` — these are generated assets, not scripts
- `data/news-briefs/` — these feed scripts, they're not scripts themselves

---

## Social descriptions: no em dashes, no AI speak

**Scope:** Every social caption block in every script in this repo (LinkedIn, Instagram Reels, TikTok, YouTube Shorts, Facebook, X, Threads). Applies in addition to the universal Rule 5 in `docs/editorial-standards.md`.

**The rule:** Social captions get the strictest scrub.

- **Zero em dashes.** Not `—`. Not `--` (the editorial-standards substitute). Use periods, commas, or restructure the sentence. The `--` substitute is fine in spoken-script sections, length justifications, and Data Source notes; it is banned in social captions because it reads as AI-generated copy on a social feed.
- **Zero AI-speak transitions.** No "Here is what this means," "Here is the part that makes this interesting," "Here is why that matters," "Worth noting," "That should change everything," "In a market like this," or any of the banned AI-speak words from Rule 5.
- **Zero throat-clearing setups.** A new paragraph in a social caption should not begin with a transition sentence whose only purpose is to set up the next sentence. Cut the transition; lead with the substance.
- **Apply this automatically every time.** Do not wait for the user to ask for the scrub. Any script draft, polish pass, or rewrite that includes social descriptions must run the descriptions through this filter before commit.

If a sentence in a social caption needs a pause that an em dash would normally create, restructure as two short sentences. "X. Y." beats "X -- Y." in every social-feed context.

---

## CapCut AI Music prompts: 300-character hard cap

**Scope:** Every CapCut AI Music prompt this repo produces, whether it lives in the `## AI Music Prompt` section of a script or is sent inline in a chat reply.

**The cap:** 300 characters maximum, including spaces and punctuation. CapCut's AI music input has a hard 300-char limit; longer prompts get truncated silently and the generator works from a partial input.

**What a CapCut prompt must include in 300 chars:**

1. Style / genre (e.g., "modern documentary editorial score")
2. BPM (e.g., "95 BPM")
3. Mood, 2-4 words (e.g., "authoritative, confident, verdict-in")
4. 3-4 instruments max (e.g., "muted piano, pulsing synth bass, soft percussion")
5. The "no vocals" constraint (always)
6. Runtime hint (e.g., "55-60s")

**What goes in the longer Suno/Udio prompt instead** (no character cap):
- Reference artists or shows (Bloomberg, NYT Daily, etc.)
- Full energy arc descriptions
- Specific harmonic guidance
- Mix instructions

If a CapCut prompt would be meaningfully better at 350 or 400 characters, flag it to the user and ask whether to split into two CapCut generations rather than ship an over-cap prompt that gets truncated.

---

## AI tells: scrub against the field guide before commit

**Scope:** Every script section and every social caption block this repo produces. Reference: [`docs/ai-tells-field-guide.md`](docs/ai-tells-field-guide.md).

**The rule:** Read the field guide mentally before drafting. The vocabulary bans (banned adjectives, verbs, metaphorical nouns, hedging markers, transition phrases, promotional buzzwords, conclusion clichés) apply automatically. The "Used Once" patterns (negative parallelisms, Rule of Three, contrast structure, data-as-character personification, aphoristic closes, triple-word repetition, "Here's the [adjective] part" reveals) must be deployed deliberately and never stacked within the same script.

**Apply at draft time, not as follow-up scrub.** If you catch yourself reaching for "delve," "tapestry," "It's not X, it's Y," or any of the patterns on the field guide list -- pick a different construction before writing it.

**Pre-commit self-audit** (per the field guide's Part 8 checklist):

- Scan every social caption for em dashes (`-` or `--`). Restructure if present.
- Count "It's not X, it's Y" / "Not just X, but Y" constructions. Max one per script.
- Count Rule-of-Three constructions (triple lists + triple adjectives + triple-word staccato). Max one per script.
- Scan against the vocabulary lists in Parts 1 of the field guide.
- Read the close aloud. If it sounds like a motivational poster, rewrite.
- Check the action layer count -- if every recent script opens with "Three plays," vary it.
- Scan for self-answered rhetorical questions.
- Verify hedging language is intentional, not reflexive.

**If a pattern works hard and earns its place, keep it.** The discipline is about not stacking, not about banishing every rhetorical move. One sharp "It's not X, it's Y" lands; three in the same script reads as AI.

**When the field guide and a script's specific editorial framing conflict:** the field guide wins unless there's a specific reason to override, documented in the script's Production Notes.

---

## Other project defaults

- **Editorial voice:** Read [`docs/editorial-standards.md`](docs/editorial-standards.md) before drafting any script. Universal rules win over series rules.
- **Series standards:** Each series has its own standard in [`docs/series/`](docs/series/). The Inside the Industry standard ([`docs/series/inside-the-industry-standard.md`](docs/series/inside-the-industry-standard.md)) is the primary one.
- **CapCut workflow:** [`docs/capcut-editing-playbook.md`](docs/capcut-editing-playbook.md) — including the music volume rule (10-15%) the AI music prompts are calibrated for.
- **Source rigor for NF:** Every NF claim needs a named source, publication date, and URL or case number. No rounding numbers. No "roughly."
- **Always `git fetch` first** when assessing repo state (D.J. works on this repo from 3 different devices).
