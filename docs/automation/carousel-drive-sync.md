# Carousel slides to Google Drive

Rendered slides land in the repo. Jennica works out of Drive. This is the bridge.

> **Built as a GitHub Action (2026-08-06).** Make.com was the first plan and it did not
> survive contact: its GitHub app has no branch-level commit watcher. Every candidate
> module turned out to be pull-request scoped, asking for a PR state and then a PR
> number, and the carousel routines push straight to `main` without ever opening a
> pull request. The Action below does the job with no third party in the path.
> The Make scenario is kept at the bottom for reference only.

## The Action

[`.github/workflows/carousel-drive-sync.yml`](../../.github/workflows/carousel-drive-sync.yml)
fires on any push to `main` touching `graphics/carousels/**`, works out which deck
folders changed, and runs [`scripts/drive_sync.py`](../../scripts/drive_sync.py) on them.
Each deck becomes a folder of the same name inside the Drive `carousels` folder.

Uploads are idempotent. A file already in the target folder is updated in place rather
than duplicated, which matters because decks get re-rendered whenever their copy changes.

Run it by hand from the Actions tab any time. Tick **Sync every deck** to push the whole
back catalogue, or leave it unticked and paste space-separated deck paths into the
**decks** box to sync exactly those:

```text
graphics/carousels/EVERGREEN-004-sellers-call-one-agent-carousel graphics/carousels/NF-018-dual-agency-2165-carousel
```

Targeting specific decks matters when some deck folders have been moved out of `carousels`
in Drive: a `--all` run cannot see them there, so it creates a second copy inside
`carousels` and leaves the moved one behind as a duplicate.

### The silent-skip bug, fixed 2026-08-12

The checkout used `fetch-depth: 2`, which is enough history to diff a single-commit push
and nothing more. Push two or more commits at once and `github.event.before` is not in the
clone, so the diff died with `fatal: bad object`. Because that `git diff` sat inside a
pipeline its exit code was thrown away, the deck list came out empty, and the job printed
**"No deck folders changed"** and finished green while skipping the entire push. That is
how `EVERGREEN-004` reached the repo on 2026-08-11 and never reached Drive.

The checkout now uses `fetch-depth: 0`, the step runs under `set -euo pipefail`, and an
unreadable `before` SHA raises a warning and falls back to `--all` instead of quietly
syncing nothing. **A run that legitimately has nothing to do still says so; a run that
cannot work out what to do now says that too.**

### Kale and KIRP split into two folders (2026-08-12)

Drive now looks like this:

```
KR Carousels/           27 Kale and D.J.-brand decks
  gbp/                  GBP post cards, 1200x900
KIRP Carousels/         3 podcast decks
```

The old `carousels` folder was 27 Kale decks to 3 podcast ones, so it keeps its
contents and gets renamed to what it already mostly was. Only the three podcast decks
move.

**What decides where a deck goes is the slug prefix.** `KIRP-*` routes to KIRP,
`KR-*` routes to KR, and anything unprefixed falls back to `lane: "podcast"` in the
deck's source markdown. A deck that matches none of that defaults to KR, because a
misfiled Kale deck is a smaller problem than a KIRP folder that quietly stops
receiving decks. One rule, `drive_sync.is_kirp()`, and both the sync and the reorg
import it, so they cannot disagree about where a deck belongs.

`DRIVE_KIRP_FOLDER_ID` is **optional**. Without it the sync finds the KIRP folder by
name beside the Kale one, creating it if it is missing, so nothing needs minting for
this to work.

**Running the split, or repairing a misfile.** Actions tab > **Drive reorg
(one-time)**. It dry-runs by default and prints exactly what it would do; tick the
apply box to make the changes. Safe to re-run: renaming a folder already named right
is a no-op, and a deck already in the KIRP folder is left alone. The dry run is also
the misfile audit, because it lists every KIRP deck currently sitting in KR.

> `kirp-test` is named like a podcast deck but has no source markdown and no `lane`,
> so it routes to KR. It is a leftover test folder. Delete it rather than fix it.

#### Routing read `lane` alone, and the daily engine broke it (2026-08-15)

