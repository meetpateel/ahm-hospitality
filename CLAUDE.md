# CLAUDE.md — AHM Hospitality website

Static marketing + investor-relations site for AHM Hospitality (Apex Hospitality Management): three family-owned hotels in Sioux Falls, SD and Worthington, MN. Full details are in `README.md`. Read it before any non-trivial change.

## Facts that matter

- **Pushing to `main` is a production deploy.** GitHub Pages serves the repo root at https://ahmhospitality.com (`CNAME`). Don't commit or push unless asked. Never delete `CNAME`.
- **No build, no dependencies.** Edit the HTML/CSS/JS directly. Don't introduce a bundler, framework, templating, or npm without the user's say-so.
- **Shared chrome is duplicated.** The `<head>` meta, topbar, nav, investor band, and footer are copy-pasted into all 12 pages. A nav/footer change must touch every file:
  `grep -l 'nav-links' *.html properties/*.html`
- `properties/*.html` reference assets with `../`. Root pages don't.
- `news.html` is intentionally hidden (not linked, not in sitemap, `Disallow` in robots.txt). Don't link it until it has real content.
- `notes/` is gitignored, local-only planning material (`TODO.md` = open questions for the family; `PLAN*.md`, `RESEARCH.md` = historical redesign docs). It may not exist in a fresh clone.

## Where things are

| Need to change… | Look in |
|---|---|
| Colors, fonts, spacing tokens | `:root` at top of `styles.css` |
| Any component style | `styles.css` (sections are banner-commented: `/* ===== NAME ===== */`) |
| Mobile menu / scroll reveal | `app.js` |
| A property's facts | `properties/<slug>.html` + its card in `properties.html` + `index.html` + `investors.html` track record |
| Photos | `photos/<slug>.jpg` (card/hero), `photos/<slug>/*.jpg` (gallery) |
| SEO | per-page `<head>`, `sitemap.xml`, `robots.txt` |

Slugs: `towneplace-suites`, `econolodge-north`, `quality-inn-worthington`.

## Rules

1. **Never invent content.** No made-up names, dates, numbers, room counts, returns, or quotes. Leave a visible `[TODO: …]` marker instead.
2. **Investor/legal copy is sensitive.** Don't reword `investors.html` or `risk-factors.html`, or any return/occupancy/ADR figure, unless explicitly asked.
3. **No inline styles** except `style="background-image: url('…')"` on a `.photo-ready` element. Add a class or modifier in `styles.css` instead.
4. **No raw hex** outside `:root`. Use the tokens.
5. **Reuse existing classes** (see README → Design system) before adding new ones. Match the existing naming: plain modifier classes like `.tight`, `.detailed`, `.alt`, `.photo-ready`.
6. Keep the canonical type scale. No per-page heading sizes.
7. Adding or removing a page or property: update nav/footer on every page if linked, `sitemap.xml`, and any "three properties" copy.

## Verify

```bash
python tools/check_links.py                 # disk + [TODO] checks, ~2s
python -m http.server 8000                  # optional: preview at http://localhost:8000
                                            # (linter also does an HTTP pass while it's running)
```

Expected warnings today: the `[TODO: FORMSPREE_ID]` form actions (contact + investors) and the `[TODO: LINK]`s in hidden `news.html`. Anything under `BROKEN-*` must be fixed.

For visual changes, check pages at desktop width and at ≤600px (breakpoints are 900 / 768 / 600).
