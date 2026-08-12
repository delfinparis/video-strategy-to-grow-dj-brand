# The Today digest

One email, every morning, that says what to film and what to post. It exists because the
producing routines had grown to five, each emailing its own draft, and nobody was telling
D.J. what the day actually looked like. He was assembling it from his inbox before filming.

**Routine:** `trig_01B6JsoWwqNzPdazGecXDjEZ`, daily at **10:15am CT**, after every producer
has finished. Gmail draft only, never sent.

**Subject: `Today - <Wed Aug 12>`.** It must never start with "Walk & Talk Options" — an
Apps Script in that mailbox auto-sends any draft whose subject begins with that string, and
this one is meant to be read, not sent.

## What it reads

It creates nothing. Everything it reports was already built and pushed by something else.

| Section | Source |
|---|---|
| **Film today** | The morning `Walk & Talk Options` Gmail draft, one line per option |
| **Post today** | `scripts/carousels/*.md` with today's `generated:` date, cross-checked against `git log --since="18 hours ago"` |
| **Anything else** | Podcast promos, spotlights, walk-and-talk scripts pushed today |
| **Needs a human** | Only appears when there is something in it |

For a **KIRP deck it leads with the amplification block** — verified handles, the Instagram
Collab instruction, the post-publish DM — because the reshare is the mechanism and the
slides are just the gift that triggers it. Anything marked `VERIFY before posting` gets
flagged loudly.

## What it will tell you is broken

The digest is also the daily health check, which is most of why it earns its slot:

- A slot in the 14-a-week grid that nothing filled
- A carousel whose markdown exists but whose slides never rendered
- A `[STAT NEEDED]` or unsourced claim in something generated today
- A handle that could not be verified
- **Two rows for the same date in the rotation table**, or a Carousel column filled for an
  entry no video covered. That table is written by two engines plus D.J., so a collision
  shows there first.

An empty slot is reported as empty. The digest never invents a post to fill the grid.

## The take pairing

On **Mon, Wed and Fri** the morning brief now carries exactly one `[TAKE]` option, drawn
from [`sacred-cows.md`](../../data/sacred-cows.md) with the slot's heat and hook family from
[`take-standard.md`](../series/take-standard.md). The 9:00am carousel builds the same belief,
so video and carousel land together.

The brief runs at 5:30am and the carousel at 9:00am, so the ordering works: if D.J. picks
the take, the entry is claimed before the carousel looks. **The brief does not write the
rotation row** — the entry is only claimed if he actually picks that option. If he picks
something else, the carousel claims its own entry and a video pairs onto it another day.

The digest checks this: on a Mon/Wed/Fri with no `[TAKE]` option, it says so, because that
means the pair will not happen.
