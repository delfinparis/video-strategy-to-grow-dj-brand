---
lane: "evergreen"
carousel_for: "VantageScore 4.0 just got FHFA approval for Fannie Mae and Freddie Mac loans, needs one month of credit history instead of six, and can count rent and utility payments, which could change who an agent assumes can't qualify yet"
hook_family: "myth-bust"
heat: 2
slide_count: 5
goal: "engagement"
generated: "2026-10-31"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
---

# Carousel: a thin credit file is not a bad credit file

**Why this deck exists.** Today's `kirp-guest-tip` deck (Mischa Fisher, aired 2026-10-30) carries
a named guest's own analysis and does not translate to Kale per `reskin_kr.py` (exit 2, confirmed
below). Per the engine's own rule, authoring a fresh KR-only topic instead so two KR decks ship
today regardless. Lane `evergreen`, `byline: "none"`, `series_mark: "KALE REALTY"` per the
daily-carousel-engine spec for this exact situation.

```
$ python3 scripts/reskin_kr.py scripts/carousels/KIRP-2026-10-31-payment-doubled-leverage-carousel.md
KIRP-2026-10-31-payment-doubled-leverage-carousel.md features a KIRP guest, so it does not
translate. Author a fresh KR topic instead.
(exit 2)
```

**Source:** today's news brief (`data/news-briefs/2026-10-31.md`) flagged VantageScore 4.0 as the
day's stat tip, sourced loosely as "NAR (via Inman)." Re-verified at build time per the repeated
Rule 1 instruction never to ship a vague attribution: fetched the two named articles underneath
the headline directly.

- Sarah Wolak, "Silvio Tavares steps down as VantageScore CEO, Anthony Hutchinson named interim
  leader," HousingWire, published October 30, 2026, 4:53pm ET:
  https://www.housingwire.com/articles/vantagescore-ceo-steps-down/
- Dave Gallagher, "What to know about VantageScore 4.0, the alternative to FICO," Real Estate
  News, published October 30, 2026:
  https://www.realestatenews.com/2026/10/30/what-to-know-about-vantagescore-4-0-the-alternative-to-fico

**The one idea:** VantageScore 4.0 needs one month of credit history instead of FICO's six, and
it can count rent and utility payments, so a buyer agents assumed couldn't qualify on thin credit
might qualify now that Fannie Mae and Freddie Mac accept scores based on it. Rule 0 criterion 4,
a surprising statistic properly sourced (the six-months-to-one-month gap, and the 11-point score
difference Rocket reports), and criterion 3, a pattern reveal (most agents still screen buyers by
the old FICO assumption).

Hook family `myth-bust` (breaks the "thin credit means can't qualify" assumption), differing from
both of today's other carousels (`data-card` and `one-tactic-breakdown`) and from the two most
recently committed decks before today (`swap-list` and `myth-bust` on 2026-10-30 -- a repeat of
the family name but not consecutive, since two different decks sit between them today).

---

## SLIDE 1 -- HOOK
**Headline:**
A new credit score just cleared for mortgages.

**Subhead:**
It needs one month of history instead of six, and that changes who qualifies.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Some buyers get turned down for thin credit, not bad credit.

**Subhead:**
A new score model counts rent and utility payments instead of waiting on six months of history.

---

## SLIDE 3 -- THE TURN
**Headline:**
One month of history. Not six.

**Body:**
VantageScore 4.0 needs just one month of credit history, where FICO needs six, and it can count
rent and utility payments too. The Federal Housing Finance Agency approved it, and Fannie Mae and
Freddie Mac now accept mortgage credit scores based on it. On loans already using it, Rocket
reports scores running about **11 points** higher than Classic FICO, and most borrowers got the
same price or a slightly better one.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What to do with a buyer who got told no before:

**Numbered list:**
1. **Ask the lender if they run VantageScore 4.0.** Not every lender has turned it on yet.
2. **Ask for both scores if the buyer has thin credit.** Someone with little card history but a clean rent and utility record could score higher on the new model.
3. **Check the price, not just the score.** A higher score only helps if it actually changes the rate or the cash needed to close.
4. **Get this confirmed before the offer, not after.** Lock in which score the pre-approval is actually using.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
A thin credit file isn't a bad credit file.

**Subhead:**
Ask about VantageScore 4.0 before you tell a buyer they can't qualify yet.

---

## Social Captions

### LinkedIn
Fannie and Freddie now accept a credit score that needs one month of history instead of six.

### Instagram
A thin credit file is not a bad credit file now that Fannie and Freddie accept VantageScore 4.0.

### Facebook
Ask your lender if they run VantageScore 4.0 before you tell a buyer with thin credit they can't qualify.

---

## Data Source

- **Claim:** "The Federal Housing Finance Agency approved VantageScore 4.0, and Fannie Mae and
  Freddie Mac now accept mortgage credit scores based on it."
  - Source: Dave Gallagher, "What to know about VantageScore 4.0, the alternative to FICO," Real
    Estate News, published October 30, 2026.
  - Who was measured: regulatory/GSE policy change, not a survey.
  - Status: confirmed.

- **Claim:** "VantageScore 4.0 needs just one month of credit history, where FICO needs six, and
  it can count rent and utility payments."
  - Source: same Real Estate News article, October 30, 2026.
  - Status: confirmed.

- **Claim:** "Rocket reports scores running about 11 points higher than Classic FICO [on loans
  already using VantageScore 4.0], and most borrowers got the same price or a slightly better
  one."
  - Source: same Real Estate News article, October 30, 2026, citing Rocket's own reported data
    and its chief business officer.
  - Who was measured: Rocket's own originated loans, self-reported by the lender, not an
    independent industry-wide study.
  - Status: confirmed as a company-reported figure, labeled as such.

- **Dropped from the original brief's framing:** the news brief attributed this story to
  "NAR (via Inman)" with no named publication or date. Re-verified at build time per the
  standing instruction never to ship a vague source; replaced with the two named, dated articles
  above. No FHFA adoption-rate figure or borrower-count estimate exists in either source, so none
  is claimed here.
