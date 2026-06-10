# Daily podcast-promo automation

Turns each newly-published Keeping It Real episode into a walk-and-talk promo, automatically, the day after it drops.

**The split:** the heavy ingest (RSS check, audio download, Whisper transcription, AI clip-hunter analysis) already lives in the sibling repo `keeping-it-real-content-system` and runs daily via its own GitHub Action (`weekly-sync.yml`, cron flipped to daily). This routine is the creative front-of-house: it watches for the new analysis, looks up the guest's socials, runs the Hype Machine, and delivers a Gmail draft. It does NOT transcribe — that's already done upstream.

```
keeping-it-real-content-system (GitHub Action, daily 3am UTC)
   RSS -> download mp3 -> Whisper transcript -> clip-hunter analysis JSON (committed)
            |
            v
this routine (Claude cloud routine, daily ~12:00 UTC / 7am Chicago)
   detect new episode -> look up guest socials -> Hype Machine promo -> Gmail draft
```

## What the routine does each day

1. **Pull both repos.** This repo (promo engine + state) and `keeping-it-real-content-system` (episode analyses). The KIR repo path is passed to the scripts via `--kir-path` / `$KIR_REPO` (its clone location differs in the cloud vs D.J.'s laptop).
2. **Detect new episodes:** `python3 scripts/podcast-promos/find_new_episodes.py --kir-path <kir>`. Prints a JSON manifest of analyzed episodes not yet in `data/podcast-promo-state.json`. If `new_count` is 0, stop and report nothing new.
3. **For each new episode:**
   a. **Build the brief:** `python3 scripts/podcast-promos/build_promo_brief.py kir "<guest or slug>"` (the deterministic five-beat data extraction).
   b. **Guest socials:** read `data/guest-socials.json` first (keyed by normalized guest name). If the guest is missing, web-search for their Instagram, TikTok, LinkedIn, Facebook, and YouTube handles (use company + location from `guest_info` to disambiguate). Verify the account is really them before trusting it. Write whatever you find back into `data/guest-socials.json` so recurring guests (Carrie McCormick, Chris Linsell, etc.) are not re-searched.
   c. **Write the full-package promo** per [`docs/series/podcast-promo-hype-machine.md`](series/podcast-promo-hype-machine.md) and the CLAUDE.md walk-and-talk rules (spoken script, B-roll, **AI Music Prompt** podcast-promo preset, all five social descriptions). Check + update the dedup registry at [`scripts/podcast-promos/promo-registry.md`](../scripts/podcast-promos/promo-registry.md) so a repeated hook/tip across 700+ episodes does not re-air.
   d. **Episode link + guest tags:** put the episode link where each platform expects it (YouTube = pinned comment, IG/TikTok = link in bio, FB/LinkedIn = link in the post) per the spec. Add the guest's verified @-handles to each platform's caption and append their handles as hashtags alongside the standard set. If a handle could not be verified, leave it out rather than guessing.
4. **Deliver a Gmail draft** (no auto-send) titled `Podcast Promo: <guest> — <episode title>`, body = the full package. Do not commit the promo to the repo (delivery is Gmail-only by choice).
5. **Update state:** add the episode `guid` to `data/podcast-promo-state.json`, commit `data/podcast-promo-state.json` + `data/guest-socials.json`, and push. The state commit is what keeps the routine idempotent across fresh cloud runs; the promo content itself is not committed.
6. **Report:** which episode(s) drafted, the tip used, and the guest handles found / not found.

## Files

| File | Purpose |
| --- | --- |
| [`scripts/podcast-promos/find_new_episodes.py`](../scripts/podcast-promos/find_new_episodes.py) | Detect analyzed episodes not yet promoed (joins KIR index + analyses + state) |
| [`scripts/podcast-promos/build_promo_brief.py`](../scripts/podcast-promos/build_promo_brief.py) | Existing five-beat brief builder (the deterministic half) |
| [`data/podcast-promo-state.json`](../data/podcast-promo-state.json) | Promoed-episode guids (idempotency). Seeded with all episodes through 2026-06-10 so the routine only acts going forward. |
| [`data/guest-socials.json`](../data/guest-socials.json) | Cache of guest social handles, written back as new guests are looked up |
| `docs/series/podcast-promo-hype-machine.md` | The promo format spec / full-package output |

## Edges

- **Episode published but not yet analyzed:** the detector skips it (no analysis file yet) and picks it up the next day once the ingest Action has transcribed it.
- **Coffee Talk episodes** (no guest) flow through the same path; `build_promo_brief.py coffeetalk <slug>` handles them, and there's no guest-social step.
- **Re-seeding:** `find_new_episodes.py --seed` marks everything currently indexed as promoed (used at setup; rarely needed again).
