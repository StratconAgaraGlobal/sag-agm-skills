# AGM Design Specification — SAG system, AGM identity

PT Agara Global Maritim (AGM). Word (A4) and PowerPoint (16:9), two editions:
**Seafood** (default) and **Marine**.

AGM is a member of the SAG Group and uses the **SAG component system
unchanged**: the same typography, geometry, component sizes and restraint as
the SAG Graphite & Slate specification. This document is that specification
with the three things that differ for AGM swapped in: the **colour roles**
(section 1), the **device** that replaces the Complexity Line (section 4) and
the **identity** (section 6: emblem, wordmark, taglines, contact). Sections 2,
3 and 5 are the SAG ones, verbatim. Where the text below still says "SAG
Yellow", read "the edition's ACCENT".

---

## 1. Colour

Roles, not names. The same eleven roles as SAG. `ACCENT_ON_DARK` is the accent
as it appears on `PANEL` (tagline line 2, the rule and its dot, tile values).

| Role | Seafood | Marine | Used for |
|---|---|---|---|
| `PAPER` | `#F5F9FD` | `#F6F8F7` | Page ground; text on dark panels |
| `PANEL` | `#052240` deep navy | `#0D2A2B` harbour green | Dark panels: masthead, section bands, contact, dark slides |
| `INK` | `#012864` | `#0D2A2B` | Document title, item text, slide headlines |
| `BODY` | `#3F4F63` | `#3E5754` | Body copy |
| `META` | `#3980C3` | `#2D5352` | Eyebrows, item numbers, page number |
| `MUTED` | `#55657A` | `#526C68` | Small labels, counts, slide footers |
| `TINT` | `#EAF3FB` | `#EAF0EE` | Callouts, response boxes, slide cards |
| `RULE` | `#8FB4DA` | `#A3B9B5` | Hairlines; bullet dashes |
| `PALE` | `#C9DCEF` | `#C9D6D3` | Text on `PANEL`; header hairline |
| `ACCENT` | `#3980C3` ocean blue | `#C4A56A` brass | Short rules, the three-bar rule's third bar |
| `ACCENT_ON_DARK` | `#8FB4DA` | `#C4A56A` | Accent on `PANEL` |

**Brass is never text on a light ground.** In the Marine edition, small
tracked labels, item numbers and the page number on light grounds use `META`
(`#2D5352`), not the accent; in Seafood they use the ocean blue `ACCENT`,
which reads well on light. (`brands.py` carries this as `LBL`.)

---

## 2. Typography

**Plus Jakarta Sans** throughout. It ships each weight as its **own Windows
font family**, so weight is selected by family name, not the bold flag:

| Weight | Select this family | Bold flag |
|---|---|---|
| 400 | `Plus Jakarta Sans` | off |
| 500 | `Plus Jakarta Sans Medium` | off |
| 600 | `Plus Jakarta Sans SemiBold` | off |
| 700 | `Plus Jakarta Sans` | **on** |
| 800 | `Plus Jakarta Sans ExtraBold` | off |

Setting bold on the ExtraBold family produces a synthetic double-bold. Don't.
Fallbacks if the family is unavailable: Aptos, then Calibri. The reference
`.docx` embeds the faces so recipients need nothing installed.

Tracking below is in **em**. In OOXML, `w:spacing w:val` is in twentieths of
a point: `val = round(size_pt × em × 20)`.

### A4 document

