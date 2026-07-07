# CapCut AI Music Prompts for Walk-and-Talk Reels

How to generate background music for D.J.'s walk-and-talk reels (Inside the Industry NF/IS/IA, The Playbook, AI Tip of the Week, podcast promos — anything that's 45-75s of D.J. talking to camera).

**D.J. edits only in CapCut.** Every prompt in this doc is written for CapCut's AI Music generator. There is no Suno/Udio prompt anymore. Copy the preset, tune 2-3 variables, paste into CapCut AI Music. Music goes **under** the voice at 10-15% volume max (per [`capcut-editing-playbook.md`](capcut-editing-playbook.md) Part 6) — its only job is to keep the viewer's nervous system engaged, never to compete with what D.J. is saying.

---

## The One Rule

**Music never out-talks D.J.** Every prompt in this doc is calibrated to produce subtle, non-melodic, voice-friendly beds. If a generated track has a hook line you start humming, it's wrong for the reel. Regenerate.

---

## The 300-character hard cap

CapCut's AI Music input truncates silently past **300 characters** (spaces and punctuation included). Every prompt below fits. If you tune one and it grows past 300, cut a descriptor rather than let CapCut work from a partial input. What a good CapCut prompt fits in 300 chars:

1. Style / genre (e.g., "modern documentary editorial score")
2. BPM as a number (e.g., "95 BPM")
3. Mood, 2-4 words (e.g., "authoritative, confident, verdict-in")
4. 3-4 instruments max (e.g., "muted piano, pulsing synth bass, soft percussion")
5. The "no vocals" constraint (always, at the start)
6. Runtime / voiceover hint (e.g., "subtle bed for voiceover, loopable")

---

## What makes a good CapCut prompt (the short version)

1. **Describe, don't command.** "Upbeat lo-fi instrumental, 95 BPM" beats "make me an upbeat song." Front-load the genre and mood.
2. **Put `Instrumental` / `no vocals` at the start.** CapCut sometimes adds vocals if you don't lead with the constraint.
3. **4-7 descriptors is the sweet spot.** Fewer = generic. More = the model gets confused and the 300-char cap bites.
4. **Name 2-3 specific instruments, not categories.** "Warm Rhodes, soft kick, subtle pad" beats "electronic."
5. **Specify intent for voiceover.** `subtle bed for voiceover`, `unobtrusive`, `doesn't compete with speech`, `loopable`, `clean low-end`.
6. **Specify what NOT to include.** `no melodic hook`, `no risers`, `no vocal chops` — exclusions matter as much as inclusions for VO beds. Trim these first if you hit the cap.
7. **BPM matters more than you think.** Walk-and-talks land best in the **90-110 BPM** range. Slower feels funereal under D.J.'s pacing; faster fights his cadence.
8. **Avoid artist names.** Use era + genre instead ("late-90s trip-hop," "modern corporate-cinematic").

---

## D.J.'s house sound (start here every time)

The default vibe for an NF (news-reactive) walk-and-talk. Modern, slightly tense, authoritative — the audio equivalent of "I have inside information and you should listen."

**Genre lane:** Modern corporate-cinematic, light electronic underscore, neutral-but-confident.
**BPM:** 95-105 (90 for sober/legal news, 105-110 for high-energy market wins).
**Key feel:** Minor key, but not dark. Think Bloomberg explainer, not true crime.
**Instrumentation:** Soft pulsing synth pad, muted plucked synth or Rhodes, light kick, subtle hi-hat shuffle, occasional restrained string layer.
**What to avoid:** Lead melodies, vocal chops, big drops, risers, "epic trailer" brass, lo-fi vinyl crackle (too casual for industry news), tropical house anything.

---

## Master template (use this 80% of the time)

```
Instrumental modern corporate-cinematic underscore, {ENERGY}, {BPM} BPM,
soft synth pad and muted plucked synth, light kick, no vocals,
subtle background for voiceover, no melodic hook, loopable
```

**Variables to fill in:**
- `{ENERGY}` — pick one: `subtle energy` / `confident and steady` / `urgent but controlled` / `reflective` / `building tension`
- `{BPM}` — 90 / 95 / 100 / 105 / 110

Keep it to 1-2 sentences. This is the same DNA as every preset below, just neutral.

---

## Calibrated presets by script type

Match the music to what the script is doing. The prompt changes; the "no vocals / voiceover-friendly" frame stays constant. Each fits under 300 chars.

### NF — News (the default walk-and-talk)

**Use when:** Settlement news, lawsuit update, regulatory move, market shift, breaking industry headline. The hook is a number or a fact.

**Vibe target:** Bloomberg / WSJ explainer. Sober, modern, slightly tense, authoritative.

```
Instrumental news-explainer underscore, urgent but controlled, 95 BPM,
pulsing minor synth pad, muted plucks, tight kick, no vocals,
subtle bed for voiceover, loopable
```

### NF — Big number / scoreboard moment

