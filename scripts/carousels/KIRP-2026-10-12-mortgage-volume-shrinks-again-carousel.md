---
lane: "stat"
carousel_for: "MBA's own October 2026 forecast: total 2027 mortgage volume falls to $1.99 trillion, down 5% from 2026, because refinances drop 17% while purchase volume actually rises slightly"
hook_family: "data-card"
heat: 2
slide_count: 5
goal: "engagement"
generated: "2026-10-12"
theme: "light"
---

# Carousel: the 2027 mortgage forecast

`stat` is today's second-oldest rotation slot after `kirp-guest-tip` (see the companion deck,
`KIRP-2026-10-12-one-system-three-hires-carousel.md`, for the full tie-break explanation: `stat`
and `do-this-dont-do-that` tie at `last_used: 2026-10-10`, and `stat` wins on array order).

Sourced per Step 2(b): today's news brief (`data/news-briefs/2026-10-12.md`) lists "MBA forecast:
Mortgage volume to dip below $2T in 2027 as 7% rates linger" (HousingWire) in its full story
list. Today's and yesterday's "stat tip" boxes were both already shipped as carousels (today's
$14.66T senior-equity figure ran 2026-10-06 as `KIRP-2026-10-06-senior-equity-high-carousel.md`;
yesterday's 27% NAR affordability figure ran 2026-10-03 as
`KIRP-2026-10-03-affordability-not-rates-carousel.md`), so neither is a new angle. The stat bank
json (`data/news-briefs/stat-bank.json`) is gitignored generated state and is not present on this
machine this session, so that source is unavailable today. Fetched the HousingWire article
directly (`https://www.housingwire.com/articles/mba-originations-forecast-2027-rates/`, byline
Flávia Furlan Nunes, published 2026-10-11, 7:22pm) rather than relying on the brief's headline
alone. Checked `scripts/carousels/` for "1.99 trillion," "MBA," and "Fratantoni" first -- no
prior deck covers this specific 2027 forecast.

**The one idea:** MBA's own forecast has total 2027 mortgage volume shrinking again, to $1.99
trillion, but not evenly -- purchase originations actually tick up slightly to $1.42 trillion
while refinances collapse 17% to $571 billion. The number that is dropping is refinance
business, not the purchase business agents actually work, which reframes "wait for rates to
drop" as planning around the wrong half of the market. Rule 0 criterion 4 (a sourced number
agents haven't seen framed this way) and criterion 3 (pattern reveal: total volume down, purchase
volume up). Hook family `data-card` (the number is the whole slide), differing from today's
companion deck (`one-tactic-breakdown`) and from the two most recently committed carousels
(`mirror` and `myth-bust`, both `*-2026-10-11-*-carousel.md`).

---

## SLIDE 1 -- HOOK
**Headline:**
**$1.99 trillion.** Smaller than this year.

**Subhead:**
The mortgage industry's own forecast for 2027.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
The group that forecasts mortgages says 2027 is smaller than 2026, not bigger.

**Subhead:**
And rates stay above 7 percent the whole year, by their own number.

---

## SLIDE 3 -- THE TURN
**Headline:**
It isn't shrinking evenly. Refinances are the ones collapsing.

**Body:**
The Mortgage Bankers Association's own October 2026 forecast puts total 2027 mortgage volume at
1.99 trillion dollars, down 5 percent from 2026's 2.1 trillion. But purchase loans actually rise
slightly, up to 1.42 trillion. Refinances fall 17 percent, down to 571 billion. The part of the
market getting smaller is refinance business. The part agents actually work, home purchases, is
not.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What this means for your business plan:

**Numbered list:**
1. **Stop waiting on a refi-driven rebound.** MBA's own forecast has refinances dropping another
   17 percent next year. That demand is not coming back soon.
2. **Plan around purchase volume, not total volume.** The headline number is shrinking because of
   refinances. Purchase volume is projected to grow slightly in the same forecast.
3. **Tell buyers 7 percent is the planning number for 2027, not a peak to wait out.** The same
   forecast has rates staying above 7 percent through next year.
4. **Ask your lender how much of their business is purchase versus refi.** A lender built around
   refinance volume has less reason to fight hard for your buyer's file next year.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Pull up your pipeline right now and count how many deals assume rates drop next year.

**Subhead:**
The group that forecasts mortgages says don't plan on it.

---

## Social Captions

### LinkedIn
The Mortgage Bankers Association's own October 2026 forecast puts total 2027 mortgage volume at
1.99 trillion dollars, down 5 percent from 2026. Rates stay above 7 percent the whole year, by
their own number.

But the drop isn't even. Purchase originations actually rise slightly, to 1.42 trillion.
Refinances fall 17 percent, to 571 billion. The shrinking half of the market is refinance
business, not the purchase business agents actually work.

Build your 2027 plan around purchase volume, not the total number, and stop waiting on a
rate-driven refi rebound that MBA's own forecast says isn't coming.

Learn more at joinkale.com

#RealEstateAgents #MortgageRates #RealtorTips #KeepingItRealPodcast

### Instagram
MBA's own forecast: total mortgage volume shrinks again in 2027, to 1.99 trillion. Rates stay
above 7 percent the whole year.

But purchase loans actually rise slightly. Refinances are the ones collapsing, down 17 percent.
Plan around the business you actually work.

#RealEstateAgents #MortgageRates #RealtorTips

### Facebook
Mortgage volume shrinks again in 2027, but not evenly. Purchase loans rise slightly while
refinances collapse 17 percent. Plan your year around the business you actually work.

#RealtorTips #RealEstateAgents

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-10-12-mortgage-volume-shrinks-again-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Light theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. This is an open deck. No keyword, no ManyChat flow, no ask on any platform.

**LinkedIn first comment:** https://joinkale.com/?src=carousel-kirp-2026-10-12-mortgage-volume-shrinks-again-carousel

**Pinned first comment (IG and FB):** "The split: purchase loans rise slightly to $1.42 trillion
in 2027. Refinances fall 17 percent to $571 billion. Full breakdown in the carousel."

---

## Data Source

- **Claim:** "Total 2027 single-family mortgage origination volume is forecast to fall 5 percent,
  to $1.99 trillion, from a projected $2.1 trillion in 2026."
  - Source: Mortgage Bankers Association 2027 baseline forecast, reported in HousingWire,
    "MBA forecast: Mortgage volume to dip below $2T in 2027 as 7% rates linger," byline Flávia
    Furlan Nunes, published 2026-10-11.
  - Who was measured: MBA's own economic forecast of national single-family mortgage
    origination volume.
  - Status: confirmed, fetched directly from the HousingWire article.
- **Claim:** "Purchase originations are forecast to rise 0.8 percent, to $1.42 trillion. Refinance
  originations are forecast to fall 17 percent, to $571 billion."
  - Source: same MBA 2027 baseline forecast, same HousingWire article.
  - Status: confirmed, same source.
- **Claim:** "30-year fixed mortgage rates stay above 7 percent through 2027."
  - Source: same HousingWire article, citing MBA's rate assumptions (10-year Treasury averaging
    5.1% in Q4 2026 and staying near 5% through 2027).
  - Status: confirmed, same source.
- **Fabrication audit:** no percentage or dollar figure is rounded or combined across sources.
  The purchase-up-while-total-down contrast on Slide 3 states both figures from the same MBA
  forecast rather than implying causation between separate studies.
