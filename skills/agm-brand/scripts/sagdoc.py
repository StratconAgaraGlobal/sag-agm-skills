# -*- coding: utf-8 -*-
"""OOXML helpers for the SAG Word system.

Three things here are not obvious and cost time to rediscover:

1. Plus Jakarta Sans exposes each weight as a separate Windows family, so
   weight is chosen by family name, not the bold flag (except 700).
2. Word hangs a table's first-cell left margin OUTSIDE the table box, so the
   box only sits flush on the page margin if tblInd gives that margin back.
3. w:trHeight sets the CONTENT height -- Word adds the cell margins on top.
"""
import os

from docx.shared import Pt, Mm, RGBColor
from docx.oxml import parse_xml
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

from palette import F400, F500, F600, F800, EMBED

DXA = 56.6929   # dxa (twips) per mm
EMU = 36000     # EMU per mm


def mm(v):
    return int(round(v * DXA))


def track(size_pt, em):
    """Letter spacing in twentieths of a point."""
    return int(round(size_pt * em * 20))


def el(tag, **attrs):
    e = OxmlElement(tag)
    for k, v in attrs.items():
        e.set(qn("w:" + k), str(v))
    return e


# ------------------------------------------------------------------- runs ---
def run(p, text, font=F400, size=10, color=None, bold=False, italic=False,
        tr=0, caps=False):
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.bold = bold
    r.italic = italic
    if color:
        r.font.color.rgb = RGBColor.from_string(color)
    rpr = r._element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = el("w:rFonts")
        rpr.insert(0, rf)
    for a in ("ascii", "hAnsi", "cs"):
        rf.set(qn("w:" + a), font)
    if tr:
        rpr.append(el("w:spacing", val=tr))
    if caps:
        rpr.append(el("w:caps", val="1"))
    return r


def fmt(p, align=None, before=0, after=0, line=None, keep=False,
        ind_l=0, ind_r=0):
    pf = p.paragraph_format
    if align is not None:
        p.alignment = align
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    if line:
        pf.line_spacing = line
    if ind_l:
        pf.left_indent = Mm(ind_l)
    if ind_r:
        pf.right_indent = Mm(ind_r)
    if keep:
        pf.keep_with_next = True
    return p


def para(doc, **kw):
    return fmt(doc.add_paragraph(), **kw)


def cell_p(cell, **kw):
    p = cell.paragraphs[0]
    if p.runs:
        p = cell.add_paragraph()
    return fmt(p, **kw)


def pborder(p, edge="bottom", color="000000", sz=6, space=4):
    pPr = p._element.get_or_add_pPr()
    bd = pPr.find(qn("w:pBdr"))
    if bd is None:
        bd = el("w:pBdr")
        pPr.append(bd)
    bd.append(el("w:" + edge, val="single", sz=sz, space=space, color=color))


# ------------------------------------------------------------------ cells ---
def shade(cell, color):
    cell._tc.get_or_add_tcPr().append(
        el("w:shd", val="clear", color="auto", fill=color))


def cborders(cell, **edges):
    tcPr = cell._tc.get_or_add_tcPr()
    bd = tcPr.find(qn("w:tcBorders"))
    if bd is None:
        bd = el("w:tcBorders")
        tcPr.append(bd)
    for e in ("top", "left", "bottom", "right"):
        if e in edges:
            v = edges[e]
            bd.append(el("w:" + e, val="none") if v is None else
                      el("w:" + e, val="single", sz=v[0], space="0", color=v[1]))


def cmargin(cell, l=0, r=0, t=0, b=0):
    tcPr = cell._tc.get_or_add_tcPr()
    old = tcPr.find(qn("w:tcMar"))
    if old is not None:
        tcPr.remove(old)
    m = el("w:tcMar")
    for k, v in (("top", t), ("left", l), ("bottom", b), ("right", r)):
        m.append(el("w:" + k, w=mm(v), type="dxa"))
    tcPr.append(m)


def valign(cell, v="center"):
    cell._tc.get_or_add_tcPr().append(el("w:vAlign", val=v))


def rowheight(row, h_mm, rule="atLeast"):
    row._tr.get_or_add_trPr().append(el("w:trHeight", val=mm(h_mm), hRule=rule))


def cantsplit(row):
    row._tr.get_or_add_trPr().append(el("w:cantSplit"))


def keeprow(row):
    """Word only holds rows together if every paragraph above is keepNext."""
    for c in row.cells:
        for p in c.paragraphs:
            p.paragraph_format.keep_with_next = True


def _prep(cells, widths):
    for c, w in zip(cells, widths):
        c.width = Mm(w)
        c.paragraphs[0].paragraph_format.space_after = Pt(0)
        cmargin(c)


