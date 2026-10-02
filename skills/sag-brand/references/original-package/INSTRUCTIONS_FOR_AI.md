> **Archived.** This is the original design package as delivered, before it was bundled into this skill. Its paths are out of date: code is now in `scripts/` and reference files are in `assets/reference/`. Follow `SKILL.md` instead.

# Instructions for an AI assistant

Paste the block below into a new conversation, and attach `DESIGN_SPEC.md`
plus the `assets/` folder. If the assistant can run code, attach `code/` too
and it can reproduce the reference files exactly.

---

## The prompt

> You are producing a document for **PT Stratcon Agara Global (SAG)**, an
> Indonesian strategic advisory and regulatory affairs consultancy. Everything
> you produce must follow the SAG **Graphite & Slate** design system, which is
> fully specified in the attached `DESIGN_SPEC.md`. Read that file before you
> write any code, and treat every number in it as exact.
>
> **What I want:** <describe the document or deck here — its purpose, its
> audience, and its content>.
>
> **Non-negotiables:**
>
> 1. **Typeface.** Plus Jakarta Sans, and nothing else. It ships each weight
>    as a separate Windows font family, so select weight by family name
>    (`Plus Jakarta Sans ExtraBold`, `... SemiBold`, `... Medium`), not by
>    turning bold on. Only weight 700 uses the bold flag. The TTF files are in
>    `assets/fonts/`.
> 2. **Colour.** Use only the eleven roles in section 1 of the spec, for the
>    jobs listed there. SAG Yellow `#F9C939` is an accent: the Complexity Line
>    tagline and short accent rules. Never as text on a light ground, never as
>    a large fill, never more than a few small marks per page.
> 3. **The Complexity Line.** Tangled strands resolving into one line, always
>    carrying "NAVIGATING COMPLEXITY, DELIVERING SIMPLICITY". Horizontal only.
>    Use the ready-made images in `assets/graphics/`, or regenerate with
>    `code/cline.py`. Never redraw it by hand and never use it without the
>    tagline.
> 4. **The logo is fixed.** Use the supplied files unchanged — never recolour,
>    redraw or reproportion the shield. `sag-logo.png` has a transparent
>    interior and goes on light grounds only; `sag-logo-plated.png` is
>    flood-filled white and works on any ground.
> 5. **Geometry.** A4 with 20 mm side margins and a 170 mm measure; 16:9 slides
>    at 338.667 × 190.5 mm with 18 mm side margins. Every full-width element
>    is exactly the measure — no element may stop short of it.
> 6. **Corner radius** 2.5 mm on document panels, 3 mm on slide cards.
> 7. **No decorative furniture.** No coloured stripes down the left edge of
>    panels, no drop shadows, no gradients, no icons, no clip art, no borders
>    except the hairlines named in the spec.
>
> **If you are producing a Word file,** read section 5 of the spec first. Word
> cannot round a table corner, so rounded panels are DrawingML `roundRect`
> shapes in `wp:inline`, inserted before `w:sectPr`. Response boxes stay as
> real tables so they grow as someone types. Build with `python-docx` plus raw
> OOXML; `code/sagdoc.py` already has the helpers.
>
> **If you are producing a deck,** build with `python-pptx`; `code/build_deck.py`
> has the five layouts.
>
> **Before you show me anything,** render it to PDF, look at the pages, and
> check: nothing clipped, nothing overflowing its panel, every full-width
> element reaching 170 mm (or 302.667 mm on slides), no question separated
> from its response box, and the type rendering in Plus Jakarta Sans rather
> than a substitute.
>
> Match the reference files in `reference/` exactly in look. If something in
> my content does not fit a component in the spec, tell me which component you
> extended and why, rather than inventing a new visual language.

---

## If the assistant cannot run code

Give it the same prompt, then ask for the **content structured to the
components** instead of a file — eyebrow, title, subtitle, intro paragraphs,
callout, contents rows, section bands, numbered items, notes, contact. Run
`code/build_doc.py` or `code/build_deck.py` yourself with that content
swapped into the `CONTENT` / `SLIDES` block at the top.

## What "the same result" depends on

Three things, in order of how often they go wrong:

1. **The fonts.** Without Plus Jakarta Sans installed, everything substitutes
   and nothing looks right. Install the five TTFs in `assets/fonts/`, or keep
   font embedding switched on in the build so recipients do not need them.
2. **The measure.** 170 mm on A4 and 302.667 mm on slides. Most drift starts
   with an element that stops 2 mm short.
3. **The restraint on yellow.** It is the fastest way to make the system stop
   looking like itself.
