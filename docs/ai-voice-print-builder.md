# The Voice Print: How to Train AI to Write Like You

*The companion to the "Stop AI From Sounding Like AI" prompt. Yesterday's prompt strips out the AI tells. This one adds back your actual voice — so the AI doesn't just sound generic-human, it sounds like YOU.*

---

## What this is

A six-phase methodology for building a "voice print" — a detailed instruction document that captures how YOU write — and deploying it across every AI tool you use.

By the end, you'll have:

- A single voice profile document, roughly 800–1,500 words
- It loads into ChatGPT custom instructions, Claude projects, Gemini Gems, or any AI tool that accepts system instructions
- Every piece of content the AI writes for you afterward matches your voice, not generic AI voice
- You can update it as your writing evolves

This guide is synthesized from the strongest publicly-available methodologies: Tiago Forte's AI Style Guide framework, Dean Seddon's voice-cloning approach, Zapier's training playbook, and several open-source prompt collections on GitHub. The recommended prompts and templates below are battle-tested versions.

---

## How long will this take?

- **Phase 1 (Gathering samples):** 30–60 minutes if you have to dig through old writing. 10 minutes if your writing is already organized.
- **Phase 2 (First-pass analysis):** 20 minutes.
- **Phase 3 (Refinement):** 30–60 minutes, possibly across two sittings.
- **Phase 4 (Build the voice document):** 20 minutes.
- **Phase 5 (Deploy):** 10 minutes.
- **Total:** Plan for 2–3 hours, ideally in one sitting with a fresh AI conversation.

You'll do this once. Then maintain it lightly over time.

---

## Phase 1: Gather your writing samples

### How many samples?

The most-cited threshold is **3 to 5 samples minimum** for basic pattern detection. The strong recommendation across the better sources is **8 to 10 samples totaling at least 5,000 words** (Dean Seddon recommends 20,000 words if you have it).

More is better up to a point. Beyond 10 samples you're getting diminishing returns and pushing context window limits.

### What kind of samples?

You want your **natural, un-edited-by-AI voice.** That means:

- Personal emails (especially longer ones to colleagues or friends)
- Long-form social posts (LinkedIn, X threads, Facebook posts that ran more than 150 words)
- Newsletter pieces
- Blog posts
- Internal memos or thought pieces
- Talking-points outlines you wrote
- DMs and Slack messages of substance (not "ok" or "thanks")
- Spoken-script transcripts of you talking, if you have them

You want to **avoid:**

- Anything an editor heavily rewrote
- Anything you wrote on a corporate template
- Anything you wrote in a voice that isn't yours (ghost-writing for someone else)
- Anything an AI already touched

### Diversity matters

Pull samples from at least three different contexts. If you only feed the AI LinkedIn posts, it learns LinkedIn-voice, not YOUR voice. Mix it up: one email, one social post, one long-form, one talking-points doc, one off-the-cuff write-up. The diversity is what lets the AI separate your CORE patterns from format-specific habits.

### Quality check before you proceed

For each sample, ask yourself: *Would I be embarrassed if someone forwarded this and said "this is exactly how Sarah writes"?* If yes, it's a good sample. If no — if it's too generic or too formal — replace it.

### Save them in one place

Drop all samples into a single text file or Google Doc. Number them. Label each with context (e.g., "Sample 1 — LinkedIn post about Q4 results, written July 2024"). The labels help the AI understand context as it analyzes.

---

## Phase 2: First-pass voice analysis

Open a fresh AI chat. Paste this analysis prompt FIRST, before any samples:

### THE ANALYSIS PROMPT

```
You are an expert in linguistics, prompt engineering, and writing-style analysis. I'm going to provide you with several samples of my writing. Your job is to analyze them deeply and identify the patterns that make my voice distinct.

For each sample I provide, identify patterns in these seven dimensions:

1. VOICE AND TONE
- Formality level (casual / professional / formal)
- Authority register (peer / mentor / journalist / coach / contrarian)
- Emotional range (where do I get warm, where do I get sharp, where do I show humor)
- Stance (confident / hedging / collaborative / direct)

2. VOCABULARY
- Signature words I use repeatedly
- Words I notably AVOID where most people would use them
- Industry-specific terminology and how I deploy it
- Slang, idioms, regionalisms, or distinctive phrasings

3. SENTENCE STRUCTURE
- Typical sentence length
- Range (do I mix short and long, or are they uniform?)
- Sentence-starter patterns (do I lead with subject, with phrases, with conjunctions?)
- Use of intentional fragments
- Active versus passive voice tendencies

4. RHYTHM AND PACING
- Where I use short staccato sentences
- Where I use longer flowing sentences
- How I transition between ideas
- Whether I rush or slow down at key moments

5. STRUCTURAL PATTERNS
- How I open pieces (hook style)
- How I structure middles (lists, dense paragraphs, breaks, anecdotes)
- How I close pieces (callback, imperative, observation, question, aphorism)
- My use of headers, lists, bullets versus continuous prose

6. SIGNATURE MOVES
- Recurring phrases I use across pieces
- Rhetorical devices I lean on (questions, contrast structures, parallelism, repetition)
- My humor style (dry / observational / self-deprecating / cutting / warm)
- How I cite or attribute things
- Distinctive punctuation habits

7. ANTI-PATTERNS (what I notably AVOID)
- Words I never use
- Constructions I steer clear of
- Tones I don't take
- Topics I don't moralize about
- Cliches I don't fall into

Do NOT begin analysis yet. Wait for me to provide my first sample. When I send a sample, analyze it across all seven dimensions. After each sample, wait for me to send the next.

When I've sent all my samples and tell you "ANALYZE THE FULL SET," produce a unified voice profile across everything, noting which patterns are consistent across all samples (your CORE voice) and which vary by context (format-specific habits).

Confirm you understand before I send the first sample.
```

