# AI Music Prompts for Walk-and-Talk Reels

How to generate background music for D.J.'s walk-and-talk reels (Inside the Industry NF/IS/IA, The Playbook, AI Tip of the Week — anything that's 45-75s of D.J. talking to camera).

This is the practical reference. Copy the templates, fill in 2-3 variables, paste into Suno / Udio / CapCut AI Music. Music goes **under** the voice at 10-15% volume max (per [`capcut-editing-playbook.md`](capcut-editing-playbook.md) Part 6) — its only job is to keep the viewer's nervous system engaged, never to compete with what D.J. is saying.

---

## The One Rule

**Music never out-talks D.J.** Every prompt in this doc is calibrated to produce subtle, non-melodic, voice-friendly beds. If a generated track has a hook line you start humming, it's wrong for the reel. Regenerate.

---

## What the research says (the short version)

These principles came out of testing Suno, Udio, and CapCut AI Music against creator/voiceover benchmarks. They're what the templates below are built on:

1. **Describe, don't command.** "Upbeat lo-fi instrumental, 95 BPM" beats "Make me an upbeat song." Front-load the genre and mood.
2. **Be explicit about no vocals.** Put `[no vocals]` or `instrumental only` at the **start** of the style prompt. In Suno, also put `[Instrumental]` in the lyrics field (or leave it empty). Both belt-and-suspenders.
3. **4-7 descriptors is the sweet spot.** Fewer = generic. More = the model gets confused and produces mush.
4. **Name 2-3 specific instruments, not categories.** "Warm Rhodes, soft kick, subtle pad" beats "electronic."
5. **Specify intent for voiceover.** Phrases that work: `background music`, `unobtrusive`, `subtle energy`, `doesn't compete with voice`, `loopable`, `clean low-end`.
6. **Specify what NOT to include.** `no risers`, `no whooshes`, `no melodic hook`, `no four-on-the-floor`, `no reverb tails` — exclusions are as important as inclusions for VO beds.
7. **BPM matters more than you think.** Walk-and-talks land best in the **90-110 BPM** range. Slower feels funereal under D.J.'s pacing; faster fights his cadence.
8. **Avoid artist names.** "Style of [artist]" gets watered-down results and risks rights issues. Use era + genre instead ("late-90s trip-hop," "modern corporate-cinematic").

Sources at the bottom.

---

## D.J.'s house sound (start here every time)

This is the default vibe for an NF (news-reactive) walk-and-talk. Modern, slightly tense, authoritative — the audio equivalent of "I have inside information and you should listen."

**Genre lane:** Modern corporate-cinematic, light electronic underscore, neutral-but-confident.
**BPM:** 95-105 (90 for sober/legal news, 105-110 for high-energy market wins).
**Key feel:** Minor key, but not dark. Think Bloomberg explainer, not true crime.
**Instrumentation:** Soft pulsing synth pad, muted plucked synth or Rhodes, light kick, subtle hi-hat shuffle, occasional restrained string layer.
**What to avoid:** Lead melodies, vocal chops, big drops, risers, "epic trailer" brass, lo-fi vinyl crackle (too casual for industry news), tropical house anything.

---

## Master template (use this 80% of the time)

### Suno / Udio (long prompt — paste into "Style of Music" field)

```
[no vocals] modern corporate cinematic underscore, instrumental only, {ENERGY}, {BPM} BPM,
soft pulsing synth pad, muted plucked synth, light kick, subtle hi-hat,
restrained string layer, clean low end, minor key but hopeful,
unobtrusive background music for voiceover, doesn't compete with speech,
loopable, no melodic hook, no vocal chops, no risers, no whooshes,
no reverb tails, no four-on-the-floor kick
```

**Lyrics field (Suno):** `[Instrumental]` — or leave empty.

**Variables to fill in:**
- `{ENERGY}` — pick one: `subtle energy` / `confident and steady` / `urgent but controlled` / `reflective` / `building tension`
- `{BPM}` — 90 / 95 / 100 / 105 / 110

### CapCut AI Music (short prompt — the box is small, keep it tight)

```
Instrumental modern corporate-cinematic underscore, {ENERGY}, {BPM} BPM,
soft synth pad and muted plucked synth, light kick, no vocals,
subtle background for voiceover, no melodic hook, loopable
```

CapCut's generator wants 1-2 sentences. Anything longer gets truncated. The short version above is the same DNA as the Suno template, compressed.

---

## Calibrated presets by script type

Match the music to what the script is doing. The prompt changes; the "no vocals / voiceover-friendly" frame stays constant.

### NF — News (the default walk-and-talk)

**Use when:** Settlement news, lawsuit update, regulatory move, market shift, breaking industry headline. The hook is a number or a fact.

**Vibe target:** Bloomberg / WSJ explainer. Sober, modern, slightly tense, authoritative.

