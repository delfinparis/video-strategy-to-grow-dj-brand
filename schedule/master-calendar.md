# Master Content Calendar

> **Post-pivot cadence in effect from Mon Apr 20, 2026.** See [`../docs/strategy/2026-04-18-pillar-pivot-decision.md`](../docs/strategy/2026-04-18-pillar-pivot-decision.md) for the governing decision and the 90-day test plan through 2026-07-19. This file is **hand-maintained** - `build.py` no longer writes it (step 8 disabled 2026-04-19).

---

## Post-Pivot Cadence (Apr 20, 2026 onwards)

**Primary pillar:** Inside the Industry (NF/IA/IS sub-types)
**Weekly volume:** 6 posts, Sunday off
**Crosspost surfaces:** 6 retained (LI Personal, FB Personal, FB Biz, IG Personal, TT Biz, YT Biz)

| Day | Primary slot | Fallback |
| --- | --- | --- |
| **Mon** | KIR Podcast Promo (this week's episode) | - |
| **Tue** | **IIR - News (NF)** | IS (synthesis) if news slow |
| **Wed** | **IIR - News (NF)** or **The Playbook** | whichever is timelier |
| **Thu** | **IIR - News (NF)** | - |
| **Fri** | **AI Tip of the Week → tapthis.co** | - |
| **Sat** | **IIR - News (NF)** | IA (Access) if D.J. attended something notable |

**Target weekly volume:** 4 NF + 1 KIR promo + 1 AI Tip. The Playbook is a conditional Wed substitute (~2x/month). IA is an opportunistic Sat substitute (~1–2x/month). IS is a quiet-week backfill on any NF slot (~2x/month).

**News input:**
- Daily brief: `python3 scripts/news_brief.py` → `data/news-briefs/YYYY-MM-DD.md`
- Manual scan: Feedly subscription with 10 real estate news feeds
- Insider signals: NAR access + Kale operational view

---

## Content Inventory (as of 2026-04-19)

| Series | Ready in repo | Cadence | Notes |
|---|---:|---|---|
| IIR - News (NF) | 1 (NF-006) | 4x/week | NF-001 to NF-005 posted (see below); news_brief.py feeds new NF |
| IIR - Access (IA) | 4 (IA-001 to IA-004) | ~1–2x/month (Sat) | Sat substitute when D.J. attends notable events |
| IIR - Synthesis (IS) | 4 (IS-001 to IS-004) | ~2x/month | Quiet-week Tue/Thu backfill |
| The Playbook (PB) | 3 (PB-001 to PB-003) | Wed conditional | Pilot batch; bench exhausts after May 6 |
| AI Tip of the Week (AIT) | 1 (AIT-001) | 1x/week (Fri) | Fri slots after Apr 24 pull from 100 AIAM bank |
| KIR Podcast Promo | 0 fresh | 1x/week (Mon) | Each Mon drops the week's new episode; one stale webinar promo in repo |
| AIAM (frozen) | 100 | - | Not posting new; feeds AI Tip of the Week selection |
| Agent Tip of the Day | 62 + 2 (064a/064b, ready) | - | 064a/064b inserted into Mon/Tue 4/20-4/21 as AI-tells variants; older curation pending |

---

## Pre-Pivot Posting Record (Apr 10 – Apr 19, 2026)

Five Inside the Industry scripts shipped under the pre-pivot 2x/week IIR cadence:

| Date | Day | Script | Status |
|---|---|---|---|
| Apr 10 | Fri | [NF-001 - NAR Settles Tuccori for $52M](../scripts/inside-the-industry/NF-001-nar-tuccori-settlement-52-million.md) | ✅ Posted |
| Apr 12 | Sun | [NF-002 - Commissions Were Supposed to Drop](../scripts/inside-the-industry/NF-002-commissions-were-supposed-to-drop.md) | ✅ Posted |
| Apr 14 | Tue | [NF-003 - The $470 Million Question](../scripts/inside-the-industry/NF-003-the-470-million-question.md) | ✅ Posted |
| Apr 16 | Thu | [NF-004 - The Batton Case Is Still Out There](../scripts/inside-the-industry/NF-004-the-batton-case-is-still-out-there.md) | ✅ Posted |
| Apr 19 | Sun | [NF-005 - Douglas Elliman Quietly Settled Too](../scripts/inside-the-industry/NF-005-elliman-quietly-settled-too.md) | Scheduled today (1 day late from original Sat Apr 18) - last pre-pivot IIR post |

AI Agent Minute and Agent Tip reels posted Apr 4–17 are backfilled in [`../data/publishing-log.csv`](../data/publishing-log.csv) with "confirm" flags - reconcile at your leisure; they do not block the forward schedule.

---

## Post-Pivot Schedule: Apr 20 – Jul 18, 2026

90-day test window. Fri Jul 19 is the end-of-test review. Scripts marked TBD get filled weekly from `news_brief.py` (NF), KIR episode drops (Mon), and the AIAM bank (Fri). All posts log to [`../data/publishing-log.csv`](../data/publishing-log.csv).

### Week 9: Apr 20 – Apr 25, 2026 *(pivot week 1)*

| Date | Day | Slot | Script | Notes |
|---|---|---|---|---|
| Apr 20 | Mon | ATOTD | [ATOTD 064a - Stop Letting ChatGPT Write Your Emails](../scripts/reels/agent-tip-of-the-day/064a-stop-letting-chatgpt-write-your-emails.md) | Inserted 2026-04-20 -- KIR Promo slot retired (low value to recruiting audience per DJ) |
| Apr 21 | Tue | ATOTD | [ATOTD 064b - Keep AI Off Your Voicemail](../scripts/reels/agent-tip-of-the-day/064b-keep-ai-off-your-voicemail.md) | Inserted 2026-04-20 -- displaces NF-006 to Thu |
| Apr 22 | Wed | The Playbook | [PB-001 - Lowball Offer](../scripts/the-playbook/PB-001-lowball-offer.md) | Wed Playbook rotation |
| Apr 23 | Thu | IIR - NF | [NF-006 - Five Brokerages Settled Scoreboard](../scripts/inside-the-industry/NF-006-five-brokerages-settled-scoreboard.md) | Displaced from Tue 4/21 by 064b insert |
| Apr 24 | Fri | AI Tip | [AIT-001 - I Want to Think About It (Claude Roleplay)](../scripts/ai-tip-of-the-week/001-i-want-to-think-about-it-claude-roleplay.md) | First Fri → tapthis.co |
| Apr 25 | Sat | IIR - IA | [IA-001 - Room With NAR Executive Team](../scripts/inside-the-industry/IA-001-room-with-nar-executive-team.md) | Sat IA substitute |

**Unscheduled bonus NFs filmed but not yet slotted:** [NF-007 (Chicago vs buyer's market)](../scripts/inside-the-industry/NF-007-home-sellers-cutting-prices.md) and [NF-008 (eXp / Zillow RESPA)](../scripts/inside-the-industry/NF-008-exp-zillow-respa-next-wave.md). Both filmed 2026-04-20. Slot into next available TBD NF slots (Apr 28 Tue and Apr 30 Thu) before those go stale.

### Week 10: Apr 27 – May 02, 2026

| Date | Day | Slot | Script | Notes |
|---|---|---|---|---|
| Apr 27 | Mon | KIR Promo | TBD | |
| Apr 28 | Tue | IIR - NF | [NF-007 - Chicago Didn't Get the Buyer's Market Memo](../scripts/inside-the-industry/NF-007-home-sellers-cutting-prices.md) | Filmed 4/20; slot here before it goes stale |
| Apr 29 | Wed | The Playbook | [PB-002 - Listing Agent Won't Return Calls](../scripts/the-playbook/PB-002-listing-agent-not-returning-calls.md) | |
| Apr 30 | Thu | IIR - NF | [NF-008 - Commission Chapter Is Closing, Kickback Chapter Is Opening (eXp RESPA)](../scripts/inside-the-industry/NF-008-exp-zillow-respa-next-wave.md) | Filmed 4/20; RESPA case is still active, still relevant |
| May 01 | Fri | AI Tip | [AIT-002 - Re-engage Ghosted Leads (3-Touch Sequence)](../scripts/ai-tip-of-the-week/002-re-engage-ghosted-leads-three-touch-sequence.md) | CTA variant: "Tip #2 of 570 at tapthis.co" |
| May 02 | Sat | IIR - IA | [IA-002 - NAR Reached Out to Me Directly](../scripts/inside-the-industry/IA-002-nar-reached-out-to-me.md) | |

### Week 11: May 04 – May 09, 2026

| Date | Day | Slot | Script | Notes |
|---|---|---|---|---|
| May 04 | Mon | KIR Promo | TBD | |
| May 05 | Tue | IIR - NF | TBD | |
| May 06 | Wed | The Playbook | [PB-003 - Buyer Asks to Cut Commission](../scripts/the-playbook/PB-003-buyer-asks-to-cut-commission.md) | Playbook pilot bench ends here |
| May 07 | Thu | IIR - NF | TBD | |
| May 08 | Fri | AI Tip | [AIT-003 - Train Claude to Write in Your Voice](../scripts/ai-tip-of-the-week/003-train-claude-to-write-in-your-voice.md) | CTA variant: "Grab this prompt and my whole library at tapthis.co" |
| May 09 | Sat | IIR - IA | [IA-003 - Chicago Agents NAR Doesn't Know About](../scripts/inside-the-industry/IA-003-chicago-agents-nar-doesnt-know-about.md) | |

### Week 12: May 11 – May 16, 2026

| Date | Day | Slot | Script | Notes |
|---|---|---|---|---|
| May 11 | Mon | KIR Promo | TBD | |
| May 12 | Tue | IIR - IS | [IS-001 - What AI Still Can't Fix](../scripts/inside-the-industry/IS-001-what-ai-still-cant-fix.md) | Tue IS backfill |
| May 13 | Wed | IIR - NF | TBD | Playbook bench exhausted; NF primary |
| May 14 | Thu | IIR - NF | TBD | |
| May 15 | Fri | AI Tip | [AIT-004 - 10-Minute AI Shutdown Ritual](../scripts/ai-tip-of-the-week/004-ai-shutdown-ritual-close-the-loops.md) | CTA variant: baseline "Full prompt plus 569 more at tapthis.co" |
| May 16 | Sat | IIR - IA | [IA-004 - Kale Mentorship Program](../scripts/inside-the-industry/IA-004-kale-mentorship-program.md) | Last IA script in inventory |

### Week 13: May 18 – May 23, 2026

| Date | Day | Slot | Script | Notes |
|---|---|---|---|---|
| May 18 | Mon | KIR Promo | TBD | |
| May 19 | Tue | IIR - NF | TBD | |
| May 20 | Wed | IIR - NF or PB | TBD | New Playbook scripts needed if PB slot resumes |
| May 21 | Thu | IIR - IS | [IS-002 - The 6% Club](../scripts/inside-the-industry/IS-002-the-6-percent-club.md) | Thu IS backfill |
| May 22 | Fri | AI Tip | TBD - select from AIAM | |
| May 23 | Sat | IIR - NF | TBD | IA inventory exhausted; need fresh IA moments |

### Week 14: May 25 – May 30, 2026

| Date | Day | Slot | Script | Notes |
|---|---|---|---|---|
| May 25 | Mon | KIR Promo | TBD | |
| May 26 | Tue | IIR - NF | TBD | |
| May 27 | Wed | IIR - NF | TBD | |
| May 28 | Thu | IIR - NF | TBD | |
| May 29 | Fri | AI Tip | TBD - select from AIAM | |
| May 30 | Sat | IIR - NF | TBD | |

### Week 15: Jun 01 – Jun 06, 2026 *(mid-test check-in)*

| Date | Day | Slot | Script | Notes |
|---|---|---|---|---|
| Jun 01 | Mon | KIR Promo | TBD | |
| Jun 02 | Tue | IIR - IS | [IS-003 - Top Producers Never Say This Word](../scripts/inside-the-industry/IS-003-top-producers-never-say-this-word.md) | **Review 4 weeks of analytics; adjust sub-type mix** |
| Jun 03 | Wed | IIR - NF | TBD | |
| Jun 04 | Thu | IIR - NF | TBD | |
| Jun 05 | Fri | AI Tip | TBD - select from AIAM | |
| Jun 06 | Sat | IIR - NF | TBD | |

### Week 16: Jun 08 – Jun 13, 2026

| Date | Day | Slot | Script | Notes |
|---|---|---|---|---|
| Jun 08 | Mon | KIR Promo | TBD | |
| Jun 09 | Tue | IIR - NF | TBD | |
| Jun 10 | Wed | IIR - NF | TBD | |
| Jun 11 | Thu | IIR - IS | [IS-004 - Brokerages That Keep Top Producers](../scripts/inside-the-industry/IS-004-brokerages-that-keep-top-producers.md) | Last IS script in inventory |
| Jun 12 | Fri | AI Tip | TBD - select from AIAM | |
| Jun 13 | Sat | IIR - NF | TBD | |

### Week 17–21: Jun 15 – Jul 18, 2026

All 14 pre-written IIR scripts are consumed by Week 16. From **Week 17 (Jun 15) through Week 21 (Jul 18)** the cadence below repeats, with every IIR slot filled from that week's `news_brief.py` output, fresh IA moments, new IS drafts from the podcast archive, and new PB scripts. Every Fri AI Tip is selected from the 100 AIAM bank.

| Day | Slot |
|---|---|
| Mon | KIR Promo (this week's episode) |
| Tue | IIR - NF |
| Wed | IIR - NF or PB |
| Thu | IIR - NF |
| Fri | AI Tip - tapthis.co |
| Sat | IIR - NF (IA substitute if D.J. attended something notable) |

**Weekly inventory targets to sustain Weeks 17–21:**
- 4 new NF drafts per week (from news brief)
- 1 new IA draft / month (when D.J. attends something)
- 1 new IS draft every 2 weeks (from podcast archive)
- 1 new PB draft every 2 weeks (to keep Wed PB substitute alive at ~2x/month)

Each Sunday, pre-plan the following week by logging ready scripts into this calendar (replacing TBDs).

---

## 2026-07-19 End-of-Test Review

Sun Jul 19 is the 90-day review. Deliverable: [`../docs/analytics/2026-07-19-pivot-results.md`](../docs/analytics/) (create on Jul 19). Compare 90 days of metrics against the success / reversal criteria in [`../docs/strategy/2026-04-18-pillar-pivot-decision.md`](../docs/strategy/2026-04-18-pillar-pivot-decision.md#success-metrics-review-july-19). Decide: permanent pivot, further adjustment, or reversal.

The post-review schedule (Week 22 onwards) will be written after the review decision.

---

## Historical (Pre-Pivot) Cadence: Feb 23 – Apr 18, 2026

Pre-pivot schedule ran **AI Agent Minute (M/W/F) + Agent Tip of the Day (T/Th/Sa)**, 6 days/week, Sunday off. That cadence produced Weeks 1–8 of posts, all filmed as reels. Source scripts live in [`../scripts/reels/ai-agent-minute/`](../scripts/reels/ai-agent-minute/) and [`../scripts/reels/agent-tip-of-the-day/`](../scripts/reels/agent-tip-of-the-day/). Rank-ordered master scripts live in [`../scripts/ai-agent-minute/`](../scripts/ai-agent-minute/) and [`../scripts/agent-tip-of-the-day/`](../scripts/agent-tip-of-the-day/).

For the Feb 23 – Apr 18 week-by-week posting schedule, see the version of this file prior to commit `c5b7b12` (README rewrite) or any earlier `build.py` output.

The original pre-pivot schedule extended through Dec 31, 2026 and Week 45, but that extended schedule assumed a cadence that no longer applies. It is superseded by this file.

---

## Bonus Reels (Unscheduled)

Reel versions of the rates-below-6% bonus script. Schedule as timely market updates whenever rates approach that level.

| # | Title | Script |
|---|-------|--------|
| B | [Rates Below 6% - Call Your Past Buyers](../scripts/reels/bonus/bonus-001a-call-past-buyers-refi.md) | Reel |
| B | [Rates Below 6% - Call Your Fence-Sitters](../scripts/reels/bonus/bonus-001b-call-fence-sitters.md) | Reel |
| B | [Rates Below 6% - Talk to Renters](../scripts/reels/bonus/bonus-001c-talk-to-renters.md) | Reel |

---

*Pivot applied: 2026-04-18 | Post-pivot schedule from: 2026-04-20 | Next review: 2026-07-19*
