---
name: sag-brand
description: "Apply the PT Stratcon Agara Global (SAG) Graphite & Slate brand to any Word document, PDF, PowerPoint deck, Claude Slides deck, HTML page, web app, internal tool, dashboard, PWA, business card, letterhead or Minutes of Meeting. Fully self-contained (fonts, logos, graphics, build code and an HTML example are bundled; Plus Jakarta Sans installs itself). Use whenever output is for or from SAG, or the user mentions SAG, Stratcon Agara, Graphite & Slate, the Complexity Line or the SAG logo, even if they don't say 'brand'. Also use when building or restyling any SAG app or UI."
---

# SAG brand — Graphite & Slate

For PT Stratcon Agara Global (SAG), an Indonesian strategic advisory, regulatory affairs and ESG consultancy. Everything needed is inside this skill folder; nothing else has to be downloaded or attached. Every number in `references/DESIGN_SPEC.md` is exact.

**Palette is green (5 Oct 2026).** The slate-blue roles were shifted to green at the same lightness and saturation; yellow, gold and the status colours are unchanged. File and variable names still say `blue` (`masthead_blue.png`, `palette.BLUE`) so existing scripts keep working. The PDFs, PPTX and DOCX under `assets/reference/` are still the old slate builds until they are regenerated, so take colours from the roles below, not from those files.

## 0. Set up (once per session, about ten seconds)
Run from this skill's folder (the folder containing this SKILL.md):

```bash
python scripts/install_fonts.py        # installs Plus Jakarta Sans weights that are missing; skips the rest
pip install python-docx python-pptx Pillow --break-system-packages   # only if an import fails
```

`install_fonts.py` checks each of the five weights first and skips any already installed. Missing ones come from Google Fonts, and if that is unreachable the copies in `assets/fonts` are used, so it never blocks the work. Without the fonts installed, PDFs render in a substitute face and nothing looks right, so confirm with `pdffonts` at the end.

Then look at `examples/sag-brand-example.html` (open it in a browser or the built-in preview) to see the logo builds, colour roles, type, Complexity Line, an A4 document and all five deck layouts. `assets/reference/` holds rendered reference files and page images.

## 1. What is bundled
| Path | What it is |
|---|---|
| `references/DESIGN_SPEC.md` | The full specification (colour, type, geometry, component sizes, Word implementation notes) |
| `references/BRAND_SYSTEM.md` | Identity rules around the spec: logo builds, clear space and misuse, naming, print colour values, Office theme, schedule colours, business card, letterhead, stamp |
| `references/APP_DESIGN.md` | How SAG apps look: screen tokens (light and dark), type, layout, components, status colours, charts, sign-in, PWA |
| `assets/app/sag-app.css` | Drop-in stylesheet for any SAG web app (tokens + components) |
| `examples/sag-app-example.html` | Reference app screens: dashboard, form, sign-in, light and dark |
| `assets/logo/` | `sag-logo.png` (light grounds), `sag-logo-plated.png` (any ground) |
| `assets/graphics/` | `masthead_blue.png`, `closing_blue.png`, `deck_band_blue.png` |
| `assets/fonts/` | Plus Jakarta Sans, 5 weights + OFL licence |
| `assets/reference/` | Reference `.docx` `.pdf` `.pptx` and previews, plus a sample MoM |
| `scripts/palette.py` | Colour roles (`BLUE`, alias `SAG`), font family names, geometry |
| `scripts/cline.py`, `graphics.py` | Complexity Line generator; masthead / closing / deck band images (masthead takes the date) |
| `scripts/sagdoc.py` | OOXML helpers: rounded panels, tables, `picture()`, `table(lmar=)`, font embedding |
| `scripts/components.py`, `brands.py` | `BrandDoc`: masthead, tiles, callout, band, kv, data_table, item, bullets, roadmap, sign_row, contact panel, running header/footer |
| `scripts/build_doc.py`, `build_mom.py`, `build_deck.py` | Reference A4 document, worked MoM, seven-layout deck |
| `scripts/build_example_html.py` | Rebuilds the HTML example |

