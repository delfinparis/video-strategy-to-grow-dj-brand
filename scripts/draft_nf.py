#!/usr/bin/env python3
"""
NF script-drafting agent for Inside the Industry.

Takes the top take(s) from a morning news brief and drafts a full, film-ready
Inside the Industry (NF) script package: the spoken script with timed beats, all
six social captions, the AI Music Prompt, and a Data Source scaffold. It reads
the repo's own standards at runtime (editorial standards, the Inside the Industry
series standard, the AI-tells field guide, the voice instructions, the music
presets, and one gold-standard example script) so the draft follows the same
rules a human would, and stays in sync with the repo instead of duplicating them.

THE HARD LINE THIS AGENT WILL NOT CROSS: it never invents a source, a stat, a
quote, or a named economist. The Data Source section is built ONLY from the
article the brief actually fetched, and every claim is flagged VERIFY before
filming. The output is therefore a DRAFT (status: needs-verification), not a
ready script. It does ~80% of the mechanical work (structure, six captions,
music prompt, scaffolding); D.J. verifies the sources and tightens the voice
before filming. This is deliberate: the #1 editorial rule is no fabricated
stats, and an automated drafter that wrote a confident Data Source section would
break it.

Input: the structured sidecar a brief run writes alongside the markdown,
  data/news-briefs/YYYY-MM-DD.takes.json
which carries each take plus its source story and fetched article body.

Usage:
  python3 scripts/draft_nf.py
  # draft the top take from today's brief sidecar

  python3 scripts/draft_nf.py --date 2026-06-14 --top 2
  # draft the top 2 takes from a specific day's sidecar

  python3 scripts/draft_nf.py --model claude-opus-4-8
  # use Opus for the drafting (higher voice fidelity if the account is entitled;
  # default is claude-sonnet-4-6, which is proven on this engine)

  python3 scripts/draft_nf.py --no-email
  # write the draft file(s) but don't email

It is also called directly by news_brief.py --draft N right after the brief is
generated, so the morning run produces both the brief and the draft.

Environment: ANTHROPIC_API_KEY required. Email reuses news_brief's delivery
(BRIEF_* or DIGEST_* env). Cost ~$0.05-0.20 per draft depending on model.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Reuse the brief engine's delivery + scrub so there is one implementation.
sys.path.insert(0, str(Path(__file__).parent))
import news_brief as nb  # noqa: E402

REPO_ROOT = Path(__file__).parent.parent
BRIEFS_DIR = REPO_ROOT / "data" / "news-briefs"
DRAFTS_DIR = REPO_ROOT / "scripts" / "inside-the-industry" / "_drafts"
DOCS = REPO_ROOT / "docs"

DEFAULT_MODEL = "claude-sonnet-4-6"

# Standards the agent reads at runtime. Caps keep the prompt bounded; the source
# of truth stays the repo file, never a copy pasted into this script.
STANDARDS_FILES = [
    ("EDITORIAL STANDARDS (universal, wins all conflicts)", DOCS / "editorial-standards.md", 22000),
    ("INSIDE THE INDUSTRY SERIES STANDARD", DOCS / "series" / "inside-the-industry-standard.md", 9000),
    ("AI-TELLS FIELD GUIDE (scrub against this)", DOCS / "ai-tells-field-guide.md", 14000),
    ("VOICE INSTRUCTIONS (write so it reads as D.J.)", DOCS / "ai-voice-custom-instructions.md", 12000),
    ("AI MUSIC PROMPT PRESETS", DOCS / "ai-music-prompts.md", 9000),
]
# One gold-standard NF as a format exemplar.
EXEMPLAR = REPO_ROOT / "scripts" / "inside-the-industry" / "NF-046-thirteen-million-frozen-by-1997-tax-rule.md"

CONFIDENCE_RANK = {"high": 3, "medium": 2, "low": 1, "": 0, None: 0}
# Chicago-local is the brand differentiator, so it wins ties over regulatory.
TIER_WEIGHT = {"chicago": 3, "regulatory": 2, "national": 1}


def now_utc():
    return datetime.now(timezone.utc)


def load_standards():
    """Read the repo's standards docs + one exemplar. Returns one big context
    string. Missing files are skipped with a note, never faked."""
    parts = []
    for label, path, cap in STANDARDS_FILES:
        try:
            text = path.read_text(encoding="utf-8")[:cap]
            parts.append(f"===== {label} =====\n{text}")
        except Exception as e:
            parts.append(f"===== {label} =====\n(could not read {path.name}: {e})")
    try:
        ex = EXEMPLAR.read_text(encoding="utf-8")[:7000]
        parts.append(f"===== GOLD-STANDARD EXAMPLE NF SCRIPT (match this format and depth) =====\n{ex}")
    except Exception:
        pass
    return "\n\n".join(parts)


DRAFT_PROMPT = """You are D.J. Paris's NF script writer for the Inside the Industry series. Draft a full, film-ready Inside the Industry NEWS/REACTIVE (NF) script package from the take and source article below, following the standards verbatim.

