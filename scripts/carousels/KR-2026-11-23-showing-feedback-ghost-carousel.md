---
lane: "evergreen"
carousel_for: "KR-exclusive fresh topic, built because today's kirp-guest-tip deck does not translate: the do-this-dont-do-that swap on showing feedback (Stupid Things bank ST-0020), going silent on a listing agent's feedback request versus a 24-hour reply with a saved three-blank template"
hook_family: "listicle-scripts"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-11-23"
---

# Carousel: twelve showings, zero replies

Today's `kirp-guest-tip` deck (`KIRP-2026-11-23-copy-the-system-carousel.md`) carries a named
guest's own words, so `reskin_kr.py` exits 2 and does not translate (`kirp_guest: true`). Per
`docs/automation/daily-carousel-engine.md`, a fresh KR-only topic is authored instead, so two KR
decks still ship today.

Sourced per Step 2(d), the Stupid Things bank: `python3 scripts/stupid_things.py pick --count 40
--stdout`, then checked every candidate's ST code against `scripts/carousels/*.md`,
`scripts/stupid-things/*.md`, and `scripts/gbp/*.md` (52 codes already in use across those three
folders). The first candidate in pick order with zero prior hits is **ST-0020** ("not replying to
showing feedback requests").

**The one idea:** a listing agent sends a feedback request after every showing and most of them
go unanswered, which leaves the seller guessing at the price, the kitchen, or the smell with no
real information, while the buyer's agent who could answer in one sentence says nothing. ST-0020
ships `receipt: NEEDS RECEIPT` in `data/stupid-things.md` by design ("no sourced number yet...
never write a hook that implies a figure nobody has checked"), so per Rule 1's qualitative
fallback this deck carries no invented statistic. The mechanism (the reply gap, and the 24-hour
fix) is argued directly.

**Target: sideways.** The entry is tagged `target: sideways` in the bank -- the audience is the
listing agent who sent the request and got silence, not the agent being asked to change. The
behavior named belongs to the agent on the other side of the showing, never the viewer.

Hook family `listicle-scripts` (the swap: what you do instead, with a saved template), differing
from today's two KIRP decks (`pov-relatable`, `myth-bust`) and from today's companion KR deck
(`myth-bust`, inherited from its KIRP source).

A Kale-branded deck built from scratch, so `byline: "none"` and `series_mark: "KALE REALTY"` are
set from the start rather than stripped by the reskin script.

---

## SLIDE 1 -- HOOK
**Headline:**
Twelve showings. **Zero** feedback replies.

**Subhead:**
Your seller is spiraling over a question only the buyer's agent can answer.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
A dozen showings, and not one agent hit reply.

**Subhead:**
The seller is guessing at the price, the kitchen, the smell. Somebody out there already knows.

---

## SLIDE 3 -- THE TURN
**Headline:**
Feedback isn't a favor. It's **the job.**

**Body:**
The showing agent already has the answer in their head: loved it but overpriced, smaller than
the listing photos made it look, dated kitchen, whatever it was. Saying nothing costs them
nothing and costs the seller real information. A reply inside 24 hours, even a flat "no strong
reaction," turns a guessing game back into a plan. It takes less than a minute once you've got
the habit built.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
The swap:

**Numbered list:**
1. **Reply within 24 hours, every time.** Even "nothing stood out" is more than silence.
2. **Save a three-blank template.** Overall reaction, dealbreaker if any, price reaction. Fill it
   in under a minute per showing.
3. **Say what you'd actually tell a friend.** Not "they'll think about it." The real reaction.
4. **Treat it as the courtesy you want back.** The next ghosted feedback request could be on
   your own listing.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Open your last five showings and reply to whichever ones are still sitting unanswered.

---

## Social Captions

_Written fresh for this Kale-exclusive deck, built because today's kirp-guest-tip topic does not
translate. Zero hashtags on LinkedIn, Instagram and Facebook per the current one-sentence caption
rule (CLAUDE.md)._

### LinkedIn
If nobody ever told you a 24-hour feedback reply is part of the job, that's a training gap, not a personality flaw.

### Instagram
Twelve showings, zero replies, and a seller losing their mind over a question any buyer's agent could answer in one sentence.

### Facebook
Chicago agents, a seller spiraling over unanswered showing feedback is usually a training gap at their agent's brokerage, not a mystery.

---

## Data Source

No sourced statistic appears on this deck. The mechanism (unanswered feedback requests leaving
sellers without real information, and the 24-hour-reply fix) is drawn from `data/stupid-things.md`
entry **ST-0020**, built per the Rule 1 fallback: the bank entry ships `receipt: NEEDS RECEIPT`
by design, flagged "no sourced number yet... never write a hook that implies a figure nobody has
checked." The mechanism is argued directly, with no invented number.

**No guest tag needed.** No named individual is quoted on this deck.
