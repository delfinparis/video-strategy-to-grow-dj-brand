#!/usr/bin/env python3
"""
Evergreen stat-tip bank for Inside the Industry.

News expires; a good stat doesn't. This module maintains a persistent bank of
"did you know X, and here's how to use it in your business" stat tips so the
morning brief always has at least one stat-anchored option, and that option
PERSISTS day to day until D.J. actually films it.

Three jobs, called by news_brief.py each morning:

1. mark_used_from_repo() -- fetch the cloud repo and scan committed (i.e. filmed)
   scripts. If a banked stat's distinctive number already appears in a script,
   mark it used so it drops off the brief. Deterministic number match, no LLM.

2. extract_stats(stories) -- pull NEW evergreen, sourced stat tips out of today's
   stat-rich items (NAR / Zillow / Redfin / HousingWire research) and add the
   unique ones to the bank. Haiku.

3. pick_best_fit(stories) -- rank the UNUSED bank against today's headlines and
   surface the one most relevant to film right now (best-fit-for-today). Haiku.

The bank lives at data/news-briefs/stat-bank.json. Nothing here is fabricated:
extraction only keeps stats with a named source, and a stat with no usable
source is dropped, not invented.
"""

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import news_brief as nb  # noqa: E402  (reuse _client / _parse_json / now)

REPO_ROOT = Path(__file__).parent.parent
BANK_PATH = REPO_ROOT / "data" / "news-briefs" / "stat-bank.json"
# Committed-script locations that count as "filmed / used".
SCRIPT_DIRS = ["scripts/inside-the-industry", "scripts/reels",
               "scripts/ai-tip-of-the-week", "scripts/the-playbook"]

STAT_MODEL = "claude-haiku-4-5-20251001"


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _loads_array(raw):
    """Robustly pull a JSON array out of a model reply, tolerating code fences
    and trailing prose (Haiku sometimes appends a note after the array)."""
    if not raw:
        return []
    raw = raw.strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    try:
        return json.loads(raw)
    except Exception:
        pass
    start = raw.find("[")
    end = raw.rfind("]")
    if start != -1 and end != -1 and end > start:
        try:
            return json.loads(raw[start:end + 1])
        except Exception:
            return []
    return []


# ---------------------------------------------------------------------------
# Bank IO
# ---------------------------------------------------------------------------
def load_bank():
    if not BANK_PATH.exists():
        return {"stats": []}
    try:
        data = json.loads(BANK_PATH.read_text())
        data.setdefault("stats", [])
        return data
    except Exception:
        return {"stats": []}


def save_bank(bank):
    BANK_PATH.parent.mkdir(parents=True, exist_ok=True)
    BANK_PATH.write_text(json.dumps(bank, indent=2), encoding="utf-8")


def _norm_number(num):
    """Normalize a number string for matching: keep digits + the unit word."""
    if not num:
        return ""
    return re.sub(r"\s+", " ", num.strip().lower())


def _stat_signature(stat):
    """Distinctive number used for dedup and used-detection."""
    return _norm_number(stat.get("number", "")) or _norm_number(stat.get("stat", ""))[:40]


# ---------------------------------------------------------------------------
# 1. Used-detection against the cloud repo (number match, no LLM)
# ---------------------------------------------------------------------------
def _git(args, timeout=40):
    try:
        return subprocess.run(["git", "-C", str(REPO_ROOT)] + args,
                              capture_output=True, text=True, timeout=timeout)
    except Exception:
        return None


def _default_branch():
    r = _git(["rev-parse", "--abbrev-ref", "origin/HEAD"])
    if r and r.returncode == 0 and "/" in r.stdout:
        return r.stdout.strip().split("/")[-1]
    return "main"