## 2. Non-negotiables
1. **Plus Jakarta Sans only.** Select the weight by family name; only 700 uses the bold flag. Never set bold on ExtraBold.
2. **Colour roles only:**
   - PAPER EFF4F1
   - PANEL 1B382A
   - INK 161A19
   - BODY 2C5040
   - META 3A604E
   - MUTED 636C68
   - TINT E2E7E4
   - RULE 8FAB9E
   - PALE B8CCC3
   - ACCENT F9C939
   - GOLD C9A227
3. **SAG Yellow is an accent only:** the tagline and short rules. Never set it as text on light (1.7:1), never use it as a large fill, and keep it to a few marks per page.
4. **Complexity Line:** horizontal, always with "NAVIGATING COMPLEXITY, DELIVERING SIMPLICITY". Use the supplied images or `cline.py`; never redraw it.
5. **Logo fixed:** `sag-logo.png` on light grounds, `sag-logo-plated.png` on any ground.
6. **Geometry:** A4 margins 20/20/14/16 mm with a **170 mm measure** (edges at 20 and 190 mm). Slides 338.667 × 190.5 mm with 18 mm margins.
7. **Corner radius:** 2.5 mm on documents, 3 mm on slide cards.
8. **No decoration:** no stripes, shadows, gradients, icons or clip art, and no borders other than the named hairlines.
9. **Logo builds and clear space:** never `sag-logo.png` on a colour; keep half the shield's height clear; minimum 14 mm print, 28 px screen. Never stretch, recolour, redraw or merge it with a partner mark (`references/BRAND_SYSTEM.md` §1).
10. **Name:** spell *Stratcon Agara Global* for clients and ministries; "SAG" is internal; "PT" only in footers, signatures, contracts and the stamp.

## 3. Building Word documents
Two routes, both in `scripts/` (imports resolve when you run from that folder or put it on `sys.path`):

- **Reference document** — `build_doc.py` builds the questionnaire-style A4 reference; `build(out, C=CONTENT)` takes a content dict, so copy `CONTENT` and swap the text. The masthead date is regenerated from `C["date"]`.
- **Any other document (minutes, reports, proposals)** — use `BrandDoc` from `components.py`; `build_mom.py` is the worked example and the pattern to copy:

```python
from brands import SAG
from components import BrandDoc
d = BrandDoc(SAG, kind="Report", title="Short title", date="30 SEPTEMBER 2026")
d.masthead(); d.title_block("EYEBROW", "Title", "Prepared for ", "Client")
d.intro(["Text with **bold** runs."]); d.tiles([("46", "ENGAGEMENTS", "Delivered")])
d.callout("HEADLINE", ["**Opportunity.** ..."]); d.band("Section", "Subtitle")
d.kv([...]); d.data_table(headers, rows, widths, marks=(2,))   # widths in mm, must total 170; d.item("Question", "POSITION GIVEN", "Answer")
d.roadmap(phases); d.sign_row([...]); d.contact_panel(...); d.closing(); d.save("out.docx")
```

Document flow: masthead → eyebrow / title / subtitle → three-bar rule → intro → tiles and callout → section bands → numbered items with response boxes, kv, data_table, bullets → notes → contact panel → closing band. Tell the user which extended components you used (kv, data_table, tiles, roadmap, sign_row, status marks).

Then convert and check: `soffice --headless --convert-to pdf out.docx`. Fonts are embedded in the .docx, so recipients need nothing installed.

### Alignment rules (these are what made boxes misalign before)
- Insert pictures with `sagdoc.picture()` (zero dist attributes); LibreOffice otherwise shifts inline images about 3 mm right.
- For tables whose first cell has left padding use `table(…, lmar=pad)` so the box sits flush in both Word and LibreOffice.
- Fixed-height shapes (tiles, callouts, panels) don't grow, so size them from the text. `callout()` estimates its own height; the contact panel is 38.5 mm so four lines never clip.
- Rows of shapes (tiles, roadmap) total 169.6 mm with the gaps as noFill shapes, so they never wrap.

