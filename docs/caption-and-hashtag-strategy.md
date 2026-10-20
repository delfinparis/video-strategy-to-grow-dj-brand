# Caption and Hashtag Strategy (2026)

The operating rules for descriptions and hashtags on every script in this repo. This is the forward-looking standard; the evidence behind it is in [`docs/analytics/2026-06-14-short-form-stress-test.md`](analytics/2026-06-14-short-form-stress-test.md). It extends, and never overrides, [`editorial-standards.md`](editorial-standards.md) and the CLAUDE.md social-caption rules (no em dashes, no AI-speak, no engagement-asks).

**Why this exists:** discovery moved from hashtags to in-app search, and hashtag over-tagging now suppresses reach on the two platforms that matter most for D.J. (LinkedIn and Instagram). The old "11 realtor hashtags per post" practice is retired.

---

## Rule 0: One sentence, every platform; hashtags only where they help (changed 2026-10-19)

**Every social caption is one sentence, on LinkedIn, Instagram, TikTok, YouTube Shorts, and Facebook.** One brand voice everywhere, no per-platform shapes. **Hashtags appear only on TikTok and YouTube Shorts, 1-2 of them** (Rule 1).

**Why:** D.J.'s call, 2026-10-19. Multi-paragraph captions with cited stats and a hashtag block looked like someone else wrote them. A working agent does not post three paragraphs from their phone every day, so the length gave the post away as ghostwritten and took the authenticity out of it. The video does the explaining. The caption only has to get the tap. And the 2026 data says hashtags do little or nothing for reach on these platforms (Mosseri, July 2026: "Hashtags work, but they've never been a good way to actually increase your reach"; Socialinsider found no link between hashtag count and reach across 75M Instagram posts; LinkedIn removed hashtag following in 2024 and Ordinal's dataset shows hashtagged posts getting about a third of the impressions).

**The rule:**

