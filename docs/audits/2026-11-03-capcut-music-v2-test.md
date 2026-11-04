# CapCut Music v2: Side-by-Side Test (2026-11-03)

Tested v2 against the old engine on three real scripts. **Result: v2 adopted 2026-11-03** and now lives in [`../ai-music-prompts.md`](../ai-music-prompts.md). Totals: A 38/45, B 40/45, C 37/45 (NF-112 C1 row reads 0s with a 5 total; the 0s are counted).

## What we're testing

- **A: current.** The prompt already in the script (v1 style: several "no X" phrases, piano/guitar leads, `loopable`).
- **B: v2.** Positive wording only, instruments chosen to stay out of the voice, a described arc instead of a loop.
- **C: v2 + one exclusion.** B with `No vocals.` added at the end. This tells us whether CapCut needs the one negation.

## How to run it (about 30 minutes)

1. Open each script's project in CapCut with D.J.'s voice track on the timeline.
2. For each arm, paste the prompt into Audio > AI music and generate **3 takes**. Use the first 3; don't cherry-pick past them.
3. Play each take under the voice at **12%**, eyes closed, start to finish.
4. Score each track in the small table right under the prompt you used. A1 is the 1st track from prompt A, A2 the 2nd, and so on. Each check is 0 (fail) or 1 (pass).

| Check | Pass means |
|---|---|
| Clean | No vocals, hums, or vocal chops |
| No hook | Nothing you'd hum afterward |
| Voice clear | Every consonant of D.J.'s line is easy to hear |
| Holds | Doesn't go flat or repetitive before the end |
| Fits | The ending and length fit the video without hard trimming |

## NF-112: Add the HOA to every payment quote

[`inside-the-industry/NF-112-add-the-hoa-to-every-payment-quote.md`](../../scripts/inside-the-industry/NF-112-add-the-hoa-to-every-payment-quote.md) · 30s. THE POINT (three Realtor.com numbers) starts at 0:06.5.

**A (current)** (251 chars)
```
Instrumental warm explainer underscore, steady and matter-of-fact, 96 BPM, soft piano, muted synth pad, light kick, no vocals, no melodic hook, no vocal chops, no risers, no whooshes, starts at full energy, unobtrusive bed for voiceover, loopable, 30s
```

Score the 3 tracks CapCut makes from prompt A:

| Track | Clean | No hook | Voice clear | Holds | Fits | Total /5 |
|---|---|---|---|---|---|---|
| A1 (1st track) |  1| 1 |  1| 1 | 1 |  5|
| A2 (2nd track) | 1 |  1| 1 |  1| 1 | 5 |
| A3 (3rd track) |1  |  1| 1 |1  | 1 | 5 |

**B (v2)** (271 chars)
```
Instrumental only. Warm minimal explainer underscore, steady and matter-of-fact, 96 BPM, 30s. Low felt synth pad, round sub bass, soft kick, light shaker. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 7s, clean ending.
```

Score the 3 tracks CapCut makes from prompt B:

| Track | Clean | No hook | Voice clear | Holds | Fits | Total /5 |
|---|---|---|---|---|---|---|
| B1 (1st track) | 1 | 1 |  1|  1|  1|  5|
| B2 (2nd track) | 1 |  1|  1| 1 | 1 |  5|
| B3 (3rd track) | 1 | 1 | 1 | 1 |1  |5  |

**C (v2 + No vocals)** (282 chars)
```
Instrumental only. Warm minimal explainer underscore, steady and matter-of-fact, 96 BPM, 30s. Low felt synth pad, round sub bass, soft kick, light shaker. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 7s, clean ending. No vocals.
```

Score the 3 tracks CapCut makes from prompt C:

| Track | Clean | No hook | Voice clear | Holds | Fits | Total /5 |
|---|---|---|---|---|---|---|
| C1 (1st track) |  0| 0 | 0 |0  | 0 | 5 |
| C2 (2nd track) | 1 |  1| 1|  1| 1 | 5 |
| C3 (3rd track) | 1 |  1| 1 |  1|  1| 5 |

## KIR promo: Mischa Fisher (Zillow Chief Economist)

[`podcast-promos/kir-mischa-fisher-2026-10-30.md`](../../scripts/podcast-promos/kir-mischa-fisher-2026-10-30.md) · 30s. Hook is a stat (payment doubled); THE POINT is a how-to.

**A (current)** (185 chars)
```
Instrumental modern interview-show theme, authoritative and warm, 95 BPM, electric piano, mellow guitar, brushed kick, no vocals, warm bed for voiceover, starts at full energy, loopable
```

Score the 3 tracks CapCut makes from prompt A:

| Track | Clean | No hook | Voice clear | Holds | Fits | Total /5 |
|---|---|---|---|---|---|---|
| A1 (1st track) | 1 |1  | 1 |1  | 1 | 5 |
| A2 (2nd track) | 1 | 1 |  1| 1 | 1 |  5|
| A3 (3rd track) | 1 | 1 | 1 | 1 | 1 | 5 |

