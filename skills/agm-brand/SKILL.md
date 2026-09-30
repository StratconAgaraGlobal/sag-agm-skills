---
name: agm-brand
description: "Apply the PT Agara Global Maritim (AGM) brand, Seafood or Marine edition, to any document, report, MoM, proposal, Word file, PDF, PowerPoint or HTML page. Fully self-contained: emblem, photos, graphics, build code and an HTML example are bundled and Plus Jakarta Sans installs itself. Use whenever output is for or from AGM, or the user mentions AGM, Agara Global Maritim, sea cucumber (teripang), Harvester vessels or FRP shipbuilding branding."
---

# AGM brand — SAG structure, AGM identity

AGM documents use the **SAG component system**: the same geometry, type, components and restraint as the SAG Graphite & Slate brand, carrying **AGM's own colours, emblem, photography and taglines**. AGM is a member of the SAG Group. Everything needed is inside this skill folder; nothing else has to be downloaded or attached.

## 0. Set up (once per session, about ten seconds)
Run from this skill's folder (the folder containing this SKILL.md):

```bash
python scripts/install_fonts.py        # installs Plus Jakarta Sans weights that are missing; skips the rest
pip install python-docx python-pptx Pillow --break-system-packages   # only if an import fails
```

`install_fonts.py` checks each of the five weights first and skips any already installed. Missing ones come from Google Fonts, and if that is unreachable the copies in `assets/fonts` are used, so it never blocks the work. Confirm with `pdffonts` at the end that nothing substituted.

Then look at `examples/agm-brand-example.html` (open it in a browser or the built-in preview; it has a Seafood / Marine switch) to see the emblem builds, colour roles, type, the AGM device, an A4 document and the five deck layouts. `assets/reference/` holds rendered reference files for both editions.

## 1. What is bundled
| Path | What it is |
|---|---|
| `references/DESIGN_SPEC.md` | The full specification: SAG's type, geometry and Word notes, with AGM colours, device and identity |
| `assets/logo/` | `agm-emblem-navy.png` (Seafood, on light), `agm-emblem-green.png` (Marine, on light), `agm-emblem-white.png` (on PANEL) |
| `assets/photos/` | `sea-cucumber-warehouse.jpg` (Seafood band), `harvester-vessel.jpg` (Marine band) |
| `assets/graphics/` | Ready masthead / closing / deck band images for both editions (the masthead date is baked in, so documents regenerate it) |
| `assets/fonts/` | Plus Jakarta Sans, 5 weights + OFL licence |
| `assets/reference/` | Reference `.docx` `.pdf` `.pptx` for both editions, plus a sample MoM |
| `scripts/palette.py`, `brands.py` | `SEAFOOD` / `MARINE` role tokens; edition objects (wordmark, taglines, photo, emblem) |
| `scripts/graphics.py` | The AGM device: photo under a flat PANEL veil + tagline + rule with accent dot |
| `scripts/sagdoc.py`, `components.py` | OOXML helpers and `BrandDoc`: masthead, tiles, callout, band, kv, data_table, item, bullets, roadmap, sign_row, contents, notes box, contact panel, running header/footer |
| `scripts/build_doc.py`, `build_mom.py`, `build_deck.py` | Reference A4 document, worked MoM, five-layout deck; all take an edition |
| `scripts/build_example_html.py` | Rebuilds the HTML example |

## 2. Pick the edition
| Edition | When | PANEL | Accent |
|---|---|---|---|
| **Seafood** (default) | sea cucumber, processing, export, trade, investors | `#052240` deep navy | `#3980C3` ocean blue |
| **Marine** | FRP shipbuilding, Harvester vessels, charter, marine services | `#0D2A2B` harbour green | `#C4A56A` brass |

The eleven role tokens (PAPER, PANEL, INK, BODY, META, MUTED, TINT, RULE, PALE, ACCENT, ACCENT_ON_DARK) are in `scripts/palette.py`, with the same jobs as SAG's roles. **Brass is never text on a light ground:** in Marine, labels and numbers on light use META, not the accent (`brands.py` handles this as `LBL`).

