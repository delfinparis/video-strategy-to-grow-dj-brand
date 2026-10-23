---
lane: "podcast"
carousel_for: "Sarah Maslowski ('the YouTube Lab'): she's closed over $140 million in real estate directly from YouTube with no paid ads and no cold calling, and her own turning point was realizing she didn't have to perform on camera, just show up as herself"
hook_family: "myth-bust"
heat: 2
slide_count: 5
goal: "reshares-and-followers"
generated: "2026-10-23"
guest: "Sarah Maslowski"
episode_aired: "2026-10-21"
guest_photo: "assets/guest-photos/2026-10-21_item1_Sarah-Maslowski.jpg"
kirp_guest: true
theme: "dark"
---

# Carousel: show up as yourself

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`dont-make-this-mistake` (`last_used: 2026-10-20`). The second slot ties at `last_used:
2026-10-21` between `market-tip` and `kirp-guest-tip`. Resolved toward `kirp-guest-tip`: Step 2(a)
was run to check archive availability before deciding the tie, and it surfaced a real, unused
episode (Sarah Maslowski, aired 2026-10-21, "YouTube Lab" segment), recording that episode as used
in `data/kirp-carousel-state.json` and downloading her headshot. Building a different topic after
that point would leave the episode consumed with nothing made from it, so `kirp-guest-tip` is
today's second deck and `market-tip` stays at `last_used: 2026-10-21` for the next rotation pass.
Today's companion deck is `KIRP-2026-10-23-never-checked-what-you-can-take-carousel.md`
(`dont-make-this-mistake`).

Sourced via `KIR_REPO=../keeping-it-real-content-system python3 scripts/kirp_source.py` (Step
2(a)), which surfaced Sarah Maslowski's solo "YouTube Lab" episode. Every claim traces to the
transcript (`keeping-it-real-content-system/data/transcripts/2026-10-21_item1_Sarah-Maslowski.txt`)
and the matching analysis JSON; see Data Source. `kirp_guest: true` is set because the deck is
built entirely on one named guest's own figures and her own stated turning point, so it does not
translate to Kale and a fresh KR topic is authored instead.

**The one idea:** Sarah's own stated mindset shift -- "I don't have to be something that I'm not.
I just have to show up as myself" -- is the thing she credits for a $140M+ YouTube-driven business
built with no paid ads and no cold calling. Rule 0 criterion 5 (a memorable, guest-branded line)
plus criterion 8 (an earned, traceable insider observation from a named guest by episode and
timestamp). Hook family `myth-bust` (the deck's whole job is correcting the belief that YouTube
leads require polish), differing from the three most recently committed decks (`data-card`,
`mirror`, `swap-list`) and from today's companion `dont-make-this-mistake` deck
(`system-indictment`).

Checked `scripts/carousels/` for "Sarah Maslowski," "YouTube," and "teleprompter" first -- no
prior deck covers this guest, this episode, or this angle. (Sarah appears in two older decks tied
to her 2026-08-19 and 2026-09-16 episodes; this is her 2026-10-21 episode, a different angle.)

---

## SLIDE 1 -- HOOK
**Headline:**
$140 million. **Zero** paid ads.

**Subhead:**
She built it on YouTube by refusing to perform on camera.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Every agent actually getting leads from YouTube looked a little boring at first.

**Subhead:**
Sarah Maslowski, a $140M+ producer out of Metro Atlanta, built her whole channel on that.

---

## SLIDE 3 -- THE TURN
**Headline:**
She stopped trying to sound like someone else on camera.

**Body:**
On Keeping It Real, Sarah Maslowski said the moment that changed everything was watching the
agents who were actually getting leads and closings from YouTube and noticing they weren't
polished. They were regular agents talking about their own market. That's when she says she
realized, in her own words, "I don't have to be something that I'm not. I just have to show up
as myself." That's the same voice she's used to close over **$140 million** in real estate
directly from YouTube, with no paid ads and no cold calling.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What Sarah Maslowski actually tells agents who haven't started:

**Numbered list:**
1. **Script it with a teleprompter app, don't wing it.** It costs more time up front, but your
   thoughts come out cleaner and the editing goes faster.
2. **Talk about your own market, not a content calendar.** Neighborhoods, commute times, what
   surprises people when they move there. If you live there, you already have the material.
3. **Let the editor do the polishing.** Every stop, stumble, and retake disappears in a good
   edit. You only have to give it something to work with.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Clients already trust the voice you use with them.

**Subhead:**
The camera doesn't need a different one. That's the whole strategy behind the $140 million.

---

## Social Captions

### LinkedIn
Sarah Maslowski closed $140 million in real estate from YouTube with no paid ads, and her turning point was realizing she didn't have to perform on camera.

### Instagram
$140 million from YouTube, zero paid ads, and her whole shift was just showing up as herself.

### Facebook
She stopped trying to sound like a YouTube person and started talking the way she already talks to clients, and that's the $140 million strategy.

---

## Verified Tags

