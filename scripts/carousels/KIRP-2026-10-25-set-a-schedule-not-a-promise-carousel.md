---
lane: "dont-make-this-mistake"
carousel_for: "ST-0019 from data/stupid-things.md: promising a buyer or seller 'I'll let you know if anything comes up' instead of a standing update schedule, which turns the client into the one chasing the deal"
hook_family: "mirror"
heat: 2
slide_count: 5
goal: "engagement"
generated: "2026-10-25"
theme: "light"
---

# Carousel: set a schedule, not a promise

Today's companion deck, `KIRP-2026-10-25-steer-the-whole-market-carousel.md`, has the full
rotation note: `do-this-dont-do-that` was the clear oldest slot, and this slot's tie between
`dont-make-this-mistake` and `kirp-guest-tip` (both `last_used: 2026-10-23`) resolved to
`dont-make-this-mistake` after Step 2(a) surfaced that the only "unused" KIRP episode stem today,
`2026-10-20_item2_Anna-Kara`, is a pipeline duplicate of the already-consumed
`2026-10-20_item1_Anna-Kara` (identical transcript audio, confirmed by diff and by
`webapp/src/data/episodes.json` listing only one Anna Kara episode on that date). Flagged, not
built from.

Sourced from the Stupid Things bank the same way as the companion deck: today's and yesterday's
news briefs offer only ST-0001/ST-0014/ST-0017, all three already built into carousels; no
`stat-bank.json` exists in this repo; went to `python3 scripts/stupid_things.py pick --count 30
--stdout` and checked candidates against `scripts/carousels/`. ST-0019 ("I'll let you know if
anything comes up") came up clean -- not built as a script or a carousel, and distinct from the
two already-built "slow fade" entries this bank carries (ST-0014's post-closing silence and
ST-0017's pre-closing silence are about disappearing; ST-0019 is about a vague promise replacing
a concrete one, a different specific mistake even though it shares the "slow fade" tag). The
entry ships `receipt: NEEDS RECEIPT` in the bank, so no number is used anywhere on this deck --
per Rule 1, the mistake and the fix are stated as the scene and the swap, with nothing invented to
decorate them.

**The one idea:** "I'll let you know if anything comes up" sounds considerate and functions as
the opposite -- it hands the client the job of monitoring the deal, so they end up texting the
agent for the update the agent never promised a time for. The fix is a standing schedule specific
enough that the client never has to ask. Hook family `mirror` (opening on the agent's own line,
said back to them, so the recognition lands before any argument does), differing from today's
companion deck (`myth-bust`) and from the two most recently committed decks before today
(`data-card`, `swap-list`, both 2026-10-24).

Checked `scripts/carousels/` for "I'll let you know," "status update," and "set a schedule" first
-- no prior deck covers this angle. (Two other decks cover adjacent but distinct mistakes:
`KIRP-2026-09-24-after-closing-silence-carousel.md` is about going quiet after the deal closes,
and `KIRP-2026-10-11-the-week-before-closing-silence-carousel.md` is about going quiet the final
week. Neither is about the vague promise itself, which is this deck's one idea.)

---

## SLIDE 1 -- HOOK
**Headline:**
"**I'll** let you know if anything comes up."

**Subhead:**
That sentence just told your client they're on their own.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
If your buyer is the one texting you for updates, you built that.

**Subhead:**
The passive promise sounds proactive. It's the opposite.

---

## SLIDE 3 -- THE TURN
**Headline:**
A vague promise turns your client into an unpaid project manager.

**Body:**
The moment you say "I'll let you know if anything comes up," the client stops waiting and starts
chasing: any word from the inspector, did the appraisal come in, what's happening with the
survey. They hired you to carry that, not to monitor it from the outside. The fix isn't a warmer
version of the same promise. It's a schedule specific enough that they never have to ask.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Replace the promise with a schedule:

**Numbered list:**
1. **Set a standing day and time.** "Every Friday by noon, you get a status update, even if
   nothing changed."
2. **Promise the exception separately.** "Anything material, you hear it from me first, not on
   Friday."
3. **Name the goal out loud.** The goal is that your client never has to type the words "any
   update?"

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
A schedule beats a promise, every time.

**Subhead:**
Say exactly when they'll hear from you. Then be early.

---

## Social Captions

### LinkedIn
"I'll let you know if anything comes up" is the line that turns your client into the one chasing updates.

### Instagram
If your client is the one texting you for the update, the vague promise did that, not them.

### Facebook
Replace "I'll let you know if anything comes up" with a standing day and time, and your client stops chasing you for news.

---

## Data Source

**No statistic is claimed anywhere in this deck.** The bank entry (`data/stupid-things.md`,
ST-0019) ships `receipt: NEEDS RECEIPT`, and per Rule 1 and the Stupid Things standard, an
unsourced figure gets dropped or the angle gets built without one rather than softened into a
plausible-sounding number. This deck does the latter: the mistake and the fix are both stated as
scene and swap, with no number anywhere in the slides, captions, or this file.

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| A client left with "I'll let you know if anything comes up" ends up initiating the update requests themselves | Yes, slides 1-3, as the scene | Nothing quantified. This is the bank entry's premise, stated in the second person about a familiar pattern, not a measured claim about any population | Scene, not statistic. Asserts nothing about how many agents do this or how often |
| The payload steps (standing schedule, separate exception promise, the no-update-request goal) | Yes, slide 4 | Editorial recommendation, directly extending the bank entry's own "swap" language ("every Friday by noon... even if it's nothing changed... anything material, you hear it from me first") | Commentary, not a statistic |

**Do-not-cite check:** clean. No agent, firm, platform, or brokerage is named anywhere in this
file.

**Reuse note:** this deck repurposes `data/stupid-things.md` entry ST-0019 for the carousel
surface. No walk-and-talk script exists yet under `scripts/stupid-things/` for this entry; this
carousel does not require that one does.
