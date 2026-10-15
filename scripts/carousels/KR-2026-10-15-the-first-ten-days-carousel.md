---
lane: "news-repurpose"
carousel_for: "Chase Whitney, The Whitney Team: the first 7-10 days on market largely set the price, a 2-3% swing worth $22,000-$33,000 on a $1.1M home"
hook_family: "mirror"
slide_count: "5"
goal: "engagement"
theme: "light"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-10-15"
reskinned_from: "KIRP-2026-10-15-the-first-ten-days-carousel"
source_script: "scripts/inside-the-industry/NF-090-first-ten-days-set-the-price.md"
heat: "3"
---

# Carousel: the first ten days

Today's two rotation slots, per `data/carousel-topic-rotation.json`: `kirp-guest-tip`
(`last_used: 2026-10-12`) is the unambiguous oldest, built as the companion deck
(`KIRP-2026-10-15-stop-automating-the-follow-up-carousel.md`). `market-tip` and
`do-this-dont-do-that` are tied next at `2026-10-13`; `market-tip` wins the tie because it is
listed first in the rotation file's `topics` array, the same array-order tiebreak used in
`KIRP-2026-10-14-stop-buying-leads-carousel.md`'s production note. `do-this-dont-do-that` and
`stat` (`last_used: 2026-10-14`) and `dont-make-this-mistake` (`last_used: 2026-10-14`) stay
banked for later in the week. This deck is the `market-tip` slot.

Sourced per Step 2(d): walk-and-talk script
`scripts/inside-the-industry/NF-090-first-ten-days-set-the-price.md`, committed in the most
recent pull (the "Add NF-089 to NF-103" / Zillow Unlock speaker-tips batch, 2026-10-13). Checked
`scripts/carousels/` for "NF-090," "first ten days," and "33,000" first -- zero prior hits, so
this angle hasn't been carouselized yet.

