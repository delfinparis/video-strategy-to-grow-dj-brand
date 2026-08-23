# Claude Instructions — video-strategy-to-grow-dj-brand

Project-specific operating rules for Claude when working in this repo. Universal editorial rules live in [`docs/editorial-standards.md`](docs/editorial-standards.md); series rules live in `docs/series/`. This file captures workflow defaults that aren't editorial — things Claude should *do every time* without being reminded.

---

## Read this first: the 2026-07-21 goal reset and gate layer

The strategy changed on 2026-07-21. Before any content strategy work, read
[`docs/strategy/2026-07-21-goal-reset-and-gate-layer.md`](docs/strategy/2026-07-21-goal-reset-and-gate-layer.md)
and [`docs/content-pillars.md`](docs/content-pillars.md). The short version:

**The one thing:** *D.J. Paris tells real estate agents exactly what to do and say to grow their business.*

**Why it changed:** the Apr-Jul 2026 pivot produced a reliable content machine and **zero** recruiting
conversations, because no post in 90 days asked a viewer to raise a hand
([the review](docs/analytics/2026-07-19-pivot-results.md)).

**The week: 20 posts.** 15 videos (6 Value Giveaways *gated*, 3 Takes, 2 News, 2 Broker Problems,
2 KIRP promos; Chicago Agent Spotlight substitutes in) + 5 carousels (2 gated, 3 open).
The 3 takes were added 2026-08-10 ([`docs/series/take-standard.md`](docs/series/take-standard.md)).

**Which content gets a gate — this decides how you write the close:**

| Content | Gate? |
|---|---|
| Value Giveaways (say-this / tool use-case / prompt), tool launches, event promos | **Gated** on IG + FB |
| Gated carousels (2 of 5) | **Gated** on IG + FB; LinkedIn gets a link in the first comment instead |
| News, Broker Problems, **Takes**, KIRP promos, Spotlight, the 3 open carousels | **Never gated**, any platform |
| Anything on **LinkedIn** | **Never a keyword gate.** Ever |

A gated close is a *value-exchange gate* (a keyword delivering a real artifact), permitted by the
Rule 4 exception in [`docs/editorial-standards.md`](docs/editorial-standards.md). Hollow bait
("comment YES," "save this," "follow for more") stays banned everywhere, gated or not. Ungated
content keeps the full "here's what you do now" close with zero engagement asks.

**Keywords are never invented on the fly.** Pull from [`data/keyword-registry.md`](data/keyword-registry.md)
and pass them verbatim — a reworded keyword silently breaks the ManyChat trigger and the leads vanish
with no error. Flow spec: [`docs/automation/manychat-flows.md`](docs/automation/manychat-flows.md).

**Quality floor:** the 3-pass rigor below is non-negotiable at 17 posts/week. If a week cannot clear
that bar, ship fewer posts. Volume is never the goal.

---

## When D.J. says "walk and talk", build today's script on demand

D.J.'s daily options are researched + committed by the 6am home-Mac job and
pushed to his phone (no email anymore). When he says **"walk and talk"** (with or
without a number), follow [`docs/automation/walk-and-talk-on-demand.md`](docs/automation/walk-and-talk-on-demand.md):
`git pull`, read today's `data/news-briefs/<today>.md`, show the numbered options,
let him pick, then build the chosen option through draft → stress-test → EP-polish
→ council review and deliver only the final v3 (with the `## AI Music Prompt` block
and the `## Council Review` block). If today's brief is missing, offer to run
`python3 scripts/news_brief.py` right then.

**Every walk-and-talk is 22-30 seconds, hard cap 35.** Set 2026-08-15, replacing the old 45-75s
range. That is **48-72 spoken words**, 85 at the absolute wall. Count the words in the finished
script and put the count in the frontmatter; do not estimate, because a draft that feels like
30 seconds is reliably 45. There is no earned-length exception anymore. The reason is completion:
sub-30s video is graded against a ~65% average-view-duration threshold and everything longer
against a stricter effective bar, so length now decides which curve the video is scored on. Full
rationale in Rule 7 of [`docs/editorial-standards.md`](docs/editorial-standards.md). If the
material will not fit, it is two scripts, not one long one.

