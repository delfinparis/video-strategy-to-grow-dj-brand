---
lane: "evergreen"
carousel_for: "MRED (the Chicago area's MLS) requires listing status changes within 48 hours of the triggering event, with a $250 fine for a late change, and why leaving a sold or pending listing marked Active is lead harvesting off the seller's own home, not a marketing delay"
hook_family: "swap-and-list"
heat: 4
slide_count: 5
goal: "engagement"
generated: "2026-09-26"
theme: "dark"
---

# Carousel: Still "Active" three weeks after it sold.

Today's rotation: two topic types tied oldest and next-oldest per `data/carousel-topic-rotation.json`
(`do-this-dont-do-that` true oldest at `2026-09-23`; `dont-make-this-mistake` and `kirp-guest-tip`
tied at `2026-09-24`, `dont-make-this-mistake` taken over `kirp-guest-tip` by list order since both
are equally stale). This deck is `do-this-dont-do-that`; the companion deck (`dont-make-this-mistake`)
is `KIRP-2026-09-26-earnest-money-clock-carousel.md`.

Source order followed: 2(a) not applicable, not a `kirp-guest-tip` deck. 2(b)/2(c) neither today's
news brief nor the stat bank carried a clean do-this/don't-do-that swap, so this pulled from the
Stupid Things Realtors Do bank (`python3 scripts/stupid_things.py pick`), entry ST-0037 "Sitting on
the pending or sold status change to keep the listing looking active." The bank entry shipped
`receipt: NEEDS RECEIPT` with a flag to cite MRED specifically, not a national generality.
Re-verified at build time per the standard: confirmed via the Chicago Association of REALTORS'
"New 48-Hour Listing Status Requirement for connectMLS" announcement (effective 2019-03-01) that
MRED requires status changes within 48 hours including weekends and holidays, carrying a $250 fine
for noncompliance; corroborated independently against MRED's own current Rules and Regulations
documentation (MRED Support Center / Rules and Regulations Department), which states the same
48-hour window and $250 automatic fine. Checked every carousel file in the repo for "MRED,"
"48 hour," and "status change" -- no match, so this is a genuinely new angle, not a repeat of the
already-built kickback (`KIRP-2026-09-20-referral-kickback-swap-carousel.md`) or disclosure
(`KIRP-2026-09-17-material-fact-disclosure-carousel.md`) entries from the same bank.

Hook family `swap-and-list` (Family 9: the exact wrong move and the exact right move, the most
saveable family) differs from the companion deck's `named-stakes` and from the most recent KIRP
decks (`system-indictment` and `defector`, both 2026-09-25).

Not a `kirp_guest` deck -- no named KIR guest, so this translates to Kale Realty via
`reskin_kr.py` without exception.

---

## SLIDE 1 -- HOOK
**Headline:**
Still **Active** three weeks after it sold.

**Subhead:**
That listing isn't being marketed anymore. It's being used to farm your leads.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
The house is sold. The listing isn't.

**Subhead:**
Buyers still call on homes that already have a contract, because nobody changed the status.

---

## SLIDE 3 -- THE TURN
**Headline:**
Chicago's MLS gives you 48 hours to change it. Some agents let it ride for weeks.

**Body:**
MRED, the Chicago area's MLS, requires an agent to change a listing's status within 48 hours of the triggering event, weekends and holidays included, and a late change carries a 250 dollar fine. Some agents leave a listing marked Active for weeks after it goes under contract anyway. Every buyer call on that "available" listing goes to the agent who left it stale, on a house they can't sell. The seller's own listing becomes the agent's lead machine.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What that means for your own listings:

**Numbered list:**
1. **Change the status the day the contract is signed, not the day you remember.** Put your MLS deadline on the calendar the moment you get a signature, not on a mental to-do list.
2. **Capture the lead honestly instead.** Tell the caller, "That one's under contract, but here are three like it," and actually have three ready to show.
3. **Check your own board's days-on-market data before you price off it.** A stale status feeds bad comps to every agent pricing nearby, including you.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
A sold listing left "Active" isn't marketing. It's using the seller's home to generate your next lead.

---

## Social Captions

### LinkedIn
MRED, the Chicago area's MLS, gives agents 48 hours to change a listing's status once it's under contract. Some leave it marked Active for weeks instead.

Every buyer call on that listing goes to the agent who left the status stale, on a house that already sold. The seller's own listing becomes somebody's lead generator, and the days-on-market data every other agent is pricing off gets corrupted along with it.

If you've got a pending or sold listing still marked Active, change it today. Then build the habit: the day a contract gets signed, the status change goes on the calendar before anything else does.

#RealEstateAgents #MLSRules #RealtorTips #InsideTheIndustry

### Instagram Reels
Still showing "Active" weeks after it went under contract? That's not a marketing delay. Every call on that listing goes to whoever left the status stale.

Change it the day the contract is signed, then hand callers three homes you can actually sell.

#RealEstateAgents #RealtorTips #MLSRules

### Facebook
A listing left "Active" after it's under contract isn't being marketed anymore. It's generating leads for whoever didn't update the status.

Change it within your MLS's deadline, every time.

#RealEstateAgents #RealtorTips

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-09-26-status-change-lead-farm-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Dark theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. Open deck, no keyword, no ManyChat flow.

**Pinned first comment (IG and FB):** "Source: Chicago Association of REALTORS, 'New 48-Hour
Listing Status Requirement for connectMLS,' effective 2019-03-01, MRED's current status-change
rule."

**LinkedIn first comment:**
https://joinkale.com/?src=carousel-kirp-2026-09-26-status-change-lead-farm-carousel

---

## Data Source

- **Claim:** "MRED, the Chicago area's MLS, requires listing status changes within 48 hours of
  the triggering event, weekends and holidays included, and a late change carries a $250 fine."
  - Source: Chicago Association of REALTORS, "New 48-Hour Listing Status Requirement for
    connectMLS," effective 2019-03-01.
    https://chicagorealtor.com/new-48-hour-listing-status-requirement-for-connectmls-effective-march-1-2019/
  - Corroborated against: MRED's current Rules and Regulations documentation (MRED Support
    Center / MRED Rules and Regulations Department), which independently states the same
    48-hour window and $250 automatic fine as of this repo's 2026-09-26 search.
  - Who was measured: not applicable. MLS operating rule and fine schedule, not a survey.
  - Status: confirmed via two independent sources (the 2019 CAR announcement and MRED's own
    current rules documentation) agreeing on the same figures. The underlying MRED Rules and
    Regulations PDF (revised 2026-03-20 per search index) could not be parsed directly to
    re-confirm the fine amount word for word, but the current MRED Support Center language
    corroborates it independently.
- **Fabrication audit:** No figure is invented or rounded. The deck does not claim any specific
  agent has been fined; it states the rule and the fine schedule as written, and frames the
  lead-harvesting consequence as a described mechanism, not an accusation against a named party.

## AI Music Prompt

Not applicable. This is a static image carousel, not a video (see `docs/series/carousel-standard.md`,
"Music prompt: only if it ships as video").
