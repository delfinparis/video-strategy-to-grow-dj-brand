---
lane: "news-repurpose"
source_script: "scripts/inside-the-industry/NF-074-half-of-buyers-never-call-a-second-agent.md"
carousel_for: "Zillow's 2025 Consumer Housing Trends Report: 50% of buyers hired the first agent they contacted, 41% hired after a single conversation"
hook_family: "named-stakes"
heat: 4
slide_count: 5
goal: "engagement"
generated: "2026-10-16"
theme: "light"
---

# Carousel: half of buyers never call back

Companion to today's `do-this-dont-do-that` deck
(`KIRP-2026-10-16-never-write-fixer-upper-carousel.md`), which has the full rotation
reasoning. This deck is the `stat` slot: `stat` and `dont-make-this-mistake` are tied at
`last_used: 2026-10-14`, and `stat` wins the array-order tiebreak explained there.

Sourced per Step 2(d): walk-and-talk script
`scripts/inside-the-industry/NF-074-half-of-buyers-never-call-a-second-agent.md`, part of the
same 2026-10-13 Zillow data batch as the companion deck's NF-079, and not yet carouselized
(checked every `NF-0` number referenced across `scripts/carousels/` -- zero prior hits for
NF-074).

**Re-verified directly against the source**, not just NF-074's own Data Source block: fetched
Zillow Group's "Consumer Housing Trends Report for Agents 2025" PDF directly
(`zillowstatic.com/bedrock/app/uploads/sites/60/2025/10/Consumer-Housing-Trends-Report-for-Agents-2025_102925.pdf`),
2026-10-16. Confirmed unchanged: among buyers who contacted at least one agent, 50% hired the
first agent they contacted (up from 47% in 2023 and 2024), and 41% hired after only one
contact. Survey: ~10,200 buyers, surveyed April-September 2025.

**The one idea:** most agents treat the first call from a new lead as a warm-up, something to
get through before the real pitch later. Zillow's numbers say there often is no later --
half the time there is no second agent to lose to, and four in ten buyers decide after one
conversation. Rule 0 criterion 4 (a sourced, surprising statistic from a 10,200-buyer survey)
and criterion 3 (pattern reveal: what most agents do with a new lead versus what the numbers
say actually wins it). Hook family `named-stakes` (a specific, sourced percentage carries the
whole slide), differing from the companion deck (`swap-list`) and from the most recently
committed carousel (`mirror`, `KIRP-2026-10-15-the-first-ten-days-carousel.md`).

Not a `kirp_guest` deck. Zillow is the data source, quoted from its own published report, not a
Keeping It Real podcast guest. This deck translates to Kale Realty via `reskin_kr.py` without
exception.

---

## SLIDE 1 -- HOOK
**Headline:**
Half of buyers never call a second agent.

**Subhead:**
The first call is not a warm-up. It is the interview.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
41% of buyers hire an agent after exactly one conversation.

**Subhead:**
Zillow surveyed about 10,200 buyers. There is often no round two.

---

## SLIDE 3 -- THE TURN
**Headline:**
Most agents treat the first call like small talk. The numbers say it's the whole decision.

**Body:**
Zillow's 2025 Consumer Housing Trends Report found that among buyers who contacted at least
one agent, 50% hired the first one they talked to, up from 47% the two years before. 41%
hired after a single conversation. The usual playbook, send a few listings and follow up
later, assumes there will be a later. For roughly half of buyers, there isn't one.

---

## SLIDE 4 -- PAYLOAD
**What you do on that first call:**
1. **Answer it fast.** Half the time, being second means you never get a turn at all.
2. **Treat it as the interview, not the intro.** The buyer may already be deciding while you're
   still warming up.
3. **Ask for the meeting on that call.** Don't default to "I'll send you some listings" and
   wait for them to call back.
4. **Stop scripting a slow follow-up sequence for a decision that often happens once.**

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Answer fast. Ask for the meeting on the first call. Don't wait for round two.

**Subhead:**
That first conversation is the interview, whether you treat it that way or not.

---

## Social Captions

### LinkedIn
Half of buyers never call a second agent.

That's from Zillow's 2025 Consumer Housing Trends Report, a survey of about 10,200 buyers.
Among buyers who contacted an agent, 50% hired the first one they talked to. 41% hired after
only one conversation.

Most of us were trained to treat that first call as a getting-to-know-you step. Send a few
listings, follow up in a couple of days, earn the meeting later.

The numbers say there often isn't a later. That first conversation is the interview.

Answer new leads fast, and ask for the meeting on that first call instead of waiting for round
two.

#RealEstateAgents #RealtorTips #LeadConversion #InsideTheIndustry

### Instagram
Half of buyers never call a second agent.

Zillow's 2025 survey of 10,200 buyers: 50% hired the first agent they contacted. 41% hired
after one conversation.

That first call is the interview. Answer fast and ask for the meeting.

#RealEstateAgents #RealtorTips #InsideTheIndustry

### Facebook
Buying a home soon? The first agent you talk to is often the one you'll hire, whether you
planned on it or not. Zillow's latest survey found 41% of buyers decide after a single
conversation.

#HomeBuying #RealEstateAgents

---

## Data Source

- **Claim:** "Half of buyers never call a second agent." / "50% hired the first one they
  talked to."
  - Source: Zillow Group, "Consumer Housing Trends Report for Agents 2025," published
    2025-10-29 (buyers: ~10,200 surveyed April-September 2025):
    https://www.zillowstatic.com/bedrock/app/uploads/sites/60/2025/10/Consumer-Housing-Trends-Report-for-Agents-2025_102925.pdf .
    Table: "Among buyers that contacted at least 1 agent," 2025 column: hired the first agent
    they contacted, 50% (47% in 2023 and 2024). Re-fetched directly in this session
    (2026-10-16), confirmed unchanged from NF-074's original 2026-10-13 fetch.
  - Status: confirmed.
- **Claim:** "41% of buyers hire an agent after exactly one conversation."
  - Source: Same report. The typical buyer had 2 contacts with an agent before hiring; 41%
    hired after only one contact.
  - Status: confirmed (41% spoken as "four in ten" / "41%").
- **Claim:** "Most agents treat the first call like small talk" / "the usual playbook assumes
  there will be a later."
  - Source: Editorial framing contrasting common practice with the measured hiring pattern, not
    a separately sourced figure.
  - Status: commentary.
- **Fabrication audit:** no figure beyond Zillow's own published 50% / 41% (and the 47% prior-
  year comparison) appears on this deck. No second, unrelated stat is blended into the same
  sentence. Matches NF-074's own fabrication audit, re-confirmed against the live source PDF.
