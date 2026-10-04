---
lane: "do-this-dont-do-that"
carousel_for: "Stop talking buyers past the number they set when they were calm"
hook_family: "mirror"
heat: 3
slide_count: 5
goal: "engagement"
generated: "2026-10-04"
theme: "dark"
---

# Carousel: Anchor to their calm number

Today's two oldest rotation slots (`data/carousel-topic-rotation.json`): `do-this-dont-do-that`
is unambiguously oldest at `last_used: 2026-10-01`. `stat` and `dont-make-this-mistake` are tied
next at `last_used: 2026-10-02`; `stat` wins the tie because it is listed before
`dont-make-this-mistake` in the rotation file's `topics` array (same array-order tiebreak
precedent used in the 2026-10-02 and 2026-09-15 builds). `kirp-guest-tip` is not today's slot, so
both KIRP decks reskin to KR normally and no fresh KR topic is needed today.

Sourced per Step 2(a)/(d): `python3 scripts/stupid_things.py pick --count 15 --stdout`, option
14, `ST-0047`, "Pushing buyers to bid above the number they set when they were calm." Checked
first: no existing carousel references "manufactured pressure," "comfort line," or talking a
buyer past their own ceiling (grep across `scripts/carousels/*.md` for "manufactured pressure,"
"bid above," "calm number" returned nothing). The bank entry ships `receipt: NEEDS RECEIPT`.
No number is sourced for this practice and none is invented: the deck runs entirely on
qualitative framing ("the real math," "house poor") per Rule 1's qualitative fallback, with zero
percentage, dollar figure, or specific count claimed anywhere in the copy.

**The one idea:** the agent who talks a buyer fifteen or twenty thousand dollars past their own
calm ceiling isn't doing them a favor, because a bigger winning bid also means a bigger
commission, and that conflict never gets named out loud. Rule 0 criterion 6, permission slip (it
is okay to tell a buyer to walk, and it is okay to lose the deal), and criterion 2, contrarian
take (agents are trained to close the gap, not to anchor against their own interest). Hook family
`mirror` (the viewer sees their own script coming out of someone else's mouth), differing from
today's companion `stat` deck (`data-card`) and from the most recently committed carousel
(`swap-and-list`, `KIRP-2026-10-03-closing-cost-credit-stack-carousel.md`).

---

## SLIDE 1 -- HOOK
**Headline:**
You talked them into a number they regret.

**Subhead:**
The push happens in escrow. The house-poor part shows up eight months later.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
"It's only twenty bucks a month" is not the real math.

**Subhead:**
It skips the part where the tax bill resets to match the higher price you just talked them into.

---

## SLIDE 3 -- THE TURN
**Headline:**
The bigger number pays you more too.

**Body:**
A buyer sets a ceiling when they're calm. Three lost offers later, exhausted, they'll agree to
almost anything you suggest. When you talk them from their number up to the next one, you didn't
just win them the house. You raised your own commission on the same call. Nobody says that part
out loud, and it's the real reason "it's only twenty bucks a month" keeps coming out of agents'
mouths.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Before you push past their number, do this:

**Numbered list:**
1. **Run the real payment, taxes included, at both prices.** The twenty-dollar line never
   mentions the reassessment that follows a higher sale.
2. **Anchor to the number they set when they were calm.** Not the one they'll agree to after
   three lost offers and no sleep.
3. **Say the sentence that can cost you the deal.** "This one's over your comfort line. There
   will be another."

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Anchor to their calm number, not their tired one.

**Subhead:**
The deal you talk them out of is the one they thank you for in a year.

---

## Social Captions

### LinkedIn (PRIMARY)
A buyer sets a number when they're calm. Three lost offers later, exhausted, they'll agree to
almost anything you suggest. When you talk them past their own ceiling, you didn't just help them
win. You raised your own commission on the same call.

Run the real payment, taxes included, at both prices before you push. Anchor to the number they
set when they were calm, not the one they'll accept when they're tired. Then say the sentence
most agents won't: this one's over your comfort line, there will be another.

The deal you talk a buyer out of is the one they thank you for in a year.

#RealEstateAgents #RealtorTips #BuyersAgent #KeepingItRealPodcast

### Instagram
Three lost offers in, a buyer will agree to almost anything you suggest. Run the real payment
with taxes before you push past their number, and anchor to the ceiling they set when they were
calm, not the one they'll accept when they're exhausted.

#RealEstateAgents #RealtorTips #BuyersAgent

### Facebook
Before you talk a buyer past their own number, run the real payment with taxes included. Anchor
to what they said when they were calm, not what they'll agree to when they're tired.

#RealEstateAgents #RealtorTips

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-10-04-anchor-the-calm-number-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Dark theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. This is an open deck. No keyword, no ManyChat flow, no ask on any platform.

**LinkedIn first comment:** https://joinkale.com/?src=carousel-kirp-2026-10-04-anchor-the-calm-number-carousel

**Pinned first comment (IG and FB):** "The sentence that costs you the deal and earns the
referral: 'This one's over your comfort line. There will be another.'"

---

## Data Source

- **Claim:** "An agent who talks a buyer past the number they set when calm is also raising their
  own commission on the same call, and that conflict is rarely named."
  - Status: editorial framing, not a statistic. This is the bank entry's own stated angle
    (`data/stupid-things.md` / `data/stupid-things.json`, ST-0047, "Manufactured pressure"),
    reasoned from how commission math works, not a claim requiring a named external source under
    Rule 1. No percentage, dollar figure, or specific count appears anywhere in this deck's copy.
  - Provenance note: ST-0047 ships `receipt: NEEDS RECEIPT` in the bank. Per the bank's own flag,
    no sourced number exists yet for this practice, so none is used. The "$520" / "$540" / "fifteen
    grand" figures in the bank's own Act 2 scene are illustrative scaffolding for the bank card,
    not script copy, and none of them appear on any slide in this deck.
  - Fabrication audit: no number invented, rounded, or borrowed. Nothing in this deck needs
    re-verification because nothing in it is a sourced statistic.
