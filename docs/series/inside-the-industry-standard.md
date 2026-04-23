# Inside the Industry - Series Standard

This document defines the per-series rules for the **Inside the Industry** series. It builds on [`editorial-standards.md`](../editorial-standards.md), which is the universal standard. Everything in the universal standard applies here. This document only adds what is specific to Inside the Industry.

**If this document and the universal standard ever conflict, the universal standard wins.**

---

## What Inside the Industry is

A short-form video series where D.J. delivers observations, analysis, and breaking news from inside the real estate industry. This is the series that leverages D.J.'s unique positioning: 700+ podcast interviews, 1 of 12 in NAR's 2026 influencer program, VP of Business Development at a 300+ agent brokerage. No other content creator has this combination of access, archive, and operational perspective.

**Core promise to the viewer:** *Something is happening in the industry that matters to your business, and D.J. is closer to it than you are.*

If a draft does not deliver an insight the viewer couldn't get from scrolling industry headlines, it is not Inside the Industry.

---

## Three sub-types

Inside the Industry has three distinct sub-types. Each has its own structure and editorial requirements. The sub-type is declared in the frontmatter `type` field.

### Type A: Access (IA-###)

**What it is.** D.J. was in a room, at a table, or on a call that the viewer wasn't. He shares what he saw, what it means, and why it matters. This is the rarest and most valuable sub-type because it cannot be replicated by any other creator.

**Source requirement.** Every IA script must describe a real, specific event D.J. attended or participated in. The event must be named (e.g., "NAR's influencer roundtable," "Kale Realty's quarterly all-hands"). If the event was private, D.J. can describe observations without quoting attendees verbatim - but he must be clear about what he observed vs. what he inferred.

**Structure:**
```
1. HOOK           - "I was just in a room with [specific people/org]."
2. OBSERVATION    - What D.J. saw, heard, or noticed. First-person, specific.
3. INSIGHT        - What it means for the viewer's business.
4. CLOSE          - "Here's what you do now." Action tied to the insight.
```

**The hook for Access scripts** is almost always the credential-plus-access pattern: "I just spent two days with NAR's executive team. Here's what they're not saying publicly." The access IS the scroll-stopper.

### Type B: Synthesis (IS-###)

**What it is.** D.J. identifies a pattern from across 700+ podcast interviews and shares the insight. This is the workhorse of the series - it turns the archive into authority. The pattern must be real, traceable to named guests, and not quantified with fabricated numbers.

**Source requirement.** Every IS script must name at least two specific podcast guests whose interviews contributed to the pattern. "I've noticed across my interviews" is not enough. "Kristee Leonard, Bari Mill, and Karina Chavez all told me the same thing" is.

**Structure:**
```
1. HOOK           - The pattern stated as a surprising observation.
2. MIRROR MOMENT  - The viewer recognizes themselves in the wrong side of the pattern.
3. INSIGHT        - The full pattern, with named guest examples.
4. REFRAME        - Why this matters now.
5. CLOSE          - "Here's what you do now." Action tied to the pattern.
```

**Critical rule for Synthesis scripts: never fabricate the quantification of a pattern.** The IS-002 "6% Club" failure happened here. When D.J. observes that "almost every top producer I've interviewed" does something, that qualitative framing is the correct expression. Do not invent a percentage to make it sound more precise. See universal Rule 1's qualitative fallback table.

### Type C: News/Reactive (NF-###)

**What it is.** D.J. reacts to breaking industry news - a lawsuit settlement, a regulatory change, a major acquisition, a market shift - and explains what it means for agents. This is the most time-sensitive sub-type. NF scripts should be drafted and filmed within days of the news breaking.

**Source requirement.** Every NF script must cite the specific news source: court filing, press release, news article, regulatory document. The Data Source section must include the publication name, date, and URL or case number. NF scripts have the strictest stat-integrity requirements because the claims are about public record.

**Structure:**
```
1. HOOK           - The headline, stated as a number or surprising fact.
2. CONTEXT        - What happened and why it matters. Background for agents who missed it.
3. INSIGHT        - What this means for the viewer's business specifically.
4. CLOSE          - "Here's what you do now." Action or watchpoint.
```

