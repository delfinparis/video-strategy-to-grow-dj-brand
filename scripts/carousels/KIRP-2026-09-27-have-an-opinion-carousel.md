---
lane: "podcast"
carousel_for: "Frances Katzen (Douglas Elliman team leader, Manhattan): market reports and media appearances built on a specific, provocative opinion instead of a neutral recap, and the same directness used one-on-one with clients"
hook_family: "sacred-cow"
heat: 4
slide_count: 5
goal: "engagement"
generated: "2026-09-27"
theme: "light"
kirp_guest: true
guest_photo: "assets/guest-photos/2026-09-24_item1_Frances-Katzen.jpg"
---

# Carousel: She tells buyers not to buy.

Today's rotation: two topic types tied oldest per `data/carousel-topic-rotation.json`.
`kirp-guest-tip` is the true oldest at `last_used: 2026-09-24`. `market-tip` and `stat` are
tied at `2026-09-25`; `market-tip` taken over `stat` by list order (the same tie-break
convention the 2026-09-26 run used: earlier entry in the `topics` array wins a tie). This deck
is `kirp-guest-tip`; the companion deck (`market-tip`) is
`KIRP-2026-09-27-rate-print-contradicts-the-wait-carousel.md`.

Source per Step 2(a): `KIR_REPO=../keeping-it-real-content-system python3 scripts/kirp_source.py`,
which picked the newest unused episode, Frances Katzen (aired 2026-09-24), a Douglas Elliman team
leader in Manhattan, and downloaded her headshot to `assets/guest-photos/2026-09-24_item1_Frances-Katzen.jpg`.
Episode marked used in `data/kirp-carousel-state.json`.

The one idea: Katzen builds her market reports and media appearances around a specific,
provocative opinion rather than a neutral recap ("Let's have an opinion. And it is
provocative... Ooh, that'll get people," 09:00), and carries the same directness into client
conversations, on the record turning down a buyer's stated want ("I just said, don't do it. Why
are you doing it? Like don't buy it just for the sake of a view," 15:45). Both quotes are
reproduced verbatim from the episode transcript's analysis JSON, trimmed only at whole-word
boundaries, never mid-sentence.

No number appears on any slide. Her production/ranking is not stated as a claim anywhere in this
deck -- she is described only as "a Douglas Elliman team leader in Manhattan," a professional
fact from the episode's own show notes, not a ranking figure requiring separate sourcing.

Hook family `sacred-cow` (Family 2: attacking the sacred practice of staying neutral and
agreeable in your marketing and with clients) differs from the companion `market-tip` deck's
`mirror` and from the two most recent KIRP decks (`named-stakes` and `swap-list`, both
2026-09-26).

`kirp_guest: true` -- a named KIR guest is quoted throughout. This deck does NOT translate to
Kale Realty. `reskin_kr.py` will exit 2 on this file, and a fresh KR topic ships in its place.

---

## SLIDE 1 -- HOOK
**Headline:**
She tells buyers **not** to buy.

**Subhead:**
A Manhattan team leader on the one habit that gets her both media appearances and repeat clients.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
A buyer wanted the view. She said don't.

**Subhead:**
Most agents chase the yes. This one will talk a client out of the purchase they came in wanting.

---

## SLIDE 3 -- THE TURN
**Headline:**
Have an opinion. On purpose.

**Body:**
Frances Katzen, a Douglas Elliman team leader in Manhattan, builds her market reports and her media appearances around one habit: a specific, provocative opinion instead of a neutral recap. "Let's have an opinion. And it is provocative," she said on Keeping It Real. "Ooh, that'll get people." The same directness shows up one-on-one. On a buyer set on a view-driven purchase, her advice was blunt: "I just said, don't do it. Why are you doing it? Like don't buy it just for the sake of a view." A neutral report gets skimmed. A stance gets quoted, and remembered as whose stance it was.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What that looks like on your next report:

**Numbered list:**
1. **Put one real opinion in your next market update, not just the numbers.** "Prices flattened" is a stat. "This is the wrong month to overprice" is a position.
2. **Say the hard thing to the client in front of you, on the spot.** Katzen's line to a buyer chasing a view: don't buy it just for that.
3. **Repeat the stance until it's yours.** "Consistency wins the race," Katzen said. "It's just showing up and doing it."

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
A market report with no opinion in it is a stat sheet nobody remembers who sent.

---

## Social Captions

### LinkedIn
Frances Katzen, a Douglas Elliman team leader in Manhattan, builds her market reports and her media appearances around one habit: a specific, provocative opinion instead of a neutral recap.

"Let's have an opinion. And it is provocative," she said on Keeping It Real. "Ooh, that'll get people."

The same directness shows up with clients. On a buyer set on a view-driven purchase: "I just said, don't do it. Why are you doing it? Like don't buy it just for the sake of a view."

A neutral report gets skimmed. A stance gets remembered as whose it was.

#RealEstateAgents #RealtorTips #KeepingItRealPodcast

### Instagram
She tells buyers not to buy. A Manhattan team leader on the one habit behind both her media appearances and her repeat clients: a real opinion, stated plainly, every time.

The line she used on a buyer chasing a view is in the carousel.

#RealEstateAgents #RealtorTips #KeepingItRealPodcast

### Facebook
A buyer wanted the view. This Manhattan agent said don't buy it just for that, on the record. The habit behind it is in the carousel.

#RealEstateAgents #RealtorTips

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-09-27-have-an-opinion-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Light theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. Open deck, no keyword, no ManyChat flow.

**Pinned first comment (IG and FB):** "Source: Frances Katzen on Keeping It Real, aired
2026-09-24. Quotes are verbatim from the episode."

**LinkedIn first comment:**
https://joinkale.com/?src=carousel-kirp-2026-09-27-have-an-opinion-carousel

**Guest tag:** Instagram @franceskatzen, Facebook "The Katzen Team," LinkedIn linkedin.com/in/franceskatzen
-- verified 2026-09-27 via Douglas Elliman's own official team page (elliman.com/team/the-katzen-team/226107),
which independently confirms the same brokerage, market, and "Top 10 List" production claim as
this episode. Full verification trail in `data/guest-socials.json`. TikTok and YouTube are
unverified -- leave untagged if either is needed.

---

## Data Source

- **Claim:** Both quotes attributed to Frances Katzen ("Let's have an opinion. And it is
  provocative... Ooh, that'll get people"; "I just said, don't do it. Why are you doing it?
  Like don't buy it just for the sake of a view"; "Consistency wins the race, right? It's just
  showing up and doing it.") are reproduced verbatim from the Keeping It Real episode transcript.
  - Source: Keeping It Real podcast, episode aired 2026-09-24, guest Frances Katzen. Sourced via
    `KIR_REPO=../keeping-it-real-content-system python3 scripts/kirp_source.py`, which reads
    `keeping-it-real-content-system/data/analysis/2026-09-24_item1_Frances-Katzen_analysis.json`
    (built from the aired episode transcript).
  - Who was measured: not applicable. Primary-source interview quotes, not a survey.
  - Status: confirmed. This is D.J.'s own recorded interview; no external re-verification needed
    beyond the transcript/analysis pipeline this repo already treats as ground truth for KIRP
    carousels.
- **No numeric claim appears on any slide.** Katzen's production or team ranking is not stated;
  only her title (team leader) and market (Manhattan, Douglas Elliman) are used, both plain
  professional facts from the episode's own show notes.

## AI Music Prompt

Not applicable. This is a static image carousel, not a video (see `docs/series/carousel-standard.md`,
"Music prompt: only if it ships as video").