**Suno/Udio prompt:**
```
[no vocals] modern news-explainer underscore, instrumental only, urgent but controlled,
95 BPM, pulsing minor-key synth pad, muted plucked synth motif, tight kick,
subtle hi-hat shuffle, light string swell on the back half,
clean low end, unobtrusive background for voiceover,
no melodic hook, no vocal chops, no risers, no whooshes, loopable
```

**CapCut prompt:**
```
Instrumental news-explainer underscore, urgent but controlled, 95 BPM,
pulsing minor synth pad, muted plucks, tight kick, no vocals,
subtle bed for voiceover, loopable
```

### NF — Big number / scoreboard moment

**Use when:** The hook is a dollar figure ($52M, $89M, $418M), a count ("five brokerages in three months"), or a deadline ("July 28").

**Vibe target:** Slightly more momentum than default NF. Confident, ticking, "the clock is moving."

**Suno/Udio prompt:**
```
[no vocals] modern financial-news underscore, instrumental only, confident with forward momentum,
100 BPM, ticking arpeggiated synth, muted Rhodes chord stabs, steady kick,
subtle ride cymbal, light analog bass, minor key with one resolved lift,
clean mix for voiceover, no melodic hook, no vocal chops, no risers, loopable
```

**CapCut prompt:**
```
Instrumental financial-news underscore, confident and ticking, 100 BPM,
arpeggiated synth, Rhodes stabs, steady kick, no vocals,
unobtrusive bed for voiceover, loopable
```

### IS — Synthesis (pattern across 700 interviews)

**Use when:** "I've interviewed 700 agents and here's what the top producers all do." More reflective and authoritative than NF. The viewer is being let in on a pattern.

**Vibe target:** Thoughtful, slightly warmer than NF. Think a documentary mid-segment under a wise narrator.

**Suno/Udio prompt:**
```
[no vocals] reflective documentary underscore, instrumental only, warm and authoritative,
90 BPM, soft felt-piano motif, ambient pad, sparse kick,
gentle upright bass, light string bed, major-leaning but grounded,
unobtrusive background for voiceover, no melodic hook, no drum fills,
no risers, no reverb tails, loopable
```

**CapCut prompt:**
```
Instrumental documentary underscore, warm and reflective, 90 BPM,
felt piano, ambient pad, sparse kick, no vocals,
quiet bed for voiceover, loopable
```

### IA — Access (D.J. was in the room)

**Use when:** "I just spent two days with NAR's executive team." The credential and the access ARE the scroll-stopper. Music should feel insider, slightly elevated.

**Vibe target:** Boardroom-modern. Slightly more polished and slightly more "high-stakes" than NF.

**Suno/Udio prompt:**
```
[no vocals] modern boardroom underscore, instrumental only, confident insider feel,
98 BPM, smooth synth pad, restrained plucked melody, soft kick,
subtle hi-hat, tasteful sub-bass, minor-to-major lift in the back half,
unobtrusive background for voiceover, no melodic hook, no vocal chops,
no whooshes, no risers, loopable
```

**CapCut prompt:**
```
Instrumental modern boardroom underscore, confident insider feel, 98 BPM,
smooth pad, plucked melody, soft kick, no vocals,
quiet bed for voiceover, loopable
```

### The Playbook — Scenario / tactical

**Use when:** D.J. walks through a specific tactical scenario ("the white duvet trick," objection handling, listing presentation moves). Practical, slightly upbeat.

**Vibe target:** Modern productivity / coaching. Light forward energy, no drama.

**Suno/Udio prompt:**
```
[no vocals] modern coaching underscore, instrumental only, light forward energy,
105 BPM, clean plucked synth, soft electric piano, steady tight kick,
subtle shaker, warm sub-bass, neutral major key, optimistic but not cheesy,
unobtrusive background for voiceover, no melodic hook, no vocal chops,
no big drop, no risers, loopable
```

**CapCut prompt:**
```
Instrumental modern coaching underscore, light forward energy, 105 BPM,
plucked synth, electric piano, tight kick, no vocals,
upbeat-but-quiet bed for voiceover, loopable
```

### AI Tip of the Week — Utility / Friday slot

**Use when:** Fri tapthis.co utility post. The CTA is the point. Music should feel modern-tech, slightly more energetic than NF.

**Vibe target:** Modern SaaS demo / product walkthrough. Clean, forward, optimistic.

**Suno/Udio prompt:**
```
[no vocals] modern tech-product underscore, instrumental only, clean and forward,
108 BPM, crisp arpeggiated synth, muted plucked lead, tight kick,
subtle hi-hat pattern, clean sub-bass, optimistic major key,
unobtrusive background for voiceover, no melodic hook, no vocal chops,
no big build, no risers, loopable
```

**CapCut prompt:**
```
Instrumental modern tech-product underscore, clean and forward, 108 BPM,
arpeggiated synth, muted lead, tight kick, no vocals,
optimistic bed for voiceover, loopable
```

