# Stupid Things Realtors Do: the bank

Standing candidates for the **Stupid Things Realtors Do** video lane. The machine-readable
bank is [`stupid-things.json`](stupid-things.json); everything below the marker is generated
from it by `scripts/stupid_things.py render`. This top half is the charter and is
hand-written.

**These are candidates, not scripts.** Nothing here ships without re-verification at build
time (universal Rule 1). A receipt that was right in June may be wrong in October.

---

## What this lane is, and why it is not The Take

A short video where D.J. names a specific thing agents do that is bad for the client or bad
for the deal, and hands over the exact thing to do instead.

The Take ([`take-standard.md`](../docs/series/take-standard.md)) requires a **who profits**
beat, which is why its bank is a list of *beliefs* with an incentive behind each one. This
lane is *behavior*. Nobody is making money off an agent who does not return a call. The take
standard names that gap itself, in its note on hook shapes 5 and 6, and says a hook with no
real beat 2 either finds one or ships as a gated Value Giveaway. This lane is the third
option, and it is ungated.

| | The Take | Stupid Things Realtors Do |
|---|---|---|
| Subject | A belief agents were taught | A behavior agents perform |
| Beat 2 | Who profits from the belief | Who pays for the behavior |
| Bank | [`sacred-cows.md`](sacred-cows.md) | this file |
| Receipt | Required | Required |
| Swap | Required | Required |
| Gate | Never | Never |

**Brokerage economics stays out of both.** Splits, fees, support, and training are Broker
Problems. If a candidate is really about what a brokerage charges, it belongs there.

---

## Angles: how the same practice runs more than once

D.J.'s rule, 2026-08-13: **the same topic can run again as long as there is a genuinely new
angle on the solution.** That is the whole reason this bank is structured the way it is.

An **angle** is a distinct take on the *fix*, not on the practice. Each entry carries a list
of them. An angle is `open` until a script spends it, then it is `used` forever.

```
available = practices with at least one open angle
```

- **Target size: 20 available.**
- **Refill trigger: 5.** When availability hits five, the refill routine runs and tops the
  bank back to twenty, by finding new practices **and** by banking fresh angles on practices
  already here.
- A practice with every angle spent is not dead. It is waiting for a new angle.

**What does not count as a new angle.** A reword. "Say the honest number first" and "lead
with the real price" are one angle wearing two coats, and `stupid_things.py intake` refuses
the second one. A new angle changes *what the viewer does on Monday*, not the sentence
describing it. The clearest test: if both angles produce the same closing instruction, it is
one angle.

## What each entry carries

| Field | What it is | Why it matters |
|---|---|---|
| `practice` | The bad behavior, named flat | The thing the video indicts |
| `looks_like` | The vivid, recognizable scenario | **Act 2, pre-written.** The single most reusable field: the scene survives every angle the practice ever runs |
| `receipt` | Named source, year, URL, the exact claim | `needed` until sourced. Never invented |
| `angles[]` | `angle` (the take on the fix), `swap` (the physical do-this), `hook` (a spoken first line) | One angle per script. The hook is a starting point, sharpened at build time |
| `target` | `sideways` or `self` | Who the friction points at |
| `family` / `category` | The four families and their sub-sections | Drives category spread in `pick` |
| `sightings[]` | Where the complaint was observed | Proves it recurs. **Not a receipt** |

## Duplicates: what the script can and cannot do

**It catches reworded angles. It cannot catch the same practice described in different words.**
This is a real limit, not a tuning problem. "Photographing a client's largest asset on a phone"
and "dark, blurry, badly composed iPhone photos on the MLS" are the same practice and score
**0.14**, which is indistinguishable from noise.

So auto-merge only fires at 0.75 and above. Between 0.30 and 0.75 the entry is **created and
flagged** for a human call, because a wrong merge buries an entry where nobody looks again,
while a duplicate is visible and fixable. Review with `dupes`, fix with `merge`.

The first bulk intake produced eight real duplicates. `dupes` surfaced four; the other four had
to be caught by reading. **Every refill needs that read.**

---

## The qualifying test

A candidate is only in this lane if it clears all five:

1. **Is it a behavior, not a belief?** If someone taught it to them and someone profits from
   it staying true, it is a Take. Send it there.
2. **Does somebody actually pay for it?** A client, a deal, the agent on the other side. If
   the only cost is aesthetic, it is a preference, not a stupid thing.
