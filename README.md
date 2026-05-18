# AHM Hospitality — Website

A static website for Apex Hospitality Management.

## What's included

- `index.html` — Home
- `about.html` — Family story, values, growth strategy
- `leadership.html` — Named principals and bios
- `properties.html` — Portfolio index (links to per-property detail pages)
- `properties/econolodge-luverne.html` — EconoLodge Luverne detail page
- `properties/econolodge-north.html` — EconoLodge North (Sioux Falls) detail page
- `properties/quality-inn-luverne.html` — Quality Inn Luverne detail page
- `properties/quality-inn-sioux-falls.html` — Quality Inn Sioux Falls detail page
- `properties/towneplace-suites.html` — TownePlace Suites by Marriott detail page
- `investors.html` — Thesis, playbook, track record, team, partnership structure, pipeline, request access
- `news.html` — News & milestones
- `contact.html` — Contact page with form
- `styles.css` — Shared stylesheet (Fraunces + Manrope, navy/cream/brass palette)
- `RESEARCH.md` — Deep research doc referenced during the redesign
- `PLAN.md` — Implementation plan for the redesign

Fonts load from Google Fonts. No build step. No dependencies. Pure HTML/CSS + a sprinkle of JS for scroll reveal.

## Deploy to Azure Static Web Apps (recommended — free)

1. Create a new GitHub repo (e.g. `ahm-hospitality`) and push all six files to the root.
2. In the Azure portal: **Create resource → Static Web App**.
3. Connect your GitHub account, pick the repo, and select the **Free** tier.
4. Build details: set **App location** to `/`, leave Output location blank. No build command needed.
5. Azure spins up an Actions workflow, deploys in 2–3 minutes, and gives you a `*.azurestaticapps.net` URL.
6. Add your custom domain (`ahmhospitality.com`) in the Custom Domains tab. SSL is automatic.

Total time: ~15 minutes. Cost: $0 hosting, ~$10/yr domain.

## Alternative: Vercel or Netlify

Drag-and-drop the folder onto vercel.com or netlify.com — live in under a minute. Also free.

## Next steps (family content to fill in)

The site is structurally complete but contains visible `[TODO: …]` placeholders anywhere the family must supply specific content. Search for `[TODO:` across the files to see them all. Do NOT fill these with invented text — they're markers for facts the family must verify.

### Critical — fill in before investor meetings

1. **Photography.** Every placeholder shown as "Photography · [property]" or "Portrait · [name]" or "Photo · [item]" needs a real image. Budget a half-day photo shoot per property (~$400–800 each locally). Once photos exist, swap each `class="prop-img placeholder"` to `class="prop-img photo-ready"` with an inline `style="background-image: url('photos/[filename]')"`.
2. **Wire the forms to Formspree.** Both `contact.html` and `investors.html` have form actions pointing to `https://formspree.io/f/[TODO: FORMSPREE_ID]`. Sign up at formspree.io (free tier), get a form ID, and replace `[TODO: FORMSPREE_ID]` with the actual ID in both files.
3. **Founder/family specifics on About page.** Open `about.html` and replace every `[TODO: YEAR / FOUNDER NAME / FIRST PROPERTY NAME / CITY / N]` with the real history. Be specific — dates, names, properties. This is the single biggest credibility lift for LPs and brand reps.
4. **Real email addresses.** Set up `info@ahmhospitality.com`, `investors@ahmhospitality.com`, `careers@ahmhospitality.com` via Google Workspace (~$7/mo) or Zoho Mail (free for 5 accounts) once the domain is pointed.
5. **Investor relations phone line.** The footer trust column on every page has `Wire verification: always call the investor relations line before transferring funds. [TODO: PHONE]`. Replace with a real line.
6. **Leadership bios.** `leadership.html` has 4 leader slots, each with `[TODO: FULL NAME / TITLE / 60–80 word bio / email / LinkedIn]`. Reduce to 2–3 slots if only 2–3 principals exist (just delete the extra `<article class="leader">` blocks).

### Important

7. **Track record numbers on Investors page.** `investors.html` Track Record section has years, occupancies, and performance sentences as `[TODO: …]`. Fill in what the family is comfortable disclosing publicly; gate the rest behind the NDA request form.
8. **Current opportunities.** `investors.html` has two active-pipeline cards with TODO fields for equity raise, preferred return, and deal thesis. Fill in as pipeline progresses.
9. **News page with 3 real items.** `news.html` has 3 placeholder news items. Replace with real: a property opening, a Marriott/Choice franchise milestone, a local-press mention. Even two reads as a running business.
10. **Property detail page specifics.** Each `properties/*.html` has rooms count, year acquired, and booking URL TODOs. Marriott/Choice.com property pages should be linked directly (not just the brand home page).

### Nice to have

11. **Favicon and OG image.** Add a favicon.ico and og-image.jpg for link previews when shared on LinkedIn/email.
12. **Plausible or Google Analytics.** Lightweight analytics to see who's reading the Investors page.
13. **Legal page.** Footer link to privacy policy + terms — required if the form submission page collects personal info at any volume.