## 4. Building decks
- **.pptx:** `build_deck.py` has seven layouts (`cover`, `divider`, `content`, `two_col`, `stat_cards`, `case_study`, `closing`). `stat_cards` takes 1 to 8 `(value, label)` pairs in rows of up to four, and numbers shrink to stay on one line. `case_study` takes the client, a meta line, challenge / what SAG did / outcome, and optionally up to 4 stats, up to 2 photos (cropped to fill) and a client logo file (without one the client name is set in ExtraBold INK). Write a `compose(prs)` that calls them and pass it to `build(out, compose)`. Tell the user to install the fonts (or run `install_fonts.py`) before opening the .pptx, since PowerPoint cannot embed them the way Word does.
- **Claude Slides artifact (1920 × 1080 canvas):** map the spec exactly with **1 mm = 5.669 px, 1 pt = 2 px**. `examples/sag-brand-example.html` contains all five slides in this mapping, ready to lift.
  - Font: Google Fonts `Plus+Jakarta+Sans:wght@400;500;600;700;800`; stack `'Plus Jakarta Sans', Arial, sans-serif`.
  - Every section uses `padding:0px` with pinned blocks:
    - margins at left 102, width 1716
    - eyebrow + headline block at top 113: eyebrow 19px 800 META, letter-spacing 3.2px, uppercase; headline 56px 800 INK, −1.2px, line-height 1.1, gap 10
    - accent rule 193 × 7 ACCENT at top 306
    - body at top 363 (cards at 397), ending by y 975
    - footer: 2px RULE line at top 1000; at top 1016, 16px MUTED "Navigating complexity, delivering simplicity" on the left and "PT Stratcon Agara Global" on the right. No page numbers.
  - Cards: TINT, radius 17, padding 45/51. Card rule 91 × 7 ACCENT, then 39px, then heading 30px 800 INK and body 22px BODY at line-height 1.3.
  - Bullets are `—` in RULE plus three `&#160;`, with the text in BODY: 26px on content slides, 22px in cards.
  - Cover and closing: PANEL ground. `deck_band_blue.png` full-bleed at top 785, height 295; plated logo at (102, 113), 86 × 102. Cover: wordmark 22px PALE; title 80px PAPER; subtitle 30px PALE; date top-right 19px. Closing: contact block from top 295.
  - Divider: 9px ACCENT bar across the top; number 108px META, title 68px PAPER, subtitle 28px PALE, at top 393, height 295.
  - Separators and multiple spaces need `&#160;` (HTML collapses spaces).
  - Upload assets from the scratchpad (paths under /tmp elsewhere are refused) and reuse the returned `/_blob/` URLs.
  - Verify before showing: render all slides with Playwright to one HTML page, swapping blob URLs for local files and the TTFs via @font-face. Flag elements past y 985 or off-canvas, look at contact sheets, then fix.
- **Deck extensions already accepted** (reuse rather than inventing new ones):
  - stat cards: a big ExtraBold number in INK on a TINT card, label in BODY
  - case-study layout: photos and stat cards on the left (760 px), then client logo + meta, challenge / what SAG did / outcome on the right
  - PANEL section bands used as org-chart headers
  - logo wall: a 6-column grid of TINT tiles with logos contained; a client with no logo file gets its name as an ExtraBold INK tile. When the count doesn't fill the rows, use flex-wrap with centred rows of 224 px tiles (e.g. 7 + 6) rather than leaving an orphan
  - grids of 4 or more cards drop the yellow card rule so yellow stays to a few marks
- Section dividers must carry real content; a bare number and title reads as empty to SAG. Otherwise drop them and let the eyebrows carry the section.
- Put a named contact on the contact panel only when the user confirms it.

