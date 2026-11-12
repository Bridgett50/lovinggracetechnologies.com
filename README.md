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
- Discovery Scout plans and checkout (ready for review, NOT live): `discovery-scout-plans.html`, `terms.html`, `refund-policy.html` (bodies in `ds_legal.py`), `discovery-scout-thanks.html`, styles in `assets/checkout.css`. Built from the plans block in `build.py`. Prices are the ones approved with the "Build all" Go on November 11, 2026 (Free $0; Done-for-you $19 per plan; Concierge $49 per trip; Scout $9/mo or $79/yr; Pro $19/mo or $149/yr). Payments are Square-hosted links from the Loving Grace Technologies, LLC Square account; paste them into `SQUARE_LINKS`. No Square credentials belong in this repo. While `CHECKOUT_OPEN = False`, those pages are noindex previews with a banner and disabled buttons, nothing links to them, they are not in the sitemap, and every existing page builds byte-for-byte the same. Going live needs Bridgett's Go, the Square links, and `TERMS_APPROVED = True` after she approves the Terms of Use and Refund Policy wording.
- Content (November 10, 2026): services first, then products; Our Name origin story;
  custom AI implementation training (not off-the-shelf courses); screenshot-only project gallery (Mo'ja Liquor, Toni Green, Packout, The Keys Vault, The Sovereign Sanctum, Flash Match, and LHS Creator Network; Mo'ja shot is of mojaliquor.com; no live project links);
  no personal name in visible copy or metadata. Canonical / Open Graph URLs use https://lovinggracetechnologies.com/.
  Contact is email only. www is a CNAME to bridgett50.github.io and redirects to the apex; its HTTPS certificate must be reissued by GitHub Pages (see Settings > Pages).