| Element | Family | Size | Colour | Tracking | Leading |
|---|---|---|---|---|---|
| Body default | 400 | 10 | `INK` | 0 | 1.0 |
| Document eyebrow | 800 | 8 | `META` | +0.20 | — |
| Document title | 800 | 23 | `INK` | −0.022 | — |
| Subtitle | 500 | 11 | `BODY` | 0 | — |
| Subtitle — counterparty | 600 | 11 | `PANEL` | 0 | — |
| Intro paragraphs | 400 | 10 | `BODY` | 0 | 1.45 |
| Callout label | 800 | 8 | `META` | +0.18 | — |
| Callout body | 400 | 9.2 | `BODY` | 0 | 1.40 |
| Contents label | 800 | 8 | `META` | +0.20 | — |
| Contents — name | 800 | 10 | `INK` | 0 | — |
| Contents — descriptor | 400 | 9 | `BODY` | 0 | — |
| Contents — count | 600 | 8.5 | `MUTED` | 0 | — |
| Section band — title (caps) | 800 | 11 | `PAPER` | +0.09 | — |
| Section band — subtitle | 500 | 8.8 | `PALE` | 0 | — |
| Item number | 800 | 15 | `META` | −0.02 | — |
| Item text | 600 | 10.6 | `INK` | 0 | 1.35 |
| Response label (caps) | 800 | 6.8 | `MUTED` | +0.22 | — |
| Contact label (caps) | 800 | 6.8 | `PALE` | +0.22 | — |
| Contact — "Eng." prefix | 500 | 11 | `PALE` | 0 | — |
| Contact — name | 800 | 15.5 | `PAPER` | −0.02 | — |
| Contact — role | 600 | 8.8 | `TINT` | 0 | — |
| Contact — org | 500 | 8.8 | `PALE` | 0 | — |
| Contact — email | 600 | 8.8 | `TINT` | 0 | — |
| Contact — phone | 400 | 8.8 | `PALE` | 0 | — |
| Header — wordmark | 800 | 6.8 | `INK` | +0.14 | — |
| Header — doc kind | 600 | 7.2 | `META` | 0 | — |
| Header — doc title | 500 | 7.2 | `MUTED` | 0 | — |
| Footer — tagline | 500 | 7 | `MUTED` | 0 | — |
| Footer — date | 600 | 6.6 | `MUTED` | +0.12 | — |
| Footer — page number | 800 | 7.5 | `META` | 0 | — |

Separators between contact items are `   ·   ` (three spaces either side) in
400 at the surrounding size, coloured `PALE`.

### 16:9 deck

Tracking here is in **points** (PowerPoint's `spc` attribute, hundredths of a
point: `spc = round(pt × 100)`).

| Element | Family | Size | Colour | Tracking |
|---|---|---|---|---|
| Cover — wordmark | 800 | 11 | `PALE` | +1.1 |
| Cover — title | 800 | 40 | `PAPER` | −0.8 |
| Cover — subtitle | 500 | 15 | `PALE` | 0 |
| Cover — date | 600 | 9.5 | `PALE` | +1.4 |
| Divider — number | 800 | 54 | `META` | −1.0 |
| Divider — title | 800 | 34 | `PAPER` | −0.7 |
| Divider — subtitle | 500 | 14 | `PALE` | 0 |
| Content — eyebrow | 800 | 9.5 | `META` | +1.6 |
| Content — headline | 800 | 28 | `INK` | −0.6 |
| Content — bullet dash | 800 | 13 | `RULE` | 0 |
| Content — bullet text | 400 | 13 | `BODY` | 0 |
| Card — heading | 800 | 15 | `INK` | −0.3 |
| Card — body | 400 | 11 | `BODY` | 0 |
| Closing — label | 800 | 9 | `PALE` | +1.8 |
| Closing — name | 800 | 26 | `PAPER` | −0.5 |
| Slide footer | 500 / 600 | 8 | `MUTED` | 0 |

Content bullets: line spacing 1.35, 11pt space before each after the first.
Card body: line spacing 1.3, 7pt after the heading.

---

## 3. Geometry

### A4 page

```
Page            210 × 297 mm
Margins         left 20, right 20, top 14, bottom 16
Header/footer   9 mm from edge
Content measure 170 mm            ← every full-width element is exactly this
Item gutter     15 mm             ← holds the item number
Item body       155 mm
Corner radius   2.5 mm
```

Different first page header/footer is **on**: page 1 has no running header
(the masthead does that job) but does carry the footer.

### Components, top to bottom

