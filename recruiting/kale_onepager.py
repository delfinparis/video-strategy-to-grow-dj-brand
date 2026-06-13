#!/usr/bin/env python3
"""
Kale Realty one-page recruiting PDF for experienced producers.
Economics-forward. Cap is the hero. Generates a print/email-ready Letter PDF.

Brand kit scraped from joinkale.com:
  logo  = recruiting/kale_white_logo.png  (white "kale Realty" wordmark)
  olive = #303328 (primary)   navy = #002f66 (secondary)   coral = #f46942 (pop)

Run: python3 recruiting/kale_onepager.py
Out: recruiting/Kale-Realty-Agent-One-Pager.pdf
"""

import os
from fpdf import FPDF

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, "kale_white_logo.png")

# ---- Brand palette (scraped from joinkale.com) --------------------------
OLIVE = (48, 51, 40)       # #303328 primary, bands
NAVY = (0, 47, 102)        # #002f66 secondary, cap box + values
CORAL = (244, 105, 66)     # #f46942 pop accent
LIGHT = (245, 245, 245)    # #f5f5f5 row fill
CHARCOAL = (38, 43, 40)
GRAY = (112, 122, 114)
WHITE = (255, 255, 255)
OLIVE_TINT = (190, 193, 182)

# ---- Contact (FILL THESE IN) --------------------------------------------
CONTACT = {
    "name": "D.J. Paris",
    "title": "VP of Business Development, Kale Realty",
    "phone": "[ phone ]",
    "email": "[ email ]",
    "booking": "[ booking link ]",
    "website": "joinkale.com",
}

W, H = 215.9, 279.4  # US Letter mm
MX = 14              # left/right margin


def t(s):
    """latin-1 safe: strip glyphs the core fonts can't encode."""
    return (s.replace("—", "-").replace("–", "-")
             .replace("’", "'").replace("‘", "'")
             .replace("“", '"').replace("”", '"')
             .replace("·", "-"))


class OnePager(FPDF):
    def header(self):
        pass

    def footer(self):
        pass


def check(pdf, x, y, color=CORAL):
    pdf.set_draw_color(*color)
    pdf.set_line_width(0.8)
    pdf.line(x, y + 1.4, x + 1.3, y + 2.7)
    pdf.line(x + 1.3, y + 2.7, x + 3.4, y - 0.2)
    pdf.set_line_width(0.2)


def section_label(pdf, x, y, text):
    pdf.set_text_color(*NAVY)
    pdf.set_font("helvetica", "B", 10)
    pdf.set_xy(x, y)
    pdf.cell(0, 5, t(text))
    pdf.set_draw_color(*CORAL)
    pdf.set_line_width(0.6)
    pdf.line(x, y + 5.7, x + 22, y + 5.7)
    pdf.set_line_width(0.2)


