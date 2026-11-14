---
lane: "market-tip"
carousel_for: "Dana Anderson, Redfin News, 2026-11-12: only 3 of the 50 biggest U.S. metros were seller's markets in October, tied for the fewest since Redfin's records began in 2016, while Chicago sits balanced; the pricing conversation agents need to have with sellers this month"
hook_family: "myth-bust"
heat: 2
slide_count: 5
goal: "engagement"
generated: "2026-11-14"
theme: "light"
---

# Carousel: only 3 markets still favor sellers

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`kirp-guest-tip` (`last_used: 2026-11-06`), built as the companion deck,
`KIRP-2026-11-14-worst-advice-carousel.md`. The second-oldest ties at `last_used: 2026-11-12`
between `market-tip` and `do-this-dont-do-that`; resolved to `market-tip` (first-listed of the
tie in the rotation file's `topics` array, the same tie-break convention earlier files used),
built here. `do-this-dont-do-that` stays at `last_used: 2026-11-12` for the next run.

Source note: today's news brief file (`data/news-briefs/2026-11-14.md`) had not been generated
yet at build time, so this deck was built from yesterday's brief (`data/news-briefs/2026-11-13.md`),
per the sourcing order in `docs/automation/daily-carousel-engine.md` (news brief, then stat bank).
That brief's "Trending" and "Full story list" sections both surface the Redfin
buyer's/seller's-market report; fetched and read
https://www.redfin.com/news/buyers-vs-sellers-october-2026/ directly today to pull the exact
figures and methodology rather than build from the headline alone.

**The one idea:** the national story is "sellers have lost the market" -- only 3 of the 50
biggest metros are still seller's markets, tied for the fewest in Redfin's records. But Chicago
itself isn't one of the 41 buyer's markets either -- it's one of 6 metros sitting balanced. The
local conversation an agent needs to have with a seller this month is narrower and less
alarming than the national headline, and that gap is the actual tip: know your own metro's
number before you have that conversation, not the national one.

Checked `scripts/carousels/*.md` for "seller's market," "buyer's market," and "Redfin" first --
no prior deck used this report or this angle.

Hook family `myth-bust` (busting "it's still a seller's market," and separately the assumption
that the national number applies locally), differing from the most recent committed deck
(`data-card`, `KIRP-2026-11-13-millennial-affordability-gap-carousel.md`) and from today's
companion deck (`named-stakes`).

No `kirp_guest` flag. This deck re-skins to KR normally.

---

## SLIDE 1 -- HOOK
**Headline:**
Only 3 markets still favor sellers.

**Subhead:**
The fewest since Redfin started tracking it, ten years ago.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Redfin just measured 50 of the biggest U.S. housing markets. Only 3 still favor sellers.

**Subhead:**
Nationwide, sellers now outnumber buyers by **70.5%**, the largest gap Redfin has recorded since
it started tracking this in 2013.

---

## SLIDE 3 -- THE TURN

**Headline:**
Chicago isn't actually one of the 41.

**Body:**
41 of the 50 metros Redfin measured are buyer's markets. Chicago isn't one of them -- it's one of
just 6 metros sitting balanced, with sellers outnumbering buyers by 8.1%, inside Redfin's own
plus-or-minus-10% band for balanced. The national headline and the Chicago conversation are two
different numbers. An agent who quotes the national one to a local seller is arguing with the
wrong data.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
What to do with this before your next listing appointment:

**Numbered list:**
1. **Pull your own metro's number, not the national one.** Redfin publishes buyer's/seller's
   status city by city. Know whether your market is balanced, buyer's, or seller's before you
   walk into the appointment.
2. **Use "balanced" as the actual pitch to a Chicago seller.** Balanced means real competition
   for well-priced listings still exists here, even while most of the country has tipped to
   buyers. That's a stronger, more honest case than either extreme.
3. **Tell nervous buyers the plain math.** Nationally, sellers outnumber buyers by 70.5%, the
   biggest gap on record. A buyer who feels like they're losing is working from the wrong year's
   market.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Before your next appointment, look up whether your own metro is balanced, buyer's, or seller's.
Bring that number, not the national headline.

---

## Social Captions

### LinkedIn
Redfin just found only 3 of the 50 biggest U.S. markets still favor sellers, and Chicago isn't a buyer's market either, it's balanced.

### Instagram
Only 3 major U.S. markets still favor sellers, and Chicago agents, that national headline isn't actually your market's number.

### Facebook
Chicago agents, the national housing market just tipped hard toward buyers, but Chicago itself is sitting balanced, here's the number to bring to your next listing appointment.

### TikTok
Only 3 of the 50 biggest housing markets still favor sellers, here's what that actually means for Chicago. #RealEstateAgent #ChicagoRealEstate

### YouTube Shorts
**Title:** Only 3 U.S. markets still favor sellers

Redfin found only 3 of the 50 biggest housing markets still favor sellers, and Chicago sits balanced, not buyer's. #RealEstateAgent #ChicagoRealEstate

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| Only 3 of the 50 most populous U.S. metros were seller's markets in October 2026 (Nassau County NY, Newark NJ, Montgomery County PA), tied for the fewest in Redfin's records dating back to 2016, matching April 2020 | Yes, slides 1, 2 | Dana Anderson, Redfin News, published 2026-11-12, "Just 3 Major U.S. Metros Are Seller's Markets -- the Fewest Since the Pandemic Freeze": "Three of the 50 most populous U.S. metro areas... were seller's markets in October... tied for the fewest in records dating back to 2016, matching April 2020." [Redfin News](https://www.redfin.com/news/buyers-vs-sellers-october-2026/) | Confirmed, named source + date, fetched and read directly today |
| Nationwide, sellers outnumbered buyers by 70.5% in October, the largest gap since Redfin's records began in 2013 | Yes, slide 2 | Same article: "Sellers outnumbered buyers by 70.5%... the largest gap since Redfin began recording this data in 2013." | Confirmed, named source + date |
| 41 of the 50 metros measured are buyer's markets; 6 are balanced, including Chicago at 8.1% (sellers outnumbering buyers by 8.1%, inside Redfin's plus-or-minus-10% balanced band) | Yes, slide 3 | Same article: "41 of the 50 metros are buyer's markets... Six are balanced: Chicago (8.1%)..." Methodology: "A market where the gap is plus or minus 10% is considered a balanced market." | Confirmed, named source + date, methodology quoted directly |

**Not used:** the article's largest-buyer's-market figures (Miami, Nashville, Las Vegas) and the
seller's-market price appreciation figure (3.3% YoY) weren't needed for this deck's one idea and
were left off slide 3 to keep the deck to its single point (the Chicago-vs-national gap), per
the five-slide, one-idea rule.

**Methodology note, spoken on slide 3 only as "balanced... inside Redfin's own plus-or-minus-10%
band":** Redfin defines a buyer's market as sellers outnumbering buyers by more than 10%, a
seller's market as sellers more than 10% fewer than buyers, and balanced as within that 10% band
either way. Buyers are estimated from typical tour-to-close time, MLS pending sales, and active
listings; sellers are active MLS listings. Figures are seasonally adjusted and subject to
revision.
