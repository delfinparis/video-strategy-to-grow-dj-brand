# Sacred cows: the takes bank

Standing candidates for the take lane on **both surfaces**: the 3 weekly take videos
(Mon/Wed/Fri, [`take-standard.md`](../docs/series/take-standard.md)) and the 3 weekly take
carousels that pair with them. A take is a defensible contrarian position that names a wrong
default, cites a source, and hands the agent something to do. Not a rant, not news.

**One entry feeds both surfaces on the same day.** The video makes the argument (the
who-profits turn is spoken); the carousel hands over the receipt in saveable form. A paired
video and carousel count as **one** use against the 8-week rotation rule, not two. That
pairing is the only reason a 3-a-week video cadence is affordable: one verification pass
covers both.

**These are candidates, not scripts.** Nothing here ships without re-verification at
build time (Rule 1, and the carousel standard's reuse rule: a stat that was right in
April may be wrong by July).

---

## The qualifying test

A candidate is only a take if it clears all four:

1. **Is there a real number behind it?** Named source, publication year. If the only
   support is "everyone knows," it is an opinion, not a take. Kill it or find the number.
2. **Does D.J. actually believe it?** He is a brokerage president on the record in trade
   press. He does not float positions he would not defend on a podcast.
3. **Would a competent agent genuinely disagree?** If every agent already nods, it is a
   tip, not a take, and it will generate nothing. The disagreement is the engine.
4. **Does it stand with the agent?** Friction points outward at a belief, a practice, or
   a system. Never at the agent for having believed it. That is the line between a
   recruiting wedge and an insult, and it is the difference between a comment thread and
   a pile-on.

## The heat ceiling

**Carousels: 3.5, and no higher.** Heat 3.5 is "defensible contrarian, cites a source,
names the wrong default," which the register already describes as high comment volume at
manageable risk.

**Video: 3.5 default, with exactly one heat 4 per week.** Rule 9.2 caps heat 4-5 at one
post a week across the entire publishing schedule, and that slot is the **Wednesday take
video**. It is one post, not one per series -- if a News or Broker Problems script wants
heat 4 that week, one of them gives way. Check the `news_brief.py` hook-cadence banner
before drafting.

**Never name a person, a brokerage, a coaching program, or a software product.** That is
heat 5 and it is banned outright on both surfaces, not rationed. Point at the practice and
the incentive behind it. Entries below that sit close to that line carry a **Heat check**.

### Specific about the practice, unidentifiable as a party

**The rule is not "avoid the name." It is "create no identifiable target."** Those are
different, and confusing them produces the two failure modes on either side of the good
version.

A knowing wink is not a shield. Defamation and commercial disparagement turn on whether a
reasonable reader can identify who is meant, not on whether the name was typed. "We all
know which brokerage does this" carries the same exposure as naming them, with less punch.
D.J. is a brokerage president quoted in the trade press, not an anonymous account.

The opposite failure is worse for the content: hedging into mush. "Some brokerages don't
provide great value" is safe and says nothing, and it will not earn a single comment.

**Go maximally specific about the practice, while the target stays a category:**

> The brokerage charging you a monthly technology fee for a website you never asked for
> and three leads a year you didn't close.

Every agent reading that supplies a name themselves, which is exactly the Rule 10.4 loop
closing in their head. Nobody can point at a defendant. Name the fee, the number, the
thing that happens on the deal, the sentence the manager says. Never the company.

**The recruiting reason, which matters more than the legal one.** These agents are the
people D.J. wants to hire. Someone at a brokerage that was obviously subtweeted cannot
come work for him without eating crow first. The post has to read as a description of
their *situation*, never an attack on their employer.

Test before shipping: **could a reader name one company with confidence?** If yes, it is
too identifiable, no matter how careful the wording. If no, and the practice still lands
hard enough that an agent recognises their own Tuesday in it, it is right.

---

## Bank

