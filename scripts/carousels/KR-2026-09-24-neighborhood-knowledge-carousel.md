---
lane: "evergreen"
byline: "none"
series_mark: "KALE REALTY"
carousel_for: "The mistake of not knowing basic factual things about the neighborhood you sell in, and the one-page market sheet fix (Stupid Things bank ST-0056)"
hook_family: "mindset-reframe"
heat: 3
slide_count: 5
goal: "engagement"
theme: "light"
generated: "2026-09-24"
---

# Carousel (KR, fresh topic): He froze on the property taxes.

This is a fresh KR-only topic, not a re-skin. Today's `kirp-guest-tip` companion deck
(`KIRP-2026-09-24-chris-wolfe-desperation-carousel.md`) carries a named guest's own story
(`kirp_guest: true`), and `python3 scripts/reskin_kr.py` correctly exited 2 on it: "features a
KIRP guest, so it does not translate. Author a fresh KR topic instead." Per Step 5, this deck is
authored fresh so two KR decks still ship today.

Sourced per Step 2(d): pulled from `data/stupid-things.md` / `data/stupid-things.json` via
`python3 scripts/stupid_things.py pick --count 8 --stdout`. ST-0056, "not knowing basic factual
things about the neighborhood you sell in," was in that pick list, has an open angle, and has not
been built into any carousel yet (checked against `scripts/carousels/*.md`). It carries a
different receipt than today's other decks: the 88% repeat-use figure on the companion KIRP deck
is a different metric from the same broader NAR report family, and neither reuses the 27%
affordability figure already spent across five earlier carousels this cycle
(`KIRP-2026-08-26-affordability-constraint-carousel.md`,
`KIRP-2026-08-29-affordability-is-the-real-objection-carousel.md`,
`KIRP-2026-09-11-affordability-not-inventory-carousel.md`, and their KR twins).

Hook family `mindset-reframe` (Rule 10: changes how the viewer sees the business -- local
knowledge as the actual engine behind repeat and referral business, not a nice-to-have),
differing from today's companion deck (`confession`) and from
`KIRP-2026-09-23-fed-rate-signal-carousel.md` (`named-stakes`), the most recent carousel in the
repo before today's batch.

Re-verified at build time: the 28%/49%/32% figures were checked against the bank's own
2026-09-10 receipt audit, which explicitly dropped an unsupported "82% of transactions" headline
derived by wrongly adding two different populations. Only the corrected, source-confirmed figures
are used here, and they are never combined into one summed claim (Rule 1: never combine two
separate stats into one sentence implying they are the same population).

---

## SLIDE 1 -- HOOK
**Headline:**
He froze on the property taxes.

**Subhead:**
A buyer asked one basic question standing in the kitchen. That was the day the deal ended, and he hadn't even shown the rest of the house.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
"What are the taxes on this house? Let me get back to you."

**Subhead:**
The buyer already knew the answer before asking. He was testing whether the agent standing in front of him did too.

---

## SLIDE 3 -- THE TURN

**Headline:**
Local knowledge is what turns into referrals, years later.

**Body:**
The median REALTOR gets **28 percent** of their business from repeat clients, up from 20 percent
the year before, per the NAR 2026 Member Profile. Agents with 16 or more years in the business
get 49 percent from repeat clients and another 32 percent from referrals. That reputation is
built one answered question at a time. A buyer who has to wait on a callback for the property
taxes remembers it, and five years from now, when a friend asks who to call, they don't call the
agent who had to check.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Build this before your next listing appointment in a new area:

**Numbered list:**
1. **One page per neighborhood, answerable without reaching for your phone.** Price per square
   foot, days on market, and the property tax reassessment cycle.
2. **Know the boundaries before you're asked.** School boundaries, permit-parking zones, and the
   transfer-tax stack for that specific town or ward.
3. **Ask three people who already live there what they complain about.** That's the detail a
   buyer actually wants, and it's the one no data sheet gives you.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Before your next showing, write down the answer to the one question you dodged last time.

**Subhead:**
That page is the difference between a one-time client and the referral that finds you five years from now.

---

## Social Captions

### LinkedIn
A buyer asked one agent the property taxes on the house they were standing in. He didn't know, and said he'd get back to her. She already knew the answer. She was testing him.

The median REALTOR gets 28 percent of their business from repeat clients, per NAR's 2026 Member Profile, and agents with 16-plus years get 49 percent from repeat clients plus 32 percent from referrals. That reputation gets built one answered question at a time, not overnight.

Kale Realty agents get trained to build a market sheet for every neighborhood they work, not just told to "know their area." Learn more at joinkale.com.

#RealEstateCareers #MarketKnowledge #RealEstateBrokerage

### Instagram
"What are the taxes on this house?" "Let me get back to you." That's the moment a buyer quietly starts looking for a different agent.

Most agents were never given a system for knowing their market cold. They just get told to figure it out.

Kale Realty agents get the systems, not just the split. Learn more at joinkale.com.

#RealEstateAgents #RealEstateCareers #MarketKnowledge

### Facebook
A buyer asked one basic question and the agent had to check. Most agents were never taught a system for knowing their market cold. Kale Realty agents get that system built in. Learn more at joinkale.com.

#RealEstateCareers #RealtorTips

---

## Loomly Handoff

**Slides:** `graphics/carousels/KR-2026-09-24-neighborhood-knowledge-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Light theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel, PDF
in the same folder). Posted from Kale's own pages; no personal byline.

**Gate:** none. Open deck, no keyword, no ManyChat flow.

**Pinned first comment (IG and FB):** "Source: NAR 2026 Member Profile via HousingWire. Full
citation in the Data Source on the carousel file."

**LinkedIn first comment:**
https://joinkale.com/?src=carousel-kr-2026-09-24-neighborhood-knowledge-carousel

---

## Data Source

- **Claim:** "The median REALTOR gets 28 percent of their business from repeat clients, up from
  20 percent the year before."
  - Source: NAR 2026 Member Profile via HousingWire
    (housingwire.com/articles/nar-2026-member-profile-experience/), 2026.
  - Who was measured: REALTOR members, self-reported share of business from repeat clients.
  - Status: confirmed. Carried over from `data/stupid-things.json`, ST-0056, whose receipt was
    re-verified in the bank's 2026-09-10 batch audit.

- **Claim:** "Agents with 16 or more years in the business get 49 percent from repeat clients and
  another 32 percent from referrals."
  - Source: same report as above.
  - Who was measured: REALTOR members with 16+ years of experience, self-reported business
    source.
  - Status: confirmed. Same bank entry. Never combined with the median-agent figure into a single
    summed statistic (Rule 1); the two populations are reported separately here, exactly as in
    the source and exactly as the bank's audit note requires. The bank's audit explicitly
    dropped an unsupported "82% of transactions come from referral or repeat business" headline
    that had wrongly summed these two different populations; that dropped figure does not appear
    anywhere in this deck.

- **Claim:** the one-page neighborhood market sheet (price per square foot, days on market,
  reassessment cycle, school boundaries, permit-parking zones, transfer-tax stack, and asking
  locals what they complain about).
  - Source: `data/stupid-things.md` / `data/stupid-things.json`, ST-0056, `angles[0].swap` field.
    Practice guidance, not a statistic; no external citation required under Rule 1.
  - Status: confirmed, drawn from the bank entry and tightened to fit the five-slide format.
