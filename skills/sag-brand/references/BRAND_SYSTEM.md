# SAG Brand System — identity rules beyond the build spec

`DESIGN_SPEC.md` holds every number for Word, PDF and PowerPoint. This file
holds the identity rules around it: logo use, naming, the extended colour
notes, the Office theme, schedules, business cards and the stamp. It merges
the **Agara Identity System v2** and the **Template Pack v2** (Ahmed Khalifa,
7–8 Sep 2026; archived in `original-package/`) into the agreed Graphite &
Slate system.

**Precedence:** `DESIGN_SPEC.md` and `SKILL.md` > this file > the archived v2
pages. §9 lists every v2 value that the agreed system replaced.

---

## 1. The logo stays exactly as it is

No redraw, cleanup or "refinement". The shield carries a yellow-to-amber
gradient (`#F8AF41` lower-left → `#F5E334` upper-right; `#F9C939` dominant,
which is where SAG Yellow comes from), a diagonal band, and a second shield
outline nested inside the first. It has no attached wordmark.

### Two builds of one artwork

The diagonal band and the ring between the outlines are **transparent** in
the original. On a dark or coloured ground they fill with that ground and the
shield collapses into a blob. So the same artwork ships in two builds:

| Build | File | Use on |
|---|---|---|
| A, as supplied (interior transparent) | `assets/logo/sag-logo.png` | White and `PAPER` only: Word documents, letterhead, ministry filings |
| B, plated (interior filled white) | `assets/logo/sag-logo-plated.png` | Every other ground: `PANEL` slides, app top bars, photos, yellow |

The single mistake worth guarding against is Build A on a colour.

### Clear space and minimum size
- Keep half the shield's height clear on all four sides: no text, rules or photo edges.
- Minimum **14 mm** in print and **28 px** on screen. Below that the ring closes up and the shield reads solid.
- Favicons (16–48 px) put the shield on a solid `#F9C939` tile rather than using the shield alone.

### Misuse: never
- stretch, squash, rotate or tilt it
- redraw or trace it (use the supplied files)
- recolour it, for a client's sector or anything else
- put Build A on a colour
- merge it with a partner mark into one graphic

## 2. Name and lockup

- **Lockup:** shield + *Stratcon Agara Global* in Plus Jakarta Sans 800, tracking −0.035 em, stacked on two lines (*Stratcon / Agara Global*) or on one.
- **"PT" stays off the mark.** The legal form belongs in footers, signature blocks, contracts and the stamp.
- **"SAG" is internal:** file names, reference codes, internal decks and internal tools. In front of a ministry or a new client, spell the name.
- **Descriptor** (where one is needed): *Regulatory · Government Relations · ESG*.
- **Website:** **stratconagaraglobal.com**, printed lowercase with no `https://` or `www.`, and linked to `https://stratconagaraglobal.com` wherever the medium allows. Corporate mail: corporate@stratconagaraglobal.com.
- **Co-branding:** partner marks sit to the right, separated by a hairline and optically matched on cap height. SAG leads on SAG-issued documents. Partner names follow the content rules in `SKILL.md` §6 (none on service pages; fine in case studies).

## 3. Colour notes

The 11 roles in `DESIGN_SPEC.md` §1 are the palette. Adopted from v2:

- **Proportion.** Roughly 50 % paper/white, 30 % slate, 17 % graphite, 3 % yellow. If a page reads as a yellow page, something has gone wrong.
- **Yellow never carries text on a light ground and never sits under white text** (1.6:1 either way). The only text pairing with yellow is `INK` on `ACCENT` (11.4:1), which is reserved for small marks such as a tag on a dark slide.
- **Print values** for `ACCENT #F9C939`: RGB 249·201·57, CMYK 0·20·85·0, ≈ Pantone 116 C. `INK #16181A`: CMYK 70·60·55·80, ≈ Black 6 C. `PANEL #1B3038`: CMYK 85·62·50·45, ≈ Pantone 5463 C. These are nearest coated matches; confirm on a wet proof, since yellows shift on press more than any other hue.
- **Status colours** for permit trackers, in documents as well as apps, sit deliberately outside the palette: see `APP_DESIGN.md` §3.

## 4. Typography notes

`DESIGN_SPEC.md` §2 sets the sizes. Adopted from v2:

- Hierarchy comes from weight. With one family, a two-weight jump does the job a second typeface would.
- **Tabular figures** in every table, tracker and fee schedule (Word: *Font → Advanced → Number forms*; web: `font-variant-numeric: tabular-nums`). Permit dates and rupiah columns must align.
- **Licence:** SIL OFL. Install on every workstation, embed in PDFs, and use on the web. No per-seat cost.
- **Fallbacks:** Aptos (current Office), then Calibri; on the web `"Plus Jakarta Sans", Aptos, "Segoe UI", system-ui, sans-serif`. Send anything final as PDF with fonts embedded.
- Decks: nothing below 11 pt; six bullets at most, one line each. If it needs more, it's a document.

## 5. Office theme (SAG.thmx)

