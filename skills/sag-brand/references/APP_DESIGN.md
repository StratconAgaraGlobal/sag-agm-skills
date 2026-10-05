# SAG App Design — Graphite & Slate on screen

How SAG web apps, internal tools, dashboards and PWAs look. It applies the
agreed brand (`DESIGN_SPEC.md`) to screens. Where this file and
`DESIGN_SPEC.md` disagree about print or slides, `DESIGN_SPEC.md` wins.

- **Drop-in code:** `assets/app/sag-app.css` holds every token and component below.
- **Reference screens:** `examples/sag-app-example.html` shows a dashboard, a form and a sign-in screen, in light and dark. Open it from the repo so the relative logo and band paths resolve.

---

## 1. Principles

1. **Quiet chrome, loud data.** Slate structure, white work surfaces, ink text. The app should feel like the documents: calm and exact.
2. **Yellow signs, it never decorates.** At most one yellow mark in the app chrome (the active nav indicator), plus yellow where it *means* something: critical-path bars and the focus ring on dark. Yellow never fills a button, never carries text on light, and is never a status.
3. **Status lives outside the palette.** Issued / in process / at risk / not started have their own muted tints (§3), so brand colour never reads as a state.
4. **One family.** Plus Jakarta Sans for everything, with weight carrying the hierarchy.
5. **No decoration.** No gradients, drop shadows, stripes, illustrations, emoji or decorative icons. Icons appear only where they *are* the control (§7).

## 2. Colour tokens

The brand constants are the same 11 roles as `scripts/palette.py`. Screens add a small set of semantic roles on top.

| Token | Light | Dark | Use |
|---|---|---|---|
| `--sag-bg` | `PAPER #EFF3F4` | `#111C21` | Page ground |
| `--sag-surface` | `#FFFFFF` | `PANEL #1B3038` | Cards, tables, inputs, sidebar |
| `--sag-surface-2` | `TINT #E2E6E7` | `#22404A` | Hover rows, active nav, notices |
| `--sag-text` | `INK #16181A` | `PAPER` | Headings, values, strong cells |
| `--sag-text-2` | `BODY #2C4550` | `PALE #B8C6CC` | Body copy |
| `--sag-text-3` | `MUTED #63696C` | `RULE #8FA3AB` | Labels, hints, placeholders |
| `--sag-eyebrow` | `META #3A5560` | `RULE` | Eyebrows |
| `--sag-line` | `TINT` | `BODY #2C4550` | Dividers between rows and cards |
| `--sag-line-strong` | `#7A8F98` | `#6A8591` | Input and secondary-button borders (≥ 3:1) |
| `--sag-focus` | `INK` | `ACCENT #F9C939` | 2 px focus ring, 2 px offset |
| `--sag-primary` | `PANEL` | `PAPER` | Primary button fill |
| `--sag-on-primary` | `PAPER` | `INK` | Primary button text |

White (`#FFFFFF`) is a screen-only surface. It is not used in print, where the ground is `PAPER`.

**Checked contrast (WCAG 2.2):** BODY on PAPER 9.1, MUTED on white 5.6, MUTED on PAPER 5.0, PAPER on PANEL 12.3, dark-mode PALE on bg 9.9, RULE on PANEL 5.2, light input border 3.4, dark input border 3.5. Yellow on white is 1.6, so **yellow is never text and never the focus ring on a light theme.**

## 3. Status colours

These are adopted from the SAG Identity System v2 permit tracker. Always pair the colour with a word; colour alone is never the signal.

| State | Light fg / bg | Dark fg / bg | Ratio (light) |
|---|---|---|---|
| Issued / done / success | `#14563B` / `#E1EFE8` | `#8FD3B0` / `#173A2E` | 7.3 |
| In process / pending / warning | `#6B510C` / `#FCEFC4` | `#F2CF6B` / `#3B3214` | 6.5 |
| At risk / error / rejected | `#8A331C` / `#F6E0D9` | `#F0A58E` / `#4A2219` | 6.5 |
| Not started / inactive | `#63676A` / `#EDEDEA` | `#B8C6CC` / `#26353B` | 4.9 |

Status chip: 12 px 700, radius 4, padding 2/8, a 6 px dot in the text colour, then the word.

## 4. Type