def table(doc, widths, ind=0.0, lmar=0.0):
    """lmar: left padding (mm) of the first cell. Word hangs that padding
    OUTSIDE the table box, so tblInd gives it back and the box sits flush on
    the page margin in both Word and LibreOffice."""
    if lmar:
        ind = ind + lmar
    try:
        t = doc.add_table(rows=1, cols=len(widths))
    except TypeError:                      # header / footer containers
        t = doc.add_table(rows=1, cols=len(widths), width=Mm(sum(widths)))
    t.autofit = False
    tblPr = t._tbl.tblPr
    tblPr.append(el("w:tblLayout", type="fixed"))
    tblPr.append(el("w:tblInd", w=mm(ind), type="dxa"))
    if lmar:
        cm = el("w:tblCellMar")
        cm.append(el("w:left", w=mm(lmar), type="dxa"))
        tblPr.append(cm)
    bd = el("w:tblBorders")
    for e in ("top", "left", "bottom", "right", "insideH", "insideV"):
        bd.append(el("w:" + e, val="none"))
    tblPr.append(bd)
    grid = t._tbl.find(qn("w:tblGrid"))
    for gc, w in zip(grid.findall(qn("w:gridCol")), widths):
        gc.set(qn("w:w"), str(mm(w)))
    _prep(t.rows[0].cells, widths)
    return t


def addrow(t, widths):
    r = t.add_row()
    _prep(r.cells, widths)
    return r


def spacer(doc, h_pt, keep=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.keep_with_next = keep
    p.add_run("").font.size = Pt(h_pt)
    return p


def picture(paragraph, path, width_mm=None, height_mm=None):
    """Insert an inline picture with zero wrap distances. Without the explicit
    distL/distR/distT/distB="0", LibreOffice adds a 0.32 cm gap and shifts the
    image about 3 mm to the right."""
    run_ = paragraph.add_run()
    kw = {}
    if width_mm:
        kw["width"] = Mm(width_mm)
    if height_mm:
        kw["height"] = Mm(height_mm)
    run_.add_picture(path, **kw)
    for inline in run_._element.iter(qn("wp:inline")):
        for a in ("distT", "distB", "distL", "distR"):
            inline.set(a, "0")
    return run_


def repeat_header(row):
    """Repeat this row at the top of every page the table runs onto."""
    row._tr.get_or_add_trPr().append(el("w:tblHeader"))


def drop_empty_first(container):
    ps = container.paragraphs
    if ps and not ps[0].runs:
        ps[0]._p.getparent().remove(ps[0]._p)


# ------------------------------------------------------- rounded panels -----
# Word cannot round a table corner. The brand panels are DrawingML roundRect
# shapes instead. They must be wp:inline (VML gets floated by Word) and be
# inserted BEFORE w:sectPr, or Word reflows them all to the end of the doc.
_NS = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
       'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/'
       'wordprocessingDrawing" '
       'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
       'xmlns:wps="http://schemas.microsoft.com/office/word/2010/'
       'wordprocessingShape"')

_SHAPE = '''<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">
<wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/>
<wp:docPr id="{sid}" name="Panel{sid}"/><wp:cNvGraphicFramePr/>
<a:graphic><a:graphicData uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
<wps:wsp><wps:cNvSpPr txBox="1"/><wps:spPr>
<a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>
<a:prstGeom prst="roundRect"><a:avLst><a:gd name="adj" fmla="val {adj}"/></a:avLst></a:prstGeom>
{fillxml}<a:ln><a:noFill/></a:ln>
</wps:spPr><wps:txbx><w:txbxContent>{body}</w:txbxContent></wps:txbx>
<wps:bodyPr rot="0" vert="horz" wrap="square" anchor="{anchor}"
 lIns="{li}" tIns="{ti}" rIns="{ri}" bIns="{bi}" anchorCtr="0"/>
</wps:wsp></a:graphicData></a:graphic></wp:inline></w:drawing></w:r>'''

_ID = [100]


