---
lane: "evergreen"
carousel_for: "Illinois Administrative Code title 68, section 1450.750(d)(1) gives a sponsoring broker one business day to deposit earnest money into the trust account, and the Illinois Real Estate License Act (225 ILCS 454, section 20-20(a)(17)) treats a late deposit as its own separate license violation"
hook_family: "named-stakes"
heat: 4
slide_count: 5
goal: "engagement"
generated: "2026-09-26"
theme: "light"
---

# Carousel: One business day. That's the law.

Today's rotation: two topic types tied oldest and next-oldest per `data/carousel-topic-rotation.json`
(`do-this-dont-do-that` true oldest at `2026-09-23`; `dont-make-this-mistake` and `kirp-guest-tip`
tied at `2026-09-24`, `dont-make-this-mistake` taken over `kirp-guest-tip` by list order since both
are equally stale). This deck is `dont-make-this-mistake`; the companion deck
(`do-this-dont-do-that`) is `KIRP-2026-09-26-status-change-lead-farm-carousel.md`.

Source order followed: 2(a) not applicable, not a `kirp-guest-tip` deck. 2(b)/2(c) neither today's
news brief nor the stat bank carried a clean single-mistake angle with a sourceable number, so this
pulled from the Stupid Things Realtors Do bank (`python3 scripts/stupid_things.py pick`), entry
ST-0007 "Sitting on earnest money instead of depositing it into the trust account on time." The
bank entry shipped `receipt: NEEDS RECEIPT` flagged as a legal-exposure entry: "cite the actual
state escrow rule ... say the exposure, never predict the verdict." Re-verified at build time:
confirmed via Illinois Administrative Code title 68, section 1450.750(d)(1) (Cornell Legal
Information Institute), which sets the deposit deadline at "no later than the next business day"
following the transaction or receipt of the funds; confirmed separately via the Illinois Real
Estate License Act of 2000, 225 ILCS 454, section 20-20(a)(17) (FindLaw), which lists failing to
maintain and timely deposit escrow moneys as its own independent ground for discipline, apart from
any dispute over the underlying deal. No enforcement action is cited or implied, per the flag's
instruction to state the exposure, not predict a verdict. Checked every carousel file in the repo
for "earnest money," "trust account," and "escrow" -- no match, so this is a genuinely new angle.

Hook family `named-stakes` (Family 6: specificity beats abstraction, the exact statute and the
exact deadline) differs from the companion deck's `swap-and-list` and from the most recent KIRP
decks (`system-indictment` and `defector`, both 2026-09-25).

Not a `kirp_guest` deck -- no named KIR guest, so this translates to Kale Realty via
`reskin_kr.py` without exception.

---

## SLIDE 1 -- HOOK
**Headline:**
**One** business day. That's the law.

**Subhead:**
That's how long Illinois gives you to get earnest money into the trust account.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
A check in your desk drawer is a license problem, not a paperwork problem.

**Subhead:**
Earnest money that hasn't hit the trust account isn't "getting to it later." It's already late.

---

## SLIDE 3 -- THE TURN
**Headline:**
Illinois doesn't give a grace period. It gives you one business day.

**Body:**
Under Illinois Administrative Code title 68, section 1450.750(d)(1), a sponsoring broker must place earnest money into the trust account no later than the next business day after the contract is signed or the money is received. The Illinois Real Estate License Act lists a late deposit as its own separate ground for discipline, under 225 ILCS 454, section 20-20(a)(17), apart from any dispute over the deal itself. The deadline isn't a guideline agents interpret. It's a specific number of days, and it starts the moment you take the check.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Fix the habit, not the memory:

**Numbered list:**
1. **Put the deposit deadline on the calendar the same hour you take the check.** An all-day event with the file name on it, not a mental note.
2. **Deposit before you leave the office that day, not "this week."** The rule counts business days, and a busy Friday still counts as one.
3. **Ask your managing broker where the trust account log lives, if you don't already know.** If you can't answer that today, that's the actual gap.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
The earnest money check isn't yours to hold onto. Illinois already told you how long you have.

---

## Social Captions

### LinkedIn
Illinois gives a sponsoring broker one business day to get earnest money into the trust account, under Illinois Administrative Code title 68, section 1450.750(d)(1). Not a week. One business day after the signature or the money changes hands.

The Illinois Real Estate License Act treats a late deposit as its own violation, separate from any dispute over the money itself, under 225 ILCS 454, section 20-20(a)(17).

If your process for depositing earnest money is "I'll get to it," fix that this week. Put the deposit deadline on your calendar the same hour you take the check, and deposit it before you leave the office that day.

#RealEstateAgents #RealtorTips #RealEstateLaw #InsideTheIndustry

### Instagram Reels
Illinois gives you one business day to get earnest money into the trust account. Not a week. One business day.

Put the deposit deadline on your calendar the moment you take the check, then deposit it before you leave the office.

#RealEstateAgents #RealtorTips #RealEstateLaw

### Facebook
Illinois law gives you one business day to deposit earnest money into the trust account. A late deposit is its own violation, separate from the deal itself.

Put the deadline on your calendar the moment you take the check.

#RealEstateAgents #RealtorTips

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-09-26-earnest-money-clock-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Light theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. Open deck, no keyword, no ManyChat flow.

**Pinned first comment (IG and FB):** "Source: Illinois Administrative Code title 68, section
1450.750(d)(1); Illinois Real Estate License Act of 2000, 225 ILCS 454, section 20-20(a)(17)."

**LinkedIn first comment:**
https://joinkale.com/?src=carousel-kirp-2026-09-26-earnest-money-clock-carousel

---

## Data Source

- **Claim:** "Illinois requires a sponsoring broker to deposit earnest money into the trust
  account no later than the next business day after the transaction is signed or the money is
  received."
  - Source: Illinois Administrative Code, title 68, section 1450.750(d)(1) (Cornell Legal
    Information Institute). https://www.law.cornell.edu/regulations/illinois/Ill-Admin-Code-tit-68-SS-1450.750
  - Who was measured: not applicable. State administrative regulation, not a survey.
  - Status: confirmed via direct fetch on 2026-09-26.
- **Claim:** "Failing to timely deposit escrow moneys, including earnest money, is its own
  independent ground for discipline under the Illinois Real Estate License Act, separate from
  any dispute over the deal itself."
  - Source: Illinois Real Estate License Act of 2000, 225 ILCS 454, section 20-20(a)(17)
    (FindLaw). https://codes.findlaw.com/il/chapter-225-professionsoccupations-and-business-operations/il-st-sect-225-454-20-20/
  - Status: confirmed via direct fetch on 2026-09-26.
- **Fabrication audit:** No enforcement action, fine amount, or named case is cited or implied,
  per the bank entry's flag to state the exposure and never predict the verdict. Both citations
  are current codified law, not a news article subject to going stale.

## AI Music Prompt

Not applicable. This is a static image carousel, not a video (see `docs/series/carousel-standard.md`,
"Music prompt: only if it ships as video").
