# Loving Grace Technologies website

Static site for lovinggracetechnologies.com. Plain HTML + CSS, no build tooling beyond `python3 build.py` (regenerates the pages).

- Brand tokens (colors, gradients, fonts) live at the top of `assets/style.css`, taken from the official kit
  (color-palette, typography-system, brand-voice-messaging boards). Official type blend, approved November 10, 2026:
  Quicksand SemiBold (H1 / wordmark), Montserrat Medium uppercase (eyebrows, nav, buttons),
  Manrope SemiBold/Medium (H2 / H3 / card titles), Inter (body and captions).
- Logos: `assets/logo-horizontal.*` (header), `assets/logo-primary-stacked.*` (About), app icon favicons
  (`favicon.ico`, `assets/favicon-*.png`, `assets/apple-touch-icon.png`), hero art `assets/hero-art.*`.
  All are crops/resizes of Bridgett's official files; the art itself is unaltered.
- Background texture: `assets/pattern-tile.jpg`, made from the kit pattern tile with lighting evened out and mirrored so it repeats without seams.
- Hosting: GitHub Pages from `main`, custom domain lovinggracetechnologies.com (CNAME file in the repo).

- Discovery Scout waitlist (November 12, 2026): `discovery-scout.html`. GitHub Pages also serves it at `/discovery-scout`, the same way `/services` serves `services.html`. The join form is email-only and opens a message to the company address, because this is a static site with no form backend. Nothing on the page is for sale. `scout_body()` in `build.py` notes what is left if joins should be stored without the visitor's email app.
- Content (November 10, 2026): services first, then products; Our Name origin story;
  custom AI implementation training (not off-the-shelf courses); screenshot-only project gallery (Mo'ja Liquor, Toni Green, Packout, The Keys Vault, The Sovereign Sanctum, Flash Match, and LHS Creator Network; Mo'ja shot is of mojaliquor.com; no live project links);
  no personal name in visible copy or metadata. Canonical / Open Graph URLs use https://lovinggracetechnologies.com/.
  Contact is email only. www is a CNAME to bridgett50.github.io and redirects to the apex; its HTTPS certificate must be reissued by GitHub Pages (see Settings > Pages).
