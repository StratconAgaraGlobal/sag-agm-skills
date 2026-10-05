# Changelog

## 2026-10-05 (graph)
- **sag-graphify: graph merged and bundled.** Ahmed's company-profile graph (SAG BOOK, visual profile, 23 profile sections, two peer-firm profiles) is merged with this skill's curated facts and now ships in `skills/sag-graphify/graph/`. That means current card titles (book titles kept as superseded), the alias table (CCP → CECEP, Uncle Johnson → Jhonshan …), the 46-engagement ruling, Diovandi, Yandra, the three Consulting Partners, the FDE team, and the SEECON, Kadin and Bitera meetings. The result is 1,030 nodes, 2,391 edges and 54 named communities, and every section 15 check passes. The curated facts are also in `graph/curated/`. The skill's query instructions now use `--graph` and `--undirected`. Added the MI / Masagena expert-overlap finding to section 3b.

## 2026-10-05
- **Auto-update:** the repo is now a Claude plugin marketplace (`.claude-plugin/marketplace.json`, plugin `sag`, no pinned version). It works with claude.ai organization sync (every push to `main` reaches everyone) and with Claude Code auto-update. The README has the three install routes. A new `release-skills` workflow publishes the `.skill` files to a rolling `latest` release on every push to `main`. The smoke test checks that the manifest lists every skill.
- **sag-brand: apps redesigned as modern product UI** (Linear / Stripe level). Inset work panel on a light grey ground, a sidebar with workspace switcher and ⌘K search, status-grouped 42 px rows with custom status glyphs, a ◆ critical-path marker in SAG yellow, a detail panel with activity history, a Gantt timeline (yellow = critical path, slate = parallel, today line), a create dialog with property pills, a command palette, and a refined sign-in. Light by default, dark opt-in, phone layouts checked.
- **sag-brand: apps.** New `references/APP_DESIGN.md` (screen tokens for light and dark, type, layout, components, status colours, charts, sign-in, PWA, accessibility, and a migration list for the existing SAG apps), the drop-in `assets/app/sag-app.css`, and `examples/sag-app-example.html` (dashboard, form, sign-in). SKILL.md has a new §5, Apps and web UI; content rules are now §6 and Verify §7.
- **sag-brand: brand system merged.** New `references/BRAND_SYSTEM.md` brings in Ahmed Khalifa's Identity System v2 and Template Pack v2 (7–8 Sep 2026): logo builds, clear space, minimum sizes and misuse; naming (PT, SAG, co-branding); print colour values; Office theme `SAG.thmx`; schedule colours; business card; letterhead and stamp. Its §9 lists every v2 value the agreed system replaced. The v2 pages are archived in `references/original-package/`. Two non-negotiables were added: logo builds and clear space, and name usage.

## 2026-10-02
- Docs audit fixes: contact panel is 38.5 mm everywhere (spec, HTML examples, sag reference builder); `components.py` import hint for AGM; AGM reference-file list; stale `code/` paths; archived-package notes; Andi Prasetyo shown by his card title, Chairman; sample contact is Ahmed Khalifa, Technical Manager, with no prefix; README install, shared-file and known-limits notes; smoke test log shows the edition.
- **sag-brand**: `build_deck.py` now builds the stat-card (`stat_cards`) and case-study (`case_study`) layouts; the reference deck shows both. The smoke test covers every stat count, photo and logo combination.
- Added **sag-graphify** (SAG knowledge and Graphify workflow, compiled 1 Oct 2026).
- **sag-brand**: synced the latest content rules (logo-wall layout, no supplier or partner names on service pages, CECEP under NDA, no academic titles in names).
- README: shared SAG / AGM graph section.
- **sag-graphify**: resolved four open items: Parga = Pargata, Bitera site area 8,200 m² (per the MoM), cable partner PT Damai Cable Indonesia (internal only), ship logo is AGM's.

## 2026-09-30
- **sag-brand**: now fully self-contained. The design package (fonts, logos, graphics, code, spec, references) is bundled; Plus Jakarta Sans installs itself with `scripts/install_fonts.py` (skips weights already installed). Added an HTML example (`examples/sag-brand-example.html`), `BrandDoc` components and a worked MoM builder.
- **agm-brand**: rebuilt to the same standard, with Seafood and Marine editions, bundled emblem, photos, device graphics, build code and an HTML example.
- **meeting-minutes-mom**: points at the bundled `build_mom.py` in each brand skill.
- Repo: README, packaging tool, smoke test and CI workflow.