3. **Is there a receipt, or can there be one?** A named source with a year, a state
   enforcement docket, a regulator's own guidance, or a documented complaint category.
   Entries ship with `receipt.status = "needed"` and they do not go on camera until it is
   cleared.
4. **Is there a swap?** An indictment with no fix is a rant, and it is the fastest way for
   this lane to cost more brand than it earns.
5. **Does it stand with the good agent?** Never at newer or struggling agents. Inexperience
   is not the target; behavior and hypocrisy are.

---

## Target class: sideways beats at-the-viewer

Every entry is tagged `target: sideways` or `target: self`.

- **`sideways`** points at the agent on the *other* side of the deal. The good agent watching
  is the wronged party, not the accused. They are vindicated, they comment, and D.J. holding
  a public standard is a recruiting asset. This is the lane's default and the take standard
  argues for it directly.
- **`self`** points at the viewer's own behavior. Harder, and it costs the viewer something
  to agree, which is what earns a follow rather than a like. Run it, but not as the default.

`stupid_things.py pick` alternates the two so the lane never becomes all-confessional or
all-finger-pointing. STUPID-001 was a `self`; the open A/B is whether `sideways` wins on
comments and sends.

---

## Heat, and the line that does not move

**Default 3.5. One heat 4 per week across the entire publishing schedule** (Rule 9.2), and
that slot is shared with every other series. Check the hook-cadence banner in the day's news
brief before drafting a 4.

**Heat 5 is banned outright.** Never name a brokerage, franchise, team, coach, coaching
program, software product presented as the villain, or an identifiable individual agent. Not
in the script, not in the captions.

**The rule is "no identifiable target," not "no name typed."** A knowing wink carries the same
exposure with less punch. Go maximally specific about the *behavior* while the target stays a
category. Ship test: could a viewer name one company with confidence? If yes, rewrite.

**Legal-exposure entries carry the highest evidence burden in the bank.** The "if you're still
doing X, you're going to get sued" shape needs the actual statute, the live litigation, or the
real enforcement docket. Say the exposure, never predict the verdict. Entries carrying a
`flag` say so.

---

## Where the sightings come from

The refill routine's working source list, and why it is not "scour Reddit." Reddit is not
directly reachable from the routine's tools: `WebFetch` is blocked on reddit.com and
`WebSearch` barely indexes subreddit threads. The sources below are the ones that actually
return, and two of them are better than Reddit anyway because they are already verified.

| Source | What it yields | Receipt grade |
|---|---|---|
| **State license enforcement dockets** (IDFPR, NV RED, CA DRE, CO DRE) | Adjudicated bad practice with case numbers | Highest. Already proven |
| **Regulator guidance and bulletins** (TREC, LLR, DRE notifications) | The behavior a regulator felt the need to warn about | High |
| **E&O carrier and real estate attorney posts** | The complaints that most often become litigation | Medium. Named category, rarely a number |
| **Consumer agent reviews** (Redfin, Trustpilot) | Verbatim client complaints, unfiltered | Low as a receipt, high as a sighting |
| **Consumer press and advice columns** | What the public is being told to watch for | Medium |
| **Industry commentary** (Substack, BAM, Inman, forum threads via Google) | Agent-on-agent critique, the sideways vein | Low as a receipt, high as a sighting |

**A sighting is not a receipt.** A sighting proves the complaint recurs. A receipt is a named
source with a year that supports the specific claim on camera. An entry with ten sightings and
no receipt still cannot ship a number.

**Vendor blogs are a trap.** Half the "bad photos cost sellers $4,200" material is published
by companies selling photography. Entries sourced that way carry a `flag` and the number stays
out until it traces to primary research.

---

## The four-beat reel this bank is built for

D.J.'s formula, and the reason every entry carries the fields it does. A complete 30-45 second
reel is already sitting in each entry:

```
HOOK          the angle's `hook` -- spoken, because captions.ai builds captions from audio
LOOKS LIKE    the entry's `looks_like` -- the recognizable scene, Act 2
WHY IT COSTS  the `receipt` -- the sourced number, said once
THE FIX       the angle's `swap` -- the do-this-instead standard
```

The build pass still runs all four passes over it. The bank hands over a strong draft, not a
finished script: the hook gets sharpened to the day, the receipt gets re-verified, and the
loop-back close gets written fresh.