**Heat 4 is the default register, and heat 5 is banned.** Also 2026-08-15. The old
"one heat-4/5 post per week" ration is gone. At 25 seconds the hook carries the entire
distribution load, so a defensible reframe is no longer a strong enough reason to stop scrolling.
Write the hook on a cost, a loss, or a wrong default that someone profits from. Two guardrails
replace the ration and both are absolute: **friction points outward** at a belief, practice, tool,
system, or incentive and never at the agent (Rule 9.4), and **heat 5 — naming a person,
brokerage, coach, or product as wrong — never ships on any series.** Institutional public record
(a filed suit, a published settlement, an announced policy) stays reportable at heat 4.

**The four passes are non-negotiable. Run them silently, deliver only the final v3.** Even when
the first draft looks strong, never skip straight to delivery. Each pass has a concrete job:

- **Pass 1 — Draft.** Build to the 3-act spine, a deliberate hook family, a pattern interrupt, the `## AI Music Prompt` block, and all five captions. The HOOK opens with a standalone **scroll-stop** first spoken line (rule below). Draft to 60 words, not to "short" — write the word budget at the top of the draft and hold to it, because cutting a 130-word script down to 60 loses the hook's sharpness every time.
- **Pass 2 — Stress-test.** Run the **Story Pass** ([`docs/series/viral-3-act-spine.md`](docs/series/viral-3-act-spine.md)) first: does Act 2 have a real turn, not a briefing? Then the **scroll-stop test**: read only the first spoken line — does it stop the scroll on its own in 3 seconds, or is it warm-up? Then the hook 3-second test, the AI-tells scrub ([`docs/ai-tells-field-guide.md`](docs/ai-tells-field-guide.md)), and for NF confirm every claim has a named source + date + URL. Fix what fails before polishing.
- **Pass 3 — EP-polish.** Count the spoken words and cut to the 48-72 band (Rule 7). Cut whole sentences, never three words off each of five sentences, and take nothing out of the hook. Sharpen the shareable moment to one sendable line, read the close aloud and kill any motivational-poster ending, then run the caption + hashtag-cap scrub below. Then hand v3 to Pass 4.
- **Pass 4 — Council review.** Run the finished v3 through the Short-Form Council ([`docs/short-form-council-pass.md`](docs/short-form-council-pass.md)): ten creator/marketer doctrines plus two research witnesses (Heath on curiosity mechanics, Berger on shareability) pressure-test the hook, retention, and shareability. Append a `## Council Review` block beneath v3 with 2-3 tested **spoken** scroll-stop variants mapped to hook families, a one-line why-it-works (hook mechanism / share driver / retention move), and the single dissent to A/B test next. It never adds manual on-screen text (captions build from audio) and never undoes a Pass-3 scrub. If the local deep-reference skill is installed (`~/.claude/skills/short-form-council`), load its book-backed `references/*.md` for depth; otherwise run from the doctrines in the doc. Then deliver v3 (script + AI Music Prompt + Council Review).

**The 0:00 scroll-stop is mandatory, and it is spoken.** The first line out of D.J.'s mouth (0:00-0:03) has to stop the scroll on its own, before any context. captions.ai builds the on-screen captions from the audio, so the scroll-stop lives in the **spoken** first line, never a manual text overlay (that is why `scripts/strip_onscreen_text_v2.py` exists). Every walk-and-talk `### HOOK` beat opens with it:

- **Front-load the tension in the first 3-5 words.** "NAR just changed what you owe your seller" stops the scroll. "Today I want to talk about some new NAR guidance" does not.
- **One complete, arresting line that opens a loop** the video then closes. No warm-up, no "hey guys," no throat-clearing sentence before it.
- **50-60% of all drop-off happens in the first 3 seconds** (2026 retention math, [`docs/hook-matrix-cheatsheet.md`](docs/hook-matrix-cheatsheet.md)). The scroll-stop is the whole distribution lever, not a nicety.
- **The hook occupies 0:00-0:03 and is one sentence.** At a 25-second runtime a 9-second hook beat is a third of the video. Land it in a single line and move.
- **Lead on the negative.** Open on what it costs, what it is taking, or what the viewer already got wrong. Loss framing lands harder and faster than gain framing at equal magnitude, and 3 seconds is not enough time for an upside promise to register. "This is costing you a listing a quarter" beats "here is how to win one more listing a quarter." Same script, different opening valence.
- **Pull a ready first line from [`docs/opener-swipe-file.md`](docs/opener-swipe-file.md)** mapped to the chosen `hook_family`, then sharpen it to the specific news. Never write the hook cold.