Below are D.J.'s actual standards documents and one gold-standard example. Follow them exactly. The universal editorial standard wins any conflict.

{standards}

================ THE STORY TO DRAFT ================
Take (already reviewed and approved as the day's pick):
- Hook idea: {hook}
- The reframe (the insider read): {reframe}
- Close (do this now): {close}
- Confidence: {confidence}

Source the brief actually fetched (this is your ONLY factual ground):
- Headline: {title}
- Outlet(s): {sources}
- URL: {url}
- Article text (verbatim, possibly partial): {body}

================ NON-NEGOTIABLE RULES FOR THIS DRAFT ================
1. SOURCING / NO FABRICATION (the #1 rule). You may ONLY assert facts that appear in the article text above. Do NOT invent statistics, dollar figures, dates, case numbers, quotes, or named economists. If the take implies a fact the article doesn't contain, write the spoken line so it does not depend on an unverified number, and add the missing fact to the Data Source section marked "VERIFY before filming -- not confirmed in fetched source." If the article text is thin, keep the script's factual claims minimal and lean on the reframe, which is opinion D.J. can stand behind.
2. STATUS. Set frontmatter status to "needs-verification". This is a draft. The Data Source section must list each spoken factual claim with the source URL above and an explicit verification note. Never present an unverified claim as confirmed.
3. STRUCTURE. Use the NF four-beat structure with timecodes: HOOK (0:00-0:12), CONTEXT, INSIGHT, CLOSE. NF hook leads with the exact sourced number or fact (no rounding, no "roughly"). The close is a "here's what you do now" action or watchpoint, never an engagement ask.
4. LENGTH. 45-75 seconds, ~100-185 spoken words. Add the Estimated Duration line and a one-paragraph length justification, like the example.
5. VOICE + AI-TELLS. Write so it reads as D.J., not as AI. Obey the field guide: no banned vocabulary, at most one "It's not X, it's Y", at most one Rule-of-Three, no self-answered rhetorical questions, no motivational-poster close.
6. NO EM DASHES anywhere in social captions. Use periods or commas.
7. SOCIAL COPY. Write all six captions (LinkedIn primary, Instagram Reels, TikTok, YouTube Shorts with title+description, Facebook, X), each platform-shaped per the example, hashtags included.
8. AI MUSIC PROMPT. Include the section per the presets: Vibe, Suno/Udio (full), CapCut (<=300 chars, starts with no-vocals constraint, includes BPM). Tune BPM/energy to this story.
9. FRONTMATTER. Fill the required Inside the Industry frontmatter (series, type: reactive, script_number: "NF-DRAFT", title, avatar, content_pillar, primary_platform, post_date: "TBD", status: needs-verification, plus heat, stat_anchored, loop_back, share_trigger). Include the WOW line and Shareable Moment.

Output ONLY the finished markdown script package, starting with the frontmatter block. No preamble, no explanation."""


POLISH_PROMPT = """You are D.J. Paris's script editor doing the MANDATORY second pass. D.J.'s rule: never ship a first draft. Stress-test the draft below against his standards, then apply the fixes and output the polished final.

Use the same standards you were given (they are repeated below). Model the stress test on the repo's audit format (docs/audits): findings graded CRITICAL / HIGH / MEDIUM, a close assessment, a changes-applied list.

{standards}

================ THE FIRST DRAFT TO STRESS-TEST AND POLISH ================
{draft}

================ STRESS TEST CHECKLIST (run every item) ================
- WOW gate (Rule 0): does it clearly clear one criterion, and is the WOW line specific?
- SOURCING (Rule 1, the hard line): is any stat, dollar figure, date, quote, or named person asserted that is NOT in the fetched article? Every such claim must be either softened to opinion or moved to Data Source marked "VERIFY before filming". A confident unsourced number is a CRITICAL finding. Status must stay needs-verification.
- HOOK (Rule 2): does the first sentence stop the scroll? NF hook leads with the exact sourced fact, no rounding.
- CLOSE (Rule 4): "here's what you do now" action or watchpoint, never an engagement ask.
- AI-TELLS (field guide): no banned vocabulary; at most one "It's not X, it's Y"; at most one Rule-of-Three; no self-answered rhetorical questions; no motivational-poster close. Flag and fix any stacking.
- EM DASHES: none in any social caption. Fix to periods/commas.
- LENGTH: 45-75s (~100-185 words). Adjust if over/under.
- VOICE: reads as D.J., not as AI.

================ OUTPUT ================
Output the POLISHED full markdown script package (same structure as the draft, frontmatter first, status still needs-verification), and at the very end append:

## Stress Test (second pass)
- **Verdict:** [POLISHED / MAJOR REWRITE / FLAGGED]
- **CRITICAL:** [findings or "none"]
- **HIGH:** [findings or "none"]
- **MEDIUM:** [findings or "none"]
- **Changes applied:** [bullet list of what you changed from the first draft]

Output ONLY the markdown. No preamble."""


def build_prompt(entry, standards):
    take = entry.get("take", {})
    story = entry.get("story", {})
    body = entry.get("body") or story.get("summary") or "(no article body was fetchable; rely on the headline and keep factual claims minimal)"
    sources = ", ".join(story.get("cross_sources") or [story.get("source", "?")])
    return DRAFT_PROMPT.format(
        standards=standards,
        hook=take.get("hook", ""),
        reframe=take.get("reframe", ""),
        close=take.get("close", ""),
        confidence=take.get("confidence", "?"),
        title=story.get("title", take.get("title", "")),
        sources=sources,
        url=story.get("link", ""),
        body=body[:6000],
    )


def call_model(prompt, model):
    client = nb._client()
    if client is None:
        return None
    try:
        msg = client.messages.create(
            model=model, max_tokens=4000,
            messages=[{"role": "user", "content": prompt}],
        )
        text = msg.content[0].text.strip()
        text = re.sub(r"^```(?:markdown)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
        return text
    except Exception as e:
        print(f"warning: draft generation failed: {e}", file=sys.stderr)
        return None


def slugify(title):
    s = re.sub(r"[^a-z0-9]+", "-", (title or "untitled").lower()).strip("-")
    return s[:60] or "untitled"


def pick_top(entries, n):
    """Highest confidence first, then Chicago/regulatory over national."""
    def key(e):
        t = e.get("take", {})
        s = e.get("story", {})
        return (CONFIDENCE_RANK.get((t.get("confidence") or "").lower(), 0),
                TIER_WEIGHT.get(s.get("tier", "national"), 1))
    return sorted(entries, key=key, reverse=True)[:n]


def run(entries, top=1, model=DEFAULT_MODEL, deliver=True):
    """Draft the top N takes. Returns list of {path, title}. Never raises."""
    if not entries:
        print("draft_nf: no take entries to draft.", file=sys.stderr)
        return []
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    standards = load_standards()
    today = now_utc().strftime("%Y-%m-%d")
    results = []
    for entry in pick_top(entries, top):
        story = entry.get("story", {})
        take = entry.get("take", {})
        title = story.get("title", take.get("title", "untitled"))
        print(f"draft_nf: drafting '{title[:70]}' on {model}...", file=sys.stderr)
        draft = call_model(build_prompt(entry, standards), model)
        if not draft:
            continue
        # Mandatory second pass: stress-test + polish (D.J.'s standing rule --
        # never ship a first draft). Falls back to the first draft if it fails.
        print("draft_nf: second pass (stress-test + polish)...", file=sys.stderr)
        polished = call_model(POLISH_PROMPT.format(standards=standards, draft=draft), model)
        if polished:
            draft = polished
        else:
            print("draft_nf: polish pass failed; keeping first draft.", file=sys.stderr)
        draft = nb._scrub(draft)  # belt-and-suspenders em-dash enforcement
        path = DRAFTS_DIR / f"{today}-{slugify(title)}.md"
        path.write_text(draft, encoding="utf-8")
        print(f"draft_nf: wrote {path}", file=sys.stderr)
        if deliver:
            subj = f"NF DRAFT {now_utc().strftime('%m/%d')}: {title[:65]} (verify before filming)"
            status = nb.send_email(subj, draft)
            print(f"draft_nf: email -> {status}", file=sys.stderr)
        results.append({"path": str(path), "title": title})
    return results


def load_sidecar(date_str):
    path = BRIEFS_DIR / f"{date_str}.takes.json"
    if not path.exists():
        print(f"draft_nf: no sidecar at {path}. Run news_brief.py first.", file=sys.stderr)
        return []
    try:
        return json.loads(path.read_text()).get("entries", [])
    except Exception as e:
        print(f"draft_nf: could not read sidecar: {e}", file=sys.stderr)
        return []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=now_utc().strftime("%Y-%m-%d"), help="Brief date YYYY-MM-DD (default today, UTC)")
    parser.add_argument("--top", type=int, default=1, help="How many takes to draft (default 1)")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Model (default {DEFAULT_MODEL})")
    parser.add_argument("--no-email", action="store_true", help="Write the draft file(s) but don't email")
    args = parser.parse_args()

    entries = load_sidecar(args.date)
    results = run(entries, top=args.top, model=args.model, deliver=not args.no_email)
    if not results:
        print("draft_nf: nothing drafted.", file=sys.stderr)
        sys.exit(1)
    for r in results:
        print(r["path"])


if __name__ == "__main__":
    main()