**Re-verified directly against the source, not just against NF-090's own Data Source block**
(Rule 1 and the carousel standard's reuse rule): fetched The Whitney Team's show notes page
directly (`thewhitneyteam.podbean.com/e/the-33000-mistake-cypress-sellers-make-before-they-list/`),
2026-10-15. Confirmed the page still reads, unchanged since NF-090 was built two days ago: "the
first 7-10 days on market largely set the price," "a 2-3% sales-price swing is realistic,"
"translating to $22,000-$33,000 on a $1.1M home." Speaker is Chase Whitney of The Whitney Team
at First Team Real Estate; episode published 2026-04-28.

**The one idea:** a listing's first 7-10 days online decide most of its eventual sale price, so
a seller who goes live before the photos and description are finished is leaving money on the
table before a single buyer walks through the door. Rule 0 criterion 4 (a sourced, surprising
statistic -- the dollar swing on a specific home price) and criterion 1 (an exact action: hold
the listing one more day if the photos aren't finished). Hook family `mirror` (the self-
recognition of having gone live before the listing was ready), differing from today's companion
deck (`swap-list`) and from the two most recently committed carousels (`sacred-cow`,
`named-stakes`, both 2026-10-14).

Not a `kirp_guest` deck. Chase Whitney is not a Keeping It Real podcast guest; he is a Zillow
Unlock 2026 conference speaker quoted from his own show's published notes, the same class of
source NF-090 itself uses. This deck translates to Kale Realty via `reskin_kr.py` without
exception.

---

## SLIDE 1 -- HOOK
**Headline:**
You listed before the photos were ready.

**Subhead:**
That decision alone can cost your seller real money.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
The first ten days a listing is live largely decide its final sale price.

**Subhead:**
Not the open house. Not the second price cut. The first ten days.

---

## SLIDE 3 -- THE TURN
**Headline:**
A weak online launch costs tours before it costs dollars.

**Body:**
Chase Whitney of The Whitney Team in Orange County says the first 7 to 10 days on market
largely set the price, because a weak online presentation reduces tours, offers, and leverage
before most buyers ever book a showing. By the time an agent "fixes" the photos on day twelve,
the buyers who would have toured in week one have already moved on to the next listing.

---

## SLIDE 4 -- PAYLOAD
**What you do differently this month:**
1. **Finish the photos before you go live.** A thin or rushed photo set is the first showing
   most buyers get, and most never book a second one.
2. **Write the full description before the listing is public.** An unfinished write-up reads as
   unfinished work to a buyer scrolling fast.
3. **Know the real cost of skipping this.** Whitney puts the swing at two to three percent. On a
   $1.1 million home, that is twenty-two to thirty-three thousand dollars.
4. **Treat day one as the best version of the listing**, not a placeholder you plan to fix
   later.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Hold the listing one more day if the photos aren't finished.

**Subhead:**
The first ten days don't get a second try.

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-10-15-the-first-ten-days-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Light theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. This is an open news-repurpose deck. No keyword, no ManyChat flow, no ask on
any platform.

**LinkedIn first comment:** https://joinkale.com/?src=carousel-kirp-2026-10-15-the-first-ten-days-carousel

**Pinned first comment (IG and FB):** "The source: Chase Whitney, The Whitney Team, 'The
$33,000 Mistake Cypress Sellers Make Before They List,' The 5 Minute Real Estate Fix, April 28,
2026."

---

## Data Source

- **Claim:** "Chase Whitney of The Whitney Team in Orange County says the first 7 to 10 days on
  market largely set the price" / "The first ten days a listing is live largely decide its
  final sale price."
  - Source: The Whitney Team, "The $33,000 Mistake Cypress Sellers Make Before They List," The 5
    Minute Real Estate Fix show notes, 2026-04-28:
    https://thewhitneyteam.podbean.com/e/the-33000-mistake-cypress-sellers-make-before-they-list/ .
    Exact wording: "the first 7-10 days on market largely set the price." Re-fetched directly in
    this session (2026-10-15), confirmed unchanged from NF-090's original 2026-10-13 fetch.
  - Who: Chase Whitney's own claim about Cypress / Orange County listings.
  - Status: confirmed. "First ten days" is the top of his 7-10 day range, inherited from NF-090.
- **Claim:** "A weak online presentation reduces tours, offers, and leverage."
  - Source: Same show notes. Exact wording: "weak online presentation reduces tours, offers, and
    leverage."
  - Status: confirmed.
- **Claim:** "He puts the swing at 2 to 3 percent. On a $1.1 million home, that's $22,000 to
  $33,000."
  - Source: Same show notes. Exact wording: "a 2-3% sales-price swing is realistic, translating
    to $22,000-$33,000 on a $1.1M home." Southern California market estimate, his own, not a
    national figure.
  - Status: confirmed. The payload slide's "twenty-two to thirty-three thousand dollars" states
    the full range; the data card on slide 2/5 does not round it to a single number.
- **Claim:** "By the time an agent fixes the photos on day twelve, the buyers who would have
  toured in week one have already moved on."
  - Source: Editorial framing built on Whitney's point that the first window sets tour volume,
    not a separately sourced figure.
  - Status: commentary.
- **Fabrication audit:** no figure beyond Whitney's own stated 7-10 day window and 2-3% / $22K-
  $33K range appears on this deck. No national average, no second source blended into the same
  sentence. Matches NF-090's own fabrication audit, re-confirmed against the live source page.

## Social Captions

### LinkedIn
A listing's first ten days online can decide its final sale price, before a single open house.

Chase Whitney of The Whitney Team in Orange County says the first 7 to 10 days on market
largely set the price. A weak launch, thin photos, an unfinished description, costs tours and
leverage right when it matters most. He puts the swing at 2 to 3 percent, up to $33,000 on a
$1.1 million home.

Most agents know to finish the photos first. Fewer get the time and support to make every
listing launch-ready on day one. Kale Realty runs flat fee, so more of what you close stays in
your pocket instead of going to overhead that doesn't help you launch a listing right.

Learn more at joinkale.com

#RealEstateAgents #ListingAgents #RealEstateMarketing #KaleRealty

### Instagram
The first ten days a listing is live can decide its final sale price.

A weak launch costs tours and leverage before a single buyer walks through the door. Finish the
photos and the description before you go live.

Kale Realty runs flat fee, so more of what you close stays with you.

#RealEstateAgents #ListingAgents #KaleRealty

### Facebook
Selling your home? The first 7 to 10 days online matter more than most sellers realize. Finish
the photos and the full description before the listing goes live.

#RealEstateAgents #KaleRealty
