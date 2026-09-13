---
lane: "podcast"
carousel_for: "Justin Black (Liv Sotheby's International Realty, Breckenridge) sends expired listings a FedEx packet instead of another call"
hook_family: "swap-list"
heat: 2
slide_count: 5
goal: "reshares-and-followers"
generated: "2026-09-13"
guest: "Justin Black"
episode_aired: "2026-09-10"
guest_photo: "assets/guest-photos/2026-09-10_item1_Justin-Black.jpg"
kirp_guest: true
theme: "dark"
---

# Carousel: Stop emailing expired listings. Mail them.

Today's oldest rotation slot, `kirp-guest-tip`, unambiguously last at `last_used: 2026-09-10`
(`data/carousel-topic-rotation.json`). Sourced per Step 2(a): ran
`KIR_REPO=../keeping-it-real-content-system python3 scripts/kirp_source.py`, which picked the
newest unused episode, Justin Black (Liv Sotheby's International Realty, Breckenridge, Colorado;
$150M in career sales; aired 2026-09-10), downloaded his headshot to
`assets/guest-photos/2026-09-10_item1_Justin-Black.jpg`, and recorded the episode in
`data/kirp-carousel-state.json`. Hook family `swap-list` (Family 9: the exact-action, "stop doing
X, do Y" shape fits the FedEx-packet tactic directly), differing from both of yesterday's decks
(`named-stakes`, `system-indictment`, `2026-09-12`) and from today's companion `stat` deck
(`sacred-cow`, `KIRP-2026-09-13-dscr-fraud-risk-carousel.md`).

`kirp_guest: true` is set because this deck names and credits Justin Black by name. It does not
translate to Kale Realty; a fresh KR topic is authored separately per
`docs/automation/daily-carousel-engine.md`.

---

## SLIDE 1 -- HOOK
**Headline:**
Stop emailing expired listings. **Mail them.**

**Subhead:**
A $150M producer says a packet in the mailbox gets the callback an email never does.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
He sends a **FedEx packet,** not a fifth phone call.

**Subhead:**
A Colorado agent with $150 million in career sales says the tactic that turns expired listings
into new business isn't another follow-up. It's something the seller can hold.

---

## SLIDE 3 -- THE TURN

**Headline:**
The packet does what the tenth call can't.

**Body:**
On the Keeping It Real Podcast, Justin Black, a real estate advisor at Liv Sotheby's
International Realty in Breckenridge, Colorado, with $150 million in career sales, said his move
on an expired listing is a physical FedEx package: a market analysis and a plain, written audit
of why the home didn't sell, sent straight to the seller's door. Every other agent chasing that
listing is sending an email or leaving a voicemail. A package that shows up by mail is the one
thing in the pile the seller actually opens, and it proves the agent already did the homework
before asking for the listing back.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Build the expired-listing packet this week:

**Numbered list:**
1. **Pull the expired MLS sheet.** Days on market, every price cut, and how many showings it
   actually got.
2. **Write a one-page, plain-language reason it didn't sell.** Price, condition, or exposure. Say
   which one. Don't hedge it.
3. **Attach a current market analysis.** What actually sold nearby this quarter, and for how much,
   not what the seller wants to hear.
4. **FedEx it to the seller's door.** No call first. No email first. Let the packet be the thing
   that opens the conversation.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Everyone calls the expired listing. **Send something instead.**

**Subhead:**
The packet gets opened on the counter. The tenth call gets declined on the screen.

---

## Social Captions

### LinkedIn
On the Keeping It Real Podcast, Justin Black of Liv Sotheby's International Realty in
Breckenridge, Colorado, a $150 million career producer, shared the move he makes on every expired
listing.

He doesn't add another call to the pile. He sends a FedEx package: a plain-language reason the
home didn't sell, plus a current market analysis, delivered to the seller's door.

The four-step build is in the carousel.

I cover tactics like this weekly on the Keeping It Real Podcast.

#RealEstateAgents #ExpiredListings #KeepingItRealPodcast

### Instagram
Every agent chasing an expired listing sends the same thing. An email. A voicemail. Another call.

A $150M producer sends a FedEx packet instead, and it's the reason sellers call him back. The
exact packet to build is in the carousel.

#RealEstateAgents #RealtorTips #ExpiredListings

### Facebook
A $150 million producer on the Keeping It Real Podcast says the move on an expired listing isn't
another call. It's a packet the seller can hold. What's inside it is in the carousel.

#RealEstateAgents #RealtorTips

---

## Verified Tags

Guest socials already verified and on file in `data/guest-socials.json` (Justin Black, verified
September 2026 via two independent web searches plus NAR 30 Under 30 cross-confirmation; no
re-verification needed per Step 6):

- Instagram: `@jblack.re` (https://www.instagram.com/jblack.re/)
- LinkedIn: https://www.linkedin.com/in/justin-black-772277150/
- Facebook: not found, leave untagged
- TikTok / YouTube: not found, leave untagged

Quote used ("$150 million in career sales") is a bio fact from the episode, not a direct quote
requiring word-for-word trim; no mid-quote edits made.

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-09-13-expired-listing-packet-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Dark theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel, PDF
in the same folder).

**Gate:** none. Open deck, no keyword, no ManyChat flow.

**Pinned first comment (IG and FB):** "Full episode with Justin Black is on the Keeping It Real
Podcast. Episode aired September 10, 2026."

**LinkedIn first comment:**
https://joinkale.com/?src=carousel-kirp-2026-09-13-expired-listing-packet-carousel

---

## Data Source

- **Claim:** "Justin Black, a real estate advisor at Liv Sotheby's International Realty in
  Breckenridge, Colorado, has $150 million in career sales."
  - Source: Keeping It Real Podcast episode with Justin Black, aired 2026-09-10 (episode stem
    `2026-09-10_item1_Justin-Black`), guest bio pulled via `scripts/kirp_source.py` from
    `keeping-it-real-content-system` episode data.
  - Who was measured: D.J.'s own podcast guest intake, a named, real interview.
  - Status: confirmed, from the episode's own guest record.

- **Claim:** "His move on an expired listing is a FedEx package containing a market analysis and a
  written audit of why the home didn't sell."
  - Source: same episode, key tactics list: "Send a FedEx package with a personalized audit to
    expired listings" and problem/solution pairing: "Converting expired listings -> Send a
    comprehensive physical packet with a market analysis and personalized audit to expired
    listings."
  - Status: confirmed, episode analysis as printed by `scripts/kirp_source.py`. Not a verbatim
    quote (no direct quote on this specific tactic was flagged in the source), so slide copy
    paraphrases the tactic rather than putting it in quotation marks.

- **Note on the AI/SEO tactic not used here:** the episode also covers Justin Black's use of AI to
  generate SEO content ("AI has already brought me almost $5 million in listings" [00:20:00]).
  Not used in this deck to keep the one-idea rule (carousel-standard.md); it is a second idea and
  would be a second deck, not a second body slide here.