### Podcast promo (Mon KIR slot)

**Use when:** "New KIR episode this week with [guest]." Warm, conversational, lifts the guest's credibility.

**Vibe target:** Modern interview-show theme. Warm, inviting, slightly elevated.

**Suno/Udio prompt:**
```
[no vocals] modern interview-show theme, instrumental only, warm and inviting,
95 BPM, soft electric piano, mellow plucked guitar, light brushed kick,
warm upright bass, subtle string pad, major key, conversational and grounded,
unobtrusive background for voiceover, no melodic hook, no vocal chops,
no risers, loopable
```

**CapCut prompt:**
```
Instrumental modern interview-show theme, warm and inviting, 95 BPM,
electric piano, mellow guitar, brushed kick, no vocals,
warm bed for voiceover, loopable
```

---

## How to use a generated track in CapCut

1. **Generate 3-4 takes.** AI music is non-deterministic. The first take is rarely the best.
2. **Listen with your eyes closed.** Same trick as the cuts pass — your ear catches "this would distract from D.J.'s voice" faster than your eye.
3. **Reject anything with a hook line.** If you find yourself humming it, it's competing with the script.
4. **Drop it on the timeline below the voice track.**
5. **Volume: 10-15% max.** Per [`capcut-editing-playbook.md`](capcut-editing-playbook.md) Part 6 mistakes table. If you can hear the music clearly over D.J., it's too loud.
6. **Fade in 0.3s at the start, fade out 0.5s at the end.** Avoids the jarring music-just-started feel.
7. **Trim to script length + 1s.** Music shouldn't outlast the close.
8. **Optional: duck under the hook.** If D.J.'s hook is a hard number ("$52 million"), drop the music to 5% for the hook line, ramp to 12% under CONTEXT.

---

## Quick troubleshooting

| Problem | Fix |
|---|---|
| Track has a melody you keep humming | Add `no melodic hook, no lead synth melody`, regenerate |
| Track feels too "epic trailer" | Add `no orchestral brass, no big build, no drop`, lower BPM by 5 |
| Track has accidental vocals or vocal chops | Move `[no vocals]` to the very start, add `no vocal chops, no choir, no aahs`, put `[Instrumental]` in lyrics field |
| Track sounds dated / 2010s EDM | Add `modern 2025 production, no four-on-the-floor, no big-room synths` |
| Track muddies under D.J.'s voice | Add `clean low end, sparse mid-range, no piano in vocal range` |
| Track has dramatic risers | Add `no risers, no whooshes, no transitions, no FX sweeps` |
| Track ends abruptly / won't loop | Add `seamless loop, no fade in, no fade out, no ending` |

---

## What this looks like in a script

Every walk-and-talk script (NF, IS, IA, Playbook, AI Tip of the Week, podcast promo) should end with an **AI Music Prompt** block beneath the Data Source section:

```markdown
## AI Music Prompt

**Vibe:** [one-line description of the energy this track should carry]

**Suno / Udio:**
> [paste calibrated prompt from the preset above, edited for this specific script]

**CapCut AI Music:**
> [paste short version]
```

Claude should generate both prompts and tune the energy / BPM to the specific script. A sober settlement update is not the same energy as a market-up tip — even though both are NF.

---

## Sources

Research that informed this guide:

- [Suno Instrumental Prompts: 50+ Tested Beats (HookGenius)](https://hookgenius.app/learn/suno-instrumental-prompts/) — voiceover-friendly prompt formula, BPM benchmarks, "no vocals" syntax for Suno v4/v5
- [AI Music Generation Prompts: Best Practices (MusicSmith)](https://musicsmith.ai/blog/ai-music-generation-prompts-best-practices) — describe-don't-command rule, exclusion lists, loopable-track guidance
- [How to Write Effective Prompts for Suno (Soundverse)](https://www.soundverse.ai/blog/article/how-to-write-effective-prompts-for-suno-ai-music-generation) — 4-7 descriptor sweet spot, genre+mood+instruments+vocals component model
- [Ultimate Udio AI Prompt Guide (OpenMusicPrompt)](https://openmusicprompt.com/blog/udio-ai-prompt-guide) — Udio's natural-language + production-keyword approach
- [CapCut AI Music Generator (CapCut docs)](https://www.capcut.com/tools/ai-music-generator) — how the in-app generator parses prompts; talking-head guidance to keep tracks subtle
- [Top AI Music Generators for YouTube Beginners (CapCut)](https://www.capcut.com/resource/top-5-ai-music-generators-for-youtube-beginners) — short-prompt format for the CapCut generator specifically
- [Real Estate Background Music Guide (Soundstripe)](https://www.soundstripe.com/blogs/music-for-real-estate-videos) — genre/mood selection logic for real-estate-creator content
