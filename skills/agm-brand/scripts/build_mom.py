# -*- coding: utf-8 -*-
"""Worked example: Minutes of Meeting on the brand component system.

Sample content only (a fictional meeting, safe to share). Copy this file, replace CONTENT
with the real minutes, and keep the structure. The structure is the one the
meeting-minutes-mom skill prescribes.

    python build_mom.py --out minutes.docx [--brand seafood|marine]
    soffice --headless --convert-to pdf minutes.docx
"""
import argparse

from brands import BRANDS, DEFAULT
from components import BrandDoc

CONTENT = dict(
    date="30 SEPTEMBER 2026",
    kind="Minutes of Meeting",
    ref="AGM-SMP-MOM-001",
    title="Sample Partner Briefing",
    subtitle_lead="Introductory discussion with ",
    subtitle_name="Sample Partner Ltd",
    intro=[
        "We met **Sample Partner Ltd** to understand how their **distribution "
        "platform** could carry our product, and what a first shipment would "
        "need.",
        "The partner is **free to join** for registered companies, and offers "
        "**deposit-backed financing** to buyers. This is fictional sample text "
        "that shows how the layout holds.",
    ],
    tiles=[("0%", "Joining fee", "Free to join"),
           ("20–30%", "Buyer deposit", "Financing option"),
           ("48–72 h", "Air freight", "Provider-dependent"),
           ("B2B", "Members only", "Companies only"),
           ("4", "Products", "Initial range")],
    headline=[
        "**Opportunity.** A low-cost channel to buyers who are already asking "
        "for the product, with optional financing.",
        "**Immediate action.** Register on the platform and confirm which "
        "products are permitted for import.",
    ],
    details=[
        ("Date", "Wednesday, 30 September 2026"),
        ("Time", "10:00 WIB (UTC+7)"),
        ("Format", "Online meeting with a screen-share demo"),
        ("Host", "Mr. Sample — the partner's local representative"),
        ("Minutes by", "Name of preparer"),
        ("Source", "Transcript of a 45-minute recording"),
    ],
    participants=[
        ("Our company", "Team lead + team", "Prospective supplier"),
        ("Sample Partner Ltd", "Mr. Sample", "Host; platform representative"),
        ("Regulator (TBC)", "Bapak Contoh", "Attended; did not respond in Q&A"),
    ],
    participants_note="Speaker labels in the transcript are unreliable; names "
                      "are taken from what was said and need checking.",
    objectives=["**Market access** — reaching buyers in the target market",
                "**Financing** — pre-sales and working capital",
                "**Regulatory entry** — registration and import rules"],
    discussion=[
        ("Can the platform help small suppliers get scale-up funding?",
         "Yes, through partner banks, subject to each bank's assessment. The "
         "main tool is **deposit-backed financing**: a 20–30% deposit, with "
         "the funding partner holding title until the goods are sold."),
        ("Does the platform insure shipments or guarantee quality?",
         "**No.** That sits in the buyer–seller agreement; the platform can "
         "arrange a provider and offers partner testing labs."),
        ("How can the platform help with registration?",
         "**Not answered.** The host proposed a session with the regulator."),
    ],
    takeaway=["The platform is a **channel, not a guarantee**: quality, "
              "insurance and registration remain our responsibility."],
    topic=("Platform terms", "What was said about fees and process",
           ["Parameter", "Detail", "Status"],
           [("Joining fee", "None for registered companies", "TBC"),
            ("Financing", "Deposit-backed; partner bank decides", "TBC"),
            ("Freight", "Provider-dependent, about 48–72 hours by air", "TO DO")],
           [50, 92, 28]),
    opportunity=(["Workstream", "What the partner provides", "Relevance"],
                 [("Buyer matching", "Introductions to registered buyers", "HIGH"),
                  ("Financing", "Deposit-backed funding", "MEDIUM"),
                  ("Logistics", "Verified freight and warehouse partners", "LOW")],
                 [42, 98, 30]),
    risks=[("Some products may not be permitted", "HIGH",
            "Check each product against the import list first"),
           ("Funding need is not yet defined", "MEDIUM",
            "Prepare a one-page funding brief"),
           ("Unclear names in the transcript", "LOW",
            "Check against the chat log and the host's minutes")],
    actions=[("A1", "Register on the platform; prepare company documents", "Us", "TBC", "OPEN"),
             ("A2", "Send a product profile for buyer matching", "Us", "TBC", "OPEN"),
             ("B1", "Circulate the official minutes", "Mr. Sample", "TBC", "PENDING"),
             ("B2", "Arrange a session with the regulator", "Mr. Sample", "TBC", "PENDING")],
    immediate="**Immediate action:** register on the platform and confirm "
              "product eligibility in parallel.",
    agenda=["Buyer demand: products, grades, volumes, price range",
            "Quality standards and partner-lab testing",
            "Investor introductions: what investors need from us"],
    phases=[("Briefing", "Done — 30 Sep 2026"), ("Register", "Supplier verification"),
            ("Eligibility", "Products confirmed"), ("Match", "Samples and pricing"),
            ("First order", "Contract and shipment")],
    review="These minutes reflect the key points discussed and the follow-up "
           "actions agreed. Send corrections or additions to the preparer "
           "within five (5) working days of issue. Distribution: internal.",
    verify=["The transcript starts mid-meeting; the opening presentation is "
            "not reflected here.",
            "Names of the regulator and the co-organiser need confirming.",
            "One figure was stated without a currency."],
    prepared=dict(label="Minutes prepared by", name="Name of preparer"),
)


