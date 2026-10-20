---
lane: "stat"
source_script: "data/news-briefs/2026-10-20.md"
carousel_for: "NAHB's October 2026 builder confidence index fell to 29, the lowest since June 2012, while the buyer-traffic sub-index hit a 2012 low and builders are discounting broadly"
hook_family: "data-card"
heat: 2
slide_count: 5
goal: "engagement"
generated: "2026-10-20"
theme: "dark"
---

# Carousel: builder confidence hits a 2012 low

`dont-make-this-mistake` is today's unambiguous oldest rotation slot (`last_used: 2026-10-17`
in `data/carousel-topic-rotation.json`). `stat` and `kirp-guest-tip` tie next at
`last_used: 2026-10-18`; `stat` wins on array order (listed before `kirp-guest-tip` in the
`topics` array), the same tiebreak this engine's prior builds use (e.g.
`KIRP-2026-10-12-mortgage-volume-shrinks-again-carousel.md`). `kirp-guest-tip` stays banked for
tomorrow. Today's two slots are `stat` (this deck) and `dont-make-this-mistake` (the companion
deck, `KIRP-2026-10-20-missing-floor-plan-carousel.md`).

Sourced per Step 2(b): today's news brief (`data/news-briefs/2026-10-20.md`) lists "Builder
confidence plunges as rate shock, costs squeeze margins" (HousingWire) and "NAHB Reports Lowest
Builder Confidence in 14 Years" (RISMedia) in its full story list. Today's own "stat tip" box
(affordability at 27%, NAR 2026 Member Profile) already ran as
`KIRP-2026-10-03-affordability-not-rates-carousel.md` and several earlier decks
(`KIRP-2026-08-26-affordability-constraint-carousel.md`,
`KIRP-2026-08-29-affordability-is-the-real-objection-carousel.md`,
`KIRP-2026-09-11-affordability-not-inventory-carousel.md`), so it is not a fresh angle. The stat
bank (`data/news-briefs/stat-bank.json`) is gitignored generated state and not present on this
machine this session. Fetched the HousingWire article directly
(`https://www.housingwire.com/articles/nahb-builder-confidence-14-year-low-october/`, published
2026-10-19, 5:09pm) rather than relying on the brief's headline alone. Checked
`scripts/carousels/` for "builder confidence," "NAHB," and "14-year" first -- no prior deck
covers this.

**The one idea:** the NAHB/Wells Fargo Housing Market Index fell to 29 in October, the lowest
reading since June 2012, and the sub-score that measures prospective buyer traffic fell even
further, to its lowest level since April 2012 outside the pandemic's opening weeks. Builders are
responding by discounting broadly (43% cut price this month, 65% added an incentive), which
reframes "new construction" as a negotiable option agents can put in front of a buyer and a
comparison point for a seller who thinks they have no competition. Rule 0 criterion 4 (a sourced
number agents haven't seen framed this way). Hook family `data-card` (the number is the whole
slide), differing from today's companion `dont-make-this-mistake` deck (`mirror`) and from the
two most recently committed carousels (`pattern-reveal` and `swap-list`, both
`*-2026-10-19-*-carousel.md`).

---

## SLIDE 1 -- HOOK
**Headline:**
**29.** The lowest since 2012.

**Subhead:**
Builder confidence just hit a level it hasn't seen in fourteen years.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Builders are cutting prices and buyers still aren't showing up.

**Subhead:**
Builder confidence just fell to its lowest point since 2012.

---

## SLIDE 3 -- THE TURN
**Headline:**
The sub-score that's worse than the headline number.

**Body:**
The NAHB's builder confidence index fell to 29 in October, the lowest reading since June 2012.
The piece of that score that tracks buyer traffic fell even further, to its lowest level since
April 2012, outside the first weeks of the pandemic. Builders are responding by discounting.
Forty-three percent cut their price this month, by six percent on average, and sixty-five percent
added an incentive on top.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What this means for your next buyer or seller conversation:

**Numbered list:**
1. **Tell buyers new construction is negotiable too.** Forty-three percent of builders cut their
   price this month, by six percent on average, and most added an incentive on top.
2. **Use the traffic number with a seller who won't move.** The buyer-traffic score builders
   report fell to its lowest level since 2012, outside the pandemic's first weeks. Fewer people
   are walking through anyone's door right now, not just theirs.
3. **Chicago gets a different story than the coasts.** The Midwest posted the highest score of
   any region this month, 40, and permits there rose 2.9 percent. The article calls it the one
   bright spot nationally.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Pull up your next new-construction comparison and lead with the discount.

**Subhead:**
Builders are negotiating right now. Act like it.

---

## Social Captions

### LinkedIn
Builder confidence just hit its lowest point since 2012, and new construction is quietly getting as negotiable as resale.

### Instagram
Builder confidence just fell to its lowest level since 2012, and builders are already discounting new construction to compensate.

### TikTok
Builder confidence just hit its lowest point since 2012, and builders are already cutting prices to compensate. #RealEstateAgent #HousingMarket

### YouTube Shorts

**Title:** Builder Confidence Just Hit a 2012 Low

**Description:** Builder confidence just fell to its lowest point since 2012, and builders are already cutting prices to compensate. #RealEstateAgent #HousingMarket

### Facebook
Builder confidence just hit its lowest point since 2012, and new construction is already getting discounted because of it.

---

## Data Source

- **Claim:** "The NAHB/Wells Fargo Housing Market Index fell three points to 29 in October 2026,
  the lowest reading since June 2012."
  - Source: HousingWire, "Builder confidence plunges as rate shock, costs squeeze margins,"
    published 2026-10-19, 5:09pm --
    https://www.housingwire.com/articles/nahb-builder-confidence-14-year-low-october/
  - Who was measured: NAHB/Wells Fargo survey of single-family homebuilders.
  - Status: confirmed, fetched directly.
- **Claim:** "The prospective-buyer-traffic sub-index fell to 18, its lowest level since April
  2012, outside the opening weeks of the pandemic."
  - Source: same HousingWire article, citing NAHB Chief Economist Robert Dietz.
  - Status: confirmed, fetched directly.
- **Claim:** "Forty-three percent of builders cut their price this month, by an average of six
  percent, and sixty-five percent used a sales incentive."
  - Source: same HousingWire article.
  - Status: confirmed, fetched directly.
- **Claim:** "The Midwest posted the highest regional score, 40 (three-month moving average),
  with permits up 2.9 percent, the only region where permits grew; the article frames it as the
  one relative bright spot."
  - Source: same HousingWire article.
  - Status: confirmed, fetched directly.
- **Fabrication audit:** every number on the deck traces to the same single HousingWire article,
  fetched directly on build day. No figures combined across separate studies, no rounding beyond
  the source's own reporting.
