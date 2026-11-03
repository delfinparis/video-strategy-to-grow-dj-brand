---
lane: "podcast"
carousel_for: "Sarah Maslowski, a $140M+ producer in the Metro Atlanta market, on Keeping It Real 2026-10-21: she built her whole lead pipeline on YouTube with no paid ads by posting through the fear instead of waiting to feel camera ready, and the permission that the agents actually getting leads and closings on YouTube were never the polished ones"
hook_family: "permission-slip"
heat: 1
slide_count: 5
goal: "engagement"
generated: "2026-11-03"
theme: "dark"
kirp_guest: true
guest_photo: "assets/guest-photos/2026-10-21_item2_Sarah-Maslowski.jpg"
---

# Carousel: the camera fear

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the oldest is
`kirp-guest-tip` (`last_used: 2026-10-31`). The next-oldest ties at `last_used: 2026-11-01`
between `market-tip` and `stat`; resolved to `market-tip` (first-listed of the tie in the
rotation file's `topics` array), built as the companion deck,
`KIRP-2026-11-03-rate-lock-in-carousel.md`.

Sourced via `KIR_REPO=../keeping-it-real-content-system python3 scripts/kirp_source.py`: episode
`2026-10-21_item2_Sarah-Maslowski`, aired 2026-10-21. Sarah Maslowski is a Metro Atlanta agent
who says she has closed over $140 million in real estate directly from YouTube with no paid ads
and no cold calling.

**The one idea:** the thing stopping most agents from starting a YouTube channel is not skill or
equipment, it is the fear of looking or sounding bad on camera, and her own early videos were
exactly that. Checked `scripts/carousels/*.md` for "Sarah Maslowski," "YouTube," and "teleprompter"
first -- her two prior decks (2026-08-19, 2026-09-16) covered a different angle (her content
pillars / posting cadence), not the camera-fear permission slip, so this is a new angle on a
repeat guest.

Hook family `permission-slip` (releasing agents from the shame of looking awkward on camera),
differing from the two most recently committed decks (`myth-bust`, `forbidden`, 2026-11-02) and
from today's companion deck (`data-card`).

`kirp_guest: true` because Sarah Maslowski is named and quoted verbatim throughout. This deck does
not translate to KR; a fresh KR topic is built per `docs/automation/daily-carousel-engine.md`.

---

## SLIDE 1 -- HOOK
**Headline:**
She hated her own voice on camera.

**Subhead:**
Sarah Maslowski still closed $140 million from YouTube with zero paid ads.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Sarah Maslowski has closed over $140 million in real estate directly from YouTube, with no paid ads and no cold calling.

**Subhead:**
"Comfort comes from doing it, **not** from waiting until you feel ready."

---

## SLIDE 3 -- THE TURN
**Headline:**
The fear was never about talent.

**Body:**
Sarah Maslowski, on Keeping It Real: "Nobody is comfortable on camera at first. Nobody." When she
started watching agents who were actually getting real leads and closings from YouTube, she
noticed they were not polished hosts or news anchors. They were regular agents talking about
their own market on camera. Her own words: "I don't have to be something that I'm not. I just
have to show up as myself and give people the information they're actually looking for."

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What Sarah says to actually do:

**Numbered list:**
1. **Script your first ten videos with a teleprompter app.** It removes the pressure of talking
   off the cuff while you get used to being on camera.
2. **Answer one question clients already ask you in person.** Neighborhoods, the commute, what
   surprises people when they move there. You already have the content.
3. **Post the awkward version.** The agents getting leads and closings started awkward too. A good
   editor cleans up the stops and starts; the footage doesn't need to be clean first.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Here's what you do now.

**Subhead:**
Open your phone. Answer the one question buyers ask you most about your area. Film it once, post it today, before you watch it back twice.

---

## Social Captions

### LinkedIn
A $140 million YouTube producer says the leads went to the awkward agents who hit record anyway.

### Instagram
She hated her own voice on camera and still closed $140 million from YouTube with no paid ads.

### Facebook
Chicago agents, the camera fear that almost stopped a $140 million producer didn't, it just made her first videos awkward.

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| "I have closed over $140 million in real estate directly from YouTube with no paid ads and no cold calling" | Yes, slides 1, 2 | Sarah Maslowski, Keeping It Real episode `2026-10-21_item2_Sarah-Maslowski`, aired 2026-10-21, verbatim per transcript `data/transcripts/2026-10-21_item2_Sarah-Maslowski.txt` (00:02:58-00:03:10) | Confirmed, named guest, named episode, timestamped |
| "Comfort comes from doing it, not from waiting until you feel ready" | Yes, slide 2 | Same transcript, 00:06:58-00:07:03 | Confirmed verbatim quote, named guest |
| "Nobody is comfortable on camera at first. Nobody." | Yes, slide 3 | Same transcript, 00:06:53-00:06:57 | Confirmed verbatim quote, named guest |
| "I don't have to be something that I'm not. I just have to show up as myself and give people the information they're actually looking for" | Yes, slide 3 | Same transcript, 00:05:17-00:05:28 | Confirmed verbatim quote, named guest |
| The agents who actually got real leads and closings on YouTube were not polished hosts or news anchors, just regular agents on camera | Yes, slide 3 | Same transcript, 00:04:27-00:05:04 | Guest's own stated observation, paraphrased |
| Teleprompter apps, scripting before filming, "removes that pressure entirely" | Yes, slide 4 item 1 | Same transcript, 00:07:21-00:07:49 | Guest's own stated tactic, paraphrased into imperative form |
| Agents already know enough market content from client questions (neighborhoods, commute, what surprises movers) | Yes, slide 4 item 2 | Same transcript, 00:08:38-00:08:55 | Guest's own stated tactic, paraphrased |
| Editing removes the stops, starts, and fumbles from filmed footage | Yes, slide 4 item 3 | Same transcript, 00:05:59-00:06:24 | Guest's own stated observation, paraphrased |

**Do-not-cite check:** Sarah Maslowski is the only named person. Her sponsors (Real Geeks,
corded.io) and her own paid five-week YouTube course (opening 2026-10-22 per the episode) are not
referenced anywhere on the deck.

**Guest tag:** Instagram @youtubewithsarah -- already verified and on file in
`data/guest-socials.json` (verified June 2026 from sarahmaslowski.com and the transcript itself,
where she says "my handle is YouTube with Sarah"). TikTok @sarahmaslowski and LinkedIn
/in/sarahmaslowski are also on file. Facebook has no confirmed handle -- left untagged if used.
Not re-verified today per the re-use rule for an already-confirmed entry.
