---
lane: "evergreen"
carousel_for: "The dont-make-this-mistake rotation slot: Stupid Things bank ST-0004, a listing agent who personally decides a buyer's offer is too weak to bother forwarding to the seller"
hook_family: "one-tactic-breakdown"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-11-25"
reskinned_from: "KIRP-2026-11-25-the-offer-you-never-sent-carousel"
---

# Carousel: the offer that never made it to the seller

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`dont-make-this-mistake` (`last_used: 2026-11-22`), built here. The second-oldest ties at
`last_used: 2026-11-23` between `stat` and `kirp-guest-tip`; resolved to `stat` (first-listed of
the tie in the rotation file's `topics` array, the same tie-break convention the 2026-11-24 run
documented), built as the companion deck, `KIRP-2026-11-25-the-portal-is-getting-quieter-carousel.md`.
`kirp-guest-tip` stays at `last_used: 2026-11-23` for the next run.

Sourced per Step 2(d) via `python3 scripts/stupid_things.py pick --count 40 --stdout`, then
checked every candidate's ST code against `scripts/carousels/*.md` (by `carousel_for`, the field
that actually names a deck's built topic, not an incidental mention) and `scripts/stupid-things/*.md`.
The first several candidates in pick order are already built: ST-0001 (`KIRP-2026-11-21-overprice-listing-swap-carousel.md`),
ST-0014 (`KIRP-2026-11-12-the-rehire-gap-carousel.md`), ST-0017 (`KIRP-2026-09-18-closing-week-silence-carousel.md`),
ST-0056 (`KR-2026-09-24-neighborhood-knowledge-carousel.md`), ST-0010 (`KIRP-2026-09-17-material-fact-disclosure-carousel.md`),
ST-0052 (`KIRP-2026-09-14-kickback-disclosure-carousel.md`), ST-0005 (`KIRP-2026-10-27-phone-shot-listing-photos-carousel.md`).
ST-0057 (wildly wrong price estimates) was skipped on purpose: its banked receipt (Relitix via
Inman) is about new-agent survival and zero-closing rates, not price accuracy -- a mismatched
receipt, not a usable one, and the same reason `KIRP-2026-09-28-dont-talk-them-out-of-their-own-agent-carousel.md`
passed on it in September. **ST-0004** ("Deciding an offer is too weak to bother presenting to
the seller") is the first candidate with zero prior hits and a clean, unmismatched `receipt:
needed` status.

**The one idea:** presenting an offer to the seller is not the listing agent's judgment call to
make. The agent who privately decides a number isn't worth the seller's time has made the
seller's decision for them, and the seller never finds out it happened.

ST-0004 ships `receipt: needed` in `data/stupid-things.json` on purpose, with no sourced number
attached. Per Rule 1's qualitative fallback, no invented figure appears on this deck. Checked
both of the bank entry's sightings before using either: Pinnacle Real Estate Academy's "Failing
to Present Offers" section (fetched directly today, revised October 16, 2026) states plainly
"Agents are expected to present all written offers to their clients," filed under a section on
negligence allegations against agents -- usable as a named, dated source for the qualitative
claim that follows. CRES Insurance's list of complaints that lead to litigation does not name
offer presentation specifically (its closest item is "multiple offers," a different claim), so
it is not cited here. No number is spoken; the duty itself is the argument.

Hook family `one-tactic-breakdown` (the single fix -- forward every offer within the hour),
differing from today's companion deck (`data-card`) and from the two most recently committed
decks before today (`swap-list` and `listicle-scripts`, both `2026-11-24`).

Target: `sideways` -- the agent on the other side of the deal, not the viewer. No `kirp_guest`
field -- no named individual is quoted, so this is not flagged, and it reskins to KR cleanly per
`docs/automation/daily-carousel-engine.md`.

---

## SLIDE 1 -- HOOK
**Headline:**
That offer was never yours to kill.

**Subhead:**
You decided it wasn't worth forwarding. The seller never knew it existed.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
A buyer's agent sent a real, signed offer. The listing agent read the number and never told anyone.

**Subhead:**
Weeks later the seller finds out, from the buyer's agent, not from you.

---

## SLIDE 3 -- THE TURN

**Headline:**
Presenting the offer isn't your opinion to withhold. It's the seller's decision to make.

**Body:**
You are allowed to think a number is low. You are not allowed to decide, on the seller's behalf,
that it's too low to see. Every written offer goes to the seller, full stop. Your read on it is
useful information, not a gate. Sit on it and the seller loses a real buyer they never got to
weigh in on, and you've made their call for them without telling them you made it.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
The fix:

**Numbered list:**
1. **Forward every written offer within the hour, no exceptions.** Weak, strong, insulting, it
   doesn't matter. The seller sees it, not your filtered version of it.
2. **Put your opinion under the offer, never instead of it.** "Here's the offer. My take: it's
   light, here's why, here's what I'd counter." The seller still makes the call.
3. **Say it out loud at the listing appointment, before any offer arrives.** "Every offer that
   comes in, you see it, same day. That's not negotiable on my end."

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Next offer that lands on your desk, forward it before you form an opinion about it.

---

## Data Source

No sourced statistic appears on this deck. The practice (a listing agent unilaterally deciding
an offer is too weak to present) and the fix (forward every written offer within the hour, put
opinion underneath it, state the policy up front) are drawn from `data/stupid-things.json` entry
**ST-0004**, built per the Rule 1 qualitative fallback: the bank entry ships `receipt: needed` by
design.

- **"Agents are expected to present all written offers to their clients," filed under negligence
  allegations against agents** (background context for the slide copy above, not spoken as a
  number on any slide)
  - Source: Pinnacle Real Estate Academy, "The Most Common Complaint Filed Against Real Estate
    Agents," originally published August 8, 2023, revised October 16, 2026 --
    https://pinnaclerealestateacademy.com/the-most-common-complaint-filed-against-real-estate-agents
  - Who was measured: not a survey; a real-estate-licensing-education publisher's own guidance
  - Status: confirmed, fetched directly today
  - Note: CRES Insurance's complaint-litigation list (the bank entry's other sighting) does not
    name offer presentation specifically and is not cited here.

**No guest tag needed.** No named individual is quoted on this deck.

## Social Captions

_Written fresh for the Kale re-skin per `docs/automation/daily-carousel-engine.md`: not carried
over from the KIRP deck. Zero hashtags on LinkedIn, Instagram and Facebook per the current
one-sentence caption rule (CLAUDE.md, superseding the older 3-5 hashtag spec for these three
platforms)._

### LinkedIn
If your brokerage never told you offer presentation isn't your call to make, that's a gap worth asking about.

### Instagram
Deciding an offer's too weak to show your seller is a decision that was never yours to make alone.

### Facebook
Chicago agents, if nobody at your brokerage ever walked you through what you owe a seller on every offer, ask why.
