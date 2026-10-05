> **Archived.** This is the original design package as delivered, before it was bundled into this skill. Its paths are out of date: code is now in `scripts/` and reference files are in `assets/reference/`. Follow `SKILL.md` instead.
>
> Also archived here: `SAG_Identity_System_v2.html` and `SAG_Template_Pack_v2_Graphite.html` (7–8 Sep 2026), the earlier identity pages. What survived from them is in `references/BRAND_SYSTEM.md`, whose §9 lists what the agreed system replaced.

# SAG Design Package — Graphite & Slate

Everything another designer or AI assistant needs to produce Word documents
and PowerPoint decks in PT Stratcon Agara Global's Graphite & Slate identity,
and get the same result each time.

Built 29 September 2026.

---

## Start here

| If you want to | Open |
|---|---|
| Hand this to an AI assistant | `INSTRUCTIONS_FOR_AI.md` — a prompt to paste, plus what to attach |
| Look up an exact value | `DESIGN_SPEC.md` — colour, type, geometry, component sizes |
| See what it should look like | `reference/previews/` |
| Rebuild the reference files | `code/` — see *Running the build* below |

---

## What's in the box

```
SAG_Design_Package_Blue/
├── README.md                  this file
├── INSTRUCTIONS_FOR_AI.md     the prompt to give another assistant
├── DESIGN_SPEC.md             the full specification
├── assets/
│   ├── fonts/                 Plus Jakarta Sans, 5 weights + OFL licence
│   ├── logo/                  sag-logo.png, sag-logo-plated.png
│   └── graphics/              masthead, closing band, deck band
├── reference/
│   ├── SAG_Document_Blue.docx / .pdf    A4 reference, every component once
│   ├── SAG_Deck_Blue.pptx     / .pdf    16:9 reference, five layouts
│   └── previews/              page and slide images
└── code/
    ├── palette.py             colour roles, font families, geometry
    ├── cline.py               the Complexity Line generator
    ├── graphics.py            masthead and band images
    ├── sagdoc.py              OOXML helpers for Word
    ├── build_doc.py           builds the A4 reference
    └── build_deck.py          builds the deck reference
```

## The two logo builds

`sag-logo.png` has a transparent interior — the diagonal stripe shows whatever
is behind it, so it belongs on white or `PAPER` grounds only.
`sag-logo-plated.png` is flood-filled white behind the shield and works on any
ground, including `PANEL`. Neither may be recoloured or redrawn.

## Fonts

Plus Jakarta Sans, SIL Open Font Licence 1.1 (`assets/fonts/OFL.txt`) — free
to use, embed and redistribute. Install all five weights; each is a separate
Windows family and the design uses four of them. The reference `.docx` embeds
them, so anyone you send it to sees the right type without installing
anything.

## Running the build

Needs Python with `python-docx`, `python-pptx` and `Pillow`:

```bash
pip install python-docx python-pptx Pillow
cd code
python graphics.py      # regenerate the banner images
python build_doc.py     # -> reference/SAG_Document_Blue.docx
python build_deck.py    # -> reference/SAG_Deck_Blue.pptx
```

To produce a real document rather than the reference, edit the `CONTENT`
dictionary at the top of `build_doc.py`, or the calls at the bottom of
`build_deck.py`. The layout holds as long as the structure does.

The reference files were rendered through Word and PowerPoint themselves, not
a converter, so what is in `reference/previews/` is what those applications
actually produce.

## The other edition

This package is the **Graphite & Slate** ("blue") edition only. There is a
second, **earth** edition in the same system — forest green and warm ivory,
used for environmental and carbon work. The two share every dimension, weight
and component; only the eleven colour roles differ. To build that edition,
swap the palette in `code/palette.py`.