Before delivering the v3, run every social caption AND its hashtag block through the
scrub in the **Social descriptions** section below: no em dashes, no AI-speak, and the
**hashtag caps** from [`docs/caption-and-hashtag-strategy.md`](docs/caption-and-hashtag-strategy.md)
(LinkedIn/IG/TikTok/YouTube 3-5, Facebook 2-3, realtor-first, one brand tag). This runs
every time, without D.J. asking. Do not copy hashtag counts from older example scripts.

Every walk-and-talk follows the **Viral 3-Act Spine** ([`docs/series/viral-3-act-spine.md`](docs/series/viral-3-act-spine.md)): HOOK (stop the scroll + promise the payoff) → STORY (the middle is a story with a turn, not a briefing) → PAYOFF (resolve the loop → "here's what you do now" action → loop-back). The stress-test pass runs the **Story Pass** before anything else. **At 22-30 seconds every series runs the compressed Act 2** -- one sentence carrying one turn, then the payload. The old narrative/tactical split (full three acts for Inside the Industry and Podcast Promo, compressed for Playbook, What Actually Works and tapthis) is retired: the compressed version is now universal, because 60 words cannot hold a developed middle. The turn still has to be there. A one-sentence Act 2 with no turn is a briefing, and the Story Pass still fails it.

For the hook itself, reach into the **Hook Matrix** (Rule 10 in [`docs/editorial-standards.md`](docs/editorial-standards.md)): pick one of the nine families on purpose, log it as `hook_family` in frontmatter, and don't repeat a family across two consecutive posts. Friction families (Sacred Cow, System Indictment, Forbidden) ride heat 4 and are now the **default**, not a weekly ration (Rule 9.2, revised 2026-08-15); they point friction outward at a belief or system and stand with the agent, never at the agent. The non-friction families stay in rotation for variety, but each still has to open on a cost or a wrong default to earn heat 4. Heat 5 is banned outright. Swap/List hooks (Family 9: "don't say X, say Y," stop-doing, do-don't-in-the-room) are the default saveable format for tactical series. Roughly every couple of weeks, run one **emotional / identity** script (Rule 10.7) instead of a tip -- a permission slip or why-this-work-matters piece -- because that's what earns follows and the long comments tactics don't. Ready first lines mapped to the nine families live in [`docs/opener-swipe-file.md`](docs/opener-swipe-file.md) -- pull from there before writing a hook cold.

