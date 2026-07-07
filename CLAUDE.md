# Claude Instructions — video-strategy-to-grow-dj-brand

Project-specific operating rules for Claude when working in this repo. Universal editorial rules live in [`docs/editorial-standards.md`](docs/editorial-standards.md); series rules live in `docs/series/`. This file captures workflow defaults that aren't editorial — things Claude should *do every time* without being reminded.

---

## When D.J. says "walk and talk", build today's script on demand

D.J.'s daily options are researched + committed by the 6am home-Mac job and
pushed to his phone (no email anymore). When he says **"walk and talk"** (with or
without a number), follow [`docs/automation/walk-and-talk-on-demand.md`](docs/automation/walk-and-talk-on-demand.md):
`git pull`, read today's `data/news-briefs/<today>.md`, show the numbered options,
let him pick, then build the chosen option through draft → stress-test → EP-polish
and deliver only the final v3 (with the `## AI Music Prompt` block). If today's
brief is missing, offer to run `python3 scripts/news_brief.py` right then.

Every walk-and-talk follows the **Viral 3-Act Spine** ([`docs/series/viral-3-act-spine.md`](docs/series/viral-3-act-spine.md)): HOOK (stop the scroll + promise the payoff) → STORY (the middle is a story with a turn, not a briefing) → PAYOFF (resolve the loop → "here's what you do now" action → loop-back). The stress-test pass runs the **Story Pass** before anything else. Narrative series (Inside the Industry NF/IS/IA, Podcast Promo) run the full three acts; tactical series (Playbook, What Actually Works, tapthis) run a compressed Act 2 -- one story beat, then the payload, and length discipline (Rule 7) wins over story.

For the hook itself, reach into the **Hook Matrix** (Rule 10 in [`docs/editorial-standards.md`](docs/editorial-standards.md)): pick one of the nine families on purpose, log it as `hook_family` in frontmatter, and don't repeat a family across two consecutive posts. Friction families (Sacred Cow, System Indictment, Forbidden) ride heat 4-5 and are capped at once per week (Rule 9.2); they point friction outward at a belief or system and stand with the agent, never at the agent. Swap/List hooks (Family 9: "don't say X, say Y," stop-doing, do-don't-in-the-room) are the default saveable format for tactical series. Roughly every couple of weeks, run one **emotional / identity** script (Rule 10.7) instead of a tip -- a permission slip or why-this-work-matters piece -- because that's what earns follows and the long comments tactics don't. Ready first lines mapped to the nine families live in [`docs/opener-swipe-file.md`](docs/opener-swipe-file.md) -- pull from there before writing a hook cold.

Pair every hook with a **visual open** (pattern interrupt) from [`docs/pattern-interrupt-cheatsheet.md`](docs/pattern-interrupt-cheatsheet.md). D.J. films walk-and-talks on a selfie stick, so the visual open is one of seven one-handed, mid-walk moves (The Stop, Push-In, Whip, Walk-Toward, One Prop, Location Cold-Open, Gesture-On-Beat). Pick one on purpose, log it as `pattern_interrupt` in frontmatter next to `hook_family`, and don't repeat the same move two posts in a row. The spoken hook still does the heavy lifting (captions.ai builds captions from audio); the visual open is the second stop signal. When the script is on-site at a property, prefer the Location Cold-Open -- the property is B-roll you can't otherwise shoot.

## When the script is posted, work the first hour (engagement ops)

These are not editorial -- they're posting-day habits the algorithm rewards harder than anything in the script (Rule 10.4-10.6):

- **Reply to every comment in the first 60 minutes.** Creator replies are weighted for distribution and turn one comment into a thread.
- **Pin a value-extending first comment** -- the exact script, the next step, the receipt/source -- never a "follow me." Drives comment-section dwell without an ask.

---

## Always include an AI Music Prompt with every walk-and-talk script

**Scope:** Any 45-75s talking-head script in this repo. Specifically:
- All `scripts/inside-the-industry/` scripts (NF, IS, IA)
- All `scripts/the-playbook/` scripts
- All `scripts/ai-tip-of-the-week/` scripts
- All `scripts/podcast-promos/` scripts
- Any new short-form talking-head series we add