- **One sentence.** Under about 150 characters. Not two sentences joined by a comma splice, not a sentence plus a hashtag line, not a sentence plus a source line.
- **Write it like D.J. typed it on a phone.** A reaction or a point of view, not a summary of the video. "If you're still telling Chicago buyers to wait for spring, you haven't looked at October" beats "Realtor.com says listing prices are down 3.5% from the summer peak."
- **The plain search phrase lives inside the sentence** (Rule 2). One sentence lands inside Instagram's 125-character preview by default.
- **Hashtags only on TikTok and YouTube Shorts, 1-2 topical keyword tags.** Zero on LinkedIn, Instagram, and Facebook (Rule 1).
- **No `Hashtags:` label, ever.** The tags go at the end of the caption sentence, on the same line, with no label in front (`...nobody tells you that. #RealEstateAgent #RealtorTips`). D.J. copies the caption and tags in one paste, so a label word comes along and has to be deleted by hand (D.J.'s call, 2026-10-19).
- **No stats, no citations, no source names in the caption.** The video and the script's Data Source section carry the receipts.
- **Same sentence on every platform is fine.** Light tweaks are allowed (Facebook can be a touch more local), but never a longer version for one platform.
- **Gated posts (IG + FB only):** the one sentence is the gate. "Comment SPLIT and I'll send you the breakeven sheet." Keyword from [`data/keyword-registry.md`](../data/keyword-registry.md), verbatim.
- **LinkedIn link-in-first-comment** (gated carousels) is unchanged. The link goes in the comment, not the caption.

**Older scripts are not examples.** Every script written before 2026-10-19 carries multi-paragraph captions and hashtag blocks. Do not copy caption length or hashtags from them.

**Re-test:** compare four weeks of one-sentence posts against the four weeks before 2026-10-19 in the content-analytics system (`scripts/analyze_posts.py`). If LinkedIn reach drops meaningfully, revisit LinkedIn only.

---

## Rule 1: Hashtags only where the platform still uses them (2026-10-19)

D.J.'s rule: keep a hashtag or two on the channels where we know the platform uses them to sort and surface a post, and drop them everywhere else.

| Platform | Count | Why |
|---|---|---|
| **TikTok** | **1-2** | The strongest case left. TikTok still reads tags as topic and search labels next to the caption keywords. Plain keyword tags (`#RealEstateAgent`, `#ChicagoRealEstate`); never `#fyp` or other generic tags. |
| **YouTube Shorts** | **1-2** | YouTube's own help docs say hashtags help viewers find videos, and tags show as clickable links above the title. Put them at the end of the description. No `#shorts`; the title does the ranking. |
| **LinkedIn** | **0** | LinkedIn removed hashtag following and hashtag feeds in 2024. In Ordinal's dataset, hashtagged posts got about a third of the impressions. |
| **Instagram** | **0** | Mosseri, July 2026: "Hashtags work, but they've never been a good way to actually increase your reach." Socialinsider found no link between hashtag count and reach across 75M posts. |
| **Facebook** | **0** | Hashtags add little; no 2026 data showing a lift. |

No brand tag anywhere. "We know it helps" is a strong word for TikTok and YouTube: neither platform publishes a reach lift from tags. They are the two where the platform still uses tags to sort content, so they keep one or two. The previous caps (3-5 on LinkedIn/Instagram/TikTok/YouTube, 2-3 on Facebook, set 2026-07-07) are retired.

D.J. does not post to X/Twitter, so there is no X caption. Scripts produce five captions: LinkedIn, Instagram, TikTok, YouTube Shorts, Facebook.

### YouTube Shorts is two fields, not one

**Added 2026-08-20, after D.J. found board rows whose YouTube block had a description and hashtags and no title.** Every other platform's caption is one line. YouTube Shorts is not:

```markdown
### YouTube Shorts

**Title:** The First-Time Buyer Number You've Been Quoting Is Wrong

**Description:** Most agents are still quoting first-time buyers a number that stopped being true this year. #FirstTimeHomeBuyer #RealEstateAgent
```

**A YouTube Shorts block with no `**Title:**` line is incomplete, not merely terse.** The title is the primary ranked text on the platform and the only part that shows in search, suggested, and the subscriptions feed. Leave it out and YouTube falls back to the first line of the description, truncated wherever it happens to end, or to nothing at all. The title does the ranking; the description is the same one sentence as every other platform.

Write it as a claim a realtor would search for, not a label. "The First-Time Buyer Number You've Been Quoting Is Wrong" beats "First-Time Buyer Stats." Under about 60 characters so it does not truncate.

---

## Rule 2: Write the sentence for in-app search, not just for the scroll

Hashtags used to be how people found content. Now it is in-app search (Instagram, TikTok, and YouTube all behave like search engines, and LinkedIn's 2026 feed reads the post semantically). The job is to put the words an agent would actually type into the one sentence.

- **Use one real search phrase** in plain language: "real estate commission," "Chicago buyers," "buyer agency agreement," "listing appointment." Use the phrase the audience would search, not jargon.
- **Captions now rank in Google, not just in-app.** Since July 2025, public Instagram posts surface in Google and Bing results (Instagram, 2025). One more reason the plain search phrase beats a clever one-liner.
- **Weave it in, never bolt it on.** The sentence still has to sound like D.J. A keyword-stuffed sentence fails Rule 0.

---

## Rule 3: Optimize for the send and for dwell, never for the comment

The 2026 signal mix rewards attention and private sharing. Comments are falling across platforms and comment-baiting is downranked.

- **Make it sendable.** The test is "would one agent DM this to another agent?" On Instagram, a send is weighted roughly 3-5x a like for reaching new audiences, and shares are the top distribution signal (Mosseri / Buffer 2026). IG shares grew +67% YoY while reach fell, so the send is the escape hatch from the 2026 crowding (Metricool 2026). Facebook Reels reward the same finish-plus-share signal. This is the "shareable moment" editorial rule pointed at the private send, not the public comment.
- **Make it hold attention (dwell).** LinkedIn's 2026 feed weights "long dwells." The video that holds them feeds this signal; the one-sentence caption just gets them into it. The existing hook and 15-second re-hook rules already serve this; keep them.
- **Never add an engagement-ask to chase this.** No "comment below," no "tag an agent," no "share this." Those are banned by editorial standard and now also downranked by LinkedIn. Sendability is earned by the content being worth sending, not by asking.

---

## Rule 4: Platform-specific notes

- **LinkedIn (#1):** the canonical surface. Same one sentence, plain words, so the semantic feed places it. Post once per ~12 hours max (a second same-day post cannibalizes the first).
- **Facebook (#2):** surging in 2026 and 74% Chicago. Same one sentence; a local word ("Chicago") earns its place here.
- **Instagram (#3):** the one sentence fits the 125-character preview, so search indexes all of it.
- **TikTok (secondary):** the sentence is the search label, plus 1-2 keyword tags.
- **YouTube (#4):** the Title does the ranking; the description is the same one sentence plus 1-2 topical tags.

---

## What did not change

- No engagement-asks. Now an algorithmic advantage as well as a brand rule.
- Strong first-line hooks, the shareable moment, the 15-second re-hook. All still serve the 2026 signal mix (dwell, sends).
- Em-dash and AI-speak scrub on every caption. Unchanged, strict as ever.

*Written 2026-06-14 from the short-form stress test. Rewritten 2026-10-19: one sentence on every platform, 1-2 hashtags on TikTok and YouTube Shorts only (Rules 0-1). Updated 2026-07-07 with the mid-2026 platform data (Metricool 2026 hashtag + share studies, Buffer 2026, Mosseri) and to drop X/Twitter (D.J. does not use it). Re-test at the July 19 pivot review. When `generate_descriptions.py` or `draft_nf.py` produce captions, they follow this standard.*