**The hook for News scripts** is almost always the specific-number pattern: "$52 million. That's what NAR just agreed to pay in the Tuccori settlement." The number IS the scroll-stopper. Numbers in NF hooks must be exact and sourced - no rounding, no "roughly," no approximation.

---

## The "Here's what you do now" close for this series

Inside the Industry closes are often more watchpoint-oriented than action-oriented, because the viewer may not be able to act on industry-level news immediately. Both forms are acceptable:

**Action close:** "Here's what you do now. Tomorrow morning, pick up one call you'd normally skip. See what happens."

**Watchpoint close:** "Here's what you do now. Watch this case. If Batton goes to trial, everything we just talked about resets. I'll cover it when it does."

The watchpoint close works for NF scripts where the news is unfolding. It still qualifies under universal Rule 4 because it gives the viewer a specific thing to pay attention to - it's not an engagement ask.

---

## Length target

- **Target: 45-60 seconds** (approximately 100-150 spoken words).
- **Hard cap: 75 seconds** (approximately 185 spoken words).
- Inside the Industry scripts typically need slightly more room than Agent Tip or Playbook because they carry more context (the news event, the 700-interview pattern, the access observation). The extra length is earned when the context is necessary for the insight to land.

---

## Data Source requirements by sub-type

| Sub-type | Minimum sources | Format |
| --- | --- | --- |
| **Access (IA)** | 1 named event D.J. attended, with date and attendees/org | Per universal Rule 1 |
| **Synthesis (IS)** | 2+ named podcast guests with episode dates | Per universal Rule 1 |
| **News (NF)** | 1+ named news source with publication date, URL or case number | Per universal Rule 1 |

---

## Protected voice signatures in this series

Inside the Industry is the primary home for D.J.'s protected voice signature (universal Rule 6):

**"I've never practiced real estate. But I've interviewed 700 people who have."**

This signature is most powerful in IS (synthesis) and IA (access) scripts, where the credential is the differentiator. It should appear no more than once per script, and only when it earns its place - typically in the hook or the reframe.

In NF (news) scripts, the signature is less relevant because the authority comes from the news source, not the interview archive. Use sparingly or not at all.

---

## Script metadata - required front matter

```markdown
---
series: "Inside the Industry"
type: "[access / synthesis / reactive]"
script_number: "[IA/IS/NF]-[###]"
title: "[title]"
avatar: "[which avatar]"
content_pillar: "inside_industry"
primary_platform: "[platform]"
post_date: "[YYYY-MM-DD]"
status: "[ready / needs-verification / draft]"
---

# [Title]

> **WOW: [one sentence -- which of the 8 criteria and why]**

## Shareable Moment
> "[the one line or stat a viewer would screenshot or forward]"

## Full Script (Spoken)
[Sub-type-specific structure: see IA/IS/NF structures above]

## Data Source
[Per universal Rule 1 format, with sub-type-specific requirements]

## Social Copy
### LinkedIn
### Instagram
### TikTok
### YouTube Shorts
### Facebook
### X
```

---

## Anti-patterns

- **Fabricating the quantification of a synthesis pattern.** This is the highest-risk failure mode for IS scripts. "Almost every top producer" is correct. "94% of top producers" is fabricated unless sourced. See the IS-002 "6% Club" failure in the universal standard.
- **Access scripts without real access.** If D.J. wasn't actually in the room, it's not an IA script. Do not reconstruct what "probably happened" at an event D.J. didn't attend.
- **News scripts with stale news.** NF scripts must be timely. If the news is more than two weeks old and the viewer has already seen it in every feed, the script needs a fresh angle or it shouldn't be written.
- **Synthesis scripts with only one guest.** If the pattern comes from a single interview, attribute it to that guest and frame it as "one guest told me" - not as a pattern across the archive. A pattern requires at least two named guests.
- **Brand intros, `[ON-SCREEN]` cues, engagement-ask closes.** All deprecated/banned per universal standard.
- **Composite or reconstructed guest quotes.** If a guest didn't say the exact words in quotes, don't use quotation marks. Paraphrase with attribution instead.
