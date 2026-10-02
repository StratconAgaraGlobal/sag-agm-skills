# Changelog

## 2026-10-02
- Added **sag-graphify** (SAG knowledge and Graphify workflow, compiled 1 Oct 2026).
- **sag-brand**: synced the latest content rules (logo-wall layout, no supplier or partner names on service pages, CECEP under NDA, no academic titles in names).
- README: shared SAG / AGM graph section.
- **sag-graphify**: resolved four open items: Parga = Pargata, Bitera site area 8,200 m² (per the MoM), cable partner PT Damai Cable Indonesia (internal only), ship logo is AGM's.

## 2026-09-30
- **sag-brand**: now fully self-contained. The design package (fonts, logos, graphics, code, spec, references) is bundled; Plus Jakarta Sans installs itself with `scripts/install_fonts.py` (skips weights already installed). Added an HTML example (`examples/sag-brand-example.html`), `BrandDoc` components and a worked MoM builder.
- **agm-brand**: rebuilt to the same standard, with Seafood and Marine editions, bundled emblem, photos, device graphics, build code and an HTML example.
- **meeting-minutes-mom**: points at the bundled `build_mom.py` in each brand skill.
- Repo: README, packaging tool, smoke test and CI workflow.