Load `Plus+Jakarta+Sans:wght@400;500;600;700;800` from Google Fonts. Stack: `"Plus Jakarta Sans", Aptos, "Segoe UI", system-ui, sans-serif`. Use only the five bundled weights (400–800); 200 and 300 are not part of the agreed system.

| Role | Size / line | Weight | Tracking | Colour |
|---|---|---|---|---|
| Page title (H1) | 28 / 1.15 | 800 | −0.02 em | text |
| Section (H2) | 20 / 1.25 | 800 | −0.01 em | text |
| Card title (H3) | 16 / 1.35 | 700 | 0 | text |
| Eyebrow | 12, caps | 800 | +0.16 em | eyebrow |
| Body | 15 / 1.5 | 400 | 0 | text-2 |
| Label | 13 | 600 | 0 | text |
| Small / hint | 12–13 | 400 | 0 | text-3 |
| Table header | 12, caps | 800 | +0.08 em | PAPER on PANEL |
| Table cell | 14 | 400 (key column 600) | 0 | text-2 |
| KPI figure | 36 / 1.1 | 800 | −0.03 em | text |
| Button | 14 | 600 | 0 | — |

- **Tabular figures** (`font-variant-numeric: tabular-nums`) on every table, KPI, date, rupiah amount and reference code.
- Nothing below 12 px. Body text never goes below 14 px on phones.
- Dates are `05 Oct 2026`. Money is `IDR 1.5T` / `Rp 250.000.000` (Indonesian grouping in Bahasa screens), or `USD 33B`.

## 5. Layout

- **8 px grid**: spacing comes in 4, 8, 12, 16, 24, 32, 48. Controls are 40 px tall, and touch targets are at least 40 × 40 (44 on phone-first apps).
- **App shell:** a 56 px `PANEL` top bar holds the plated logo (32 px tall; 28 px is the floor), the wordmark *Stratcon Agara Global* in 800 PAPER, a hairline, then the app name in 500 PALE. Account and help sit right as ghost buttons. Below that comes a 240 px sidebar on `surface` and the main column (max 1200 px of content, 32 px padding; 16 px on phones).
- **Page head:** eyebrow (context) → H1 → actions right-aligned on the same baseline. Primary action last.
- **Phones (≤ 860 px):** the sidebar becomes a horizontally scrolling tab row, and the active indicator becomes a 3 px yellow underline. At ≤ 480 px the wordmark drops and the shield alone carries the bar. Never scroll the page horizontally; wide tables scroll inside their wrapper.
- **Radius:** 8 px on cards, inputs, buttons and table wrappers. 4 px on chips. This is the screen equivalent of the 2.5 mm document radius.
- **Elevation:** none. Separate with a 1 px `line` border and the bg/surface step, not shadows. The one exception is a modal, which gets a 40 % INK scrim.

## 6. Components

| Component | Spec |
|---|---|
| Primary button | `primary` fill, `on-primary` text, 40 px, radius 8, 600 14 px. One per view. |
| Secondary button | `surface` fill, `line-strong` 1 px border, `text` colour |
| Ghost button | transparent, `text-2`; hover `surface-2`. Cancel, toolbars, top bar. |
| Danger button | risk bg / risk fg. Put destructive actions behind a confirm step. |
| Input / select / textarea | `surface`, 1 px `line-strong`, radius 8, 40 px, padding 8/12, 15 px text. Label above in 600 13 px and hint below in 12 px `text-3`. Invalid: risk-coloured border + the hint rewritten as the error. |
| Card | `surface`, 1 px `line`, radius 8, padding 24 |
| KPI card | Card with a 36 px 800 figure and a 13 px label below. No icons, no trend arrows unless the data has a trend. |
| Table | Wrapper card. Header row PANEL with 12 px caps PAPER (the screen echo of the document section band). Rows 12/16 padding, `line` dividers, hover `surface-2`. Dates and codes `nowrap`, numbers right-aligned. |
| Status chip | §3 |
| Notice | `surface-2` block, radius 8, 14 px. Risk and OK variants use the status colours. |
| Accent rule | 32 × 4 px ACCENT under a card or form title: the screen version of the slide accent rule. One per view at most, and none in grids of four or more. |
| Nav item | 40 px, 600 14 px `text-2`. Active: `surface-2` + `text` + 4 px ACCENT bar on the left edge (the one yellow mark in the chrome). |
| Modal | 560 px max, card styling, title H2, actions bottom-right, closes with Esc and by clicking the scrim. |
| Empty state | One line of `text-2` saying what will appear here, plus the action that fills it. No illustration. |
| Toast | Bottom-centre, PANEL ground, PAPER text, 4 s. Errors stay until dismissed. |