| Platform | Handle | Verification |
|---|---|---|
| Instagram | @youtubewithsarah (https://www.instagram.com/youtubewithsarah/) | Already verified in `data/guest-socials.json` (June 2026), carried forward per Step 6 without re-verification. On this exact episode, [00:11:53]-[00:12:00], Sarah states her own handle: "over on Instagram, my handle is YouTube with Sarah, and that is Sarah with an H," confirming the stored handle independently. |
| TikTok | @sarahmaslowski (https://www.tiktok.com/@sarahmaslowski) | Already verified in `data/guest-socials.json` (June 2026), carried forward per Step 6. |
| LinkedIn | linkedin.com/in/sarahmaslowski | Already verified in `data/guest-socials.json` (June 2026), carried forward per Step 6. |
| YouTube | "Moving to Georgia" (https://www.youtube.com/c/MovingtoGeorgia) | Already verified in `data/guest-socials.json` (June 2026), carried forward per Step 6. |
| Facebook | **VERIFY before posting** -- not found | `data/guest-socials.json` records Facebook as unverified (`null`). Left untagged per the never-guess rule. |

No update written to `data/guest-socials.json`: nothing new was verified, the stored June 2026
record was reused as-is per Step 6's "if the guest is there, use it and do not re-verify."

---

## Instagram Collab

Add Sarah Maslowski as a **Collaborator** using the verified @youtubewithsarah handle above.

---

## Post-publish DM

Send to Sarah (via her verified @youtubewithsarah Instagram) right after the post goes live:

> Hey Sarah, thanks for doing the YouTube Lab episode, "I don't have to be something that I'm
> not, I just have to show up as myself" is exactly the line agents who are scared of the camera
> need to hear. Made a carousel out of it and tagged you. Hope the course launch goes well.

No ask beyond the eventual Collab accept. No pitch, no mention of Kale.

---

## Data Source

Every claim traces to the episode transcript
(`keeping-it-real-content-system/data/transcripts/2026-10-21_item1_Sarah-Maslowski.txt`) and the
matching analysis JSON (`keeping-it-real-content-system/data/analysis/2026-10-21_item1_Sarah-Maslowski_analysis.json`),
aired 2026-10-21.

- **"Over $140 million in real estate directly from YouTube with no paid ads and no cold
  calling."**
  - Source: Sarah Maslowski, Keeping It Real, episode aired 2026-10-21, [00:03:03]-[00:03:12]
    (and restated in the cold open, [00:00:00]): "I have closed over $140 million in real estate
    directly from YouTube with no paid ads and no cold calling."
  - Who was measured: Sarah Maslowski's own stated production, not an independently audited
    figure. Corroborated by the analysis JSON's `production_level`: "$140M+ producer."
  - Status: confirmed, verbatim self-report, attributed to the guest by name, episode, and
    timestamp, consistent with Rule 1's "guest's direct observation from a specific, citeable
    interaction" standard. Rendered on the slides exactly as "$140 million," no rounding.

- **"I don't have to be something that I'm not. I just have to show up as myself."**
  - Source: Sarah Maslowski, [00:05:04]-[00:05:17], confirmed verbatim against both the raw
    transcript and the analysis JSON's `clip_worthy_moments` entry for this timestamp.
  - Status: confirmed, verbatim.

- **Teleprompter tactic** ("script your video before you film... your videos are cleaner, your
  thoughts are more organized, your editing is faster").
  - Source: Sarah Maslowski, [00:07:21]-[00:07:44].
  - Status: confirmed, close paraphrase of a verbatim on-air statement.

- **Market-knowledge content tip** ("if you live in your market, you already know more than
  enough to make a ton of videos... what are the best neighborhoods, what surprises people when
  they move there").
  - Source: Sarah Maslowski, around [00:08:33] per the analysis JSON's `problems_addressed`
    entry, corroborated against the raw transcript's matching passage.
  - Status: confirmed.

- **Guest facts** (Metro Atlanta Market, $140M+ producer).
  - Source: analysis JSON `guest_info` (`production_level: "$140M+ producer"`, `location: "Metro
    Atlanta Market"`), corroborated by Sarah's own line, [00:09:08]-[00:09:15]: "when I first
    started in the metro Atlanta market, I was one of the first agents making YouTube content
    here" (the raw transcript mis-renders this as "the metro at Lena Market"; the analysis JSON's
    structured `location` field and the audible phrase both confirm "Metro Atlanta Market").
  - Status: confirmed.

- **Fabrication audit:** One figure on the deck ($140 million), attributed to the named guest by
  episode and timestamp, presented as her own self-reported production, not an independently
  audited external statistic -- same standing as the Anna Kara deck's 99%/178 figures. No figures
  combined across separate claims. Her five-week YouTube course (opening 2026-10-22) was
  deliberately left off the deck: naming it would read as promoting a paid product on D.J.'s own
  account rather than crediting the guest's tactic, and it is not needed to make the one idea
  land.
