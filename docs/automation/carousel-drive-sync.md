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

Run it by hand from the Actions tab any time, and tick **Sync every deck** to push the
whole back catalogue rather than just what changed.

### One-time setup

Two repo secrets, and one sharing step that is easy to forget.

1. **Create a service account.** In Google Cloud console, pick or create a project,
   enable the **Google Drive API**, then create a service account. No roles needed; it
   only ever touches folders explicitly shared with it.
2. **Create a JSON key** for that service account and download it.
3. **Share the Drive folder with the service account.** Open `My Drive > carousels`,
   Share, paste the service account's email (it looks like
   `something@project-id.iam.gserviceaccount.com`), give it **Editor**. Without this the
   Action authenticates fine and then reports the folder does not exist, because a
   service account sees nothing by default.
4. **Add the repo secrets** under Settings > Secrets and variables > Actions:

   | Secret | Value |
   |---|---|
   | `GOOGLE_SERVICE_ACCOUNT_JSON` | The entire contents of the JSON key file |
   | `DRIVE_CAROUSELS_FOLDER_ID` | `14ZkFmPVWjZL0cJGNM3cfiFwanomVKVQW` |

5. **Test it.** Actions tab, "Carousel slides to Drive", Run workflow, tick "Sync every
   deck". All 16 decks should appear in Drive.

Until those secrets exist the Action runs and fails at the last step. Nothing else
breaks; the routines and the renderer do not depend on it.

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
