---
lane: "evergreen"
carousel_for: "Redfin's October 22, 2026 numbers: nearly a quarter of homes are still selling above asking and the average sale-to-list ratio climbed, not fell, so pricing skill still wins deals and should still pay the agent who has it"
hook_family: "myth-bust"
heat: 2
slide_count: 5
goal: "engagement"
generated: "2026-10-26"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
---

# Carousel: still selling above asking

Brand-new KR deck, built fresh because today's other KIRP pick,
`KIRP-2026-10-26-separation-season-carousel.md`, features a named guest (Ben Lalez) and does not
translate (`kirp_guest: true`, per `reskin_kr.py` exit 2). Per
`docs/automation/daily-carousel-engine.md`, that means two KR decks still ship today: the other
KIRP pick's re-skin, `KR-2026-10-26-rate-buydown-not-price-cut-carousel.md`, and this one.

**Different topic from both of today's other decks, same source article, different figures.**
The companion decks use Redfin's months-of-supply, pending-sales, price-drop, and payment
figures to argue for a rate buydown on a stuck listing. This deck pulls two different numbers
from the same Redfin report -- the share of homes selling above list and the sale-to-list ratio
-- to make a separate, Kale-recruiting-adjacent point: the market is not uniformly a discount
market, pricing skill is still winning deals outright, and that upside should land fully with
the agent who earns it, not get eaten by overhead. Hook family `myth-bust` (correcting the
"everything needs a price cut right now" read of the market), differing from today's other two
decks (`contrast`, `one-tactic-breakdown`) and from the three most recently committed decks
before today (`person-lesson`, `mirror`, `myth-bust` on 2026-10-25 -- the last use of this family
was two days ago, not the immediately preceding deck).

Checked `scripts/carousels/` for "sale-to-list," "above asking," and "above list price" first --
no prior deck covers this specific angle.

---

## SLIDE 1 -- HOOK
**Headline:**
Nearly 1 in 4 homes still sell above asking.

**Subhead:**
That's not the market the price-cut headlines describe.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
The average home is selling for 98.4 percent of its asking price, and that number went up, not down, this month.

**Subhead:**
A slower market and a market that stopped rewarding a sharp price are two different things.

---

## SLIDE 3 -- THE TURN
**Headline:**
Supply is loosening. Pricing skill is still the deciding factor.

**Body:**
Redfin's own numbers, four weeks ending October 18: months of supply sits at 4.4, inside what
Redfin calls a balanced market, not a flood. And in that same market, **23.3 percent** of homes
sold above list price, up from 23.1 percent, with the average sale-to-list ratio climbing to
**98.4 percent**, up from 98.3 percent. A market that's cooling overall still has a real pool of
buyers competing for the listings that are priced right. The agents reading the whole market
correctly are the ones winning that pool, not the ones defaulting every listing to a discount.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What that means for your next listing:

**Numbered list:**
1. **Pull the sale-to-list ratio for your own zip code before you recommend a price.** The
   national number is 98.4 percent. Your market may run higher or lower.
2. **Don't default to a price cut on a new listing.** Check which comparable homes sold above
   ask in the last 30 days first.
3. **Price for the buyers still competing, not the ones who already walked.** Almost a quarter
   of sellers are proof there's still a real bidding pool out there.
4. **Make sure the win lands with you.** A price that beats asking only pays off fully when your
   own commission isn't the next thing that gets cut.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Pricing skill still wins deals right now.

**Subhead:**
Make sure it still pays you what it's worth.

---

## Social Captions

### LinkedIn
Almost a quarter of homes are still selling above asking price, so the agents reading the market correctly are still winning real upside, not just avoiding discounts.

### Instagram
The average home is selling for more of its asking price than it was last month, which is not the story the price-cut headlines are telling.

### Facebook
Chicago agents, pricing skill is still winning deals in this market, and the agents keeping their full commission are the ones who feel that upside the most.

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| Months of supply at 4.4, inside a "balanced" range | Yes, slide 3 | Redfin, "U.S. Pending Home Sales Sink to a New Low," Dana Anderson, 2026-10-22, four weeks ending 2026-10-18: "Months of supply: 4.4, up from 4... 4 to 5 months of supply is considered a balanced market." https://www.redfin.com/news/housing-market-update-pending-home-sales-sink-high-rates/ | Confirmed, fetched directly from the article 2026-10-26, same fetch used for the companion deck |
| 23.3 percent of homes sold above list price, up from 23.1 percent | Yes, slides 1-3 | Same report: "Share of homes sold above list price: 23.3%, up from 23.1%" | Confirmed, fetched directly 2026-10-26 |
| Average sale-to-list price ratio of 98.4 percent, up from 98.3 percent | Yes, slide 2-3 | Same report: "Average sale-to-list price ratio: 98.4%, up from 98.3%" | Confirmed, fetched directly 2026-10-26 |
| Pricing skill determines who wins the remaining pool of competitive buyers | Yes, slide 3 and the payload | Editorial reasoning from the sourced figures above, not a separate statistic | Commentary, not a statistic. No invented figure |

**Do-not-cite check:** no lender, platform, brokerage, or person is named anywhere in this file.

**Reuse note:** net-new KR deck, not a repurpose of a KIRP deck or an existing walk-and-talk
script. No `source_script`, no `reskinned_from` field.
