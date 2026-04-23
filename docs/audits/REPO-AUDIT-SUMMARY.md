# Repo-Wide Editorial Audit Summary

**Audit date:** 2026-04-18
**Standard applied:** [`docs/editorial-standards.md`](../editorial-standards.md) (universal) + per-series standards in [`docs/series/`](../series/)
**Scope:** 465 script files across all series

---

## What was audited

All script files under `scripts/`:

| Location | Files |
| --- | ---: |
| `scripts/ai-agent-minute/` | 100 |
| `scripts/agent-tip-of-the-day/` | 62 |
| `scripts/inside-the-industry/` | 14 |
| `scripts/the-playbook/` | 3 |
| `scripts/bonus/` | 1 |
| `scripts/podcast-promos/` | 1 |
| `scripts/reels/ai-agent-minute/` | 171 |
| `scripts/reels/agent-tip-of-the-day/` | 103 |
| `scripts/reels/bonus/` | 10 |
| **Total** | **465** |

---

## What was fixed automatically

### Mechanical compliance (all 465 files)

| Fix | Count | Rule |
| --- | ---: | --- |
| Brand intros stripped | 100 | Editorial brief: brand intros deprecated |
| `[ON-SCREEN: ...]` bracketed cues stripped | 352 | Rule 2: captions.ai renders audio only |
| `> **On-Screen Text:**` blockquote cues stripped | 276 | Rule 2: same captions.ai rule |
| "See you next time." close lines stripped | 373 | Editorial brief: sign-off deprecated |
| Em/en dashes replaced with `--` | 7 | Rule 5: em dashes banned |
| Banned AI-speak words replaced | 19 files | Rule 5: merged banned word list |
| Direct engagement asks reworded | 2 files | Rule 4: no engagement asks |

### WOW gate metadata (Rule 0)

All 465 scripts now carry a `> **WOW: ...**` line right after the H1 title. The WOW line names which of the 8 clip-worthy criteria the script hits and gives a one-sentence specificity rationale.

Lines are auto-generated from frontmatter (series, ai_tool, guest, scenario_category, sub-type) and the script title. They are v1 placeholders. D.J. can refine individual lines for punch, but every script now has the gate in place.

### Engagement-ask close audit (Rule 4)

A smart close-stripper ran across all 465 scripts and:
- Stripped trailing engagement-ask tails from 26+ files (kept the tip/action content, removed only the "Then tell me if...", "Drop X below", "-- be honest", "Yes or no", etc. portions)
- Removed 38+ pure rhetorical-question close lines that served no editorial purpose ("Have you X?", "Do you Y?", "When's the last time Z?")

Lines containing tip/action verbs (open, paste, send, pull, run, buy, use, block, pick, call) were preserved even if they ended with a soft question, because those sentences still deliver the actual tip.

---

## What was NOT fixed (requires human judgment)

These are editorial decisions that cannot be automated. They're flagged here so the next pass knows what to tackle.

### 1. Data Source section format

Most scripts have a `## Data Source` section, but the format is inconsistent. The universal standard (Rule 1) requires:

```markdown
- [Claim as written in script]
 - Source: [exact publication name, year]
 - Who was measured: [agents / consumers / listings / etc.]
 - Status: [confirmed / unverified / placeholder]
```

**Only IS-002 has been reformatted to this standard.** The other ~180 main-series scripts still have prose-style Data Source sections. This needs a per-script manual pass.

### 2. Stat integrity verification

Any script with a specific number, percentage, or named guest needs its claims cross-referenced against the KIR podcast archive or external sources. The IS-002 audit is the pattern: search for the exact quote, verify the guest name and episode, then update citations.

**Known stat-integrity risk areas (priority for manual review):**

- Any script with a percentage in the spoken line (search `%` or `percent` across scripts)
- Any script that names a guest by name (verify the claim attributed to them)
- Any script referencing "$X million" production (verify the named producer exists at that volume)

### 3. WOW line polish

The auto-generated WOW lines satisfy the structural requirement (each names a criterion + specificity). A few read awkwardly because the title had unusual punctuation. D.J. can refine individual ones for sharpness.

**Suggested polish targets:** scripts where the title is a sentence fragment or ends with ellipsis - the WOW line may read clunky.

### 4. "Here's what you do now" close construction

