# Stoic lesson of the day (8am email)

Personal, not content work. Every morning at about 8am Central, one Stoic
quote, a short lesson on it, and one exercise you can finish in 5 minutes
land in delfinparis@gmail.com. Built as a twin of the
[DBT skill email](dbt-skill-email.md).

## How it works

| Piece | What it does |
|---|---|
| `data/stoic-lessons.json` | The library: 36 lessons, 12 each from Marcus Aurelius, Epictetus, and Seneca, interleaved so no two days in a row share a teacher. |
| `scripts/stoic_lesson.py` | Picks today's lesson, `(date - 2026-10-01) % 36`, and renders the subject, plain-text and HTML body as JSON. No state, no network, no API key. |
| Routine **Stoic lesson of the day** | Claude Code routine, 8:00am `America/Chicago` daily. It runs `python3 scripts/stoic_lesson.py today` and sends the result through the Gmail connector. |

Because the pick is computed from the date, a missed day just skips that
lesson. The rotation never drifts, and re-running on the same day sends the
same lesson.

## Quotes are verbatim

Every quote comes word for word from a public-domain translation: George Long
for Marcus Aurelius (Gutenberg #15877) and Epictetus (Gutenberg #10661), and
Richard Mott Gummere for Seneca's letters (Wikisource). Long and Gummere read
older ("thou," "to-day") than modern paperbacks, which is the price of quoting
exactly without copyright trouble. Do not swap in modern translations such as
Hays or Robertson; they are under copyright.

`python3 scripts/stoic_lesson.py check-quotes` downloads the source texts and
confirms every quote appears in them. Run it after adding or editing a lesson.

## Common changes

- **Add or edit a lesson:** edit `data/stoic-lessons.json`, then run
  `check-quotes`. Every exercise must fit in 5 minutes and need nothing but
  you. Adding entries changes which lesson lands on which day from then on;
  that's fine.
- **Preview a day:** `python3 scripts/stoic_lesson.py preview --date 2026-10-14`
- **See the whole rotation:** `python3 scripts/stoic_lesson.py list`
- **Change the time or pause it:** update the routine in claude.ai/code
  (Routines), not this repo.
