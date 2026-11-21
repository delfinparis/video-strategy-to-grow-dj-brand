---
lane: "evergreen"
carousel_for: "The stat rotation slot: FHA loan delinquencies hit 11.74% in Q3 2026, up 96 basis points year over year, while the overall mortgage delinquency rate rose to 4.42% (MBA National Delinquency Survey, reported by HousingWire 2026-11-19), and what that means for agents working FHA-financed buyers and sellers weighing FHA offers"
hook_family: "myth-bust"
slide_count: 5
goal: "engagement"
generated: "2026-11-21"
theme: "light"
---

# Carousel: the loan falling behind fastest

Second of today's two rotation slots (see
`KIRP-2026-11-21-overprice-listing-swap-carousel.md` for the tie-break note on `stat` vs
`dont-make-this-mistake`). This is the `stat` deck: "one sourced number and what it means."

Sourced per Step 2(b): `data/news-briefs/2026-11-21.md` does not exist yet this morning, so this
deck pulls from yesterday's brief, `data/news-briefs/2026-11-20.md`, "Full story list" entry
"Mortgage delinquencies rise to 4.42% in Q3 2026 - HousingWire" (dated 2026-11-19). The brief
only carries the headline, so every figure below was re-verified at build time by fetching
`https://www.housingwire.com/articles/mortgage-delinquencies-q3-2026/` directly: overall
delinquency rate (seasonally adjusted, one-to-four-unit residential) 4.42%, up 5 bps from Q2 and
43 bps from a year earlier; FHA loans 11.74%, down 5 bps from Q2 but up 96 bps year over year;
conventional loans 2.73%, up 1 bp from Q2 and 11 bps year over year; VA loans 5.00%, up 11 bps
from Q2 and 50 bps year over year. Primary source named in the article: the Mortgage Bankers
Association's National Delinquency Survey. Byline: "HousingWire Automation," reviewed by a
HousingWire editor before publication, dated 2026-11-19.

Checked `scripts/carousels/*.md` for "11.74," "FHA delinquenc," and "National Delinquency
Survey" first -- no prior deck uses this figure or this article.

Hook family `myth-bust`, differing from today's companion deck (`pov-relatable`) and from the
three most recently committed decks before today (`one-tactic-breakdown`, `data-card`,
`listicle-scripts`, all dated 2026-11-20).

No `kirp_guest` field -- no named guest quoted, so this is not flagged, and it reskins to KR
cleanly per `docs/automation/daily-carousel-engine.md`.

---

## SLIDE 1 -- HOOK
**Headline:**
FHA loans are not the safe bet.

**Subhead:**
FHA delinquencies just hit 11.74 percent, up 96 basis points from a year ago.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
11.74 percent of FHA loans are behind on payment right now.

**Subhead:**
That's the loan type most of your first-time buyers are using to get in the door.

---

## SLIDE 3 -- THE TURN

**Headline:**
The loan built for first-time buyers is the one falling behind fastest.

**Body:**
FHA delinquencies rose to 11.74 percent in the third quarter of 2026, up 96 basis points from a
year ago, while conventional loans sit at 2.73 percent and VA loans at 5.00 percent (Mortgage
Bankers Association National Delinquency Survey, reported by HousingWire, November 2026).
Delinquencies across every loan type climbed to 4.42 percent overall, up 43 basis points year
over year. FHA is the entry point for buyers with the thinnest reserves, and thinner reserves
are exactly where a rising payment shows up first.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
What this changes about how you work an FHA deal:

**Numbered list:**
1. **Ask about the reserve cushion before you ask about the rate.** A pre-approval tells you
   what a buyer can borrow. It doesn't tell you what happens if their hours get cut for two
   months.
2. **Flag FHA financing to a seller as context, not a red flag, when offers come in.** The loan
   type is carrying more strain industry-wide right now. That's information for the seller's
   decision, not a reason to rank it last automatically.
3. **Build a plain conversation about payment cushion into every FHA buyer consult.**
   Delinquencies in this loan type are rising faster than any other. The agents who have that
   conversation early keep clients out of trouble later.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
On your next FHA buyer consult, ask about their cushion after a job disruption before you talk
about the rate.

---

## Social Captions

### LinkedIn
FHA loan delinquencies climbed to 11.74 percent in the third quarter, the fastest rising loan type in the latest mortgage data.

### Instagram
The loan most first-time buyers use to get in the door is the one falling behind fastest right now.

### Facebook
Chicago agents, FHA delinquencies just hit 11.74 percent, and that's the loan type carrying most of your first-time buyers.

### TikTok
FHA loan delinquencies hit 11.74% this quarter, the fastest rising loan type in the latest mortgage data. #RealEstateAgent #ChicagoRealEstate

### YouTube Shorts
**Title:** The loan quietly falling behind

FHA loan delinquencies hit 11.74% this quarter, the fastest rising loan type in the latest mortgage data. #RealEstateAgent #ChicagoRealEstate

---

## Data Source

- **"FHA delinquencies rose to 11.74 percent in the third quarter of 2026, up 96 basis points
  from a year ago."**
  - Source: Mortgage Bankers Association National Delinquency Survey, Q3 2026, as reported by
    HousingWire, "Mortgage delinquencies rise to 4.42% in Q3 2026" (2026-11-19).
    [https://www.housingwire.com/articles/mortgage-delinquencies-q3-2026/](https://www.housingwire.com/articles/mortgage-delinquencies-q3-2026/)
  - Who was measured: one-to-four-unit residential mortgage loans, FHA segment.
  - Status: confirmed by direct fetch today, 2026-11-21. Figure quoted verbatim, no rounding.

- **"Conventional loans sit at 2.73 percent and VA loans at 5.00 percent."**
  - Source: same HousingWire article, same survey, confirmed by the same direct fetch.
  - Who was measured: one-to-four-unit residential mortgage loans, by loan type.
  - Status: confirmed, quoted verbatim.

- **"Delinquencies across every loan type climbed to 4.42 percent overall, up 43 basis points
  year over year."**
  - Source: same HousingWire article, same survey.
  - Who was measured: one-to-four-unit residential mortgage loans, all types, seasonally
    adjusted.
  - Status: confirmed, quoted verbatim.

- **Fabrication audit:** All four figures (overall, FHA, conventional, VA) trace to the single
  named HousingWire article above, which itself names the Mortgage Bankers Association's
  National Delinquency Survey as the underlying source. Re-verified at build time by direct
  fetch rather than relying on the brief's headline alone. No invented numbers; no figure
  combined across two unrelated sources.
