# Video Strategy To Grow D.J. Brand

A unified 6-day/week video content strategy combining two series -- **AI Agent Minute** and **Agent Tip of the Day** -- to build D.J. Paris's social media presence and recruit real estate agents to Kale Realty through the Keeping It Real Podcast brand.

---

## The Schedule

| Day | Series | Focus |
|-----|--------|-------|
| **Monday** | AI Agent Minute | Start the week with an actionable AI prompt |
| **Tuesday** | Agent Tip of the Day | Podcast guest wisdom and tactics |
| **Wednesday** | AI Agent Minute | Mid-week AI tactic |
| **Thursday** | Agent Tip of the Day | Guest insight to break up AI content |
| **Friday** | AI Agent Minute | "Try this over the weekend" AI prompt |
| **Saturday** | Agent Tip of the Day | Weekend-friendly, lighter content |
| _Sunday_ | _Off_ | |

---

## By the Numbers

| Metric | Count |
|--------|-------|
| Total scripts | 162 |
| AI Agent Minute scripts | 100 |
| Agent Tip of the Day scripts | 62 |
| Videos per week | 6 |
| Weeks of full 6-day content | ~21 |
| AI-only continuation after tips exhaust | ~13 more weeks |
| Total content runway | ~34 weeks (through Oct 2026) |

---

## Timeline

| Milestone | Date | Week |
|-----------|------|------|
| Series Launch | Mon Feb 23, 2026 | 1 |
| AI Tier 1+2 complete (top 33 scripts) | Fri May 8, 2026 | 11 |
| Agent Tips exhaust (all 62 scripts) | Thu Jul 16, 2026 | 21 |
| AI all 100 complete | Mon Oct 12, 2026 | 34 |

---

## The Two Series

### AI Agent Minute (100 scripts)
**Format:** D.J. Paris talking to camera, ~60 seconds
**Formula:** Do X -- Not Y -- To Get Z
**Focus:** Every script teaches agents how to use a specific AI tool (Claude, ChatGPT, Perplexity) for a real estate task
**Source:** Original scripts created for the Keeping It Real content system
**Ranked:** 1-100 by a composite of polish score, universal appeal, hook virality, and series positioning value

Scripts: [`scripts/ai-agent-minute/`](scripts/ai-agent-minute/)
Rankings: [`rankings/ai-agent-minute-rankings.md`](rankings/ai-agent-minute-rankings.md)

### Agent Tip of the Day (62 scripts)
**Format:** D.J. Paris presenting guest wisdom from Keeping It Real podcast episodes, ~60 seconds
**Focus:** Real-world tactics, mindset shifts, and systems from top-producing agents
**Source:** Extracted from 700+ podcast episodes, quality-gated (scores 7-10 out of 10)
**Ranked:** By score and diversity optimization (guest, avatar, and content pillar variety)
**Guests:** 23 unique podcast guests represented

Scripts: [`scripts/agent-tip-of-the-day/`](scripts/agent-tip-of-the-day/)
Rankings: [`rankings/agent-tip-rankings.md`](rankings/agent-tip-rankings.md)

---

## Quick Links

- [Master Calendar (day-by-day schedule)](schedule/master-calendar.md)
- [Weekly Breakdown](schedule/weekly-breakdown.md)
- [AI Agent Minute Rankings (1-100)](rankings/ai-agent-minute-rankings.md)
- [Agent Tip Rankings (1-62)](rankings/agent-tip-rankings.md)
- [Avatar Profiles](docs/avatars.md)
- [Content Pillars](docs/content-pillars.md)
- [Filming Guide](docs/filming-guide.md)

---

## After the Tips Run Out (Week 21+)

Agent Tip scripts exhaust around July 16, 2026. Three options:

1. **Pull from the bench.** There are 38 additional evaluated podcast scripts (scored but not published) plus 595 clip-worthy moments already extracted from the podcast archive. Many can be polished into new Agent Tip scripts.

2. **Generate new tips.** The Keeping It Real content system has a complete prompt pipeline (clip hunter > script writer > kill judge) that can process any of the 700+ podcast episodes into new scripts.

3. **Switch to 5-day/week.** Drop Saturday and continue with AI Agent Minute on M/W/F plus a new or modified series on T/Th.

**Recommendation:** Start evaluating Option 1 by June 1 (6 weeks before exhaustion).

---

## Build System

All generated content (scripts, calendar, rankings) is produced by `build.py`:

```bash
python3 build.py
```

This reads source data from the `keeping-it-real-content-system` repo and generates everything. Re-run if scripts are added, reordered, or the start date changes.

**Dependencies:** Python 3 standard library only. macOS required (uses `textutil` for RTF conversion).

---

## Repository Structure

```
video-strategy-to-grow-dj-brand/
├── README.md                     # This file
├── build.py                      # Generates all content from sources
├── scripts/
│   ├── ai-agent-minute/          # 100 markdown files (001-100, rank-ordered)
│   └── agent-tip-of-the-day/     # 62 markdown files (001-062, rank-ordered)
├── schedule/
│   ├── master-calendar.md        # Day-by-day posting schedule
│   └── weekly-breakdown.md       # Week-by-week themes + avatar coverage
├── rankings/
│   ├── ai-agent-minute-rankings.md
│   └── agent-tip-rankings.md
└── docs/
    ├── avatars.md                # 6 agent persona profiles
    ├── content-pillars.md        # 5 content pillar definitions
    └── filming-guide.md          # Equipment, session planning, platform specs
```

---

*Built: February 23, 2026 | Source: Keeping It Real Content Intelligence System*