## 5. Apps and web UI
For any app, internal tool, dashboard, admin page or PWA, read `references/APP_DESIGN.md` first and start from `assets/app/sag-app.css` (copy it in, or inline it in single-file apps). `examples/sag-app-example.html` shows the result.
- The bar is modern product software (Linear, Stripe): crisp, dense, keyboard-friendly. A light grey app ground (`#F3F5F3`) with the work on one inset white panel; a sidebar with the shield in the workspace switcher; 52 px header bars with breadcrumb, view switcher and one primary action; 42 px rows grouped by status; a detail panel with properties and an activity history; a ⌘K palette; a create dialog with property pills.
- SAG yellow means **critical path**: the ◆ marker on rows and the bars on the timeline. Never a button, never text on light, never a status, never chrome decoration.
- Status uses its own glyphs and colours (not started ◌, in process ◐, issued ✓, at risk !), always with a word somewhere.
- Plus Jakarta Sans 400–800, 13–14 px UI type, tabular figures. Lucide outline icons in grey. Two soft elevation levels, no gradients or emoji. Light by default; dark only as an opt-in theme.
- The Complexity Line appears only on the sign-in screen, as a slate strip along the foot (`deck_band_blue.png`).
- Check 390 px wide (and the dark theme, if offered) before showing the user.

For logo builds, naming, the Office theme, schedules, business cards, letterhead and the stamp, see `references/BRAND_SYSTEM.md`.

## 6. SAG content rules
- Andi Prasetyo prefers a background, supporting role:
  - frame the work as SAG's
  - where a title is needed, use his business-card title, Chairman (confirmed by the user, 2 Oct 2026); otherwise don't single him out
  - where the SAG BOOK names him, keep the book's wording and name him once at most
- Jagorawi toll-road land clearance (1978) is **"SAG legacy"**, with no names. Don't call land acquisition "eminent domain"; use "land acquisition and clearance for public-interest infrastructure" (Law No. 2 of 2012).
- Galang Batang (Nanshan Group, Bintan KEK): no site photos, for privacy; describe facility types instead. The Nanshan Group logo is approved for the case study and the logo wall.
- Where sources disagree, the SAG Company Overview figures win (e.g. 46 engagements, IDR 1.5T+, USD 33B, 700K+ m², 10,000+ jobs).
- Sources (ask the user to attach them when needed; they are not bundled):
  - case studies, key experts, specialist bench and photos: SAG BOOK.pdf (`pdfimages`, then crop the baked-in captions)
  - partners and headshots: SAG_Company_Overview.pdf
  - client logos: the SAGxThryve.pdf ending page (combine each image with its smask)
  - FDE team: SAG_AI_FDE_Team.pdf
- **Never name or show supplier/partner companies on service pages.** SAG resells their products (EV chargers, cable), and naming them lets clients go direct. Present the offering as SAG's own ("supplied by SAG", "what we supply"), with no partner logos, "through partners" wording or placeholders. Company names and logos are fine in case studies.
  - internal only, never in client-facing output: EV charging from Bescore; cable from PT Damai Cable Indonesia
- CECEP is under NDA: never name it. Describe it by its work, e.g. "a Chinese state-owned clean-energy and environmental group".
- Names carry no academic titles (Dr., S.H., S.E.), for consistency. In "how we work" visuals, SAG sits in the middle, between the client and government.
- Mark projections as projections (e.g. the Mamuju cooperative figures) and concept visuals as concepts (Jasa Marga fibre image).

## 7. Verify
- Render every page (`pdftoppm -r 60`) and look at them; build a contact sheet for long documents.
- Measure edges with pdfplumber (20.0 / 190.0 mm).
- Check nothing is clipped, no band is orphaned at a page foot, no question is separated from its box, yellow is used with restraint, and `pdffonts` lists only Plus Jakarta Sans.
- For minutes of meeting, the `meeting-minutes-mom` skill defines the content structure; this skill supplies the look (`build_mom.py`).
