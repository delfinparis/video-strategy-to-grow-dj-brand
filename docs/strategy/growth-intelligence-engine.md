# Growth Intelligence Engine

A weekly engine that scours a curated watchlist of creator-growth sources, extracts the concrete tactics worth knowing about, and scores each one against D.J. Paris's actual situation, so the output is "here are two things to try this week," not "here are forty hours of video to watch."

Built 2026-06-13. Runs via [`scripts/growth_digest.py`](../../scripts/growth_digest.py).

---

## Why this exists

Following the right channels gives good signal. The bottleneck is consumption: nobody has time to watch eight YouTube channels and four podcasts a week and translate them into action. This engine moves the work from "watch everything, then decide" to "review a ranked one-page digest, then decide."

The differentiator over just subscribing is the **scoring layer**. A generic growth tip ("end every video telling people to follow you") is good advice for most creators and a direct violation of D.J.'s [editorial standards](../editorial-standards.md). The engine knows the difference and files that tactic under **Skip** with the reason, so D.J. sees what the playbooks push without absorbing the parts that would undercut the brand.

---

## What it does, step by step

1. **Resolve the watchlist.** Handles and show names (not brittle IDs) resolve to feeds at runtime, via the YouTube channel page and the iTunes Search API. Resolutions are cached. Anything that fails to resolve is reported in the digest, never faked.
2. **Pull what's new** in the last 7 days across YouTube uploads, podcast episodes, and top-of-week Reddit threads. A seen-cache prevents re-surfacing the same item next week.
3. **Fetch the substance.** YouTube captions (via `youtube-transcript-api`) for the newest videos, podcast show notes, Reddit post bodies. If captions aren't available, it falls back to the video description.
4. **Extract + score with Claude.** The model pulls concrete tactics (ignoring "be consistent" filler) and assigns each a verdict, a fit score, a novelty score, and a "how D.J. runs this" note, all grounded in the context block below.
5. **Write the digest** to `data/growth-digests/YYYY-Www.md`, grouped into three buckets.

---

## The three buckets

| Bucket | Meaning |
|---|---|
| **1. Implement this week** | High fit for D.J.'s platforms and goal, breaks none of his rules. Pick one or two. |
| **2. Adapt with caution** | Good underlying idea, but needs reshaping (wrong platform, or a rule conflict that can be engineered around). The digest says what to change. |
| **3. Skip -- conflicts rules** | What the growth playbooks push that D.J. should ignore on purpose. Mostly engagement-ask CTAs. Listed so the decision to skip is conscious, not accidental. |

An empty "Implement" bucket is a valid week. The [WOW gate](../editorial-standards.md) logic applies here too: don't force a tactic into a slot.

---

## The scoring rubric

Every tactic is judged against D.J.'s real context, which the script hands to the model on every run (kept in sync with [`README.md`](../../README.md) and [`editorial-standards.md`](../editorial-standards.md)):

- **Recruiting-first goal.** Audience growth only matters insofar as it serves Chicago-agent recruiting for Kale, then the NAR relationship, podcast growth, and national reach, in that order.
- **Platform priority.** Personal LinkedIn first, then personal Facebook, then personal Instagram, then brand YouTube, with TikTok as a short-form test surface. A tactic that only pays off on a platform D.J. deprioritizes scores lower.
- **Hard editorial rules as auto-flags.** A tactic that requires an engagement-ask CTA, a fabricated or "plausible specific" stat, em dashes, AI-speak, or burned-in on-screen text (captions.ai renders audio only) is flagged as a conflict and routed to **Adapt** or **Skip**, never **Implement**.
- **Novelty.** Generic advice is filtered out. Only tactics with a concrete, executable mechanic survive.

---

## The watchlist

Edit the lists at the top of [`scripts/growth_digest.py`](../../scripts/growth_digest.py) to tune the feed.

**YouTube**
- Colin and Samir -- creator economy and platform changes
- Creator Science (Jay Clouse) -- tactical systems, best signal-to-noise
- Think Media (Sean Cannell) -- YouTube growth for creator-businesses
- Modern Millie -- tactics for small and mid-size channels
- Roberto Blake -- creator business and YouTube growth
- Jade Beason -- social strategy, short-form, monetization
- Katie Steckly -- content systems and repurposing for solo creators
- Hook Point (Brendan Kane) -- hooks and short-form retention

**Podcasts**
- Creator Science (Jay Clouse)
- The Colin and Samir Show
- Online Marketing Made Easy (Amy Porterfield)
- The Jasmine Star Show

**Reddit**
- r/NewTubers, r/socialmedia, r/InstagramMarketing, r/content_marketing, r/TikTokMarketing

**Maintenance.** If a YouTube creator changes their handle, resolution 404s and the failure is listed in the digest. Update the handle in the script. Verify a handle by opening `youtube.com/@handle` in a browser. The same applies to a renamed podcast or a dead subreddit.

---

## Running it

```bash
# one-time: install deps
pip install feedparser anthropic youtube-transcript-api
export ANTHROPIC_API_KEY=sk-ant-...

# normal weekly run
python3 scripts/growth_digest.py

# wider window / cheaper run / raw list
python3 scripts/growth_digest.py --lookback 14
python3 scripts/growth_digest.py --no-transcripts
python3 scripts/growth_digest.py --no-llm
```

Cost is roughly five to fifteen cents per run on `claude-sonnet-4-6`. Sonnet (not Haiku) is used on purpose: deciding whether a tactic quietly violates an editorial rule is a judgment job. `--no-transcripts` roughly halves the cost on slow weeks.

---

## Scheduling and the hosting decision

The engine runs **locally via launchd**, weekly on Monday at 6:00am. Setup is in [`scripts/com.djparis.growthdigest.plist.template`](../../scripts/com.djparis.growthdigest.plist.template), mirroring the existing daily `news_brief` job.

Local, not cloud, is deliberate. YouTube caption fetching and Reddit pulls are far more reliable from a residential IP than a cloud datacenter IP, the same constraint that forces the [voice-tuning workflow](../../README.md) to download locally. A cloud cron routine is possible but would intermittently fail to fetch transcripts, which are the engine's richest input. If the Mac is asleep at the scheduled time, launchd runs the job when it next wakes.

---

## How this fits the repo

The digest is an **input to ideation**, parallel to the daily [`news_brief.py`](../../scripts/news_brief.py). News brief answers "what should I make a video about." Growth digest answers "how should I make and distribute it better." Neither writes content. Both feed the human decision.

*Built 2026-06-13. Next watchlist review: fold into the 2026-07-19 pivot review.*
