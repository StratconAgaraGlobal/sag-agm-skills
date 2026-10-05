# SAG and AGM skills

Claude skills for the SAG Group's documents.

| Skill | Use it for |
|---|---|
| `sag-brand` | Anything for PT Stratcon Agara Global: Word, PDF, PowerPoint, Claude Slides, HTML, **web apps and dashboards**, business cards, minutes. Graphite & Slate brand. |
| `agm-brand` | Anything for PT Agara Global Maritim, in the Seafood or Marine edition. Same structure as SAG, with AGM's colours, emblem and photography. |
| `meeting-minutes-mom` | Minutes of Meeting content and structure. Uses the look from whichever brand skill applies. |
| `sag-graphify` | SAG's knowledge (people and current titles, services, clients, case studies, meetings, documents) with source-authority rules, plus the workflow to build and query a [Graphify](https://github.com/Graphify-Labs/graphify) knowledge graph. AGM is covered as a separate entity, so one graph can hold both. |

Each brand skill is **self-contained**: fonts, logos, photos, graphics, build code, the design spec, reference files and an HTML example are all inside the skill folder. Nothing else needs to be downloaded or attached. Plus Jakarta Sans installs itself the first time it is needed; weights that are already installed are skipped.

## Install, and stay up to date automatically

The repo is a plugin marketplace (`.claude-plugin/marketplace.json`) holding one plugin, `sag`, with all four skills. No version is pinned, so **every commit to `main` is a new version**. Pick the route that matches how your team uses Claude.

### A. Whole organization, every Claude surface (recommended, Team or Enterprise plan)

An Owner does this once and nobody else has to do anything:

1. claude.ai → **Organization settings → Plugins & skills → Add → Sync from GitHub**.
2. Connect GitHub, choose `StratconAgaraGlobal/sag-agm-skills`, and install the Claude GitHub App on the repo if asked.
3. Leave **Sync automatically** on. Claude adds a webhook, so every push to `main` re-syncs.
4. Set the `sag` plugin's access to **Installed by default** (or **Required**).

Members get the skills in claude.ai, Cowork, the desktop app and Claude Code. Their own GitHub access isn't needed.

### B. Claude Code, per person

Each person runs this once (the repo is private, so git needs a stored credential):

```bash
gh auth login && gh auth setup-git            # once per machine
claude plugin marketplace add StratconAgaraGlobal/sag-agm-skills
claude plugin install sag@sag-agm-skills
```

Then turn on auto-update: in a session run `/plugin` → **Marketplaces** → `sag-agm-skills` → **Enable auto-update**. Claude Code then pulls new commits in the background after each start. Without it, `claude plugin update sag@sag-agm-skills` updates by hand. Skills show up as `sag:sag-brand`, `sag:agm-brand` and so on, and trigger on their own as before.

No GitHub SSH key? Set `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` to skip the SSH attempt and clone over HTTPS.

An admin can do all of route B for everyone through managed settings (claude.ai → Organization settings → Claude Code → Managed settings):

```json
{
  "extraKnownMarketplaces": {
    "sag-agm-skills": {
      "source": { "source": "github", "repo": "StratconAgaraGlobal/sag-agm-skills" },
      "autoUpdate": true
    }
  },
  "enabledPlugins": { "sag@sag-agm-skills": true }
}
```

### C. Manual upload (claude.ai or desktop without organization sync)