## Series buckets (D.J., 2026-08-13)

The same bank feeds four different audiences depending on which entries get grouped. Filter by
`family` and `target`:

| Bucket | Pulls from | What it does |
|---|---|---|
| **"Don't be THAT agent"** | Responsiveness and showings, plus co-op etiquette | Lands with agents. Quietly recruits the good ones who are tired of working with the bad ones |
| **"Red flags when hiring an agent"** | Trust, ethics and conflicts, plus the pushy and ghosting entries | Consumer-facing reach. Positions D.J. as the honest pro |
| **"Why agents fail, and it's not the market"** | Competence, preparation and systems | Pure recruiting content |
| **"Same MLS, different results"** | The tools-vs-work entry plus the photo and pricing entries | The value argument, without a commission conversation |

**Chicago-specific proof points to lean on**, since local beats national for a Chicago
recruiting audience: the 89-vs-123-day photo study, the Illinois disclosure statute
(765 ILCS 77), Illinois dual-agency law (225 ILCS 454/15-45), and the ~47-day Chicago
days-on-market figure.

## Using the bank

```bash
python3 scripts/stupid_things.py health          # exit 10 = refill due
python3 scripts/stupid_things.py pick --count 5  # the shortlist
python3 scripts/stupid_things.py log --id ST-0001 --script scripts/stupid-things/...md
```

Say **"stupid things"** in Claude Code to see the shortlist, **"stupid things 2"** to build
that one through the four passes. Claude re-verifies the receipt at build time regardless of
what the bank says. The bank is a shortlist, not a clearance.

Full chain, refill contract, and the routine's job:
[`../docs/automation/stupid-things-bank.md`](../docs/automation/stupid-things-bank.md).

---

<!-- BANK:START -->

_Generated by `scripts/stupid_things.py render` on 2026-08-13. Do not hand-edit this region; edit `data/stupid-things.json`._

**60 available** of 69 practices (target 20, refill at 5).

### After the close

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0014 | Disappearing the day after closing and never contacting the client again | self | NAR via Stylograph 2026 | 4 | 1 |

### Agent-to-agent cooperation

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0020 | Never replying to showing feedback requests, leaving the seller in the dark | sideways | NorthstarMLS 2026 | 1 | 1 |
| ST-0021 | Calling another agent without identifying yourself or naming the listing | sideways | **needed** | 1 | 0 |
| ST-0022 | Only texting during negotiations and refusing to get on the phone | sideways | **needed** | 1 | 0 |
| ST-0023 | Sitting on a submitted offer with no acknowledgment of receipt | sideways | OneKey MLS 2026 | **spent** | 1 |
| ST-0024 | Setting an offer deadline and never telling the other agents the seller already accepted | sideways | NAR 2026 Code of Ethics, Standard of Practice 1-15 2026 | 1 | 1 |

### Co-op etiquette

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0068 | Leaning on the agent across the deal to quarterback your side of the transaction | sideways | **needed** | 1 | 0 |
| ST-0069 | Turning the cooperating agent into your unpaid errand service | sideways | **needed** | 1 | 0 |

### Confidence and respect

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0054 | Leaking your own client's bottom line or motivation to the other side | sideways | **needed** | 1 | 0 |
| ST-0055 | Badmouthing the other agent or the seller in front of your own buyers | sideways | NAR Code of Ethics Article 15 2026 | **spent** | 2 |

### Conflicts of interest

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0051 | Steering buyers toward the agent's own listings or higher-commission homes | sideways | Illinois 225 ILCS 454/15-45 2026 | 1 | 1 |
| ST-0052 | Taking undisclosed kickbacks from recommended inspectors, lenders, or title companies | sideways | RESPA Section 8, 12 CFR 1024.14 2026 | 1 | 2 |
| ST-0053 | Double-ending by talking an unrepresented buyer out of getting their own agent | sideways | Illinois 225 ILCS 454/15-45 2026 | 1 | 1 |

### Contract and paperwork craft

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0059 | Submitting sloppy offers with blank lines, outdated forms, and missing addenda | self | **needed** | 1 | 0 |
| ST-0060 | Not being able to explain the contract you wrote without reading it | self | **needed** | 1 | 0 |
| ST-0061 | Writing a full-price offer for a buyer with no pre-approval or proof of funds | self | **needed** | 1 | 0 |
| ST-0062 | Showing up to the closing table unprepared and flailing in front of the client | self | **needed** | 1 | 0 |

