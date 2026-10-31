---
lane: "podcast"
carousel_for: "Mischa Fisher, Zillow's chief economist: the typical mortgage payment has doubled in five years while incomes are up only a third, but a 30-plus month inventory streak hands buyers real negotiating leverage most agents aren't using yet"
hook_family: "data-card"
heat: 2
slide_count: 5
goal: "reshares-and-followers"
generated: "2026-10-31"
guest: "Mischa Fisher"
episode_aired: "2026-10-30"
guest_photo: "assets/guest-photos/2026-10-30_item1_Mischa-Fisher.webp"
kirp_guest: true
theme: "dark"
---

# Carousel: the payment doubled, so did the leverage

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`dont-make-this-mistake` (`last_used: 2026-10-28`), built as the companion deck,
`KIRP-2026-10-31-vanishing-before-closing-carousel.md`. The second-oldest was a tie at
`last_used: 2026-10-29` between `stat` and `kirp-guest-tip`. Ran `kirp_source.py` first to check
whether the guest archive could actually clear the tie-breaker before committing to it --
it returned a fresh, unused episode (Mischa Fisher, aired 2026-10-30), so `kirp-guest-tip`
resolved the tie and `stat` stays at `last_used: 2026-10-29` for the next run.

Source per Step 2(a): `KIR_REPO=../keeping-it-real-content-system python3 scripts/kirp_source.py`,
episode `2026-10-30_item1_Mischa-Fisher`. Guest: Mischa Fisher, Chief Economist at Zillow,
recorded live at the Zillow Unlock Conference in Las Vegas. `kirp_guest: true` is set because a
named guest's own data and direct quotes are the entire deck -- the field that stops
`reskin_kr.py` from republishing Fisher's analysis under Kale's logo with the credit stripped off.

**The one idea:** the scary number agents keep repeating to buyers is the rate. The real number is
the mortgage payment doubling in five years against incomes up only a third, which is what Fisher
actually said on the show -- and the number agents aren't using is the inventory streak: 30-plus
straight months of rising supply, the longest run in years, which hands buyers negotiating room on
repairs and contingencies that didn't exist two years ago. Rule 0 criterion 8, an earned
inside-the-industry observation traceable to a named guest (Mischa Fisher, aired 2026-10-30), and
criterion 7, a mindset reframe (the rate isn't the only number that moved).

Hook family `data-card`, differing from the two most recently committed decks before today
(`swap-list` and `myth-bust`, both 2026-10-30) and from today's paired deck (`one-tactic-breakdown`,
`KIRP-2026-10-31-vanishing-before-closing-carousel.md`).

Both quotes below are verbatim from the episode transcript
(`data/transcripts/2026-10-30_item1_Mischa-Fisher.txt` in the KIR repo) and the structured analysis
(`data/analysis/2026-10-30_item1_Mischa-Fisher_analysis.json`), trimmed only from the ends, never
the middle.

---

## SLIDE 1 -- HOOK
**Headline:**
Mortgage payments doubled in five years.

**Subhead:**
Zillow's chief economist says buyers still have leverage. Here's where it is.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
"Don't get too hung up on where rates are."

**Subhead:**
Mischa Fisher, Zillow's chief economist, says the math still works for buyers who move now.

---

## SLIDE 3 -- THE TURN
**Headline:**
The payment is real. So is the leverage.

**Body:**
The typical cost of a mortgage payment has doubled in the last five years, while incomes are only
up by a third, Zillow's chief economist Mischa Fisher said on Keeping It Real. But the rate isn't
the only number that moved. Inventory has climbed for **30-plus** straight months, the longest
stretch in years. More homes on the market means buyers can finally negotiate the repairs and
contingencies they used to just accept.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What to do with your next rate-shy buyer:

**Numbered list:**
1. **Say the real math out loud.** Show the exact monthly number and what it buys, instead of letting the rate alone scare them off.
2. **Point to the inventory streak.** Thirty-plus straight months of rising supply means buyers have more to choose from than they have in years.
3. **Negotiate what used to be fixed.** Repairs, contingencies, and closing costs are back on the table.
4. **Check one Zillow number a month.** Fisher's own pick: the change in home values, at zillow.com/research.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
The payment doubled. The leverage did too.

**Subhead:**
Use both the next time a buyer says they're waiting for rates to drop.

---

## Social Captions

### LinkedIn
Zillow's chief economist told me the rate isn't the real story for buyers right now, the 30-month inventory streak is.

### Instagram
Mortgage payments doubled in five years, and Zillow's chief economist says buyers still have leverage most agents aren't using.

### Facebook
Buyers who feel priced out by the rate are missing the inventory streak that's actually working in their favor.

---

## Verified Tags

Mischa Fisher's handles, checked today against `data/guest-socials.json` (not previously present,
added below):

- LinkedIn: https://www.linkedin.com/in/mischafisher -- verified via the hyperlink on his name in
  the episode's own show notes (`keeping-it-real-content-system/webapp/src/data/episodes.json`,
  episode id 1, published 2026-10-30).
- Instagram, TikTok, Facebook, YouTube: not found in the episode description, the transcript, or
  his personal website link. **VERIFY before posting.** Leave untagged on every platform until
  confirmed.

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-10-31-payment-doubled-leverage-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Dark theme, 1080x1350.

**Platform routing:** Instagram (carousel, no tag, handle unverified), Facebook (carousel, no tag),
LinkedIn (document carousel, PDF in the same folder, tag linkedin.com/in/mischafisher).

**Gate:** none. This is an open deck. No keyword, no ManyChat flow, no ask on any platform.

**LinkedIn first comment:** https://joinkale.com/?src=carousel-kirp-2026-10-31-payment-doubled-leverage-carousel

**Pinned first comment (IG and FB):** "Mischa Fisher is Zillow's chief economist. Both quotes on
this deck are his, verbatim, from his conversation with D.J. on Keeping It Real."

---

## Data Source

- **Claim:** "The typical cost of a mortgage payment has doubled in the last five years, while
  incomes are only up by a third."
  - Source: Keeping It Real podcast, episode aired 2026-10-30, guest Mischa Fisher (Chief
    Economist, Zillow), transcript timestamp approximately 00:17:40-00:17:50
    (`data/transcripts/2026-10-30_item1_Mischa-Fisher.txt`); confirmed against the structured
    episode analysis's `quotable_insights` field
    (`data/analysis/2026-10-30_item1_Mischa-Fisher_analysis.json`).
  - Who was measured: national mortgage payment cost and income growth, Fisher's own stated
    figures on-air.
  - Status: confirmed, named guest, specific moment.

- **Claim:** "Don't get too hung up on where rates are."
  - Source: same episode, transcript timestamp approximately 00:16:03-00:16:09; matches the
    `clip_worthy_moments` quote in the analysis file at timestamp 15:04. Trimmed only from the end
    (the clause continues "...walking through the math of it"); no words inside the quoted sentence
    were altered.
  - Status: confirmed, verbatim.

- **Claim:** "We've been on a 30 plus month continuous streak of additional inventory."
  - Source: same episode, transcript timestamp approximately 00:16:14-00:16:19.
  - Who was measured: national housing inventory, Zillow data, Fisher's own stated figure.
  - Status: confirmed, verbatim.

- **Claim:** Fisher's own preferred metric for agents to check monthly is the change in home
  values, at Zillow Research.
  - Source: same episode, transcript timestamp approximately 00:10:53-00:11:05; matches
    `key_tactics` in the analysis file ("Use Zillow's research data to track changes in home
    values," timestamp 11:05).
  - Status: confirmed, named guest's own stated tactic.