def xesc(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;"))


def xrun(text, font=F400, size=10, color="000000", tr=0):
    sp = '<w:spacing w:val="%d"/>' % tr if tr else ""
    return ('<w:r><w:rPr><w:rFonts w:ascii="{f}" w:hAnsi="{f}" w:cs="{f}"/>'
            '<w:color w:val="{c}"/><w:sz w:val="{s}"/><w:szCs w:val="{s}"/>{sp}'
            '</w:rPr><w:t xml:space="preserve">{t}</w:t></w:r>').format(
        f=font, c=color, s=int(round(size * 2)), sp=sp, t=xesc(text))


def xpara(runs, before=0, after=0, line=None, tab_mm=None, jc=None):
    tabs = ('<w:tabs><w:tab w:val="right" w:pos="%d"/></w:tabs>'
            % mm(tab_mm)) if tab_mm else ""
    sp = ('<w:spacing w:before="%d" w:after="%d" w:line="%d" w:lineRule="auto"/>'
          % (int(before * 20), int(after * 20), int(line * 240))) if line else \
         ('<w:spacing w:before="%d" w:after="%d"/>'
          % (int(before * 20), int(after * 20)))
    j = '<w:jc w:val="%s"/>' % jc if jc else ""
    return "<w:p><w:pPr>%s%s%s</w:pPr>%s</w:p>" % (sp, tabs, j, "".join(runs))


def shape(w_mm, h_mm, fill, body, radius=2.5, pad=(5.5, 2.6, 5.5, 2.6),
          anchor="ctr"):
    """fill=None draws nothing -- a spacer, since wp:inline ignores distL/R."""
    _ID[0] += 1
    adj = int(round(min(radius, min(w_mm, h_mm) / 2.0) /
                    min(w_mm, h_mm) * 100000))
    fx = ('<a:solidFill><a:srgbClr val="%s"/></a:solidFill>' % fill
          if fill else "<a:noFill/>")
    return _SHAPE.format(cx=int(w_mm * EMU), cy=int(h_mm * EMU), adj=adj,
                         fillxml=fx, body=body, sid=_ID[0], anchor=anchor,
                         li=int(pad[0] * EMU), ti=int(pad[1] * EMU),
                         ri=int(pad[2] * EMU), bi=int(pad[3] * EMU))


def emit(doc, shapes_xml, before=0, after=0, keep=False):
    kn = "<w:keepNext/>" if keep else ""
    p = ('<w:p %s><w:pPr>%s<w:spacing w:before="%d" w:after="%d"/></w:pPr>%s</w:p>'
         % (_NS, kn, int(before * 20), int(after * 20), "".join(shapes_xml)))
    doc.element.body.find(qn("w:sectPr")).addprevious(parse_xml(p))


# --------------------------------------------------------------- embedding --
def embed_fonts(path, fontdir):
    """Embed the family so the recipient sees it without installing anything.

    Each face is stored as an obfuscated .odttf: the first 32 bytes are XORed
    with the 16-byte little-endian form of the fontKey GUID, applied twice.
    """
    import zipfile
    import uuid

    zin = zipfile.ZipFile(path, "r")
    items, order = {}, []
    for n in zin.namelist():
        items[n] = zin.read(n)
        order.append(n)
    zin.close()

    ft = items["word/fontTable.xml"].decode("utf-8")
    relname = "word/_rels/fontTable.xml.rels"
    if relname in items:
        rels = items[relname].decode("utf-8")
    else:
        rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<Relationships xmlns="http://schemas.openxmlformats.org/'
                'package/2006/relationships"></Relationships>')
        order.append(relname)

    relparts, n = [], 0
    for fam, reg, bold in EMBED:
        tags = ""
        for kind, fn in (("embedRegular", reg), ("embedBold", bold)):
            if not fn:
                continue
            n += 1
            guid = str(uuid.uuid4()).upper()
            raw = bytes.fromhex(guid.replace("-", ""))
            key = (bytes(reversed(raw[0:4])) + bytes(reversed(raw[4:6])) +
                   bytes(reversed(raw[6:8])) + raw[8:16])
            data = bytearray(open(os.path.join(fontdir, fn), "rb").read())
            for i in range(32):
                data[i] ^= key[i % 16]
            target = "word/fonts/font%d.odttf" % n
            items[target] = bytes(data)
            order.append(target)
            relparts.append(
                '<Relationship Id="rIdF%d" Type="http://schemas.openxmlformats'
                '.org/officeDocument/2006/relationships/font" '
                'Target="fonts/font%d.odttf"/>' % (n, n))
            tags += ('<w:%s r:id="rIdF%d" w:fontKey="{%s}" w:subsetted="false"/>'
                     % (kind, n, guid))
        marker = '<w:font w:name="%s">' % fam
        if marker in ft:
            close = ft.index("</w:font>", ft.index(marker))
            ft = ft[:close] + tags + ft[close:]
        else:
            ft = ft.replace("</w:fonts>", '<w:font w:name="%s">%s</w:font>'
                            '</w:fonts>' % (fam, tags))

    items["word/fontTable.xml"] = ft.encode("utf-8")
    items[relname] = rels.replace(
        "</Relationships>", "".join(relparts) + "</Relationships>").encode("utf-8")

    ct = items["[Content_Types].xml"].decode("utf-8")
    if "obfuscatedFont" not in ct:
        i = ct.index(">", ct.index("<Types")) + 1
        ct = (ct[:i] + '<Default Extension="odttf" ContentType="application/'
              'vnd.openxmlformats-officedocument.obfuscatedFont"/>' + ct[i:])
    items["[Content_Types].xml"] = ct.encode("utf-8")

    st = items["word/settings.xml"].decode("utf-8")
    if "embedTrueTypeFonts" not in st:
        i = st.index(">", st.index("<w:settings")) + 1
        st = st[:i] + "<w:embedTrueTypeFonts/>" + st[i:]
    items["word/settings.xml"] = st.encode("utf-8")

    tmp = path + ".tmp"
    zo = zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED)
    for k in order:
        zo.writestr(k, items[k])
    zo.close()
    os.replace(tmp, path)
    return n