D.J. calls these "walk-and-talks." They get cut in CapCut and need a music bed at 10-15% volume per [`docs/capcut-editing-playbook.md`](docs/capcut-editing-playbook.md) Part 6.

**The rule:** Every walk-and-talk script must end with an `## AI Music Prompt` section *beneath* the `## Data Source` section. D.J. edits only in CapCut, so there is a single CapCut prompt — no Suno/Udio. Format:

```markdown
## AI Music Prompt

**Vibe:** [one-line description tuned to this specific script's energy]

**CapCut AI Music:**
> [calibrated CapCut prompt, <=300 chars — start from the matching preset in docs/ai-music-prompts.md, then tune BPM/energy/key descriptors to the actual script content]
```

**Where to pull the templates from:** [`docs/ai-music-prompts.md`](docs/ai-music-prompts.md) has CapCut presets for each sub-type (NF default, NF big-number, IS, IA, Playbook, AI Tip of the Week, podcast promo) plus the master template and the troubleshooting table.

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

**Scope:** Every social caption block in every script in this repo (LinkedIn, Instagram Reels, TikTok, YouTube Shorts, Facebook). Applies in addition to the universal Rule 5 in `docs/editorial-standards.md`.

**No X/Twitter captions.** D.J. does not use X. Scripts produce five captions (LinkedIn, Instagram Reels, TikTok, YouTube Shorts, Facebook). Do not add an `### X (Twitter)` block to any script, and remove one if you find it in an older script you're editing.

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

The CapCut prompt is the only music prompt (no Suno/Udio). If a descriptor won't fit, drop the least-important exclusion (`no risers`, `no reverb tails`) rather than ship an over-cap prompt that gets truncated. If a prompt would be meaningfully better at 350-400 chars, flag it and ask whether to split into two CapCut generations.

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

## Building a podcast promo? Use the Hype Machine engine

Any walk-and-talk that promotes a podcast episode (Keeping It Real or Coffee Talk with Tim & D.J.) goes through the engine, not freehand. It turns one episode into a "on this episode we got into X, Y, Z, we solved these problems for agents, here's a tip for your next client" promo.

1. **Build the brief:** `python scripts/podcast-promos/build_promo_brief.py <kir|coffeetalk> <episode-query>` (query matches a guest name or slug fragment). It pulls the episode's own intelligence into the five-beat arc and writes a brief to `scripts/podcast-promos/_briefs/`.
2. **Read the format spec:** [`docs/series/podcast-promo-hype-machine.md`](docs/series/podcast-promo-hype-machine.md) -- the arc, the source adapters, and the full-package output spec.
3. **Check + update the registry:** [`scripts/podcast-promos/promo-registry.md`](scripts/podcast-promos/promo-registry.md). Across 700+ KIR episodes the same tip repeats; verify the hook and tip haven't aired, then add a row.
4. **Output the full package** to `scripts/podcast-promos/<show>-<slug>.md`: spoken script + B-roll + AI music prompt (Podcast promo preset) + all five social descriptions. Reference: [`scripts/podcast-promos/kir-2026-01-30-amanda-pendleton.md`](scripts/podcast-promos/kir-2026-01-30-amanda-pendleton.md).

The tip is the payload: lift one physical, do-it-tomorrow tactic from the episode. No fabricated stats -- every number traces to the analysis JSON (KIR) or the aired script (Coffee Talk).

---

## Other project defaults

- **Editorial voice:** Read [`docs/editorial-standards.md`](docs/editorial-standards.md) before drafting any script. Universal rules win over series rules.
- **Series standards:** Each series has its own standard in [`docs/series/`](docs/series/). The Inside the Industry standard ([`docs/series/inside-the-industry-standard.md`](docs/series/inside-the-industry-standard.md)) is the primary one.
- **CapCut workflow:** [`docs/capcut-editing-playbook.md`](docs/capcut-editing-playbook.md) — including the music volume rule (10-15%) the AI music prompts are calibrated for.
- **Source rigor for NF:** Every NF claim needs a named source, publication date, and URL or case number. No rounding numbers. No "roughly."
- **Always `git fetch` first** when assessing repo state (D.J. works on this repo from 3 different devices).
