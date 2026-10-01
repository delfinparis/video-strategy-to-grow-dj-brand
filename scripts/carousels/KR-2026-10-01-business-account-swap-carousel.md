---
lane: "evergreen"
carousel_for: "Your commission account is hiding whether your business actually makes money"
hook_family: "mirror"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-10-01"
reskinned_from: "KIRP-2026-10-01-business-account-swap-carousel"
heat: "1.5"
---

# Carousel: The business account swap

Do-this-dont-do-that deck. `data/carousel-topic-rotation.json` had `do-this-dont-do-that` as the
unambiguous oldest slot (`last_used: 2026-09-28`), ahead of `market-tip` and
`dont-make-this-mistake` (tied at `2026-09-29`) and `stat` / `kirp-guest-tip` (tied at
`2026-09-30`). `market-tip` wins the tie for today's second slot because it is listed first of
the two in the rotation file's `topics` array (same array-order tiebreak used on prior runs).
`kirp-guest-tip` is not today's slot, so both decks reskin to KR normally; no fresh KR topic
needed.

Sourced per Step 2(d): `scripts/stupid-things/STUPID-029-your-commission-goes-into-your-personal-account.md`,
committed this week, status draft, not yet built as a carousel (checked: no existing carousel
file references "business checking," "personal account," or "commingling"). The source script's
Data Source attributes the underlying premise to a named Keeping It Real guest's on-air comment.
This deck does not carry that name or quote forward -- the premise itself (mixing personal and
business money hides whether a business is profitable) is standard small-business accounting
practice, not a claim that needs a citation, and leaving the guest's name and words out of a
deck that isn't built via `kirp_source.py` avoids the exact failure `kirp_guest` exists to catch:
a named person's material surfacing in a deck that might get mistaken for guest content. No
statistic is used anywhere in this deck, so there is no number to round, source, or fabricate.
`kirp_guest` is correctly **not** set.

**The one idea:** one bank account for both the business and the household means there is no
clean answer to "did this business make money this year." Rule 0 criterion 1, tactical
specificity (the exact three-step fix), and criterion 6, permission slip (agents who've been
avoiding this can just do it this week, no judgment). Hook family `mirror` (Family 1: a private
behavior almost every agent recognizes in their own banking app), differing from today's paired
deck (`named-stakes`) and from the most recently committed carousels
(`swap-list`, `KR-2026-09-30-four-minute-reply-carousel.md`; `named-stakes`,
`KIRP-2026-09-30-gig-worker-prediction-carousel.md`; `data-card`,
`KIRP-2026-09-30-rate-lockin-reversal-carousel.md`).

---

## SLIDE 1 -- HOOK
**Headline:**
One bank account is hiding your profit.

**Subhead:**
Mix personal and business money and there's no clean answer to "did I make money this year."

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
You can't tell if your business actually makes money.

**Subhead:**
Not because you're bad at math. Because the mortgage, the groceries, and the commission all hit
the same account.

---

## SLIDE 3 -- THE TURN
**Headline:**
Commingling isn't a shortcut. It's a blind spot.

**Body:**
When every commission and every personal expense pass through one account, nothing separates
what the business earned from what the household spent. Every decision about marketing, splits,
or hiring help becomes a guess instead of a number. At tax time, the only tool left is a
highlighter and a year of bank statements.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What changes this week:

**Numbered list:**
1. **Open a separate business checking account.** Every commission goes in. Nothing else does.
2. **Pay every business cost from that account**, not your personal one. Marketing, mileage,
   software, all of it.
3. **Pay yourself on the same day every month**, like a paycheck, and ask a CPA whether an LLC
   makes sense for you.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Open the account before your next commission check.

**Subhead:**
That's the day you'll finally know what you actually make.

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-10-01-business-account-swap-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Dark theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. This is an open deck. No keyword, no ManyChat flow, no ask on any platform.

**LinkedIn first comment:** https://joinkale.com/?src=carousel-kirp-2026-10-01-business-account-swap-carousel

**Pinned first comment (IG and FB):** "The three steps: separate business checking account,
every commission in and every cost out, pay yourself on a set day. Ask a CPA about an LLC."

---

## Data Source

- **Claim:** "Mixing personal and business money hides whether a business is profitable, and
  makes marketing, hiring, and tax-time decisions guesses instead of calculations."
  - Status: editorial framing, not a statistic. This is standard small-business accounting
    practice (the case for separate business and personal accounts), not a claim requiring a
    named external source under Rule 1. No percentage, dollar figure, or specific number appears
    anywhere in this deck's copy.
  - Fabrication audit: no number invented, rounded, or borrowed. Nothing in this deck needs
    re-verification because nothing in it is a sourced fact.

## Social Captions

### LinkedIn (PRIMARY)
If your commission and your mortgage payment come out of the same account, you can't actually
answer "did my business make money this year." Every marketing dollar, every hire, every split
decision turns into a guess instead of a number you can check.

The brokerage you're at should be the one telling you this before tax season does. A separate
business account, every commission in and every cost out, paid to yourself on a set day. It's a
five minute setup that tells you more about your business than most agents learn in a year.

Learn more at joinkale.com

#RealEstateAgents #RealEstateBusiness #ChicagoRealEstate #KaleRealty

### Instagram
You can't tell if your business makes money when the mortgage and the commission hit the same
account. A separate business account fixes it in a week, not a quarter.

Learn more at joinkale.com

#RealEstateAgents #RealEstateBusiness #ChicagoRealEstate

### Facebook
One account for business and personal money means you can't tell what your business actually
earns. Open a separate account, run every commission and cost through it, and know your number.

Learn more at joinkale.com

#RealEstateAgents #ChicagoRealEstate
