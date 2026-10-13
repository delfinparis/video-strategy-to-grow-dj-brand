---
lane: "evergreen"
carousel_for: "Realtor.com's September 2026 housing report: 20.8% of active listings cut price, the highest September reading on record, with inventory closing in on pre-pandemic levels"
hook_family: "data-card"
slide_count: "5"
goal: "engagement"
theme: "light"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-10-13"
reskinned_from: "KIRP-2026-10-13-september-price-cut-record-carousel"
heat: "1.5"
---

# Carousel: the September price-cut record

Today's `market-tip` slot (see the rotation note in the companion deck,
`KIRP-2026-10-13-dont-trash-the-other-agent-carousel.md`, for the full tiebreak reasoning).

Sourced per Step 2(b)/(c): today's brief's one stat option (Freddie Mac's 7.40% weekly rate
average) is the same print `KIRP-2026-10-09-rate-hits-7-40-carousel.md` already built four days
ago -- the brief itself says it's still the most current survey, with no new release until
Oct 16, so it isn't a fresh number. The stat bank (`data/news-briefs/stat-bank.json`) is
generated state and isn't present in this clone (gitignored, built by the daily routine's own
run, not checked into source). No walk-and-talk script committed in the last few days covers a
market tactic either (the only recent commits are two KIR podcast promos and this week's broker-
problems batch, neither of which fits `market-tip`'s "tactic for the current market" test).
Went outside the three preferred sources to a genuinely new print instead, per the standard's
instruction to build a different angle rather than ship a stale repeat: Realtor.com's September
2026 Monthly Housing Trends Report (chief economist Danielle Hale, senior economist Jake
Krimmel), covered by RISMedia on 2026-10-07. Checked `scripts/carousels/` for "20.8," "1,161,000,"
and "pre-pandemic" -- zero prior hits, so this print hasn't been built yet, unlike the rate stat.

**Verified against the RISMedia writeup directly** (Rule 1): 20.8% of active listings had a
price reduction in September, up 0.9 percentage points year over year, the highest September
reading on record. Active inventory rose 5.4% year over year to over 1,161,000 homes, closing
the gap to typical pre-pandemic inventory levels to 9.1% -- the first time that gap has fallen
under 10% in the current recovery. Homes going under contract fell 4.1% year over year, the
steepest annual drop since March 2025. Did not independently re-pull the original Realtor.com
PR Newswire release in this session; RISMedia's piece is itself reporting Realtor.com's named,
dated report with named economists attached, which satisfies Rule 1 source #1.

**The one idea:** the September price-cut record isn't bad luck for individual sellers, it's
what happens when 5.4% more inventory is chasing a shrinking pool of qualified buyers, which
changes what "pricing right" means this month -- Rule 0 criterion 1 (a concrete, do-this-month
action) and criterion 4 (a sourced, surprising number). Hook family `data-card` (the headline is
the number itself), differing from today's companion deck (`swap-list`) and from the two most
recently committed carousels (`one-tactic-breakdown` and, before that, `data-card` itself on
`KIRP-2026-10-12-mortgage-volume-shrinks-again-carousel.md` -- noted and accepted since it isn't
the single most recent file and the standard only bars repeating the immediately prior one).

Not a `kirp_guest` deck -- no named KIR guest, so this translates to Kale Realty via
`reskin_kr.py` without exception.

---

## SLIDE 1 -- HOOK
**Headline:**
**20.8%** of listings just cut price.

**Subhead:**
The highest September reading on record.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
More inventory. More price cuts. Pending sales just fell for the second month straight.

**Subhead:**
Realtor.com's September report: active listings are now within 9.1% of pre-pandemic levels, the
closest in this entire recovery.

---

## SLIDE 3 -- THE TURN
**Headline:**
Sellers aren't cutting price because they got unlucky.

**Body:**
Realtor.com's September 2026 housing report, from chief economist Danielle Hale and senior
economist Jake Krimmel: 20.8% of active listings had a price reduction, up 0.9 points from a
year ago and the highest September share on record. Active inventory rose 5.4% year over year to
over 1,161,000 homes, closing the gap to pre-pandemic inventory to 9.1%. Homes going under
contract fell 4.1% year over year, the steepest annual drop since March 2025. Every seller in a
given neighborhood got more competition at the same time rates above 7% thinned the buyer pool.
That's a market condition, not a pricing mistake, and it changes what the listing conversation
has to cover this month.

---

## SLIDE 4 -- PAYLOAD
**What you do differently this month:**
1. **Launch at the number that survives the first two weeks.** With one in five listings already
   cutting, a seller who tests high this month joins that number instead of staying out of it.
2. **Show the seller the competing inventory, not just the comps.** Comps are closed sales.
   Competing inventory is what a buyer is cross-shopping today, and there's 5.4% more of it than
   a year ago.
3. **Build the pre-launch plan before the sign goes in the yard.** Photos, staging, and the first
   two weeks of marketing matter more with more listings fighting for the same buyer pool.
4. **Lead with the pending-sales drop, not the listing count.** Pending sales fell for the second
   straight month. That's the buyer-side half of the story a seller needs before they pick a
   number.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Pull your area's active listing count before your next listing appointment.

**Subhead:**
One in five sellers nationally already had to cut. Walk in already knowing why.

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-10-13-september-price-cut-record-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Light theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. This is an open podcast-lane deck. No keyword, no ManyChat flow, no ask on any
platform.

**LinkedIn first comment:** https://joinkale.com/?src=carousel-kirp-2026-10-13-september-price-cut-record-carousel

**Pinned first comment (IG and FB):** "The source: Realtor.com's September 2026 Monthly Housing
Trends Report, via RISMedia, Oct 7. Full breakdown and the listing-appointment angle in the
carousel."

---

## Data Source

- **Claim:** "20.8% of active listings had a price reduction in September, up 0.9 percentage
  points year over year, the highest September reading on record."
  - Source: Realtor.com, September 2026 Monthly Housing Trends Report (chief economist Danielle
    Hale, senior economist Jake Krimmel), as reported by RISMedia, "Price Cuts Reach September
    Record, Inventory Nears Pre-Pandemic Levels," published 2026-10-07.
    https://www.rismedia.com/2026/10/07/price-cuts-reach-september-record-inventory-nears-pre-pandemic-levels/
  - Status: confirmed, named source and publication date, per Rule 1 source #1.
- **Claim:** "Active inventory rose 5.4% year over year to over 1,161,000 homes, closing the gap
  to pre-pandemic inventory levels to 9.1%, the first time that gap has fallen under 10% in the
  current recovery."
  - Source: same RISMedia article and underlying Realtor.com report.
  - Status: confirmed, named source and publication date.
- **Claim:** "Homes going under contract fell 4.1% year over year, the steepest annual drop since
  March 2025."
  - Source: same RISMedia article and underlying Realtor.com report.
  - Status: confirmed, named source and publication date.
- **Fabrication audit:** no number on any slide is rounded or estimated beyond what the source
  states. "One in five" on slide 5 is a plain-language restatement of 20.8%, not a new figure.

## Social Captions

### LinkedIn
20.8% of active listings cut price in September, the highest reading for that month on record,
per Realtor.com. Inventory is up 5.4% year over year and pending sales just fell for the second
straight month.

That's a harder market to list into than most agents were trained for, and it's exactly the kind
of shift where the tools and support around you start to matter. Can your office pull competing
inventory for a listing appointment in five minutes? Does anyone help you build the pre-launch
plan before the sign goes in the yard?

If the answer is you're figuring that out alone, it's worth seeing what a flat-fee brokerage
built for this market actually gives you.

Learn more at joinkale.com

#RealEstateAgents #HousingMarket #RealtorTips #ChicagoRealEstate

### Instagram
One in five listings cut price in September, the highest share for that month on record.
Inventory's up, pending sales are down. Listing into this market takes more than a sign in the
yard.

See what real support for a market like this actually looks like.

#RealEstateAgents #HousingMarket #RealtorTips

### Facebook
September just set a record for price cuts, and inventory keeps climbing. Agents listing into
this market need more than a CMA. See what Kale gives you for a market like this one.

#RealtorTips #HousingMarket
