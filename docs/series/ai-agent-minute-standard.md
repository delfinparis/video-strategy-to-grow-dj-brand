# AI Agent Minute - Series Standard

This document defines the per-series rules for the **AI Agent Minute** series. It builds on [`editorial-standards.md`](../editorial-standards.md), which is the universal standard. Everything in the universal standard applies here. This document only adds what is specific to AI Agent Minute.

**If this document and the universal standard ever conflict, the universal standard wins.** This file captures only series-specific structure, beats, and acceptance criteria.

**Source lineage.** This standard is adapted from the [KIR POLISH_PROMPT.md](https://github.com/delfinparis/keeping-it-real-content-system/blob/main/content/ai-tips-scripts/POLISH_PROMPT.md). Four things from KIR are explicitly not adopted in this repo:

1. The fixed brand intro (*"This is D.J. Paris with Keeping It Real Podcast and Kale Realty..."*) - D.J. no longer uses brand intros.
2. The `[ON-SCREEN: ...]` callouts - captions.ai auto-captions audio only; written-in overlays do not render.
3. The "plausible specific" numbers rule - all numbers in this repo must trace to a source (universal Rule 1).
4. The "specific question" CTA - every AI Agent Minute script ends on a "Here's what you do now" close (universal Rule 4).

Em dashes from the original KIR prompt have been stripped wherever adapted; see universal Rule 5.

---

## What AI Agent Minute is

A short-form video series for real estate agents showing how to use a specific AI tool to solve a specific, named business problem, with an exact prompt the viewer can copy and run today. The series positions D.J. as the senior, warm, peer-level mentor who has already figured out what works and is handing it over without the hype.

**Core promise to the viewer:** *In 60 seconds you will leave with one thing you can copy-paste into Claude (or ChatGPT, or whatever) right now and get a real result before your next coffee.*

If a draft does not deliver that promise, it is not AI Agent Minute.

---

## Mandatory elements

Every AI Agent Minute script must include all of these. This is a superset of the universal standard, not a replacement for it.

### 1. A real AI tool, named specifically

Not "AI." Not "an AI assistant." The exact tool: Claude, ChatGPT, Perplexity, Gemini, Cursor, whatever. Name it. Reference the version if it matters (e.g., Claude Opus for long context, ChatGPT o1 for reasoning). If the script does not name a specific tool, it is not AI Agent Minute - it is a mindset piece, and belongs in a different series.

### 2. The exact prompt, shown in quotes in the spoken line

Not "ask Claude to practice objections with you." The actual words D.J. reads aloud:

> *Type this into Claude: "Act as a seller who just said 'I want to think about it' after my listing presentation. Stay in character. Push back the way a real seller would."*

The prompt has to be short enough to remember and specific enough to work on the first try. If it is four paragraphs long, it will not get used. Write prompts the viewer can retype from memory after watching.

The prompt gets delivered **spoken, not on-screen text.** See the universal Rule 2 override on captions.ai.

### 3. A single named business problem

One problem per script. Not "follow-up and objections and lead gen." One. The script titles itself around the problem ("Re-engage ghosted leads with AI"), and the structure spends its entire budget on that one problem and its one fix.

### 4. The "it worked in 60 seconds" demonstration

Somewhere in the spoken line, make it concrete that the viewer can use this right now. Not "try this sometime." *"Open Claude. Paste this prompt. You'll have a usable draft before you finish your coffee."*

### 5. A "why now" beat

One sentence near the reframe that names why this tip matters this month, not in general. The NAR settlement, the current commission environment, a market shift, a tool that just launched. Inherited from universal Rule 3.

---

## Structure

AI Agent Minute scripts must move through these beats in this order. No brand intro. No "See you next time" sign-off. The tip itself is the sign-off.

```
1. HOOK - First spoken sentence. Stops scroll. Opens a loop. No warm-up.
2. MIRROR MOMENT - Name the specific business pain, with time/place, in second person.
3. AGITATION - What the pain is costing. Specific, not abstract.
4. THE AI FIX - Tool named. Exact prompt delivered in spoken quotes.
5. REFRAME - Why this matters. Why now. One credibility signal max.
6. HERE'S WHAT YOU DO NOW - Exact action at the viewer's own life. Executable in the next hour.
```

### Why this order

The hook earns attention in the first 1.5 seconds, before the viewer knows or cares who D.J. is. The mirror moment makes them feel *seen* - they are not being lectured to, they are being described. The agitation makes them need the fix. The fix is the exact prompt they came for - the moment the video has to earn. The reframe elevates the tactic into a shift. The close hands them a specific action they can execute in the next hour, which is what drives saves (they come back to it) and shares (they send it to a colleague with the same problem).

Think of it like a late-night monologue: the joke lands first, the host owns the room, then the content rolls.

### Beat length guidance (for a 60-second script)

| Beat | Target seconds | Target words |
| --- | --- | --- |
| Hook | 3-5 | 8-12 |
| Mirror moment | 8-12 | 20-30 |
| Agitation | 5-8 | 12-20 |
| AI fix (including exact prompt) | 20-30 | 50-75 |
| Reframe + why now | 8-12 | 20-30 |
| Here's what you do now | 5-8 | 12-20 |
| **Total** | **~60s** | **~130-150 words** |

If the draft runs longer, the agitation and reframe are usually the padding. Cut there first. The prompt text itself should rarely be cut - it is the reason the video exists.

---

## The 15-second re-hook

Every AI Agent Minute script is over 20 seconds and therefore requires a 15-second re-hook line (universal Rule 2). The re-hook usually lands at the transition from mirror moment to agitation, or from agitation to fix.

Re-hooks that work for this series:

- *"And here is the part almost every agent misses."*
- *"But the thing nobody tells you is what happens next."*
- *"This is the step every agent skips, and it is the one that changes the outcome."*
- *"Stay with me for ten more seconds - this is the part you're going to screenshot."*

Note: "screenshot" is directive but not an engagement ask - it tells the viewer what to do for themselves, not for the channel. Compare to "save this," which is banned.

---

## Scoring rubric

Every AI Agent Minute draft gets scored on these seven dimensions, 1-10, before it is committed. This is adapted from the KIR POLISH_PROMPT scoring rubric with two adjustments: the "Specificity" dimension explicitly disqualifies invented plausible specifics, and the "Voice Match" dimension explicitly checks the banned AI-speak list.

| Dimension | Question | 10/10 looks like |
| --- | --- | --- |
| **Hook + Loop** | Does the first spoken sentence stop the scroll AND open a loop that must be closed? | Passes the 3-second test. Contains a specific promise the rest of the script delivers. |
| **Mirror Moment** | Does the problem beat create an "that's exactly me" recognition? | Uses time, place, and second person. Viewer has lived the exact scene. |
| **Specificity** | Is the AI tool named? Is the exact prompt shown in quotes? Is the fix immediately actionable? No invented plausible specifics? | Tool named. Prompt quoted in spoken line. No fake numbers. Viewer could run the prompt from memory. |
| **Emotional Arc** | Does the script move the viewer from curious → seen → uncomfortable → hopeful → motivated → committed? | Every beat shifts emotion. No flat patches. |
| **Contrast Structure** | Is there a "most agents vs. top producers" moment that creates in-group desire? | At least one contrast line in the hook, problem, or reframe. |
| **Shareability** | Is there one moment so good the viewer thinks "someone I know needs this"? | One explicit shareable moment flagged in metadata, in the first 30 seconds. |
| **Voice Match** | Does it sound like D.J. - warm, direct, peer-level - with zero AI-speak from the banned list? | Reads aloud smoothly. Contractions. No passive voice. No banned words. No em dashes. |

**Score threshold for filming:** a script must score 7/10 or higher on every dimension AND pass every item on the universal pre-commit checklist. A 6 on any dimension means rewrite, not film.

---

## Script metadata - required front matter

Every AI Agent Minute script must carry this front matter and these in-doc sections:

```markdown
---
series: "AI Agent Minute"
title: "[title]"
category: "[category]"
avatar: "[which avatar this is for]"
ai_tool: "[exact tool name]"
score: [overall 1-10 after self-scoring]
tier: [1, 2, 3 -- priority for filming order]
post_date: "[YYYY-MM-DD]"
---

# [Title]

> **WOW: [one sentence -- which of the 8 clip-worthy criteria this hits and why]**

## Shareable Moment
> "[the one line a viewer would screenshot or forward to a colleague]"

## Why This Rank
[One sentence on why this is tier 1, 2, or 3.]

## Full Script (Spoken)
[The spoken script, following the 6-beat structure above.]

## Data Source
[Every stat, claim, and guest attribution, with source name + year + who was measured + status. See universal Rule 1.]

## Scores (Self-Assessed)
- Hook + Loop: X/10
- Mirror Moment: X/10
- Specificity: X/10
- Emotional Arc: X/10
- Contrast Structure: X/10
- Shareability: X/10
- Voice Match: X/10
- **Overall:** X/10

## Producer Note
[One line. Filming priority, accuracy check, or overlap warning.]

## Social Copy
### Instagram
### TikTok
### YouTube Shorts
### Facebook
### LinkedIn
```

The `> **WOW: ...**` line is the first thing a reviewer reads. If it is vague, the script is vague. See universal Rule 0.

---

## Length target for AI Agent Minute

- **Target: 45-60 seconds** (approximately 100-150 spoken words).
- **Hard cap: 75 seconds** (approximately 185 spoken words). KIR's original 150-200 word range is tightened here because the reels scorecard found anything 70+ seconds tanks retention on a single static shot.
- If a draft runs past 75 seconds, cut the agitation and the reframe first. The prompt itself is almost never the thing to cut.
- If the prompt *is* the thing making the script long, the prompt is too complicated and should be rewritten.

---

## Anti-patterns (things this series must never do)

- **Generic AI advice.** "Use AI for lead follow-up" is not AI Agent Minute. "Open Claude right now and paste this exact prompt" is AI Agent Minute.
- **Brand intro.** Deprecated. The tip is the brand.
- **"See you next time" sign-off.** Deprecated. The "here's what you do now" close is the sign-off.
- **`[ON-SCREEN: ...]` cues.** Do not render via captions.ai. Strip all of them.
- **Prompts that are paragraphs long.** If the viewer can't retype it from memory, it won't get used.
- **Fabricated tool behavior.** Do not describe a Claude or ChatGPT output you did not actually run. If the script says "Claude will give you a three-paragraph email," run the prompt first and make sure Claude actually does that.
- **Generic CTA.** "Let me know what you think" is banned. Universal Rule 4.

---

## Known issue: existing scripts pre-date this standard

The scripts currently in [`scripts/ai-agent-minute/`](../../scripts/ai-agent-minute/) were polished against the KIR POLISH_PROMPT v2.0 before this standard existed. They contain the four things this standard overrides: brand intros, `[ON-SCREEN: ...]` cues, "See you next time" closes, and "specific question" CTAs. They also contain em dashes.

Those scripts need a one-pass audit to bring them into compliance. The audit workflow is documented in [`script-audit-workflow.md`](script-audit-workflow.md) *(coming next)*. Do not film any existing AI Agent Minute script until it has been audited against this standard.
