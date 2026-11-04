# CapCut AI Music Prompts v2 (DRAFT, pending test)

> **Status: not live.** The live engine is still [`ai-music-prompts.md`](ai-music-prompts.md). This draft replaces it only after the side-by-side test in [`audits/2026-11-03-capcut-music-v2-test.md`](audits/2026-11-03-capcut-music-v2-test.md) passes. Built from the 2026-11-03 audit of 310 shipped prompts.

Background music for D.J.'s walk-and-talks. D.J. edits only in CapCut, so there is one CapCut prompt per script and no Suno/Udio. Music sits under the voice at 10-15% volume ([`capcut-editing-playbook.md`](capcut-editing-playbook.md) Part 6).

## What changed from v1, and why

| v1 habit | v2 rule | Why |
|---|---|---|
| ~3 "no X" phrases per prompt | Describe what you want. One exclusion max, only to fix a problem you heard | Text-to-music models read words as things to include. "No vocal chops" spends characters naming vocal chops |
| Piano, electric piano, guitar, plucks as the lead sounds | Pick instruments by register: low pad or sub bass plus one high, airy element | Those instruments sit in 1-4 kHz, the band speech needs for clarity. That's why beds "muddy under D.J." |
| `loopable` in 99% of prompts | Describe the arc: full energy, a lift, a clean ending | A 30s track never loops. Asking for a loop asks for the flat, unchanging bed we don't want |
| `starts at full energy` + `no intro build` | `Full energy from the first beat` | Same instruction twice |
| Copy the preset, change nothing | Change mood, lift time, and one instrument per script | 40% of shipped prompts were 80%+ identical to a preset |

## The One Rule

**Music never out-talks D.J.** If you catch yourself humming the track, it's wrong. Regenerate.

## Prompt anatomy (in this order, 300 characters max)

1. `Instrumental only.` Always first.
2. Style + mood (2-4 words) + BPM as a number + the script's real runtime (`30s`; Stupid Things `40s`).
3. Three or four instruments chosen by register (table below).
4. `Sparse midrange, leaves room for a speaking voice.`
5. The arc: `Full energy from the first beat, subtle lift at {L}, clean ending.` Set `{L}` to where THE POINT starts (about 7s when the point is a number) or the halfway mark (15s).

CapCut truncates silently past 300 characters, spaces included. Count every prompt. If it runs over, shorten the style words before touching steps 1, 4 or 5.

## Choosing instruments by register

| Use freely (stays out of the voice) | Use sparingly, low or as single notes | Avoid as the main sound |
|---|---|---|
| low synth pad, sub bass, upright bass, held low strings, kick, brushed kit, shaker, hi-hat, tambourine, high synth shimmer, high harmonics | felt piano ("a few low notes"), Rhodes ("low chords"), arpeggiated synth ("low") | lead synth, electric piano chords, strummed or plucked guitar, plucked synth, strings melody, brass |

## Master template

```
Instrumental only. Minimal modern documentary underscore, confident and steady, 98 BPM, 30s. Warm low synth pad, soft sub bass, light kick, airy shaker. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 15s, clean ending.
```

Swap: mood (`confident and steady` / `urgent but controlled` / `reflective` / `warm and inviting`), BPM (90-110; slower is funereal under D.J., faster fights his pace), lift time.

## Presets by lane

Each fits under 300. Start here, then tune to the script.

**NF news (default).** Bloomberg-explainer tension. Lift at 7s, where the number lands.
```
Instrumental only. Modern news-explainer underscore, urgent but controlled, minor key, 95 BPM, 30s. Pulsing low synth pad, deep sub bass, tight kick, soft ticking hi-hat. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 7s, clean ending.
```

**NF big number / deadline.** The clock is moving.
```
Instrumental only. Financial-news underscore, confident and ticking, 100 BPM, 30s. Low arpeggiated synth, deep sub bass, steady kick, crisp clock-like hi-hat. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 7s, clean ending.
```

**IS synthesis (patterns across 700 interviews).** Warmer, documentary narrator.
```
Instrumental only. Documentary underscore, warm and reflective, 90 BPM, 30s. Soft ambient pad, a few low felt piano notes, sparse kick, airy texture. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 15s, clean ending.
```

**IA access (D.J. was in the room).** Polished, high-stakes.
```
Instrumental only. Modern boardroom underscore, polished insider feel, 98 BPM, 30s. Smooth low pad, deep sub bass, soft kick, shimmering high synth. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 15s, clean ending.
```

