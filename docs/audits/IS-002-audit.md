# Audit: IS-002 "The 6% Club"

**Script under audit:** [`scripts/inside-the-industry/IS-002-the-6-percent-club.md`](../../scripts/inside-the-industry/IS-002-the-6-percent-club.md)
**Audit date:** 2026-04-15
**Standard applied:** [`docs/editorial-standards.md`](../editorial-standards.md) (universal)
**Verdict:** **REWRITE APPLIED** (2026-04-16). Original had multiple stat-integrity violations. Rewrite strips fabricated 6%/94%, adds mirror moment + agitation + re-hook, attributes guest quote to Karina Chavez with verified episode citation. Source file overwritten.

This script is also the pilot audit used to validate the new editorial standard. If the standard catches what's wrong here, it catches what's wrong everywhere.

---

## Findings

Grouped by severity. Each finding cites the rule it violates.

### CRITICAL - stat fabrications (Rule 1)

**C1. "Top 6%" and "94%" are fabricated numbers.** This is the exact failure documented in the editorial standard's "Known past failures" section. The 700-interview pattern that top producers still answer their own phone is real. The specific 6%/94% split is invented to match the "X% Club" template from the real 9% Club LinkedIn post. D.J. has directly flagged this as the IS-002 v1 fabrication.

**Appears in:**

- Title: *"The 6% Club: Why 94% of Top Producers I've Interviewed Still Answer Their Own Phone"*
- LinkedIn caption: *"But the top 6% that I have interviewed do not do it."* / *"Especially when the top 6% still do."*
- Instagram Reels caption: *"The top 6%?"* / *"The 6% Club isn't joining. They're picking up."*
- TikTok caption: *"94% outsource their phones. The top 6% do something completely different."*
- YouTube Shorts title: *"The 6% Club -- What 94% of Real Estate Agents Have Outsourced..."*
- YouTube description: *"This is the pattern 94% of the industry has outsourced and the top 6% refuses to."*
- X caption: *"94% of the industry has outsourced it."*

Every single one of these must be stripped or reframed qualitatively. See Rule 1's qualitative fallback table.

**C2. "$100 million dollars a year" in the hook is unsupported.** The Data Source section lists Kristee Leonard ($50M), Bari Mill ($40M), and Karina Chavez (no production volume given). There is no named $100M producer in Data Source, which means the "$100 million" in the hook is likely padding for rhetorical range. Either name a real $100M+ guest in Data Source, or strip the $100M from the hook.

**C3. "One of my guests put it this way: 'I don't know what deal is in that call until I pick it up.'"** This quote is not attributed to a specific named guest in the Data Source section. Either it's a real line from a real guest D.J. can point to on a specific episode - in which case it must be attributed by name - or it's a composite/reconstructed quote, which is a fabrication under Rule 1. **Cannot be shipped until D.J. verifies the source.** Tag for verification before filming.

### CRITICAL - Data Source section is non-compliant (Rule 1)

**C4. Data Source section does not use the required format.** Current entries list guest names and internal script references. The universal standard requires each claim to include source name, publication year (or episode number and date), who was measured, and status (confirmed / unverified / placeholder). Rewrite in the required format.

### HIGH - structural beats missing (Rule 3)

**H1. No mirror moment.** The DATA beat reads as a data dump, not as a mirror moment. A mirror moment puts the viewer in a specific time and place with second person. This script never does. Viewers who have outsourced their phone should feel seen and slightly embarrassed by the mirror; instead they feel lectured to.