def main():
    pdf = OnePager(orientation="P", unit="mm", format=(W, H))
    pdf.set_auto_page_break(False)
    pdf.set_margins(MX, 0, MX)
    pdf.add_page()

    # ===== HEADER BAND =====================================================
    pdf.set_fill_color(*OLIVE)
    pdf.rect(0, 0, W, 30, "F")
    pdf.set_fill_color(*CORAL)
    pdf.rect(0, 30, W, 1.0, "F")

    # white logo, vertically centered in the band
    pdf.image(LOGO, x=MX, y=8.5, h=13)

    pdf.set_text_color(*WHITE)
    pdf.set_font("helvetica", "I", 11)
    pdf.set_xy(W - 95 - MX, 10.5)
    pdf.cell(95, 6, t("Keep more of what you earn."), align="R")
    pdf.set_text_color(*OLIVE_TINT)
    pdf.set_font("helvetica", "", 7.5)
    pdf.set_xy(W - 95 - MX, 17)
    pdf.cell(95, 5, t("CHICAGO'S 100% COMMISSION BROKERAGE"), align="R")

    # ===== HERO ============================================================
    pdf.set_text_color(*CORAL)
    pdf.set_font("helvetica", "B", 9)
    pdf.set_xy(MX, 38)
    pdf.cell(0, 5, t("FOR EXPERIENCED PRODUCERS"))

    pdf.set_text_color(*CHARCOAL)
    pdf.set_font("helvetica", "B", 22)
    pdf.set_xy(MX, 43.5)
    pdf.cell(0, 11, t("A true 100% commission model,"))
    pdf.set_xy(MX, 53.5)
    pdf.cell(0, 11, t("with one of the lowest caps in Chicago."))

    pdf.set_text_color(*GRAY)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_xy(MX, 65.5)
    pdf.multi_cell(W - 2 * MX, 5.4, t(
        "Flat per-deal fees. No franchise fees. No surprise deductions. "
        "You pay a small flat fee per closing until you hit your cap, then "
        "every residential sale the rest of your year is yours."))

    # ===== CAP HIGHLIGHT ===================================================
    cap_y = 81
    pdf.set_fill_color(*NAVY)
    pdf.rect(MX, cap_y, W - 2 * MX, 28, "F")

    pdf.set_text_color(*CORAL)
    pdf.set_font("helvetica", "B", 38)
    pdf.set_xy(MX + 6, cap_y + 4.5)
    pdf.cell(58, 20, t("$6,000"))

    pdf.set_draw_color(255, 255, 255)
    pdf.set_line_width(0.3)
    pdf.line(MX + 66, cap_y + 6, MX + 66, cap_y + 22)

    pdf.set_text_color(*WHITE)
    pdf.set_font("helvetica", "B", 11)
    pdf.set_xy(MX + 72, cap_y + 6)
    pdf.cell(0, 5.5, t("Your total annual fee cap."))
    pdf.set_font("helvetica", "", 9.5)
    pdf.set_xy(MX + 72, cap_y + 12)
    pdf.multi_cell(W - 2 * MX - 78, 4.8, t(
        "After about 15 residential closings, the per-deal fee stops. Every "
        "sale the rest of your anniversary year is 100% yours. Resets each year."))

    # ===== THE NUMBERS (fee table) =========================================
    sec_y = 116
    section_label(pdf, MX, sec_y, "THE NUMBERS")

    rows = [
        ("Residential sales", "$400 flat per closing", "Capped at $6,000/yr, then $0"),
        ("Residential rentals", "80 / 20 split", "plus $15 per transaction"),
        ("Commercial sales", "90 / 10 split", "no transaction fee"),
        ("Commercial rentals", "90 / 10 split", "plus $15 per transaction"),
    ]
    ry = sec_y + 7
    rh = 10
    for i, (label, val, note) in enumerate(rows):
        if i % 2 == 0:
            pdf.set_fill_color(*LIGHT)
            pdf.rect(MX, ry, W - 2 * MX, rh, "F")
        pdf.set_text_color(*CHARCOAL)
        pdf.set_font("helvetica", "B", 11)
        pdf.set_xy(MX + 4, ry + 1.8)
        pdf.cell(60, 6, t(label))
        pdf.set_font("helvetica", "B", 11)
        pdf.set_text_color(*NAVY)
        pdf.set_xy(MX + 66, ry + 1.8)
        pdf.cell(48, 6, t(val))
        pdf.set_font("helvetica", "", 9)
        pdf.set_text_color(*GRAY)
        pdf.set_xy(MX + 118, ry + 2.1)
        pdf.cell(0, 6, t(note))
        ry += rh

    # ===== TWO COLUMNS: costs + included ==================================
    col_y = ry + 8
    colL = MX
    colR = MX + (W - 2 * MX) / 2 + 4

    section_label(pdf, colL, col_y, "MONTHLY & ANNUAL")
    cost_items = [
        ("$54 / mo", "Training, technology & support"),
        ("$249 / yr", "E&O insurance"),
        ("$0", "Franchise fees, ever"),
    ]
    cy = col_y + 8
    for amt, desc in cost_items:
        pdf.set_text_color(*NAVY)
        pdf.set_font("helvetica", "B", 12)
        pdf.set_xy(colL, cy)
        pdf.cell(26, 6, t(amt))
        pdf.set_text_color(*CHARCOAL)
        pdf.set_font("helvetica", "", 9.5)
        pdf.set_xy(colL + 27, cy + 0.6)
        pdf.cell(0, 5, t(desc))
        cy += 9.5

    section_label(pdf, colR, col_y, "WHAT'S INCLUDED")
    included = [
        "Custom IDX personal website",
        "Full CRM",
        "Premium dotloop",
        "Thousands of marketing assets",
        "Mentorship program (25+ mentors)",
        "Monthly cross-brokerage training",
        "AI prompt library (tapthis.co)",
    ]
    iy = col_y + 8
    pdf.set_font("helvetica", "", 9.8)
    for item in included:
        check(pdf, colR, iy)
        pdf.set_text_color(*CHARCOAL)
        pdf.set_xy(colR + 6, iy)
        pdf.cell(0, 5, t(item))
        iy += 7.4

    # ===== FOOTER BAND =====================================================
    fy = H - 30
    pdf.set_fill_color(*OLIVE)
    pdf.rect(0, fy, W, 30, "F")
    pdf.set_fill_color(*CORAL)
    pdf.rect(0, fy, W, 1.0, "F")

    pdf.set_text_color(*WHITE)
    pdf.set_font("helvetica", "B", 13)
    pdf.set_xy(MX, fy + 6)
    pdf.cell(0, 6, t("Let's talk about your move."))

    pdf.set_text_color(*OLIVE_TINT)
    pdf.set_font("helvetica", "B", 10)
    pdf.set_xy(MX, fy + 14)
    pdf.cell(0, 5, t(CONTACT["name"]))
    pdf.set_font("helvetica", "", 9)
    pdf.set_xy(MX, fy + 19)
    pdf.cell(0, 5, t(CONTACT["title"]))

    pdf.set_font("helvetica", "", 9)
    pdf.set_text_color(*WHITE)
    contact_line = "  |  ".join([CONTACT["phone"], CONTACT["email"], CONTACT["website"]])
    pdf.set_xy(W - 120 - MX, fy + 14)
    pdf.cell(120, 5, t(contact_line), align="R")
    pdf.set_xy(W - 120 - MX, fy + 19)
    pdf.cell(120, 5, t("Book a confidential conversation: " + CONTACT["booking"]), align="R")

    out = os.path.join(HERE, "Kale-Realty-Agent-One-Pager.pdf")
    pdf.output(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
