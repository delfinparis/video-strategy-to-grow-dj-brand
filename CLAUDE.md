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

## Other project defaults

- **Editorial voice:** Read [`docs/editorial-standards.md`](docs/editorial-standards.md) before drafting any script. Universal rules win over series rules.
- **Series standards:** Each series has its own standard in [`docs/series/`](docs/series/). The Inside the Industry standard ([`docs/series/inside-the-industry-standard.md`](docs/series/inside-the-industry-standard.md)) is the primary one.
- **CapCut workflow:** [`docs/capcut-editing-playbook.md`](docs/capcut-editing-playbook.md) — including the music volume rule (10-15%) the AI music prompts are calibrated for.
- **Source rigor for NF:** Every NF claim needs a named source, publication date, and URL or case number. No rounding numbers. No "roughly."
- **Always `git fetch` first** when assessing repo state (D.J. works on this repo from 3 different devices).
