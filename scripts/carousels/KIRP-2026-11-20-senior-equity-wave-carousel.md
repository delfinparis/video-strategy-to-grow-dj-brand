---
lane: "evergreen"
carousel_for: "The market-tip rotation slot: homeowners 62+ now hold $14.66 trillion in home equity, an all-time high and a 2025 wealth-share crossover (HousingWire), and the outreach tactic that opens the conversation before Zillow's pre-seller push gets there first"
hook_family: "data-card"
slide_count: 5
goal: "engagement"
generated: "2026-11-20"
theme: "light"
---

# Carousel: the senior equity wave

Second of today's two rotation slots (see
`KIRP-2026-11-20-manage-energy-not-time-carousel.md` for the tie-break note on `market-tip` vs
`do-this-dont-do-that`). This is the `market-tip` deck: "a tactic for the current market, what
an agent does differently this month."

Sourced per Step 2(b): `data/news-briefs/2026-11-20.md` does not exist yet this morning (the
walk-and-talk brief routine runs separately and had not landed), so this deck pulls from
yesterday's brief, `data/news-briefs/2026-11-19.md`, which carries this cycle's evergreen stat
tip: homeowners 62 and older hold $14.66 trillion in home equity, an all-time high. Source as
the brief lists it: HousingWire. Re-verified at build time per the stat-sourcing rule: fetched
`https://www.housingwire.com/articles/senior-wealth-underwriting-gap/` directly and confirmed
the figure verbatim ("Homeowners 62 and older hold $14.66 trillion in home equity, an all-time
high"), plus the 2025 wealth-share crossover ("Americans 70 and older hold a larger share of the
nation's real estate wealth than Americans aged 40 to 54" for the first time on record, and older
homeowners now control roughly 26% of America's $48 trillion in real estate wealth). Byline
Gerald Green; the piece carries a `datePublished` of 2026-07-01, consistent with the brief's own
framing of this as a persisting evergreen stat tip rather than this week's news.

Checked `scripts/carousels/*.md` for "14.66," "senior equity," and "62 and older" first -- no
prior deck uses this figure or this article.

**The one idea:** the brief's own "how to use it" line names the tactic -- most agents are
competing hardest for the thinnest slice of the market (first-time buyers), while homeowners 62+
now hold a record $14.66 trillion in equity and most of them have not run the number. The agent
who starts that conversation this month, before Zillow's pre-seller outreach (also in this
week's brief) gets to the same homeowner first, owns it.

Hook family `data-card` (the headline is the number itself, auto-sized by the renderer),
differing from today's companion deck (`one-tactic-breakdown`) and from the two most recently
committed decks before today (`one-tactic-breakdown`, `pov-relatable`,
`KIRP-2026-11-20-manage-energy-not-time-carousel.md` and `KIRP-2026-11-19-slow-showing-reply-carousel.md`).

No `kirp_guest` field -- no named guest quoted, so this is not flagged, and it reskins to KR
cleanly per `docs/automation/daily-carousel-engine.md`.

---

## SLIDE 1 -- HOOK
**Headline:**
$14.66 trillion.

**Subhead:**
That's how much home equity owners 62 and older are sitting on right now, an all-time high.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Most of your past clients have no idea what their house is actually worth now.

**Subhead:**
Older homeowners just passed everyone else in real estate wealth. Most agents are still chasing
first-time buyers.

---

## SLIDE 3 -- THE TURN

**Headline:**
The wealthiest sellers in the market aren't the ones agents are courting.

**Body:**
For the first time on record, Americans 70 and older now hold a bigger share of the nation's
real estate wealth than Americans 40 to 54. That crossover happened in 2025. Older homeowners
now control roughly 26% of America's $48 trillion in real estate wealth, and homeowners 62 and
older alone hold $14.66 trillion of it, an all-time high. Most of that equity sits unexamined,
because nobody has told the homeowner what the number actually is this year.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
What to do with it this month:

**Numbered list:**
1. **Pull your closed-client list and flag everyone 62 and older.** This is the group holding
   the equity, and most of them haven't gotten a current number from anyone.
2. **Send a current equity estimate, not a pitch.** One number, one personal note. No listing
   ask attached.
3. **Open the downsizing or life-planning conversation before anyone else does.** A platform is
   already reaching out to sellers before they list. The agent who calls first keeps the
   relationship.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Pick ten past clients age 62 or older. Send each one their current equity number this week, no
pitch attached.

---

## Social Captions

### LinkedIn
Homeowners 62 and older now hold $14.66 trillion in home equity, an all-time high, and for the
first time on record older homeowners control a bigger share of real estate wealth than
homeowners in their 40s and 50s.

### Instagram
Most of your past clients have no idea their house just crossed into real money.

### Facebook
Chicago agents, your clients 62 and older are sitting on more home equity than ever, and most of them don't know the current number.

### TikTok
Homeowners 62 and older now hold a record $14.66 trillion in home equity. #RealEstateAgent #ChicagoRealEstate

### YouTube Shorts
**Title:** The equity wave agents are missing

Homeowners 62 and older now hold a record $14.66 trillion in home equity, and most agents aren't talking to them about it. #RealEstateAgent #ChicagoRealEstate

---

## Data Source

- **"Homeowners 62 and older hold $14.66 trillion in home equity, an all-time high."**
  - Source: HousingWire, "Seniors Hold Record Housing Wealth, Underwriting Still Misses It," by
    Gerald Green. [https://www.housingwire.com/articles/senior-wealth-underwriting-gap/](https://www.housingwire.com/articles/senior-wealth-underwriting-gap/)
  - Status: confirmed by direct fetch of the article today, 2026-11-20. Figure quoted verbatim,
    no rounding.

- **"For the first time on record, Americans 70 and older hold a larger share of the nation's
  real estate wealth than Americans aged 40 to 54. That crossover happened in 2025. Older
  homeowners now control roughly 26% of America's $48 trillion in real estate wealth."**
  - Source: same HousingWire article, same byline, confirmed by the same direct fetch.
  - Status: confirmed, quoted near-verbatim.

- **Fabrication audit:** Both figures trace to the single named article above, fetched and
  re-read at build time. No invented numbers; no figure combined across two unrelated sources.