Each entry: the belief, who profits from it staying true, the turn, and where evidence
lives. `evidence: in-repo` means the sourcing already exists here and needs re-checking.
`evidence: research` means the number has to be found and verified before it can ship.

### Marketing and social

**"Stack hashtags for reach."**
Profits: nobody, it is inherited folklore. Turn: the tag stack is doing nothing the
first 125 characters could not do better. Evidence: in-repo,
[myths-that-dont-move-the-needle.md](../docs/myths-that-dont-move-the-needle.md) #1,
plus [caption-and-hashtag-strategy.md](../docs/caption-and-hashtag-strategy.md).

**"Ask for the comment."**
Profits: engagement-bait coaching. Turn: the ask is what suppresses the post. Evidence:
in-repo, myths #4. Note the irony is the point: this deck earns its comments without an ask.

**"Post as often as you can."**
Profits: content-mill services selling volume. Turn: past a threshold the extra posts
compete with each other. Evidence: in-repo, myths #3.

**"Chase the follower count."**
Profits: growth services and follower-count vanity. Turn: followers are not distribution
anymore; the feed does not care who follows you. Evidence: in-repo, myths #5.

**"Every reach drop is a shadowban."**
Profits: nobody, it is a comfort story. Turn: it is usually the hook. Evidence: in-repo,
myths #10. Heat check: this one lands closest to blaming the agent, so frame it as the
platform being indifferent rather than the agent being bad.

**"#fyp and #foryou boost your TikTok reach."**
Profits: nobody, it is cargo cult. Turn: TikTok has confirmed they do nothing for
distribution. Evidence: in-repo, myths #2.

**"Repost your TikToks to Reels."**
Profits: nobody, it is a time-saver that costs reach. Turn: the unoriginal-content
classifiers catch it. Evidence: in-repo, myths #6.

**"If a post flops, delete it and repost it later."**
Profits: nobody. Turn: the duplicate gets almost nothing and you forfeit the original's
residual distribution. Evidence: in-repo, myths #7.

**"Post at exactly the right time or you miss the window."**
Profits: scheduling tools selling a best-time chart. Turn: the charts openly contradict
each other because they are population averages, and roughly 70 percent of an Instagram
post's views land in the first 72 hours anyway. Evidence: in-repo, myths #8.

**"Keep every video under 15 seconds."**
Profits: nobody, it is a rule that outlived its platform. Turn: length is
retention-relative; a 15-second video with a weak hook loses to a 60-second one that
holds. Evidence: in-repo, myths #9.

### Brokerage economics

**"Switching means starting over. Your clients won't follow."**
Profits: the brokerage that wants retention without earning it. Turn: roughly two in
three sellers come from referral or repeat business, and they chose the agent. Evidence:
in-repo, [recruiting-objections.md](../docs/recruiting-objections.md) rank 2. Re-verify
the NAR figure before shipping.

**"The national brand gives you credibility with clients."**
Profits: the brand charging for it. Turn: consumers rank brokerage brand near the bottom
of what they care about. Evidence: in-repo, objection map rank 3. Needs the current NAR
Profile citation.

**"A cheap brokerage means you're on your own."**
Profits: full-fee brokerages, and it is **often true** at the volume plays. Turn: the
honest version is that price and support are independent variables, and most agents have
only ever seen them bundled. Evidence: in-repo, objection map rank 1. This is the closest
thing to a Kale pitch in the bank, so it has to be argued on the general case and never
mention Kale in the slides.

**"Going cheap means admitting you're not a serious producer."**
Profits: the identity economy around brokerage badges. Turn: identity dressed as
strategy. Evidence: in-repo, objection map rank 4. Highest emotional charge here, handle
with care: it is about the belief, never about agents who hold it.

**"You plateau because you need a better split."**
Profits: recruiters using split as the only lever. Turn: the split is downstream of
volume; a better split on the same production is a raise, not a business. Evidence:
research.