After stripping engagement asks, some scripts have a weakened close. In most cases, the final surviving sentence is still a reasonable at-the-viewer's-life observation. But some scripts would be stronger with an explicit `Here's what you do now. [concrete action].` rewrite of the close.

**Priority for close rewrites:** scripts where the close was entirely an engagement ask, and the only remaining close is the reframe from the preceding beat. Those scripts now end on a reframe with no action - they're still compliant (the reframe counts as an acceptable close per Rule 4 pattern 1) but would be stronger with an explicit action close.

---

## Per-series notes

### AI Agent Minute (100 + 171 reels)

- Brand intros fully stripped from all 100 main scripts and 171 reels.
- "See you next time" closes stripped across the board.
- `[ON-SCREEN: ...]` cues stripped from 352 instances across the series.
- WOW gates added to all.
- **Remaining work:** Data Source reformatting, stat integrity verification, per-script close polish.

### Agent Tip of the Day (62 + 103 reels)

- Engagement-ask closes aggressively stripped (many scripts had "Then tell me if your engagement numbers don't change" style CTAs that were removed while preserving the preceding action).
- WOW gates added naming the guest and the tactic.
- **Remaining work:** Guest attribution verification against KIR transcripts (similar to how Karina Chavez was verified for IS-002), Data Source reformatting.

### Inside the Industry (14)

- IS-002 fully audited and rewritten with verified citations (the "6% Club" fabrication was fixed).
- WOW gates added to all sub-types (IA = earned observation, IS = pattern reveal, NF = surprising statistic).
- Closes reviewed and confirmed compliant for IA, IS, and NF sub-types (observation closes, news watchpoint closes, and memorable-line closes are all allowed per Rule 4).
- **Remaining work:** Stat integrity verification across NF scripts (settlement amounts, case numbers), guest attribution across IS scripts.

### The Playbook (3)

- WOW gates added.
- Closes already compliant ("Try it on your next lowball", "Send this exact text", "Try this exact question").
- **Remaining work:** Content is on-standard. Could use more scripts to fill out the series per the scenario categories in [`docs/series/the-playbook-standard.md`](../series/the-playbook-standard.md).

### Reels (284)

- Full mechanical fixer pass applied (brand intros, `[ON-SCREEN]`, On-Screen Text blockquotes, "See you next time", em dashes).
- WOW gates added.
- Engagement-ask closes stripped.
- **Remaining work:** Reels are derived from main scripts, so any content fixes to a main script should propagate to its reels.

---

## Commits (chronological)

1. `32bca3b` - Initial editorial standard rewrite + AIAM per-series + IS-002 pilot audit
2. `4299937` - IS-002 fully rewritten with verified Karina Chavez quote attribution
3. `2a66f2f` - Per-series standards for Agent Tip, The Playbook, Inside the Industry
4. `ece7ff0` - Mechanical audit across all 465 scripts (brand intros, `[ON-SCREEN]`, etc.)
5. `8b30d23` - WOW gates on 181 main-series scripts + engagement-ask close strip
6. _(this commit)_ - WOW gates on 284 reels + On-Screen Text blockquote strip + close audit

---

## How to continue the audit

When ready to do the remaining editorial work:

**For Data Source reformatting** (most mechanical of the remaining work):
- Iterate through `scripts/` by series
- Convert each `## Data Source` section to the required bullet format
- Flag any claim lacking source + year + who-was-measured as `status: unverified` and write an audit doc under `docs/audits/` listing what needs verification

**For stat integrity verification** (highest editorial risk):
- Start with any script that contains a percentage, "$X million" claim, or named guest quote
- Use the same pattern as the IS-002 audit: search the KIR transcript archive for the quote or the claim, verify the guest name and episode, then update citations
- Scripts that can't be verified move to `status: needs-verification` until D.J. confirms

**For close polish** (lowest priority, highest-judgment):
- Scripts where only the reframe remains after engagement-ask stripping
- Candidate scripts: any script where the final surviving line is an observation rather than an action
- Add a `Here's what you do now. [concrete action]` line where the concrete action is obvious from the tip content

---

## Helper scripts added to the repo

| File | Purpose |
| --- | --- |
| [`scripts/audit_fix.py`](../../scripts/audit_fix.py) | Mechanical fixer: brand intros, `[ON-SCREEN]`, "See you next time", em dashes |
| [`scripts/add_wow_gates.py`](../../scripts/add_wow_gates.py) | Generates per-script WOW lines from frontmatter |
| [`scripts/cleanup_wow_gates.py`](../../scripts/cleanup_wow_gates.py) | Cleans up WOW line formatting (acronyms, punctuation) |
| [`scripts/fix_closes.py`](../../scripts/fix_closes.py) | Smart engagement-ask stripper |
| [`scripts/strip_onscreen_text_v2.py`](../../scripts/strip_onscreen_text_v2.py) | Strips `> **On-Screen Text:**` blockquotes (reels variant) |

All are idempotent - safe to re-run after new scripts are added to the repo.