def _number_variants(num):
    """A few literal search forms for one number, e.g. '13.1 million' -> also
    '13.1M', '13.1m'. Keeps git grep matching robust across how a script writes it."""
    num = (num or "").strip()
    if not num:
        return []
    variants = {num, num.lower()}
    m = re.match(r"([\d.,]+)\s*(million|billion|thousand)", num, re.I)
    if m:
        unit = {"million": "M", "billion": "B", "thousand": "K"}[m.group(2).lower()]
        variants.add(f"{m.group(1)}{unit}")
        variants.add(f"{m.group(1)}{unit.lower()}")
    return [v for v in variants if len(v) >= 2]


def mark_used_from_repo(bank):
    """Fetch the repo, scan committed scripts, mark a stat used if its distinctive
    number appears in any filmed script. Returns count newly marked used."""
    _git(["fetch", "-q", "origin"])  # CLAUDE.md: always fetch first
    branch = _default_branch()
    tree = f"origin/{branch}"
    # Confirm the tree object is reachable; otherwise fall back to local files.
    have_tree = bool(_git(["rev-parse", "--verify", "-q", tree]) and
                     _git(["rev-parse", "--verify", "-q", tree]).returncode == 0)
    newly = 0
    for stat in bank["stats"]:
        if stat.get("status") == "used":
            continue
        sig = stat.get("number") or ""
        variants = _number_variants(sig)
        if not variants:
            continue
        found = False
        for v in variants:
            if have_tree:
                r = _git(["grep", "-F", "-i", "-q", "-e", v, tree, "--"] + SCRIPT_DIRS)
                if r and r.returncode == 0:
                    found = True
                    break
            else:
                # Local fallback: scan working-tree script files.
                for d in SCRIPT_DIRS:
                    dd = REPO_ROOT / d
                    if not dd.exists():
                        continue
                    for p in dd.rglob("*.md"):
                        try:
                            if v.lower() in p.read_text(errors="ignore").lower():
                                found = True
                                break
                        except Exception:
                            continue
                    if found:
                        break
            if found:
                break
        if found:
            stat["status"] = "used"
            stat["used_detected"] = now_iso()
            newly += 1
    return newly


# ---------------------------------------------------------------------------
# 2. Extraction: add new evergreen stat tips from today's items
# ---------------------------------------------------------------------------
EXTRACT_PROMPT = """You are building D.J. Paris's bank of EVERGREEN real estate stat tips for Chicago agents. From the items below, extract only genuinely useful, SOURCED, durable statistics that an agent could turn into a "did you know X, here's how to use it in your business" video any week (not tied to a breaking-news moment).

Rules:
- Only a stat with a NAMED source (NAR, Zillow, Redfin, HousingWire, Realtor.com, a named report) and ideally a year. No source -> drop it. Never invent a number or a source.
- Must be evergreen: a behavioral or structural stat (e.g. "X% of buyers found their agent through a referral"), NOT a this-week market reading (rates, this month's inventory).
- "number" must be the single most distinctive figure exactly as it should be searched (e.g. "13.1 million", "78%", "$384,606").
- "tip" = one concrete sentence on how a Chicago agent uses this stat in their business.

Items:
{items}

Output JSON array ONLY (may be empty):
[
  {{"stat": "the stat in one sentence", "number": "78%", "source": "NAR Profile of Home Buyers and Sellers 2025", "url": "...", "tip": "how the agent uses it"}}
]
Aim for 0-4 high-quality entries. Quality over quantity; an empty array is fine."""


