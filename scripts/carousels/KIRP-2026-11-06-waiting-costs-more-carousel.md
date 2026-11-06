---
lane: "podcast"
carousel_for: "Anna Kara, a top 1% mortgage producer at Anna Kara Loans (Burbank/Los Angeles), on Keeping It Real 2026-10-20: her answer to the buyer who says they'll wait for rates to drop, and the competition math (one house, 61 offers) that shows waiting usually costs more than the rate does"
hook_family: "myth-bust"
heat: 1
slide_count: 5
goal: "engagement"
generated: "2026-11-06"
theme: "dark"
kirp_guest: true
guest_photo: "assets/guest-photos/2026-10-20_item3_Anna-Kara.jpg"
---

# Carousel: waiting for rates to drop costs more

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`kirp-guest-tip` (`last_used: 2026-11-03`), built here. The second-oldest ties at
`last_used: 2026-11-04` between `stat` and `do-this-dont-do-that`; resolved to `stat`
(first-listed of the tie in the rotation file's `topics` array, the same tie-break convention
earlier files used), built as the companion deck,
`KIRP-2026-11-06-the-deductible-cap-carousel.md`. `do-this-dont-do-that` stays at
`last_used: 2026-11-04` for the next run.

Sourced via `KIR_REPO=../keeping-it-real-content-system python3 scripts/kirp_source.py`: episode
`2026-10-20_item3_Anna-Kara`, aired 2026-10-20. Anna Kara is a top 1% mortgage producer in Los
Angeles.

**The one idea:** agents hear "I'll wait until rates drop" constantly, and the instinct is to
argue the rate. Anna Kara's answer is to show the buyer the competition math instead: her own
experience is that a house with 5 competing offers today can have 20, 30, even 61 once rates
fall, and that competition is what actually moves the purchase price, more than the rate ever
would have cost them.

Checked `scripts/carousels/*.md` for "Anna Kara" first -- she has four prior decks
(`2026-10-21-one-answer-not-the-answer`, `2026-10-23-show-up-as-yourself` is Sarah Maslowski not
Kara, `2026-10-25-set-a-schedule-not-a-promise` and `2026-10-25-steer-the-whole-market` are
Stupid Things entries, not Kara). The one actual repeat guest is
`KIRP-2026-10-21-one-answer-not-the-answer-carousel.md`, which covered her "shop 178 lenders, a
bank's no is one answer, not the answer" tactic. This is a different quote, a different
transcript timestamp, and a different tactic (the waiting-costs-more math, not the
lender-shopping math), so it is a new angle on a repeat guest.

Hook family `myth-bust` (busting "waiting for a lower rate saves money"), differing from the
most recent committed deck (`named-stakes`, `KIRP-2026-11-05-lender-referral-lock-carousel.md`)
and from today's companion deck (`data-card`).

`kirp_guest: true` because Anna Kara is named and quoted verbatim throughout. This deck does not
translate to KR; a fresh KR topic is built per `docs/automation/daily-carousel-engine.md`.

---

## SLIDE 1 -- HOOK
**Headline:**
Waiting for rates to drop costs more.

**Subhead:**
A top 1% mortgage producer's math on why buying now usually wins.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Anna Kara is a top 1% mortgage producer in Los Angeles. Here's what she tells buyers who say
they're waiting for rates to drop.

**Subhead:**
"If it's a 1% higher rate right now, that property, when the rates drop, you're going to pay
**$150,000** more on the purchase price."

---

## SLIDE 3 -- THE TURN

**Headline:**
It was never really about the rate.

**Body:**
Anna Kara, on Keeping It Real: a house that draws 5 competing offers today can draw 20 or 30
once rates fall, because every buyer who was waiting shows up at the same time. She has watched
it happen in Los Angeles with 30, 40, even 50 offers on a property, and she has personally worked
one transaction that drew 61 offers. That surge in competition, not the rate itself, is what
actually pushes the purchase price up.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
What Anna says to actually do:

**Numbered list:**
1. **Run the monthly-payment math out loud, before the price math.** Her own line to a buyer
   spooked by a rate tick: it's often "only like $60 difference on your monthly payment," not the
   deal-breaker it feels like in the moment.
2. **Show them the competition number, not just the rate number.** Five offers today versus 20,
   30, or 61 once rates drop is the real cost of waiting, and it's a harder number to argue with
   than a rate quote.
3. **Tell them the regret pattern.** She says she has never met a single buyer who regrets
   purchasing five, ten, or twenty years ago. The rate can be revisited later. The price locked in
   that day can't.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Next time a buyer says they're waiting for rates to drop, don't argue the rate. Show them what
happened to the last house that had 5 offers when everyone else decided to wait too.

---

## Social Captions

### LinkedIn
A top 1% mortgage producer says the buyers waiting for rates to drop are about to compete with 61 offers instead of 5.

### Instagram
She closes loans on both coasts and says waiting for rates to drop usually costs buyers more, not less.

### Facebook
Chicago agents, here's the exact math a top mortgage producer uses on buyers who say they'll wait for rates to drop.

### TikTok
A mortgage producer's math on why waiting for rates to drop usually backfires. #RealEstateAgent #MortgageTips

### YouTube Shorts
**Title:** Why waiting for rates to drop usually costs more

A top 1% mortgage producer's math on why buying now beats waiting for rates to drop. #RealEstateAgent #MortgageTips

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| "If it's a 1% higher rate right now, that property, when the rates drop, you're going to pay $150,000 more on the purchase price." | Yes, slide 2 | Anna Kara, Keeping It Real episode `2026-10-20_item3_Anna-Kara`, aired 2026-10-20, verbatim per transcript `data/transcripts/2026-10-20_item3_Anna-Kara.txt` (00:22:17-00:22:30), trimmed from the front only ("So that" removed, "if" capitalized) | Confirmed, named guest, named episode, timestamped |
| A house with 5 competing offers today can have 20 or 30 once rates drop; she has seen 30, 40, 50 offers in her own California/LA market, and one transaction of hers drew 61 offers | Yes, slide 3 | Same transcript, 00:21:54-00:22:17 | Confirmed, guest's own stated experience, paraphrased |
| "It's only like $60 difference on your monthly payment" when explaining a rate uptick to a client | Yes, slide 4 item 1 | Same transcript, 00:20:54-00:21:03 | Confirmed verbatim fragment, quoted inline |
| She has never met a single person who regrets buying a property five, ten, or twenty years ago | Yes, slide 4 item 3 | Same transcript, 00:22:40-00:22:51 | Confirmed, guest's own stated observation, paraphrased |

**Not used:** a later line in the same passage ("The rate you could always change, but the
purchase price that you're debt, you're not going to be able to finish that") reads as a
transcription artifact and was paraphrased into the takeaway instead of quoted directly, since
the raw text is not cleanly parseable as a verbatim sentence.

**Do-not-cite check:** Anna Kara is the only named person. Her episode sponsor (Real Geeks) is
not referenced anywhere on the deck.

**Guest tag:** Instagram @annakaraloans, TikTok @annakaraloan (singular "loan," not "loans" --
confirm before pasting), LinkedIn /in/annakaraloans, Facebook /annakaraloans/ -- already verified
and on file in `data/guest-socials.json` (verified 2026-10-21 from annakaraloans.com, reached from
the episode description link). Not re-verified today per the re-use rule for an already-confirmed
entry.