## Design system

**Tokens** (in `:root`, `styles.css:5-21`) — never use raw hex anywhere else:

| Token | Value | Use |
|---|---|---|
| `--navy` | `#0F2A3F` | Primary brand, headings, logo, dark backgrounds |
| `--navy-deep` | `#081B2C` | Footer, hero overlay edges, strategy items |
| `--cream` | `#F6F1E8` | Page background, body text on navy |
| `--cream-warm` | `#EFE7D6` | `section.alt` background, placeholder fill |
| `--brass` | `#B5764F` | CTA, eyebrows on dark, hover, active nav, focus outline |
| `--ink` | `#1A1A1A` | Default body text (use sparingly — harsh) |
| `--ink-soft` | `#3D3D3D` | Story / narrative paragraphs |
| `--muted` | `#6B6B6B` | Tertiary text, eyebrows on light, addresses |
| `--line` | `#D9D2C4` | Borders on light bg |

**Type scale** (canonical — every page renders identically):
- `h1` = `clamp(36px, 6vw, 64px)` weight 300 (both `.hero` and `.page-hero`)
- `h2` = `clamp(28px, 4vw, 44px)` weight 400 (every section header)
- `h3` = `20px` weight 500 (cards and rows)
- `.lead` = `clamp(15px, 1.6vw, 18px)` weight 300 (hero sub-text)
- `.prose p` = `16px` line-height 1.8 (story body)
- `.body-note` = `14px` line-height 1.7 (callouts, brand descriptions)
- `.prop-summary` = `13px` line-height 1.7 (property card descriptions)
- `.wire-verify` = `11px` opacity 0.6 (footer fine print)

**Fonts**: Fraunces (display, italic at 600+) + Manrope. Both from Google Fonts via `@import` at the top of `styles.css`.

**Mobile breakpoints** (cascading down):
- `≤900px` — hamburger drawer; investor partnership rows collapse; property-detail/hero stack
- `≤768px` — news items stack; topbar tightens; logo subtitle hides
- `≤600px` — hero h1 scales down; property-specs `<dl>` stacks; gallery 1-col; form inputs forced to 16px (prevents iOS zoom)

**Component classes** (re-use; don't duplicate):
- `.section-head`, `.section-inner`, `.section-narrative` — page layout
- `.prose`, `.body-note`, `.prop-summary`, `.wire-verify` — body paragraph variants
- `.portfolio-stats` / `.portfolio-stat` — properties page header strip
- `.brand-grid` / `.brand-block` / `.brand-name` / `.brand-meta` — franchise blocks
- `.partnership-list` / `.partnership-row` / `.pr-label` — investors page LLC structure
- `.contact-note` — cream callout with brass border
- `.property-card`, `.property-card-link`, `.prop-*`, `.property-hero`, `.property-detail`, `.property-gallery`
- `.btn`, `.btn-primary`, `.btn-ghost`, `.btn-dark`
- `.eyebrow`, `.rule`
- `.skip-link` (offscreen until keyboard-focused; targets `#main`)

**Accessibility:**
- Every page has `<a class="skip-link" href="#main">` right after `<body>`, and the first content `<section>` carries `id="main"`
- `:focus-visible` puts a 2px brass outline on every interactive element — keyboard only, mouse clicks stay clean
- Form inputs use 16px font on mobile to prevent iOS auto-zoom
- All clickable surfaces are ≥44px tall on touch devices (`@media (pointer: coarse)`)
- Decorative photos are `background-image` on `<div>`s — text alternatives come from the adjacent `h1`/`h3` or section heading

**Anti-patterns** (rejected — see commit history):
- Inline `style="font-size: ..."` blocks → use a class
- Raw hex colors → use a token
- Brass on cream for body paragraphs → AA fails at 13px (brass is for eyebrows, CTAs, accents only)
- Per-page heading clamps (h2: 38 vs 44 vs 46 vs 48) → one canonical scale

**Honest placeholder pattern**: any `.placeholder` element uses cream-warm background + dashed `--line` border + a small muted label. When a real photo ships, swap the class to `.photo-ready` and add `background-image: url(...)`.

## Files

| File | Purpose |
|---|---|
| `index.html` | Home |
| `about.html` | Family story, values, principles |
| `leadership.html` | Named principals (4 slots) |
| `properties.html` | Portfolio index (5 linked cards) |
| `properties/*.html` | 5 per-property detail pages |
| `investors.html` | Thesis, playbook, track record, pipeline, request-access form |
| `news.html` | News & milestones (currently hidden from nav) |
| `contact.html` | Contact form + direct emails |
| `styles.css` | Shared stylesheet (~1.1k lines) |
| `app.js` | Mobile nav toggle + scroll-reveal observer |
| `tools/check_links.py` | Link / image / form-target linter — run before pushing |

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Linter

Before pushing, run:

```bash
python tools/check_links.py
```

Reports any broken internal link, missing image on disk, or remaining `[TODO:` placeholder in an `href`.
