---
lane: "dont-make-this-mistake"
source_script: "data/news-briefs/2026-10-11.md"
carousel_for: "Going quiet during the week before closing, the highest-anxiety week of the whole deal, and the daily one-liner that fixes it"
hook_family: "mirror"
heat: 2
slide_count: 5
goal: "engagement"
generated: "2026-10-11"
theme: "dark"
---

# Carousel: the week-before-closing silence

`dont-make-this-mistake` and `market-tip` are today's two oldest rotation slots.
`dont-make-this-mistake` sits unambiguously oldest at `last_used: 2026-10-08` in
`data/carousel-topic-rotation.json`. `market-tip` and `kirp-guest-tip` are tied next at
`2026-10-09`; `market-tip` wins the tie because it is listed before `kirp-guest-tip` in the
`topics` array, the same array-order tiebreak this engine's prior builds have used (e.g.
`KIRP-2026-10-09-rate-hits-7-40-carousel.md`). `kirp-guest-tip` stays banked for tomorrow.

Sourced per Step 2(b): today's walk-and-talk brief, `data/news-briefs/2026-10-11.md`, Realtor
Tips option 3 (ST-0017, "vanishing during the week before closing," target: self, receipt:
Redfin). Checked `scripts/carousels/` first for this angle: the overpricing mistake (ST-0001)
already ran as `KIRP-2026-10-07-win-the-appointment-carousel.md`, and the post-closing
disappearing act (ST-0014) overlaps with the already-shipped referral-ratio deck
(`KIRP-2026-10-08-only-call-when-you-need-something-carousel.md`), so this deck uses the third
option instead: the agent who goes quiet in the final week before closing, not before or after
it. No prior carousel covers this specific window.

**The one idea:** the week before closing is the buyer's highest-anxiety week of the entire
transaction, and an agent who goes quiet in it because nothing has technically changed yet
costs themselves the trust that closing is supposed to confirm. The fix is a daily one-line
update, even when there's nothing new to report, plus verifying wire instructions by phone,
never email. Hook family `mirror` (the deck reflects the agent's own habit back at them),
differing from today's companion `market-tip` deck (`myth-bust`) and from the two most recently
committed carousels (`data-card`, `KIRP-2026-10-10-the-list-size-ceiling-carousel.md`, and
`swap-list`, `KIRP-2026-10-10-the-texter-swap-carousel.md`).

---

## SLIDE 1 -- HOOK
**Headline:**
You went quiet the week they're **wiring savings.**

**Subhead:**
Nothing changed on your end. Everything changed on theirs.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
The week before closing is the most anxious week of the whole deal.

**Subhead:**
It's also the week most agents go quiet, because nothing new happened yet.

---

## SLIDE 3 -- THE TURN
**Headline:**
Silence doesn't mean calm. It means they're guessing.

**Body:**
By the time a deal reaches its final week, the buyer has already waited months to get there.
Then the lender wants one more document, the walkthrough isn't confirmed, and their agent goes
quiet because there's no news yet. The buyer doesn't read that as calm. They read it as the
deal falling apart, and they start checking email at midnight. "No news" is not nothing. It's a
message you're choosing not to send.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Run this every day the week before closing:

**Numbered list:**
1. **Send one line, even with no update.** "Lender has everything, waiting on clear to close,
   expect Thursday. Nothing needed from you." Silence and "no news" are not the same thing.
2. **Name the next step before they ask for it.** Walkthrough time, wire date, what still has
   to happen. Guessing is what makes a buyer anxious, not waiting.
3. **Verify wire instructions by phone, never email.** Say it directly: "I will never email you
   new wire instructions. If you get an email that looks like it's from me, call me first."
4. **Confirm the walkthrough in writing the day before.** One less thing for them to carry into
   closing day.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
If you have a closing this week, send today's update right now.

**Subhead:**
Even if the update is "nothing new yet." That's still a message.

---

## Social Captions

### LinkedIn (PRIMARY)
The week before closing is the most anxious week of the whole transaction, and it's also the
week most agents go quiet.

Nothing new happened yet, so there's nothing to report, so the update doesn't get sent. The
buyer doesn't read that as calm. They read it as the deal falling apart, and they start
checking email at midnight.

Send one line every day that week, even when nothing changed. Name the next step before they
ask. And say out loud that you will never send new wire instructions by email, so a buyer knows
to call you first if one shows up.

Learn more at joinkale.com

#RealtorTips #RealEstateAgents #ClientExperience #KeepingItRealPodcast

### Instagram
Nothing changed on your end. Everything changed on theirs. The week before closing is the most
anxious week of the deal, and it's also the week most agents go quiet.

Send one line a day, even when there's no update. And tell every buyer: wire instructions never
come by email. Call first.

#RealtorTips #RealEstateAgents #ClientExperience

### Facebook
The week before closing, send one update a day, even if nothing changed. And never let new wire
instructions arrive by email without a call first.

#RealtorTips #RealEstateAgents

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-10-11-the-week-before-closing-silence-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Dark theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. This is an open deck. No keyword, no ManyChat flow, no ask on any platform.

**LinkedIn first comment:** https://joinkale.com/?src=carousel-kirp-2026-10-11-the-week-before-closing-silence-carousel

**Pinned first comment (IG and FB):** "The exact line to send every day that week: 'Lender has
everything, waiting on clear to close, expect Thursday. Nothing needed from you.'"

---

## Data Source

- **Claim:** "The typical U.S. home spent about 64 days on market before going under contract
  in early 2026, the longest stretch in six years."
  - Source: Redfin, 2026. Carried from today's walk-and-talk brief
    (`data/news-briefs/2026-10-11.md`, ST-0017 receipt).
  - Who was measured: homes listed for sale, national data.
  - Status: confirmed, used only as stakes-setting context (a deal that already took months to
    reach its final week is not one to let collapse from silence), not as the deck's central
    claim.
- **Claim:** going quiet during the final week costs trust, and a daily one-liner plus phone
  verification of wire instructions fixes it.
  - Source: D.J.'s own tactical guidance, carried verbatim from the brief's ST-0017 entry (the
    swap and the exact phone-verification line).
  - Status: tactical guidance, not a measured statistic.
- **Fabrication audit:** no percentage, survey, or dollar figure is invented. The only sourced
  number (64 days, Redfin 2026) is used exactly as the brief states it, with no rounding and no
  causal claim attached beyond setting the stakes.
