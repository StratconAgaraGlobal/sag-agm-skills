# SAG App Design — Graphite & Slate product UI

How SAG web apps, internal tools, dashboards and PWAs look. The bar is modern product software (Linear, Stripe): crisp, dense, quiet, keyboard-friendly, with the brand carried by meaning rather than decoration. Where this file and `DESIGN_SPEC.md` disagree about print or slides, `DESIGN_SPEC.md` wins.

- **Drop-in code:** `assets/app/sag-app.css` holds every token and component below.
- **Reference screens:** `examples/sag-app-example.html` has the approvals list with a detail panel, the timeline, the create dialog, the ⌘K palette and sign-in, in light and dark. Open it from the repo so the relative asset paths resolve.

---

## 1. Principles

1. **The work is the loudest thing on screen.** A light grey app ground with the work on one inset white panel. The chrome is quiet: hairlines, small type, grey icons.
2. **Dense but calm.** 42 px rows, 13–14 px type, 52 px header bars. Hierarchy comes from weight and grey levels, not size jumps or colour.
3. **Brand by meaning.** SAG yellow is the **critical path**: the ◆ marker on a row, and the bars on the timeline. It's never a button, never text on light, never a status, never decoration. The shield sits in the workspace switcher.
4. **Status has its own language:** four glyphs (not started ◌, in process ◐, issued ✓, at risk !) in colours outside the brand palette, always next to a word somewhere on screen.
5. **Keyboard first.** ⌘K palette, single-key shortcuts shown as `kbd` chips (C = new filing, G T = go to timeline).
6. **Depth, softly.** Two elevation levels only (§2). No gradients, illustrations or emoji. Icons are Lucide outline (§7).

## 2. Tokens

The brand constants are the same 11 roles as `scripts/palette.py`. Light is the default; dark applies only with `<html data-theme="dark">`.

| Token | Light | Dark | Use |
|---|---|---|---|
| `--sag-app` | `#F3F5F5` | `#0E171B` | App ground: sidebar, around the panel, group headers |
| `--sag-surface` | `#FFFFFF` | `#142127` | The work panel, dialogs, menus, inputs |
| `--sag-hover` | `#F5F7F7` | `#18272E` | Row and item hover |
| `--sag-selected` | `#EDF1F2` | `#1E3139` | Selected row, active nav, pressed segment |
| `--sag-text` | `INK #16181A` | `#F1F4F5` | Titles, row text, values |
| `--sag-text-2` | `BODY #2C4550` | `PALE` | Body and secondary text |
| `--sag-text-3` | `MUTED #63696C` | `RULE` | Labels, meta, refs, dates (the lightest grey allowed for text) |
| `--sag-icon` | `#8A9196` | `#6F858E` | Icons only, never text |
| `--sag-line` | `#E5E9EA` | `#22343B` | Hairlines |
| `--sag-line-strong` | `#84969E` | `#5B747F` | Text-input borders (≥ 3:1) |
| `--sag-primary` | `PANEL #1B3038` | `#F1F4F5` | The primary button |
| `--sag-shadow-1` | 1 px hairline ring + 1 px soft drop | hairline ring | Panel, cards, secondary buttons, pressed segment |
| `--sag-shadow-2` | 32 px soft drop + ring | deeper drop + ring | Dialogs, palette, menus, sign-in card |

Radius: 12 px panel and dialogs, 8 px buttons and inputs, 6 px pills, segment buttons and timeline bars, full pills for chips and tags.

**Contrast:** MUTED on white 5.6, BODY on white 10.1, white on PANEL 13.8, input border 3.1, icon grey 3.2 (icons only). Yellow on white is 1.6, so it's never text and never the focus ring on light; INK on yellow (timeline labels) is 11.4.

## 3. Status

| State | Glyph | Icon colour | Chip fg / bg (light) |
|---|---|---|---|
| Not started | dashed ring | `#8A9196` | `#5C6366` / `#EEF0F0` |
| In process | ring + half fill | `#B7861B` | `#6B510C` / `#FDF3D3` |
| Issued / done | filled ✓ | `#1F7A53` | `#14563B` / `#E7F3ED` |
| At risk / error | filled ! | `#B4472A` | `#8A331C` / `#F9E7E1` |