**"New agents get no training at a cheap brokerage."**
Profits: full-fee brokerages, and like the support objection it is **often true**. Turn:
agents pay big-brand fees and then train off YouTube anyway. Evidence: in-repo,
[recruiting-objections.md](../docs/recruiting-objections.md) rank 5. **Heat check:** argue
the general case, never mention Kale in the script.

**"Monthly fees will eat you alive at low volume."**
Profits: percentage-split brokerages, because low volume is exactly where a fat split
costs most. Turn: run the actual arithmetic at three deals a year. Evidence: in-repo,
objection map rank 6. **Heat check:** this is the entry closest to being a Kale ad. It
only ships if it passes the test in
[content-recruiting-integration.md](../docs/content-recruiting-integration.md): would D.J.
publish it if he were recruiting nobody this month?

**"Revenue share is passive income."**
Profits: the recruiting-driven models built on it. Turn: income that depends on recruiting
is a second job, not passive. Evidence: research. **Heat check:** argue the model. Naming
the company is heat 5 and banned.

**"Joining a team is the fastest way to grow."**
Profits: team leads who need production. Turn: sometimes true and sometimes an expensive
apprenticeship the agent never graduates from. Evidence: research. Frame honestly as a
depends, which makes it more defensible, not less.

### Practice

**"Open houses are how you get buyers."**
Profits: the listing agent who wants Sunday coverage. Turn: a small share of buyers find
their home at one. Evidence: in-repo, EVERGREEN-003 already ran this as a data card, so a
take version needs a different angle or an 8-week gap.

**"You need a bigger CRM / more leads."**
Profits: lead vendors. Turn: the database an agent already owns is unworked. Evidence:
in-repo, EVERGREEN-002 pop-by system. Same 8-week rule.

**"Narrate the house on a showing."**
Profits: nobody, it is nerves. Turn: talking is performing, listening is closing.
Evidence: in-repo, PB-007. Already carouseled, needs the gap.

**"Answer every lead in five minutes or lose it."**
Profits: speed-to-lead software. Turn: worth checking whether the number survives
scrutiny, and what it costs an agent to organise a day around it. Evidence: research.
Flag: do not ship unless the counter-number is solid.

**"Price it high, you can always come down."**
Profits: the agent who wanted the listing and bought it with a number. Turn: the first
two weeks are the only two weeks of real attention, and a price cut spends them. Evidence:
research. Needs a current days-on-market or price-reduction figure before it ships.

**"The listing presentation is what wins the listing."**
Profits: presentation-template sellers and the coaching built around the appointment.
Turn: the decision usually happened before the appointment; the presentation confirms it.
Evidence: in-repo, script 065 (the loop-back example in editorial-standards Rule 9.1).
Already aired as a video, so a take version needs a new angle or an 8-week gap.

**"Send a monthly market update email."**
Profits: nobody, it is inherited from a decade when it was novel. Turn: a monthly stat
dump trains the list to skip your name. Evidence: research. The in-repo starting point is
the Family 2 opener in [opener-swipe-file.md](../docs/opener-swipe-file.md).

**"Farm a zip code with mailers."**
Profits: print and mail vendors, who get paid whether or not it works. Turn: the spend is
real and immediate, the attribution is neither. Evidence: research. Needs a cost-per-lead
comparison before it ships.

**"Never tell a seller no."**
Profits: nobody, it is conflict avoidance dressed as service. Turn: the agent who never
pushes back gets hired and then ignored. Evidence: research, and this one is a candidate
for the archive tie-in instead of a stat.

### Prospecting and follow-up

**"Ask a cold lead if they're still looking."**
Profits: nobody, it is the path of least resistance. Turn: the question invites a no and
gives the lead an easy exit. Evidence: in-repo, Family 9 line in
[opener-swipe-file.md](../docs/opener-swipe-file.md). The swap is the whole payload here,
so this is the natural Monday entry.

**"Expireds and FSBOs are where the business is."**
Profits: dialer software and the coaching that sells the list. Turn: it is the most
contested pool in the market and the agent with no differentiator loses it. Evidence:
research.

