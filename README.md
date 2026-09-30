# SAG and AGM skills

Claude skills for the SAG Group's documents.

| Skill | Use it for |
|---|---|
| `sag-brand` | Anything for PT Stratcon Agara Global: Word, PDF, PowerPoint, Claude Slides, HTML, minutes. Graphite & Slate brand. |
| `agm-brand` | Anything for PT Agara Global Maritim, in the Seafood or Marine edition. Same structure as SAG, with AGM's colours, emblem and photography. |
| `meeting-minutes-mom` | Minutes of Meeting content and structure. Uses the look from whichever brand skill applies. |

Each brand skill is **self-contained**: fonts, logos, photos, graphics, build code, the design spec, reference files and an HTML example are all inside the skill folder. Nothing else needs to be downloaded or attached. Plus Jakarta Sans installs itself the first time it is needed; weights that are already installed are skipped.

## Install

**Claude desktop / Cowork (easiest).** Get the `.skill` files (run `python tools/package_skills.py`, or take them from a release), then in Claude open *Settings → Capabilities → Skills → Upload skill* and add each file.

**Claude Code.** Copy the folders into your skills directory:

```bash
cp -r skills/* ~/.claude/skills/        # macOS / Linux
xcopy skills\* %USERPROFILE%\.claude\skills\ /E /I     # Windows
```

## Use

Just ask. Mention SAG, AGM, or the type of document and the skill loads: "Write a proposal for AGM's sea cucumber export programme", "Make the SAG MoM for today's meeting as a Word file and PDF", "Build a SAG deck from this outline".

To see what a brand looks like, open `skills/<name>/examples/<name>-example.html` in any browser. It has the logo builds, colours, type, an A4 document and the deck layouts (AGM has a Seafood / Marine switch).

## What happens on first run

The skill runs `scripts/install_fonts.py`:

1. Checks each of the five Plus Jakarta Sans weights and skips any already installed.
2. Downloads the missing ones from Google Fonts.
3. If Google Fonts cannot be reached, uses the copies in `assets/fonts` (OFL licensed). It never blocks the work.

Installs are per-user (no admin rights needed). Word files embed the fonts, so recipients need nothing. PowerPoint cannot embed fonts, so anyone opening a `.pptx` should run the installer first.

Requirements for building files: Python 3.9+, `python-docx`, `python-pptx`, `Pillow`, and LibreOffice (`soffice`) for PDF conversion.

## Repo layout

```
skills/
  sag-brand/            SKILL.md, scripts/, assets/, examples/, references/
  agm-brand/            same layout, plus both editions
  meeting-minutes-mom/  SKILL.md
tools/package_skills.py zips each skill to dist/<name>.skill
tests/smoke_test.py     builds every document, deck and example for both brands
.github/workflows/      runs the smoke test on every push
```

## Maintaining

- Edit a skill in `skills/<name>/`, run `python tests/smoke_test.py`, then `python tools/package_skills.py`.
- If you change `example_template.html` or the assets, rebuild the example with `python scripts/build_example_html.py` inside that skill.
- Both brand skills share `components.py` (`BrandDoc`); keep the two copies in step.

## Known limits

- The AGM emblem files are PNG recovered from AGM's finished documents. If the vector artwork arrives, replace the files in `assets/logo` under the same names.
- Only two AGM photographs are bundled. Add more via an `Edition` subclass in `brands.py`.
- The SAG deck stat-card and case-study layouts are described in `SKILL.md` but not yet coded in `build_deck.py`.

See `LICENSE-NOTES.md` for licensing.
