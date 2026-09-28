---
lane: "evergreen"
carousel_for: "ST-0053 from data/stupid-things.md: talking an unrepresented buyer out of getting their own agent, then writing the deal as an undisclosed dual agent -- what Illinois law (225 ILCS 454/15-45) actually requires before that's allowed"
hook_family: "swap-list"
heat: 4
slide_count: 5
goal: "engagement"
generated: "2026-09-28"
theme: "light"
---

# Carousel: Don't say this to an unrepresented buyer.

Today's rotation: two topic types tied oldest per `data/carousel-topic-rotation.json`.
`stat` was the true oldest at `last_used: 2026-09-25`, built as the companion deck
(`KIRP-2026-09-28-small-investors-entry-price-carousel.md`). `do-this-dont-do-that` and
`dont-make-this-mistake` tied for next-oldest at `2026-09-26`; `do-this-dont-do-that` taken
by list order, the same tie-break convention prior runs used.

Source order followed: 2(a) not applicable, not a `kirp-guest-tip` deck. 2(b) today's and
yesterday's news briefs both surfaced the same three "realtor tips" entries (ST-0010, ST-0052,
ST-0001), and all three are already the subject of multiple carousels in this repo
(`KIRP-2026-09-17-material-fact-disclosure-carousel.md`, `KIRP-2026-09-14-kickback-disclosure-carousel.md`,
`KIRP-2026-09-19-four-week-pricing-window-carousel.md` and their KR twins), so building from
them again would be a repeat, not a new angle. Went to the broader Stupid Things bank
(`data/stupid-things.json`) instead and filtered for an entry with a `confirmed` receipt, an
open angle, and no prior appearance in `scripts/carousels/` (checked every `ST-####` id against
the carousel folder). Three qualified: ST-0051, ST-0053, ST-0057. Picked ST-0053 -- the
double-ending / unrepresented-buyer angle -- over ST-0051 (self-listing steering, a close
cousin) for variety, and over ST-0057 because that entry's banked receipt (a 2026 Relitix new-agent
survival stat) does not actually support its stated claim about price estimates and would need a
real re-source, not just re-verification, to ship honestly.

Re-verified the receipt today rather than trusting the bank's "confirmed" status per Rule 1 and
the Stupid Things standard's "re-verify at build time, every time": fetched 225 ILCS 454/15-45
directly (FindLaw's codified text). Confirmed it requires informed written consent from all
clients for dual agency, plus a separate written confirmation at the point an offer is made, and
that a licensee cannot act as a dual agent when they or an affiliated entity is a party to the
transaction. Matches the bank's claim exactly; nothing softened, nothing added.

Hook family `swap-list` (Family 9: the exact wrong line and the exact right one) differs from
the most recent file in `scripts/carousels/` (`sacred-cow`) and from the companion deck today
(`named-stakes`).

Not a `kirp_guest` deck -- no named KIR guest, so this translates to Kale Realty via
`reskin_kr.py` without exception.

---

## SLIDE 1 -- HOOK
**Headline:**
Don't say this to an unrepresented buyer.

**Subhead:**
The listing agent's favorite line costs the buyer more than either of you thinks.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
"You don't need your own agent." That's not free advice.

**Subhead:**
The person saying it already represents the seller. Now they're representing the buyer too, and the buyer never agreed to it.

---

## SLIDE 3 -- THE TURN
**Headline:**
That sentence collapses into dual agency.

**Body:**
When a listing agent talks an unrepresented buyer out of getting their own agent and writes the deal instead, that's dual agency, representing both sides of one transaction. In Illinois, 225 ILCS 454/15-45 only permits it with informed written consent from every client, disclosed before it happens and confirmed again in writing at the offer. A buyer told "you don't need your own agent" almost never gets that disclosure. What they get is a faster close for the one agent who already owes a duty to the other side.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What to say instead when an unrepresented buyer calls on your listing:

**Numbered list:**
1. **Say who you represent, first.** "I represent the seller. You're welcome to your own agent, and it costs you nothing to have someone in your corner."
2. **Only go dual if they insist, in writing.** Illinois requires informed written consent from both sides, plus a second written confirmation when the offer is made. Skip either step and the file is exposed, not just the buyer.
3. **Note that you disclosed it.** A one-line file note or text confirming you offered representation protects you as much as it protects them.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
The buyer's right to their own agent doesn't cost you the deal. Hiding it does.

---

## Social Captions

### LinkedIn
"You don't need your own agent, I can just write it up for you." An unrepresented buyer hears that from the listing agent more often than most clients realize.

That listing agent already represents the seller. Writing the buyer's offer too makes it dual agency, and in Illinois, 225 ILCS 454/15-45 only allows that with informed written consent from every client, disclosed up front and confirmed again in writing at the offer.

The better line costs nothing to say: "I represent the seller. You're welcome to your own agent, and it costs you nothing to have someone in your corner."

#RealEstateAgents #RealtorTips #BuyerRepresentation

### Instagram
"You don't need your own agent." If a buyer hears that from the listing agent, it's not free advice. That agent already represents the seller.

In Illinois, writing both sides of a deal requires informed written consent, disclosed up front and confirmed again at the offer. What to say instead is in the carousel.

#RealEstateAgents #RealtorTips #BuyerRepresentation

### Facebook
The listing agent telling an unrepresented buyer they don't need their own agent isn't doing them a favor. That agent already represents the seller.

Illinois law requires written consent before one agent can represent both sides. Say that instead.

#RealEstateAgents #RealtorTips

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-09-28-dont-talk-them-out-of-their-own-agent-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Light theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. Open deck, no keyword, no ManyChat flow.

**Pinned first comment (IG and FB):** "Source: Illinois Real Estate License Act, 225 ILCS 454/15-45 (dual agency, informed written consent)."

**LinkedIn first comment:**
https://joinkale.com/?src=carousel-kirp-2026-09-28-dont-talk-them-out-of-their-own-agent-carousel

---

## Data Source

- **Claim:** "Illinois law (225 ILCS 454/15-45) permits a licensee to act as a dual agent, that
  is, to represent both parties in the same transaction, only with the informed written consent
  of all clients, disclosed before the dual agency begins, and reconfirmed in a separate written
  confirmation at the time an offer or contract is executed. A licensee cannot act as a dual
  agent when the licensee or an entity in which they hold an ownership interest is itself a
  party to the transaction."
  - Source: Illinois Real Estate License Act, 225 ILCS 454/15-45, current codified text, fetched
    directly from FindLaw's Illinois statutes on 2026-09-28.
    https://codes.findlaw.com/il/chapter-225-professionsoccupations-and-business-operations/il-st-sect-225-454-15-45/
  - Who was measured: n/a -- statutory text, not survey or observational data.
  - Status: confirmed by direct fetch today. This re-verifies (does not merely repeat) the
    Stupid Things bank's 2026-09-10 batch check of the same statute for entry ST-0053.
- **Fabrication audit:** No figure or statistic in this deck. The claim is a paraphrase of the
  statute's actual requirements, not a summary "the law says agents must disclose" -- the specific
  written-consent and written-confirmation mechanics are stated because they are what the statute
  says, not because they sound stronger.

## AI Music Prompt

Not applicable. This is a static image carousel, not a video (see `docs/series/carousel-standard.md`,
"Music prompt: only if it ships as video").
