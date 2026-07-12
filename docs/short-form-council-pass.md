# The Short-Form Council — Pass 4 (final board review)

The council is the last pass of every walk-and-talk build: draft (Pass 1) ->
stress-test (Pass 2) -> EP-polish (Pass 3) -> **council review (Pass 4)**. Where
Passes 2 and 3 run this repo's mechanical checklists (Story Pass, scroll-stop
test, AI-tells scrub, caption + hashtag caps), Pass 4 runs the finished v3 past
ten proven creator/marketer doctrines and two research witnesses. It is the
strategic + psychological layer the checklists don't cover, and it always ends
with the one experiment to run next.

**It never breaks a house rule.** No manual on-screen text (captions.ai builds
captions from the spoken audio, so every hook lives in the spoken first line).
No em dashes in captions, AI Music Prompt stays, 300-char CapCut cap, hashtag
caps, NF source rigor. The council sharpens within those rules, never around
them.

**Deep-reference note.** The full council, with book-backed distillations
(Hook Point, The Guide to Going Viral, Made to Stick, Contagious, the MrBeast
production doc), lives in the LOCAL skill at `~/.claude/skills/short-form-council`.
Those distillations are copyrighted source material and are intentionally NOT in
this public repo. If the local skill is installed on this machine, load its
`references/*.md` for depth. If not, run the pass from the doctrines below --
they are original synthesis and fully portable.

---

## The board (doctrines — embody them, don't blend them)

The value is friction. Each voice has a bias and a pet question. A member who
agrees with everyone gets cut from that round.

**Ten members (debaters):**

1. **Alex Hormozi** — value density. "Where's the reward? Boredom is the only
   enemy. The hook is 20% of the job; the payoff earns the follow." Attacks
   fluff and throat-clearing.
2. **MrBeast** — retention to the second. "Prove the first 3 seconds earn the
   next. Re-hook before attention decays. Escalate, one payoff, abrupt end, no
   dull moments." Maps to your 50-60% first-3-seconds drop-off math.
3. **Brendan Kane** — the hook is a testable device in a 3-second world. "Which
   hook family is this, and where's the second variant? Your first hook is never
   your best. Test, don't guess."
4. **Gary Vaynerchuk** — volume + native + culture. "Does this smell like an ad
   or like the platform? Is it riding what's actually happening this week?"
5. **Donald Miller** — clarity (StoryBrand). "Who's the hero, you or the agent
   watching? One problem, one plan. Two CTAs is zero CTAs." (Also the
   `storybrand` skill.)
6. **Byron Lazine (BAM)** — industry newsjacker. "What's the take, and is it
   fast enough to own the story before anyone else? React to the headline."
   Your native lane.
7. **Eric Simon (The Broke Agent)** — relatability. "Will one agent send this to
   another and say 'this is us'? Where's the recognition, the inside beat?"
8. **Justin Welsh** — sustainable solo system. "Can D.J. actually run this every
   day, alone, on a selfie stick? Is it a repeatable template or a one-off?"
9. **Jon Youshaei** — platform mechanics. "What's the pattern interrupt / visual
   open? What proven format is this remixing? The first frame is a headline."
10. **Chris Do (The Futur)** — the human. "Where's the vulnerable beat that
    earns the follow? Every trigger here is tactic-flavored; give me one honest
    line that costs something." Guards your ~biweekly emotional/identity script.

**Two research witnesses (called on mechanism claims, they don't posture):**

- **Chip & Dan Heath (Made to Stick)** — curiosity + memorability. Called when
  someone says "this creates curiosity" or "this is clear." Rules on: did you
  OPEN the loop before closing it (Aha after Huh), and are you the "tapper"
  assuming the agent hears the tune in your head (Curse of Knowledge)?
- **Jonah Berger (Contagious)** — shareability. Called when someone says "this'll
  get shared." Rules on: is the emotion HIGH-arousal (awe, anger, anxiety,
  excitement, amusement -- "make people mad, not sad," not low-arousal
  contentment/sadness)? Is there Social Currency? And the valuable-virality
  check: if an agent retells this in one sentence, does D.J.'s point survive, or
  does it fall out?

**Who checks whom (self-balancing):** Hormozi/MrBeast (cut, optimize) vs Chris Do
(protect the human beat). GaryVee (ship fast) vs Miller/Heath (clarity). Byron/Eric
(insider) vs Kane (broadly packaged hook). Welsh (sustainable) vs MrBeast (maximal).
Youshaei (format) vs Chris Do/Miller (meaning). Any "it'll go viral" -> Berger
rules. Any "great hook" -> Heath rules.

---

## How to run Pass 4 (in D.J.'s format)

Input: the polished **v3** from Pass 3 (spoken script, 5 captions, hook_family,
pattern_interrupt, AI Music Prompt). Do this silently, then append one block.

1. **Convene 4-7 members with the most at stake** for this script's series/goal
   (a friction NF -> Byron leads, Hormozi + MrBeast + Berger weigh in; an
   emotional/identity script -> Chris Do leads, Heath + Eric weigh in). Each says
   what they'd CHANGE, in character, in one line. Don't run all twelve every time.
2. **Call the witnesses** on any curiosity/clarity claim (Heath) or share/viral
   claim (Berger).
3. **Surface the one real disagreement and resolve it with a decision** tied to
   the script's actual goal (reach vs saves vs follows vs reshares). Don't paper
   over it.
4. **Sharpen the spoken scroll-stop.** Produce **2-3 spoken first-line variants**
   (never on-screen-text-only), each mapped to a hook family from
   [`hook-matrix-cheatsheet.md`](hook-matrix-cheatsheet.md) /
   [`opener-swipe-file.md`](opener-swipe-file.md), labeled by the family and the
   Berger emotion each uses. These are the A/B fuel.
5. **Confirm the pattern interrupt** ([`pattern-interrupt-cheatsheet.md`](pattern-interrupt-cheatsheet.md))
   is the right one-handed selfie-stick move for this open, or suggest a better fit.

## The output: append a `## Council Review` block beneath v3

Keep it tight. Do NOT restate the script. Format:

```markdown
## Council Review

**Scroll-stop variants (spoken, pick one to A/B):**
1. "<variant>"  [hook_family: X | emotion: Y]
2. "<variant>"  [hook_family: X | emotion: Y]
3. "<variant>"  [hook_family: X | emotion: Y]

**Pattern interrupt:** <the confirmed or upgraded visual open>

**Why it should work:**
- Hook mechanism (Heath): <one line>
- Share/save driver (Berger/Hormozi): <one line>
- Retention move (MrBeast): <one line>

**The dissent (your next A/B test):** <the one member still objecting + the
single experiment to run because of it>
```

That block is the whole deliverable of Pass 4. The v3 above it stays in full
repo format; the council layer makes it battle-tested and hands D.J. the next
experiment instead of a shrug.

## Guardrails

- **Embody, don't blend.** If every member sounds agreeable, the round was run
  wrong. Keep the edges.
- **Everything stays in D.J.'s format.** Spoken scroll-stop only, no manual text
  overlays, 5 captions (no X), AI Music Prompt intact, house-rule scrubs already
  applied in Pass 3 are not undone here.
- **Solo-executable only.** Selfie stick, one person, mid-walk. Reject any
  member suggestion that needs a crew or budget (take MrBeast's rigor, not his
  scale).
- **Tie every call to the stated goal.** "More shareable" is meaningless until
  you know the goal was reshares. If the goal was follows, Berger yields to
  Chris Do and Miller.
