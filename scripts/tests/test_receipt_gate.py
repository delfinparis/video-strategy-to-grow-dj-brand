#!/usr/bin/env python3
"""Harness for the receipt source/year gate in stupid_things.py.

    python3 scripts/tests/test_receipt_gate.py

No dependencies, no network. Calls the real screen_receipt() and
receipt_problems() bodies.

Why this file exists: on 2026-09-10 all 39 confirmed receipts in the bank were
re-checked against their own cited pages and 19 were false. Every failure was
one of two moves -- the number came from a company selling something, or the
year on the receipt was the year it was banked rather than the year the source
was published. The gate refuses both at intake. These cases are the proof it
refuses them, and the proof it does not refuse the good ones.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import stupid_things as st  # noqa: E402

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("  PASS  " + name)
    else:
        FAIL += 1
        print(f"  FAIL  {name}  -> {detail}")


def rec(url, year=2026, published="2026-01-01", claim="a figure", status="confirmed"):
    r = {"status": status, "source": "src", "year": year, "url": url, "claim": claim}
    if published is not None:
        r["published"] = published
    return r


def screen(r, cautions=None):
    return st.screen_receipt(r, cautions or [])


print("\nA. A number from someone selling something cannot be confirmed")
for host, label in [
    ("https://placester.com/real-estate-marketing-academy/tips", "marketing software vendor"),
    ("https://justcall.io/blog/lead-conversion.html", "call software vendor"),
    ("https://www.virtuance.com/blog/eye-tracking-study/", "photography vendor grading itself"),
    ("https://listwithclever.com/real-estate-blog/bedroom/", "referral marketplace"),
    ("https://www.stylograph.ai/blog/retention-gap", "AI content blog"),
    ("https://nowbam.com/how-buyers-find-agents/", "trade aggregator"),
]:
    out, note = screen(rec(host))
    check(f"{label} downgraded", out["status"] == "needed" and "allowlist" in (note or ""),
          f"{out['status']} / {note}")

print("\nB. The number is never deleted, only made unspeakable")
out, note = screen(rec("https://placester.com/x", claim="71% prefer social agents"))
check("original claim preserved", out.get("original_claim") == "71% prefer social agents",
      str(out.get("original_claim")))
check("and the reason travels with it", "allowlist" in out.get("caution", ""),
      out.get("caution", ""))

print("\nC. The year must be the source's, not the year it was banked")
out, note = screen(rec("https://www.redfin.com/blog/photos/", year=2026, published="2019-06-03"))
check("THE REDFIN CASE: 2019 article banked as 2026 is refused",
      out["status"] == "needed" and "disagrees" in (note or ""), f"{out['status']} / {note}")
out, note = screen(rec("https://hbr.org/2011/03/the-short-life-of-online-sales-leads",
                       year=2026, published="2011-03-01"))
check("THE HBR CASE: 2011 study banked as 2026 is refused",
      out["status"] == "needed", f"{out['status']} / {note}")
out, note = screen(rec("https://www.nar.realtor/x", year=2026, published=None))
check("no publication date at all is refused",
      out["status"] == "needed" and "published" in (note or ""), f"{out['status']} / {note}")

print("\nD. Good receipts still get through")
for url in [
    "https://www.nar.realtor/about-nar/governing-documents/code-of-ethics/2026-code",
    "https://www.law.cornell.edu/uscode/text/12/2607",
    "https://codes.findlaw.com/il/chapter-765-property/il-st-sect-765-77-55/",
    "https://www.housingwire.com/articles/nar-2026-member-profile-experience/",
    "https://www.inman.com/2026/05/14/new-agents-say-how-theyre-surviving/",
    "https://www.consumerfinance.gov/rules-policy/regulations/1024/14/",
    "https://www.zillow.com/research/overpricing-impacts-time-market-12476/",
]:
    out, note = screen(rec(url, year=2026, published="2026-05-08"))
    check(f"accepted: {url.split('/')[2]}", out["status"] == "confirmed", f"{out['status']} / {note}")

print("\nE. The gate does not touch what it is not for")
out, note = screen(rec("https://placester.com/x", status="needed"))
check("an already-needed receipt is left alone", out["status"] == "needed" and note is None,
      f"{out['status']} / {note}")
out, note = screen({}, [])
check("an empty receipt is left alone", out == {} and note is None, str(out))

print("\nF. A named caution still fires, and the gate runs before it")
cautions = [{"label": "87% of agents fail", "reason": "industry legend",
             "say_instead": "use the Relitix figure",
             "match_terms": ["87% of agents"]}]
out, note = screen(rec("https://www.nar.realtor/x", claim="87% of agents fail in year one"), cautions)
check("caution catches the named number on an otherwise-clean source",
      out["status"] == "needed" and "87% of agents" in (note or ""), f"{out['status']} / {note}")
out, note = screen(rec("https://placester.com/x", claim="87% of agents fail"), cautions)
check("the source gate wins when both apply", "allowlist" in (note or ""), str(note))

print("\nG. Two stats in one claim is a warning, not a refusal")
probs = st.receipt_problems(rec("https://www.nar.realtor/x", claim="88% would, only 12% do"))
check("warned", any(s == "warn" and "separate figures" in m for s, m in probs), str(probs))
check("not refused", not any(s == "hard" for s, m in probs), str(probs))
audited = rec("https://www.nar.realtor/x", claim="88% would, only 12% do")
audited["verified_check"] = {"date": "2026-09-10", "result": "confirmed with corrections"}
check("an audited receipt is not re-warned about its own findings prose",
      not any(s == "warn" for s, m in st.receipt_problems(audited)),
      str(st.receipt_problems(audited)))

print(f"\n{PASS} passed, {FAIL} failed\n")
sys.exit(1 if FAIL else 0)