def extract_stats(stories, bank, model=STAT_MODEL):
    """Extract new evergreen stat tips from today's stories; add unique ones to
    the bank. Returns count added."""
    client = nb._client()
    if client is None or not stories:
        return 0
    blocks = []
    for i, s in enumerate(stories[:25]):
        blocks.append(f"[{i+1}] ({s.get('source','?')}) {s.get('title','')}\n  {s.get('summary','')[:220]}\n  Link: {s.get('link','')}")
    try:
        msg = client.messages.create(
            model=model, max_tokens=1500,
            messages=[{"role": "user", "content": EXTRACT_PROMPT.format(items="\n\n".join(blocks))}],
        )
        found = _loads_array(msg.content[0].text)
    except Exception as e:
        print(f"stat_bank: extraction failed: {e}", file=sys.stderr)
        return 0
    existing = {_stat_signature(s) for s in bank["stats"]}
    added = 0
    for f in found:
        if not isinstance(f, dict) or not f.get("number") or not f.get("source"):
            continue
        sig = _norm_number(f.get("number"))
        if sig in existing:
            continue
        existing.add(sig)
        bank["stats"].append({
            "stat": f.get("stat", ""),
            "number": f.get("number", ""),
            "source": f.get("source", ""),
            "url": f.get("url", ""),
            "tip": f.get("tip", ""),
            "added": now_iso(),
            "status": "unused",
            "used_detected": None,
        })
        added += 1
    return added


# ---------------------------------------------------------------------------
# 3. Best-fit-for-today selection
# ---------------------------------------------------------------------------
RANK_PROMPT = """D.J. Paris films one short video a day for Chicago real estate agents. Below is his bank of UNUSED evergreen stat tips and today's news headlines. Pick the stat tips most worth filming TODAY, judged by relevance to what's in the news right now and seasonal timing.

Today's headlines:
{headlines}

Unused stat bank:
{bank}

Output JSON array ONLY, best first, top {n}:
[
  {{"idx": 2, "why_today": "one phrase on why this stat fits right now"}}
]
"idx" is the [n] number of the stat."""


def pick_best_fit(stories, bank, n=1, model=STAT_MODEL):
    """Rank unused stats by fit to today. Returns list of stat dicts (with an
    added 'why_today'). Falls back to oldest-unused if the LLM is unavailable."""
    unused = [s for s in bank["stats"] if s.get("status") != "used"]
    if not unused:
        return []
    client = nb._client()
    if client is None:
        return sorted(unused, key=lambda s: s.get("added", ""))[:n]
    headlines = "\n".join(f"- {s.get('title','')}" for s in stories[:15]) or "(no headlines today)"
    bank_text = "\n".join(
        f"[{i+1}] {s.get('stat','')} (source: {s.get('source','')}; added {s.get('added','')})"
        for i, s in enumerate(unused)
    )
    try:
        msg = client.messages.create(
            model=model, max_tokens=800,
            messages=[{"role": "user", "content": RANK_PROMPT.format(
                headlines=headlines, bank=bank_text, n=n)}],
        )
        ranked = _loads_array(msg.content[0].text)
    except Exception as e:
        print(f"stat_bank: ranking failed: {e}", file=sys.stderr)
        return sorted(unused, key=lambda s: s.get("added", ""))[:n]
    out = []
    for r in ranked[:n]:
        idx = r.get("idx")
        if isinstance(idx, int) and 1 <= idx <= len(unused):
            stat = dict(unused[idx - 1])
            stat["why_today"] = r.get("why_today", "")
            out.append(stat)
    return out or sorted(unused, key=lambda s: s.get("added", ""))[:n]


# ---------------------------------------------------------------------------
# Orchestration helper for news_brief.py
# ---------------------------------------------------------------------------
def run_daily(stories, top=1):
    """Full daily stat-bank cycle: prune used, extract new, pick best-fit.
    Returns (stat_tips, summary_note). Never raises."""
    bank = load_bank()
    try:
        used = mark_used_from_repo(bank)
    except Exception as e:
        used = 0
        print(f"stat_bank: used-detection skipped: {e}", file=sys.stderr)
    added = extract_stats(stories, bank)
    tips = pick_best_fit(stories, bank, n=top)
    save_bank(bank)
    total_unused = sum(1 for s in bank["stats"] if s.get("status") != "used")
    note = f"{added} added, {used} marked used, {total_unused} unused in bank"
    return tips, note
