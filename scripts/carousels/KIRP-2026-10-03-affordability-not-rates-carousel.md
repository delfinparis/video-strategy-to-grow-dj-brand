---
lane: "market-tip"
carousel_for: "NAR's 2026 Member Profile: 27% of agents say affordability, not rates or inventory, is the top thing stopping a buyer from closing"
hook_family: "named-stakes"
heat: 3
slide_count: 5
goal: "engagement"
generated: "2026-10-03"
theme: "light"
---

# Carousel: Affordability beat the rate excuse

`market-tip` is today's second-oldest rotation slot, tied with `do-this-dont-do-that` at
`last_used: 2026-10-01` in `data/carousel-topic-rotation.json`. `market-tip` wins the tie because
it is listed before `do-this-dont-do-that` in the rotation file's `topics` array (same
array-order tiebreak used on 2026-10-01 and 2026-10-02). `kirp-guest-tip` was today's
unambiguous oldest slot, built as the paired deck.

Sourced per Step 2(b): yesterday's news brief (`data/news-briefs/2026-10-02.md`) surfaces the
evergreen stat tip -- "Affordability is the top constraint keeping buyers out of the market at
27%," sourced to the NAR 2026 Member Profile via HousingWire. Re-verified independently at build
time per Rule 1 rather than trusting the brief's paraphrase: fetched the HousingWire article
directly today, 2026-10-03
(https://www.housingwire.com/articles/nar-2026-member-profile-experience/, published 2026-06-25
by Brooklee Han). The brief's framing needed one correction: the 27% is agents' own ranking of
what limits *their clients*, not a buyer or consumer survey, and the article gives the next two
reasons by name (lack of inventory, 12%; difficulty finding the right property, 11%), which this
deck uses to make the point sharper than the brief did. Checked first: no existing carousel uses
this NAR 2026 Member Profile affordability figure.

**The one idea:** agents rank affordability as the #1 reason a buyer stalls, by more than two to
one over the next closest reason (lack of inventory). That reframes "they're waiting for rates to
drop" as the wrong read -- the fix isn't waiting, it's making this month's payment work. Rule 0
criterion 4 (a sourced number agents haven't seen framed this way) and criterion 6 (a controllable
action: run the payment math now instead of waiting on the Fed). Hook family `named-stakes` (a
real, sourced number carries the whole hook), differing from today's paired deck
(`swap-and-list`) and from the most recently committed carousel (`data-card`,
`KIRP-2026-10-02-fraud-cost-per-case-carousel.md`).

---

## SLIDE 1 -- HOOK
**Headline:**
Rates aren't the problem. Price is.

**Subhead:**
The #1 reason agents say buyers stall this year, straight from NAR's newest member survey.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
27% of agents say affordability is the #1 thing stopping a sale.

**Subhead:**
Not inventory. Not the wrong house. NAR's 2026 Member Profile, reported June 2026.

---

## SLIDE 3 -- THE TURN
**Headline:**
**27%** picked affordability. Inventory got 12%.

**Body:**
NAR asked brokerage specialists what limits their clients from completing a purchase.
Affordability won by more than two to one over the next closest reason, lack of inventory, and
nearly three to one over "can't find the right property." Buyers aren't shopping longer. They're
running math that doesn't close yet.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What that changes about this month's conversation:

**Numbered list:**
1. **Run the full monthly number before the tour.** Taxes and insurance included, not just
   principal and interest.
2. **Put a seller-paid rate buydown on every offer you write.** It moves the payment more than a
   price cut moves the payment.
3. **Build a 3-to-5 home list priced for today's payment.** Show it before a buyer says they're
   "just going to wait."

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
The buyer wasn't waiting on the Fed. They were waiting on math that works.

**Subhead:**
Have that conversation this week, before they stop looking altogether.

---

## Social Captions

### LinkedIn (PRIMARY)
NAR's 2026 Member Profile asked brokerage specialists one question: what's limiting your clients
from completing a purchase? Affordability won by a wide margin at 27%, more than double the next
reason, lack of inventory, at 12%. Difficulty finding the right property came in at 11%.

That ranking says something agents keep missing. The story everyone tells is "buyers are waiting
for rates to drop." The data says they're not waiting on the Fed. They're stuck on a monthly
number that doesn't work yet.

Three things change this month because of that. Run the full payment, taxes and insurance
included, before a buyer ever sees a listing. Put a seller-paid rate buydown on every offer, since
it moves the payment more than a price cut does. And build a short list, three to five homes,
priced for today's payment, ready before a buyer says they're going to wait it out.

Source: NAR 2026 Member Profile, reported by HousingWire, June 25, 2026.

#RealEstateAgents #HomeAffordability #MarketUpdate

### Instagram
27% of agents say affordability, not rates or inventory, is the #1 thing stopping a sale.
Inventory only got 12%.

Buyers aren't waiting for rates to drop. They're waiting for a payment that works. Three moves for
this month's conversations are in the carousel.

Source: NAR 2026 Member Profile, via HousingWire, June 2026.

#RealEstateAgents #HomeAffordability #MarketUpdate

### Facebook
NAR's newest member survey: 27% of agents say affordability, not rates, is the top thing stalling
a sale. The fix isn't waiting for rates. It's making this month's payment work. Full breakdown in
the carousel.

#RealEstateAgents #MarketUpdate

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-10-03-affordability-not-rates-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Light theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. This is an open deck. No keyword, no ManyChat flow, no ask on any platform.

**LinkedIn first comment:** https://joinkale.com/?src=carousel-kirp-2026-10-03-affordability-not-rates-carousel

**Pinned first comment (IG and FB):** "The source: NAR's 2026 Member Profile, as reported by
HousingWire, June 25, 2026. Full citation in the Data Source on the carousel file."

---

## Data Source

- **Claim:** "27% of brokerage specialists (agents) name affordability as the factor most
  limiting their clients from completing a home purchase, ahead of lack of inventory (12%) and
  difficulty finding the right property (11%)."
  - Source: National Association of REALTORS, 2026 Member Profile, as reported by HousingWire,
    "NAR 2026 Member Profile: Experience," by Brooklee Han, published 2026-06-25
    (https://www.housingwire.com/articles/nar-2026-member-profile-experience/).
  - Who was measured: brokerage specialists/agents surveyed by NAR, asked what most limits their
    clients from completing a purchase -- an agent-perception survey, not a direct buyer or
    consumer survey.
  - Status: confirmed. Fetched directly today, 2026-10-03, from the HousingWire article.

- **Correction from the source brief:** yesterday's news brief (`data/news-briefs/2026-10-02.md`)
  paraphrased this as "affordability is the top constraint keeping buyers out of the market,"
  which reads as a buyer survey. The underlying NAR figure is agents ranking what limits their
  clients, a narrower and more accurate claim. No slide or caption in this deck states or implies
  it is a buyer-reported figure.

- **Scope caveat:** this is a national NAR survey of agents, not Chicago-specific, and no slide or
  caption claims a local figure.
