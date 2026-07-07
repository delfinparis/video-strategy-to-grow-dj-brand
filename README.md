# Video Strategy To Grow D.J. Brand

A short-form video content strategy whose **primary purpose is generating warm recruiting leads for Kale Realty** through D.J. Paris's personal social presence and the Keeping It Real Podcast brand.

> **Current phase: Inside the Industry pivot (decided 2026-04-18, 90-day test through 2026-07-19).**
> Socials are now centered on industry news, access, and synthesis - not a four-pillar mix. See [`docs/strategy/2026-04-18-pillar-pivot-decision.md`](docs/strategy/2026-04-18-pillar-pivot-decision.md) for the full decision and the data that drove it. This README reflects the post-pivot cadence; the next review is 2026-07-19.

---

## Positioning

> D.J. Paris is the industry insider for real estate agents who don't have time to read 12 real estate newsletters. He sees what's happening across the industry, has a take, and tells you what it means for your business in 60 seconds.

**Podcast promise:** deep interviews with top producers on how to be a better agent.
**Socials promise:** sharp takes on industry news, access moments, and patterns from 700+ interviews - in 60 seconds or less.

The two surfaces answer different questions and don't cannibalize. Both reinforce the same credibility pillars: NAR access, 700-episode podcast archive, Kale operational view.

---

## Brand Goals (priority order)

1. **Kale Realty recruiting in Chicago** - primary, most valuable, drives D.J.'s compensation
2. NAR relationship deepening
3. Keeping It Real Podcast subscriber growth
4. National thought leader reach

Every strategy decision is filtered through "does this serve #1?" first. The content-to-recruiting bridge is documented in [`docs/content-recruiting-integration.md`](docs/content-recruiting-integration.md) - read that before making any content strategy decision.

---

## The Schedule

| Day | Primary slot | Fallback / substitute |
|---|---|---|
| **Mon** | KIR Podcast Promo (new episode) | - |
| **Tue** | **Inside the Industry - News (NF)** | IS (synthesis) if news slow |
| **Wed** | **Inside the Industry - News (NF)** or **The Playbook** | Whichever is timelier |
| **Thu** | **Inside the Industry - News (NF)** | - |
| **Fri** | **AI Tip of the Week → tapthis.co** | - |
| **Sat** | **Inside the Industry - News (NF)** | IA (Access) when D.J. attended something notable |
| _Sun_ | _Off_ | - |

**Weekly volume:** 6 posts, ~67% news-commentary focus.

- **4 NF slots/week** minimum (Tue, Wed-when-news, Thu, Sat)
- **1 KIR podcast promo/week** (Mon)
- **1 AI Tip of the Week/week** (Fri) - the sole slot with a direct tapthis.co CTA
- **Playbook** = conditional Wed slot (~2x/month when scenario content is timelier than news)
- **IA (Access)** = opportunistic Sat substitute (~1–2x/month)
- **IS (Synthesis)** = quiet-week backfill (~2x/month)

See [`schedule/master-calendar.md`](schedule/master-calendar.md) for the day-by-day schedule.

---

## Pillar Status (post-pivot)

| Pillar | Status | Role |
|---|---|---|
| **Inside the Industry** | **Primary, actively extending** | 4 slots/week across NF/IA/IS sub-types |
| **The Playbook** | Keep, reframed | Conditional Wed slot; "Inside the Industry: The Playbook" framing |
| **KIR Podcast Promo** | Active | Mon cross-promotion; Thu teaser optional |
| **AI Tip of the Week** | Active utility slot | Fri only; drives tapthis.co for recruiting pixel retargeting |
| **Agent Tip of the Day** | Curate heavily | Keep only named-guest credential tips; mothball the rest |
| **AI Agent Minute** | **Frozen** | 100 audited scripts in place; re-home plan due 2026-06-01 |

See [`docs/content-pillars.md`](docs/content-pillars.md) and [`docs/strategy/2026-04-18-pillar-pivot-decision.md`](docs/strategy/2026-04-18-pillar-pivot-decision.md) for full definitions.

---

## Platform Priority

Personal accounts dramatically outperform brand accounts for Kale recruiting. Metricool baseline (April 2026):