### Send your samples

After the AI confirms, paste sample 1. Wait for analysis. Paste sample 2. Wait. Continue until you've sent all your samples.

**Why one at a time and not all at once:** The AI's analysis of sample 2 will be sharper because it can already see patterns from sample 1. By sample 5, the AI is identifying nuances it would have missed if you'd dumped everything in at once. This is what Tiago Forte found in his original methodology, and it holds up across other practitioners.

### Trigger the synthesis

After all samples are analyzed, send:

```
ANALYZE THE FULL SET. Produce my unified voice profile per the original instructions. Identify which patterns appear in all or most samples (my CORE voice) versus which vary by format (context-specific habits).
```

Read the output. This is your raw voice profile.

---

## Phase 3: Refine the voice profile

The first-pass analysis will be roughly 70% accurate. Refining is what gets you to 90%+.

### Three refinement loops

**Loop 1: Test the voice on a new piece.**

Ask the AI:

```
Using the voice profile you just built, write a 150-word [pick a format — LinkedIn post, email opening, blog intro] on this topic: [pick a topic in your usual subject area].
```

Read the output. Mark it up like an editor:

- Underline lines that feel off (too formal, wrong vocabulary, wrong rhythm)
- Circle lines that feel genuinely YOU
- Flag any specific words or phrases you'd never use

**Loop 2: Feed your edits back.**

Tell the AI:

```
Here's your draft with my edits. Tell me what specifically you missed in the voice profile that caused these mistakes. Then update the profile with what you learned.
```

Paste your annotated version. The AI will revise the profile.

**Loop 3: Repeat with a different format.**

Ask the AI to write something in a DIFFERENT format than Loop 1 — if Loop 1 was a social post, Loop 3 is an email. This catches voice elements that only show up in some formats.

After three loops most people have a voice profile that consistently produces work they'd put their name on without editing.

### Common refinement adjustments

- "I use 'and' as a sentence starter much more than the profile suggests"
- "I never use Oxford commas / I always use Oxford commas — the profile got this wrong"
- "I'm sharper than this. Cut the hedging."
- "I use the word 'just' a lot. Add it to my signature vocabulary."
- "I never write 'utilize.' Always 'use.' Add to anti-patterns."
- "I open most pieces with a question or a number, never with 'In today's...'"
- "I don't use bullet lists as much as the profile says. I write more in paragraphs."

The more specific your corrections, the better the next pass.

---

## Phase 4: Build your final voice profile document

After refinement, ask the AI to deliver the FINAL version in second-person-imperative format (commands directed at "the writer," meaning the AI itself in future sessions):

```
Deliver the final voice profile as a clean instructional document I can paste into any AI tool's custom instructions or project setup. Use second-person imperative format ("Write...", "Avoid...", "Open with..."). Structure it under these section headers:

## Identity
## Tone Defaults
## Vocabulary I Use
## Vocabulary I Avoid  
## Sentence Patterns
## Structural Patterns
## Signature Moves
## Anti-Patterns (What I Don't Do)
## Calibration Sample

For the Calibration Sample, write one 100-word paragraph in my voice on a topic of your choosing in my usual subject area. This serves as a reference for future AI sessions.

Make every directive specific and concrete. No abstract guidance. No vague tone descriptors. Every instruction should be something an AI can verify against the actual writing it's producing.
```

This is your **voice print.** Save it as `voice-profile.md` (or whatever you want to call it) and treat it like a versioned document — v1.0 today, v1.1 next month after you've used it for a while and noticed gaps.

---

## Phase 5: Deploy the voice print

### Option A: ChatGPT Custom Instructions

