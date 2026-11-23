---
lane: "podcast"
carousel_for: "Mengjiao Chen (first-year full-time agent, Greater Seattle area/Bellevue): she books an appointment a day cold-calling expired listings, then has no follow-up system once the appointment is over, and keeps hoping someone hands her a system to copy instead of building her own"
hook_family: "pov-relatable"
slide_count: 5
goal: "reshares-and-followers"
generated: "2026-11-23"
guest: "Mengjiao Chen"
episode_aired: "2026-11-20"
guest_photo: "assets/guest-photos/2026-11-20_item9019_Mengjiao-Chen.jpg"
kirp_guest: true
theme: "dark"
---

# Carousel: the system you're hoping someone hands you

Today's two rotation slots, per `data/carousel-topic-rotation.json`: oldest is `kirp-guest-tip`
(`last_used: 2026-11-20`), built here. Second-oldest ties at `last_used: 2026-11-21` between
`stat` and `do-this-dont-do-that`; resolved to `stat`, first-listed of the tie in the rotation
file's `topics` array (same tie-break convention prior runs used), built as the companion deck,
`KIRP-2026-11-23-first-time-buyer-at-40-carousel.md`.

Sourced per Step 2(a): `KIR_REPO=../keeping-it-real-content-system python3 scripts/kirp_source.py`
surfaced the newest unused episode, Mengjiao Chen (first-year full-time agent, Greater Seattle
area, Bellevue; aired 2026-11-20, the monthly "Breakthrough with Michael" live-coaching format
with coach Michael Open). The script downloaded her headshot to
`assets/guest-photos/2026-11-20_item9019_Mengjiao-Chen.jpg` and recorded the episode in
`data/kirp-carousel-state.json`. Full transcript at
`keeping-it-real-content-system/data/transcripts/2026-11-20_item9019_Mengjiao-Chen.txt`.

**Quote re-verification.** The printed brief's "verbatim quotes" field and the analysis JSON's
`clip_worthy_moments` quote are both close paraphrases, not exact transcript lines (the analysis
JSON timestamps the quote at 20:00, but the actual exchange is at 00:11:13-00:11:26). This deck
quotes the real transcript lines at their real timestamps instead -- see Data Source.

**The one idea:** MJ's cold-calling script works. She calls expired listings, offers to help
find out why the house didn't sell, and books an appointment a day. What breaks is everything
after the appointment: no debrief with her managing broker, no planned next message for an
interested lead, no system for when to follow up. Her own words name the trap exactly: she is
hoping to find a book or a system she can copy rather than build one of her own. D.J.'s cold-open
framing of the episode is the deck's turn: the system you're waiting for someone to hand you
doesn't exist, and the fix is building the one that fits how you actually work.

Hook family `pov-relatable` (the relatable freeze after a hard-won appointment), differing from
today's companion deck (`myth-bust`) and from the most recent committed decks before today
(`KIRP-2026-11-22-affordability-constraint-carousel.md`: `data-card`;
`KIRP-2026-11-22-contract-you-didnt-write-carousel.md`: `one-tactic-breakdown`).

`kirp_guest: true` is set because a named guest's own words and her own struggle carry the deck,
so this does not translate to Kale and a fresh KR topic is authored instead.

---

## SLIDE 1 -- HOOK
**Headline:**
She books the appointment. Then she **freezes.**

**Subhead:**
A first-year agent's cold-calling win, and the exact gap that opens right after it.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
The scary calls aren't her problem. What happens after is.

**Subhead:**
Mengjiao Chen, first-year full-time agent, Greater Seattle area. One appointment a day, cold-calling expired listings.

---

## SLIDE 3 -- THE TURN
**Headline:**
She wants a system to **copy.** Not one to build.

**Body:**
Her own words on the show: "I'm hoping I could read a book or have a system that I can just
duplicate and copy. I'm not sure why I haven't created one of my own yet." That's the exact trap.
She can get a stranger on the phone to agree to a meeting. What she doesn't have is a plan for
what happens the moment that meeting ends. D.J.'s framing of the episode names the fix: the
system you're waiting for someone to hand you doesn't exist. You build the one that fits how you work.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
Four things to build before your next appointment:

**Numbered list:**
1. **Write your next line for every outcome, before you dial.** Know what you say to a "yes," a
   "maybe," and a "not now" so you're not improvising the second you hang up.
2. **Debrief with your broker after the appointment, not just before it.** She prepped her CMA
   with her managing broker going in, then never went back to ask what came next.
3. **Give every interested lead a reason to hear from you again.** Not a check-in text. A reason,
   tied to something they actually said.
4. **Log the follow-up the same day.** A note you can't find a week later was never a system.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Here's what you do now.

**Subhead:**
Pick one lead you have no next step planned for, and write that exact next message before today ends.

---

## Social Captions

### LinkedIn
A first-year agent on Keeping It Real books an appointment a day from cold calls and still freezes the second the appointment ends.

### Instagram
She's booking an appointment a day cold-calling expired listings, and she just told her coach on air she's still hoping someone hands her the system instead of building one.

