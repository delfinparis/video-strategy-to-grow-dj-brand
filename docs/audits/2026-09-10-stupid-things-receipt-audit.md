# Receipt audit: the Stupid Things bank, 2026-09-10

Every one of the 39 `receipt: confirmed` entries in `data/stupid-things.json` was
re-checked against its own cited page on 2026-09-10.

**8 held. 11 were partly wrong. 19 were false. 1 could not be checked.**

The bank was the only thing deciding what the 5:30am brief offered, and it was
printing "receipt: confirmed" on numbers that do not exist.

## How it started

D.J. replied `1. 2` to the morning brief and got one script back for the wrong
option ([walk-and-talk-delivery.md](../automation/walk-and-talk-delivery.md)).
Rebuilding the lost pick meant re-verifying its receipt, which failed. So did the
next one. Three for three in a morning was enough to check all of them.

## What failed, and why

Every failure was one of two moves.

**1. The number came from someone selling something.** Six of the nine failing
sources were vendors: a marketing-software company, a call-software company, a
photography company grading its own photographs, a lead directory, a home-services
marketplace, an AI content blog. A vendor's content-marketing page is not a
research report, and "71% of buyers prefer an agent with a strong social presence"
traces to a CRM vendor. "Listings with video get 400% more inquiries" traces to
nobody at all -- it is credited to NAR everywhere and does not survive tracing.

**2. The year was the year it was banked, not the year it was published.** A 2019
Redfin article resting on a 2013 study went in as "Redfin 2026." A 2011 Harvard
Business Review study went in as 2026. NAR's 2024 Profile went in as 2026. Rule 1
requires a source *and* a publication year, and a wrong year makes a stale number
read as current, which is the version a commenter beats.

## The failures

| Entry | Banked | The source |
|---|---|---|
| ST-0003, ST-0023 | NAR's 2026 Code added offer-acknowledgment guidance; many MLSs now **require** written acknowledgment | **The opposite.** OneKey MLS *removed* the requirement. Written confirmation is on request only, no longer an MLS rule; the duty moved to SOP 1-7 |
| ST-0006, ST-0033, ST-0036, ST-0041 | Photos 87% most useful, detailed info 85%, 52% find home online | **41%** and **39%**. No 52% figure. 2024 data banked as 2026 |
| ST-0005, ST-0031 | Pro photos: $3,000-$11,200 more, 118% more views | **$3,400**-$11,200; no 118% figure anywhere. 2019 article, 2013 study, banked 2026 |
| ST-0042, ST-0045 | 71% prefer agents with social presence; video = 400% more inquiries | 71% traces to REsimpli, a marketing vendor. 400% is an unverifiable industry myth |
| ST-0063 | HBR analysis of **2.24 million leads**, 7x more likely to qualify | The study audited **2,241 firms**. Off by 1,000x. HBR 2011, B2B tech, not real estate |
| ST-0067 | 68% of sellers / 52% of buyers find their agent by referral | **43% of buyers, 37% of sellers** |
| ST-0029 | ~70% of buyers interview only one agent | Not on the page at all |
| ST-0020, ST-0026 | 24-hour feedback window; confirm appointment before travel | Neither claim is on the page. Page is July 2025 |
| ST-0064 | 44% of agents give up after one follow-up | Not on the page |
| ST-0028 | Respect the time because the owner may be returning | Page is about buyers lingering between showings. 2023 |
| ST-0016 | NAR responsiveness ranking | Same page already disproved for ST-0002 |
| ST-0025 | Chicago home takes ~47 days | Same page already disproved for ST-0011: it is a **29-51 day range** |

Downgraded to `receipt: needed`, each carrying the finding in its `claim` field.
The numbers were not deleted. A writer who reaches for one now reads why it cannot
be spoken.

## The partials, and what they became

Nine were right but cited wrong, and survived with corrections:

- **ST-0010, ST-0050** cited 765 ILCS 77/**35**, which carries the form (24 items,
  not the banked 23) but no remedy. The remedy is **77/55**, now verified and
  quoted: actual damages and court costs, with attorney's fees at the court's
  discretion -- "may award," not automatic.
- **ST-0052** cited 12 CFR 1024.14 for penalties it does not contain. The penalties
  are **12 U.S.C. 2607(d)**: fine up to $10,000, up to a year, and treble the
  charge paid. Now verified and quoted.
- **ST-0013, ST-0055** cited the case-interpretations page, which carries neither
  the Article 15 text nor the social-media language. Both live in the 2026 Code:
  **SOP 15-2** covers statements made "by technological means (e.g., the Internet)."
- **ST-0032** was right but sourced to a referral marketplace's blog. Re-sourced to
  the **2024 IRC** itself.
- **ST-0049** keeps only the NAR RCI figure (18% of buyers waive, September 2024).
  The **$11,222 does not exist on the page**; the 86% and $14,000 are real but
  trace to Porch.com and are marked not-for-camera.
- **ST-0056** keeps 28% and 49%/32%. The headline **82% could not be found** and
  appears to have been derived by adding the veterans' two figures.
- **ST-0014** keeps the 88%. The paired **12% traces to a mortgage lender's blog**,
  not NAR.
- **ST-0030** was pointed at a DataDigest article that does not carry its figures.
  Re-sourced, and "mostly under $25,000" corrected to **57%**.

Two more went to `needed`: **ST-0034** (a vendor's own study of its own product,
no sample size) and **ST-0065** (two hops from primary, no methodology at either).
**ST-0027** could not be checked -- stlrealtors.com 403s every fetch -- and Rule 1
does not let an unconfirmed figure read as confirmed.

## The guardrail was poisoned too

`receipt_cautions` exists to stop known-bad numbers. **Five of its seven entries
pointed writers at figures this audit killed** -- it was telling them to replace the
myth with "44% quit after one follow-up (JustCall)," "roughly 70% interview only one
agent (NAR)," "88%/12%," and the Redfin photo figures. All five `say_instead` fields
now say the replacement is dead and no sourced substitute exists yet.

A list of known-bad numbers is only as good as the numbers it recommends instead.

## What stops it recurring

`scripts/stupid_things.py` now gates receipts at intake and can run the same gate
backwards over the bank:

```bash
python3 scripts/stupid_things.py receipt-check    # exit 13 = a banked receipt would be refused today
python3 scripts/tests/test_receipt_gate.py        # 25 cases, offline
```

A receipt may only be born `confirmed` if its host is somewhere Rule 1 actually
accepts (`RECEIPT_SOURCE_ALLOW`) and it records `published`, the source's real
publication date, agreeing with the year on the receipt. Anything else is
downgraded to `needed` and says why. A host can be added to the allowlist
deliberately -- that is how the IRC got in -- but never by accident.

## The state now

| | Before | After |
|---|---:|---:|
| Confirmed receipts | 39 | 17 |
| Need a receipt | 30 | 52 |
| Ready to script with a confirmed receipt | 32 | 14 |
| Available angles | 60 | 60 |

**Availability did not move**, because it is counted in angles, not receipts. The
lane keeps producing at the same rate; the scripts just run the scene and the swap
without a number, which is what the NEEDS RECEIPT posture was always for.

## The rule this leaves behind

A `confirmed` receipt is a claim about a page someone opened. Fourteen of the
nineteen failures would have been caught by opening the page once. The bank is a
shortlist, not a clearance -- re-verify at build time, every path, every time.