Go to **Settings → Personalization → Custom Instructions** in ChatGPT.

There are two fields. Use them like this:

- **"What would you like ChatGPT to know about you?"** — Paste your Identity, Tone Defaults, and Vocabulary sections (the *who I am* parts). About 1,500 characters max.
- **"How would you like ChatGPT to respond?"** — Paste your Sentence Patterns, Structural Patterns, Signature Moves, and Anti-Patterns sections (the *how I write* parts). About 1,500 characters max.

If your full profile is over 3,000 characters total, trim by cutting examples. The instructions, not the examples, are what ChatGPT uses.

Save. Test by asking ChatGPT to write something. Should sound like you.

### Option B: Claude Projects

Create a new Project. Paste the entire voice profile (no length limit) into Project Instructions. Every chat inside that Project will write in your voice.

This is the cleanest option if you have Claude Pro. The full profile loads with no trimming, and you can have separate projects for different content types ("Newsletter voice," "Social voice," "Coaching emails voice") if you have meaningfully different registers.

### Option C: Gemini Gems

Create a new Gem. Paste your voice profile into the Instructions field. Most users find Gemini handles longer instructions well.

### Option D: Build a Custom GPT (advanced)

If you're on ChatGPT Plus and you have your voice profile dialed, build a Custom GPT:

1. Go to **Explore GPTs → Create**
2. In the Configure tab, paste your voice profile in the Instructions field
3. In the Knowledge section, upload your original writing samples (the ones from Phase 1) as files
4. Set Conversation Starters to your most common requests ("Write a LinkedIn post about...", "Draft an email replying to...")
5. Save as private or share within your team

The advantage of the Custom GPT is that it can reference your original samples directly during generation, not just the abstract profile. The output quality jumps noticeably.

### Option E: Always-paste method (no subscription required)

If you're using a free AI tool or want maximum portability:

1. Save your voice profile as a `.txt` or `.md` file
2. At the start of every new AI chat, paste it as your first message before you ask anything
3. The AI will apply it for that conversation

Tedious, but works with any tool.

### Combine with the anti-AI-tell prompt

For best results, deploy your voice profile **alongside** yesterday's "Stop AI From Sounding Like AI" prompt:

1. Anti-AI-tell prompt loads the BANS (what not to do)
2. Voice profile loads the SIGNATURE (what to do)

Together they produce writing that sounds like you AND doesn't sound like AI. Without both, you risk either generic-non-AI prose (anti-tell only) or AI-flavored-imitation-of-you (voice only).

---

## Phase 6: Maintain and update

Your voice will evolve. The profile should evolve with it.

### Light maintenance (monthly)

Every month or so, when you write something off-AI that you really like, do a quick check: does this match what's in the voice profile? If not, what's different? Update the profile.

### Heavy maintenance (every 6 months)

Twice a year, repeat Phase 1 with 3–5 of your most recent unique writings. Compare the new analysis to your existing profile. Update where your voice has shifted.

### Version it

Number every revision (v1.0, v1.1, v1.2). Keep a changelog at the bottom of the profile noting what changed. This helps you roll back if a refinement made the output worse.

### When the AI's output starts feeling generic again

Two common culprits:

1. The AI model was updated and behaves differently. Re-test the profile and refine.
2. Your writing has drifted from what's in the profile. Update the profile.

---

## The Voice Profile Template

If you want a faster path or you'd rather build the profile manually without using AI to analyze samples, fill out this template:

```
# My Voice Profile

## Identity
- I am a [profession / role / area of expertise].
- My audience is [description: who reads my work, their level, their priorities].
- My voice is best described as [pick 3-5 adjectives, e.g., "direct, slightly contrarian, dry-humored, data-led, practical"].

## Tone Defaults
- Default register: [casual / professional / formal / mixed]
- When teaching: [shift description, e.g., "more patient, more examples"]
- When debating: [shift description, e.g., "sharper, less hedging"]
- When closing: [shift description, e.g., "land on imperative or quotable line"]

## Vocabulary I Use
- Signature words I use often: [list 10-20 specific words]
- Industry-specific terms and how I deploy them: [list with notes]
- Slang, idioms, or regionalisms: [list]

## Vocabulary I Avoid
- Specific words I never use: [list]
- Phrases I never use: [list]
- Tones I never take: [list]

## Sentence Patterns
- Typical sentence length: [shorter than X / mixed X-Y / longer than Y words]
- Variation: [describe — uniform? extreme? what's the pattern?]
- How I open sentences: [e.g., "often with conjunctions like 'And' or 'But'"; "with subject first"; "with phrases"]
- How I end sentences: [describe]
- Fragments: [when I use them, e.g., "for emphasis after a longer sentence"]
- Active vs passive: [tendency]

## Structural Patterns
- How I open pieces: [hook style — number, question, contrarian statement, story drop, etc.]
- How I structure middles: [paragraphs / lists / sections / mixed]
- How I close pieces: [callback, imperative, observation, question, single-sentence punch]
- Headers, lists, bullets vs prose: [tendencies]

## Signature Moves
- [Move 1 — describe with example, e.g., "I often pair a specific stat with a contrarian framing in the same sentence"]
- [Move 2]
- [Move 3]

## Anti-Patterns (What I Don't Do)
- [Specific thing I avoid 1]
- [Specific thing I avoid 2]
- [Specific thing I avoid 3]

## Calibration Sample
A 100-word piece in my voice. Use this as the reference for tone, rhythm, and structure when generating new content:

[paste a piece of your real writing here, 100 words or so]

---

When generating new content for me, write to this profile. Match the rhythm, vocabulary, and structure described above. If I tell you the output sounds wrong, identify which specific element of this profile slipped and revise.
```

