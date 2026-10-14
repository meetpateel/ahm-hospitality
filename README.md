# AHM Hospitality — Website

Marketing and investor-relations site for **AHM Hospitality (Apex Hospitality Management)**, a family-operated owner/operator of branded hotels in Sioux Falls, SD and Worthington, MN.

- **Live:** https://ahmhospitality.com
- **Stack:** hand-written static HTML + one shared stylesheet + one small vanilla JS file. No build step, no package manager, no framework.
- **Hosting:** GitHub Pages, served from the root of `main` (`CNAME` → `ahmhospitality.com`). **Every push to `main` is live within a minute or two.**

> Working with Claude Code? Start with [`CLAUDE.md`](CLAUDE.md). It's the short version of this file, plus the rules for editing.

---

## Repo layout

```
.
├── index.html                 Home: hero, 3-property grid, "we operate what we own", investor band
├── about.html                 Family history (since 2015), operating principles
├── leadership.html            Family principals
├── properties.html            Portfolio index: operating properties + conversion, brand blocks
├── properties/
│   ├── towneplace-suites.html         TownePlace Suites by Marriott (Sioux Falls), 67 rooms, flagship
│   ├── econolodge-north.html          EconoLodge North (Sioux Falls), 80 rooms
│   └── quality-inn-worthington.html   Quality Inn Worthington, MN, 56 rooms, converting from Super 8
├── investors.html             Thesis, playbook, track record, team, structure, request-package form
├── risk-factors.html          Reg D–style risk disclosures (linked from footer + investors)
├── privacy.html               Privacy & terms
├── contact.html               Contact form + direct emails
├── news.html                  HIDDEN: placeholder page, not in nav/sitemap, disallowed in robots.txt
│
├── styles.css                 The only stylesheet (~1.45k lines, design tokens at the top)
├── app.js                     Mobile nav toggle + scroll-reveal observer (loaded `defer` on every page)
├── photos/                    <slug>.jpg = card/hero image; <slug>/*.jpg = gallery images
├── tools/check_links.py       Link / image / form-target / [TODO] linter
│
├── sitemap.xml, robots.txt    SEO (update sitemap when adding/removing a page)
├── CNAME                      GitHub Pages custom domain. Do not delete.
└── notes/                     Local-only planning docs (gitignored): PLAN*.md, RESEARCH.md, TODO.md
```

Property slugs are shared across files: `towneplace-suites`, `econolodge-north`, `quality-inn-worthington`.
The slug is used in `properties/<slug>.html`, `photos/<slug>.jpg`, `photos/<slug>/`, and `sitemap.xml`.

## Local preview

```bash
python -m http.server 8000
# open http://localhost:8000
```

## Before pushing

```bash
python tools/check_links.py
```

- Always checks: every internal `href`/`src`/`url(...)` exists on disk, and lists any `[TODO:` placeholder used as a link or form target.
- If the local server above is running, it also checks that each internal link returns HTTP 2xx/3xx. Without a server it skips that pass and says so.
- Exits non-zero only on **broken** links. `TODO-LINK` entries are warnings.

## Page anatomy (shared by every page)

Each page is self-contained HTML that repeats the same shared chrome:

1. `<head>`: title, description, canonical, Open Graph/Twitter tags, `styles.css`
2. `<a class="skip-link" href="#main">`
3. `.topbar` (location + email)
4. `<nav class="nav">`: logo, `.nav-links` (the current page's link carries `class="active"`), `.nav-cta`, `.nav-toggle`
5. Content `<section>`s. The first one has `id="main"`.
6. Most pages: `.investor-band` CTA section
7. `<footer>`: 4-column grid + `.footer-bottom` (Privacy & Terms · Risk Factors)
8. `<script defer src="app.js">`

**There is no templating.** The nav and footer are copy-pasted into all 12 pages. Pages in `properties/` use `../` prefixes for every asset and link. To change the nav or footer, change it in every file (`grep -l 'nav-links' *.html properties/*.html`).

## Design system

**Tokens** (in `:root` at the top of `styles.css`). Never use raw hex anywhere else.

| Token | Value | Use |
|---|---|---|
| `--navy` | `#0F2A3F` | Primary brand, headings, logo, dark backgrounds |
| `--navy-deep` | `#081B2C` | Footer, hero overlay edges |
| `--cream` | `#F6F1E8` | Page background, body text on navy |
| `--cream-warm` | `#EFE7D6` | `section.alt` background, placeholder fill |
| `--brass` | `#B5764F` | CTA, eyebrows on dark, hover, active nav, focus outline |
| `--ink` | `#1A1A1A` | Default body text (use sparingly) |
| `--ink-soft` | `#3D3D3D` | Story / narrative paragraphs |
| `--muted` | `#6B6B6B` | Tertiary text, eyebrows on light, addresses |
| `--line` | `#D9D2C4` | Borders on light backgrounds |

**Type scale** (canonical; don't add per-page overrides):
- `h1` = `clamp(36px, 6vw, 64px)` weight 300 (`.hero` and `.page-hero`)
- `h2` = `clamp(28px, 4vw, 44px)` weight 400
- `h3` = `20px` weight 500
- `.lead`, `.body-note`, `.prop-summary`, `.wire-verify` are the paragraph variants

**Fonts:** Fraunces (display) + Manrope (body), loaded from Google Fonts via `@import` at the top of `styles.css`.

**Breakpoints:** `≤900px` hamburger drawer and stacked layouts · `≤768px` news/topbar tighten · `≤600px` hero scales down, gallery is 1 column, inputs forced to 16px (prevents iOS zoom).

**Reusable components:** `.section-head` (`.tight` variant), `.section-inner`, `.section-narrative` · `.property-grid` (`.detailed` variant on the properties page) / `.property-card` / `.prop-*` · `.property-hero`, `.property-detail`, `.property-gallery`, `.gallery-tile` · `.brand-grid` / `.brand-block` · `.partnership-list` / `.partnership-row` · `.investor-band` / `.investor-inner` · `.contact-grid`, `.contact-form`, `.contact-note` · `.btn` + `.btn-primary | .btn-ghost | .btn-dark` · `.center-cta` · `.eyebrow` · `.skip-link`.

Defined but currently unused (kept for reuse): `section.dark`, `.prose`, `.rule`, `.container`, `.opportunity*` (the Active Pipeline cards, removed from investors.html after the Luverne deals fell through).

**Photos:** decorative images are `background-image` on a `<div>`, never `<img>`. The div gets class `photo-ready`, and the only inline style allowed anywhere is the image URL:

```html
<div class="gallery-tile photo-ready" style="background-image: url('../photos/towneplace-suites/lobby.jpg');"></div>
```

Sizing and positioning come from CSS. Until a real photo exists, use the `.placeholder` class with a `.placeholder-label` instead.

**Accessibility:** skip link on every page · brass `:focus-visible` outline · touch targets ≥44px on coarse pointers · AA contrast (brass is for eyebrows/CTAs/accents only, never body copy on cream).

**Rejected patterns** (see git history): inline `style=` for anything but `background-image` · raw hex colors · per-page heading sizes · italic `<em>` accent words in headlines (five remain on properties.html; removing them is a copy decision).

## Content rules

- **Never invent facts.** Names, dates, room counts, occupancy, ADR, dollar figures, and returns come from the family only. Where content is missing, leave a visible `[TODO: …]` marker. `grep -rn "\[TODO" --include=*.html .` lists them.
- This is an investor-facing site with securities-adjacent content (`investors.html`, `risk-factors.html`). Treat performance claims, return figures, and risk language as legal copy: change them only when explicitly asked.
- When a property is added or removed, update: `properties/<slug>.html`, `photos/<slug>*`, `properties.html`, the home grid in `index.html`, the "three properties" wording in hero/CTA copy, `investors.html` track record, `sitemap.xml`, and OG tags if the image changes.

## Open items

Tracked in `notes/TODO.md` (local only). The site-blocking ones:
- **Formspree ID:** both `contact.html` and `investors.html` forms post to `https://formspree.io/f/[TODO: FORMSPREE_ID]`, so submissions fail on the live site.
- `news.html` has 15 `[TODO:` placeholders. It stays hidden until real items exist.