| Platform | Followers | Audience Quality | Priority |
|---|---|---|---|
| **Personal LinkedIn** | 7,001 | 49% Greater Chicago, 31% Real Estate, 34% Senior, every major Chicago brokerage represented | **#1** |
| **Personal Facebook** | 2,878 | 74.2% Chicago, +122% engagement growth | **#2** |
| **Personal Instagram** | 7,569 | 16,304 views/30 days, 72.2% non-follower reach | **#3** |
| **Brand YouTube** (Keeping It Real) | 2,440 | Largest brand audience, 700-episode archive | **#4** |
| **TikTok (brand)** | - | Strongest engagement-rate surface for IIR content | utility |
| **Facebook (brand)** | - | Secondary distribution | utility |

See [`docs/platform-strategy.md`](docs/platform-strategy.md) for the full distribution cascade.

---

## The Recruiting Funnel

The bridge from content to a Kale conversation:

```
Fri AI Tip of the Week ─┐
IIR posts w/ soft CTA ─┼─► tapthis.co ─► 5 pixels fire ─► 30-90d retargeting
KIR podcast promo ─┘ (Meta, Google, LinkedIn, Reddit, TikTok)
 │
 ▼
 joinkale.com ─► webinar ─► book-a-call
 │
 ▼
 Close CRM (Jennica → Ana → D.J.)
```

**Leading indicator:** weekly tapthis.co clicks (feeds the retargeting audience).
**Lagging indicator:** Kale book-a-call volume 30-90 days later.

Full spec (metrics per stage, attribution model, Sunday ritual, alert thresholds): [`docs/analytics/recruiting-funnel-dashboard.md`](docs/analytics/recruiting-funnel-dashboard.md).

---

## By the Numbers (as of 2026-04-19)

| Series | Scripts in repo | Status |
|---|---:|---|
| Inside the Industry (NF/IA/IS) | 14 | Primary, extending |
| The Playbook | 3 | Pilot, 1x/week conditional |
| AI Tip of the Week | 2 | Active, 1x/week |
| Agent Tip of the Day | 62 | Curation pending |
| AI Agent Minute | 100 | Frozen |
| Podcast promos | 1 | Active, 1x/week |

**Content runway:** Inside the Industry is effectively unlimited - NF is fed by a daily news brief ([`scripts/news_brief.py`](scripts/news_brief.py)), IS is fed by the 700-episode podcast archive, IA by D.J.'s actual industry calendar. Pre-drafted IS queue target: ~6 weeks for slow-news-week backfill.

---

## 90-Day Pivot Test

| Milestone | Date |
|---|---|
| Pivot start | 2026-04-21 |
| Mid-test check-in | 2026-06-02 |
| End-of-test review | 2026-07-19 |

Success, reversal, and adjustment criteria are defined in [`docs/strategy/2026-04-18-pillar-pivot-decision.md`](docs/strategy/2026-04-18-pillar-pivot-decision.md). All posts are logged in [`data/publishing-log.csv`](data/publishing-log.csv); weekly metrics snapshots land in [`data/metrics/`](data/metrics).

---

## Quick Links