def build(out, brand_key=DEFAULT, C=CONTENT):
    brand = BRANDS[brand_key]
    d = BrandDoc(brand, C["kind"], C["title"], C["date"])
    # ------------------------------------------------------------ page 1 --
    d.masthead()
    d.title_block("%s  ·  %s  ·  v0.9 DRAFT" % (C["kind"].upper(), C["ref"]),
                  C["title"], C["subtitle_lead"], C["subtitle_name"])
    d.intro(C["intro"])
    d.tiles(C["tiles"])
    d.callout("Headline for management", C["headline"])
    d.page_break()
    # ------------------------------------------------- details / key talk --
    d.band("Meeting details", "Who, when and why", first=True)
    d.kv(C["details"])
    d.label("Participants")
    d.data_table(["Organisation", "Name", "Role / capacity"], C["participants"],
                 [55, 45, 70])
    d.note(C["participants_note"])
    d.label("Meeting objective")
    d.bullets(C["objectives"])

    d.page_break()
    d.band("Key discussion", "Questions raised and positions given", first=True)
    for q, a in C["discussion"]:
        d.item(q, "Position given", a)
    d.callout("Key takeaway", C["takeaway"], before=12)

    # ------------------------------------------------------------- topics --
    t, sub, hdr, rows, widths = C["topic"]
    d.band(t, sub)
    d.data_table(hdr, rows, widths, marks=(2,), align=["l", "l", "c"])
    d.band("Opportunity for us", "Preliminary view")
    hdr, rows, widths = C["opportunity"]
    d.data_table(hdr, rows, widths, marks=(2,), align=["l", "l", "c"])
    d.note("Relevance ratings are a preliminary view and need management review.")
    d.band("Considerations & risks", "What could stop a first shipment")
    d.data_table(["Consideration", "Impact", "Proposed mitigation"],
                 [(a, b, c) for a, b, c in C["risks"]], [72, 24, 74],
                 marks=(1,), align=["l", "c", "l"])

    # ---------------------------------------------------- actions / steps --
    d.band("Action items", "A = us  ·  B = counterparty")
    d.data_table(["No.", "Action", "Owner", "Target", "Status"], C["actions"],
                 [14, 84, 30, 18, 24], marks=(4,),
                 align=["l", "l", "l", "l", "c"])
    d.band("Next steps", "Immediate action and roadmap")
    d.para(C["immediate"], before=6)
    d.label("Agenda for the next discussion")
    d.numbered(C["agenda"])
    d.roadmap(C["phases"], done=1)

    # ---------------------------------------------------------- approval --
    d.band("Review & approval", "Corrections within five working days")
    d.para(C["review"], before=6)
    p = C["prepared"]
    d.sign_row([("Prepared by", p["name"], BRANDS[brand_key].name),
                ("Reviewed by", "", "Management"),
                ("Approved by", "", "Management")])
    d.callout("Items to verify before issue (v1.0)", C["verify"], before=12)
    c = BRANDS[brand_key].contact
    d.contact_panel(p["label"], p["name"],
                    line2=[BRANDS[brand_key].name] + ([c["address"]] if c.get("address") else []),
                    line3=[c["email"], c["phone"]])
    d.closing()
    return d.save(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="minutes.docx")
    ap.add_argument("--brand", default=DEFAULT, choices=sorted(BRANDS))
    print(build(**{"out": ap.parse_args().out, "brand_key": ap.parse_args().brand}))
