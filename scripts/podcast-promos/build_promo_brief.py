#!/usr/bin/env python3
"""
Podcast Promo Hype Machine — brief builder.

Reads one podcast episode and emits a filled "promo brief": the five beats of the
hype-machine arc, pre-populated with the episode's own intelligence, plus the
ready-to-run instruction for writing the full-package promo.

The brief is the deterministic half (data extraction). The voice/writing half is
done by Claude (or D.J.) running the brief through the format spec:
    docs/series/podcast-promo-hype-machine.md

Usage:
    python build_promo_brief.py kir 2026-01-30_item1_Amanda-Pendleton
    python build_promo_brief.py coffeetalk ep01-the-88-percent-lie

Episode id is matched loosely (substring, case-insensitive) so you can pass a
guest name or a slug fragment:
    python build_promo_brief.py kir pendleton
    python build_promo_brief.py coffeetalk 88-percent

Portable: a third show plugs in by adding a loader function + a SHOWS entry.
No third-party dependencies.
"""

import json
import sys
from pathlib import Path

HOME = Path.home()
GH = HOME / "GitHub Projects"

KIR_ANALYSIS_DIR = GH / "keeping-it-real-content-system" / "data" / "analysis"
COFFEETALK_SCRIPT_DIR = GH / "coffeetalk-episode-registry" / "scripts"
COFFEETALK_REGISTRY = GH / "coffeetalk-episode-registry" / "registry.md"

OUT_DIR = Path(__file__).resolve().parent / "_briefs"
SPEC = "docs/series/podcast-promo-hype-machine.md"
REGISTRY = "scripts/podcast-promos/promo-registry.md"


def die(msg):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def find_one(directory, pattern, query, suffix):
    """Find a single file in `directory` matching `query` (substring, ci)."""
    if not directory.exists():
        die(f"source directory not found: {directory}\n"
            f"(is the sibling repo cloned? run `git fetch` if working across devices)")
    q = query.lower()
    hits = sorted(p for p in directory.glob(pattern) if q in p.name.lower())
    if not hits:
        die(f"no episode in {directory} matching '{query}'")
    if len(hits) > 1:
        names = "\n  ".join(h.stem.replace(suffix, "") for h in hits)
        die(f"'{query}' matched {len(hits)} episodes — be more specific:\n  {names}")
    return hits[0]


# ---------------------------------------------------------------------------
# KIR adapter (guest interviews)
# ---------------------------------------------------------------------------
def load_kir(query):
    path = find_one(KIR_ANALYSIS_DIR, "*_analysis.json", query, "_analysis")
    data = json.loads(path.read_text())
    g = data.get("guest_info", {}) or {}

    cred = ", ".join(x for x in (g.get("title"), g.get("company"),
                                 g.get("production_level")) if x)
    guest = g.get("name") or "the guest"

    # Hook candidates, sharpest first: tactical clips, surprising stats, quotables.
    hooks = []
    for c in data.get("clip_worthy_moments", []) or []:
        q = c.get("quote")
        if q:
            hooks.append(f'[{c.get("clip_type","clip")} @ {c.get("timestamp","?")}] "{q}"')
    for q in data.get("quotable_insights", []) or []:
        hooks.append(f'[quotable] "{q}"')
    for t in data.get("key_tactics", []) or []:
        if t.get("tactic"):
            hooks.append(f'[tactic @ {t.get("timestamp","?")}] {t["tactic"]}')

    topics = data.get("main_topics", []) or []

    problems = []
    for p in data.get("problems_addressed", []) or []:
        problems.append(f'{p.get("specific_problem","?")} '
                        f'-> {p.get("solution_summary","?")} (@ {p.get("timestamp","?")})')

    # Tip candidates: concrete tactics win over abstract takeaways.
    tips = []
    for t in data.get("key_tactics", []) or []:
        if t.get("tactic"):
            tips.append(f'{t["tactic"]} ({t.get("context","")} @ {t.get("timestamp","?")})')
    for c in data.get("clip_worthy_moments", []) or []:
        if c.get("clip_type") == "tactical_specificity" and c.get("quote"):
            tips.append(f'(from clip) {c["quote"]}')
    for a in data.get("target_avatars", []) or []:
        if a.get("key_takeaway"):
            tips.append(f'(takeaway) {a["key_takeaway"]}')

    return {
        "show": "Keeping It Real",
        "frame": f"{guest}, {cred}, came on the show.",
        "guest": guest,
        "credential": cred,
        "hook_candidates": hooks,
        "topics": topics,
        "problems": problems,
        "tip_candidates": tips,
        "summary": data.get("episode_summary", ""),
        "resources": [f'{r.get("name")} — {r.get("context","")}'
                      for r in data.get("resources_mentioned", []) or []],
        "source_path": str(path),
        "slug": "kir-" + path.stem.replace("_analysis", "").split("_item")[0]
                + "-" + (guest.lower().replace(" ", "-")),
        "listen": "this week's Keeping It Real episode",
    }


