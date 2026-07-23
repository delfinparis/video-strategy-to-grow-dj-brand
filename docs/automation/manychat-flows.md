# ManyChat Flows — the gate, the qualifier, the routing

**Status:** spec. ManyChat not yet purchased. This document is what to build inside ManyChat + Close once it is, and it is the single source of truth for how a comment becomes a qualified lead.

Governing strategy: [`../strategy/2026-07-21-goal-reset-and-gate-layer.md`](../strategy/2026-07-21-goal-reset-and-gate-layer.md). Editorial permission for the gate: the Rule 4 value-exchange exception in [`../editorial-standards.md`](../editorial-standards.md). Keyword allocation: [`../../data/keyword-registry.md`](../../data/keyword-registry.md).

---

## The whole flow, one picture

```
Gated post (IG or FB only) ends with a spoken keyword ask
        |
Viewer comments the keyword
        |
ManyChat auto-replies in the comment ("check your DMs") + opens a DM
        |
DM delivers the asset immediately (link or file) -- promise kept first, no gate before the payoff
        |
Q1 GEOGRAPHY: "Sending it now. So I point you at the right stuff -- you licensed in Illinois?"
        |  [ Yes, Illinois ]      [ No / another state ]
        |
Q2 INTENT (asked of everyone): "Real quick -- what's the ONE thing you'd change about
        your brokerage if you could?"
        [ Split / fees ]  [ Support / training ]  [ Not enough leads ]  [ Nothing, I'm happy ]
        |
Email capture: "Want me to send new plays like this straight to you? Drop your best email."
        |
Write to Close (see field map) + route to the right nurture
```

Two design rules that make this work and keep it on the right side of the editorial standard:

1. **Deliver the asset BEFORE the questions.** The viewer asked for a thing; give it first. The questions come after the promise is kept, framed as "so I can help you better," never as a toll gate. This is what separates a value exchange from bait.
2. **Every question is optional to answer.** If they ghost after the asset, they still got the asset and they are still a captured lead. The qualifier improves a lead; it never blocks one.

---

## Q2 is the fix for lead quality (do not skip it)

The geography question alone was the original design, and it was not enough. It filters *where* someone is, never *whether they are recruitable*. A person who comments for a free prompt is, by default, a content fan, not a switch-ready agent -- the gate optimizes for the easiest yes, which selects against movers.

**Q2 is the intent filter.** One tap turns every giveaway lead into a qualified-or-not signal, and it hands Ana a warm opener ("you mentioned your split -- can I show you the math on that?"). It is the highest-leverage, lowest-cost fix in the whole system. It runs on every gated flow, giveaway or carousel.

---

## Routing: the four-way sort

| Illinois? | Q2 answer | Segment | What happens |
|---|---|---|---|
| Yes | Split / Support / Leads | 🔥 **HOT Chicago** | Close status set for Ana; Ana works it personally within the week; enters the "how Kale fixes [their pain]" 3-email branch |
| Yes | Nothing, I'm happy | **Warm Chicago** | 4-email value nurture, soft Kale; revisit in 90 days |
| No | any | **National** | KIRP + tools value nurture. No Kale, ever. This is the KIRP-listener + tool-user route |
| (no answer) | (no answer) | **Unqualified capture** | Email in Close, source-tagged, generic value nurture until they self-identify |

---

## Close field map

The flow writes these on lead create/update. IDs verified 2026-07-21.

| Purpose | Field | Value |
|---|---|---|
| Lead source | `cf_U9j9E5v9LuS4SMLZfI854gU88tmhi0GLVlxtzbZp1yD` (Kale Lead Source) | `IG Gate - <keyword>` / `FB Gate - <keyword>` |
| Chicago flag | `cf_aKZB3coV3WITJnadFpvz3v68CxwtUFZLwGriTYE2sNv` (Chicago Agent) | Yes / No |
| **Brokerage pain (NEW field to create)** | Brokerage Pain (text or choice) | Split / Support / Leads / Happy |
| Pipeline stage | `cf_v8hykgKmpI4sXeaJ6tOO90V7h1Sumi7o88xXGKQKlbx` (Pipeline Stage) | New Lead → Responded |

**One field must be created in Close before launch:** *Brokerage Pain* (choice field: Split-fees / Support-training / Leads / Happy). Without it, Q2's answer has nowhere to land and the whole quality fix evaporates.

---

## The nurture sequences (Fix 2 — capture is a dead list without these)

An email in Close with no follow-up is not a lead. Each segment gets a sequence. Build in Close; templates can start from [`../close-email-templates/`](../close-email-templates/).

**HOT Chicago (pain stated)** — the only sequence with a hard recruiting goal:
1. Deliver-more: "here's the full [asset], plus the two I didn't put in the video"
2. Pain-specific: "you said [split/support/leads] -- here's exactly what that costs you per year at a typical shop, and what it looks like at Kale" (soft, math-first, never a hard pitch; FB-throttle logic applies to tone even in email)
3. Proof: a Chicago agent who switched for that exact reason (real, sourced, with permission)
4. Ana's personal note / call booking

**Warm Chicago (happy)** — value first, Kale as a whisper:
1-4. Best plays, tools, and one KIRP episode each, with a single soft "when you're ever curious what Kale's flat model looks like, reply and I'll send the one-pager."

**National** — no Kale at all:
1-4. Tools + KIRP episodes matched to their stated pain. The goal is a listener and a tool user, and eventually a referral relationship. Never a recruiting ask they can't act on.

---

## Ownership

| Job | Owner |
|---|---|
| Build + maintain ManyChat flows | D.J. sets up (his accounts); Jennica swaps keywords per the registry |
| Create the Brokerage Pain field in Close | D.J. / whoever owns Close config |
| Work HOT Chicago leads | Ana |
| Nurture sequences (build + send) | Ana |
| Broker-problem comment mining (ungated posts) | Jennica flags Chicago complainers into Close |

---

## Launch checklist

- [ ] ManyChat purchased, IG + FB connected
- [ ] Brokerage Pain field created in Close
- [ ] One flow built and tested end-to-end (comment → DM → asset → Q1 → Q2 → email → Close record with correct source tag)
- [ ] The three nurture sequences built in Close
- [ ] At least one flagship asset (the Objection Response Vault) actually exists and is good
- [ ] Keyword registry seeded with the launch set
- [ ] Everyone in the ownership table knows their job