`lane: "podcast"` was the whole rule from 2026-08-12, and it held for exactly as long
as every KIRP deck was an episode deck. The daily carousel engine then started
building two KIRP decks a day whose `lane` is the *content* type instead
(`stat`, `market-tip`, `do-this-dont-do-that`, `dont-make-this-mistake`). None of
those equal `podcast`, so all four decks from 2026-08-14 and 2026-08-15 hit the
KR default and were filed under **KR Carousels**.

Nothing errored. The decks rendered, committed, and synced; only the parent folder
was wrong, and the 08-14 watchdog reported `ok` because it checked that the files
existed in Drive without checking *where*. Two days of KIRP decks were misfiled
before anyone saw it.

The fix is the prefix rule above: the engine, `reskin_kr.py`, and the folder names
already agree on `KIRP-`/`KR-`, so routing now reads the one signal that cannot drift
from what the deck actually is. **Any Drive check has to verify the parent folder,
not just existence** — misfiled and delivered look identical otherwise.

### GBP post cards ride the same pipe (2026-08-12)

Google Business Profile cards render to `graphics/gbp/` as flat files
(`YYYY-MM-DD-<slug>.png`), not a folder per deck, so the whole folder is the unit of
sync rather than each card. The workflow watches `graphics/gbp/**` alongside the
carousels and is now called **Graphics to Drive**, because it is no longer only slides.

Where they land depends on one optional secret:

| `DRIVE_GBP_FOLDER_ID` | Result |
|---|---|
| unset (today) | cards go to `carousels > gbp` in Drive |
| set to a folder id | cards upload straight into that folder |

Nothing needs doing to make the sync work. Set the secret only to give the cards their
own top-level Drive folder instead of a subfolder of `carousels`.

Cards are rendered by [`scripts/render_gbp.py`](../../scripts/render_gbp.py) at 1200x900,
which is GBP's aspect ratio. Carousel slides are 1080x1350 and **cannot** be reused as
GBP images: the center-crop between the two eats the headline and the byline.

### Why OAuth and not a service account

The first attempt used a service account and got as far as authenticating and
opening the folder before Drive rejected the upload:

> Service Accounts do not have storage quota.

A service account owns no Drive storage, so it cannot put a file in a personal My
Drive. Google's two sanctioned workarounds, shared drives and domain-wide delegation,
both require Google Workspace. `delfinparis@gmail.com` is a personal account, so the
sync authenticates **as D.J.** with a refresh token instead, and the files land against
his own quota. The service account and its key are dead; delete them if you like.

### One-time setup

**1. OAuth consent screen** (Google Cloud console > APIs & Services > OAuth consent
screen), in the `carousel-drive-sync` project:

- User type **External**, add `delfinparis@gmail.com` as a test user.
- Then set **Publishing status to "In production"**. This one matters. While the app
  sits in *Testing*, Google expires refresh tokens after **7 days**, and the sync would
  quietly stop working a week later. Publishing shows an "unverified app" warning at
  consent, which is expected for a personal script: click Advanced, then continue.

**2. OAuth client** (APIs & Services > Credentials > Create credentials > OAuth client
ID): application type **Desktop app**. Download the JSON.

**3. Mint the token**, once, on the Mac:

```bash
pip install google-auth-oauthlib
python3 scripts/drive_auth.py ~/Downloads/client_secret_*.json
```

A browser opens, you approve, and it prints three values.

