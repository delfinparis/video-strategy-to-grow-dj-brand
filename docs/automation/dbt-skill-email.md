# DBT skill of the day (8am email)

Personal, not content work. Every morning at about 8am Central, one DBT skill
and one exercise you can finish in 5 minutes anywhere lands in
delfinparis@gmail.com.

## How it works

| Piece | What it does |
|---|---|
| `data/dbt-skills.json` | The library: 36 skills across the four DBT modules (Mindfulness, Distress Tolerance, Emotion Regulation, Interpersonal Effectiveness), interleaved so no two days in a row share a module. |
| `scripts/dbt_skill.py` | Picks today's skill, `(date - 2026-10-01) % 36`, and renders the subject, plain-text and HTML body as JSON. No state, no network, no API key. |
| Routine **DBT skill of the day** | Claude Code routine, 7:58am `America/Chicago` daily. It runs `python3 scripts/dbt_skill.py today` and sends the result through the Gmail connector. Change nothing else. |

Because the pick is computed from the date, a missed day just skips that
skill. The rotation never drifts, and re-running on the same day sends the
same skill.

## Common changes

- **Add or edit a skill:** edit `data/dbt-skills.json`. Every exercise must
  fit in 5 minutes and need nothing but you. Adding entries changes which skill
  lands on which day from then on; that's fine.
- **Preview a day:** `python3 scripts/dbt_skill.py preview --date 2026-10-14`
- **See the whole rotation:** `python3 scripts/dbt_skill.py list`
- **Change the time or pause it:** update the routine in claude.ai/code
  (Routines), not this repo.
