# Changelog

## 2026-09-30
- **sag-brand**: now fully self-contained. The design package (fonts, logos, graphics, code, spec, references) is bundled; Plus Jakarta Sans installs itself with `scripts/install_fonts.py` (skips weights already installed). Added an HTML example (`examples/sag-brand-example.html`), `BrandDoc` components and a worked MoM builder.
- **agm-brand**: rebuilt to the same standard, with Seafood and Marine editions, bundled emblem, photos, device graphics, build code and an HTML example.
- **meeting-minutes-mom**: points at the bundled `build_mom.py` in each brand skill.
- Repo: README, packaging tool, smoke test and CI workflow.