The glyphs are `<symbol>`s (`st-idle`, `st-wait`, `st-ok`, `st-risk`) in the example's sprite; copy them. Lists group by status with a sticky group header (glyph, name, count). Use chips where a status stands alone (tables, exports).

## 4. Type

Plus Jakarta Sans 400–800 only. Stack: `"Plus Jakarta Sans", Aptos, "Segoe UI", system-ui, sans-serif`.

| Role | Size | Weight | Colour |
|---|---|---|---|
| Detail / dialog title | 17–19 | 700, −0.015 em | text |
| Stat value | 22 | 700, tabular | text |
| Row text, nav | 13.5 | 500 (active nav 600) | text / text-2 |
| Breadcrumb | 13.5 | 600 current, 400 parents | text / text-3 |
| Body, descriptions | 13–14 | 400 | text-2 |
| Labels, group headers | 12–13 | 600 | text-3 / text |
| Refs, dates, counts | 12–12.5 | 400, tabular | text-3 |
| `kbd` | 11 | 600 | text-3 |

Tabular figures on every ref code, date, count and amount. Dates are `14 Nov` in lists, `14 Nov 2026` in detail. Refs are `SAG-014`.

## 5. Layout

- **App frame:** a 236 px sidebar on `--sag-app`, then the work panel inset 8 px with radius 12 and `shadow-1`.
- **Sidebar, top to bottom:**
  - workspace switcher (shield `sag-logo.png` 20 px + *Stratcon Agara Global* 700 + chevron)
  - search button with `⌘K`
  - nav items (30 px, 16 px grey icon, label, optional count)
  - section labels (11.5 px 600 `text-3`)
  - clients with 16 px monogram tiles
  - the user at the foot
- **Active nav:** `selected` fill, 600 text, dark icon. No yellow in the chrome.
- **Header bar:** 52 px, hairline below. Breadcrumb → view switcher (segmented: List / Timeline / Board) → spacer → ghost Filter and Display → primary action with its shortcut.
- **Summary strip** (optional, under the bar): cells split by hairlines. The first cell is wider and holds a segmented progress bar (issued / in process / at risk / not started) with a legend.
- **List + detail:** the list fills; a 340 px detail panel opens on the right for the selected row. It holds the ref and actions, the title, description, a property grid (96 px labels) and an activity timeline with a note bubble.
- **Responsive:**
  - ≤ 1180 px: the detail panel becomes a separate page.
  - ≤ 960 px: summary goes 2 × 2, and the view switcher and ghost buttons collapse.
  - ≤ 860 px: the sidebar becomes a mobile bar (menu, shield, page title, avatar); the panel goes full-bleed; refs, tags and the "Critical" word drop (the ◆ stays); the timeline scrolls sideways.
  - Never scroll the page horizontally.

## 6. Components

| Component | Spec |
|---|---|
| Primary button | 32 px, radius 8, PANEL with white 600 13 px, 1 px soft drop + inner top highlight, optional icon and `kbd`. One per view. |
| Secondary button | White with `shadow-1` (ring, no border), `text` |
| Ghost button | Transparent, grey icon, `selected` on hover. Toolbars, Cancel, icon-only (28 × 28) actions. |
| Segmented control | `app` track with a hairline; the pressed button is white with `shadow-1` |
| Row | 42 px: glyph · ref (64 px) · title (ellipsis) · ◆ Critical · spacer · authority tag · date · owner avatar. Hover `hover`; selected `selected` + 2 px PANEL inset bar on the left. |
| Group header | 36 px, `app` fill, sticky, glyph + name 600 + count |
| Tag | Pill, hairline border, 12 px 500 `text-2`. Use for authorities and other plain attributes. |
| Critical marker | 8 px ACCENT diamond (with a faint bronze ring so it holds on white) + "Critical" 12 px 600 `text-2` |
| Avatar | 22 px circle, initials 9.5 px 700. Soft neutral tints vary by person, and no photos in dense lists. |
| Property grid | 96 px label column `text-3`, values 500 `text` with an icon, glyph or tag |
| Activity | Vertical hairline, 22 px icon nodes, **bold event** + detail, date below in `text-3`, optional note bubble on `app` |
| Dialog (create) | 620 px, radius 12, `shadow-2`. Breadcrumb head + close; a borderless 19 px title input and a borderless description; a row of **property pills** (status, authority, owner, target, critical path); a footer with attach, a "Create more" switch and the primary button with `⌘↵`. |
| Command palette | 560 px, `shadow-2`. 52 px input with `esc`; grouped results (filings with glyph + ref, actions with shortcuts); selected item `selected`; a footer with ↑↓ / ↵ / esc hints. |
| Text input (forms) | 40 px, 1 px `line-strong`, radius 8; focus is a PANEL border + 3 px 12 % slate halo (yellow halo in dark). Label above 13 px 600. |
| Toast | Bottom-centre, `shadow-2`, PANEL fill, white text, 4 s. Errors stay until dismissed. |
| Empty state | One line of `text-2` saying what will appear here, plus the action that fills it. No illustration. |

