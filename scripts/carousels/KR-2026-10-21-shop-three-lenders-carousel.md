---
lane: "evergreen"
carousel_for: "Realtor.com's October 2026 mortgage-rate report found a very competitive lender is worth about $5,800 more buying power than a typical one, so a buyer needs more than one quote to find out which kind they're talking to"
hook_family: "swap-list"
slide_count: "5"
goal: "engagement"
theme: "light"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-10-21"
reskinned_from: "KIRP-2026-10-21-shop-three-lenders-carousel"
source_script: "scripts/stupid-things/STUPID-031-sending-your-buyer-to-one-lender.md"
heat: "2"
---

# Carousel: get three Loan Estimates, not one

`market-tip` is today's second slot. `market-tip` and `do-this-dont-do-that` tie at
`last_used: 2026-10-19`; `market-tip` wins on array order (listed before `do-this-dont-do-that`
in `data/carousel-topic-rotation.json`'s `topics` array, the same tiebreak this engine's prior
builds use, e.g. `KIRP-2026-10-20-builder-confidence-2012-low-carousel.md`). `kirp-guest-tip`
is today's companion deck (`KIRP-2026-10-21-one-answer-not-the-answer-carousel.md`).

Sourced per Step 2(d): `scripts/stupid-things/STUPID-031-sending-your-buyer-to-one-lender.md`, a
walk-and-talk script committed 2026-10-14 (part of the research batch STUPID-031 to 040), still
`status: draft` and unfilmed. Checked `scripts/carousels/` first: no prior deck covers "one
lender," "Loan Estimate," or STUPID-031 (an earlier grep hit on the phrase "one lender" matched
two unrelated FHA/senior-housing decks on the word "lender" alone, not this script). The script's
own stat was re-opened and confirmed 2026-10-14; the source URL is on a domain (mediaroom.realtor.
com) this session's web fetch tool cannot reach today to re-confirm directly, so this deck reuses
the already-confirmed citation from STUPID-031.md's Data Source rather than re-fetching, flagged
below.

**The one idea:** a buyer who gets only one lender quote has nothing to compare it against.
Realtor.com's October 2026 mortgage-rate report found the gap between a typical retail lender and
a very competitive one was about 19 basis points, worth roughly $5,800 in buying power on a
$2,000 monthly principal-and-interest budget. The fix: every buyer gets three written Loan
Estimates in the same week before picking a lender. Rule 0 criterion 1 (tactical specificity --
the exact document to request and how many) plus criterion 4 (a sourced, surprising number: a
lender choice is worth almost six grand in house). Hook family `swap-list` (the deck hands over
the exact words and the exact document to ask for), differing from the two most recently
committed carousels (`data-card`, `mirror`) and from today's companion `kirp-guest-tip` deck
(`named-stakes`).

---

## SLIDE 1 -- HOOK
**Headline:**
One lender quote is just a **guess.**

**Subhead:**
A better lender can be worth $5,800 more house.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Your buyer's "trusted lender" might be the expensive one. They'll never know with one quote.

**Subhead:**
Realtor.com found the gap between lenders can run $5,800 in buying power.

---

## SLIDE 3 -- THE TURN
**Headline:**
The rate isn't the whole story. The total cost is.

**Body:**
Realtor.com's October 2026 mortgage-rate report, built on Freddie Mac's loan-level data covering
more than 1.3 million purchase loans from 2023 to 2025, found the difference between a typical
retail lender and a very competitive one was about 19 basis points. On a $2,000 monthly
principal-and-interest budget, that gap is worth roughly $5,800 in buying power. A single quote
gives a buyer no way to tell which kind of lender they're looking at.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What to tell every buyer before they pick a lender:

**Numbered list:**
1. **Get a Loan Estimate from three different lenders, the same week.** This is the lender's
   official federal cost sheet, not a verbal quote.
2. **Lay the three side by side.** Compare the rate and the total cost, not just the rate on top.
3. **Don't drop a trusted lender. Make them compete.** The point is comparison, not loyalty. A
   trusted lender who's also competitive will show it on paper.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Three Loan Estimates, one week, before anyone signs anything.

**Subhead:**
Make your buyer compare lenders before they pick one.

---

## Data Source

- **Claim:** "Realtor.com's October 2026 mortgage-rate report found the difference between a
  typical retail lender and a very competitive one was about 19 basis points, worth roughly
  $5,800 in buying power on a $2,000 monthly principal-and-interest budget."
  - Source: Realtor.com, "Homebuyers Can Beat the Headline Mortgage Rate by Shopping, Saving and
    Strengthening Credit," press release, published 2026-10-01:
    https://mediaroom.realtor.com/2026-10-01-Homebuyers-Can-Beat-the-Headline-Mortgage-Rate-by-Shopping,-Saving-and-Strengthening-Credit
  - Who was measured: mortgages, not opinions. Freddie Mac's Single-Family Loan-Level Dataset,
    1,351,302 purchase loans originated January 2023 to December 2025, per the release's own
    methodology.
  - Status: confirmed by this repo on 2026-10-14 (re-opened and re-verified that day for
    STUPID-031; see `scripts/stupid-things/STUPID-031-sending-your-buyer-to-one-lender.md`'s own
    Data Source section for the full citation trail, including the named economist quote). Not
    independently re-fetched for this carousel: mediaroom.realtor.com returned "unable to fetch"
    from this session's web tool today. The underlying figure is seven days old as of this build
    and was confirmed directly at that time, so it is treated as current rather than re-pulled
    sight-unseen; a fresh re-check is due before this figure is reused again after today.
  - Not spoken on the slides but corroborating: Jake Krimmel, senior economist at Realtor.com,
    quoted in the same release: "Buyers should seek multiple loan estimates, compare the full
    terms, not just the advertised rate."
- **Fabrication audit:** one statistic on the deck, traced to a single named report and dataset,
  no figures combined across separate studies, no rounding beyond the source's own reporting.
  "Three" lenders and "the same week" are the tip's own instruction, not a number from the
  source.

## Social Captions

### LinkedIn
A $5,800 difference between lenders is a conversation worth having with every buyer before anyone signs anything, and a flat fee split means you keep the commission either way.

### Instagram
One lender quote is a guess, and the agent who makes buyers compare three is the one who gets the referral when it's worth $5,800.

### Facebook
Three Loan Estimates in one week can be worth $5,800 in buying power for your buyer, and a flat fee split means that work pays you in full too.