### Cutting corners on protection

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0049 | Talking buyers into waiving the inspection to make the offer look cleaner | self | Preferred Inspections 2026 | 1 | 2 |
| ST-0050 | Coaching a seller to hide a known defect off the disclosure form | sideways | Illinois Residential Real Property Disclosure Act, 765 ILCS 77 2026 | **spent** | 2 |

### Duty and disclosure

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0004 | Deciding an offer is too weak to bother presenting to the seller | sideways | **needed** | 1 | 2 |
| ST-0009 | Rushing a client through signing so they don't have time to understand what they're agreeing to | sideways | **needed** | 1 | 2 |
| ST-0010 | Leaving a material property fact out of the disclosure and hoping nobody asks | sideways | Illinois Residential Real Property Disclosure Act, 765 ILCS 77 2026 | 2 | 4 |

### Lead response and follow-up

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0063 | Taking four hours to respond to a new lead, then blaming the lead quality | self | Harvard Business Review, analysis of 2.24 million leads, via Motarme 2026 | 1 | 1 |
| ST-0064 | One-and-done follow-up, marking a lead dead after a single unanswered text | self | JustCall 2026 | 1 | 1 |
| ST-0065 | Buying more leads to fix what is actually a follow-up problem | self | JustCall 2026 | 1 | 0 |

### Manufactured pressure

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0046 | Manufacturing false urgency with a deadline that does not exist on paper | sideways | **needed** | 1 | 0 |
| ST-0047 | Pushing buyers to bid above the number they set when they were calm | self | **needed** | 1 | 0 |
| ST-0048 | Guilting or insulting a client who pushes back on your advice | sideways | **needed** | 1 | 0 |

### Market competence

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0056 | Not knowing basic factual things about the neighborhood you sell in | self | NAR via HousingWire 2026 | 1 | 1 |
| ST-0057 | Giving wildly wrong price estimates, property after property | self | Relitix via Inman 2026 | 1 | 1 |
| ST-0058 | Emailing the disclosures with sign where highlighted and never walking the client through them | sideways | **needed** | 1 | 0 |

### Marketing and strategy

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0036 | Throw it on the MLS and pray, with no staging, no marketing plan, and no launch | self | NAR Profile of Home Buyers and Sellers 2026 | 1 | 0 |
| ST-0037 | Sitting on the pending or sold status change to keep the listing looking active | sideways | **needed** | 1 | 0 |

### Marketing the listing

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0005 | Photographing a client's largest asset on a phone, in bad light, and putting it in the MLS | self | NAR and Redfin 2026 | 2 | 5 |
| ST-0006 | Writing 'Beautiful home, must see!' as the entire MLS description | self | NAR Profile of Home Buyers and Sellers 2026 | 2 | 3 |

### Money and licensing

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0007 | Sitting on earnest money instead of depositing it into the trust account on time | sideways | **needed** | 1 | 2 |
| ST-0008 | Practicing on a lapsed license, or letting sponsorship lapse and working anyway | sideways | **needed** | 1 | 2 |

### Offers and negotiation

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0012 | Telling buyer's agents there are multiple offers when there are none | sideways | **needed** | 1 | 0 |
| ST-0013 | Running down the agent on the other side of the deal in front of your own client | sideways | NAR Code of Ethics Article 15 2026 | 2 | 2 |

### Personal brand and digital presence

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0042 | Posting nothing but Just Listed, Just Sold, and call me graphics | self | Placester 2026 | 1 | 1 |
| ST-0043 | Using a headshot that is ten years and twenty pounds out of date | self | **needed** | 1 | 0 |
| ST-0044 | Running inconsistent branding across the website, Instagram, and business card | self | **needed** | 1 | 0 |
| ST-0045 | Having a dead or broken digital presence when the client Googles you | self | NAR and Placester 2026 | 1 | 0 |

### Pricing and listing intake

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0001 | Taking a listing at a price the comps don't support, because another agent already agreed to it and you don't want to lose the appointment | self | Realtor.com 2026 | 2 | 2 |
| ST-0015 | Walking into a listing appointment with a CMA you pulled that morning and never read | self | **needed** | 1 | 0 |