**The Playbook / Unlock Insights / What Actually Works (tactical).** Light forward energy. Firmer and less cheerful for hard-conversation scripts.
```
Instrumental only. Modern coaching underscore, light forward energy, 104 BPM, 30s. Warm low synth pad, bouncy sub bass, tight kick, airy shaker. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 15s, clean ending.
```

**Take.** Confident, not a rant. At heat 4, drop to ~96 BPM and go more controlled, never more aggressive.
```
Instrumental only. Modern editorial underscore, confident, unhurried, slightly pointed, 100 BPM, 30s. Low synth pad, round sub bass, tight kick, soft hi-hat. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 15s, clean ending.
```

**AI Tip of the Week.** Clean SaaS-demo optimism.
```
Instrumental only. Modern tech-product underscore, clean and optimistic, 108 BPM, 30s. Low arpeggiated synth, deep sub bass, tight kick, bright high sparkle. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 15s, clean ending.
```

**Podcast promo (KIR / Coffee Talk).** Warm interview-show feel.
```
Instrumental only. Modern interview-show underscore, warm and inviting, 95 BPM, 30s. Soft low synth pad, warm sub bass, brushed kick, airy tambourine. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 15s, clean ending.
```

**Stupid Things (40s lane).** Calm, sensible, level.
```
Instrumental only. Calm walking underscore, sensible and level, 94 BPM, 40s. Warm low pad, muted sub bass, soft kick, brushed hi-hat. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 20s, clean ending.
```

**Broker Problems.** Patient, uneasy, unresolved.
```
Instrumental only. Sparse ambient documentary underscore, patient and uneasy, minor key, 90 BPM, 30s. Held low strings, low sustained bass, soft brushed percussion. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 15s, clean ending.
```

**Chicago Agent Spotlight.** Sincere, major-key tribute.
```
Instrumental only. Warm acoustic underscore, sincere and uplifting, major key, 92 BPM, 30s. Low upright bass, soft brushed kick, gentle high acoustic harmonics. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 15s, clean ending.
```

## Tuning to the script

Before writing the prompt, write the **Vibe** line from the script's key moment, not its series. A sober settlement update and a market-up tip are both NF and need different beds. Then change at least three things from the preset: mood words, lift time, and one instrument. If THE POINT turns on a number, lift at 7s. If it builds to a turn in PAYOFF, lift at 15s.

## In CapCut

1. Audio > AI music > paste the prompt > Generate. Make 3-4 takes; the first is rarely the best.
2. Listen under D.J.'s real voice track at 12%, eyes closed. Reject anything with a hook you'd hum or anything that blurs his consonants.
3. Volume 10-15%. Fade in 0.3s, fade out 0.5s, trim to script length + 1s.
4. Optional: dip to 5% under a hard-number hook, back to 12% after. Use Auto Ducking if your CapCut version has it; otherwise keyframe.

## Troubleshooting (one fix at a time, then regenerate)

| Problem | Try first (positive) | Then, if still wrong (one exclusion) |
|---|---|---|
| Vocals or vocal chops appear | Make sure `Instrumental only.` is first | Add `No vocals.` at the end |
| A melody you keep humming | Add `minimal, textural` to the style words | `no lead melody` |
| Blurs D.J.'s voice | Swap the mid instrument for a pad or high shimmer | `no piano` / `no guitar` |
| Too epic or trailer-like | Lower BPM 5, add `understated` | `no brass` |
| Big swells or whooshes | `steady, even dynamics` | `no risers` |
| Feels flat by second 20 | Move the lift earlier, add `gentle build in the last third` | -- |
| Sounds dated (2010s EDM) | `modern minimal production` | `no four-on-the-floor` |

## Script block format

```markdown
## AI Music Prompt

**Vibe:** [one line, from the script's key moment]

**CapCut AI Music:**
> [prompt, <=300 characters, `Instrumental only.` first]
```

## Sources

- [CapCut AI Music Generator](https://www.capcut.com/tools/ai-music-generator): the single "Describe your music" box, takes, fades, copyright check
- [CapCut audio ducking guide](https://www.capcut.com/create/audio-ducking-for-clear-dialogue-in-video): Auto Ducking on supported versions, keyframes otherwise
- [Stable Audio Open model card](https://huggingface.co/audo/stable-audio-open-1.0/raw/main/README.md) and [MusicGen negative-prompt discussion](https://huggingface.co/spaces/facebook/MusicGen/discussions/30): exclusions belong in a separate negative field, which CapCut doesn't have
- [USPTO 8538749](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8538749): speech intelligibility concentrates in 1-4 kHz, peaking near 2 kHz