### Facebook
A first-year agent gets the appointment from a cold call, then doesn't know what to say next, and that gap is the whole episode.

### TikTok
First-year agent books an appointment a day cold-calling expired listings, then freezes right after. #RealEstateAgent #RealEstateTips

### YouTube Shorts
**Title:** She books the appointment. Then freezes.

A first-year agent's cold-calling win, and the exact gap that opens the moment the appointment ends. #RealEstateAgent #RealEstateTips

---

## Verified Tags

| Platform | Handle | Verification |
|---|---|---|
| Instagram | **VERIFY before posting** | `data/guest-socials.json` already carries a `mengjiao-chen` entry from a web search run 2026-11-21: no verified personal handle found on any platform, limited public social footprint for a first-year agent. Not re-guessed here. |
| TikTok | **VERIFY before posting** | Same entry, same result. |
| LinkedIn | **VERIFY before posting** | Same entry, same result. |
| Facebook | **VERIFY before posting** | Same entry, same result. |

No change written to `data/guest-socials.json` -- the existing entry (verified 2026-11-21, one
day before this build) already reflects a clean no-handles-found search and does not need
re-running per the CLAUDE.md rule to use an existing registry entry rather than re-verify.

---

## Instagram Collab

**Cannot be set up.** No verified Instagram handle exists for Mengjiao Chen. Do not guess one
and do not invite a Collab from an unverified handle. If D.J. gets her handle directly, add it to
`data/guest-socials.json` and set up the Collab by hand before this posts.

---

## Post-publish DM

**Cannot be sent via Instagram** -- no verified handle. If D.J. has another way to reach her
(the episode's own contact path, or a number from the show's booking process), the message to
send is:

> Hey MJ, thanks for being so honest on the show this month, the "I want a system to copy, not
> build" line is going to land with a lot of first-year agents who feel exactly that. Made a
> carousel out of the cold-calling-to-follow-up gap and credited you. Keep going on the expired
> listings, that part is already working.

No ask beyond eventual contact. No pitch, no mention of Kale.

---

## Data Source

Every claim traces to the episode transcript
(`keeping-it-real-content-system/data/transcripts/2026-11-20_item9019_Mengjiao-Chen.txt`),
aired 2026-11-20, the live-coaching "Breakthrough with Michael" segment with coach Michael Open.

- **"I call the expired listings and I would pull up nearby the expired and get their full
  number and just call to ask them if they're still planning to sell... I would like to be a
  value to them to help them find out reasons why the house did not sell."**
  - Source: Mengjiao Chen, [00:12:01]-[00:12:25], lightly tightened for the slide (transcription
    filler words removed, no change of meaning).
  - Status: confirmed, close paraphrase of a verbatim on-air statement.

- **"I can book one appointment a day and last two weeks I've been going to appointments. Then I
  find out I am not as successful at closing at the appointment."**
  - Source: Mengjiao Chen, [00:11:13]-[00:11:26] (the raw transcript reads "book one appointment
    at day," an evident transcription typo for "a day," corrected here).
  - Status: confirmed, close paraphrase. **Correction to the analysis JSON:** the
    `clip_worthy_moments` entry timestamps a similar-sounding quote at [20:00]-[21:00] and phrases
    it as "but then I freeze on what comes after" -- that exact wording does not appear at that
    timestamp. The real freeze-after-the-appointment admission is the quote above, at [00:11:13].

- **"I'm hoping I could read a book or I could have a system that I can just duplicate and copy.
  I'm not sure why I have not created a system of my own yet."**
  - Source: Mengjiao Chen, [00:42:20]-[00:42:49].
  - Status: confirmed, close paraphrase of a verbatim on-air statement. This is the deck's turn
    and the single most load-bearing line in the file.

- **"You're waiting for somebody to hand you the perfect system... the system you're looking for
  doesn't exist and how to build the one that fits you."**
  - Source: D.J. Paris, cold-open narration, [00:00:00]-[00:00:22]. This is the host's framing of
    the episode, not a quote from Mengjiao Chen, and is attributed to D.J. in the slide-3 body
    copy accordingly.
  - Status: confirmed, verbatim.

- **She did not debrief her managing broker after the appointment, only before it (the CMA
  prep).**
  - Source: Mengjiao Chen, [00:16:00]-[00:16:25]: "Before I went to the appointment, I talked to
    the managing broker and kind of learned how to pull the CMA together... but I did not talk to
    the managing broker after the appointment."
  - Status: confirmed, close paraphrase.

- **Guest facts (first-year full-time agent, Greater Seattle area/Bellevue, former special
  education teacher and Mandarin interpreter, licensed five years, landlord for 10 years).**
  - Source: episode introduction, [00:05:05]-[00:05:19], corroborated by
    `keeping-it-real-content-system/data/analysis/2026-11-20_item9019_Mengjiao-Chen_analysis.json`.
  - Status: confirmed.

- **Fabrication audit:** No invented numbers. The deck carries no external statistic, only a
  named guest's own verbatim struggle and the host's own framing, both attributed and timestamped
  against the primary transcript rather than the analysis JSON's paraphrase.