### Pricing and listing-appointment integrity

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0038 | Overpricing to win the listing, then hammering the seller for cuts every thirty days | self | Zillow 2026 | **spent** | 1 |
| ST-0039 | Overpromising buyers already waiting in order to lock up the listing | sideways | **needed** | 1 | 0 |
| ST-0040 | Panic-cutting your own commission the moment a seller pushes back on it | self | **needed** | 1 | 0 |
| ST-0041 | Being unable to explain the difference between the tools you have and the work you do | self | NAR Profile of Home Buyers and Sellers 2026 | 1 | 0 |

### Responsiveness and communication

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0002 | Going radio silent after the contract is signed, as if the job ended at acceptance | sideways | NAR 2026 | 2 | 4 |
| ST-0003 | Not returning the buyer's agent's call on a live submitted offer | sideways | OneKey MLS 2026 | 2 | 3 |

### Showings and access

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0011 | Listing a property with no showing instructions, no working lockbox, and a phone number nobody answers | sideways | Virtuance 2026 | 2 | 3 |
| ST-0025 | Call agent to show with no lockbox, turning a showing into a multi-day ordeal | sideways | Virtuance 2026 | **spent** | 1 |
| ST-0026 | Not confirming showings, so buyers get dragged across town to a locked door | sideways | NorthstarMLS 2026 | 1 | 0 |
| ST-0027 | Showing up late or no-showing and blowing up everyone else's schedule | sideways | St. Louis REALTORS 2021 | 1 | 1 |
| ST-0028 | Overstaying the showing window while the next agent and their buyers wait | sideways | Selling CF 2026 | 1 | 1 |
| ST-0029 | Taking days to schedule a showing while the listing sells to somebody faster | self | NAR via Virginia REALTORS 2025 | 1 | 1 |
| ST-0030 | The part-timer who hides the day job and cannot keep pace with the transaction | self | HousingWire and Colibri 2026 | 1 | 2 |

### Systems and sphere

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0066 | Running the business out of the Contacts app, a legal pad, and memory | self | **needed** | 1 | 2 |
| ST-0067 | The secret agent who is too embarrassed to tell their own network what they do for a living | self | NAR 2025 via BAM 2025 | 1 | 1 |

### The listing itself

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0031 | Dark, blurry, badly composed iPhone photos on the MLS | self | NAR and Redfin 2026 | **spent** | 3 |
| ST-0032 | Calling a windowless or closetless room a bedroom in the listing | sideways | IRC via ListWithClever and HomeLight 2026 | 1 | 2 |
| ST-0033 | Submitting an incomplete MLS listing with no room sizes, no remarks, and no HOA information | self | NAR Profile of Home Buyers and Sellers 2026 | **spent** | 1 |
| ST-0034 | Over-Photoshopping listing images so the house is unrecognizable in person | self | Virtuance eye-tracking study 2026 | 1 | 1 |
| ST-0035 | Reusing old or expired-listing photos instead of shooting the house fresh | self | **needed** | 1 | 0 |

### The slow fade

| ID | Practice | Target | Receipt | Open angles | Sightings |
|---|---|---|---|---|---|
| ST-0016 | The pre-contract superstar who disappears after the client signs | self | NAR 2026 | **spent** | 1 |
| ST-0017 | Vanishing during the week before closing | self | Redfin 2026 | 1 | 1 |
| ST-0018 | Ghosting on loose ends after the keys change hands | self | **needed** | **spent** | 0 |
| ST-0019 | Putting the entire follow-up burden on the client with 'I'll let you know if anything comes up' | self | **needed** | 1 | 0 |

### Rejected, never re-bank

- **Waiting until week six to bring up a price reduction on a stale listing** Not rejected on merit. Owned by NF-067 (Inside the Industry), which already works the price-cut timing lane with Denver Q2 data. Kept out so the two lanes do not ship the same argument twice. Revisit after NF-067 posts.
- **Agents who are bad at their job because they are new or inexperienced** Punching down. The lane's floor: hypocrisy and bad behavior are the targets, inexperience is not. Never bank a variant of this, however it is phrased.
- **Agents who are stupid, lazy, or bad people** Character attacks, not behavior. Rule 9.4: the cohort name cannot be the insult, and friction points at the practice, never at the person. A candidate phrased as a character judgment gets rewritten as the behavior or dropped.

<!-- BANK:END -->
