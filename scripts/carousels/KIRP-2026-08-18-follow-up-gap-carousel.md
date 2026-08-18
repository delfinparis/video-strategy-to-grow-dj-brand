---
lane: "market-tip"
carousel_for: "The follow-up gap: why top producers aren't more talented, just harder to shake off"
hook_family: "myth-bust"
heat: 1.5
slide_count: 5
goal: "engagement"
generated: "2026-08-18"
theme: "light"
---

# Carousel: The follow-up gap

Market-tip deck. Today's rotation gave `stat` as oldest (last used 2026-08-14), but that topic
is still unsourceable in this cloud session: the only evergreen stat visible here is the NAR
2026 Member Profile affordability figure from `data/news-briefs/2026-08-16.md`, and that exact
figure already ran on the 2026-08-15 GBP card. No 2026-08-17 or 2026-08-18 news brief exists to
supply a fresh one, and the live stat-bank file (`data/news-briefs/stat-bank.json`) is
gitignored and generated on D.J.'s home Mac, invisible to this session. `stat` is skipped again
and named here, not built.

Next-oldest after `stat` were `market-tip` and `kirp-guest-tip`, tied at 2026-08-16.
`kirp-guest-tip` was also tried and skipped: `scripts/kirp_source.py` returned
`2026-08-11_item2_Austin-Clarence`, then `2026-08-05_item2_Sam-Burke`, then
`2026-08-05_item3_Sam-Burke` in successive runs. Comparing each against its `item1` sibling in
`keeping-it-real-content-system/data/analysis/`, the `itemN` files for both guests are
near-identical re-analyses of the same recording (same quotes to the second, same timestamps,
same tactics, `analyzed_at` dates days apart), not distinct episode segments. Austin Clarence
and Sam Burke each already have a KIRP carousel in this repo. Building a third pass on either
guest's identical material would republish an already-credited episode under a "new" label,
which risks the guest relationship the format exists to protect. All three duplicate stems are
now marked used in `data/kirp-carousel-state.json` so the picker will not offer them again; the
underlying duplicate-analysis-file bug in the KIR archive needs a fix on the analysis side, not
a workaround here. `kirp-guest-tip` is skipped and named for today.

Falls to `market-tip`, source (d): `scripts/inside-the-industry/IS-005-the-follow-up-gap.md`
(committed 2026-08-15, walk-and-talk script under `scripts/`). Same facts, same sourcing as the
aired script. No new claims, no new numbers. Hook family `myth-bust` ("you don't have a lead
problem, you have a follow-up problem" is the reframe the source script already runs on).
Light theme. Not a guest deck; no `kirp_guest` field, no `guest_photo`.

---

## SLIDE 1 -- HOOK
**Headline:**
You don't have a lead problem.

**Subhead:**
You have a follow-up problem. Here's the fix.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
That lead you filed under dead isn't dead.

**Subhead:**
You just stopped texting them.

---

## SLIDE 3 -- THE TURN
**Headline:**
It was never about **talent.**

**Body:**
After 700 Keeping It Real interviews, the pattern holds across every top producer: they aren't
more gifted, they just keep following up long after everyone else quietly gives up. A
fifty-million-dollar producer still answers her own phone. Another built his whole business on
staying in touch, not new leads. None of it is a tactic. It's a refusal to disappear.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Do this before the day ends:

**Numbered list:**
1. **Pull up your phone.** Find five people you messaged once and never circled back on.
2. **Write one real note to each.** Not a blast, not a pitch. "Thought of you, hope you're well."
3. **Send all five today.** Before you talk yourself into waiting for a better moment.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
The leads are already in your phone. You just have to **text them.**

**Subhead:**
Five notes, sent today, is the whole play.

---

## Social Captions

### LinkedIn (PRIMARY)
You don't have a lead problem. You have a follow-up problem.

After 700 Keeping It Real interviews, the gap between top producers and everyone else isn't
talent. It's that they keep following up long after the rest of us would have quit.

You get a lead, reach out once or twice, hear nothing, and quietly file that person under dead.
They aren't dead. You just stopped.

Find five people you messaged once and never circled back on. Send each one a real note today.
Not a blast. A note.

Learn more at joinkale.com

#RealEstateAgents #TopProducer #KeepingItRealPodcast

### Instagram
700 interviews taught me one thing: top producers aren't more talented. They just don't stop
texting.

That lead you filed under dead? Still in your phone. Still waiting.

Slide 4 has the exact move for today.

Learn more at joinkale.com

#RealEstateAgents #RealtorLife #ChicagoRealEstate

### Facebook
The gap between top producers and everyone else isn't talent. It's that they keep following up
long after the rest of us quit. Find five people you messaged once and never circled back on.
Send each a real note today.

Learn more at joinkale.com

#RealEstateAgents #RealtorLife

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-08-18-follow-up-gap-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Light theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. Open deck. No keyword, no ManyChat flow, no ask on any platform.

**LinkedIn first comment:** https://joinkale.com/?src=carousel-kirp-2026-08-18-follow-up-gap-carousel

**Pinned first comment (IG and FB):** The exact note, word for word: "Thought of you. Hope
you're well."

---

## Data Source

- **Claim:** "I've never practiced real estate. But I've interviewed over 700 agents who have."
  - Source: Protected voice signature (editorial-standards Rule 6). Keeping It Real Podcast,
    2015-2026, 700+ episodes. Carried forward from `IS-005-the-follow-up-gap.md` verbatim, not
    re-derived.
  - Status: confirmed

- **Claim:** "A fifty-million-dollar producer still answers her own phone."
  - Source: D.J. Paris direct observation, Keeping It Real Podcast (KIR 2026-01-22), Kristee
    Leonard. Same attribution used in `IS-001`, `IS-002`, and `IS-005`.
  - Status: confirmed

- **Claim:** "Another built his whole business on staying in touch, not new leads."
  - Source: D.J. Paris direct observation, Keeping It Real Podcast (KIR 2025-11-26), Garrett
    Maroon. Same attribution used in `IS-001`, `IS-004`, and `IS-005`. `IS-005`'s own Data
    Source flags this guest as documented on relationship-as-business specifically, not
    follow-up cadence in isolation; kept here in the same qualitative form the source script
    already uses.
  - Status: confirmed (relationship-as-business pattern)

- **Claim:** "None of it is a tactic. It's a refusal to disappear." (the central pattern)
  - Source: Synthesis across 700+ KIR interviews, per `IS-005-the-follow-up-gap.md`'s own Data
    Source block. Framed qualitatively per Rule 1. No specific interview count claimed beyond
    the protected voice signature above.
  - Status: confirmed qualitatively
