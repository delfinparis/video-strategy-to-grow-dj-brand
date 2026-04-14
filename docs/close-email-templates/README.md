# Close Email Templates: Content-to-Call Bridge

This library gives D.J. (and Ana / Jennica when applicable) ready-to-send email templates triggered by a content engager hitting Close CRM.

## How this library fits the recruiting bridge

The Sunday bridge protocol (see [`../content-recruiting-integration.md`](../content-recruiting-integration.md)) pulls engagers from Personal LinkedIn / Instagram / Facebook into Close with a `Content Source Detail` field set to the specific post they engaged with. That field is the trigger for picking which template below to use.

**The flow:**

1. Lead enters Close with `Content Source Detail = "NF-001 Tuccori post 4/10/26"`
2. D.J. (or Ana) opens this folder and picks the matching template (`drip-001-tuccori.md`)
3. Paste into Close, adjust the greeting, send
4. Follow up with a call within 48 hours via the "DJ Warm Outreach This Week" Smart View

## Voice rules (enforced by `../editorial-standards.md`)

Every template in this library follows the same rules as every other piece of content in this repo:

- **No fabricated stats.** Every specific number traces to a source documented in the matching script file.
- **No engagement asks.** No "follow me," no "subscribe," no "tag a broker." The ask is always a specific offer to the recipient: a call, a resource, a question they might want answered.
- **No em dashes.** Use `--` or restructure.
- **"D.J. Paris"** with periods. Not "DJ Paris."
- **Short.** Three-line body, max. Longer emails don't get read. Close is not Substack.
- **One specific offer per email.** Never stack two asks. Never introduce three ideas. One clear next step.

## When not to use a template

If the lead is inbound (they reached out first via joinkale.com, DM, or an event), these templates are the wrong fit. Inbound leads use the standard workflow in [`../recruiting-call-scripts.md`](../recruiting-call-scripts.md). This library is **only** for warm content engagers who self-selected via a specific post.

## Template inventory

| File | Triggered by | Pillar | Positioning |
|------|--------------|--------|-------------|
| [`drip-001-tuccori.md`](drip-001-tuccori.md) | NF-001 engagement | Inside the Industry | Chicago-local authority, settlement expertise |
| [`drip-002-nar-reached-out.md`](drip-002-nar-reached-out.md) | IA-002 engagement | Inside the Industry | NAR influencer credential, insider access |
| [`drip-003-ai-judgment.md`](drip-003-ai-judgment.md) | IS-001 engagement | Inside the Industry | Counter-positioning against AI crowd, 700-interview authority |
| [`drip-004-six-percent-club.md`](drip-004-six-percent-club.md) | IS-002 engagement | Inside the Industry | Top-producer behavioral pattern, practical |
| [`drip-005-lowball-play.md`](drip-005-lowball-play.md) | PB-001 engagement | The Playbook | Tactical field intelligence, Jefferson Fisher model |

## Updating this library

Any time a new Inside the Industry or The Playbook script goes live and earns meaningful engagement (50+ reactions on LinkedIn, or 5+ qualified profile views), add a matching template here. The library should grow with the content catalog.

When retiring a script, retire its template too. Stale references ("saw you liked my post from 6 months ago...") damage trust and signal D.J. is operating from a script instead of a relationship.