## 7. Icons

Icons are allowed only where the icon *is* the control or saves real space: search, close, menu, sort, download, external link, kebab. Use [Lucide](https://lucide.dev), outline, 18 px, 1.75 stroke, `currentColor`, always with an `aria-label` or visible text. Never use them in KPI cards, headings or nav labels, and never as decoration.

## 8. Data visualisation

- Series order: `PANEL #1B3038`, `RULE #8FA3AB`, `GOLD #C9A227`, `PALE #B8C6CC`. In dark mode, `PANEL` swaps for `PAPER`. Four series at most; past four, use a table.
- **Schedules use the deck meanings everywhere:** yellow (`ACCENT`) = critical path, slate = parallel filings, grey (`PALE`) = passive monitoring. Yellow is legitimate here because it means something.
- Gridlines are `line` at 1 px. Axis labels 12 px `text-3`, tabular. Label lines directly; use a legend only when direct labels don't fit.
- No 3D, no pie charts with more than three slices, no gradients.

## 9. Brand moments

- **Sign-in / splash:** PANEL ground, plated logo + wordmark centred above a white card, and `assets/graphics/deck_band_blue.png` (the Complexity Line with the tagline) as `background-image`, bottom, full width. This is the only screen that carries the Complexity Line.
- **Favicon:** the shield on a solid `#F9C939` tile at 16/32/48 px (the ring between the outlines closes up at that size if the shield stands alone).
- **PWA / app icon:** plated logo centred on `PANEL`, 20 % safe padding, `purpose: "any maskable"`.
- **Manifest:** `"theme_color": "#1B3038"`, `"background_color": "#1B3038"`, and a `<meta name="theme-color" content="#1B3038">`.
- **Footer** (where an app has one): *Navigating complexity, delivering simplicity* left and *PT Stratcon Agara Global* right, 12 px `text-3`.

## 10. Words on screen

- Spell the name, *Stratcon Agara Global*, in the top bar and on anything a client sees. "SAG" is fine inside internal tools, file names and reference codes. "PT" belongs in the footer and legal text only.
- Buttons are verbs ("Register", "Export PDF", "Send"), never "OK" or "Submit".
- Bilingual apps: Bahasa Indonesia and English with the same layout; allow 30 % text growth.
- All the content rules in SKILL.md §6 apply to apps too: no supplier or partner names on service screens, CECEP never named, no academic titles in people's names.

## 11. Accessibility checklist

- [ ] Text ≥ 4.5:1, UI boundaries ≥ 3:1 (the tokens already pass; don't invent new greys)
- [ ] Visible focus on every control (`:focus-visible`, the `--sag-focus` ring)
- [ ] Status is never shown by colour alone
- [ ] Every input has a `<label>`; errors are linked with `aria-describedby`
- [ ] Works at 390 px wide and 200 % zoom without horizontal page scroll
- [ ] `prefers-reduced-motion` honoured (transitions are 150 ms, ease-out, and only on colour)
- [ ] Light and dark both checked (`data-theme` overrides the OS)

## 12. Existing SAG apps that need migrating

These predate the agreed system and still use the old navy/gold look:

| App | Today | Change to |
|---|---|---|
| SAG Email Generator / Admin (`SAG_Codes/site`) | Inter / Arial / Georgia; manifest `#0C1E38` | Plus Jakarta Sans; `sag-app.css`; manifest `#1B3038` |
| SAG Business Card Generator | navy `#0C1E38`, gold `#C8960A`, Inter + Playfair Display | PANEL / ACCENT / GOLD roles, Plus Jakarta Sans only; card layout per `BRAND_SYSTEM.md` §7 |
| Printed business cards (2026 batch) | Playfair serif name, navy ground | Reprint per `BRAND_SYSTEM.md` §7 at the next order |

HTML email bodies are a separate medium (no web fonts in most clients): use the same colours with an `Arial, sans-serif` fallback, and keep the layout to tables.
