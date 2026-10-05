# SAG App Design — Graphite & Slate on screen

How SAG web apps, internal tools, dashboards and PWAs look. It applies the
agreed brand (`DESIGN_SPEC.md`) to screens. Where this file and
`DESIGN_SPEC.md` disagree about print or slides, `DESIGN_SPEC.md` wins.

- **Drop-in code:** `assets/app/sag-app.css` holds every token and component below.
- **Reference screens:** `examples/sag-app-example.html` shows a dashboard, a form and a sign-in screen. Open it from the repo so the relative logo and band paths resolve.

---

## 1. Principles

1. **Light by default.** White surfaces, hairlines and generous space. Slate is for text and for the one primary action, not for big areas of chrome. Dark is an opt-in theme.
2. **Hairlines, not boxes.** Separate with 1 px lines and whitespace. Group the KPIs into one strip, and don't fill table headers.
3. **Yellow signs, it never decorates.** There's one yellow mark in the chrome (the active nav item), plus yellow where it *means* something: critical-path bars and the accent rule under a form title. Yellow never fills a button, never carries text on light, and is never a status.
4. **Status lives outside the palette.** Issued / in process / at risk / not started have their own soft tints (§3), so brand colour never reads as a state.
5. **One family.** Plus Jakarta Sans for everything, with weight carrying the hierarchy.
6. **No decoration.** No gradients, drop shadows, illustrations, emoji or decorative icons. Icons appear only where they help a control (§7).

## 2. Colour tokens

The brand constants are the same 11 roles as `scripts/palette.py`. Screens add semantic roles on top. Light is the default; dark applies only with `<html data-theme="dark">`.

| Token | Light (default) | Dark (opt-in) | Use |
|---|---|---|---|
| `--sag-bg` | `#FFFFFF` | `#101A1F` | App ground |
| `--sag-surface` | `#FFFFFF` | `#16252B` | Cards, top bar, inputs |
| `--sag-subtle` | `#F6F8F8` | `#1B2D34` | Hover, search well, notices |
| `--sag-selected` | `PAPER #EFF3F4` | `#22404A` | Active nav, selected rows, avatar |
| `--sag-text` | `INK #16181A` | `PAPER` | Headings, values, key cells |
| `--sag-text-2` | `BODY #2C4550` | `PALE #B8C6CC` | Body copy |
| `--sag-text-3` | `MUTED #63696C` | `RULE #8FA3AB` | Labels, table headers, hints, placeholders |
| `--sag-eyebrow` | `META #3A5560` | `RULE` | Eyebrows |
| `--sag-line` | `#E6EAEB` | `#26383F` | Hairlines between rows and around cards |
| `--sag-line-strong` | `#84969E` | `#6A8591` | Input and secondary-button borders (≥ 3:1) |
| `--sag-focus` | `PANEL` | `ACCENT #F9C939` | Focus ring |
| `--sag-primary` | `PANEL #1B3038` | `PAPER` | Primary button fill |
| `--sag-on-primary` | `#FFFFFF` | `INK` | Primary button text |

White is a screen-only surface. In print the ground stays `PAPER`.

**Checked contrast (WCAG 2.2):** MUTED on white 5.6, MUTED on `#F6F8F8` 5.2, BODY on white 10.1, white on PANEL 13.8, input border 3.1, dark-theme PALE on bg 10.1, dark RULE on surface 6.0. Yellow on white is 1.6, so **yellow is never text and never the focus ring on light.**

## 3. Status colours

Status chips are pills: 12 px 600, padding 3/10, a 6 px dot in the text colour, then the word. Always pair the colour with the word, because colour alone is never the signal.

| State | Light fg / bg | Dark fg / bg | Ratio (light) |
|---|---|---|---|
| Issued / done / success | `#14563B` / `#E7F3ED` | `#8FD3B0` / `#173A2E` | 7.6 |
| In process / pending / warning | `#6B510C` / `#FDF3D3` | `#F2CF6B` / `#3B3214` | 6.8 |
| At risk / error / rejected | `#8A331C` / `#F9E7E1` | `#F0A58E` / `#4A2219` | 6.8 |
| Not started / inactive | `#5C6366` / `#EEF0F0` | `#B8C6CC` / `#26353B` | 5.4 |

## 4. Type

Load `Plus+Jakarta+Sans:wght@400;500;600;700;800` from Google Fonts. Stack: `"Plus Jakarta Sans", Aptos, "Segoe UI", system-ui, sans-serif`. Use only the five bundled weights (400–800).