Fill it out from memory or while looking at your favorite recent piece you wrote.

---

## Common mistakes to avoid

**Mistake 1: Using AI-edited samples.** Your "samples" need to be writing the AI hasn't touched. If you fed last year's blog posts that you wrote with AI help into the analysis, you're cloning the AI, not yourself.

**Mistake 2: Vague descriptors.** "Conversational tone" tells the AI nothing. "Sentences average 12-15 words, often opening with conjunctions like 'And' or 'But,' frequently including parenthetical asides" tells the AI everything.

**Mistake 3: Skipping the refinement loops.** First-pass profiles are 70% accurate. Most people accept the first pass and end up disappointed. The refinement loops are where the magic happens.

**Mistake 4: Loading only one format of sample.** If all your samples are LinkedIn posts, you'll get LinkedIn-voice. Mix formats.

**Mistake 5: Not pairing with anti-AI-tell instructions.** Voice profile alone won't strip out AI tells from new generations. You need both.

**Mistake 6: Forgetting to version.** When you refine in three months, you'll wish you had v1.0 to compare to.

---

## What you should see when it's working

When your voice profile is dialed, three things happen:

1. **Read your AI-generated outputs without editing.** If you can paste straight to LinkedIn or send straight as an email without touching anything, the profile is working.

2. **A colleague who knows your writing reads it and can't tell.** This is the real test. Forward a draft to someone who's read enough of your work to know your voice. If they don't suspect AI, you're done.

3. **You stop revising prompts every time.** You ask for what you want ("Write a LinkedIn post about X") and the AI nails the voice on the first try. No "make it more casual" follow-ups.

If you're getting one or two of these but not all three, refine one more loop. If you're getting all three, you have a working voice print.

---

## The combined deployment

Your final AI setup, after both yesterday's and today's instructions, looks like this:

**In your AI tool's custom instructions / project setup:**

```
[PASTE: AI Voice Custom Instructions — Stop AI From Sounding Like AI prompt]

[PASTE: Your Voice Profile]
```

In that order. The anti-AI-tell prompt runs the bans first; the voice profile then writes inside the constraints.

Everything the AI produces for you from that point on:

- Doesn't use em dashes
- Doesn't say "delve," "tapestry," "robust," and the rest of the AI vocabulary
- Doesn't stack negative parallelisms or Rule-of-Three constructions
- Sounds like you specifically — your vocabulary, your sentence patterns, your signature moves
- Doesn't sound generically human; sounds like YOUR human

---

## Sources

This guide synthesizes methodology from:

- Tiago Forte, "How to Create an AI Style Guide" (Forte Labs)
- Dean Seddon, "How I Make ChatGPT Sound Like Me" (Signal Newsletter)
- Zapier, "How to Train ChatGPT to Write Like You"
- LikeOne.ai, "How to Train AI to Write Like You: A Step-by-Step Voice Cloning Guide"
- CyberCorsairs, "The Ultimate ChatGPT Voice Cloning Prompt"
- GenAI Training NZ, "How to Train ChatGPT to Write in YOUR Voice"
- Writing for Devs, "Clone Your Writing Voice With This AI Prompt"
- GodofPrompt, "How to Make ChatGPT Write Like You"
- ZAKA, "How to Train ChatGPT to Write Like You"
- Christopher S. Penn, "Style Transfer in Generative AI Writing"
- f/awesome-chatgpt-prompts (GitHub, 143k+ stars)
- mustvlad/ChatGPT-System-Prompts (GitHub)
- LouisShark/chatgpt_system_prompt (GitHub)
- Descript, "3 Ways to Get ChatGPT to Write Like You"
- MakeUseOf, "How to Train ChatGPT to Write Like You"

---

*Version 1.0. End of guide. Pair with the "Stop AI From Sounding Like AI" prompt for full coverage.*
