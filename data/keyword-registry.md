# Keyword Registry

The master list of every ManyChat gate keyword and every LinkedIn source-tag. One row per offer. Same discipline as the podcast promo registry: check here before assigning a keyword so offers do not silently repeat and keywords do not collide.

Governing spec: [`../docs/automation/manychat-flows.md`](../docs/automation/manychat-flows.md). Strategy: [`../docs/strategy/2026-07-21-goal-reset-and-gate-layer.md`](../docs/strategy/2026-07-21-goal-reset-and-gate-layer.md).

---

## Rules

- **Keep the active set small and repeated.** Five keywords the audience learns beats twenty they do not. Reuse an evergreen keyword across weeks rather than minting a new one for every video.
- **The keyword is passed to Loomly / posted verbatim.** A reworded keyword ("comment SCRIPT" vs "comment SCRIPTS") silently breaks that post's ManyChat trigger and the leads vanish with no error. Jennica copies it exactly from this file.
- **One keyword = one asset = one ManyChat flow.** If the asset changes, either update the flow or use a new keyword; never point one keyword at two things.
- **Gated posts are IG + FB only.** LinkedIn never carries a keyword; it carries a source-tagged link instead (see the source-tag table).

---

## Active keywords (IG + FB gates)

| Keyword | Asset delivered | Pillar / flavor | Flow built? | First used | Notes |
|---|---|---|---|---|---|
| `SCRIPTS` | Objection Response Vault (the flagship "say this" doc) | Giveaway / "say this, not that" | ☐ | — | Reuse across all "say this" tip videos + the gated script carousel |
| `PROMPT` | 700-prompt vault (tapthis.co) | Giveaway / AI prompt | ☐ | — | The weekly prompt video |
| `VAULT` | Objection Vault (alias reserved) | — | ☐ | — | Reserved; do not assign elsewhere |
| `VOICE` | /sound-like-you tool | Tool launch (cycle 1) | ☐ | — | First tool launch |
| `TOOLKIT` | AI webinar toolkit / /webinar tools | Giveaway / tool use-case | ☐ | — | Frame by use case, rotate the entry point |
| `WEBINAR` | Event registration link | Event promo (weeks 4-6 of cycle) | ☐ | — | Removes the outbound link from the post (fixes FB -10.5x throttle) |
| `LIST` | The checklist/template from a gated carousel payload | Carousel / gated | ☐ | — | Generic carousel gate; pair with the specific asset per post |

☐ = flow not yet built in ManyChat. Flip to ✅ with the date once tested end-to-end.

---

## LinkedIn source-tags (link-based capture, no keyword)

LinkedIn gated carousels drop a link in the **first comment** (not the post body -- LinkedIn downranks body links). The link carries a source tag so Close can tell a LinkedIn tool lead from an IG gate lead from an organic tapthis visitor. Without the tag, all three blur into one bucket and attribution dies.

Scheme: `tapthis.co/<asset>?src=li-<slug>`

| Link | src tag | Maps to asset | Close source value |
|---|---|---|---|
| `tapthis.co/scripts?src=li-scripts` | `li-scripts` | Objection Response Vault | `LinkedIn - Scripts` |
| `tapthis.co/?src=li-prompts` | `li-prompts` | 700-prompt vault | `LinkedIn - Prompts` |
| `tapthis.co/sound-like-you?src=li-voice` | `li-voice` | Sound Like You tool | `LinkedIn - Voice` |
| `tapthis.co/webinar?src=li-toolkit` | `li-toolkit` | Webinar toolkit | `LinkedIn - Toolkit` |

The tapthis capture page reads `src` and writes the matching Close source value on the email it captures. (Requires the source-tag handling added to `kale-ai-prompts/app/api/capture-email/route.ts`.)

---

## Retired / burned keywords

None yet. When an offer is permanently retired, move its row here so the keyword is not accidentally reused for a different asset (which would misroute anyone who comments the old word on an old post still floating in the feed).
