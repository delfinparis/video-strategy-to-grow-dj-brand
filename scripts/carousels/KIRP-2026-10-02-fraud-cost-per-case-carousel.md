---
lane: "stat"
carousel_for: "Real estate fraud losses jumped 90 percent in two years while complaints rose only 30 percent, FBI data shows, meaning the average loss per case is up 46 percent"
hook_family: "data-card"
heat: 3
slide_count: 5
goal: "engagement"
generated: "2026-10-02"
theme: "light"
---

# Carousel: The real fraud trend is the price per case

`stat` is today's second-oldest rotation slot, tied with `kirp-guest-tip` at `last_used:
2026-09-30` in `data/carousel-topic-rotation.json`. `stat` wins the tie because it is listed
before `kirp-guest-tip` in the rotation file's `topics` array (same array-order tiebreak used on
2026-10-01). `dont-make-this-mistake` was today's unambiguous oldest slot, built as the paired
deck. `kirp-guest-tip` is not today's slot, so both decks reskin to KR normally.

Sourced per Step 2(b): today's news brief (`data/news-briefs/2026-10-02.md`) surfaces "As fraud
costs hit $275M, NAR helps real estate agents spot red flags with new digital hub" (Inman,
2026-10-01) as an NF candidate. Re-verified independently at build time per Rule 1 rather than
trusting the brief's headline figure: fetched NAR's own newsroom article directly today,
2026-10-02 ("Online Real Estate Fraud Climbed to $275M in 2025, FBI Says," published
2026-04-13), which gives the full year-by-year breakdown, not just the single $275M headline
number. Checked first: no existing carousel uses "$275 million," "275M," or any of these FBI/IC3
fraud figures.

**The one idea:** the complaint count isn't what's climbing fastest, the dollar amount per case
is. Complaints rose 30 percent from 2023 to 2025; the money lost rose 90 percent; the average
loss per complaint rose 46 percent. Rule 0 criterion 4, surprising statistic (a sourced number
agents haven't seen framed this way), and criterion 3, pattern reveal (what looks like "more
scams" is actually "bigger scams"). Hook family `data-card`, differing from today's paired deck
(`one-tactic-breakdown`) and from the most recently committed carousels (`named-stakes`,
`KIRP-2026-10-01-price-cut-timing-carousel.md`; `mirror`,
`KIRP-2026-10-01-business-account-swap-carousel.md`; `data-card` last appeared two days earlier
on `KIRP-2026-09-30-rate-lockin-reversal-carousel.md`, a different topic).

---

## SLIDE 1 -- HOOK
**Headline:**
$275 million lost to fraud last year.

**Subhead:**
The FBI's own numbers, and the one habit that catches most of it before the wire goes out.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Complaints are up 30 percent. The money lost is up 90 percent.

**Subhead:**
FBI data on real estate fraud, 2023 to 2025. The average loss per case is climbing, not just the
count.

---

## SLIDE 3 -- THE TURN
**Headline:**
The scams aren't getting more common. They're getting more expensive.

**Body:**
The FBI's Internet Crime Complaint Center logged 9,521 real estate fraud complaints in 2023,
totaling about $145 million. By 2025 that was 12,368 complaints and $275 million. Complaints rose
30 percent. The money lost rose 90 percent. The average loss per complaint climbed from about
$15,000 to about $22,000, a 46 percent jump. Whoever is running these scams isn't casting a wider
net. They're walking away with more per deal.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Before the next wire goes out, check:

**Numbered list:**
1. **Call the title company at a number you looked up yourself.** Never the number on the email
   with the new instructions.
2. **Treat any sudden change to wire instructions as a stop sign.** Verify it by phone before you
   move a dollar.
3. **Look at the sender's email domain, not just the name on it.** One swapped letter is the
   whole scam.
4. **Ask anyone who refuses a phone or video call why.** NAR's own fraud hub flags that refusal
   as a top warning sign.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
A hub doesn't stop a wire fraud. A phone call does.

**Subhead:**
Pick up the phone before you ever move someone else's money.

---

## Social Captions

### LinkedIn (PRIMARY)
Real estate fraud cost $275 million last year, according to the FBI's Internet Crime Complaint
Center. That's up from about $145 million in 2023.

Complaints only rose 30 percent in that time. The money lost rose 90 percent. The average loss
per complaint climbed from about $15,000 to about $22,000. Whoever is running these scams isn't
casting a wider net. They're walking away with a bigger number per deal.

NAR just launched a fraud hub listing the warning signs: a seller who won't verify their
identity, documents that don't match, a sudden change to wire instructions, an email domain
that's one letter off, a buyer or seller who refuses to ever get on the phone.

A list of red flags doesn't stop a wire fraud. Verifying every wire instruction by phone, on a
number you looked up yourself, does.

#RealEstateAgents #RealEstateFraud #WireFraud #KeepingItRealPodcast

### Instagram
Real estate fraud hit $275 million last year, FBI data shows, up from $145 million in 2023. The
average loss per complaint climbed 46 percent. Before your next wire, verify the instructions by
phone, on a number you looked up yourself.

#RealEstateAgents #RealEstateFraud #WireFraud

### Facebook
Real estate fraud losses hit $275 million last year, the FBI says, up from $145 million two years
ago. Verify every wire instruction by phone before you move anyone's money.

#RealEstateAgents #WireFraud

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-10-02-fraud-cost-per-case-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Light theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. This is an open deck. No keyword, no ManyChat flow, no ask on any platform.

**LinkedIn first comment:** https://joinkale.com/?src=carousel-kirp-2026-10-02-fraud-cost-per-case-carousel

**Pinned first comment (IG and FB):** "The source: FBI Internet Crime Complaint Center data, as
reported by NAR, April 13, 2026. Full citation in the Data Source on the carousel file."

---

## Data Source

- **Claim:** "$275 million lost to real estate fraud in 2025, up from about $145 million in
  2023."
  - Source: FBI Internet Crime Complaint Center (IC3) data, as reported by the National
    Association of REALTORS, "Online Real Estate Fraud Climbed to $275M in 2025, FBI Says,"
    published 2026-04-13
    (https://www.nar.realtor/news/real-estate-news/online-real-estate-fraud-climbed-to-275m-in-2025-fbi-says).
  - Who was measured: complaints filed to the FBI's IC3 nationally, not an agent or consumer
    survey.
  - Status: confirmed. Fetched directly today, 2026-10-02, from NAR's own newsroom article.

- **Claim:** "12,368 complaints in 2025, versus 9,521 in 2023, about a 30 percent increase in the
  number of complaints."
  - Source: same as above.
  - Status: confirmed.

- **Claim:** "The average loss per complaint climbed from about $15,000 in 2023 to about $22,000
  in 2025, a 46 percent increase."
  - Status: math performed on the real reported figures above, shown here per Rule 1.
    $145,000,000 / 9,521 = $15,229. $275,000,000 / 12,368 = $22,233.
    ($22,233 - $15,229) / $15,229 = 46.0%.

- **Scope caveat:** these are the FBI IC3's own reported national totals for real estate-related
  internet crime complaints, not survey data of agents or consumers, and are U.S. national
  figures, not Chicago-specific. No slide or caption claims otherwise.

- **Dropped framing:** 2022 logged higher losses than either year used here ($397 million per the
  same NAR article), so this deck does not claim fraud is "at a record" or "at an all-time high."
  The claim made is limited to the 2023-to-2025 trend, which the data supports directly.
