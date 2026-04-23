# Agent Tip of the Day - Series Standard

This document defines the per-series rules for the **Agent Tip of the Day** series. It builds on [`editorial-standards.md`](../editorial-standards.md), which is the universal standard. Everything in the universal standard applies here. This document only adds what is specific to Agent Tip of the Day.

**If this document and the universal standard ever conflict, the universal standard wins.**

---

## What Agent Tip of the Day is

A short-form video series where D.J. delivers one specific, actionable tip drawn from a real podcast guest interview. Every tip is guest-sourced - meaning it came from a named person on a specific episode, not from a generic observation or a composite. The series positions D.J. as the curator of 700+ conversations, handing over the single most useful thing each guest said.

**Core promise to the viewer:** *In 30 to 45 seconds, you'll leave with one thing a real top producer does that you can try today.*

If a draft does not deliver that promise, it is not Agent Tip of the Day.

---

## Mandatory elements

### 1. A named guest and a real episode

Every Agent Tip script must trace its tip to a specific podcast guest. Not "a top producer told me." Not "I've noticed across interviews." A named person who said a real thing on a real episode.

The Data Source section must include:
- Guest name
- Episode title and date
- The specific thing the guest said or did that became the tip
- Status: confirmed

If the tip cannot be attributed to a specific guest, it belongs in Inside the Industry (synthesis type), not Agent Tip.

### 2. The "Actual Tip" gate - exact words, exact action, or exact frame

This series is the strictest application of the universal Rule 0 "Actual Tip" gate. Every script must deliver one of:

- **The exact words to say** - a script, a sentence, a subject line the viewer can copy
- **The exact action to take** - a specific step with a specific trigger ("when X happens, do Y")
- **The exact frame shift** - a reframe that changes a decision the viewer is about to make

"Build trust" is not a tip. "Keep a white duvet in your trunk and drape it over the master bed before every showing" is a tip. The specificity is the series.

### 3. One share trigger per script

Every script should identify one reason a viewer would share it. Document this in the frontmatter as `share_trigger`. Common triggers for this series:

- **"I do that too"** - the tip validates something the viewer already does
- **"I never thought of that"** - the tip is surprising and immediately usable
- **"My colleague needs this"** - the tip solves a problem the viewer sees others having
- **"This is exactly my problem"** - the tip names a specific pain and solves it

---

## Structure

Agent Tip of the Day scripts move through these beats in this order.

```
1. HOOK - First spoken sentence. Stops scroll. Opens a loop.
2. SETUP - Who is the guest? What's the context? (2-3 sentences max)
3. INSIGHT - The tip itself. Exact words, exact action, or exact frame.
4. REFRAME - Why this matters. Connect to the viewer's business.
5. CLOSE - "Here's what you do now." Specific, immediate action.
```

### Beat length guidance (for a 40-second script)

| Beat | Target seconds | Target words |
| --- | --- | --- |
| Hook | 3-5 | 8-12 |
| Setup | 5-8 | 12-20 |
| Insight (the tip) | 12-18 | 30-45 |
| Reframe | 5-8 | 12-20 |
| Close | 5-8 | 12-20 |
| **Total** | **~40s** | **~80-110 words** |

### Why this order

The hook earns attention. The setup gives just enough context so the viewer knows who said this and why it matters (no more). The insight IS the video - the single specific thing the viewer came for. The reframe elevates. The close hands them something to do right now.

---

## Length target

- **Target: 30-45 seconds** (approximately 65-110 spoken words).
- **Hard cap: 60 seconds** (approximately 130-150 words).
- Agent Tip scripts should be the shortest in the repo. The discipline is compression. If the tip needs more than 45 seconds of explanation, it's either two tips (split it) or it belongs in The Playbook (which has room for scenario + response + why).

---

## The hook for this series

The hook almost always takes one of two forms:

**Form 1: Guest-credential-plus-surprising-detail.**
"A $40 million producer just told me she's terrible at prospecting. She still answers her phone at 7pm."

**Form 2: Cost-of-inaction or missed-opportunity lead.**
"You have 300 listing photos on your phone doing nothing. A top producer turned hers into her entire marketing strategy."

Both forms open a curiosity loop the viewer needs to close. The guest's credential (production volume, specialty, achievement) is the credibility anchor; the surprising detail is the scroll-stopper.

---

## The close for this series

Always the "Here's what you do now" pattern from universal Rule 4. For Agent Tip, the close should be the most compressed, specific version possible:

- "Here's what you do now. Next showing, throw a white duvet in your trunk. Drape it over the bed. Takes thirty seconds."
- "Here's what you do now. Open your photos. Pick three listing shots. Post them with a one-line story about the house. Do it before lunch."

One action. One sentence describing it. Executable in the next hour.

---

## Script metadata - required front matter

```markdown
---
series: "Agent Tip of the Day"
title: "[title]"
guest: "[guest full name]"
avatar: "[which avatar]"
content_pillar: "[pillar]"
score: [1-10]
post_date: "[YYYY-MM-DD]"
day: "[day of week]"
source_file: "[KIR episode reference if available]"
share_trigger: "[one of: 'I do that too' / 'I never thought of that' / 'My colleague needs this' / 'This is exactly my problem']"
status: "[ready / needs-verification / draft]"
---

# [Title]

> **WOW: [one sentence -- which of the 8 clip-worthy criteria this hits and why]**

## Shareable Moment
> "[the one line a viewer would forward to a colleague]"

## Full Script (Spoken)
[5-beat structure: HOOK, SETUP, INSIGHT, REFRAME, CLOSE]

## Data Source
[Every claim with source, who-was-measured, status per universal Rule 1]

## Social Copy
### Instagram
### TikTok
### YouTube Shorts
### Facebook
### LinkedIn
### X
```

---

## Anti-patterns

- **Tips without a named guest.** If no guest is attributed, it's not Agent Tip.
- **Generic advice.** "Follow up more" is not a tip. "Send this exact text to every past client on Friday" is.
- **Two tips in one script.** One tip per video. If you have two, make two videos.
- **Long setup before the tip.** The setup exists to earn credibility for the insight, not to tell the guest's life story. Two to three sentences max.
- **Brand intros.** Deprecated. The tip is the brand.
- **`[ON-SCREEN: ...]` cues.** Do not render via captions.ai. Strip all.
- **Engagement-ask closes.** Banned. Use "Here's what you do now."

---

## Known issue: existing scripts pre-date this standard

The ~59 scripts in [`scripts/agent-tip-of-the-day/`](../../scripts/agent-tip-of-the-day/) were written before this standard existed. Common issues to audit:

- Many use a CTA beat instead of a "Here's what you do now" close
- Some have weak hooks that need compression
- Some may have claims that need Data Source verification
- WOW gate metadata is missing from all
- Some may carry banned AI-speak words or passive voice

These scripts need a compliance pass. See the audit workflow for how to apply this standard to existing scripts.
