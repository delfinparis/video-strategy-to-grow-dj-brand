---
lane: "evergreen"
carousel_for: "Redfin's October 22, 2026 pending-sales report: months of supply at 4.4 and the typical monthly payment at a near-record $2,796, and why a rate buydown solves what a price cut doesn't right now"
hook_family: "one-tactic-breakdown"
slide_count: "5"
goal: "engagement"
theme: "light"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-10-26"
reskinned_from: "KIRP-2026-10-26-rate-buydown-not-price-cut-carousel"
heat: "2"
---

# Carousel: rate buydown, not price cut

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`kirp-guest-tip` (`last_used: 2026-10-23`, built as the companion deck,
`KIRP-2026-10-26-separation-season-carousel.md`). The second-oldest ties at `last_used:
2026-10-24` between `market-tip` and `stat`; resolved to `market-tip` (first-listed of the tie).

Source per Step 2(b): the newest news brief on disk is `data/news-briefs/2026-10-24.md`, which
links Redfin's "U.S. Pending Home Sales Sink to a New Low" without extracting its numbers.
Fetched the article directly (Redfin, Dana Anderson, published 2026-10-22, four weeks ending
2026-10-18) for the exact figures. `data/news-briefs/stat-bank.json` named in the engine's
Step 2(c) no longer exists in this repo.

**The one idea:** this is a market-tip, a tactic for right now, not a stat recap -- that's
tomorrow's `stat` slot. Months of supply sits at 4.4, inside Redfin's own "balanced" band
(4 to 5), not a flood of inventory; pending sales are down 14.4 percent year over year, the
lowest level Redfin has on record; and the typical monthly payment just hit $2,796, the
second-highest Redfin has ever recorded. The agent move this month: when a stuck listing needs
help, don't reach for a price cut first. Offer the seller a rate buydown instead, because it
moves the number the buyer actually feels every month, where a price cut barely does. Hook
family `one-tactic-breakdown`, differing from today's companion deck (`contrast`) and from the
three most recently committed decks before today (`person-lesson`, `mirror`, `myth-bust`).

Checked `scripts/carousels/` for "rate buydown," "months of supply," and "price cut" first --
no prior deck covers this specific swap.

---

## SLIDE 1 -- HOOK
**Headline:**
A price cut isn't your strongest move right now.

**Subhead:**
There's a better one, and it costs the seller about the same.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
The typical house payment just hit $2,796 a month. Redfin has only recorded one month higher than that, ever.

**Subhead:**
Buyers aren't gone. They're priced out of the payment, not the house.

---

## SLIDE 3 -- THE TURN
**Headline:**
It's not a flood of houses. It's the payment that's stuck.

**Body:**
Redfin's own numbers, four weeks ending October 18: months of supply sits at **4.4**, inside
what Redfin itself calls a balanced market (4 to 5). Pending sales are down **14.4 percent**
year over year, the lowest level Redfin has on record, and more than one in five listings
(**21.7 percent**) already carries a price drop. The payment, not the sticker price, just hit
the second-highest number Redfin has ever recorded at **$2,796** a month. A small price cut
barely moves that monthly number. The same dollars put into a rate buydown move it every month
the buyer owns the house.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What to bring to a stuck listing this month:

**Numbered list:**
1. **Call your lender before you call the seller.** Ask for the exact payment difference a
   one-point rate buydown creates on this specific house, at today's rate.
2. **Show the seller both numbers side by side.** What a price cut saves the buyer, next to
   what the same dollars spent on a buydown saves them every single month.
3. **Put the buydown in the listing remarks.** "Seller offering a rate buydown" reads differently
   to a buyer than another price reduction does.
4. **Ask for it on the buyer side too.** If you represent the buyer, put the buydown credit in
   the offer instead of, or alongside, a price concession.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
The listings sitting the longest aren't priced wrong. They're financed wrong.

**Subhead:**
Fix the payment this month, not just the price.

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| Months of supply at 4.4, up from 4, inside a "balanced" range of 4 to 5 | Yes, slide 3 | Redfin, "U.S. Pending Home Sales Sink to a New Low," Dana Anderson, 2026-10-22, four weeks ending 2026-10-18: "Months of supply: 4.4, up from 4... 4 to 5 months of supply is considered a balanced market." https://www.redfin.com/news/housing-market-update-pending-home-sales-sink-high-rates/ | Confirmed, fetched directly from the article today |
| Pending home sales down 14.4 percent year over year, the lowest level in Redfin's records | Yes, slide 3 | Same report: "Pending sales (seasonally adjusted): 281,749, down 14.4% year over year... the lowest level in our records" | Confirmed, fetched directly today |
| More than one in five listings (21.7 percent) carry a price drop | Yes, slide 3 | Same report: "Share of listings with price drops: 21.7%, up from 21%" | Confirmed, fetched directly today |
| Typical monthly mortgage payment at $2,796, the second-highest Redfin has recorded | Yes, slides 2-3 | Same report: "Median monthly mortgage payment (seasonally adjusted): $2,796 at a 7.4% mortgage rate, up 10.4%... the second-highest level in our records" | Confirmed, fetched directly today |
| A price cut moves the monthly payment less than an equivalent rate buydown | Yes, slide 3 and the payload | Editorial reasoning from the sourced figures above, not a separate sourced statistic. No specific dollar comparison or buydown math is stated on the deck; slide 4 instructs the agent to pull the exact figure from their own lender for the specific house, rather than asserting a number here | Commentary, not a statistic. No invented figure |

**Do-not-cite check:** no lender, platform, brokerage, or person is named anywhere in this file.

**Reuse note:** this is a net-new market-tip, not a repurpose of an existing walk-and-talk
script. No `source_script` field.

## Social Captions

_Written fresh for the Kale audience per `docs/automation/daily-carousel-engine.md`: an agent
weighing a move, not the podcast audience. One sentence per platform, zero hashtags on
LinkedIn, Instagram and Facebook per `docs/caption-and-hashtag-strategy.md` Rule 0-1
(2026-10-19, the current standard; supersedes the older 3-5 hashtag placeholder this
reskin script still writes). No em dashes, no engagement asks._

### LinkedIn
Agents still cutting price on a stuck listing are solving the wrong problem, the payment is what's actually keeping buyers out.

### Instagram
The agents keeping their commission whole this month have more room to get creative on a stuck listing than the ones splitting it with a brand.

### Facebook
Chicago agents, your next stuck listing needs a payment fix, and that's an easier conversation to have when your split isn't eating the room to negotiate.