## 3. Identity (fixed)
- **Legal name:** PT AGARA GLOBAL MARITIM (short: AGM). Set it in type beside the emblem: 800 weight, tracked. As the running-header wordmark it is 6.8 pt at +0.14 em.
- **Emblem:** eight-point star, crescent, ship on waves. It has no wordmark. Use the three supplied builds; never recolour beyond them, redraw, stretch or add effects. The bundled files are PNG (recovered from AGM's finished documents); if the designer's vector artwork arrives, swap it in under the same filenames.
- **Masthead descriptor:**
  - Seafood: "Sea Cucumber (Teripang) · Processing & Export · Indonesia"
  - Marine: "FRP Shipbuilding & Marine Services · Jakarta, Indonesia"
- **Taglines** (band line 1 / line 2 / footer):
  - Seafood: SOURCED AND PROCESSED IN INDONESIA / PROCESSED TO A HIGHER STANDARD / "Premium Indonesian sea cucumber, processed to a higher standard"
  - Marine: HARVESTER SERIES | MADE IN INDONESIA / BUILT FOR YOUR OPERATIONS / "Fiberglass vessels for commercial marine operations"
- **Contact block:** +62 819-231-001 · www.agmaritim.com · corporate@stratconagaraglobal.com · Marunda, North Jakarta, Indonesia.
- **Tone:** confident and concrete. Lead with figures. Use British spelling.

## 4. Structure and formatting (inherited from SAG — treat as exact)
- **Page:** A4, margins L/R 20, T 14, B 16 mm. The **170 mm measure** is exact: every full-width element's left edge sits at 20 mm and its right edge at 190 mm.
- **Typeface:** Plus Jakarta Sans only. Select the weight by family name (`… ExtraBold` / `SemiBold` / `Medium`). Only 700 uses the bold flag.
- **Page 1:** masthead (170 × 56 mm, regenerated with the document date) → eyebrow → title → subtitle → three-bar rule (RULE, PALE, ACCENT) → intro → tiles and callout.
- **Later pages:** section bands; numbered items with response boxes; kv, data_table, bullets, roadmap, sign_row; finish with the contact panel and the closing band.
- **Running header** (emblem · wordmark · "<Doc kind> <title>") and **footer** (tagline · DATE · page). Page 1 has no header.
- **The AGM device replaces the Complexity Line:** AGM photography under a flat PANEL veil, with the two-line tagline and a rule ending in an accent dot. Generate it with `graphics.py`; never hand-draw it. No gradients, shadows, clip art, left-edge stripes or pill tags.
- 2.5 mm corner radius on documents, 3 mm on slide cards. The full numbers are in `references/DESIGN_SPEC.md`.

## 5. Build
Import from `scripts/` (run from that folder, or put it on `sys.path`).

- **Word (default) + PDF:** pattern in `build_mom.py`, or any document:

```python
from brands import BRANDS
from components import BrandDoc
b = BRANDS["seafood"]            # or "marine"
d = BrandDoc(b, kind="Proposal", title="Short title", date="30 SEPTEMBER 2026")
d.masthead(); d.title_block("EYEBROW", "Title", "Prepared for ", "Client")
d.intro(["Text with **bold** runs."]); d.tiles([("0%", "TRADING FEE", "Free to use")])
d.callout("HEADLINE", ["**Opportunity.** ..."]); d.band("Section", "Subtitle")
d.kv([...]); d.data_table(headers, rows, widths, marks=(2,))
d.item("Question", "POSITION GIVEN", "Answer"); d.roadmap(phases); d.sign_row([...])
d.contact_panel("YOUR CONTACT", "Name", line2=[b.name], line3=[b.contact["email"]])
d.closing(); d.save("out.docx")     # embeds the fonts
```

  Then `soffice --headless --convert-to pdf out.docx`. `build_doc.py` is the questionnaire-style reference (contents strip, response boxes, notes box).
- **Deck (.pptx):** `build_deck.py` has the five layouts (`cover`, `divider`, `content`, `two_col`, `closing`) with the AGM emblem, device band and taglines. Write a `compose(prs)` and call `build(out, compose, edition="seafood")`. Fonts cannot be embedded in .pptx, so tell the user to install them (`install_fonts.py`) before opening it.
- **Claude Slides / HTML:** same tokens, type and restraint; the slide markup in `examples/agm-brand-example.html` uses the 1920 × 1080 mapping (1 mm = 5.669 px, 1 pt = 2 px). The Slides rules in the sag-brand skill apply with AGM's colours, emblem, band and footer text.
- **Other photos:** the device works with any AGM photo. Copy an `Edition` subclass in `brands.py`, point `photo` at the file and set `photo_y` (0 = crop from the top, 1 = from the bottom).
- Extended components (tiles, kv, data_table with status marks, roadmap, sign_row, contents, notes box) are all in `components.py`. Tell the user which you used.

## 6. Alignment rules (these are what made boxes misalign before)
- **Pictures:** insert with `sagdoc.picture()`, which sets `distL/distR/distT/distB="0"`. Without them LibreOffice adds a 0.32 cm wrap gap and shifts the image about 3 mm right.
- **Tables whose first cell has left padding** (shaded key cells, signature boxes): build with `table(…, lmar=<that padding>)`. This sets `tblCellMar` left and `tblInd`, so Word and LibreOffice both put the box flush on the margin.
- **Fixed-height shapes** (callouts, tiles, contact panel) don't grow. `callout()` sizes itself from the text; the contact panel is 38.5 mm so the email line isn't clipped.
- **Rows of shapes** (tiles, roadmap) total 169.6 mm, with gaps as noFill shapes, so they never wrap.

## 7. Verify
- Render at 40–80 dpi and view every page; use a contact sheet for long documents.
- Measure the edges with pdfplumber: every image or rect wider than 20 mm must start at 20.0 mm and end at 190.0 mm.
- Check nothing is clipped, tiles sit on one line, no band is orphaned at a page foot, tables repeat their headers, and `pdffonts` lists only PlusJakartaSans.
- For minutes of meeting, the `meeting-minutes-mom` skill defines the content; this skill supplies the look (`scripts/build_mom.py`).
