---
lane: "stat"
carousel_for: "Meta's Claire Bauman and Mina Khan, at Zillow Unlock 2026: viewers decide to keep watching or scroll within four tenths of a second, so the hello and your name are the first thing to cut"
hook_family: "data-card"
heat: 3
slide_count: 5
goal: "engagement"
generated: "2026-10-29"
theme: "light"
---

# Carousel: four tenths of a second

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`kirp-guest-tip` (`last_used: 2026-10-26`), built as the companion deck,
`KIRP-2026-10-29-ai-will-expose-you-carousel.md`. The second-oldest ties at `last_used:
2026-10-27` between `stat` and `do-this-dont-do-that`; resolved to `stat` (first-listed of the
tie in the rotation file's `topics` array).

Source per Step 2(d): no news brief exists newer than `data/news-briefs/2026-10-20.md` (today is
2026-10-29), and `data/news-briefs/stat-bank.json` does not exist in this repo. Went to a
walk-and-talk script committed in the last two days instead:
`scripts/unlock-insights/UNLOCK-36-four-tenths-of-a-second.md`, one of the Zillow Unlock 2026
reels committed 2026-10-27. Checked `scripts/carousels/*.md` for "four tenths," "0.4 seconds,"
and "Claire Bauman" first -- no prior deck covers this session.

**The one idea:** at Zillow Unlock 2026, Meta's Claire Bauman and Mina Khan said viewers decide
whether to keep watching a video or keep scrolling within four tenths of a second. That means
the hello, the name, and the warm-up most agent videos open with are already costing the view
before the point ever arrives. The fix is structural, not stylistic: open on what the viewer
cares about, keep the face centered where roughly 60% of viewing attention stays, and cut
everything before the hook. Same caveat the source script carries: the figure comes from
Zillow's AI-written session summary, and no independent public report was found naming Meta's
own source for the 0.4-second number; it is presented as reported from the named session, the
way the shipped walk-and-talk already presents it.

Hook family `data-card` (the number is the whole slide), differing from the two most recently
committed decks before today (`myth-bust`, `one-tactic-breakdown`, 2026-10-28) and from today's
companion deck (`contrast`).

---

## SLIDE 1 -- HOOK
**Headline:**
Your video gets 0.4 seconds.

**Subhead:**
That's the whole window before someone decides to keep watching or scroll past.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
At Zillow Unlock, Meta's own team said viewers decide to keep watching or scroll within four tenths of a second.

**Subhead:**
Your name hasn't even finished by then.

---

## SLIDE 3 -- THE TURN
**Headline:**
The fix isn't a better video. It's a better first frame.

**Body:**
Meta's Claire Bauman and Mina Khan, at Zillow Unlock 2026: viewers decide almost instantly,
within **0.4 seconds**, whether to keep watching. They also flagged that roughly 60% of viewing
attention stays in the center of the frame, away from the platform's own buttons. Put those two
together and the lesson is specific: skip the hello and your name, open on what the viewer
actually cares about, and keep your face in the middle of the shot.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Fix your next video before you film it:

**Numbered list:**
1. **Cut the hello and your name.** Open on frame one with the point, not the warm-up.
2. **Lead with what the viewer cares about.** Not what you want to tell them first.
3. **Keep your face centered in the frame.** That's where the attention actually sits.
4. **Pull up your last video and watch the first second.** If it's a greeting, that view was
   already gone before you said anything useful.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
You don't get a warm-up. You get four tenths of a second.

**Subhead:**
Spend it on the point, not the hello.

---

## Social Captions

### LinkedIn
Meta told agents at Zillow Unlock that viewers decide to keep watching or scroll within four tenths of a second, so the hello is the first thing to cut.

### Instagram
Watch the first second of your last real estate video and ask honestly if it would stop you from scrolling.

### Facebook
If your video opens with your name before the point, you're losing the viewer before they know what it's about.

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| Viewers decide to keep watching or scroll within four tenths (0.4) of a second | Yes, slides 1-3, 5 | Claire Bauman (Client Solutions Manager, Meta) and Mina Khan (Creative Strategist, Meta), "Go From Liked to Trusted: Create the Kind of Social Presence that Earns the Call," Impact Session, Zillow Unlock 2026, Day 2, Wed Oct 14 2026: "users decide whether to keep watching almost instantly (within 0.4 seconds)." https://www.unlockconference.com/session-insights/go-from-liked-to-trusted-create-the-kind-of-social-presence-that-earns-the-call/ | Reported by named speakers at a specific, citeable session. The figure comes from Zillow's AI-written session summary; no independent public report naming Meta's own source for the 0.4-second figure was located for this build. Presented as reported from the named session, same caveat as the source walk-and-talk script `scripts/unlock-insights/UNLOCK-36-four-tenths-of-a-second.md` |
| Roughly 60% of viewing attention stays in the center "safe zone" of the frame | Yes, slide 3 | Same session: "Keep key messages, text, and faces within the central 'safe zone' (roughly a 4:5 box) since about 60% of viewing attention stays in that middle area and avoids being covered by platform UI buttons." | Same status as above |

**Do-not-cite check:** no lender, platform, brokerage, or person other than the two named Meta
speakers is referenced anywhere in this file. Meta's own Edits app, demoed in the same session,
is deliberately left off the deck -- no product pitch.

**Reuse note:** repurposed from `scripts/unlock-insights/UNLOCK-36-four-tenths-of-a-second.md` (a
Zillow Unlock 2026 walk-and-talk, not a Keeping It Real podcast guest). No `kirp_guest` flag; no
`source_script` field since this is a carousel-native repackage of a different series' script,
same facts, same sourcing, no new claims.
