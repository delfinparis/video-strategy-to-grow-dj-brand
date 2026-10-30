---
lane: "evergreen"
carousel_for: "Realtor.com research (PR Newswire, published 2026-06-11): homes that close around the four-week mark sell 1.8 percentage points above the monthly average for comparable homes, while homes still on market at eighteen weeks close 1.3 points below, and the swap that keeps an inflated listing price from turning into that slide"
hook_family: "swap-list"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-10-30"
reskinned_from: "KIRP-2026-10-30-overpriced-listing-swap-carousel"
heat: "3"
---

# Carousel: the overpriced-listing swap

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`do-this-dont-do-that` (`last_used: 2026-10-27`), built here. The second-oldest ties at
`last_used: 2026-10-28` between `market-tip` and `dont-make-this-mistake`; resolved to
`market-tip` (first-listed of the tie in the rotation file's `topics` array, the same tie-break
convention earlier files used), built as the companion deck,
`KIRP-2026-10-30-senior-housing-wealth-carousel.md`. `dont-make-this-mistake` stays at
`last_used: 2026-10-28` for the next run.

Source per Step 2(b): today's news brief, `data/news-briefs/2026-10-30.md`, "Realtor tips" section,
option 1 (`ST-0001`, "Taking a listing at a price the comps don't support, because another agent
already agreed to it"). Re-verified the receipt at build time per Rule 1: fetched
https://www.prnewswire.com/news-releases/by-week-four-your-listing-is-either-getting-offers-or-price-cuts-302797293.html
directly today. The release gives the two percentages but does not attribute them to a quote from
Joel Berner (Realtor.com's senior economist, the release's only named speaker), so the deck does
not put these specific numbers in his mouth. Checked `scripts/carousels/*.md` for "price cuts,"
"four-week," and "comps" first -- no prior deck covers this release.

**The one idea:** an agent who quotes the highest number to win a listing isn't doing the seller
a favor. Realtor.com's own research shows the penalty for the resulting long sit: homes that
close around the four-week mark outperform the monthly average, and homes still sitting at
eighteen weeks underperform it by more. The swap is pricing to the comps out loud, and writing
a reduction schedule into the listing agreement up front if a seller insists on testing high.

Hook family `swap-list` (the wrong move and the right one, in the agent's own words at the
listing table), differing from the two most recently committed decks before today (`contrast`,
`data-card`, both 2026-10-29) and from today's companion deck (`myth-bust`).

---

## SLIDE 1 -- HOOK
**Headline:**
You didn't win that listing. You bought it.

**Subhead:**
The agent who quoted the highest number isn't doing the seller a favor.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Three agents pitch a seller. The one who quotes highest gets the listing, then the blame.

**Subhead:**
Thirty days later, the price-cut conversation starts.

---

## SLIDE 3 -- THE TURN
**Headline:**
The real cost isn't the number. It's how long it sits.

**Body:**
Realtor.com's own research found that homes closing around the **four-week** mark sell for **1.8
percentage points above** the monthly average for comparable homes. Homes still sitting at
**eighteen weeks** close **1.3 points below** that average, a swing of more than three points
either way. An inflated price doesn't win the seller a better number. It buys a longer sit, and
the longer sit is what drags the final price down.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Say this at the listing appointment instead:

**Numbered list:**
1. **Price to the comps, out loud.** Give the honest number before you ever hear a competing one.
2. **If they want to test high, put it in writing.** A reduction schedule, in the listing
   agreement, on day one.
3. **Name the deadline before you sign.** "If we have no offer by this date, the price drops to
   this number."
4. **Walk from a listing you can't price honestly.** A fast, well-priced listing beats a stale,
   inflated one every time.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
A high number isn't a win. It's a loan against the closing price.

**Subhead:**
Price it honestly, or put the cut in writing before you sign.

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| Homes that close around the four-week mark sell for 1.8 percentage points above the monthly average for comparable homes | Yes, slides 3, 5 | Realtor.com research release, "By Week Four, Your Listing Is Either Getting Offers Or Price Cuts," distributed via PR Newswire, published June 11, 2026: "Homes that close around the four-week mark sell for 1.8 percentage points above the monthly average for comparable homes." https://www.prnewswire.com/news-releases/by-week-four-your-listing-is-either-getting-offers-or-price-cuts-302797293.html | Confirmed. Re-verified today via direct fetch of the release. The release's percentages are not attributed to a quote from Joel Berner (the only named speaker); he is credited elsewhere in the release but not with these two figures, so he is not named alongside the numbers on this deck. |
| Homes still on the market at eighteen weeks close 1.3 percentage points below the monthly average | Yes, slides 3, 5 | Same release: "Homes on the market for 18 weeks close 1.3 percentage points below the monthly average." | Same status as above. |

**Do-not-cite check:** no lender, platform, brokerage, or person other than the named Realtor.com
release is referenced anywhere in this file.

## Social Captions

_Written fresh for the Kale audience per `docs/automation/daily-carousel-engine.md`: an agent
weighing a move, not the podcast audience. One sentence per platform, zero hashtags on
LinkedIn, Instagram and Facebook per `docs/caption-and-hashtag-strategy.md` Rule 0-1
(2026-10-19, the current standard; supersedes the older 3-5 hashtag placeholder this
reskin script still writes). No em dashes, no engagement asks._

### LinkedIn
An agent who still has to inflate a number to win a listing is selling you on their pitch, not the house.

### Instagram
A brokerage that trains you to overprice for the appointment is setting up the price cut you'll have to explain later.

### Facebook
Kale Realty agents keep their full commission instead of handing a cut to a brand that rewards the highest quote, not the honest one.