**4. Add four repo secrets** at
[Settings > Secrets and variables > Actions](https://github.com/delfinparis/video-strategy-to-grow-dj-brand/settings/secrets/actions):

| Secret | Value |
|---|---|
| `GOOGLE_OAUTH_CLIENT_ID` | printed by the script |
| `GOOGLE_OAUTH_CLIENT_SECRET` | printed by the script |
| `GOOGLE_OAUTH_REFRESH_TOKEN` | printed by the script |
| `DRIVE_CAROUSELS_FOLDER_ID` | `14ZkFmPVWjZL0cJGNM3cfiFwanomVKVQW` (already set) |

**5. Test.** Actions tab > "Graphics to Drive" > Run workflow, tick **Sync every
deck**. All 16 decks should appear in Drive.

The refresh token is a live credential with full access to D.J.'s Drive. It goes into
GitHub secrets and nowhere else, never into a file in this repo.

### If it breaks later

`invalid_grant` on refresh means the token was revoked or expired. The usual cause is
the consent screen slipping back to Testing status. Fix that, re-run `drive_auth.py`,
update the `GOOGLE_OAUTH_REFRESH_TOKEN` secret.

---

## Reference: the Make.com approach that did not work

## Why Make.com and not the routine itself

The Google Drive connector can upload a file, but only by being handed the file's
base64 content. A 150KB slide is roughly 200,000 characters of base64, and a deck is
nine of them. A cloud routine would have to emit ~1.8MB of base64 into its own output to
upload one carousel. That is not a workable path.

Make moves the bytes without any model touching them. The routines already commit
rendered slides to git, so Make only has to mirror a folder.

## The shape

```
routine renders -> git push -> Make sees the commit -> copies to My Drive > carousels
```

Everything under `graphics/carousels/<deck-slug>/` mirrors to `My Drive > carousels >
<deck-slug>/`, matching the folder layout already there from the July batch.

## The Make scenario

**Trigger: GitHub > Watch Commits**
- Repo: `delfinparis/video-strategy-to-grow-dj-brand`
- Branch: `main`
- Limit: 5

**2. Iterator** over the commit's `files[]` array.

**3. Filter** — only carousel output:
- `filename` starts with `graphics/carousels/`
- and `filename` matches `.png|.pdf|.txt` at the end
- and `status` is not `removed`

**4. HTTP > Make an API Key Auth request** — fetch the file bytes:
- URL: `https://api.github.com/repos/delfinparis/video-strategy-to-grow-dj-brand/contents/{{filename}}?ref={{sha}}`
- Header: `Accept: application/vnd.github.raw`
- API key connection: a GitHub personal access token with `repo` scope (the repo is private)
- **Parse response: NO.** The body must stay binary or the PNGs corrupt.

**5. Google Drive > Search for Files/Folders** — find the deck folder:
- Search in: `carousels` (folder id `14ZkFmPVWjZL0cJGNM3cfiFwanomVKVQW`)
- Query: name equals the second-to-last path segment of `filename`, i.e. the deck slug
- Type: folder

**6. Router**
- Route A, when step 5 returned nothing: **Google Drive > Create a Folder**, named the
  deck slug, inside `carousels`.
- Route B: pass through.

**7. Google Drive > Upload a File**
- Folder: the id from step 5 or step 6
- File name: the last path segment of `filename`
- Data: the binary body from step 4
- **Overwrite if exists**, because a deck gets re-rendered whenever its copy changes.

**Schedule:** every 15 minutes is plenty. The routines run once a day at most.

## Getting the deck slug in Make

`filename` arrives as `graphics/carousels/KIRP-carrie-mccormick-carousel/slide-03.png`.

- deck slug: `{{split(filename; "/")[3]}}`
- file name: `{{last(split(filename; "/"))}}`

Make's `split` is 1-indexed, so element 3 is the folder and element 4 is the file.

## Reconciling what is already there

The `carousels` folder in Drive holds 14 decks from a one-time build on July 12 and 13,
under shortened names (`NF-060-listing-off-zillow`) that do not match the repo slugs
(`NF-060-should-i-keep-listing-off-zillow-carousel`). Those decks also predate the
current design, the sampled colors, the footer, and the no-asks close.

Simplest reconciliation: **delete the 14 old folders once the sync is running.** Every
one has been re-rendered in the current design and will re-sync under its repo slug.
Nothing is lost that git does not hold.

## If Make turns out to be a nuisance

The alternative is a GitHub Action in this repo that pushes to Drive with a Google
service account, triggered on any change under `graphics/carousels/`. It is more
reliable and version-controlled, but it needs a service account created in Google Cloud,
the `carousels` folder shared with that account's email, and the JSON key stored as a
repo secret. More setup up front, less to babysit after. Say the word and it gets built.
