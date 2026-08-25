---
lane: "market-tip"
carousel_for: "Rates eased again, but pending sales hit their lowest point since January. The rate was never the real objection."
hook_family: "myth-bust"
heat: 2
slide_count: 5
goal: "engagement"
generated: "2026-08-25"
theme: "dark"
---

# Carousel: The rate wasn't the objection

Market-tip deck, today's oldest-dated rotation type (last used 2026-08-22). Not sourced from
today's news brief (`data/news-briefs/2026-08-25.md`, option 5), because that brief's headline
claim did not hold up under re-verification (Rule 1): the brief said rates fell "for the second
week in a row," citing Fortune's daily tracker at 6.72%, but Fortune's own page showed that
figure was actually up 5 basis points from the prior week, not down. Rebuilt the angle from
Freddie Mac's own weekly survey instead, fetched directly at build time: the PMMS 30-year fixed
averaged 6.65% for the week of August 20, 2026, down 2 basis points from 6.67% the week before
(https://www.freddiemac.com/pmms). Paired against NAR's Pending Home Sales Report, published
August 18, 2026, which put July's signed contracts down 2.3% month over month and 2.2% year over
year, the lowest level since January 2026, confirmed across NAR's own newsroom, Bloomberg, and
Mortgage Professional America.

**The one idea:** rates ticked down again and contract signings still fell to an eight-month low,
so the rate itself is not what is holding buyers back. Rule 0 criterion 3, pattern reveal (the gap
between the number agents lead with and the number that actually moved), and criterion 1,
tactical specificity (three questions to ask instead of quoting the rate). Hook family
`myth-bust`, differing from the two most recently committed carousels (`swap-list` and
`data-card`, both 2026-08-24) and from today's paired deck (`system-audit`,
`KIRP-2026-08-25-portal-dependency-mistake-carousel.md`).

---

## SLIDE 1 -- HOOK
**Headline:**
Rates fell again. Buyers still aren't signing.

**Subhead:**
Pending sales just hit their lowest point since January. The rate was never the real objection.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Your buyer isn't waiting on a number anymore.

**Subhead:**
Contract signings dropped to an eight-month low even as rates eased. Something else is holding them back.

---

## SLIDE 3 -- THE TURN
**Headline:**
The objection changed. Most scripts didn't.

**Body:**
Freddie Mac's own weekly survey shows the 30-year fixed easing to **6.65%** the week of August
20, down from 6.67% the week before. NAR's Pending Home Sales Report, out August 18, shows signed
contracts fell 2.3% in July and sit at their lowest level since January. If the rate alone were
the blocker, a small drop should have moved that number. It didn't. The hesitation sitting in most
pipelines right now is confidence, not math, and a rate update doesn't answer it.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What to ask instead of quoting the rate:

**Numbered list:**
1. **"What would make you feel confident closing this month, not just the rate?"** Surfaces the real hesitation instead of a number neither of you controls.
2. **"If prices dip after you buy, what's your plan?"** Answers the fear directly instead of arguing rates will fall further.
3. **"What does this house cost at today's price trend in six months?"** Replaces a rate debate with a dollar one they can picture.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
The rate conversation was never the objection.

**Subhead:**
The confidence conversation is. Have that one next.

---

## Social Captions

### LinkedIn (PRIMARY)
Freddie Mac's weekly survey put the 30-year fixed at 6.65 percent for the week of August 20, down from 6.67 percent the week before.

NAR's own pending home sales report, published August 18, told a different story. Signed contracts fell 2.3 percent in July and sit at their lowest level since January.

If the rate alone were the objection, a small drop should have moved that number. It didn't. The hesitation sitting in most pipelines right now is confidence, not math.

Slide 4 has three questions that get at the real objection instead of another rate update.

#RealEstateAgents #MortgageRates #RealtorTips #KeepingItRealPodcast

### Instagram
Rates eased again the week of August 20. Pending home sales still fell to their lowest point since January.

If the rate were the real objection, that drop should have moved the number. Slide 4 has three questions that get at what's actually holding your buyer back.

#RealEstateAgents #MortgageRates #RealtorTips

### Facebook
Rates ticked down again and contract signings still hit an eight-month low. The rate isn't the objection anymore. Slide 4 has three better questions to ask.

#RealEstateAgents #MortgageRates

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-08-25-rate-confidence-carousel/slide-01.png` through
`slide-05.png`. Upload in filename order. Dark theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. This is an open deck. No keyword, no ManyChat flow, no ask on any platform.

**LinkedIn first comment:** https://joinkale.com/?src=carousel-kirp-2026-08-25-rate-confidence-carousel

**Pinned first comment (IG and FB):** "The numbers: Freddie Mac PMMS, week of August 20, 2026
(6.65%, down from 6.67%), and NAR's Pending Home Sales Report, published August 18, 2026 (signed
contracts down 2.3% in July, lowest since January). Full citations in the Data Source on the
carousel file."

---

## Data Source

- **Claim:** "The 30-year fixed mortgage rate averaged 6.65% for the week of August 20, 2026,
  down from 6.67% the week before."
  - Source: Freddie Mac, Primary Mortgage Market Survey (PMMS), week of August 20, 2026 --
    https://www.freddiemac.com/pmms
  - Who was measured: Freddie Mac's national weekly lender survey.
  - Status: confirmed, fetched directly at build time (2026-08-25).
- **Claim:** "Pending home sales fell 2.3% in July 2026 and were down 2.2% year over year, the
  lowest level since January 2026."
  - Source: National Association of Realtors, "NAR Pending Home Sales Report Shows 2.3% Decrease
    in July," published August 18, 2026 --
    https://www.nar.realtor/newsroom/NAR-Pending-Home-Sales-Report-Shows-2-3-Decrease-in-July
  - Who was measured: NAR's national index of signed purchase contracts (pending sales), not
    closed sales.
  - Status: confirmed, cross-checked against Bloomberg and Mortgage Professional America coverage
    of the same NAR release at build time (2026-08-25).
- **Correction note:** today's news brief (option 5) claimed rates fell "for the second week in a
  row" at 6.72%, sourced to Fortune's daily tracker. Fetched Fortune's own page directly and found
  6.72% was up 5 basis points from the prior week, contradicting the brief's framing. Dropped that
  figure and rebuilt the angle on Freddie Mac's PMMS instead, which is the survey the industry
  treats as the reference rate.