- **[2026-04-18 Pillar Pivot Decision](docs/strategy/2026-04-18-pillar-pivot-decision.md) - current governing document**
- [2026-04-18 Cross-Surface Analytics Synthesis](docs/analytics/2026-04-18-cross-surface-synthesis.md) - the data that drove the pivot
- [Recruiting Funnel Dashboard (spec)](docs/analytics/recruiting-funnel-dashboard.md) - metrics per stage + Sunday review ritual
- [Master Calendar](schedule/master-calendar.md) - post-pivot schedule through 2026-07-19
- [Content → Recruiting Integration](docs/content-recruiting-integration.md)
- [Editorial Standards](docs/editorial-standards.md) - required reading before writing any script
- [Inside the Industry Standard](docs/series/inside-the-industry-standard.md) - primary series standard
- [The Playbook Format Guide](docs/the-playbook-format.md)
- [Platform Strategy](docs/platform-strategy.md) - includes the mid-2026 algorithm refresh
- [Caption & Hashtag Strategy](docs/caption-and-hashtag-strategy.md)
- [Myths That Don't Move the Needle](docs/myths-that-dont-move-the-needle.md) - 2026 myth-busting checklist
- [Filming Guide](docs/filming-guide.md) *(to be updated for 4x/week reactive cadence)*
- [CapCut Editing Playbook](docs/capcut-editing-playbook.md)
- [Avatar Profiles](docs/avatars.md)

---

## Build System

Scripts, calendar, and rankings for the original two series (AI Agent Minute, Agent Tip of the Day) are generated by `build.py`:

```bash
python3 build.py
```

This reads source data from the `keeping-it-real-content-system` repo. Re-run when scripts are added, reordered, or the start date changes.

News briefing:

```bash
python3 scripts/news_brief.py
```

Produces a daily LLM-triaged top-5 stories brief to `data/news-briefs/YYYY-MM-DD.md` with angle suggestions for NF scripts. Use `--no-llm` for a raw feed pull.

Growth-intelligence digest:

```bash
python3 scripts/growth_digest.py
```

Weekly companion to the news brief. Scours a curated watchlist of creator-growth sources (YouTube, podcasts, Reddit), extracts concrete tactics, and scores each against D.J.'s platform priority, recruiting-first goal, and editorial rules. Output lands in `data/growth-digests/YYYY-Www.md`, grouped into Implement / Adapt / Skip. Where the news brief answers "what to make a video about," this answers "how to make and distribute it better." Full spec: [`docs/strategy/growth-intelligence-engine.md`](docs/strategy/growth-intelligence-engine.md).

**Note:** The Playbook, Inside the Industry, AI Tip of the Week, and podcast promos are hand-authored in their respective `scripts/` subfolders and not yet integrated into `build.py`.

**Dependencies:** Python 3 standard library only. macOS required (`textutil` for RTF).

---

## Repository Structure

```
video-strategy-to-grow-dj-brand/
├── README.md # This file
├── build.py # Generates AIAM + Agent Tip content
├── generate_descriptions.py # Generates platform-specific descriptions
├── sync_descriptions_to_notion.py
├── scripts/
│ ├── inside-the-industry/ # PRIMARY: IA, IS, NF scripts
│ ├── the-playbook/ # Conditional Wed scenarios
│ ├── ai-tip-of-the-week/ # Fri utility slot → tapthis.co
│ ├── podcast-promos/ # Mon KIR episode drops
│ ├── agent-tip-of-the-day/ # Curation pending
│ ├── ai-agent-minute/ # Frozen (100 scripts)
│ ├── reels/ # Generated reel assets
│ ├── bonus/
│ ├── news_brief.py # Daily news-feed triage
│ ├── com.djparis.newsbrief.plist.template
│ ├── growth_digest.py # Weekly creator-growth tactic digest
│ └── com.djparis.growthdigest.plist.template
├── data/
│ ├── publishing-log.csv # Every post, for attribution
│ ├── metrics/ # Weekly snapshots YYYY-WW.csv
│ ├── news-briefs/ # Daily news briefs
│ └── growth-digests/ # Weekly growth-intelligence digests
├── descriptions/
│ ├── ai-agent-minute/
│ └── agent-tip-of-the-day/
├── schedule/
│ ├── master-calendar.md
│ └── weekly-breakdown.md
├── rankings/
├── docs/
│ ├── strategy/ # Pivot decisions and governance
│ ├── analytics/ # Cross-surface data + reports
│ ├── series/ # Per-series editorial standards
│ ├── audits/
│ ├── close-email-templates/
│ ├── editorial-standards.md # Universal editorial rules
│ ├── content-pillars.md
│ ├── content-recruiting-integration.md
│ ├── inside-the-industry-playbook.md
│ ├── the-playbook-format.md
│ ├── platform-strategy.md
│ ├── filming-guide.md
│ ├── capcut-editing-playbook.md
│ ├── avatars.md
│ ├── speaker-assets.md
│ ├── recruiting-call-scripts.md
│ └── mentor-stories-collection.md
```

---

*Built: 2026-02-23 | Inside the Industry pivot: 2026-04-18 | Next review: 2026-07-19 | Source: Keeping It Real Content Intelligence System*