| Component | Size | Fill | Padding (L/T/R/B) | Notes |
|---|---|---|---|---|
| Masthead | 170 × 56 mm image | — | — | 25.1 mm logo zone + 30.9 mm device band; radius baked in |
| Three-bar rule | 3 × (17 × 1.1 mm) | `RULE`, `PALE`, `ACCENT` | — | Exact row height; 5 pt air above and below |
| Callout | 170 × 42 mm | `TINT` | 6 / 5 / 6 / 5 | Top-anchored |
| Contents row | 43 / 92 / 35 mm cols | — | 0 / 2.2 / 0 / 2.2 | 4.6 mm row height; 0.25 pt `TINT` rule between rows |
| Section band | 170 × 12.7 mm | `PANEL` | 5.5 / 2.6 / 6 / 2.6 | Centre-anchored; subtitle on a right tab at 158.5 mm |
| Item — question row | 15 + 155 mm | — | body 0 / 1.2 / 0 / 1 | Number top-aligned in the gutter |
| Item — label row | 15 + 155 mm | — | body 0 / 3.2 / 0 / 1.4 | |
| Item — response box | 155 mm, `trHeight` 14 mm | `TINT` | 5 / 2.5 / 5 / 2.5 | Renders 19 mm; 1 pt `RULE` top border only |
| Notes box | 155 mm, `trHeight` 27 mm | `TINT` | 5 / 2.5 / 5 / 2.5 | Renders 32 mm |
| Contact panel | 170 × 38.5 mm | `PANEL` | 7 / 6.5 / 7 / 7 | |
| Closing band | 170 × 30.9 mm image | — | — | Radius baked in |

Vertical rhythm, as point-sized empty paragraphs: 13 pt before the title
block, 5 pt around the three-bar rule, 9 pt before the callout, 13 pt before
the contents strip and the notes box, 11 pt before each section band (2 pt
for the first on a page), 6 pt before each item, 14 pt before the contact
panel, 6 pt before the closing band.

### Running header and footer

Header: three cells `7.5 / 47 / 115.5 mm`, bottom-aligned, 1.6 mm bottom
padding, 0.5 pt `PALE` bottom border. Shield at 4.6 mm high, then the
wordmark; document kind and title right-aligned in the third cell.

Footer: two cells `124 / 46 mm`, 1.8 mm top padding, 0.5 pt `RULE` top
border. Tagline left; date, a `·`, then the `PAGE` field right.

### 16:9 slide

```
Slide           338.667 × 190.5 mm   (13.333 × 7.5 in)
Side margins    18 mm
Content measure 302.667 mm
Card radius     3 mm
```

| Layout | Ground | Structure |
|---|---|---|
| Cover | `PANEL` | Device band full-bleed across the bottom 52 mm; logo at (18, 20) 18 mm high; text block from y 48; date top-right |
| Divider | `PANEL` | 1.6 mm `ACCENT` rule across the very top; number / title / subtitle centred vertically |
| Content | `PAPER` | Eyebrow + headline from y 20; 34 × 1.2 mm `ACCENT` rule at y 54; body from y 64 at 82 % measure |
| Cards | `PAPER` | Same head; cards at y 70, 56 mm tall, 8 mm gutters, equal widths; 16 × 1.2 mm `ACCENT` rule 8 mm inside each card's top |
| Closing | `PANEL` | Cover furniture, contact block from y 52 |

Light slides carry a footer: 0.35 mm `RULE` line at y 176.5, tagline left,
organisation name right, both at y 179.5.

---

## 4. The AGM device

AGM has no Complexity Line. Its banner device is **photography under a flat
`PANEL` veil**, carrying the two-line tagline and a rule that ends in an accent
dot. Generated, never hand-drawn: `scripts/graphics.py`.

```
photo        width-fit, cropped vertically (brands.py: photo_y), no other filter
veil         PANEL at 78 % opacity over the whole photo (flat: no gradient)
tagline      two lines, ExtraBold 8.6 pt, letter-spacing 0.085 em, centred at 62 % of the width
             line 1 in white, line 2 in ACCENT_ON_DARK
rule         from 144.2 to 165.6 mm (of the 170 mm measure), ACCENT_ON_DARK,
             ending in a 0.5 mm-radius dot
masthead     170 x 56 mm: 25.1 mm PANEL zone (emblem 15.3 mm at x 5.1, wordmark
             10.5 pt ExtraBold +0.10 em at x 25.7, descriptor 6.6 pt, date right)
             + 30.9 mm device band. Corners rounded 2.5 mm, baked in.
closing      170 x 30.9 mm device band alone
deck band    338.667 x 52 mm, full-bleed, square corners
```

