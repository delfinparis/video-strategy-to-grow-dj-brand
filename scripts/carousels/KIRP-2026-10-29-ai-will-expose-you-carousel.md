---
lane: "podcast"
carousel_for: "Kim Rittberg, video and speaking coach for real estate agents and founders, on Keeping It Real 2026-10-28: AI won't replace agents, it will expose the ones making generic content, and the fix is feeding AI your own differentiators instead of letting it write for anybody"
hook_family: "contrast"
heat: 2
slide_count: 5
goal: "engagement"
generated: "2026-10-29"
theme: "dark"
kirp_guest: true
guest_photo: "assets/guest-photos/2026-10-28_item1_Kim-Rittberg.jpg"
---

# Carousel: AI will expose you

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`kirp-guest-tip` (`last_used: 2026-10-26`). The second-oldest ties at `last_used: 2026-10-27`
between `stat` and `do-this-dont-do-that`; resolved to `stat` (first-listed of the tie in the
rotation file's `topics` array), built as the companion deck,
`KIRP-2026-10-29-four-tenths-of-a-second-carousel.md`.

Sourced via `KIR_REPO=../keeping-it-real-content-system python3 scripts/kirp_source.py`: episode
`2026-10-28_item1_Kim-Rittberg`, aired 2026-10-28. Kim Rittberg is a video and speaking coach for
real estate agents and founders, a former decade-plus TV producer and media executive (including
Netflix), who now teaches agents to get confident on camera.

**The one idea:** agents keep asking whether AI will replace them. Kim's answer, verbatim from
the episode: "AI is not going to replace you, but it is going to expose you and show you who you
really are." The exposure happens because generic AI scripts and brokerage-issued content look
identical across every agent using them; the fix is feeding AI your own unique differentiators
(years in the business, a niche, a credential, a personality trait) so the output can't be
anybody else's, and pairing that with a compelling first two seconds on every video. Checked
`scripts/carousels/*.md` for "Kim Rittberg," "AI exposes," and "generic content" first -- no
prior deck covers this episode or this angle.

Hook family `contrast` (generic AI content vs. the agent's own differentiators), differing from
the two most recently committed decks before today (`myth-bust`, `one-tactic-breakdown`,
2026-10-28) and from today's companion deck (`data-card`).

`kirp_guest: true` because Kim Rittberg is named and quoted verbatim throughout. This deck does
not translate to KR; a fresh KR topic is built per `docs/automation/daily-carousel-engine.md`.

---

## SLIDE 1 -- HOOK
**Headline:**
AI won't replace you. It will expose you.

**Subhead:**
A video coach who trains agents says the second part is already happening.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Video coach Kim Rittberg, a former TV producer and Netflix media executive, on what AI does to agents who skip this step.

**Subhead:**
"The one thing that AI cannot copy right now is **you**."

---

## SLIDE 3 -- THE TURN
**Headline:**
Generic content is the thing AI is exposing.

**Body:**
Kim Rittberg, on Keeping It Real: "In the world of content, social media content, video content,
AI is going to expose everybody who is not making truly original content." Her point: if you're
putting out AI content or brokerage content that anyone else with the same tools could post, it
doesn't make a client trust you more, and it never did. The thing AI can't copy is **you**
specifically, your years of experience, your niche, your personality. That has to be in the
content, not just in your head.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What Kim says to actually do:

**Numbered list:**
1. **Feed AI your own differentiators first.** Your market, your niche, your credentials, what
   makes you you, not just a prompt about real estate.
2. **Redline every AI draft like a contract.** Cut anything that could have been written for
   Joe, Jane, or any other agent in your area.
3. **Nail the first two seconds, every time.** Kim's own words: it's going to "either torpedo
   your content or make it amazing."
4. **Get on video if you aren't already.** AI made generic content easy for everyone, which made
   showing up as yourself the actual differentiator.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
AI isn't coming for your job. It's coming for your sameness.

**Subhead:**
The agents it exposes are the ones who never showed up as themselves in the first place.

---

## Social Captions

### LinkedIn
A video coach who trains agents put it plainly: AI won't replace you, it will expose the agents whose content could be anyone's.

### Instagram
Before you post another AI-written caption, ask if it sounds like you or like every other agent using the same prompt.

### Facebook
Chicago agents, the fix for AI-sounding content isn't better prompts, it's feeding AI the stuff about you that nobody else can copy.

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| "AI is not going to replace you, but it is going to expose you and show you who you really are" | Yes, slide 1 concept, slide 5 | Kim Rittberg, Keeping It Real episode `2026-10-28_item1_Kim-Rittberg`, aired 2026-10-28, verbatim per transcript `data/transcripts/2026-10-28_item1_Kim-Rittberg.txt` (00:03:09-00:03:17), and matching the `kirp_source.py` quote output | Confirmed, named guest, named episode, timestamped |
| "The one thing that AI cannot copy right now is you. You being uniquely charming, you being uniquely insightful." | Yes, slide 2 | Same transcript, 00:05:18-00:05:26 | Confirmed verbatim quote, named guest |
| "In the world of content, social media content, video content, AI is going to expose everybody who is not making truly original content" | Yes, slide 3 | Same transcript, 00:04:00-00:04:12 | Confirmed verbatim quote, named guest |
| The redline-the-AI-draft and first-two-seconds tactics | Yes, slide 4 | Same transcript, 00:06:34-00:06:49 (redline) and 00:07:44-00:07:54 ("I want to see every video have a really compelling first two seconds. That is going to either torpedo your content or make it amazing.") | Guest's own stated tactics, paraphrased into imperative form for the numbered list, quote on item 3 kept verbatim |
| Kim Rittberg is a former TV producer and media executive, including Netflix | Yes, slide 2 | Same transcript, 00:03:36-00:03:41: "I was a former TV producer for over a decade and I was a media executive. I launched a weekly video unit and I worked at Netflix" | Confirmed, guest's own stated bio |

**Do-not-cite check:** Kim Rittberg is the only named person. Her sponsors (Real Geeks,
corded.io) and her own paid program (Video Bootcamp) are not referenced anywhere on the deck.

**Guest tag:** Instagram @kimrittberg -- already verified and on file in `data/guest-socials.json`
(verified July 2026 from Kim's own website, kimrittberg.com, and multiple Keeping It Real episode
pages; also confirmed in a separate episode's transcript where D.J. spells the handle on air).
Not re-verified today per the re-use rule for an already-confirmed entry. LinkedIn
(linkedin.com/in/kimrittberg) and YouTube (@kimrittbergcontent) are also on file if needed;
Facebook is listed as "plausible, not fully confirmed" and TikTok has no confirmed handle --
leave either untagged if used.