| Role | Size / line | Weight | Tracking | Colour |
|---|---|---|---|---|
| Page title (H1) | 28 / 1.15 | 800 | −0.025 em | text |
| Lede under H1 | 15 | 400 | 0 | text-3 |
| Card / section title (H2) | 18 / 1.3 | 700 | −0.01 em | text |
| Eyebrow | 12, caps | 700 | +0.14 em | eyebrow |
| Body | 15 / 1.55 | 400 | 0 | text-2 |
| Label | 13 | 600 | 0 | text |
| Hint / caption | 12–13 | 400 | 0 | text-3 |
| Table header | 12, sentence case | 600 | 0 | text-3 |
| Table cell | 14 (key column 600 text, sub-line 12 text-3) | 400 | 0 | text-2 |
| KPI figure | 32 / 1.15 | 800 | −0.03 em | text |
| Button / nav | 14 | 600 / 500 | 0 | — |

- **Tabular figures** (`font-variant-numeric: tabular-nums`) on every table, KPI, date, rupiah amount and reference code.
- Nothing below 11 px (nav section labels); body never below 14 px on phones.
- Dates are `05 Oct 2026`. Money is `IDR 1.5T` / `Rp 250.000.000` (Indonesian grouping in Bahasa screens), or `USD 33B`.

## 5. Layout

- **8 px grid**: spacing comes in 4, 8, 12, 16, 20, 24, 28, 36, 40, 56. Controls are 38–40 px tall.
- **Top bar:** 64 px, white, 1 px hairline below. It holds `sag-logo.png` (Build A, correct on white) at 30 px tall (28 px is the floor), the wordmark *Stratcon Agara Global* in 800 `text`, a hairline, then the app name in 500 `text-3`. On the right go search (a `subtle` well with a search icon) and the user's initials avatar. In dark, swap to `sag-logo-plated.png` (`.sag-on-light` / `.sag-on-dark`).
- **Sidebar:** 232 px, white, hairline on the right. Uppercase 11 px section labels in `text-3`, items 38 px in 500 `text-2`, and counts right-aligned in `text-3`. The active item gets a `selected` fill, 600 `text`, and a 3 px ACCENT bar on its left edge.
- **Main:** padding 36/40, 1200 px of content at most. The page head is eyebrow → H1 → lede, with actions on the right: secondary first, then the one primary.
- **Phones (≤ 860 px):** the sidebar becomes a scrolling tab row, and the active mark becomes a 3 px yellow underline. Search hides at ≤ 960 px and the wordmark at ≤ 480 px. KPI strips go 2 × 2, and secondary table columns drop (`.sag-hide-sm`). Never scroll the page horizontally.
- **Radius:** 10 px cards, 8 px inputs and buttons, pills for chips. **Elevation:** none. Use hairlines and space. The one exception is a modal, which gets a 40 % INK scrim.

## 6. Components

| Component | Spec |
|---|---|
| Primary button | `primary` fill, white text, 38 px, radius 8, 600 14 px, an optional 18 px icon before the label. One per view. |
| Secondary button | White, 1 px `line-strong` border, `text` colour |
| Ghost button | Transparent, `text-2`; hover `subtle`. Use for Cancel and toolbars. |
| Danger button | Risk bg / risk fg. Put destructive actions behind a confirm step. |
| Input / select / textarea | White, 1 px `line-strong`, radius 8, 40 px, padding 8/12, 15 px. Hover darkens the border; focus is a `focus` border plus a 3 px 12 % slate halo. Label above (600 13 px), hint below (12 px `text-3`). Invalid: risk border, and the hint rewritten as the error. |
| Card | White, 1 px `line`, radius 10, padding 24 (20 on phones). The head row holds an H2 left and a quiet link or meta right. |
| KPI strip | One card split into four cells by hairlines: label 13 px `text-3`, figure 32 px 800, note 12 px `text-3`. No icons and no trend arrows unless the data has a trend. |
| Table | No header fill: 12 px 600 `text-3` headers over a hairline. Rows 14 px padding with hairlines between and none after the last. The key column is 600 `text` with a 12 px sub-line. Dates and codes `nowrap`, numbers right-aligned. Inside a card the first and last columns sit flush with the card padding. |
| Status chip | §3 |
| Notice | `subtle` fill, hairline border, radius 8, 14 px, with an info icon. Risk and OK variants use the status tints. |
| Accent rule | 28 × 3 px ACCENT under a form or page title, at most one per view. |
| Avatar | 34 px circle, `selected` fill, initials 12 px 700 |
| Modal | 560 px max, card styling, H2 title, actions bottom-right; closes on Esc and on a scrim click. |
| Empty state | One line of `text-2` saying what will appear here, plus the action that fills it. No illustration. |
| Toast | Bottom-centre, PANEL fill, white text, 4 s. Errors stay until dismissed. |