The date in the masthead is part of the image, so regenerate it per document
(`BrandDoc.masthead()` does this for you).

---

## 5. Implementation notes

These are the things that cost time to rediscover.

**Word cannot round a table corner.** The rounded panels are DrawingML
`roundRect` shapes. They must be wrapped in `wp:inline` — VML `v:roundrect`
renders correctly but Word floats it, which breaks the flow. The corner
radius is `adj`, in 1/100000 of the shorter side:
`adj = radius_mm / min(w_mm, h_mm) × 100000`.

**Raw XML must be inserted before `w:sectPr`.** Appending to the body puts it
after the section properties and Word reflows everything to the end of the
document.

**`wp:inline` ignores `distL` / `distR`.** To put a gap between two inline
shapes, insert a third shape of the gap's width with `<a:noFill/>`.

**Inline shapes do not auto-grow.** Their height is fixed at build time, so
compute it from the content or the text clips. The response boxes are
deliberately *tables*, not shapes, so they expand as the recipient types.

**`w:tblInd`.** Word hangs a table's first-cell left margin outside the table
box, so the box only sits flush on the page margin if `tblInd` is set to that
same margin.

**`w:trHeight` is the content height** — Word adds the cell margins on top. A
19 mm box is `trHeight` 14 mm plus 2.5 mm top and bottom.

**Keeping a block together.** `cantSplit` stops a row splitting internally;
it does not hold rows together. For that, every paragraph in every *earlier*
row must have `keepNext` — including the empty ones in the gutter cells.
Leave the last row without it, or the chain runs on into the next block.

**Header and footer tab stops.** The built-in Header and Footer styles carry
their own centre and right tabs, which beat a paragraph-level tab stop. Lay
the running header and footer out as borderless tables instead.

**Adjacent cells sharing a fill** show a hairline seam when the PDF is
rasterised. A 1 pt border in the fill colour reduces it; it never fully
disappears, but it does not print. Rounded panels avoid the issue entirely.

**Font embedding.** Each face is stored as `word/fonts/fontN.odttf`, XOR-
obfuscated: take the `fontKey` GUID, reorder to little-endian
(`raw[0:4]` reversed + `raw[4:6]` reversed + `raw[6:8]` reversed + `raw[8:16]`),
and XOR the file's first 32 bytes with that 16-byte key, wrapping once. Add
the `odttf` default content type and `<w:embedTrueTypeFonts/>` in
`settings.xml`.

---

## 6. AGM identity (fixed)

- **Legal name:** PT Agara Global Maritim (short: AGM). Set in type beside the
  emblem: ExtraBold, tracked; as the running-header wordmark 6.8 pt at +0.14 em.
- **Emblem:** eight-point star, crescent, ship on waves; no wordmark of its own.
  Three flat builds: `agm-emblem-navy.png` (Seafood, on light),
  `agm-emblem-green.png` (Marine, on light), `agm-emblem-white.png` (on
  `PANEL`). Never recolour beyond these three, redraw, stretch or add effects.
- **Masthead descriptor:** Seafood "Sea Cucumber (Teripang) · Processing &
  Export · Indonesia"; Marine "FRP Shipbuilding & Marine Services · Jakarta,
  Indonesia".
- **Taglines** (band line 1 / line 2 / footer):
  - Seafood: SOURCED AND PROCESSED IN INDONESIA / PROCESSED TO A HIGHER STANDARD /
    "Premium Indonesian sea cucumber, processed to a higher standard"
  - Marine: HARVESTER SERIES | MADE IN INDONESIA / BUILT FOR YOUR OPERATIONS /
    "Fiberglass vessels for commercial marine operations"
- **Contact block:** +62 819-231-001 · www.agmaritim.com ·
  corporate@stratconagaraglobal.com · Marunda, North Jakarta, Indonesia.
- **Header logo** on light grounds: the navy emblem (Seafood) or green emblem
  (Marine).
