---
lane: "news-repurpose"
carousel_for: "Zillow's 2026 listing-words study: fixer-upper listings sold for 14% less than expected, turnkey and remodeled sold for more"
hook_family: "swap-list"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-10-16"
reskinned_from: "KIRP-2026-10-16-never-write-fixer-upper-carousel"
source_script: "scripts/inside-the-industry/NF-079-never-write-fixer-upper.md"
heat: "4"
---

# Carousel: never write fixer-upper

Today's two rotation slots, per `data/carousel-topic-rotation.json`: `do-this-dont-do-that`
(`last_used: 2026-10-13`) is the unambiguous oldest. `stat` and `dont-make-this-mistake` are
tied next at `2026-10-14`; `stat` wins the tie because it is listed before
`dont-make-this-mistake` in the `topics` array, the same array-order tiebreak used in
`KIRP-2026-10-13-dont-trash-the-other-agent-carousel.md`'s production note. `market-tip` and
`kirp-guest-tip` (both `last_used: 2026-10-15`) stay banked for later in the week. This deck is
the `do-this-dont-do-that` slot; the companion `stat` deck is
`KIRP-2026-10-16-half-of-buyers-never-call-back-carousel.md`.

Sourced per Step 2(d): walk-and-talk script
`scripts/inside-the-industry/NF-079-never-write-fixer-upper.md`, part of the 2026-10-13 Zillow
data batch and not yet carouselized (checked every `NF-0` number referenced across
`scripts/carousels/` -- zero prior hits for NF-079). It is a clean do-this-don't-do-that: the
word agents reach for on a dated listing versus the words that actually sell.

**Re-verified directly against the source**, not just against NF-079's own Data Source block
(carousel standard's reuse rule): fetched Zillow's press release directly
(`zillow.mediaroom.com/2026-03-24-Cottagecore,-customization-quartzite-Zillows-2026-home-features-that-sell-for-more`),
2026-10-16. Confirmed unchanged: analysis of 2M+ listings sold in 2025 across 600+ phrases,
"fixer-uppers sell for 14% less" (relative to expected price), "turnkey" homes sold for 2.9%
more, "remodeled" homes sold for 2.2% more.

**The one idea:** the word "fixer-upper" is not a neutral description, it is an instruction to
every buyer scrolling the listing to show up with a lowball before they have seen a single room.
Rule 0 criterion 4 (a sourced, surprising statistic across 2M+ listings) and the Actual Tip gate
(the exact words to cut and the exact words to use instead). Hook family `swap-list` (don't
write X, write Y), differing from the companion `stat` deck (`named-stakes`) and from the most
recently committed carousel (`mirror`, `KIRP-2026-10-15-the-first-ten-days-carousel.md`).

Not a `kirp_guest` deck. Zillow is the data source, quoted from its own published press release,
not a Keeping It Real podcast guest. This deck translates to Kale Realty via `reskin_kr.py`
without exception.

---

## SLIDE 1 -- HOOK
**Headline:**
Never write "fixer-upper" in a listing.

**Subhead:**
That word is quietly costing your seller money.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
"Fixer-upper" tells every buyer to lowball you before they see the kitchen.

**Subhead:**
Zillow studied more than two million listings. The word has a price.

---

## SLIDE 3 -- THE TURN
**Headline:**
Fixer-upper homes sold for 14% less than expected.

**Body:**
Zillow analyzed over 2 million listings sold in 2025 across 600-plus phrases. Homes labeled
"fixer-upper" sold for 14% less than expected. "Turnkey" was tied to 2.9% more, and
"remodeled" to 2.2% more. Part of that gap is the house itself. But the label also arrives
before a buyer has toured a single room, and it tells them exactly how to open the
negotiation.

---

## SLIDE 4 -- PAYLOAD
**The swap, word for word:**
1. **Don't write "fixer-upper."** It reads as permission to lowball before a showing.
2. **Do write what it actually needs.** "Original windows." "Dated kitchen." "Needs a new
   roof." Specific, not a label.
3. **Don't write "handyman special" or "as-is" as the headline.** Same lowball signal, different
   words.
4. **Do let buyers price the work themselves.** They will do the math either way. Give them
   the facts, not a word that does it for them at your seller's expense.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Check every active listing you have. Find the word "fixer-upper." Take it out.

**Subhead:**
Say what the house needs. Let buyers price the work, not the label.

---

## Data Source

- **Claim:** "Fixer-upper homes sold for 14% less than expected."
  - Source: Zillow, "Cottagecore, customization & quartzite: Zillow's 2026 home features that
    sell for more," press release, 2026-03-24:
    https://zillow.mediaroom.com/2026-03-24-Cottagecore,-customization-quartzite-Zillows-2026-home-features-that-sell-for-more .
    Exact text: "fixer-uppers sell for 14% less." Premiums measured as sale price relative to
    expected price. Re-fetched directly in this session (2026-10-16), confirmed unchanged from
    NF-079's original 2026-10-13 fetch.
  - Status: confirmed (correlation, not causation -- homes called fixer-uppers often do need
    work; the label is a contributing factor, not the sole cause).
- **Claim:** "Zillow analyzed over 2 million listings sold in 2025 across 600-plus phrases."
  - Source: Same release.
  - Status: confirmed.
- **Claim:** "Turnkey was tied to 2.9% more, and remodeled to 2.2% more."
  - Source: Same release: turnkey +2.9%, remodeled +2.2%.
  - Status: confirmed.
- **Claim:** "The label tells buyers exactly how to open the negotiation."
  - Source: Editorial framing built on the measured sale-price gap, not a separately sourced
    figure.
  - Status: commentary.
- **Fabrication audit:** no figure beyond Zillow's own published 14% / 2.9% / 2.2% percentages
  appears on this deck. No second source blended into the same sentence. Matches NF-079's own
  fabrication audit, re-confirmed against the live source page.

## Social Captions

### LinkedIn
If your listing copy still says "fixer-upper," you're costing your seller money and you
probably don't know it.

Zillow's 2026 study of more than two million 2025 listings found homes labeled fixer-upper
sold for 14% less than expected. "Turnkey" and "remodeled" sold for more. The label reaches
every buyer before they've toured a room, and it tells them exactly how low to open.

Agents who get real training on how to price, position, and write a listing don't lose that
14% by accident. It's one small habit among many that separates a flat-fee model that
actually teaches you from one that just takes your split and leaves you guessing.

Learn more at joinkale.com.

#RealEstateAgents #ListingAgents #RealEstateMarketing #ChicagoRealtors

### Instagram
Still writing "fixer-upper" in your listings? Zillow's latest study says that word alone is
tied to homes selling for 14% less than expected.

Small habits like this are the difference between agents who are taught and agents who are
left to guess. Kale Realty agents get both the split and the training.

#RealEstateAgents #ListingAgents #ChicagoRealtors

### Facebook
Agents, the words in your listing matter more than you think. Zillow's newest study found
"fixer-upper" listings sold for 14% less than expected. Kale Realty trains agents on the
details that actually move a sale price. Learn more at joinkale.com.

#RealEstateAgents #ChicagoRealEstate
