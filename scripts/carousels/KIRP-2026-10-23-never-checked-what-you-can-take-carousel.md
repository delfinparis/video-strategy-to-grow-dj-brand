---
lane: "evergreen"
source_script: "scripts/broker-problems/BP-026-never-checked-what-you-can-take.md"
carousel_for: "The ownership audit from BP-026: the business assets (database, listing photos, closing files, business-card contact info) an agent could actually take if they changed firms, and why almost nobody has ever checked which of it is actually theirs to take"
hook_family: "system-indictment"
heat: 4
slide_count: 5
goal: "engagement"
generated: "2026-10-23"
theme: "light"
---

# Carousel: never checked what you can take

Today's two rotation slots, per `data/carousel-topic-rotation.json`: `dont-make-this-mistake`
(unambiguous oldest, `last_used: 2026-10-20`) and `kirp-guest-tip` (tied at `last_used:
2026-10-21` with `market-tip`; see the companion deck,
`KIRP-2026-10-23-show-up-as-yourself-carousel.md`, for the tiebreak reasoning).

No news brief exists for 2026-10-23 or 2026-10-22 (the newest on disk is 2026-10-13, too stale
for Step 2(b)), and `data/news-briefs/stat-bank.json` referenced in the engine's source order no
longer exists in this repo (Step 2(c) unavailable). Fell to Step 2(d): the newest walk-and-talk
script committed in the last several days is
`scripts/broker-problems/BP-026-never-checked-what-you-can-take.md` (committed 2026-10-18), the
ownership-audit broker-problem script. Same facts, same sourcing, no new claims, per the
news-repurpose discipline in `docs/series/carousel-standard.md`. No firm, platform, product, or
person is named anywhere in the source script or on this deck, same as the source requires.

**The one idea:** almost no agent has ever checked which of their own business assets (database,
listing photography, closing files, the contact info on their own business cards) they could
actually take with them if they changed firms, because nobody at any brokerage is assigned to
walk them through it. The source script's own `Receipt: not needed` note holds here too: this is
a checklist, not a statistic, so no number is claimed or invented anywhere on this deck. Hook
family `system-indictment` (family 4), the same family the source script logged, since the
deck's whole point is the same one: point the friction at the arrangement, never at the agent.
Differs from the three most recently committed decks (`data-card`, `mirror`, `swap-list`) and
from today's companion `kirp-guest-tip` deck (`myth-bust`).

Checked `scripts/carousels/` for "never checked," "what you can take," and "ownership audit"
first -- no prior deck covers this angle.

---

## SLIDE 1 -- HOOK
**Headline:**
You've never checked **what** you can take.

**Subhead:**
Six things most agents have never actually audited.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Your database, your listing photos, and your closing files all sit on a system you don't own.

**Subhead:**
Almost nobody has ever checked which of it they could take with them.

---

## SLIDE 3 -- THE TURN
**Headline:**
The problem isn't that you'd lose it. It's that **you don't know.**

**Body:**
Whether you could export your contacts, your listing photography, or your closing files if you
left your brokerage depends on the firm, the platform, and what your own listing agreement
actually says. There's no answer that's true everywhere, and no one claim covers every agent.
What is true everywhere: almost nobody has ever checked, because nobody at any firm is assigned
to sit an agent down and walk them through it.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
The audit, so you're not finding out the hard way:

**Numbered list:**
1. **Your database.** Not just the names, the contact history, notes, and lead source. Names
   export more often than history does.
2. **Your listing photography.** Commissioning it isn't the same as owning the rights to it; the
   license usually runs to whoever paid the photographer.
3. **Your closing files and transaction archive.** The one nobody checks until a complaint lands
   years later and the login that held it stopped working.
4. **The phone number and email on every business card you've handed out.** The one almost every
   agent who's switched firms names first.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Find out what you can take before you need to, not after.

**Subhead:**
Ask the question now. The time to learn the answer is never during a move.

---

## Social Captions

### LinkedIn
Most agents have never checked which of their own database, listing photos, or closing files they could actually take with them.

### Instagram
You have never checked what you can take with you if you ever change firms, and that is the whole problem.

### Facebook
Nobody sits an agent down and explains what happens to their database or their files if they ever leave, so almost no one has checked.

---

## Data Source

**No statistic is claimed anywhere on this deck**, carried over from the source script's own
`stat_anchored: false`. There is no number on any slide beyond "six things" and "the fourth,"
neither of which is a measurement.

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| Most agents have never checked which business assets they can take with them | Yes, slides 1-3, as the viewer's own situation | `scripts/broker-problems/BP-026-never-checked-what-you-can-take.md`: second-person address, asserts nothing about any firm or any share of agents. Bank entry B2 (`data/brokerage-pain.md`) is marked `Receipt: not needed` with an explicit instruction not to invent a statistic about CRM export | Second-person address, not a population claim, same as the source |
| Contacts, listing photography, and closing files commonly sit on brokerage-provided systems | Yes, slides 2-4 | Structural premise from the source script, not a finding about any named firm | Premise, not receipt, same as the source |
| Any specific asset cannot be exported or taken | No, never | Nothing. Varies by firm, platform, agreement, and state; no universally true answer exists | Hard block, carried from the source. Slide 3 states the question is unanswerable in general, not that the answer is "no" |
| How many agents can export their database | No | Nothing. No source exists for this | Never added, same as the source |
| The name of any CRM, review platform, transaction platform, or MLS product | No, never | Each asset lives in named software in real life | Hard block, carried from the source |
| The fourth item (phone/email on business cards) | Yes, spoken on slide 4, unlike the source video, which withheld it as a comment-engine device | The source script's own pinned comment already names this item publicly, so printing it on a screenshot payload (whose job is to be a complete, self-contained reference, per `docs/series/carousel-standard.md`) does not disclose anything the source hasn't already made public | Deliberately included here. The video withholds it to engineer a comment; the carousel's job is a complete, savable checklist, so it's spoken |

**Do-not-cite check:** clean. No person, firm, franchise, platform, or product is named anywhere
in this file, matching the source script's own clean audit.

**Reuse note:** this deck repackages BP-026's angle (bank entry B2, angle 1) for the carousel
surface. It does not log a new entry in `data/brokerage-pain.md`; the source script already
carries that bookkeeping.