## 7. Icons

Use [Lucide](https://lucide.dev), outline, 18 px, 1.75 stroke, `currentColor`, only where they help a control: search, add, export/download, info, close, menu, sort, external link, more. Always give them a text label or an `aria-label`. Never put them in KPI cards, headings or nav labels, and never use them as decoration.

## 8. Data visualisation

- Series order: `PANEL #1B3038`, `RULE #8FA3AB`, `GOLD #C9A227`, `PALE #B8C6CC`. In dark, `PANEL` swaps for `RULE` and `RULE` for `PALE`. Four series at most; past four, use a table.
- **Schedules use the deck meanings everywhere:** yellow (`ACCENT`) = critical path, slate = parallel filings, light grey (`TINT`) = passive monitoring. Bars are 8 px pills on hairline month gridlines.
- Gridlines are `line` at 1 px. Axis labels are 11–12 px `text-3`, tabular. Label lines directly, and use a legend only when direct labels don't fit.
- No 3D, no pie charts with more than three slices, no gradients.

## 9. Brand moments

- **Sign-in:** a white page with the logo + wordmark, "Sign in" in H1, Google as a secondary button, an "or" divider, the email field and a primary Continue. Along the foot sits a 180 px slate strip carrying `assets/graphics/deck_band_blue.png` (the Complexity Line with the tagline) as `background-image` on `.sag-signin-band`. This is the only screen that carries the Complexity Line.
- **Favicon:** the shield on a solid `#F9C939` tile at 16/32/48 px (the shield alone closes up at that size).
- **PWA / app icon:** the plated logo centred on `PANEL`, 20 % safe padding, `purpose: "any maskable"`.
- **Manifest:** `"theme_color": "#FFFFFF"`, `"background_color": "#FFFFFF"`, and `<meta name="theme-color" content="#FFFFFF">`, matching the white top bar.
- **Footer** (where an app has one): *Navigating complexity, delivering simplicity* left and *PT Stratcon Agara Global* right, 12 px `text-3`.

## 10. Words on screen

- Spell the name, *Stratcon Agara Global*, in the top bar and on anything a client sees. "SAG" is fine inside internal tools, file names and reference codes. "PT" belongs in the footer and legal text only.
- Buttons are verbs ("Register", "Export", "New filing"), never "OK" or "Submit".
- Bilingual apps: Bahasa Indonesia and English with the same layout; allow 30 % text growth.
- All the content rules in SKILL.md §6 apply to apps too: no supplier or partner names on service screens, CECEP never named, no academic titles in people's names.

## 11. Accessibility checklist

- [ ] Text ≥ 4.5:1, UI boundaries ≥ 3:1 (the tokens already pass, so don't invent new greys)
- [ ] Visible focus on every control (the `--sag-focus` ring or border)
- [ ] Status is never shown by colour alone
- [ ] Every input has a `<label>`, and errors are linked with `aria-describedby`
- [ ] Works at 390 px wide and at 200 % zoom without horizontal page scroll
- [ ] `prefers-reduced-motion` honoured (transitions are 150 ms, ease-out, colour only)
- [ ] Check the dark theme if the app offers one

## 12. Existing SAG apps that need migrating

These predate the agreed system and still use the old navy/gold look:

| App | Today | Change to |
|---|---|---|
| SAG Email Generator / Admin (`SAG_Codes/site`) | Inter / Arial / Georgia; manifest `#0C1E38` | Plus Jakarta Sans; `sag-app.css`; manifest `#FFFFFF` |
| SAG Business Card Generator | navy `#0C1E38`, gold `#C8960A`, Inter + Playfair Display | `sag-app.css` for the tool; the card itself per `BRAND_SYSTEM.md` §7 |
| Printed business cards (2026 batch) | Playfair serif name, navy ground | Reprint per `BRAND_SYSTEM.md` §7 at the next order |

HTML email bodies are a separate medium (most clients have no web fonts): use the same colours with an `Arial, sans-serif` fallback, and keep the layout to tables.
