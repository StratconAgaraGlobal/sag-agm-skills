# -*- coding: utf-8 -*-
"""Reference A4 document (questionnaire / information request) in the AGM
system, both editions. Sample content only: swap CONTENT for the real text.

    python build_doc.py --out request.docx [--edition seafood|marine]
"""
import argparse

from brands import BRANDS, DEFAULT
from components import BrandDoc

CONTENT = dict(
    date="24 SEPTEMBER 2026",
    kind="Information Request",
    title="Document Title Goes Here",
    subtitle_lead="Prepared by PT Agara Global Maritim for ",
    subtitle_name="Counterparty Name",
    intro=[
        "Opening paragraph. One or two sentences saying why this document "
        "exists and what the reader is being asked to do with it.",
        "Second paragraph. Set out the scope: what the document covers, what "
        "it deliberately leaves out, and anything the reader should have to "
        "hand before they start.",
        "Third paragraph. State how precise the answers need to be, and say "
        "plainly that an incomplete answer is better than no answer.",
    ],
    callout_label="How to respond",
    callout=[
        "Type each answer into the shaded box beneath the question. The boxes "
        "expand as you type, and they also print as blank boxes if you prefer "
        "to write by hand.",
        "A useful answer gives the figure or position first, then any "
        "conditions, then whether it is final or indicative.",
    ],
    contents_label="What this document covers",
    sections=[
        ("Context", "Where this came from", [
            "First question. Keep it to one idea, phrased so the answer can "
            "be a figure, a position or a short statement."]),
        ("Scope", "What is being asked for", [
            "Second question, sitting under its own section band.",
            "Third question. Sections can hold as many items as needed and "
            "the numbering runs continuously across the whole document."]),
        ("Commercials", "What it costs and who pays", [
            "Fourth question.",
            "Fifth question, a longer one, to show how a question that runs "
            "to two or three lines sits against its number in the gutter and "
            "stays locked to its own response box."]),
    ],
    notes_label="Anything else we should know",
    notes_sub="Context, constraints or corrections that the questions above "
              "do not reach.",
    contact_label="Your contact at PT Agara Global Maritim",
    contact_name="Name Surname",
)


def build(out, edition=DEFAULT, C=CONTENT):
    b = BRANDS[edition]
    d = BrandDoc(b, C["kind"], C["title"], C["date"])
    d.masthead()
    d.title_block(C["kind"].upper(), C["title"], C["subtitle_lead"],
                  C["subtitle_name"])
    d.intro(C["intro"])
    d.callout(C["callout_label"], C["callout"])
    d.contents(C["contents_label"],
               [(t, s, "%d question%s" % (len(i), "" if len(i) == 1 else "s"))
                for t, s, i in C["sections"]])
    d.page_break()
    for k, (title, sub, items) in enumerate(C["sections"]):
        d.band(title, sub, first=(k == 0))
        for q in items:
            d.item(q, "Response", "", min_h=14)
    d.notes_box(C["notes_label"], C["notes_sub"])
    c = b.contact
    d.contact_panel(C["contact_label"], C["contact_name"],
                    line2=[b.name, c["address"]],
                    line3=[c["email"], c["phone"]])
    d.closing()
    return d.save(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="AGM_Document.docx")
    ap.add_argument("--edition", default=DEFAULT, choices=sorted(BRANDS))
    a = ap.parse_args()
    print(build(a.out, a.edition))