# ---------------------------------------------------------------------------
# Coffee Talk adapter (Tim & D.J., stat-driven, no guest)
# ---------------------------------------------------------------------------
def load_coffeetalk(query):
    path = find_one(COFFEETALK_SCRIPT_DIR, "*.md", query, "")
    script = path.read_text()

    registry_row = ""
    if COFFEETALK_REGISTRY.exists():
        for line in COFFEETALK_REGISTRY.read_text().splitlines():
            cells = [c.strip() for c in line.split("|")]
            # registry table: # | Air Date | Title | Central Hook Stat | Topic | Supporting
            if len(cells) >= 7 and path.stem.split("-", 1)[-1][:6].lower() in line.lower():
                registry_row = line
                break

    return {
        "show": "Coffee Talk with Tim & D.J.",
        "frame": "Tim and I opened this week's Coffee Talk with the hook stat below.",
        "guest": None,
        "credential": None,
        "hook_candidates": ["(use the Central Hook Stat from the registry row / aired script — "
                            "do NOT introduce a stat the episode didn't air)"],
        "topics": ["(pull the topic category + 2 supporting angles from the aired script)"],
        "problems": ["(name the agent problem the hook stat exposes)"],
        "tip_candidates": ["(pick the single most portable of the episode's 3 required action steps)"],
        "summary": "Full aired script below — extract beats from it. Stat discipline: every "
                   "stat in the promo must already exist in this script.",
        "resources": [],
        "source_path": str(path),
        "registry_row": registry_row,
        "aired_script": script,
        "slug": "coffeetalk-" + path.stem,
        "listen": "this week's Coffee Talk with Tim & D.J.",
    }


SHOWS = {"kir": load_kir, "coffeetalk": load_coffeetalk}


def bullets(items, empty="(none in source — derive from summary / aired script)"):
    if not items:
        return f"  - {empty}"
    return "\n".join(f"  - {x}" for x in items)


def render(b):
    lines = []
    A = lines.append
    A(f"# Promo Brief — {b['show']}")
    A("")
    A(f"**Source:** `{b['source_path']}`  ")
    A(f"**Suggested filename:** `scripts/podcast-promos/{b['slug']}.md`")
    A("")
    A("> Fill the five beats below into the full-package promo. The data here is")
    A(f"> lifted from the episode — do not invent. Frame: {b['frame']}")
    A("")
    A("---")
    A("")
    A("## Beat 1 — The Hook (first SPOKEN line; steal the single most surprising thing)")
    A(bullets(b["hook_candidates"]))
    A("")
    A("## Beat 2 — The X-Y-Z (\"On this episode we got into...\" — 3 topics, agent language)")
    A(bullets(b["topics"]))
    if b.get("credential"):
        A(f"  - credibility token (compress to one line): {b['credential']}")
    A("")
    A("## Beat 3 — What We Solved (name 1-2 REAL agent problems the episode answers)")
    A(bullets(b["problems"]))
    A("")
    A("## Beat 4 — The Tip (the payload: one physical, do-it-tomorrow tactic)")
    A(bullets(b["tip_candidates"]))
    A("")
    A("## Beat 5 — The Close (\"here's what you do now\": listen + apply the tip)")
    A(f"  - listen to {b['listen']}")
    A("")
    if b.get("resources"):
        A("## Resources mentioned (optional — name-drop only if it sharpens the tip)")
        A(bullets(b["resources"]))
        A("")
    A("## Episode summary (context only)")
    A(f"{b['summary']}")
    A("")
    if b.get("registry_row"):
        A("## Coffee Talk registry row (stat dedup — must hold)")
        A(f"`{b['registry_row']}`")
        A("")
    if b.get("aired_script"):
        A("## Aired script (extract beats from here)")
        A("```")
        A(b["aired_script"].strip())
        A("```")
        A("")
    A("---")
    A("")
    A("## How to finish this promo")
    A(f"1. Read the format spec: `{SPEC}`")
    A(f"2. Read `{REGISTRY}` and check your planned HOOK and TIP for repeats.")
    A("3. Write the full package (spoken script + B-roll + music prompt + 5 social")
    A(f"   descriptions) to `scripts/podcast-promos/{b['slug']}.md`.")
    A(f"4. Add a row to `{REGISTRY}` with the hook + tip you used.")
    return "\n".join(lines)


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in SHOWS:
        die(f"usage: python build_promo_brief.py <{'|'.join(SHOWS)}> <episode-query>")
    show, query = sys.argv[1], " ".join(sys.argv[2:])
    b = SHOWS[show](query)
    text = render(b)
    OUT_DIR.mkdir(exist_ok=True)
    out = OUT_DIR / f"{b['slug']}-brief.md"
    out.write_text(text)
    print(text)
    print(f"\n[brief written to {out}]", file=sys.stderr)


if __name__ == "__main__":
    main()