**"Follow up until they tell you to stop."**
Profits: sequence software sold on activity counts. Turn: persistence without a reason to
call is how an agent gets muted rather than hired. Evidence: research.

**"Buy portal leads to fill the pipeline."**
Profits: the portals. Turn: paying for a lead the agent then has to compete for is buying
a coin flip at retail. Evidence: research. **Heat check:** argue the model, never a named
portal. D.J. is on the record in trade press on portal issues and a named version reads as
score-settling.

**"Real estate is a numbers game."**
Profits: activity-based coaching that can sell a dial count more easily than a skill.
Turn: it is a numbers game only after the conversation works; volume on a broken
conversation just scales the broken part. Evidence: research or archive tie-in.

### Tech and AI

**"Use AI to write your listing descriptions."**
Profits: the tool vendors, and it is the single most common agent use case. Turn: the
default output is detectable and it is the one piece of writing a client actually reads.
Evidence: in-repo, [ai-tells-field-guide.md](../docs/ai-tells-field-guide.md) and the
voice-print builder docs. Strong candidate because D.J. teaches AI, which makes this a
Family 3 Defector hook rather than a Family 2 attack.

**"AI is going to replace agents."**
Profits: doom content, and the vendors selling the cure for it. Turn: it replaces the
parts of the job nobody was paying for anyway. Evidence: research.

**"Automate your follow-up completely."**
Profits: automation vendors. Turn: automation is good at reaching, bad at the sentence
that gets a reply. Evidence: research.

**"You need every tool in the stack."**
Profits: every vendor at every conference. Turn: tool count is inversely correlated with
the one system an agent actually runs. Evidence: research.

### Career and identity

**"Your first year is supposed to be brutal."**
Profits: brokerages whose model depends on churn. Turn: the difficulty is not a rite of
passage, it is an unmanaged onboarding. Evidence: in-repo, the Family 4 opener in
[opener-swipe-file.md](../docs/opener-swipe-file.md). This is a natural Wednesday heat-4
System Indictment.

**"Go full-time or you're not serious."**
Profits: the recruiting pitch that needs a full-time body. Turn: the part-timer who works
a real database beats the full-timer who waits at open houses. Evidence: research.
**Heat check:** this defends a cohort rather than attacking one, which is the right shape.

**"Just hustle harder."**
Profits: hustle-culture coaching. Turn: hours are the input an agent controls least and
measures worst. Evidence: research or archive tie-in.

**"Niche down immediately."**
Profits: branding consultants. Turn: a niche picked before you have any transaction data
is a guess with a logo on it. Evidence: research.

**"Your personal brand needs a logo and a color palette."**
Profits: designers and brand packages sold to new licensees. Turn: nobody has ever chosen
an agent on a color palette. Evidence: research.

---

## Rotation

Do not repeat an entry inside **8 weeks**, and do not run two from the same section back
to back. Log each use below.

**One row per entry, not per surface.** A paired video and carousel share a row. The video
claims the entry when D.J. films and logs it here; the 9:00am carousel routine reads this
table and does not re-pick a claimed entry.

**Runway.** 3 entries a week against a 42-entry bank with an 8-week no-repeat rule is
roughly 14 weeks of clean rotation. When the bank drops under 24 unused entries, refill it
before the rotation starts forcing repeats. Entries marked `Evidence: research` do not
count toward runway until their number is verified, which is roughly a third of the bank
today, so the real verified runway is shorter than the headline number.

Rows dated before 2026-08-10 predate the video lane and are carousel-only.

| Date | Entry | Video | Carousel |
|---|---|---|---|
| 2026-08-07 | "Stack hashtags for reach" (Marketing and social) | -- | `scripts/carousels/TAKE-hashtag-stacking-carousel.md` |
| 2026-08-10 | "Switching means starting over. Your clients won't follow." (Brokerage economics) | -- | `scripts/carousels/TAKE-switching-brokerages-carousel.md` |