**Use when:** The hook is a dollar figure ($52M, $89M, $418M), a count ("five brokerages in three months"), or a deadline ("July 28").

**Vibe target:** Slightly more momentum than default NF. Confident, ticking, "the clock is moving."

```
Instrumental financial-news underscore, confident and ticking, 100 BPM,
arpeggiated synth, Rhodes stabs, steady kick, no vocals,
unobtrusive bed for voiceover, loopable
```

### IS — Synthesis (pattern across 700 interviews)

**Use when:** "I've interviewed 700 agents and here's what the top producers all do." More reflective and authoritative than NF. The viewer is being let in on a pattern.

**Vibe target:** Thoughtful, slightly warmer than NF. A documentary mid-segment under a wise narrator.

```
Instrumental documentary underscore, warm and reflective, 90 BPM,
felt piano, ambient pad, sparse kick, no vocals,
quiet bed for voiceover, loopable
```

### IA — Access (D.J. was in the room)

**Use when:** "I just spent two days with NAR's executive team." The credential and the access ARE the scroll-stopper. Music should feel insider, slightly elevated.

**Vibe target:** Boardroom-modern. Slightly more polished and "high-stakes" than NF.

```
Instrumental modern boardroom underscore, confident insider feel, 98 BPM,
smooth pad, plucked melody, soft kick, no vocals,
quiet bed for voiceover, loopable
```

### The Playbook — Scenario / tactical

**Use when:** D.J. walks through a specific tactical scenario ("the white duvet trick," objection handling, listing presentation moves). Practical, slightly upbeat.

**Vibe target:** Modern productivity / coaching. Light forward energy, no drama.

```
Instrumental modern coaching underscore, light forward energy, 105 BPM,
plucked synth, electric piano, tight kick, no vocals,
upbeat-but-quiet bed for voiceover, loopable
```

### AI Tip of the Week — Utility / Friday slot

**Use when:** Fri tapthis.co utility post. The CTA is the point. Music should feel modern-tech, slightly more energetic than NF.

**Vibe target:** Modern SaaS demo / product walkthrough. Clean, forward, optimistic.

```
Instrumental modern tech-product underscore, clean and forward, 108 BPM,
arpeggiated synth, muted lead, tight kick, no vocals,
optimistic bed for voiceover, loopable
```

### Podcast promo (Mon KIR slot)

**Use when:** "New KIR episode this week with [guest]." Warm, conversational, lifts the guest's credibility.

**Vibe target:** Modern interview-show theme. Warm, inviting, slightly elevated.

```
Instrumental modern interview-show theme, warm and inviting, 95 BPM,
electric piano, mellow guitar, brushed kick, no vocals,
warm bed for voiceover, loopable
```

---

## How to use a generated track in CapCut

1. **Generate 3-4 takes.** AI music is non-deterministic. The first take is rarely the best.
2. **Listen with your eyes closed.** Your ear catches "this would distract from D.J.'s voice" faster than your eye.
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
| Track feels too "epic trailer" | Add `no orchestral brass, no big build`, lower BPM by 5 |
| Track has accidental vocals or vocal chops | Move `Instrumental / no vocals` to the very start, add `no vocal chops` |
| Track sounds dated / 2010s EDM | Add `modern production, no four-on-the-floor, no big-room synths` |
| Track muddies under D.J.'s voice | Add `clean low end, sparse mid-range` |
| Track has dramatic risers | Add `no risers, no whooshes` |
| Track ends abruptly / won't loop | Add `seamless loop, no fade` |

Note: with the 300-char cap, you often can't stack every fix in one prompt. Add the one that targets the specific problem, drop a less-important descriptor to make room, and regenerate.

---

## What this looks like in a script

Every walk-and-talk script (NF, IS, IA, Playbook, AI Tip of the Week, podcast promo) should end with an **AI Music Prompt** block beneath the Data Source section:

```markdown
## AI Music Prompt

**Vibe:** [one-line description of the energy this track should carry]

**CapCut AI Music:**
> [calibrated CapCut prompt from the preset above, <=300 chars, tuned for this specific script]
```

Claude generates the CapCut prompt and tunes the energy / BPM to the specific script. A sober settlement update is not the same energy as a market-up tip — even though both are NF.

---

## Sources

Research that informed this guide:

- [CapCut AI Music Generator (CapCut docs)](https://www.capcut.com/tools/ai-music-generator) — how the in-app generator parses prompts; talking-head guidance to keep tracks subtle
- [Top AI Music Generators for YouTube Beginners (CapCut)](https://www.capcut.com/resource/top-5-ai-music-generators-for-youtube-beginners) — short-prompt format for the CapCut generator specifically
- [AI Music Generation Prompts: Best Practices (MusicSmith)](https://musicsmith.ai/blog/ai-music-generation-prompts-best-practices) — describe-don't-command rule, exclusion lists, loopable-track guidance
- [Real Estate Background Music Guide (Soundstripe)](https://www.soundstripe.com/blogs/music-for-real-estate-videos) — genre/mood selection logic for real-estate-creator content
