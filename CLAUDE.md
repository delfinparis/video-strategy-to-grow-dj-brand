# Claude Instructions — video-strategy-to-grow-dj-brand

Project-specific operating rules for Claude when working in this repo. Universal editorial rules live in [`docs/editorial-standards.md`](docs/editorial-standards.md); series rules live in `docs/series/`. This file captures workflow defaults that aren't editorial — things Claude should *do every time* without being reminded.

---

## When D.J. says "walk and talk", build today's script on demand

D.J.'s daily options are researched + committed by the 6am home-Mac job and
pushed to his phone (no email anymore). When he says **"walk and talk"** (with or
without a number), follow [`docs/automation/walk-and-talk-on-demand.md`](docs/automation/walk-and-talk-on-demand.md):
`git pull`, read today's `data/news-briefs/<today>.md`, show the numbered options,
let him pick, then build the chosen option through draft → stress-test → EP-polish
→ council review and deliver only the final v3 (with the `## AI Music Prompt` block
and the `## Council Review` block). If today's brief is missing, offer to run
`python3 scripts/news_brief.py` right then.

**The four passes are non-negotiable. Run them silently, deliver only the final v3.** Even when
the first draft looks strong, never skip straight to delivery. Each pass has a concrete job:

- **Pass 1 — Draft.** Build to the 3-act spine, a deliberate hook family, a pattern interrupt, the `## AI Music Prompt` block, and all five captions. The HOOK opens with a standalone **scroll-stop** first spoken line (rule below).
- **Pass 2 — Stress-test.** Run the **Story Pass** ([`docs/series/viral-3-act-spine.md`](docs/series/viral-3-act-spine.md)) first: does Act 2 have a real turn, not a briefing? Then the **scroll-stop test**: read only the first spoken line — does it stop the scroll on its own in 3 seconds, or is it warm-up? Then the hook 3-second test, the AI-tells scrub ([`docs/ai-tells-field-guide.md`](docs/ai-tells-field-guide.md)), and for NF confirm every claim has a named source + date + URL. Fix what fails before polishing.
- **Pass 3 — EP-polish.** Cut to length (Rule 7), sharpen the shareable moment to one sendable line, read the close aloud and kill any motivational-poster ending, then run the caption + hashtag-cap scrub below. Then hand v3 to Pass 4.
- **Pass 4 — Council review.** Run the finished v3 through the Short-Form Council ([`docs/short-form-council-pass.md`](docs/short-form-council-pass.md)): ten creator/marketer doctrines plus two research witnesses (Heath on curiosity mechanics, Berger on shareability) pressure-test the hook, retention, and shareability. Append a `## Council Review` block beneath v3 with 2-3 tested **spoken** scroll-stop variants mapped to hook families, a one-line why-it-works (hook mechanism / share driver / retention move), and the single dissent to A/B test next. It never adds manual on-screen text (captions build from audio) and never undoes a Pass-3 scrub. If the local deep-reference skill is installed (`~/.claude/skills/short-form-council`), load its book-backed `references/*.md` for depth; otherwise run from the doctrines in the doc. Then deliver v3 (script + AI Music Prompt + Council Review).

**The 0:00 scroll-stop is mandatory, and it is spoken.** The first line out of D.J.'s mouth (0:00-0:03) has to stop the scroll on its own, before any context. captions.ai builds the on-screen captions from the audio, so the scroll-stop lives in the **spoken** first line, never a manual text overlay (that is why `scripts/strip_onscreen_text_v2.py` exists). Every walk-and-talk `### HOOK` beat opens with it:

- **Front-load the tension in the first 3-5 words.** "NAR just changed what you owe your seller" stops the scroll. "Today I want to talk about some new NAR guidance" does not.
- **One complete, arresting line that opens a loop** the video then closes. No warm-up, no "hey guys," no throat-clearing sentence before it.
- **50-60% of all drop-off happens in the first 3 seconds** (2026 retention math, [`docs/hook-matrix-cheatsheet.md`](docs/hook-matrix-cheatsheet.md)). The scroll-stop is the whole distribution lever, not a nicety.
- **Pull a ready first line from [`docs/opener-swipe-file.md`](docs/opener-swipe-file.md)** mapped to the chosen `hook_family`, then sharpen it to the specific news. Never write the hook cold.

Before delivering the v3, run every social caption AND its hashtag block through the
scrub in the **Social descriptions** section below: no em dashes, no AI-speak, and the
**hashtag caps** from [`docs/caption-and-hashtag-strategy.md`](docs/caption-and-hashtag-strategy.md)
(LinkedIn/IG/TikTok/YouTube 3-5, Facebook 2-3, realtor-first, one brand tag). This runs
every time, without D.J. asking. Do not copy hashtag counts from older example scripts.

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
- **Hashtag caps from [`docs/caption-and-hashtag-strategy.md`](docs/caption-and-hashtag-strategy.md), applied at draft time.** LinkedIn/Instagram/TikTok/YouTube Shorts = **3-5 hashtags**, Facebook = **2-3**. Realtor-first, exactly one brand tag (`#InsideTheIndustry` or `#KeepingItRealPodcast`), drop the long tail (`#RealtorLife`, `#RealEstateCoaching`, `#realtortok`, generic community tags). Fewest hashtags that still categorize the post. Do the discovery work with a real search keyword in the first line/125 chars, not a tag stack (Rule 2 of that doc).
- **Never copy hashtag counts from an older example script.** Scripts written before 2026-07-07 (NF-060 and earlier) carry the retired 11-14 tag stacks. Build the hashtag block fresh from the caps above every time; do not lift it from a reference file.
- **Apply this automatically every time.** Do not wait for the user to ask for the scrub. Any script draft, polish pass, or rewrite that includes social descriptions must run the descriptions AND the hashtag block through this filter before commit.

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

## Doing a Chicago Agent Spotlight? Follow the standard

When D.J. says **"spotlight"** (or picks the Chicago Agent Spotlight option in the daily brief), build it per [`docs/series/chicago-agent-spotlight-standard.md`](docs/series/chicago-agent-spotlight-standard.md). Scout one fresh Chicago agent in the news, **verify the social handle before tagging** (never guess), verify every fact to a named source, and never AI-generate the person's face. Frame on the person + the lesson, not the rival brokerage; no poaching tone. Build the full unit (walk-and-talk + companion carousel + verified tags + post-publish DM), then log the carousel to the **Daily Carousels** Notion database (https://app.notion.com/p/27267ba77da64ef5a5033fc1dd992a0a) with the full slide copy in the page body. Judge these on reshares + followers, not saves. Reference: [`scripts/chicago-agent-spotlight/dawn-bremer-2026-07-08.md`](scripts/chicago-agent-spotlight/dawn-bremer-2026-07-08.md).

## Other project defaults

- **Editorial voice:** Read [`docs/editorial-standards.md`](docs/editorial-standards.md) before drafting any script. Universal rules win over series rules.
- **Series standards:** Each series has its own standard in [`docs/series/`](docs/series/). The Inside the Industry standard ([`docs/series/inside-the-industry-standard.md`](docs/series/inside-the-industry-standard.md)) is the primary one.
- **CapCut workflow:** [`docs/capcut-editing-playbook.md`](docs/capcut-editing-playbook.md) — including the music volume rule (10-15%) the AI music prompts are calibrated for.
- **Source rigor for NF:** Every NF claim needs a named source, publication date, and URL or case number. No rounding numbers. No "roughly."
- **Always `git fetch` first** when assessing repo state (D.J. works on this repo from 3 different devices).
