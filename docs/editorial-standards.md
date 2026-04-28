# Editorial Standards

This document defines the non-negotiable content rules for every script and social post in this repository. Every writer (human or AI) working on any series in this project must read this doc before drafting new content and must pass the checklist at the bottom before committing anything.

These rules exist because real agents make real business decisions based on content we publish. Accuracy, voice integrity, and scroll-stopping quality are not aesthetic preferences. They are the foundation of the brand and the relationship with every reader.

**How this standard was built.** It merges three sources:
- The **[Coffee Talk system prompt](https://github.com/delfinparis/coffeetalk-episode-registry/blob/main/system-prompt.md)** — the rigor: banned AI-speak, stat integrity, authenticity rules, numbers-in-dialogue.
- The **[KIR POLISH_PROMPT.md](https://github.com/delfinparis/keeping-it-real-content-system/blob/main/content/ai-tips-scripts/POLISH_PROMPT.md)** — the engagement mechanics: curiosity gap, mirror moment, re-hook, problem-agitation-solution, contrast structure, emotional arc, shareable moment, "why now" urgency.
- **D.J. Paris's enforcement rules** — no fabricated stats, no engagement asks, no em-dashes, "D.J. Paris" with periods, and the CTA is always a "here's what you do now" action at the viewer's own life.

Where the three sources conflict, this document owns the resolution. Specifically: the KIR polish prompt has been adapted to strip em-dashes, ban "plausible specific" invented numbers, kill all on-screen-text-only hooks (captions.ai renders audio only), and replace the "ask a specific question" CTA with the stricter "here's what you do now" close.

---

## Rule 0: The WOW Gate

**Before a script gets written, it has to earn the write.** If the script is not going to make a scrolling agent stop and say "wait, what?" — don't write it. Ship fewer, sharper videos. Do not fill a slot.

### The 8 clip-worthy criteria

Every script must satisfy at least one of these eight criteria (inherited from the Keeping It Real content system, sharpened for this repo):

1. **Tactical specificity.** A concrete step the viewer can do today. Not "work hard," not "follow up." "When a buyer asks for a commission cut, here is the exact sentence you say back." The more specific, the better. Names, numbers, exact phrasing, exact tools.

2. **Contrarian take.** Goes against conventional real estate wisdom. Not contrarian for the sake of it. Contrarian because the conventional wisdom is actually costing agents money or time. If the reframe is real, agents will feel the floor shift.

3. **Pattern reveal.** Contrasts what most agents do with what top producers do. "Most agents prospect when they need deals. The top one percent prospect when they don't." The gap has to be real and the consequence has to be real.

4. **Surprising statistic.** A number that makes the viewer stop scrolling because they didn't know it. Must pass the Stat Integrity rules in Rule 1. A stat without a source does not qualify, no matter how punchy it sounds.

5. **Memorable one-liner.** A quotable, copyable phrase that encapsulates a real idea. "Your database is your retirement account." "AI gives you leverage. Experience gives you judgment. One of those takes twenty years." The line has to carry weight on its own, outside the video.

6. **Permission slip.** Releases an agent from guilt or shame. "It is okay to fire a bad client." "You are allowed to hate open houses." Permission slips work because they name the private thing agents already feel but won't say out loud.

7. **Mindset reframe.** Changes how the viewer sees the business. "You are not in the real estate business. You are in the relationship business." Reframes work when they are structurally true, not when they are rhetorically clever.

8. **Earned inside-the-industry observation.** Something D.J. learned from a specific podcast guest, the NAR influencer seat, or a real Kale Realty situation. Must be traceable to an actual moment. "A $50M producer I interviewed last month told me..." is fine if the producer exists and said that thing. It is not fine if the quote is composite or reconstructed.

### The WOW Test

Before writing, answer in one sentence: **"A scrolling agent stops on this video because ___."** If you cannot finish that sentence with one of the eight criteria above, the script does not get written. Pick a different topic.

Write the answer at the top of the script draft as a blockquote so the writer and the reviewer can both audit it:

```markdown
> **WOW: [one sentence -- which of the 8 criteria and why]**
```

This line is not for the viewer. It is a gate. If it is vague, the script will be vague.

### The "Actual Tip" Gate

If the script is a tip (Agent Tip of the Day, The Playbook, reels), it has to deliver one of these three things and the viewer has to be able to point to it after watching:

- **The exact words to say** (a script, a sentence, a subject line, a prompt)
- **The exact action to take** (a specific step, a specific tool, a specific trigger)
- **The exact frame shift** (a reframe that changes a decision the viewer is about to make)

Generic advice is banned. "Build trust" is not a tip. "Send this one text to every past client this Friday: [exact words]" is a tip. If you can't fill in the exact words, exact action, or exact frame, you don't have a tip yet — you have a topic. Keep researching.

---

## Rule 1: Never Fabricate Statistics

**Every number, percentage, ratio, or specific claim in any script must trace to one of these three sources. No exceptions.**

### Acceptable sources

1. **A verifiable external source** — a news article, research report, court filing, Metricool export, LinkedIn analytics export, MLS data, NAR publication, etc. The source must be nameable with a publication year.
2. **D.J. Paris's direct observation** from a specific, citeable interaction — a podcast guest by name, the NAR influencer event, a Kale Realty internal observation. The observation must be tied to a real named person or a real named moment, not a composite.
3. **Math performed on real data** — e.g. "5.7% engagement rate" calculated from actual impressions and engagements in a LinkedIn analytics export. Show the math in the Data Source section.

### Stat integrity — hard rules

These are inherited from the Coffee Talk standard and enforced here with equal weight.

1. **Every stat must name a specific source AND publication year.** "NAR 2024 Profile of Home Buyers and Sellers" is acceptable. "NAR" alone is not. "Studies show" is never acceptable.
2. **Survey stats must note who was surveyed.** Agent-reported data and consumer-reported data carry different weight and tell different stories. Label which one you are using.
3. **Never combine two separate stats into one sentence.** Placing two distinct findings in a single sentence creates a false implication that they came from the same study or that one caused the other.
4. **No "directionally accurate" stats, even flagged.** If a stat cannot be verified with a specific source and year, it does not go in the script. A placeholder is better than an unverifiable number. Use this format in drafts: `[STAT NEEDED: description of what to find -- suggested source and search terms]`. Never ship a script with a placeholder still in it.
5. **Never fabricate a plausible-sounding number.** If a stat feels right but can't be sourced, it gets pulled. Credibility is worth more than a punchy hook built on a made-up figure.
6. **Never reuse a stat across scripts without re-verifying it.** A stat that was right in April may be wrong by July. Re-check the source every time.

### Explicit override: the "plausible specific" rule is banned here

The KIR POLISH_PROMPT ("Hyper-Specific Numbers" principle) instructs writers: *"If you don't have a real stat, use a plausible specific ('spend seven minutes instead of forty-five') rather than a vague one."* **That rule is banned in this repo.** Plausible-but-invented specifics are fabrications by another name. When a real number is not available, use qualitative framing (see below) — not an invented specific.

### What counts as a fabrication

- Inventing a percentage to make a hook sound punchier
- Rounding a real number without documenting the actual number
- Using "studies show" or "data shows" without a specific source
- Borrowing a stat from memory of a similar article without re-verifying
- Generating a number to fit a template structure (the mistake that killed IS-002 v1)
- Attributing a quote to "a guest" or "a top producer" without an actual guest
- Claiming D.J. has observed something specific across X interviews without being able to name at least three of them
- Saying "over 700 interviews" and then generalizing a pattern that actually came from one guest. If the pattern is from one guest, say "one guest told me"
- Using a "plausible specific" fake number in place of a vague one (the banned KIR override)

### Enforcement: the Data Source section

Every script in this repo has a `## Data Source` section. **Every number, percentage, or specific claim in the spoken script must appear in that section with a citation in this format:**

```markdown
- [Claim as written in script]
  - Source: [exact publication name, year]
  - Who was measured: [agents / consumers / listings / etc.]
  - Status: [confirmed / unverified / placeholder]
```

If a claim is in the script but not in the Data Source — or is in the Data Source but marked `unverified` or `placeholder` — it is not ready to ship. Either cite it or strip it before committing.

The Data Source section must be filled in BEFORE the spoken script is drafted, not after. Research first, then write. When research and writing happen in the same pass, the writer reaches for numbers that sound right to fit the sentence rhythm. That is how fabrications happen.

### The qualitative fallback

When a quantitative claim would be stronger but no source exists, reframe qualitatively:

| Don't write | Write instead |
| --- | --- |
| "9 times out of 10" | "More often than not" / "Most of the time" |
| "The top 6%" | "Almost every top producer I've interviewed" |
| "94% of agents" | "Most agents" / "Almost everyone else" |
| "Within 20 minutes" | "Quickly, usually within an hour or two" |
| "Seven minutes instead of forty-five" (plausible specific) | "A fraction of the time it used to take" |
| "Last Tuesday, she answered a 7pm call" | If there's no real source: remove the detail or generalize ("One of my guests told me about an evening call") |

Qualitative framing is always preferable to a false-but-punchy number. A slightly less snappy line is cheap. A fact-checked failure is expensive.

### Known past failures (so we don't repeat them)

- **IS-002 "The 6% Club"** (April 2026). Claude invented the "6% / 94%" split to match the structural template of D.J.'s real "9% Club" LinkedIn post. The 700-interview observation that top producers still answer their phone was real; the specific percentage was not. Script was posted before the fabrication was caught.
- **PB-001 "Lowball Offer"** (April 2026, pre-publish). Claude invented "nine times out of ten, the buyer's agent comes back within twenty minutes." No source. Caught and rewritten to "More often than not, the buyer's agent comes back quickly with context" before filming.

These failures are the reason this document exists. Read them before writing anything new.

---

## Rule 2: The Scroll-Stopper Hook

**The first spoken line of the script is the whole job.** If it does not earn the next three seconds, the rest of the script never gets watched. This rule takes precedence over elegant openings, context-setting, and anything that feels like "warming up."

### Captions.ai reality: the hook must live in the spoken line

D.J. uses captions.ai, which auto-generates on-screen captions from the audio track only. **Separate on-screen text overlays you write into the script do not render in the final video.** That means:

- Any `[ON-SCREEN: "..."]` cue is decorative, not real. It will not appear on screen.
- The entire pattern interrupt must be carried by the first sentence D.J. speaks aloud.
- Do not rely on an on-screen title card to do work the spoken hook isn't doing.

This is an explicit override of the KIR POLISH_PROMPT's "writing for muted viewers" principle, which assumes manually burned-in on-screen text. In this repo, captions.ai auto-captions the audio, so the hook earns attention through the spoken line or not at all.

### What the first line must do

The first spoken line must do one of these four things. No other opens qualify:

1. **State a surprising specific.** A real number, a real name, a real moment. "I watched a $50M producer miss a listing because of one text." Specific beats abstract every time.
2. **Name the viewer's private problem out loud.** The thing they feel but won't say. "You are losing listings to agents who are worse than you are." This only works if the statement is actually true for the target avatar.
3. **Make a contrarian claim the viewer expects you not to make.** "I teach AI to agents. I am not bullish on AI replacing this job." The pattern interrupt is the tension between the credential and the claim.
4. **Drop the viewer mid-story.** No setup. "She answered a 7pm call on a Tuesday. Two weeks later she had the listing." The story has to be real and the rest of the script has to unpack it.

### The Curiosity Gap: open a loop the viewer must close

The hook's job isn't just to stop the scroll. It is to create a tension that can only be resolved by watching to the end. The strongest hooks do both — they stop the scroll AND promise a specific payoff the viewer needs to see delivered.

- **Weak:** "Your CRM drip campaign is costing you business."
- **Strong (open loop):** "Your CRM drip campaign is costing you business. And I'm going to show you the exact text that fixes it in the next thirty seconds."

The second version stops the scroll AND makes the viewer need to see the text. Build open loops into hooks wherever the payoff is real and specific.

### What the first line cannot do

- It cannot start with "So," "Alright," "Here's the thing," "Hey guys," or any other throat-clear.
- It cannot be a rhetorical question the viewer doesn't care about yet. "Have you ever wondered..." is dead.
- It cannot be context-setting that delays the hook. If a credential matters, the hook weaponizes it ("I teach AI to agents, and...") rather than introducing it ("Hi, I'm D.J., and I teach AI to agents. Today we are going to talk about...").
- It cannot live only in an on-screen text overlay. See above — captions.ai only renders audio.

### The 3-second test

Read the first spoken line aloud. In under three seconds, does it make a stranger want to hear the next sentence? If no, rewrite it. The test is not "is it clever." The test is "does it earn the next breath."

### The 15-second re-hook

Viewer retention data shows a second major drop-off point at 15 to 20 seconds. Every script over 20 seconds must place a re-engagement line at roughly the 15-second mark — a phrase that re-establishes stakes, deepens curiosity, or teases what's coming. This is inherited from the KIR POLISH_PROMPT.

**Re-hook phrases that work:**

- "And here's the part most agents completely miss..."
- "But here's where it gets worse."
- "This is the step everyone skips, and it's the one that matters most."
- "What I'm about to show you takes four minutes. It should take most agents four months to figure out on their own."

The re-hook doesn't need to be dramatic. It just needs to remind the viewer there is a reason to stay.

### Hook patterns D.J. uses well (copy these, don't copy *from* these)

- **Credential-plus-contradiction:** "I teach real estate agents how to use AI. And after 700 podcast interviews, I can tell you the one thing AI is never going to fix."
- **Specific-number lead:** "403 percent more inquiries. From one thing almost no agent does."
- **Named-guest hook:** "A $40 million producer just told me she's terrible at prospecting. She still answers her phone at 7pm."
- **Cost-of-inaction lead:** "Your top agent is about to quit. Not because of splits."

These are patterns, not templates. Do not mass-produce them — they lose force when they repeat across consecutive posts.

---

## Rule 3: Problem-Agitation-Solution Arc

After the hook, the script must move the viewer through a specific structural arc inherited from the KIR POLISH_PROMPT. Skipping any beat kills retention.

### The arc

1. **Hook** — see Rule 2. Stops the scroll, opens a loop.
2. **Problem (the Mirror Moment).** Name the specific mistake or pain the viewer is living. Use second person. Use time and place. Not "most agents struggle with follow-up" but "It's Tuesday morning. You have fourteen leads in your CRM you haven't touched in three weeks. You open the compose window. You stare at it. You close it. You tell yourself you'll do it tomorrow." The viewer who has lived that Tuesday morning will not scroll.
3. **Agitation.** Name what the problem is costing them. Not the abstract cost — the specific cost. The referral that never came. The listing that went to someone worse. The client that Googled them and picked the other agent. The viewer needs to feel the weight of the problem before the solution will feel valuable.
4. **The fix.** Deliver the exact words, exact action, or exact frame shift (see Rule 0's "Actual Tip" gate). This is what they stayed for. Reward them with specificity, not generality.
5. **Reframe.** Why this matters to their business or their life. This is the line that turns a tactic into a shift in how they see their work.
6. **"Here's what you do now" close.** See Rule 4.

### Contrast structure: the single highest-performing pattern

"Most agents do X. Top producers do Y." This pattern works because it creates an immediate in-group / out-group dynamic. The viewer wants to belong to the top group. Use it at least once per script — in the hook, the problem, or the reframe.

Examples:

- "Most agents use AI to write content. Top producers use it to rehearse conversations they are afraid to have."
- "Most agents check email first thing every morning. The top 10 percent haven't opened their inbox before 10am in years."
- "Most agents know what to do. The agents who actually do it built a system so they don't have to rely on knowing."

### The emotional arc

Map the emotional state of the viewer at each beat. If the script does not move through this arc, rewrite until it does.

| Beat | Target emotion |
| --- | --- |
| Hook | *Startled / curious* — "wait, what?" |
| Problem / Mirror Moment | *Seen / validated* — "that's exactly me" |
| Agitation | *Uncomfortable* — "I need to fix this" |
| Fix | *Hopeful / relieved* — "I can actually do this" |
| Reframe | *Motivated* — "this matters more than I realized" |
| Close | *Committed* — "I'm doing this right now" |

### The shareable moment

The most shared short-form content contains one moment so good the viewer immediately thinks "someone I know needs to see this." Usually one of:

- A stat that is shocking or counterintuitive (and sourced — see Rule 1)
- A contrast that perfectly captures a frustration they share with colleagues
- A specific tactic so concrete they feel guilty not forwarding it
- A permission slip that validates something they felt but never heard out loud

Every script should have one. Identify it explicitly in the script metadata. If it is buried in the middle of the script, move it forward.

### "Why now" urgency

Every script should contain a reason why this tip matters right now, not in general. The AI landscape is changing fast. The NAR settlement changed the rules. The market is shifting. Agents who adopt this now have a head start on everyone who waits.

This doesn't have to be heavy-handed. One sentence near the reframe: "And with the market where it is right now, this is the kind of edge that compounds."

---

## Rule 4: The "Here's What You Do Now" Close — No Engagement Asks

**The close is always an action at the viewer's own life.** Not at the channel. Not a question. Not a plea for engagement. The tip earns the close.

### The rule

Every script ends with one variant of *"Here's what you do now"* — a specific, immediate action the viewer takes in their own business or day, tied directly to the tip they just heard. The action happens offscreen, in their life. They don't owe the channel anything back.

Examples of the "Here's what you do now" close:

- *"Here's what you do now. Open your texts. Pick one past client. Send this exact message: [exact words]. Before you do anything else today."*
- *"Here's what you do now. Pull up your top producer's LinkedIn, and look at the three posts that have the most comments. Copy the structure, not the content. Post one by Friday."*
- *"Here's what you do now. Tomorrow morning, pick up one call you'd normally skip. See what happens."*

The close is not optional. Every script has to land here. The specific action has to be executable in the next hour, not "someday when I have time."

### Banned closes

| Phrase | Why it's banned |
| --- | --- |
| "Follow me for more" | Positions as still-needing-followers |
| "Subscribe for more" | Same problem |
| "Save this" / "Bookmark this" | Telling people what to do *for you*, not earning it |
| "Tag a broker" / "Tag a friend" | Engagement farming |
| "Reply and tell me what happened" | Fishing for comments |
| "Drop it below" | Tabloid energy |
| "What's your take?" | Weak rhetorical filler |
| "Let me know in the comments" | Same as above |
| "Share this with someone who needs to hear it" | Share-begging |
| "Hit the follow" / "Hit the like" | Self-explanatory |

### Explicit override: KIR's "specific question CTA" is not adopted

The KIR POLISH_PROMPT says the CTA should be *"a direct question that makes someone want to reply."* **This repo does not adopt that rule.** Questions at the end of scripts drift toward engagement-asking and soften the close. Use the "Here's what you do now" action instead.

### Why

Every engagement ask signals "I am at the stage where I need you to do something for me." The brand D.J. is building — with a senior Chicago real estate audience, a direct NAR relationship, and 700 podcast episodes worth of credibility — is positioned as the opposite. He is the person you should already be following because of who he is and what he has access to. Asking for the follow undercuts that position every time.

Reference creators to model: Steven Bartlett (Diary of a CEO), Ryan Serhant, Jefferson Fisher. None of them end their best content with "follow for more." Their content earns engagement through sharpness.

### Podcast mentions are different

You can say *"I cover shifts like this weekly on the Keeping It Real Podcast"* or *"More from inside the industry on the Keeping It Real Podcast."* These are informational — they tell the reader where else to find D.J. — without asking them to do anything. That is fine.

The test: does the phrase DIRECT the reader to take an action for your benefit, or INFORM them that more content exists? Informational is fine. Directive is banned.

---

## Rule 5: Voice, Dialogue, and Formatting

These rules apply to every spoken line and every caption. They are inherited from the Coffee Talk editorial standard and the KIR POLISH_PROMPT, merged.

### Banned AI-speak — merged list

Never use these words or phrases in any script, caption, or post. They signal generated text and kill the voice on any platform.

**From the Coffee Talk list:**

> dive into, delve, unleash, seamlessly, robust, cutting-edge, empower, pivotal, transformative, unlock, it's worth noting, furthermore, notably, at the end of the day, in today's world, landscape, navigate, leverage *(except as a literal financial term)*, synergy, holistic, impactful, take it to the next level, best practices, circle back, bandwidth, move the needle, double down, actionable insights *(say "action steps" instead)*, unpack *(except as slang in a natural spoken context)*, elevate

**Added from the KIR POLISH_PROMPT:**

> game-changer, level up, supercharge, revolutionize

**Added from D.J.'s direct feedback and observed AI tells:**

> really, basically, kind of, you know, like, right?, hey guys, today I want to talk about, in this video, let me tell you about

If you catch yourself about to use any of these, stop and rewrite the line from scratch. If the sentence falls apart when you remove the AI-speak word, the sentence had no idea in it — that is the real signal.

### Punctuation

- **Never use em dashes (—) or en dashes (–).** Use two hyphens (`--`), a period, or a comma, or restructure the sentence. Em dashes are the single most widely recognized AI-writing tell. Zero exceptions in scripts, captions, or stage directions. This overrides the KIR POLISH_PROMPT's "dashes for natural pauses and breaths" guidance.
- **No ellipses (...) for stylistic effect.** If a thought trails off, write the trailing off in words.
- **No ALL CAPS for emphasis.** If a word needs emphasis, restructure the sentence so the emphasis falls naturally when spoken aloud.

### Authenticity rules

- **Contractions required in all spoken lines.** "Do not" becomes "don't." "They are" becomes "they're." "It is" becomes "it's." No exceptions. Uncontracted speech sounds written, not spoken.
- **No passive voice in spoken lines.** Rewrite every passive construction. "Offers get submitted without a call" becomes "agents submit offers without ever calling." The agent, or the buyer, or the seller, is always the subject.
- **No self-answered rhetorical questions.** Do not ask a question and answer it yourself in the same breath. If you pose a rhetorical question, let it sit for a beat before answering, or cut the question and state the answer directly.
- **Always "D.J. Paris"** with periods, never "DJ Paris."
- **No emojis in brand content** unless explicitly requested.

### Numbers in dialogue

- **Maximum two numbers per spoken line.** Viewers cannot track more than two figures at once in real time. If a line contains three or more numbers, split it across two lines.
- **Numbers under 10 must be spelled out in dialogue.** "Three offers," not "3 offers." "Five minutes," not "5 minutes." This reads more naturally when spoken aloud and transcribes cleaner in captions.ai.
- **Percentages expressed as "X in Y" wherever possible.** "One in four" lands harder than "25 percent." "Nine out of ten" hits differently than "90 percent." Use the ratio form unless the percentage itself is the story.

### Credibility signals — wear the authority lightly

D.J. has interviewed 700+ top-producing agents over 12+ years and sits as 1 of 12 in NAR's 2026 influencer program. This is enormous authority. It must be deployed naturally, not as a credential dump. Weave in at most one credibility signal per script, conversationally.

- **Natural:** "In twelve years of talking to top producers, I've never met one who didn't have this system."
- **Natural:** "I've interviewed over 700 agents on the Keeping It Real Podcast. This came up in almost every conversation about lead gen."
- **Forced (avoid):** "As the host of a top real estate podcast with 3.2 million downloads..."

### Pacing — write for delivery, not reading

- **Short punchy sentences for emphasis.** Like this.
- **Longer sentences for explanation, where the viewer needs to process the idea and follow the logic through to its conclusion.**
- **Never end a section with a weak word.** The last word of every sentence carries disproportionate weight on camera.
- **Read every line aloud before finalizing.** If it makes you stumble, rewrite it.
- **No sentences longer than 25 words.** Break them up.

### Paragraph and hook formatting for captions

- **Short paragraphs** (1 to 3 sentences each) in any long-form caption. LinkedIn and Facebook both favor short paragraph blocks.
- **Hook in the first 2 to 3 lines** of any caption. Assume mobile cutoff at roughly 150 to 210 characters depending on platform.

---

## Rule 6: Protected Voice Signatures

Some phrases, once established as part of the brand, become protected voice signatures. They should not be rewritten casually across content generations. If a signature phrase needs to change, the change should be made deliberately, documented, and propagated consistently across every asset.

### Currently protected signatures

**"I've never practiced real estate. But I've interviewed 700 people who have."**

- **Meaning.** D.J. holds a real estate license but has never represented a client or worked a transaction on behalf of a buyer or seller. His authority comes from hosting the Keeping It Real Podcast (700+ episodes) and being 1 of 12 nationally in NAR's 2026 influencer program.
- **Scope.** Every speaker asset, every Inside the Industry script that references D.J.'s credentials, every bio, every one-sheet. The phrase is the pattern interrupt that preempts the "why should we listen to a non-agent?" question and turns it into the differentiator.
- **Variants allowed.** "I don't practice real estate" (in prose flow), "Licensed but never practiced" (in very short spaces like Instagram bios), "I hold a real estate license. I've never used it to represent a client." (in longer formal writing).
- **Variants banned.** "I've never sold a house" (inaccurate -- D.J. has sold his own home as a homeowner). "I'm not an agent" (inaccurate -- he is a licensed agent, just non-practicing). "I'm not a broker" (inaccurate -- he is the VP of Business Development at a brokerage).
- Full context in `docs/speaker-assets.md`. Read that document before rewriting any reference to D.J.'s practitioner status.

### The test for adding a new protected signature

A phrase becomes protected when:

1. It has appeared in 3+ published pieces of content without being rewritten.
2. It has become the single most distinctive thing a reader remembers about D.J.'s positioning.
3. Replacing it with a synonym would weaken the brand meaningfully.

When those three conditions are met, document the phrase in this section along with its meaning, scope, allowed variants, and banned variants. Then enforce it on every new piece of content.

---

## Rule 7: Length and Pacing

**Target 30 to 60 seconds. Hard cap 90 seconds. Every second past 45 must earn its place.** This rule is grounded in the reels-scorecard review of D.J.'s first five reels, which found that videos over 70 seconds with a single static shot tanked retention and algorithmic reach, and that the 30-45 second range was the retention sweet spot.

### Word-count targets

At a natural delivery pace of roughly 130-150 spoken words per minute:

- **30 seconds** ≈ 65-75 spoken words
- **45 seconds** ≈ 100-110 spoken words
- **60 seconds** ≈ 130-150 spoken words
- **90 seconds** ≈ 195-225 spoken words (the hard cap, rarely justified)

### The length discipline

- A script longer than 45 seconds must have a documented reason — in the script metadata — why it earned the extra length. "The topic is complex" is not a reason. "This is a four-beat story and cutting a beat kills the payoff" is a reason.
- A script longer than 60 seconds must have a 15-second re-hook in the spoken line to catch the drift point.
- A script longer than 75 seconds should probably be two scripts. Before committing, ask: can this be split into two videos with a shared through-line? Usually yes, and usually better.
- If a tip can be told in 30 seconds and the draft is 60 seconds, the draft is wrong. Cut it.

### No padding

Every sentence either advances the arc or gets cut. Specifically, cut:

- Repeated phrasing that restates the same idea for "rhythm"
- Context the viewer does not need in order to act on the tip
- Credentials that the hook already carries
- Second, third, or fourth examples when one example did the work
- Any sentence that does not move the viewer through the emotional arc in Rule 3

The reels scorecard observation stands: *"If YOU get bored watching your own video at 2x speed, your audience definitely will."*

---

## Rule 8: Writing Discipline (Anti-AI-Style Prose)

This rule covers the surface-level texture of every line we ship — the stuff that decides whether prose reads like a person who knows what they're doing or like default chatbot output someone pasted in. Rules 1 through 7 cover content rigor, voice, and structure. This rule covers everything you cannot cover with a banned-words list.

### 8.1 Don't optimize to "sound human"

AI text detectors are probabilistic, not proof. Don't manufacture mistakes, slang, fake hedges, or staged messiness to dodge an algorithm. Don't break grammar on purpose. Don't insert random sentence-length wobble. The goal is prose that fits the medium, the audience, and the reader's job. If you do that well, the prose reads as human as a side effect.

The recurring problem in AI-written copy is regularity and mismatch, not any single feature. Use em dashes where they belong (in this repo: never -- see Rule 5). Use commas, colons, semicolons where they belong. Stop reaching for the same connective in the same role across every paragraph.

### 8.2 Specificity must be earned

Every substantial paragraph in a long-form caption, listing, doc, or essay block needs at least one concrete anchor.

**Counts as concrete:**

- A proper noun the reader could look up
- A specific number that isn't only a date or version
- A direct quote
- A named decision, moment, or thread
- A checkable detail
- A user-facing or observed consequence

**Does not count:**

- "many," "various," "several," "a lot of"
- "in ways that mattered," "broad implications," "meaningful changes"
- "the standard X arc," "as is often the case," "the usual pattern"
- vague intensifiers in place of claims: "essentially," "fundamentally," "ultimately"
- milestone names, dates, titles, or feature labels standing alone with no consequence attached

**Specificity theater is banned.** Don't add decorative factuality (invented milestone names, suspiciously exact claims, synthetic quotes) to avoid sounding generic. Fewer verified facts beat many guessed ones every time. This extends Rule 1 from numbers to all decorative specificity.

### 8.3 High-fragility facts: quotes, metrics, future claims, causality

These four categories need source support for the **exact claim**, not just a nearby topic. Treat them with extra discipline.

- **Direct quotes and close paraphrases.** Words attributed to a specific person must be in a transcript or document. "Karina said something like X" without a transcript is a fabrication risk.
- **Public metrics.** "5.7% engagement rate" needs a source that reports 5.7%, not 5% or "around six percent."
- **Future claims.** "Releases in April" needs the published roadmap. If the source is old or tentative, say "planned for" or "scheduled for" or cut the date.
- **Causal claims.** "Caused, drove, proved, enabled, prevented, explained, led directly to" all need source support for the relationship, not just the two facts on either side. If the evidence only supports sequence or correlation, weaken to "coincided with," "appeared alongside," "was followed by," or cut the relationship.

### 8.4 Don't launder analysis through vague authority

Banned without a named source: *experts say, observers note, research suggests, critics argue, many believe.* If you can't name the source and stay within what it actually proves, cut the claim or attribute it. This extends the Rule 1 ban on "studies show" to its full vague-authority family.

### 8.5 Don't narrate hidden mechanisms as fact

Internal logic, unseen motives, back-end behavior, what an algorithm or organization is "really" doing — if the reader couldn't observe it and you can't verify it, don't write it as fact. Replace with the observable consequence.

| Don't write | Write instead |
| --- | --- |
| The internal logic finally understood what mattered | After the change, obviously irrelevant outcomes stopped showing up |
| NAR is positioning itself for | NAR has publicly said... / NAR's recent moves include |
| The algorithm decided to surface | After the update, posts with X started appearing higher in feed |

### 8.6 Plain-text formatting artifacts

In chat, comments, captions, casual Markdown, and any prose typed straight into a CMS or social composer, prefer **straight ASCII quotes and apostrophes** by default. Smart quotes (curly), curly apostrophes, and single-character ellipses (`…`) read as pasted-from-chatbot signals in casual prose now. They are fine in typeset publication-facing output. If text arrived by copy-paste from a doc or LLM tool, normalize it before posting. This applies to every social caption, every email, every Eventbrite listing, every CMS-pasted block.

### 8.7 Regularity is the real tell

LLM writing usually fails not because of any single phrase but because the same move repeats until it dominates. Watch for:

- Parallel three-part cadence by reflex inside sentences (*clearer, faster, cheaper*)
- Concession-plus-positive rhythm (*not X, but Y* / *may sound X, but Y*)
- Paragraph-closing type definitions (*the kind of X where Y*)
- Identical paragraph arcs (one neat claim sentence at the top, orderly elaboration below, every paragraph)
- The same punctuation move every paragraph (e.g. every paragraph builds to a colon)
- The same controlling metaphor or contrast returning until it feels too tidy
- Stacked mini-sentences for impact in every section
- Multiple sentences doing list work even when nothing is bulleted

**The test:** Name the single most repeated visible pattern in your draft. If the same move appears three or more times, or dominates two consecutive paragraphs, rewrite at least one occurrence. Three-item parallel lists count even if the sentence isn't a list.

The fix is not random variation. It is breaking the repeated pattern where it starts to dominate.

### 8.8 Catalog prose vs. argument prose

A paragraph mostly composed of names, milestones, categories, feature nouns, or labels is **catalog prose**. A piece where each paragraph maps cleanly to a single bucket — *background, mechanism, impact, response, ending* — is **system-tour prose**. Both feel templated.

For long-form (LinkedIn captions over 4 paragraphs, Eventbrite bodies, retrospectives, planning docs), don't give one paragraph to each milestone or one paragraph to each topic bucket unless that mapping is the actual point. Pick one constraint, one shift, one consequence — and trace it across paragraphs that depend on each other instead of sitting like labeled boxes.

### 8.9 Cohere through reference. Don't perform.

- Use pronouns and continued reference when the reader can track them. Don't restate the full frame in every paragraph.
- Treat *Furthermore, Moreover, Additionally, Importantly, Notably* as transitions you have to justify, not default sentence starters.
- No keynote cadence. No mission-statement phrasing. No applause-line endings. No service-desk tone (*Great question, Absolutely, I hope this helps, Feel free to reach out*).
- Start where the answer starts. Stop where the answer stops.

### 8.10 Calibrate stance to genre

- If the piece is opinion, review, or commentary — Inside the Industry IA/IS, Playbook reframes, podcast take posts — let the writer appear. State a view in one sentence.
- If the piece is neutral summary or documentation — a Data Source section, a docs page, a meeting note — don't inject first person or attitude to feel human.
- Don't sand opinion-genre material down to evenly polite neutrality.
- Don't manufacture stance where the genre doesn't call for it.

### 8.11 Expanded formula-phrase watchlist

Not bans -- places to check whether the writing slipped into formula. Most of these are not in the Rule 5 banned-AI-speak list because they're sentence patterns rather than single words.

Sentence-level moves to scrutinize:

- *It's important to note that, It's worth noting that, When it comes to, In conclusion*
- *in today's fast-paced world, ever-evolving landscape, at the end of the day*
- *dive deep into, embark on a journey, navigate (used as a vague metaphor)*
- *It's not X, it's Y / Not because X, but because Y / What matters is... / The real issue is... / This is not just X, it is Y*
- *is a testament to, serves as / stands as (when "is" or "has" would be clearer)*
- *plays a key role / plays a pivotal role*
- *reflects broader, symbolizes, showcases, highlights, underscores* (when attached to generic significance rather than evidence)
- Persuasive three-part cadence used by reflex
- Paragraph-closing *the kind of X where Y*
- Fake-human hedge chains (*I think... maybe... sort of*) when the uncertainty isn't real
- Forced register lowering or inserted slang
- Decorative emoji and checkmark bullets in prose contexts

Note: Rule 3's "Most agents do X. Top producers do Y." contrast structure is intentionally a permitted form of *It's not X, it's Y* in this repo. The rule above bans the formula as a *reflexive* sentence move, not the deliberate contrast pattern that earns its place.

### 8.12 Revision pass for any piece over roughly 150 words

Run these checks in order before committing. They are tripwires, not goals to optimize for. Use them to catch genericity, false specificity, and modular structure -- not to manufacture variation for its own sake.

1. **Register fit.** Format and tone match the medium and the request.
2. **Concrete-anchor audit.** Every substantial paragraph has at least one concrete anchor (8.2). At least one paragraph in any analysis or commentary is built around a single observed example, not category summary.
3. **Fact discipline.** Pick the three most fragile factual claims (8.3). If you can't vouch for them, attribute them, soften them, or cut them.
4. **Source-fit check.** Every cited source actually supports the exact claim, not a nearby topic.
5. **Regularity tripwire.** Name the single most repeated visible pattern. If it shows up 3+ times or dominates two consecutive paragraphs, rewrite one occurrence.
6. **Repeated-frame check.** If a central metaphor or contrast appears throughout, decide whether it's a useful motif or a too-neat scaffold. Vary or cut where it's just decoration.
7. **Stance and voice.** If the genre expects a visible writer, did you state the view? If the genre expects neutrality, did you keep it neutral?
8. **Developed thought.** For pieces over four paragraphs, identify one place where the prose pauses, doubles back, or notices a concrete detail off the main line. If the piece runs in a perfectly straight line from claim to conclusion, find one moment to break that.
9. **Shape and spine.** State the organizing principle in five words or fewer and the controlling claim in one sentence. If the shape is just *starting state → changes → verdict* or each paragraph is a single labeled bucket, restructure (8.8).
10. **Over-correction.** Did you add fake-human moves -- typos, slang, forced asides, random fragments, artificial sentence-length wobble -- just to break a pattern?

These checks are for revision, not visible self-reporting. Do not output the audit unless asked. The audit is for the writer, not the reader.

---

## Pre-Commit Checklist

Every new script must pass all of these before committing. If any one is "no," the script is not ready.

### The WOW Gate

- [ ] The `> **WOW: ...**` line at the top of the draft names which of the 8 clip-worthy criteria the script hits and why.
- [ ] The "actual tip" gate is satisfied: exact words, exact action, or exact frame shift the viewer can point to.
- [ ] A scrolling agent can finish the sentence "I stopped on this because ___" in concrete terms after watching.
- [ ] The script identifies its shareable moment explicitly in metadata, and that moment is in the first 30 seconds.

### Stat integrity

- [ ] Every number, percentage, or specific claim in the spoken script appears in the Data Source section with source name, publication year, who was measured, and status.
- [ ] Zero fabricated stats, percentages, or quantitative claims.
- [ ] Zero "plausible specific" invented numbers (e.g. "seven minutes instead of forty-five" without a source).
- [ ] Zero `[STAT NEEDED: ...]` placeholders remaining in the script.
- [ ] Zero stats that combine two separate findings in one sentence.
- [ ] At least one credibility anchor documented in Data Source (specific podcast guest, real observation, verified source).

### Hook and structure

- [ ] First spoken line passes the 3-second test — it earns the next breath without throat-clearing.
- [ ] First spoken line is one of the four allowed hook types in Rule 2.
- [ ] The hook opens a curiosity loop that the rest of the script must close.
- [ ] No script relies on on-screen-text-only hooks. The pattern interrupt lives in the spoken audio (captions.ai constraint).
- [ ] The script moves through Hook → Mirror Moment → Agitation → Fix → Reframe → Close.
- [ ] The contrast structure ("Most agents do X. Top producers do Y.") appears at least once, where natural.
- [ ] The emotional arc (curious → seen → uncomfortable → hopeful → motivated → committed) is traceable beat by beat.
- [ ] If the script is over 20 seconds, a 15-second re-hook is present.
- [ ] At least one "why now" urgency line is present near the reframe.

### Voice and formatting

- [ ] Zero em dashes or en dashes anywhere, including captions and stage directions.
- [ ] Zero ellipses used for effect in dialogue.
- [ ] Zero ALL CAPS emphasis in dialogue.
- [ ] Zero banned AI-speak words from the merged list (dive into, delve, seamlessly, robust, pivotal, transformative, unlock, empower, it's worth noting, game-changer, level up, supercharge, revolutionize, really, basically, kind of, you know, etc.).
- [ ] All spoken lines use contractions.
- [ ] No passive voice in spoken lines.
- [ ] No self-answered rhetorical questions.
- [ ] "D.J. Paris" spelled with periods everywhere it appears.
- [ ] No spoken line contains more than two numbers.
- [ ] Numbers under 10 spelled out in spoken lines.
- [ ] Percentages expressed as "X in Y" ratios wherever possible.
- [ ] No sentence longer than 25 spoken words.
- [ ] At most one credibility signal; worn lightly.

### Close

- [ ] The close is a "Here's what you do now" action at the viewer's own life — not a question, not an engagement ask.
- [ ] The action is executable in the next hour, not "someday."
- [ ] Zero engagement asks across spoken script AND all platform captions (LinkedIn, Instagram, Facebook, TikTok, YouTube Shorts, X).
- [ ] Zero "follow me," "subscribe," "save this," "tag a broker," "let me know in the comments," or "what's your take" phrases.

### Length

- [ ] Script is 90 seconds or less (hard cap).
- [ ] If over 45 seconds, the script metadata documents why the extra length is earned.
- [ ] If over 60 seconds, the script has a 15-second re-hook.
- [ ] If over 75 seconds, the writer has considered splitting into two scripts and documented why not.
- [ ] No padding: every sentence advances the arc or is cut.

### Writing discipline (Rule 8)

- [ ] Every substantial paragraph in any long-form caption has at least one concrete anchor.
- [ ] Zero vague authority ("experts say," "research suggests," "observers note") without a named source.
- [ ] Zero hidden-mechanism claims (internal logic, unseen motives, what a system is "really" doing) narrated as fact.
- [ ] Causal language ("caused, drove, proved, enabled, led to") only where the source supports the relationship -- not just sequence or correlation.
- [ ] Quotes are exact, sourced, and verifiable. Future-tense claims have a published roadmap or are softened to "planned for."
- [ ] Plain-text contexts (captions, emails, CMS pastes) use straight ASCII quotes and apostrophes -- no smart quotes or single-char ellipses copied from a chatbot.
- [ ] Regularity tripwire: the most repeated visible pattern doesn't show up 3+ times or dominate two consecutive paragraphs.
- [ ] No catalog or system-tour prose: paragraphs depend on each other instead of mapping one-to-one with labeled buckets.
- [ ] Stance matches genre: opinion pieces have a stated view; neutral pieces aren't injected with first person.
- [ ] No fake-human moves: no manufactured typos, slang, forced asides, or artificial sentence-length wobble.

### Final read

- [ ] Read the full spoken script aloud. If any line sounds written instead of spoken, rewrite it.
- [ ] Watch the script at 2x mental speed. If it drags, cut.
- [ ] The script could be posted and fact-checked by a careful reader without any claim failing.

---

## Scope

This document applies to every series in the repository:

- **AI Agent Minute** (Pillar 1)
- **Agent Tip of the Day** (Pillar 2)
- **The Playbook** (Pillar 3)
- **Inside the Industry** (Pillar 4) — all sub-types (IA, IS, NF)
- **Reels and bonus content**

And every platform surface within each script:

- Spoken script
- LinkedIn caption
- Instagram caption
- Facebook caption
- TikTok caption
- YouTube Shorts title and description
- X / Twitter post

No exceptions. No carve-outs.

---

## When in Doubt

If you're not sure whether a claim is supported, whether a phrase crosses the line into engagement-asking, or whether a hook really earns the next breath — default to the more conservative choice. Cut the number. Cut the ask. Rewrite the hook. The content is always stronger when every line has earned its place.

When a reader or a future version of yourself reads this repo in six months, they should be able to trace every number to a source, every close to a "here's what you do now" action, and every hook to a reason a stranger would stop scrolling. If they can't, we failed.
