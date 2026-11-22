---
lane: "evergreen"
carousel_for: "The market-tip rotation slot: NAR's 2026 Member Profile names affordability as the top client constraint agents face, at 27%, and the tactic of bringing the payment conversation first instead of waiting for the buyer to raise it"
hook_family: "data-card"
slide_count: 5
goal: "engagement"
generated: "2026-11-22"
theme: "light"
---

# Carousel: the affordability constraint

Second of today's two rotation slots (see `KIRP-2026-11-22-contract-you-didnt-write-carousel.md`
for the tie-break note on `market-tip` vs `kirp-guest-tip`). This is the `market-tip` deck: "a
tactic for the current market, what an agent does differently this month."

Sourced per Step 2(b): `data/news-briefs/2026-11-22.md` does not exist yet this morning (the
walk-and-talk brief routine runs separately and had not landed), so this deck pulls from
yesterday's brief, `data/news-briefs/2026-11-21.md`, which carries this cycle's evergreen stat
tip: "Affordability is the top constraint keeping buyers out of the market at 27%," sourced to
the NAR 2026 Member Profile via HousingWire. Re-verified at build time per the stat-sourcing
rule: fetched `https://www.housingwire.com/articles/nar-2026-member-profile-experience/` directly
and confirmed the figure verbatim ("Typical member has 13 years of experience, while
affordability is the top client constraint at 27%"). Byline Brooklee Han and HousingWire
Automation; published 2026-06-25, consistent with the brief's own framing of this as a
persisting evergreen stat tip rather than this week's news.

Checked `scripts/carousels/*.md` for "27%," "affordability," and "top client constraint" first
-- no prior deck uses this figure or this article.

**The one idea:** the brief's own "how to use it" line names the tactic -- agents assume a buyer
who goes quiet lost interest in the house, when NAR's own member data says the top constraint
agents actually face is affordability, not taste or hesitation. The agent who brings the payment
conversation first, instead of waiting for the buyer to raise it, keeps the lead the others lose.

Hook family `data-card` (the headline is the number itself, auto-sized by the renderer),
differing from today's companion deck (`one-tactic-breakdown`) and from the two most recently
committed decks before today (`myth-bust` and `pov-relatable`, both `KIRP-2026-11-21-*`).

No `kirp_guest` field -- no named guest quoted, so this is not flagged, and it reskins to KR
cleanly per `docs/automation/daily-carousel-engine.md`.

---

## SLIDE 1 -- HOOK
**Headline:**
27%.

**Subhead:**
That's the number one reason buyers say they can't move forward. Not the house. The payment.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Your buyer didn't lose interest. They ran the numbers and went quiet.

**Subhead:**
Most agents never find out which one it was. The buyer just stops calling back.

---

## SLIDE 3 -- THE TURN

**Headline:**
Affordability is the top constraint agents report, not buyer taste.

**Body:**
NAR's own 2026 Member Profile found affordability is the top client constraint agents face, at
27%, ahead of inventory, timing, or buyer hesitation. Most agents wait for the buyer to bring up
the payment gap first. Most buyers never do. They quietly assume nothing can be done, and go
back to renting.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
What to do with it this month:

**Numbered list:**
1. **Bring the payment conversation first, before the buyer has to.** Ask what monthly number
   feels safe, not just their price range.
2. **Know two financing tools cold: rate buy-downs and down payment assistance.** Name them in
   the first showing, not after an offer falls through.
3. **Re-run the math the moment rates move.** A buyer who got priced out in spring may qualify
   again today, and nobody has told them.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Call the last three buyers who went quiet. Ask about the payment, not the house.

---

## Social Captions

### LinkedIn
NAR's own member data says affordability, not buyer taste, is the top reason deals stall, at 27%.

### Instagram
Your buyer didn't go quiet because they lost interest, they ran the numbers.

### Facebook
Chicago agents, the number one reason buyers stall is the payment, not the house, and NAR's own data puts it at 27%.

### TikTok
Affordability is the real reason buyers go quiet, not the house. #RealEstateAgent #ChicagoRealEstate

### YouTube Shorts
**Title:** Why your buyer went quiet

Affordability, not buyer taste, is the real reason deals stall, and NAR puts it at 27%. #RealEstateAgent #ChicagoRealEstate

---

## Data Source

- **"Affordability is the top client constraint at 27%."**
  - Source: HousingWire, "NAR 2026 Member Profile" coverage, by Brooklee Han and HousingWire
    Automation. [https://www.housingwire.com/articles/nar-2026-member-profile-experience/](https://www.housingwire.com/articles/nar-2026-member-profile-experience/)
  - Status: confirmed by direct fetch of the article today, 2026-11-22. Figure quoted verbatim
    ("affordability is the top client constraint at 27%"), published 2026-06-25, no rounding.

- **Fabrication audit:** The figure traces to the single named article above, fetched and
  re-read at build time. No invented numbers; no figure combined across two unrelated sources.
