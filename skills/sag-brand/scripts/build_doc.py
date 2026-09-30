# -*- coding: utf-8 -*-
"""Reference A4 document in the SAG Graphite & Slate system.

Sample content only -- it is here to show every component once. Swap CONTENT
for the real document and the layout holds.
"""
import os
import tempfile

from docx import Document
from docx.shared import Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn

from palette import BLUE as P, F400, F500, F600, F800, PAGE, W, GUTTER, RADIUS
import graphics
from sagdoc import (mm, track, el, run, fmt, para, cell_p, shade, cborders,
                    cmargin, valign, rowheight, cantsplit, keeprow, table,
                    addrow, spacer, drop_empty_first, shape, emit, xrun,
                    xpara, embed_fonts)

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")
LEFT, RIGHT = WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.RIGHT
BODY_W = W - GUTTER

CONTENT = dict(
    eyebrow="INFORMATION REQUEST",
    title="Document Title Goes Here",
    subtitle_lead="Prepared by PT Stratcon Agara Global for ",
    subtitle_name="Counterparty Name",
    date="24 SEPTEMBER 2026",
    intro=[
        "Opening paragraph. One or two sentences saying why this document "
        "exists and what the reader is being asked to do with it.",
        "Second paragraph. Set out the scope: what the document covers, what "
        "it deliberately leaves out, and anything the reader should have to "
        "hand before they start.",
        "Third paragraph. State how precise the answers need to be, and say "
        "plainly that an incomplete answer is better than no answer.",
    ],
    callout_label="HOW TO RESPOND",
    callout=[
        "Type each answer into the shaded box beneath the question. The boxes "
        "expand as you type, and they also print as blank boxes if you prefer "
        "to write by hand.",
        "A useful answer gives the figure or position first, then any "
        "conditions, then whether it is final or indicative.",
        "Please return completed responses to name@stratconagaraglobal.com.",
    ],
    contents_label="WHAT THIS DOCUMENT COVERS",
    sections=[
        ("Context", "Where this came from", [
            "First question. Keep it to one idea, phrased so the answer can "
            "be a figure, a position or a short statement.",
        ]),
        ("Scope", "What is being asked for", [
            "Second question, sitting under its own section band.",
            "Third question. Sections can hold as many items as needed and "
            "the numbering runs continuously across the whole document.",
        ]),
        ("Commercials", "What it costs and who pays", [
            "Fourth question.",
            "Fifth question, a longer one, to show how a question that runs "
            "to two or three lines sits against its number in the gutter and "
            "stays locked to its own response box.",
        ]),
    ],
    notes_label="ANYTHING ELSE WE SHOULD KNOW",
    notes_sub="Context, constraints or corrections that the questions above "
              "do not reach.",
    contact_label="YOUR CONTACT AT STRATCON AGARA GLOBAL",
    contact_prefix="Eng. ",
    contact_name="Ahmed Y. S. Khalifa",
    contact_role="Project Strategic Engineer",
    contact_org="PT Stratcon Agara Global",
    contact_mail="ahmed.khalifa@stratconagaraglobal.com",
    contact_tel="+62 812 10020646",
    running_left="Information Request",
    running_right="Document Title Goes Here",
    tagline="Navigating complexity, delivering simplicity",
)


