---
lane: "do-this-dont-do-that"
carousel_for: "The agent who quotes the highest price to win a listing appointment isn't doing the seller a favor, and the data shows exactly what it costs"
hook_family: "swap-list"
heat: 2
slide_count: 5
goal: "engagement"
generated: "2026-10-07"
theme: "dark"
---

# Carousel: Win the appointment, lose the listing

`do-this-dont-do-that` is today's unambiguous oldest rotation slot
(`last_used: 2026-10-04` in `data/carousel-topic-rotation.json`), ahead of `market-tip` and
`dont-make-this-mistake` (tied at `2026-10-05`, `market-tip` winning the tie on array order,
same convention `KIRP-2026-10-01-business-account-swap-carousel.md` used). `stat` and
`kirp-guest-tip` both sit at `2026-10-06` and are not in play today.

Sourced per Step 2(b): today's news brief (`data/news-briefs/2026-10-07.md`), option 1 under
"Realtor tips (do this, not that)" -- `ST-0001`, taking a listing at a price the comps don't
support to win the appointment over an honest agent. The brief's receipt (Realtor.com, Joel
Berner, "more than 3 percentage points," published 2026-06-11) was re-verified at build time per
the standing re-verify rule: confirmed via Inman's coverage of the same Realtor.com report
("Realtor report: sellers have a 4-week window for best price," 2026-06-11) -- homes closing at
or before the 4-week mark sell 1.8% more than homes at the average 52-day days-on-market, homes
still active at 18 weeks sell 1.3% less, a 3-percentage-point spread. Checked first: no existing
carousel in `scripts/carousels/` references "four-week window," "Joel Berner," or this spread.

**The one idea:** the agent who promises the seller the highest number at the listing
appointment isn't competing on service, they're borrowing against the listing's best week and
charging the seller interest at closing. Rule 0 criterion 3, pattern reveal (what the flattering
agent does vs. what the data says happens next), and criterion 4, surprising statistic (the
3-point spread). Hook family `swap-list` (the deck's whole structure is the swap), differing
from today's paired deck (`myth-bust`) and from the most recently committed carousels
(`data-card`, `one-tactic-breakdown`, and `system-indictment`, all in the 2026-10-06 batch).

---

## SLIDE 1 -- HOOK
**Headline:**
The highest price isn't the best price.

**Subhead:**
It's the one that costs you three percent at closing.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Every week your listing sits, it loses leverage.

**Subhead:**
Homes that sell fast make more money than homes that sell eventually.

---

## SLIDE 3 -- THE TURN
**Headline:**
Here's the three-point gap nobody shows the seller.

**Body:**
Realtor.com tracked closed listings and found homes that sell at or before the four-week mark
bring in **1.8%** more than homes at the average 52-day pace. Homes still sitting at eighteen
weeks sell for 1.3% less. That's a three-point spread between pricing it right on day one and
pricing it to win the appointment. (Realtor.com, Senior Economist Joel Berner, 2026.)

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Do this, not that, at the listing appointment:

**Numbered list:**
1. **Don't quote the number that wins the appointment.** Quote the number the comps support,
   even when another agent already promised more.
2. **Do put the reduction schedule in the listing agreement on day one.** If the seller wants to
   test a higher number anyway, the cut is already agreed to, not a fight in week six.
3. **Do show the seller the three-point spread.** The agent who waits to cut isn't protecting
   the price. They're spending it.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Price it like week four, not week eighteen.

**Subhead:**
That's the only number that actually shows up at closing.

---

## Social Captions

### LinkedIn (PRIMARY)
The agent who promises the highest price at the listing appointment isn't doing the seller a
favor. They're borrowing against the listing's best week, and the seller pays it back with
interest at closing.

Realtor.com tracked closed listings and found homes that sell at or before the four-week mark
bring in 1.8% more than homes at the average 52-day pace. Homes still active at eighteen weeks
sell for 1.3% less. That's a three-point spread, and it starts the day the price gets set too
high to win the appointment.

Quote the number the comps support, not the number that flatters the seller. If they want to
test a higher price anyway, put the reduction schedule in the listing agreement on day one, so
the cut is a plan instead of a fight in week six.

Learn more at joinkale.com

#RealtorTips #ListingAgents #RealEstatePricing #KeepingItRealPodcast

### Instagram
The highest price quoted at the appointment isn't the best price for the seller. Homes that sell
inside four weeks bring in 1.8% more than average. Homes still sitting at eighteen weeks sell for
1.3% less. Price it like week four, not week eighteen.

#RealtorTips #ListingAgents #RealEstatePricing

### Facebook
Quoting the highest price to win the listing appointment costs the seller a three-point spread
at closing. Price to the comps, and put the reduction schedule in writing on day one.

#RealtorTips #ListingAgents

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-10-07-win-the-appointment-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Dark theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. This is an open deck. No keyword, no ManyChat flow, no ask on any platform.

**LinkedIn first comment:** https://joinkale.com/?src=carousel-kirp-2026-10-07-win-the-appointment-carousel

**Pinned first comment (IG and FB):** "The three-point spread: homes sold inside four weeks
bring in 1.8% more than average. Homes still active at eighteen weeks sell for 1.3% less.
(Realtor.com, Joel Berner, 2026.)"

---

## Data Source

- **Claim:** "Homes that close at or before the four-week mark sell 1.8% more than homes at the
  average 52-day days-on-market pace. Homes still active at eighteen weeks sell for 1.3% less, a
  three-percentage-point spread."
  - Source: Realtor.com, report covered by Inman, "Realtor report: sellers have a 4-week window
    for best price," published 2026-06-11. Statement attributed to Realtor.com Senior Economist
    Joel Berner.
  - Who was measured: closed home sale listings via MLS and deed records, not a survey of agents
    or consumers.
  - Status: confirmed. Re-verified at build time against Inman's coverage of the same report,
    matching the figures in today's news brief's `ST-0001` receipt ("more than 3 percentage
    points").
  - Fabrication audit: no number rounded or recombined. The 52-day average-pace baseline and the
    exact 1.8%/1.3% figures are carried verbatim from the verified source.