Before writing Act 2, decide the **story shape** ([`docs/storytelling-formats.md`](docs/storytelling-formats.md)): whose story is this and what arc does it run? Ten first-person formats, each rated Adopt / Adapt / Reject for D.J. and rewritten to survive Rules 1, 4, and 5. Format 2 (lead with proof, then teach) is the tactical workhorse; Format 10 (tell someone else's story, sourced from the KIR archive or the Kale mentor protocol) is the highest-value one and the most under-used. Formats 4 and 5 are rejected -- do not build them. Log the choice as `story_format` in frontmatter when a script deliberately runs one. Two traps that doc exists to stop: **the mad-lib blanks invite fabrication** (a "lowest moment" picked off a menu is a Rule 1 failure), and **every CTA in the source material is a Rule 4 engagement ask** -- rebuild closes on Rule 10.4/10.5 instead.

Pair every hook with a **visual open** (pattern interrupt) from [`docs/pattern-interrupt-cheatsheet.md`](docs/pattern-interrupt-cheatsheet.md). D.J. films walk-and-talks on a selfie stick, so the visual open is one of seven one-handed, mid-walk moves (The Stop, Push-In, Whip, Walk-Toward, One Prop, Location Cold-Open, Gesture-On-Beat). Pick one on purpose, log it as `pattern_interrupt` in frontmatter next to `hook_family`, and don't repeat the same move two posts in a row. The spoken hook still does the heavy lifting (captions.ai builds captions from audio); the visual open is the second stop signal. When the script is on-site at a property, prefer the Location Cold-Open -- the property is B-roll you can't otherwise shoot.

## The Notion Content Board is where finished scripts wait

Every lane's picked-over inventory lives on the [Content Board](https://www.notion.so/35037694472d47d9a5c8c34cfa95d9e4)
in Notion, and **every row carries its finished v3 in the page body** -- D.J. opens
a row and films it. A row with a good hook and an empty body is a failure, not a
draft. The contract, the lane targets, and the body template are in
[`docs/automation/content-board.md`](docs/automation/content-board.md); the
deterministic half is `scripts/content_board.py` (exit 10 = work due, same
convention as `stupid_things.py`). The board carries no Source and no Bank ref
column on purpose -- the receipt lives under `## Data Source` in the body and the
bank pointer lives in the footer line.

## When the script is posted, work the first hour (engagement ops)

These are not editorial -- they're posting-day habits the algorithm rewards harder than anything in the script (Rule 10.4-10.6):

- **Reply to every comment in the first 60 minutes.** Creator replies are weighted for distribution and turn one comment into a thread.
- **Pin a value-extending first comment** -- the exact script, the next step, the receipt/source -- never a "follow me." Drives comment-section dwell without an ask.

---

## Always include an AI Music Prompt with every walk-and-talk script

**Scope:** Any 22-35s talking-head script in this repo. Specifically:
- All `scripts/inside-the-industry/` scripts (NF, IS, IA)
- All `scripts/the-playbook/` scripts
- All `scripts/takes/` scripts
- All `scripts/ai-tip-of-the-week/` scripts
- All `scripts/podcast-promos/` scripts
- Any new short-form talking-head series we add

D.J. calls these "walk-and-talks." They get cut in CapCut and need a music bed at 10-15% volume per [`docs/capcut-editing-playbook.md`](docs/capcut-editing-playbook.md) Part 6.

**The rule:** Every walk-and-talk script must end with an `## AI Music Prompt` section *beneath* the `## Data Source` section. D.J. edits only in CapCut, so there is a single CapCut prompt — no Suno/Udio. Format:

```markdown
## AI Music Prompt

**Vibe:** [one-line description tuned to this specific script's energy]

**CapCut AI Music:**
> [calibrated CapCut prompt, <=300 chars — start from the matching preset in docs/ai-music-prompts.md, then tune BPM/energy/key descriptors to the actual script content]
```

**Where to pull the templates from:** [`docs/ai-music-prompts.md`](docs/ai-music-prompts.md) has CapCut presets for each sub-type (NF default, NF big-number, IS, IA, Playbook, AI Tip of the Week, podcast promo) plus the master template and the troubleshooting table.

**Don't just paste the preset verbatim.** Tune it:
- **BPM:** 90 for sober/legal news, 95 default NF, 100 for big-number / scoreboard moments, 105-108 for tactical/upbeat, 90 for reflective synthesis.
- **Energy descriptor:** Match the script's emotional register. A $52M settlement is "urgent but controlled." A "five brokerages in three months" scoreboard is "confident with forward momentum." A reflective IS about top producers is "warm and authoritative."
- **Key feel:** Default minor-key-but-hopeful. Major-leaning for Playbook/AI Tip/Podcast Promo. Avoid pure-dark minor unless the news genuinely warrants it (it almost never does).

**Non-negotiables in every prompt** (these are what make tracks voiceover-safe):
- `[no vocals]` or `instrumental only` at the **start** of the style prompt
- `no melodic hook, no vocal chops, no risers, no whooshes`
- `unobtrusive background for voiceover` or `doesn't compete with speech`
- `loopable`
- Specify BPM as a number

**When in doubt:** Use the NF default preset from [`docs/ai-music-prompts.md`](docs/ai-music-prompts.md) and tune from there.

---

## When updating older scripts

If you're editing a script that doesn't have an `## AI Music Prompt` section yet, add one. Don't ask first — it's a known gap from before this rule existed.

---

## What walk-and-talk does NOT include

These series don't need an AI Music Prompt block (different format or already-set audio):
- `scripts/agent-tip-of-the-day/` — frozen / curation-pending, don't touch
- `scripts/ai-agent-minute/` — frozen, don't touch
- `scripts/reels/` — these are generated assets, not scripts
- `data/news-briefs/` — these feed scripts, they're not scripts themselves

---

## Social descriptions: no em dashes, no AI speak

**Scope:** Every social caption block in every script in this repo (LinkedIn, Instagram Reels, TikTok, YouTube Shorts, Facebook). Applies in addition to the universal Rule 5 in `docs/editorial-standards.md`.

**No X/Twitter captions.** D.J. does not use X. Scripts produce five captions (LinkedIn, Instagram Reels, TikTok, YouTube Shorts, Facebook). Do not add an `### X (Twitter)` block to any script, and remove one if you find it in an older script you're editing.

**The rule:** Social captions get the strictest scrub.

- **Zero em dashes.** Not `—`. Not `--` (the editorial-standards substitute). Use periods, commas, or restructure the sentence. The `--` substitute is fine in spoken-script sections, length justifications, and Data Source notes; it is banned in social captions because it reads as AI-generated copy on a social feed.
- **Zero AI-speak transitions.** No "Here is what this means," "Here is the part that makes this interesting," "Here is why that matters," "Worth noting," "That should change everything," "In a market like this," or any of the banned AI-speak words from Rule 5.
- **Zero throat-clearing setups.** A new paragraph in a social caption should not begin with a transition sentence whose only purpose is to set up the next sentence. Cut the transition; lead with the substance.
- **Hashtag caps from [`docs/caption-and-hashtag-strategy.md`](docs/caption-and-hashtag-strategy.md), applied at draft time.** LinkedIn/Instagram/TikTok/YouTube Shorts = **3-5 hashtags**, Facebook = **2-3**. Realtor-first, exactly one brand tag (`#InsideTheIndustry` or `#KeepingItRealPodcast`), drop the long tail (`#RealtorLife`, `#RealEstateCoaching`, `#realtortok`, generic community tags). Fewest hashtags that still categorize the post. Do the discovery work with a real search keyword in the first line/125 chars, not a tag stack (Rule 2 of that doc).
- **Never copy hashtag counts from an older example script.** Scripts written before 2026-07-07 (NF-060 and earlier) carry the retired 11-14 tag stacks. Build the hashtag block fresh from the caps above every time; do not lift it from a reference file.
- **Apply this automatically every time.** Do not wait for the user to ask for the scrub. Any script draft, polish pass, or rewrite that includes social descriptions must run the descriptions AND the hashtag block through this filter before commit.

If a sentence in a social caption needs a pause that an em dash would normally create, restructure as two short sentences. "X. Y." beats "X -- Y." in every social-feed context.

---

## CapCut AI Music prompts: 300-character hard cap

**Scope:** Every CapCut AI Music prompt this repo produces, whether it lives in the `## AI Music Prompt` section of a script or is sent inline in a chat reply.

**The cap:** 300 characters maximum, including spaces and punctuation. CapCut's AI music input has a hard 300-char limit; longer prompts get truncated silently and the generator works from a partial input.

**What a CapCut prompt must include in 300 chars:**

1. Style / genre (e.g., "modern documentary editorial score")
2. BPM (e.g., "95 BPM")
3. Mood, 2-4 words (e.g., "authoritative, confident, verdict-in")
4. 3-4 instruments max (e.g., "muted piano, pulsing synth bass, soft percussion")
5. The "no vocals" constraint (always)
6. Runtime hint (e.g., "25-30s")

The CapCut prompt is the only music prompt (no Suno/Udio). If a descriptor won't fit, drop the least-important exclusion (`no risers`, `no reverb tails`) rather than ship an over-cap prompt that gets truncated. If a prompt would be meaningfully better at 350-400 chars, flag it and ask whether to split into two CapCut generations.

---

## AI tells: scrub against the field guide before commit

**Scope:** Every script section and every social caption block this repo produces. Reference: [`docs/ai-tells-field-guide.md`](docs/ai-tells-field-guide.md).

**The rule:** Read the field guide mentally before drafting. The vocabulary bans (banned adjectives, verbs, metaphorical nouns, hedging markers, transition phrases, promotional buzzwords, conclusion clichés) apply automatically. The "Used Once" patterns (negative parallelisms, Rule of Three, contrast structure, data-as-character personification, aphoristic closes, triple-word repetition, "Here's the [adjective] part" reveals) must be deployed deliberately and never stacked within the same script.

**Apply at draft time, not as follow-up scrub.** If you catch yourself reaching for "delve," "tapestry," "It's not X, it's Y," or any of the patterns on the field guide list -- pick a different construction before writing it.

**Pre-commit self-audit** (per the field guide's Part 8 checklist):

- Scan every social caption for em dashes (`-` or `--`). Restructure if present.
- Count "It's not X, it's Y" / "Not just X, but Y" constructions. Max one per script.
- Count Rule-of-Three constructions (triple lists + triple adjectives + triple-word staccato). Max one per script.
- Scan against the vocabulary lists in Parts 1 of the field guide.
- Read the close aloud. If it sounds like a motivational poster, rewrite.
- Check the action layer count -- if every recent script opens with "Three plays," vary it.
- Scan for self-answered rhetorical questions.
- Verify hedging language is intentional, not reflexive.

**If a pattern works hard and earns its place, keep it.** The discipline is about not stacking, not about banishing every rhetorical move. One sharp "It's not X, it's Y" lands; three in the same script reads as AI.

**When the field guide and a script's specific editorial framing conflict:** the field guide wins unless there's a specific reason to override, documented in the script's Production Notes.

---

## Building a podcast promo? Use the Hype Machine engine

Any walk-and-talk that promotes a podcast episode (Keeping It Real or Coffee Talk with Tim & D.J.) goes through the engine, not freehand. It turns one episode into a "on this episode we got into X, Y, Z, we solved these problems for agents, here's a tip for your next client" promo.

1. **Build the brief:** `python scripts/podcast-promos/build_promo_brief.py <kir|coffeetalk> <episode-query>` (query matches a guest name or slug fragment). It pulls the episode's own intelligence into the five-beat arc and writes a brief to `scripts/podcast-promos/_briefs/`.
2. **Read the format spec:** [`docs/series/podcast-promo-hype-machine.md`](docs/series/podcast-promo-hype-machine.md) -- the arc, the source adapters, and the full-package output spec.
3. **Check + update the registry:** [`scripts/podcast-promos/promo-registry.md`](scripts/podcast-promos/promo-registry.md). Across 700+ KIR episodes the same tip repeats; verify the hook and tip haven't aired, then add a row.
4. **Output the full package** to `scripts/podcast-promos/<show>-<slug>.md`: spoken script + B-roll + AI music prompt (Podcast promo preset) + all five social descriptions. Reference: [`scripts/podcast-promos/kir-2026-01-30-amanda-pendleton.md`](scripts/podcast-promos/kir-2026-01-30-amanda-pendleton.md).

The tip is the payload: lift one physical, do-it-tomorrow tactic from the episode. No fabricated stats -- every number traces to the analysis JSON (KIR) or the aired script (Coffee Talk).

---

## D.J. says "takes"? Show the week's options, then build the pick

When D.J. says **"takes"** (with or without a number), work from the weekly brief:

1. `git pull` (3 devices), then read the newest `data/take-briefs/*.md`.
2. Show the options as a short numbered list: the cow plus its one-line hook. No preamble.
3. D.J. picks a number, or several. Build each per the standard below.
4. If today's brief is missing, run `python3 scripts/take_brief.py` right then. It needs no API
   key and no network. If the brief exists but its options still say `_[routine fills in]_`, the
   Sunday routine died halfway: source the receipts and write the hooks live before building.

The brief is produced Sunday 7:00am CT by the **Take Brief** routine, which runs the script and
then web-verifies every option marked NEEDS RECEIPT. Full chain, and why it deliberately does
NOT use the walk-and-talk email machinery: [`docs/automation/take-brief.md`](docs/automation/take-brief.md).

## Building a take? Follow the take standard

Build per [`docs/series/take-standard.md`](docs/series/take-standard.md). Three a week,
Mon/Wed/Fri, ungated on every platform, output to `scripts/takes/TAKE-###-slug.md`.
The short version:

1. **Re-verify the receipt before drafting, every time**, whatever the brief says. A brief is a
   shortlist, not a clearance. Entries marked `evidence: research` in
   [`data/sacred-cows.md`](data/sacred-cows.md) have no sourced number yet; if one cannot be
   found, drop the option rather than soften the claim. No repeats inside 8 weeks.
2. **Five beats in 60 words.** THE COW → WHO PROFITS → THE RECEIPT → THE SWAP → LOOP-BACK. Beat 2
   (who makes money from this belief surviving) is what makes it a take instead of a tip. Beat 4
   is the "do Y instead" half and it is not optional -- an indictment with no swap is a rant.
   Under the 22-30s rule each beat is **one sentence**, and beats 1 and 2 often share one:
   "You are still paying for [cow], and [who] is the reason it never dies."
3. **Heat: 4 every day the lane runs.** Mon, Wed and Fri all sit at 4. The old "3.5 Mon/Fri,
   one 4 on Wed" split is retired along with the Rule 9.2 weekly ration (2026-08-15) -- there is
   no friction slot to spend anymore. Heat 5 (naming a person, brokerage, coach, or product)
   is banned outright in this lane, as everywhere.
4. **Rotate the hook family** so three swaps a week don't read formulaic: Mon Family 9, Wed
   Family 2 or 4, Fri Family 5, 7, or 8. Never the same family as the day's paired carousel.
5. **Pair it.** Each take shares its bank entry with that day's take carousel and logs one row in
   the rotation table for both. Video argues it, carousel hands over the receipt.
6. **Never gate a take.** No keyword, on any platform, including IG and FB.

Two extra checks in the stress-test pass: the **rant test** (strip the swap -- is what's left
still worth posting?) and the **recruiting test** (read the hook as a good agent who might join
Kale; do they respect D.J. more or less?).

## D.J. says "stupid things"? Pull from the bank, then build the pick

The **Stupid Things Realtors Do** lane names a specific bad behavior and hands over the exact
fix. It is **not** The Take: a take needs a *who profits* beat, and nobody profits from an agent
who doesn't return a call. Charter and qualifying test:
[`data/stupid-things.md`](data/stupid-things.md).

1. `git pull` (3 devices), then `python3 scripts/stupid_things.py pick --count 5 --stdout`.
2. Show the options as a short numbered list. No preamble.
3. D.J. picks a number. Build it through the four passes, out to
   `scripts/stupid-things/STUPID-###-slug.md`.
4. **Re-verify the receipt at build time, every time.** Most bank entries ship
   `receipt: needed` on purpose. If a number cannot be sourced to a named publisher and a year,
   drop it or run the script without a number. Never soften an unverified figure into a claim.
5. **Log the angle when the script is done**, or it stays in the pool and gets built twice:
   `python3 scripts/stupid_things.py log --id ST-00XX --script scripts/stupid-things/...md`

**Availability is counted in angles, not practices** (D.J., 2026-08-13). The same practice runs
again as long as the angle on the *solution* is new; a reword is not a new angle and
`intake` refuses it. Bank target 20, refill fires at 5, and the weekly routine only does the
expensive scouring when `health` returns exit code 10. Full chain:
[`docs/automation/stupid-things-bank.md`](docs/automation/stupid-things-bank.md).

Two things this lane does that the others do not: every entry is tagged `target: sideways`
(the agent on the other side of the deal) or `target: self` (the viewer), and `pick` alternates
them so the lane never becomes all-confessional or all-finger-pointing. Sideways is the default
because the good agent watching is the wronged party, not the accused. Say **"stupid things
refill"** to run a refill by hand.

## Doing a Chicago Agent Spotlight? Follow the standard

When D.J. says **"spotlight"** (or picks the Chicago Agent Spotlight option in the daily brief), build it per [`docs/series/chicago-agent-spotlight-standard.md`](docs/series/chicago-agent-spotlight-standard.md). Scout one fresh Chicago agent in the news, **verify the social handle before tagging** (never guess), verify every fact to a named source, and never AI-generate the person's face. Frame on the person + the lesson, not the rival brokerage; no poaching tone. Build the full unit (walk-and-talk + companion carousel + verified tags + post-publish DM), then log the carousel to the **Daily Carousels** Notion database (https://app.notion.com/p/27267ba77da64ef5a5033fc1dd992a0a) with the full slide copy in the page body. Judge these on reshares + followers, not saves. Reference: [`scripts/chicago-agent-spotlight/dawn-bremer-2026-07-08.md`](scripts/chicago-agent-spotlight/dawn-bremer-2026-07-08.md).

## Other project defaults

- **Editorial voice:** Read [`docs/editorial-standards.md`](docs/editorial-standards.md) before drafting any script. Universal rules win over series rules.
- **Series standards:** Each series has its own standard in [`docs/series/`](docs/series/). The Inside the Industry standard ([`docs/series/inside-the-industry-standard.md`](docs/series/inside-the-industry-standard.md)) is the primary one.
- **CapCut workflow:** [`docs/capcut-editing-playbook.md`](docs/capcut-editing-playbook.md) — including the music volume rule (10-15%) the AI music prompts are calibrated for.
- **Source rigor for NF:** Every NF claim needs a named source, publication date, and URL or case number. No rounding numbers. No "roughly."
- **Always `git fetch` first** when assessing repo state (D.J. works on this repo from 3 different devices).