Every push to `main` rebuilds the `.skill` files on the [**latest** release](https://github.com/StratconAgaraGlobal/sag-agm-skills/releases/tag/latest) (`.github/workflows/release-skills.yml`). Download them and upload in *Settings → Capabilities → Skills → Upload skill*. Uploads don't update themselves, so re-upload after changes, or use route A.

To build locally instead: `python tools/package_skills.py` (files land in `dist/`).

### Remove an old manual copy

If you copied the folders into `~/.claude/skills/` before, delete those copies after installing the plugin, so the stale ones don't load next to the live ones.

## Use

Just ask. Mention SAG, AGM, or the type of document and the skill loads: "Write a proposal for AGM's sea cucumber export programme", "Make the SAG MoM for today's meeting as a Word file and PDF", "Build a SAG deck from this outline".

To see what a brand looks like, open `skills/<name>/examples/<name>-example.html` in any browser. It has the logo builds, colours, type, an A4 document and the deck layouts (AGM has a Seafood / Marine switch). For how SAG apps look, open `skills/sag-brand/examples/sag-app-example.html`, which has a dashboard, a form and a sign-in screen in light and dark.

## What happens on first run

The skill runs `scripts/install_fonts.py`:

1. Checks each of the five Plus Jakarta Sans weights and skips any already installed.
2. Downloads the missing ones from Google Fonts.
3. If Google Fonts cannot be reached, uses the copies in `assets/fonts` (OFL licensed). It never blocks the work.

Installs are per-user (no admin rights needed). Word files embed the fonts, so recipients need nothing. PowerPoint cannot embed fonts, so anyone opening a `.pptx` should run the installer first.

Requirements for building files: Python 3.9+, `python-docx`, `python-pptx`, `Pillow`, and LibreOffice (`soffice`) for PDF conversion.

## The shared SAG / AGM graph

`sag-graphify` holds the facts and the rules for resolving conflicts (business cards beat the SAG BOOK for titles, and so on); Graphify turns SAG's and AGM's documents into a graph that Claude queries before answering.

1. Install `sag-graphify` and install Graphify as described in its SKILL.md (section 15).
2. Build the graph from the shared Drive folders, then commit the `graphify-out/` folder to this repo (or a sibling repo) so everyone queries the same graph instead of rebuilding it.
3. When documents change, update the graph with Graphify's update command and commit the new `graphify-out/`.

**Keep this repository private.** `sag-graphify` contains staff phone numbers and emails, unresolved board-title questions and client details that are not for the public, and a built graph will contain more.

## Repo layout

```
.claude-plugin/         marketplace.json: the repo as a Claude plugin marketplace (auto-update)
skills/
  sag-brand/            SKILL.md, scripts/, assets/ (incl. app/sag-app.css), examples/, references/
                        (DESIGN_SPEC, BRAND_SYSTEM, APP_DESIGN)
  agm-brand/            same layout, plus both editions
  meeting-minutes-mom/  SKILL.md
  sag-graphify/         SKILL.md
tools/package_skills.py zips each skill to dist/<name>.skill
tests/smoke_test.py     builds every document, deck and example for both brands
.github/workflows/      smoke test on every push; release-skills publishes .skill files on every push to main
```

## Maintaining

- Edit a skill in `skills/<name>/`, run `python tests/smoke_test.py`, and open a PR. Merging to `main` is the release: org sync, Claude Code auto-update and the `latest` release all pick it up. Don't add a `version` to `marketplace.json`, or users stop receiving commits until it is bumped.
- Adding a new skill folder? Add it to the `skills` list in `.claude-plugin/marketplace.json` (the smoke test fails until you do).
- If you change `example_template.html` or the assets, rebuild the example with `python scripts/build_example_html.py` inside that skill.
- Both brand skills carry identical copies of `components.py` (`BrandDoc`), `sagdoc.py` and `install_fonts.py`, and near-identical `build_mom.py`; keep the copies in step.

## Known limits

- The AGM emblem files are PNG recovered from AGM's finished documents. If the vector artwork arrives, replace the files in `assets/logo` under the same names.
- Only two AGM photographs are bundled. Add more via an `Edition` subclass in `brands.py`.
- The SAG stat-card and case-study layouts are in the `.pptx` builder but not yet in `examples/sag-brand-example.html` or the bundled reference deck in `assets/reference/`.
- The logo wall and the PANEL org-chart bands described in the sag-brand `SKILL.md` are not coded in `build_deck.py` yet.
- The bundled reference `.docx` / `.pdf` files still show the earlier 35.5 mm contact panel; rebuild them with LibreOffice when convenient.

See `LICENSE-NOTES.md` for licensing.
