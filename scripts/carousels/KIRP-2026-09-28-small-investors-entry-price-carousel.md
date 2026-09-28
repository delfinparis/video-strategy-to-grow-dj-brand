---
lane: "evergreen"
carousel_for: "Realtor.com's 2025 investor purchase report, released 2026-06-23: small investors (fewer than 10 purchases a year) made 63% of all investor home purchases in 2025, the highest share in 15+ years, buying at a $330,000 median price while mega investors (350+ purchases a year) fell to 7.5% of purchases, down 70% from their pandemic peak"
hook_family: "named-stakes"
heat: 3
slide_count: 5
goal: "engagement"
generated: "2026-09-28"
theme: "dark"
---

# Carousel: 63 percent. Highest in 15 years.

Today's rotation: two topic types tied oldest per `data/carousel-topic-rotation.json`. `stat`
was the true oldest at `last_used: 2026-09-25`. This deck is `stat`; the companion deck
(`do-this-dont-do-that`) is `KIRP-2026-09-28-dont-talk-them-out-of-their-own-agent-carousel.md`,
tied for next-oldest at `2026-09-26` with `dont-make-this-mistake` and taken by list order, the
same tie-break convention prior runs used.

Source order followed: 2(a) not applicable, not a `kirp-guest-tip` deck. 2(b) today's news
brief (`data/news-briefs/2026-09-28.md`) carried a "Today's stat tip" pointing at Realtor.com's
investor-purchase research via HousingWire but only as a one-line summary ("investor activity
remained stable"). Fetched the underlying Realtor.com report directly for the actual figures
rather than building off the paraphrase, since HousingWire's write-up did not itself carry the
investor-type breakdown that makes this a carousel and not a shrug.

Pulled: Realtor.com's 2025 investor purchase analysis, released 2026-06-23, senior economist
Hannah Jones. Small investors (fewer than 10 purchases/year) made 63% of investor purchases in
2025, the highest share in at least 15 years, at a $330,000 median purchase price against a
$440,000 overall market median. Mega investors (350+ purchases/year) fell to 7.5% of purchases,
down 70% from their pandemic peak. Checked every carousel file in the repo for "small investor,"
"Realtor.com," and "Hannah Jones" -- no match, so this is a fresh data point.

Hook family `named-stakes` (Family 6: a real, specific number carries the whole hook) differs
from the most recent file in `scripts/carousels/` (`sacred-cow`) and from the companion deck
today (`swap-list`).

Not a `kirp_guest` deck -- no named KIR guest, so this translates to Kale Realty via
`reskin_kr.py` without exception.

---

## SLIDE 1 -- HOOK
**Headline:**
**63 percent.** Highest in 15 years.

**Subhead:**
That's the share of 2025's investor home purchases made by someone who bought fewer than 10 properties, not a hedge fund.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Your buyer keeps losing entry-level homes to an "investor." It's not who they think.

**Subhead:**
It's not a fund with a spreadsheet. It's someone who bought one house this year and wrote a stronger offer.

---

## SLIDE 3 -- THE TURN
**Headline:**
The competitor at the entry price point isn't institutional.

**Body:**
In 2025, small investors, people buying fewer than 10 properties a year, made up 63 percent of all investor home purchases, the highest share in at least 15 years. Mega investors, the kind buying 350 or more homes a year, made up just 7.5 percent, down 70 percent from their pandemic peak. The small investors aren't chasing luxury either: their median purchase price was $330,000, well under the $440,000 overall market median. (Realtor.com, released 2026-06-23, senior economist Hannah Jones.)

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What that changes for the entry-level buyer conversation:

**Numbered list:**
1. **Prep buyers for a local competitor, not a corporate one.** The bidder outpacing them at $330,000 is more often one person with a rental property than a fund with an algorithm.
2. **Ask the listing agent who else has called.** A seller fielding small-investor interest at the entry price has real information your buyer needs before writing the offer.
3. **Explain the number, not just the market.** An agent who can say why the $330,000 band is competitive earns more trust than one who just says it's a tough market.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
The competition at the entry price point has a name. It isn't Wall Street.

---

## Social Captions

### LinkedIn
Small investors, people buying fewer than 10 properties a year, made up 63 percent of all investor home purchases in 2025. That's the highest share in at least 15 years, according to Realtor.com's 2025 investor purchase report, released June 23, 2026.

Their median purchase price was $330,000. Mega investors, the 350-plus-a-year kind, fell to just 7.5 percent of purchases, down 70 percent from their pandemic peak.

If your buyer keeps losing homes in that price band, the bidder beating them usually isn't a fund. It's someone with one rental property and a faster offer.

#RealEstateAgents #InvestorInsights #HomeBuyingTips

### Instagram
63 percent. That's the share of 2025's investor home purchases made by someone buying fewer than 10 properties a year, the highest share in 15 years, per Realtor.com.

Their median purchase price was $330,000. If your buyer's been outbid at that price point, the competitor probably isn't who they think.

#RealEstateAgents #RealtorTips #HomeBuyingTips

### Facebook
Small investors made up 63 percent of all investor home purchases in 2025, the highest share in 15 years, per Realtor.com. Their median purchase price was $330,000.

If your buyer keeps losing entry-level homes, that's who they're actually up against.

#RealEstateAgents #RealtorTips

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-09-28-small-investors-entry-price-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Dark theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. Open deck, no keyword, no ManyChat flow.

**Pinned first comment (IG and FB):** "Source: Realtor.com, 2025 investor purchase report,
released June 23, 2026."

**LinkedIn first comment:**
https://joinkale.com/?src=carousel-kirp-2026-09-28-small-investors-entry-price-carousel

---

## Data Source

- **Claim:** "Small investors (fewer than 10 purchases a year) made up 63% of all investor home
  purchases in 2025, the highest share in at least 15 years, at a $330,000 median purchase price
  against a $440,000 overall market median. Mega investors (350+ purchases a year) made up 7.5%
  of purchases, down 70% from their pandemic peak."
  - Source: Realtor.com, 2025 investor purchase analysis, released 2026-06-23, senior economist
    Hannah Jones. https://www.housingwire.com/articles/investor-home-purchases-2025/
    (HousingWire's coverage of the same Realtor.com report, fetched directly for the figures).
  - Who was measured: Realtor.com's classification of residential property purchases by buyer
    type (investor purchase volume, not agent-reported or consumer-survey data).
  - Status: confirmed, fetched directly from the report coverage on 2026-09-28.
- **Fabrication audit:** No figure is rounded. The $330,000 vs $440,000 comparison and the 63%
  / 7.5% / 70% figures are each stated exactly as reported, not combined into a single derived
  statistic.

## AI Music Prompt

Not applicable. This is a static image carousel, not a video (see `docs/series/carousel-standard.md`,
"Music prompt: only if it ships as video").
