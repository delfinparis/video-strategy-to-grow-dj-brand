---
lane: "evergreen"
carousel_for: "KR-exclusive fresh topic, built because today's kirp-guest-tip deck does not translate: the dont-make-this-mistake angle on negotiating a deal entirely by text and refusing to get on the phone (Stupid Things bank ST-0022), and the swap (call for anything with a number attached, text only to confirm what the call settled)"
hook_family: "swap-list"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-11-26"
---

# Carousel: the call you won't make

Today's `kirp-guest-tip` deck (`KIRP-2026-11-26-ai-cant-recommend-you-carousel.md`) carries a
named guest (Kevin McCarthy, Real Geeks), so per `docs/automation/daily-carousel-engine.md` it
does not translate to Kale. This is the fresh KR-only topic authored in its place, so two KR
decks ship today regardless.

Sourced per Step 2(d): `python3 scripts/stupid_things.py pick --count 40 --stdout`, then checked
every candidate's ST code against `scripts/carousels/*.md` (by `carousel_for`, not an incidental
mention). The first many candidates in pick order are already built: ST-0001, ST-0014, ST-0017,
ST-0056, ST-0010, ST-0052 (all built well before today), ST-0037, ST-0051, ST-0019, ST-0015,
ST-0012, ST-0007, ST-0002 (all previously built, confirmed by the grep above).
**ST-0022** ("Only texting during negotiations and refusing to get on the phone") is the first
candidate in pick order with zero prior hits.

**The one idea:** text strips tone. A firm "no" typed out reads as rude; a real concession reads
as weak. The agent on the other end fills in whatever blank suits them, because they can't hear
hesitation, urgency, or how firm you actually are. A phone call closes that gap in real time. The
agents who consistently win a contested negotiation are the ones willing to make the call instead
of hiding behind a thread of texts.

ST-0022 ships `receipt: needed` in `data/stupid-things.json` on purpose, with no sourced number
attached. Per Rule 1's qualitative fallback, no invented figure appears on this deck. No number is
spoken; the mechanism (tone doesn't survive text, and the agents who win do it on the phone) is
the argument.

Hook family `swap-list` (text for logistics, call for leverage), differing from today's companion
deck (`myth-bust`) and from the two most recently committed decks before today
(`KIRP-2026-11-25-the-offer-you-never-sent-carousel.md`: `one-tactic-breakdown`;
`KIRP-2026-11-25-the-portal-is-getting-quieter-carousel.md`: `data-card`).

Target: `sideways` -- the agent on the other side of the deal, not the viewer.

---

## SLIDE 1 -- HOOK
**Headline:**
Real negotiations don't happen by **text.**

**Subhead:**
The agents who win contested deals still pick up the phone.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
An agent who negotiates an entire deal by text is hiding from the hardest part of the job.

**Subhead:**
Tone, urgency, and how firm you actually are don't survive being typed out.

---

## SLIDE 3 -- THE TURN

**Headline:**
Text is for logistics. **Calls** are for leverage.

**Body:**
A typed "no" reads as rude. A typed concession reads as weak. Either way, the agent on the other
end fills in the blank with whatever assumption suits them, because text gives them nothing else
to go on. A phone call lets you hear hesitation, push back in the moment, and close a gap in one
conversation instead of across six text bubbles over two days. The agents who consistently win a
contested negotiation are the ones willing to make the uncomfortable call.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
The swap:

**Numbered list:**
1. **Call for anything with a number attached.** Price, repair credit, closing date, any ask
   that's actually negotiable gets a phone call, not a paragraph.
2. **Text only to confirm what the call already settled.** "Per our call, seller agrees to a
   $4,000 credit, closing moves to the 15th." Text documents the deal. It doesn't make the deal.
3. **If the other agent won't pick up, say so in writing.** "Per my voicemail and text at 2pm,
   following up here" protects your client and still leaves the door open for them to call back.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Next time a number's on the table, call before you type.

---

## Social Captions

_Written fresh for this Kale-exclusive topic per `docs/automation/daily-carousel-engine.md`.
Zero hashtags on LinkedIn, Instagram and Facebook per the current one-sentence caption rule
(CLAUDE.md)._

### LinkedIn
If nobody ever taught you how to negotiate on the phone, you're not bad at it, you were never trained.

### Instagram
An agent who negotiates entirely by text isn't being efficient, they're avoiding the part of the job that takes real skill.

### Facebook
Chicago agents, if every negotiation you've won happened over text, ask how many you lost before you ever called.

---

## Data Source

No sourced statistic appears on this deck. The practice (negotiating an entire deal by text and
refusing to get on the phone) and the fix (call for anything with a number attached, text only to
confirm what the call settled, document in writing when the other side won't answer) are drawn
from `data/stupid-things.json` entry **ST-0022**, built per the Rule 1 qualitative fallback: the
bank entry ships `receipt: needed` by design.
