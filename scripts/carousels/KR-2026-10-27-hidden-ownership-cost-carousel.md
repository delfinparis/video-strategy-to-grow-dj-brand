---
lane: "evergreen"
carousel_for: "Zillow and Thumbtack's October 2026 hidden-cost report: owning a home runs $16,566 a year on top of the mortgage, and why an agent shows a buyer that number before they write an offer"
hook_family: "data-card"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-10-27"
reskinned_from: "KIRP-2026-10-27-hidden-ownership-cost-carousel"
heat: "2"
---

# Carousel: the hidden ownership cost

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`stat` (`last_used: 2026-10-24`). The second-oldest ties at `last_used: 2026-10-25` between
`do-this-dont-do-that` and `dont-make-this-mistake`; resolved to `do-this-dont-do-that`
(first-listed of the tie in the rotation file), built as the companion deck,
`KIRP-2026-10-27-phone-shot-listing-photos-carousel.md`.

Source per Step 2(b): no news brief exists for 2026-10-25, 2026-10-26, or 2026-10-27; the newest
on disk is `data/news-briefs/2026-10-24.md`, which has no stat-card-shaped number not already
spent (the Redfin pending-sales figures it links went into yesterday's market-tip deck).
`data/news-briefs/stat-bank.json` named in the engine's Step 2(c) still does not exist in this
repo. Went outside the brief to a same-week report: a Zillow and Thumbtack hidden-cost analysis,
published 2026-10-22, fetched directly (see Data Source below) rather than relying on the
brief's unexpanded headline link.

**The one idea:** the mortgage payment is not the whole monthly number, and the gap is now
$16,566 a year, about $1,380 a month, split across maintenance, insurance, and property taxes.
Insurance is the fastest-moving piece, up 54 percent over five years. The agent move: price the
full carrying cost for a buyer before they fall for a listing on the mortgage number alone.

Hook family `data-card` (the whole deck is built around one big number), differing from today's
companion deck (`swap-list`) and from the two most recently committed decks before today
(`mirror`, `myth-bust`, both 2026-10-25).

Checked `scripts/carousels/` for "hidden cost," "16,566," and "Thumbtack" first -- no prior deck
covers this report.

---

## SLIDE 1 -- HOOK
**Headline:**
The mortgage is not the real payment.

**Subhead:**
Owning this house adds $16,566 a year the mortgage never counted.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
$16,566. That's what a house costs every year after the mortgage check clears.

**Subhead:**
Insurance, taxes, and upkeep. Not optional, not occasional.

---

## SLIDE 3 -- THE TURN
**Headline:**
The mortgage is the smallest surprise in the budget.

**Body:**
Zillow and Thumbtack's report, published October 22, 2026: the typical homeowner pays **$16,566**
a year in costs the mortgage payment never includes, about $1,380 a month on top of it.
Maintenance is the biggest piece at **$11,171**, property taxes add **$3,129**, and homeowners
insurance, now **$2,266**, has climbed **54 percent** over the last five years, the
fastest-rising of the three. Zillow senior economist Kara Ng: "Long after they receive the keys,
insurance, taxes and upkeep are recurring expenses to plan for."

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Run this before a buyer writes an offer:

**Numbered list:**
1. **Price the full monthly number, not just the mortgage.** Add roughly $1,380 to the lender's
   estimate before the buyer falls for the payment on the listing sheet.
2. **Pull a current insurance quote, not last year's rate.** Premiums are up 54 percent in five
   years; a stale number undersells the real payment.
3. **Show the actual tax bill, not the MLS field's guess.** A recent reassessment can move that
   number more than the mortgage rate will.
4. **Put a maintenance line in writing.** $11,171 a year is the typical homeowner's biggest
   hidden cost; a buyer who sees it coming doesn't blame their agent later.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
The buyer who sees the whole number trusts the agent who showed it to them.

**Subhead:**
Show the carrying cost before the mortgage company does.

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| Typical homeowner pays $16,566 a year in costs the mortgage doesn't include, about $1,380 a month | Yes, slides 1-3 | Zillow and Thumbtack hidden-cost analysis, published 2026-10-22, reported by Fox Business: "Total annual cost: $16,566, or about $1,380 per month on top of the mortgage payment." https://www.foxbusiness.com/economy/owning-home-comes-hidden-price-tag-its-getting-more-expensive | Confirmed, fetched directly today |
| Maintenance $11,171, property taxes $3,129, homeowners insurance $2,266 | Yes, slide 3 and the payload | Same report, same URL: breakdown figures as reported | Confirmed, fetched directly today |
| Homeowners insurance up 54 percent over the last five years | Yes, slides 3-4 | Same report, same URL: "Insurance premium increase: Up 54% over the last five years, the largest jump among the hidden costs" | Confirmed, fetched directly today |
| Kara Ng, Zillow senior economist, quote | Yes, slide 3 | Same report, same URL: "Long after they receive the keys, insurance, taxes and upkeep are recurring expenses to plan for." Attributed to Kara Ng, Zillow Senior Economist | Confirmed, fetched directly today |

**Do-not-cite check:** no lender, platform, brokerage, or person other than the named Zillow
economist is referenced anywhere in this file.

**Reuse note:** net-new stat carousel, not a repurpose of an existing walk-and-talk script. No
`source_script` field.

## Social Captions

### LinkedIn
An agent who still owes half their commission has less room to spend an afternoon walking a buyer through the $16,566 a lender's quote leaves out.

### Instagram
The agents who make time to run the real monthly number with a buyer are usually the ones who kept their whole commission.

### Facebook
Kale Realty agents keep their full commission, which buys the time it takes to show a buyer the real carrying cost before they write an offer.