**B (v2)** (273 chars)
```
Instrumental only. Modern interview-show underscore, warm and authoritative, 95 BPM, 30s. Soft low synth pad, warm sub bass, brushed kick, airy tambourine. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 15s, clean ending.
```

Score the 3 tracks CapCut makes from prompt B:

| Track | Clean | No hook | Voice clear | Holds | Fits | Total /5 |
|---|---|---|---|---|---|---|
| B1 (1st track) |  1| 1 |1  |1  |1  |5  |
| B2 (2nd track) | 1 | 1 | 1 | 1 | 1 | 5 |
| B3 (3rd track) | 1 | 1 | 1 | 1 |  1|  5|

**C (v2 + No vocals)** (284 chars)
```
Instrumental only. Modern interview-show underscore, warm and authoritative, 95 BPM, 30s. Soft low synth pad, warm sub bass, brushed kick, airy tambourine. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 15s, clean ending. No vocals.
```

Score the 3 tracks CapCut makes from prompt C:

| Track | Clean | No hook | Voice clear | Holds | Fits | Total /5 |
|---|---|---|---|---|---|---|
| C1 (1st track) | 1 | 1 | 1 |1  |1  |5  |
| C2 (2nd track) | 0 |1  | 1 |0  |0  |2  |
| C3 (3rd track) | 1 | 1 | 1 | 1 | 1 | 5 |

## PB-008: The Day 30 price reduction call

[`the-playbook/PB-008-day-30-price-reduction-call.md`](../../scripts/the-playbook/PB-008-day-30-price-reduction-call.md) · ~52s (122 words, see note). Re-hook "Say this instead" lands near 0:15.

**A (current)** (190 chars)
```
Instrumental modern coaching underscore, confident and steady, 100 BPM, plucked synth, electric piano, tight kick, no vocals, no melodic hook, unobtrusive bed for voiceover, loopable, 50-55s
```

Score the 3 tracks CapCut makes from prompt A:

| Track | Clean | No hook | Voice clear | Holds | Fits | Total /5 |
|---|---|---|---|---|---|---|
| A1 (1st track) | 1 | 0 | 0 | 0 | 1 |2  |
| A2 (2nd track) | 1 | 1 | 0 |1  |1  |4  |
| A3 (3rd track) | 0 |  1| 1 | 0 | 0 | 2 |

**B (v2)** (282 chars)
```
Instrumental only. Modern coaching underscore, confident and steady, serious not cheerful, 100 BPM, 50s. Warm low synth pad, soft sub bass, tight kick, airy hi-hat. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 15s, clean ending.
```

Score the 3 tracks CapCut makes from prompt B:

| Track | Clean | No hook | Voice clear | Holds | Fits | Total /5 |
|---|---|---|---|---|---|---|
| B1 (1st track) | 1 |1  |  1| 1 | 1 | 5 |
| B2 (2nd track) | 0 | 0|  0|  0| 0 | 0|
| B3 (3rd track) | 1 | 1 |1  |1  | 1 |  5|

**C (v2 + No vocals)** (293 chars)
```
Instrumental only. Modern coaching underscore, confident and steady, serious not cheerful, 100 BPM, 50s. Warm low synth pad, soft sub bass, tight kick, airy hi-hat. Sparse midrange, leaves room for a speaking voice. Full energy from the first beat, subtle lift at 15s, clean ending. No vocals.
```

Score the 3 tracks CapCut makes from prompt C:

| Track | Clean | No hook | Voice clear | Holds | Fits | Total /5 |
|---|---|---|---|---|---|---|
| C1 (1st track) | 1 | 1 | 1 | 1 | 1 | 5 |
| C2 (2nd track) | 1 | 1 | 1 | 1 | 1 |  5|
| C3 (3rd track) | 1 | 1 | 1 | 1 |  1| 5 |

## Reading the results

- **B or C beats A by 2+ points per script on average** → adopt v2.
- **C beats B on Clean** (B let vocals in on 2+ of 9 takes) → v2 keeps `No vocals.` at the end as standard.
- **B and C tie on Clean** → keep B. Positive wording is enough and the characters go to the arc.
- **A wins on Voice clear** → the register rule isn't the problem; tell Claude which takes blurred his voice.
- **Holds fails across arms** → move the lift earlier and add `gentle build in the last third` before rolling out.

## Note on PB-008

PB-008 is 122 words (~52s), which breaks editorial-standards Rule 7 (30s max). The Playbook series doc still cites a 50-second cap, so the two docs conflict. The test prompt uses `50s` to match the script as written; this doesn't settle which rule is right.

## After the test

Paste the filled tables back to Claude. If v2 passes, the rollout updates: `ai-music-prompts.md` (replaced by v2), `CLAUDE.md` (the AI Music Prompt and 300-char sections), `scripts/apps-script/walk-and-talk-project.gs` (drafter instructions), `scripts/draft_nf.py` (instructions, plus raising its 9,000-char doc load cap, since v2 is ~9,900 chars), the series standards that hard-code `[no vocals]` first, the short-form-council skill, and the ad/webinar scripts in `sales-workflow` and `ai-webinar`.