def build(out, embed=True, C=CONTENT):
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Mm(PAGE["w"]), Mm(PAGE["h"])
    sec.left_margin, sec.right_margin = Mm(PAGE["ml"]), Mm(PAGE["mr"])
    sec.top_margin, sec.bottom_margin = Mm(PAGE["mt"]), Mm(PAGE["mb"])
    sec.header_distance, sec.footer_distance = Mm(PAGE["header"]), Mm(PAGE["footer"])

    doc.element.insert(0, el("w:background", color=P["PAPER"]))
    doc.settings.element.append(el("w:displayBackgroundShape"))

    st = doc.styles["Normal"]
    st.font.name = F400
    st.font.size = Pt(10)
    st.font.color.rgb = RGBColor.from_string(P["INK"])
    st.element.rPr.rFonts.set(qn("w:hAnsi"), F400)
    st.element.rPr.rFonts.set(qn("w:cs"), F400)
    st.paragraph_format.space_after = Pt(0)
    st.paragraph_format.line_spacing = 1.0

    # ------------------------------------------------------------ masthead --
    # The date is baked into the masthead image, so regenerate it per document
    mh = os.path.join(tempfile.mkdtemp(), "masthead.png")
    graphics.masthead(mh, date=C["date"])
    p = para(doc, align=LEFT)
    p.add_run().add_picture(mh, width=Mm(W))

    # --------------------------------------------------------- title block --
    p = para(doc, before=13)
    run(p, C["eyebrow"], font=F800, size=8, color=P["META"], tr=track(8, 0.20))
    p = para(doc, before=4)
    run(p, C["title"], font=F800, size=23, color=P["INK"], tr=track(23, -0.022))
    p = para(doc, before=3.5)
    run(p, C["subtitle_lead"], font=F500, size=11, color=P["BODY"])
    run(p, C["subtitle_name"], font=F600, size=11, color=P["PANEL"])

    spacer(doc, 5)                      # three-bar accent rule
    t = table(doc, [17, 17, 17, W - 51])
    rowheight(t.rows[0], 1.1, "exact")
    for c, k in zip(t.rows[0].cells[:3], ("RULE", "PALE", "ACCENT")):
        shade(c, P[k])
    spacer(doc, 5)

    for i, txt in enumerate(C["intro"]):
        p = para(doc, before=0 if i == 0 else 5, line=1.45, ind_r=6)
        run(p, txt, font=F400, size=10, color=P["BODY"])

    # ------------------------------------------------------------- callout --
    spacer(doc, 9)
    body = [xpara([xrun(C["callout_label"], F800, 8, P["META"], track(8, 0.18))],
                  after=4)]
    for i, line in enumerate(C["callout"]):
        body.append(xpara([xrun(line, F400, 9.2, P["BODY"])],
                          before=0 if i == 0 else 3.5, line=1.4))
    emit(doc, [shape(W, 42.0, P["TINT"], "".join(body), RADIUS,
                     pad=(6, 5, 6, 5), anchor="t")])

    # ------------------------------------------------------------ contents --
    spacer(doc, 13)
    p = para(doc)
    run(p, C["contents_label"], font=F800, size=8, color=P["META"],
        tr=track(8, 0.20))
    spacer(doc, 4)
    cols = [43, 92, W - 135]
    t = table(doc, cols)
    for k, (title, sub, items) in enumerate(C["sections"]):
        r = t.rows[0] if k == 0 else addrow(t, cols)
        rowheight(r, 4.6)
        cantsplit(r)
        for c in r.cells:
            valign(c, "center")
            cmargin(c, t=2.2, b=2.2)
            if k < len(C["sections"]) - 1:
                cborders(c, bottom=(2, P["TINT"]))
        cmargin(r.cells[2], r=1, t=2.2, b=2.2)
        run(cell_p(r.cells[0], align=LEFT), title, font=F800, size=10,
            color=P["INK"])
        run(cell_p(r.cells[1], align=LEFT), sub, font=F400, size=9,
            color=P["BODY"])
        n = len(items)
        run(cell_p(r.cells[2], align=RIGHT),
            "%d question%s" % (n, "" if n == 1 else "s"), font=F600, size=8.5,
            color=P["MUTED"])

    para(doc).add_run().add_break(WD_BREAK.PAGE)

    # ------------------------------------------------------------ sections --
    num = 0
    for k, (title, sub, items) in enumerate(C["sections"]):
        spacer(doc, 2 if k == 0 else 11, keep=True)
        band = xpara([xrun(title.upper(), F800, 11, P["PAPER"], track(11, 0.09)),
                      "<w:r><w:tab/></w:r>",
                      xrun(sub, F500, 8.8, P["PALE"])], tab_mm=W - 11.5)
        emit(doc, [shape(W, 12.7, P["PANEL"], band, RADIUS,
                         pad=(5.5, 2.6, 6, 2.6))], keep=True)

        for txt in items:
            num += 1
            spacer(doc, 6, keep=True)
            t = table(doc, [GUTTER, BODY_W])

            r0 = t.rows[0]
            cantsplit(r0)
            valign(r0.cells[0], "top")
            cmargin(r0.cells[0], t=1.2)
            cmargin(r0.cells[1], l=0, t=1.2, b=1)
            run(cell_p(r0.cells[0], align=LEFT), "%02d" % num, font=F800,
                size=15, color=P["META"], tr=track(15, -0.02))
            run(cell_p(r0.cells[1], align=LEFT, line=1.35, keep=True, ind_r=4),
                txt, font=F600, size=10.6, color=P["INK"])

            r1 = addrow(t, [GUTTER, BODY_W])
            cantsplit(r1)
            cmargin(r1.cells[1], l=0, t=3.2, b=1.4)
            run(cell_p(r1.cells[1], align=LEFT, keep=True), "RESPONSE",
                font=F800, size=6.8, color=P["MUTED"], tr=track(6.8, 0.22))
            keeprow(r0)
            keeprow(r1)

            r2 = addrow(t, [GUTTER, BODY_W])
            cantsplit(r2)
            rowheight(r2, 14)          # + 5mm cell margins = 19mm box
            box = r2.cells[1]
            shade(box, P["TINT"])
            cborders(box, top=(8, P["RULE"]), left=None, bottom=None, right=None)
            cmargin(box, l=5, r=5, t=2.5, b=2.5)
            cell_p(box)

    # --------------------------------------------------------------- notes --
    spacer(doc, 13, keep=True)
    t = table(doc, [GUTTER, BODY_W])
    r0 = t.rows[0]
    cantsplit(r0)
    cmargin(r0.cells[1], l=0, b=1.4)
    run(cell_p(r0.cells[1], align=LEFT), C["notes_label"], font=F800, size=8,
        color=P["META"], tr=track(8, 0.20))
    run(cell_p(r0.cells[1], align=LEFT, before=2.5, line=1.4), C["notes_sub"],
        font=F400, size=9.2, color=P["BODY"])
    keeprow(r0)
    r1 = addrow(t, [GUTTER, BODY_W])
    cantsplit(r1)
    rowheight(r1, 27)
    box = r1.cells[1]
    shade(box, P["TINT"])
    cborders(box, top=(8, P["RULE"]), left=None, bottom=None, right=None)
    cmargin(box, l=5, r=5, t=2.5, b=2.5)
    cell_p(box)

    # ------------------------------------------------------------- contact --
    spacer(doc, 14)
    cbody = [
        xpara([xrun(C["contact_label"], F800, 6.8, P["PALE"], track(6.8, 0.22))],
              after=4.5),
        xpara([xrun(C["contact_prefix"], F500, 11, P["PALE"]),
               xrun(C["contact_name"], F800, 15.5, P["PAPER"],
                    track(15.5, -0.02))], after=2),
        xpara([xrun(C["contact_role"], F600, 8.8, P["TINT"]),
               xrun("   ·   ", F400, 8.8, P["PALE"]),
               xrun(C["contact_org"], F500, 8.8, P["PALE"])], after=3.5),
        xpara([xrun(C["contact_mail"], F600, 8.8, P["TINT"]),
               xrun("   ·   ", F400, 8.8, P["PALE"]),
               xrun(C["contact_tel"], F400, 8.8, P["PALE"])]),
    ]
    emit(doc, [shape(W, 35.5, P["PANEL"], "".join(cbody), RADIUS,
                     pad=(7, 6.5, 7, 7))])

    spacer(doc, 6)
    p = para(doc, align=LEFT)
    p.add_run().add_picture(
        os.path.join(ASSETS, "graphics", "closing_blue.png"), width=Mm(W))

    # ------------------------------------------------------ header/footer ---
    # Header/Footer styles carry their own tab stops, which beat a
    # paragraph-level one, so these are laid out as tables.
    sec.different_first_page_header_footer = True

    drop_empty_first(sec.header)
    ht = table(sec.header, [7.5, 47, W - 54.5])
    for c in ht.rows[0].cells:
        cborders(c, bottom=(4, P["PALE"]))
        cmargin(c, b=1.6)
        valign(c, "bottom")
    cell_p(ht.rows[0].cells[0], align=LEFT).add_run().add_picture(
        os.path.join(ASSETS, "logo", "sag-logo.png"), height=Mm(4.6))
    run(cell_p(ht.rows[0].cells[1], align=LEFT), "PT STRATCON AGARA GLOBAL",
        font=F800, size=6.8, color=P["INK"], tr=track(6.8, 0.14))
    p = cell_p(ht.rows[0].cells[2], align=RIGHT)
    run(p, C["running_left"], font=F600, size=7.2, color=P["META"])
    run(p, "  ·  ", font=F400, size=7.2, color=P["PALE"])
    run(p, C["running_right"], font=F500, size=7.2, color=P["MUTED"])

    for foot in (sec.footer, sec.first_page_footer):
        drop_empty_first(foot)
        ft = table(foot, [W - 46, 46])
        for c in ft.rows[0].cells:
            cborders(c, top=(4, P["RULE"]))
            cmargin(c, t=1.8)
        run(cell_p(ft.rows[0].cells[0], align=LEFT), C["tagline"], font=F500,
            size=7, color=P["MUTED"])
        p = cell_p(ft.rows[0].cells[1], align=RIGHT)
        run(p, C["date"], font=F600, size=6.6, color=P["MUTED"],
            tr=track(6.6, 0.12))
        run(p, "  ·  ", font=F400, size=7, color=P["PALE"])
        fld = el("w:fldSimple", instr=" PAGE ")
        sub = p.add_run("1")
        sub.font.size = Pt(7.5)
        sub.font.color.rgb = RGBColor.from_string(P["META"])
        sub._element.get_or_add_rPr().insert(
            0, el("w:rFonts", ascii=F800, hAnsi=F800, cs=F800))
        fld.append(sub._element)
        p._p.append(fld)

    doc.save(out)
    if embed:
        embed_fonts(out, os.path.join(ASSETS, "fonts"))
    return out


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Build the SAG reference file (edit the content block at the top, or import build() and call it with your own content).")
    ap.add_argument("--out", default="SAG_Document_Blue.docx", help="output path (default: ./SAG_Document_Blue.docx)")
    print(build(ap.parse_args().out))