## 7. Icons

Use [Lucide](https://lucide.dev), outline, 16 px (14 px in pills and breadcrumbs), 1.75 stroke, `--sag-icon` grey by default and `text` when active. Keep them in an SVG `<symbol>` sprite and reference them with `<use>`. Every icon-only button gets an `aria-label`.

## 8. Timeline and charts

- **Gantt:** a 210 px label column (glyph + name), month columns on hairline gridlines, 40 px rows, and 24 px bars with radius 6 and the label inside.
  - **Yellow = critical path** (INK label), **slate = parallel** (white label), **grey 6 px line = monitoring**: the same meanings as the decks.
  - Done bars are 62 % opacity with a ✓. At risk adds a 1.5 px risk-colour ring. *Today* is a 1 px ink line with an ink tag.
  - Position bars with `--s`/`--e` (months from the start) and `--n` (months shown).
- **Charts:** series order `PANEL`, `RULE`, `GOLD`, `PALE`, four at most. Gridlines `line`, axis labels 11–12 px `text-3` tabular. Label directly. No 3D, no gradients, no pies over three slices.

## 9. Brand moments

- **Sign-in:** `app` ground, a centred white card with `shadow-2` (shield + wordmark, "Sign in to <app>", Google as secondary, an "or" divider, email, primary Continue), and the Complexity Line band (`deck_band_blue.png`) as a 150 px slate strip along the foot. This is the only screen that carries the Complexity Line.
- **Favicon:** the shield on a solid `#F9C939` tile at 16/32/48 px.
- **PWA icon:** the plated logo on `PANEL`, 20 % safe padding, maskable. **Manifest:** `theme_color` and `background_color` `#F3F5F5`.

## 10. Words on screen

- *Stratcon Agara Global* in the workspace switcher and on anything a client sees. "SAG" is fine in refs and internal labels; "PT" only in legal text.
- Buttons are verbs ("New filing", "Create filing", "Export"). Sentence case everywhere, except refs.
- Bahasa Indonesia and English share the layout; allow 30 % growth.
- The content rules in SKILL.md §6 apply: no supplier names on service screens, CECEP never named, no academic titles.

## 11. Accessibility checklist

- [ ] Text ≥ 4.5:1 and UI boundaries ≥ 3:1. Use the tokens; `--sag-icon` is for icons only.
- [ ] Visible focus on every control (`:focus-visible`, slate ring; yellow in dark)
- [ ] Status never by colour alone: glyph shape + word
- [ ] Every icon-only button has an `aria-label`; dialogs have `role="dialog"` and trap focus
- [ ] Every shortcut is also reachable by mouse
- [ ] 390 px wide and 200 % zoom work without page-level horizontal scroll
- [ ] `prefers-reduced-motion` honoured (transitions are 120 ms, colour only)

## 12. Existing SAG apps that need migrating

| App | Today | Change to |
|---|---|---|
| SAG Email Generator / Admin (`SAG_Codes/site`) | Inter / Arial / Georgia; navy manifest `#0C1E38` | `sag-app.css`, app frame + list/detail; manifest `#F3F5F5` |
| SAG Business Card Generator | navy `#0C1E38`, gold `#C8960A`, Inter + Playfair Display | `sag-app.css` for the tool; the card itself per `BRAND_SYSTEM.md` §7 |
| Printed business cards (2026 batch) | Playfair serif name, navy ground | Reprint per `BRAND_SYSTEM.md` §7 at the next order |

HTML email bodies are a separate medium (most clients have no web fonts): use the same colours with an `Arial, sans-serif` fallback and table layout.