**H2. No agitation beat.** The script never names what it costs to outsource the phone. A real cost (a deal that never showed up, a repeat client who went somewhere else, a referral that didn't get recognized) is needed between the mirror moment and the fix.

**H3. No 15-second re-hook.** The script runs ~58 seconds, well past the 20-second threshold. The universal standard requires a re-hook at roughly 15s to catch the drift point. Missing.

**H4. No WOW gate line in metadata.** The script has a "Strongest Line" blockquote but not the `> **WOW: ...**` gate required by Rule 0. Must be added.

**H5. No Shareable Moment metadata.** Rule 0 requires every script to explicitly flag its shareable moment in metadata. The strongest candidate is the guest quote - but that quote can't be used until C3 is resolved.

### MEDIUM - voice and formatting

**M1. Hook contains three numbers in one spoken line.** *"agents doing 25, 50, even 100 million dollars a year"* is 3 numbers. Rule 5 caps at 2 per spoken line. Split or cut.

**M2. Hook is marginally slow.** The first spoken sentence is 30+ words before the payload lands ("still do one thing every other agent has outsourced"). Passes the 3-second test barely. Could be tightened for more punch.

### LOW - what's working

**L1. The close is excellent.** *"Tomorrow morning, pick up one call you'd normally skip. See what happens."* This is already a textbook "here's what you do now" close - it's literally cited in the editorial standard as the example. Keep as-is.

**L2. The contrast structure is present.** "Top producers do X. Every other agent does Y." Works. Keep the structure; fix the numbers behind it.

**L3. The core observation is real.** Multiple named top producers (Kristee Leonard, Bari Mill, Karina Chavez) from the Data Source support the underlying pattern. The script's problem is not the observation - it's the fabricated quantification wrapped around the observation.

---

## Proposed rewrite

This rewrite strips every instance of the fabricated "6%/94%" split, reframes qualitatively, adds a mirror moment and agitation, adds the 15-second re-hook, keeps the strong close, and rewrites the Data Source section in the required format. The guest quote is kept *but tagged for verification before filming* - if D.J. can attribute it to a specific episode, it stays; if not, it gets replaced.

```markdown
---
series: "Inside the Industry"
type: "synthesis"
script_number: "IS-002"
title: "What Every Top Producer I've Interviewed Still Does Themselves"
avatar: "The Stuck Intermediate, The Aspiring Top Producer"
content_pillar: "inside_industry"
primary_platform: "LinkedIn"
post_date: "2026-05-13"
status: "needs-verification"
template: "700-interviews synthesis"
---

# What Every Top Producer I've Interviewed Still Does Themselves

**Pillar:** Inside the Industry | **Type:** Synthesis | **Template:** 700-interviews synthesis
**Primary Platform:** LinkedIn | **Post Date:** Wednesday, May 13, 2026

> **WOW: Pattern reveal from 700 interviews -- the one thing every top producer refuses to delegate, even though the rest of the industry has. It's the opposite of what scaling advice tells agents to do.**

## Shareable Moment
> "[GUEST NAME TBD]: 'I don't know what deal is in that call until I pick it up.'" *(Tagged for verification -- see Data Source.)*

## Full Script (Spoken)

### HOOK (0:00-0:06)
After 700 podcast interviews with top producers, I've noticed one thing almost every one of them still does themselves. And the rest of the industry has outsourced it.

### MIRROR MOMENT (0:06-0:16)
You know the drill. Your phone rings at 6:47 on a Tuesday. Unknown number. You're mid-email, you glance at it, you let it go. You'll call back in the morning. You've trained yourself not to interrupt your day for every ring.

### AGITATION + RE-HOOK (0:16-0:26)
Here's the part almost every agent misses. That 6:47 call was someone about to sign with the agent who picks up. By the time you call back in the morning, there's nothing to call back about.

### INSIGHT (0:26-0:44)
Here's the pattern. When I ask top producers -- agents doing $40, $50 million a year -- what they still do themselves that they probably shouldn't, the answer is almost always the same. They still answer their own phone.

Not a call center. Not an assistant. Not voicemail. They pick up.

It's not that they don't know they could delegate it. Every one of them knows. It's that they think the call is where the relationship lives, and the relationship is the entire business. [GUEST NAME TBD] put it to me this way: "I don't know what deal is in that call until I pick it up."

### REFRAME (0:44-0:54)
So the question isn't whether you can afford to answer your own phone. It's whether you can afford not to. Especially when almost every top producer I've interviewed still does.

### CLOSE (0:54-0:60)
Tomorrow morning, pick up one call you'd normally skip. See what happens.

**Estimated Duration:** ~60 seconds | **Word Count:** ~155 words

## Data Source

- **Claim:** "After 700 podcast interviews with top producers..."
 - Source: Keeping It Real Podcast, 2015-2026, 700+ episodes
 - Who was measured: Real estate agents interviewed by D.J. Paris
 - Status: confirmed

- **Claim:** "agents doing $40, $50 million a year"
 - Source: Kristee Leonard ($50M producer, KIR episode referenced in archive - verify episode number and date)
 - Source: Bari Mill ($40M producer, KIR episode referenced in archive - verify episode number and date)
 - Who was measured: Named podcast guests
 - Status: confirmed on production volume, verify episode citations before filming

- **Claim:** "That 6:47 call was someone about to sign with the agent who picks up."
 - Source: Karina Chavez (KIR episode on evening call responsiveness - verify episode number)
 - Who was measured: Named podcast guest describing her own business
 - Status: Pattern is confirmed from multiple guests; the 6:47pm specific framing is composite. If we want to keep a specific time in the script, attribute to Karina's actual episode. Otherwise reframe to "an evening call."

- **Claim (guest quote):** "I don't know what deal is in that call until I pick it up."
 - Source: **NEEDS VERIFICATION.** D.J. to identify the specific podcast guest and episode before filming. If the quote is composite or reconstructed, it must be replaced with either (a) a verbatim quote from a specific named guest, or (b) a paraphrased version clearly framed as "the way top producers describe it to me" without quotation marks.
 - Status: **placeholder**

- **Claim:** "almost every top producer I've interviewed still does"
 - Source: Synthesis from named guests above plus broader pattern across KIR archive
 - Who was measured: D.J.'s observation across ~700 guest interviews
 - Status: confirmed as a qualitative pattern; deliberately not quantified per Rule 1

- **Template note:** This script replaces the original "X% Club" template. The real "9% Club" LinkedIn post (4/1/2026, 651 impressions on Personal LI) used a verifiable 9% number from a specific source. The "6% Club" in the original IS-002 draft fabricated the 6/94 split to mimic the template structure. That is the exact failure mode the editorial standard was written to prevent.

## Scores (Self-Assessed Against Universal Standard)

- WOW Gate: passes (pattern reveal)
- Hook + Loop: 8/10 (credential-plus-contradiction, opens loop)
- Mirror Moment: 8/10 (added; specific time, second person)
- Specificity: 7/10 (guest quote blocks a 9 until verified)
- Emotional Arc: 8/10 (curious → seen → uncomfortable → motivated → committed)
- Contrast Structure: 9/10 (strong "top producers vs. everyone else")
- Shareability: 7/10 (guest quote is the strongest line, gated by C3)
- Voice Match: 9/10 (clean, conversational, no banned words)

## Producer Note
**DO NOT FILM UNTIL C3 IS RESOLVED.** The guest quote attribution is blocking. D.J. needs to point to a specific episode or replace the quote with either a named, attributed line or a paraphrased observation. Once that's done, this is a strong tier-1 script.

## Social Media

### LinkedIn (PRIMARY)
**Caption:**
I've interviewed over 700 real estate agents on the Keeping It Real Podcast.

Here's something I've noticed that surprises me every time.

When I ask top producers, agents doing forty, fifty million a year in volume, what they still do themselves that they probably shouldn't, the answer is almost always the same.

They still answer their own phone.

Not a call center. Not an assistant. Not voicemail. They pick up.

Agents at every other production level have outsourced it. They forward. They screen. They let it go to voicemail and return calls in batches. All of that is reasonable.

Almost every top producer I've talked to does not do it.

It's not a lack of awareness. Every one of them knows they could delegate it. It's not a time problem either. They're busier than anyone.

It's a belief that answering the phone is beneath a certain level of success. Top producers don't agree. They think the call is where the relationship lives, and the relationship is the entire business.

One of my guests put it to me this way. "I don't know what deal is in that call until I pick it up." *(Quote pending verification -- see Data Source.)*

So the real question isn't whether you can afford to answer your own phone. It's whether you can afford not to.

That's one pattern from 700 interviews. There's a whole catalog.

**Hashtags:** #RealEstate #Leadership #TopProducers #RealtorLife #ChicagoRealEstate #KeepingItRealPodcast #Relationships

### Instagram Reels
**Caption:**
I've interviewed 700 real estate agents. When I ask top producers what they still do themselves that they probably shouldn't, the answer is almost always the same.

They answer their own phone.

Not a call center. Not an assistant. They pick up. Almost every top producer I've talked to still does, even though the rest of the industry has outsourced it.

They think the call is where the relationship lives.

*"I don't know what deal is in that call until I pick it up."* [Quote pending verification.]

Tomorrow morning, pick up one call you'd normally skip.

**Hashtags:**
#realestate #realtor #realtorlife #topproducers #chicagorealestate #realestate2026 #realestateagent #keepingitrealpodcast #insidetheindustry #chicagorealtor #kalerealty

### TikTok
**Caption:**
700 interviews with top real estate agents. Here's the one thing almost every one of them still does themselves.

**Text overlay for hook frame:** *Not used -- captions.ai handles on-screen text from the spoken audio. Hook lives in the first spoken line.*

**Hashtags:**
#realtortok #realestatetok #realtor #topproducers #realtorlife #realestatenews #insidetheindustry

### YouTube Shorts
**Title:** The One Thing Every Top Producer I've Interviewed Still Does Themselves

**Description:**
D.J. Paris has interviewed 700+ real estate agents on the Keeping It Real Podcast. When he asks top producers what they still do themselves that they probably shouldn't, the answer is almost always the same. This is the one thing the rest of the industry has outsourced, and top producers refuse to.

More from inside the industry on the Keeping It Real Podcast.

**Hashtags:** #shorts #realestate #realtor #topproducers #realestatelife #keepingitrealpodcast

### Facebook
**Caption:**
I've interviewed over 700 real estate agents on the Keeping It Real Podcast.

Here's something I've noticed that surprises me every time.

When I ask top producers what they still do themselves that they probably shouldn't, the answer is almost always the same.

They still answer their own phone.

Not a call center. Not an assistant. Not voicemail. They pick up.

Agents at every other production level have outsourced it. Almost every top producer I've interviewed has not.

It isn't a lack of awareness. They know they could delegate. It isn't a time problem either. They're busier than anyone.

It's a belief that answering the phone is beneath a certain level of success. Top producers don't agree. They think the call is where the relationship lives, and the relationship is the entire business.

One of my guests put it this way. "I don't know what deal is in that call until I pick it up." *(Quote pending verification.)*

The real question isn't whether you can afford to answer your own phone. It's whether you can afford not to.

**Hashtags:** #RealEstate #Relationships #TopProducers #ChicagoRealEstate

### X (Twitter)
**Caption:**
700 podcast interviews later, here's a pattern that surprises me every time:

Top producers still answer their own phone.

The rest of the industry has outsourced it.

*"I don't know what deal is in that call until I pick it up."* [Quote pending verification.]

Tomorrow morning, pick up one call you'd normally skip.

**Hashtags:** #RealEstate #TopProducers
```

---

## Changes summary (what the rewrite did)

| Change | Count | Rule |
| --- | --- | --- |
| Stripped "6%" / "94%" fabrications | 8 instances across all captions | Rule 1 |
| Stripped "$100 million" (unsupported) | 1 | Rule 1 |
| Added `> **WOW:**` gate metadata | +1 line | Rule 0 |
| Added `## Shareable Moment` metadata | +1 section | Rule 0 |
| Added mirror moment beat (6:47 Tuesday call) | +1 beat | Rule 3 |
| Added agitation beat (cost of missing the call) | +1 beat | Rule 3 |
| Added 15-second re-hook ("Here's the part almost every agent misses") | +1 line | Rule 2 |
| Tagged guest quote for verification | metadata + `placeholder` status | Rule 1 |
| Rewrote Data Source section in compliant format | full section | Rule 1 |
| Reduced hook to 2 numbers maximum ($40M, $50M) | Hook | Rule 5 |
| Added self-scoring section | +1 section | AIAM standard (applies here too) |
| Kept the "Tomorrow morning, pick up one call you'd normally skip" close | unchanged | Rule 4 (already compliant) |
| Kept "That's one pattern from 700 interviews. There's a whole catalog" as LinkedIn close | unchanged | Rule 4 (observation-implies-catalog pattern) |

---

## Resolution (2026-04-16)

All four open items resolved:

1. **Guest quote attribution.** The original quote *"I don't know what deal is in that call until I pick it up"* could not be found verbatim in the KIR transcript archive. It was likely reconstructed by Claude. Replaced with Karina Chavez's real words from KIR episode "90 Referrals Each Year & Converting Motels Into Homes" (2025-12-09): *"Always answer your phone. You never know what you're going to get."*
2. **Episode info verified from transcripts.** Kristee Leonard: KIR 2026-01-22 "The Gift Of Desperation," $50M annual, Austin TX. Bari Mill: KIR 2025-12-10 "From Division 1 Soccer To 40M in Year Six," $40M, Chicago. Karina Chavez: KIR 2025-12-09 "90 Referrals Each Year," Keller Williams.
3. **$100M removed from hook.** No individual agent guest at $100M+ production was found in the archive. Steve Shull (KIR 2023-01-12) coaches clients at $100M+ but is not a producing agent himself. Hook now references $40M/$50M only, traced to real guests.
4. **Source file overwritten** with the rewrite. Original fabricated version replaced.

---

## How this audit scales

This file is the template for auditing the rest of the repo. For each script, the audit file at `docs/audits/[SCRIPT-ID]-audit.md` should have:

1. **Verdict line** at the top (SHIP / DO NOT SHIP / NEEDS VERIFICATION).
2. **Findings** grouped CRITICAL / HIGH / MEDIUM / LOW, each citing a rule.
3. **Proposed rewrite** in a code block (or linked to a sibling file if too long).
4. **Changes summary** table.
5. **What I need from D.J. before shipping.**

The 60+ existing scripts can be audited in parallel this way, one file per audit. Then D.J. reviews, approves, and the audits get applied to the source scripts in a batch commit.