Set once under *Design → Colors → Customize Colors* in Word and PowerPoint, save as `SAG.thmx`, and set Plus Jakarta Sans in both the heading and body font slots. Every chart, table and shape then inherits the palette. The accents are ordered so default charts start in slate, not yellow.

| Theme slot | Role | Hex |
|---|---|---|
| Text/Background — Dark 1 | INK | `16181A` |
| Text/Background — Light 1 | White | `FFFFFF` |
| Text/Background — Dark 2 | PANEL | `1B3038` |
| Text/Background — Light 2 | PAPER | `EFF3F4` |
| Accent 1 | PANEL | `1B3038` |
| Accent 2 | RULE | `8FA3AB` |
| Accent 3 | GOLD | `C9A227` |
| Accent 4 | META | `3A5560` |
| Accent 5 | PALE | `B8C6CC` |
| Accent 6 | ACCENT | `F9C939` |
| Hyperlink | META | `3A5560` |
| Followed hyperlink | MUTED | `63696C` |

## 6. Schedules and trackers

The same three meanings in every deck, document and app:

- **Yellow (`ACCENT`) = critical path**
- **Slate (`PANEL`) = parallel filings**
- **Grey (`PALE`) = passive monitoring**

Permit trackers use `data_table` with a PANEL header row, tabular figures, and status in the status colours, never brand yellow. Mark dates and statuses as illustrative whenever they are.

## 7. Business card — 90 × 55 mm

| | |
|---|---|
| Trim | 90 × 55 mm (Indonesian standard) |
| Bleed | 3 mm all round (96 × 61 mm artboard) |
| Safe area | 4 mm inside trim |
| Stock | 350 gsm, matt laminate |
| Type | Name 12 pt 800; role 7.5 pt 600; contact 7.5 pt 400; all Plus Jakarta Sans |
| Output | CMYK, 300 dpi, fonts outlined, crop marks |

- **Front:** flat `PANEL` ground (no gradient). Plated logo (Build B) 10 mm high with the two-line wordmark in PAPER at top-left; name in 800 PAPER and role in 600 PALE at the foot; one `ACCENT` edge bleeding off the right. The yellow edge must bleed, or a 0.5 mm mis-cut shows white. The name and role are the only things that change between staff.
- **Back:** the Complexity Line with the tagline (`cline.py`) on `PANEL`. No contact details, no second logo.
- **Contact face** (when the back must carry details): `PAPER` stock, Build A logo, a short `GOLD` rule, email in 600 `INK`, phone, stratconagaraglobal.com and address in 400 `BODY`. Never set the email in gold or yellow.
- Titles come from the person's business card as confirmed (see `sag-graphify`). No academic titles in names.
- If gold foil is used, it replaces the rule only. Never foil the shield, which already carries its own yellow.

The 2026 printed batch (Playfair serif, navy) predates this system; reprint to this spec at the next order.

## 8. Letterhead and stamp

- **Letterhead (A4):** Build A logo + lockup top-left; address, website (stratconagaraglobal.com) and phone top-right in 400 `MUTED`; a reference block (Ref / Date / Attn) in tabular 500; one short `ACCENT` rule as the whole brand statement. Everything below it is `INK` on white so a ministry reads the letter, not the letterhead. Margins and measure follow `DESIGN_SPEC.md` §3 (20 / 20 mm, 170 mm). The footer reads *PT Stratcon Agara Global · Jakarta, Indonesia* with page *n of m*.
- **Reference codes:** `SAG/<type>/<year>-<nnnn>`, e.g. `SAG/RR/2026-0011` (RR = regulatory roadmap, RA = regulatory affairs letter).
- **Company stamp (cap perusahaan):** 38 mm, the shield inside the ring at 45 % scale with *STRATCON AGARA GLOBAL* and *Jakarta · Indonesia*. It is one ink, so hand the maker Build B as single-colour SVG and ask for a proof impression before the batch. It is used on signed letters, powers of attorney and OSS submissions.

## 9. What v2 had that the agreed system replaced

Don't reintroduce these; they are recorded so nobody mistakes the archive for current.

| v2 value | Agreed value |
|---|---|
| Paper `#F3F3F1` | `PAPER #EFF3F4` |
| Bronze `#7A5C0E` for eyebrows on white; Amber `#E9A227` second plane | Not in the palette. Eyebrows are `META`; charts use §5 |
| Weights 200 / 300 (ExtraLight, Light ledes) | 400–800 only (the five bundled weights) |
| A4 margins 25 / 22 / 20 mm, 150 mm measure | 20 / 20 / 14 / 16 mm, **170 mm** measure |
| Deck body 15 pt; yellow square bullets | 13 pt; `—` dash bullets in `RULE` |
| Section divider: full-bleed yellow | `PANEL` with a 1.6 mm `ACCENT` rule across the top |
| Cover: graphite-to-slate gradient | Flat `PANEL`; no gradients anywhere |
| Six deck masters | Seven layouts in `build_deck.py` (incl. stat cards and case study) |
| Edition B "Earth & Botanical" (forest green, ivory) | Not adopted. Graphite & Slate is the one SAG palette; AGM has its own skill |
| Gradient card fronts | Flat `PANEL` |
