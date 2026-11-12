# Generates the static pages. Run: python3 build.py
EMAIL = "bridgettsanders50@lovinggracetechnologies.com"
# Canonical site is the custom domain. Apex A records point at GitHub Pages.
# www is a CNAME to bridgett50.github.io; GitHub Pages redirects it to the apex.
SITE = "https://lovinggracetechnologies.com/"
NAV = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("products.html", "Work"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]
FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@500;600&family=Montserrat:wght@500&family=Quicksand:wght@600&display=swap" rel="stylesheet">'
)
CSS_V = "20261112a"
ICONS = {
    "agent": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><path d="M12 10.6v2.8M10.6 12h2.8"/></svg>',
    "seat": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="5" width="17" height="11" rx="2"/><path d="M9 20h6M12 16v4"/><path d="M8.5 11.2l2.2 2 4.8-4.6"/></svg>',
    "music": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 18V6l10-2v12"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="16.5" cy="16" r="2.5"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg>',
    "scale": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v16M7 20h10M5 7h14"/><path d="M5 7l-2.5 6a3 3 0 0 0 5 0L5 7zM19 7l-2.5 6a3 3 0 0 0 5 0L19 7z"/></svg>',
    "key": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="8" cy="12" r="3.5"/><path d="M11.5 12H21M18 12v3M15 12v2"/></svg>',
    "spark": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v5M12 16v5M3 12h5M16 12h5M6 6l3 3M15 15l3 3M18 6l-3 3M9 15l-3 3"/></svg>',
    "flow": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="4" width="6" height="6" rx="1.2"/><rect x="14.5" y="4" width="6" height="6" rx="1.2"/><rect x="9" y="14" width="6" height="6" rx="1.2"/><path d="M9.5 7h5M12 10v4"/></svg>',
    "sys": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="4.5" width="17" height="15" rx="2"/><path d="M3.5 9h17M8 4.5v4.5"/></svg>',
    "web": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 9h18M7 5v4"/></svg>',
    "train": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 19V7l8-3 8 3v12"/><path d="M4 7l8 3 8-3M12 10v9"/><path d="M8 19v-6.5M16 19v-6.5"/></svg>',
    "docs": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3.5h7l5 5V20.5H7z"/><path d="M14 3.5V9h5M9.5 13h5M9.5 16.5h5"/></svg>',
    "box": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.5 8 12 4l8.5 4-8.5 4z"/><path d="M3.5 8v8L12 20l8.5-4V8M12 12v8"/></svg>',
    "consult": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="8.5" cy="8" r="2.6"/><path d="M3.6 18.5v-1.2A4.4 4.4 0 0 1 8 13h1"/><circle cx="15.5" cy="8" r="2.6"/><path d="M20.4 18.5v-1.2A4.4 4.4 0 0 0 16 13h-1"/></svg>',
    "scout": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5v1.8M12 18.7V20.5M3.5 12h1.8M18.7 12H20.5"/><path d="m14.7 9.3-1.6 3.8-3.8 1.6 1.6-3.8z"/></svg>',
}

def ic(k):
    return f'<div class="icon">{ICONS[k]}</div>'

def ldjson():
    import json
    # ProfessionalService is a schema.org LocalBusiness type. Service-area
    # business: city and state only. No street address is published.
    data = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "@id": SITE + "#business",
        "name": "Loving Grace Technologies, LLC",
        "legalName": "Loving Grace Technologies, LLC",
        "url": SITE,
        "logo": SITE + "assets/emblem-512.png",
        "image": SITE + "assets/og-image.jpg",
        "email": EMAIL,
        "description": "Human-centered technology for government and commercial teams: workflow and AI automation, systems planning, websites, training, research, and small business consulting.",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Grenada",
            "addressRegion": "MS",
            "addressCountry": "US",
        },
        "areaServed": [
            {"@type": "City", "name": "Grenada", "containedInPlace": {"@type": "State", "name": "Mississippi"}},
            {"@type": "Country", "name": "United States"},
        ],
        "knowsAbout": [
            "Workflow and AI automation",
            "Systems planning",
            "Website development",
            "AI implementation training",
            "Technical documentation",
            "Packout and contents inventory software",
            "Small business consulting",
        ],
        "slogan": "Where Consciousness Meets Technology",
    }
    return '<script type="application/ld+json">' + json.dumps(data, separators=(",", ":")) + "</script>"

PAGE_TMPL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#CDCED6">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{site}assets/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<link rel="canonical" href="{url}">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" href="assets/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
{fonts}
<link rel="stylesheet" href="assets/style.css?v={css_v}">
{ld}
</head>
<body>
<header class="site"><div class="wrap">
<a class="brand" href="index.html" aria-label="Loving Grace Technologies home"><picture><source srcset="assets/logo-horizontal.webp" type="image/webp"><img src="assets/logo-horizontal.jpg" alt="Loving Grace Technologies" width="900" height="309"></picture></a>
<nav aria-label="Main"><ul>{nav}</ul></nav>
</div></header>
<main>
{body}
</main>
<footer class="site"><div class="wrap">
<div>
<div class="wordmark" aria-label="Loving Grace Technologies"><span class="loving">Loving</span> <span class="grace">Grace</span><small>TECHNOLOGIES</small></div>
<p class="sig">Sacred by design. Powered by innovation. Guided by grace.</p>
<p class="sig" style="font-size:14px;margin-top:10px;max-width:28rem">Named for a simple idea: machines should watch over people with grace, and people should remain in charge.</p>
</div>
<div>
<nav aria-label="Footer"><a href="services.html">Services</a><a href="products.html">Work</a><a href="discovery-scout.html">Discovery Scout</a><a href="about.html">About</a><a href="contact.html">Contact</a><a href="privacy.html">Privacy</a></nav>
<p><a href="mailto:{email}">{email}</a></p>
<p>Grenada, Mississippi</p>
</div>
<div class="foot-bottom">
<p class="motto">Technology with purpose<span>&bull;</span>Intelligence with compassion<span>&bull;</span>Innovation with integrity</p>
<p>&copy; 2026 Loving Grace Technologies, LLC</p>
</div>
</div></footer>
</body>
</html>
"""

def page(fn, title, desc, body, extra_ld="", extra_head=""):
    nav = "".join(
        f'<li><a href="{h}"{" aria-current=page" if h == fn else ""}>{t}</a></li>'
        for h, t in NAV
    )
    path = "" if fn == "index.html" else fn
    return PAGE_TMPL.format(
        title=title, desc=desc, url=SITE + path, site=SITE,
        fonts=FONTS, css_v=CSS_V, ld=ldjson() + extra_ld + extra_head, nav=nav, body=body, email=EMAIL,
    )

def shot(stem, title, cap):
    return (
        "<figure><div class=\"shot\"><picture>"
        f"<source srcset=\"assets/{stem}.webp\" type=\"image/webp\">"
        f"<img src=\"assets/{stem}.jpg\" alt=\"{title}\" width=\"1440\" height=\"1100\">"
        "</picture></div><figcaption>"
        f"<h3>{title}</h3><p>{cap}</p></figcaption></figure>"
    )

GALLERY = (
    "<div class=\"gallery\">"
    + shot("portfolio-moja", "Mo'ja Liquor website",
           "A public-facing website for a Mississippi package store, designed and built for the shop's own brand, gift orders, and pickup-ready shopping.")
    + shot("portfolio-toni", "Toni Green artist website",
           "An official artist site for vocalist Toni Green, built to present her music, merch, booking, and the release of God Knew Her Name.")
    + shot("portfolio-packout", "Loving Grace Packout software",
           "Contents inventory, packout, storage, packback, condition documentation, and claims-reporting software for insurance contents work.")
    + shot("portfolio-keys", "The Keys Vault website",
           "A resource site for courses, eBooks, and tools, with materials in English and Spanish.")
    + shot("portfolio-sanctum", "The Sovereign Sanctum website",
           "A public site for The Sovereign Sanctum, presenting its science, spirit, and robotics work.")
    + shot("portfolio-flash", "Flash Match",
           "A speed-dating web app for timed match rounds and event sign-up.")
    + shot("portfolio-lhs", "LHS Creator Network",
           "A creator-network roster and CRM, shown at its public sign-in page.")
    + "</div>"
)

def discovery_ld():
    import json
    # Waitlist page only. No Offer, price, or download URL: nothing is for sale
    # here, and the working product is not public.
    data = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "@id": SITE + "discovery-scout.html#webpage",
        "url": SITE + "discovery-scout.html",
        "name": "Discovery Scout waitlist",
        "description": "Plan legal outdoor hunts with Discovery Scout. It scores areas from commercially allowed open data and explains why. Waitlist only. Nothing to buy here.",
        "about": {
            "@type": "SoftwareApplication",
            "name": "Discovery Scout",
            "applicationCategory": "LifestyleApplication",
            "operatingSystem": "Web",
            "description": "A planning tool from Loving Grace Technologies for legal outdoor hunts. It uses commercially allowed open data, scores areas, and explains the reasons. It does not guarantee finds. This page is a waitlist. Planned plans are not for sale here.",
            "featureList": [
                "Area scores with reasons you can read",
                "Planning from commercially allowed open data: geology, land status, and documented public sites",
                "Topics: gems, gold, fossils, shark teeth, meteorites, metal detecting of modern items only, and storm and expedition planning",
            ],
            "provider": {"@id": SITE + "#business"},
        },
        "publisher": {"@id": SITE + "#business"},
    }
    return '<script type="application/ld+json">' + json.dumps(data, separators=(",", ":")) + "</script>"


def scout_body():
    # Delivery: static GitHub Pages cannot accept a form post. The form is a
    # progressive enhancement over mailto. Submitting it opens the visitor's
    # email app with the address filled in; they send the message to finish
    # joining. A plain mailto link is on the page for when no app opens.
    #
    # Left to wire, if joins should be stored without the visitor's email app:
    # a form endpoint that emails or saves the address only. FormSubmit
    # (formsubmit.co) needs no account, but the first use must be confirmed
    # from the company inbox, and a server-side activation attempt was blocked
    # by Cloudflare. Do not add a checkout, prices, or extra fields.
    script = (
        "<script>\n"
        "(function () {\n"
        '  var form = document.getElementById("waitlist-form");\n'
        "  if (!form) return;\n"
        '  form.addEventListener("submit", function (event) {\n'
        "    event.preventDefault();\n"
        "    if (!form.reportValidity()) return;\n"
        '    var input = document.getElementById("waitlist-email");\n'
        '    var email = (input && input.value || "").trim();\n'
        '    var body = "Please add this address to the Discovery Scout waitlist:\\n" + email + "\\n\\nJoining is free. This is not a purchase.";\n'
        '    var note = document.getElementById("joined");\n'
        "    if (note) {\n"
        "      note.hidden = false;\n"
        "      note.focus();\n"
        "    }\n"
        '    window.location.href = "mailto:' + EMAIL + '?subject=" + encodeURIComponent("Discovery Scout waitlist") + "&body=" + encodeURIComponent(body);\n'
        "  });\n"
        "})();\n"
        "</script>"
    )
    return f'''
<div class="page-head"><div class="wrap"><h1><span class="gold">Discovery</span> Scout</h1><p>A planning tool for legal outdoor hunts. <a href="#waitlist">Join the waitlist</a>. Nothing on this page is for sale.</p></div></div>
<section class="approach"><div class="wrap">
<article class="card product">{ic("scout")}
<span class="caption">Planning tool</span>
<h2>Plan the hunt. Read the reasons.</h2>
<p>Discovery Scout helps people plan legal outdoor hunts using commercially allowed open data: geology, land status, and documented public sites. It scores areas and explains the reasons for each score. It is a planning tool, not a guarantee of finds.</p>
<p>Planning topics are gems, gold, fossils, shark teeth, meteorites, metal detecting of modern items only, and storm and expedition planning.</p>
<ul>
<li>Scores come with reasons you can read</li>
<li>The data is commercially allowed open data</li>
<li>Metal detecting is limited to modern items</li>
<li>It is not for archaeological or artifact hunting, and it is not a way to take cultural artifacts</li>
<li>It does not give permission to enter land, dig, or collect. Site rules and collecting laws are yours to check before you go</li>
</ul>
<p>Loving Grace Technologies is a technology company in Grenada, Mississippi. This page is the public waitlist. It is not a login, and it does not open the working product.</p>
</article>
</div></section>
<section class="textured-tile approach" id="plans"><div class="wrap">
<p class="caption">Not offered for purchase here</p>
<h2>Planned plans</h2><div class="rule"></div>
<p class="lead">These are names for plans we expect to offer later. They are not offered for purchase on this page. There is no checkout and no payment.</p>
<div class="grid plans">
<article class="card"><p class="caption">Coming soon</p><h3>Free</h3><p>A planned way to plan a legal hunt with open data and read the reasons behind each area score.</p></article>
<article class="card"><p class="caption">Coming soon</p><h3>Done-for-you</h3><p>A planned option where a trip plan is prepared for you. You still decide whether to go, and you book any dig site or operator yourself.</p></article>
<article class="card"><p class="caption">Coming soon</p><h3>Concierge planning</h3><p>Planning help for a trip you want to take. You book the dig site or operator directly. Loving Grace Technologies does not book the trip.</p></article>
<article class="card"><p class="caption">Coming soon</p><h3>Scout and Pro</h3><p>Planned subscription tiers for ongoing planning access. They are not open for purchase on this page.</p></article>
</div>
</div></section>
<section class="approach" id="waitlist" aria-labelledby="waitlist-title"><div class="wrap">
<h2 id="waitlist-title">Join the waitlist</h2><div class="rule"></div>
<div class="card waitlist">
<p id="joined" class="joined" tabindex="-1" role="status" hidden>Your email app should open with the waitlist message filled in. Send that message to finish joining. We will use the address only to write when there is news. Joining is free, and it is not a purchase. If no email app opens, use the link under the form.</p>
<p id="waitlist-help">Leave an email address and send it to us. We will write when there is news about Discovery Scout, and we use the address only for that. Joining the waitlist is free. This page does not take payment.</p>
<form id="waitlist-form" action="mailto:{EMAIL}?subject=Discovery%20Scout%20waitlist" method="post" enctype="text/plain">
<div class="field">
<label for="waitlist-email">Email</label>
<input id="waitlist-email" name="email" type="email" autocomplete="email" inputmode="email" autocapitalize="none" spellcheck="false" maxlength="254" required aria-describedby="waitlist-help">
</div>
<button class="btn primary" type="submit">Join the waitlist</button>
</form>
<p class="hint">If the form does not open an email app, email <a href="mailto:{EMAIL}?subject=Discovery%20Scout%20waitlist">{EMAIL}</a> with the subject &ldquo;Discovery Scout waitlist&rdquo;.</p>
<p class="hint">Loving Grace Technologies, LLC. Grenada, Mississippi, United States.</p>
</div>
{script}
</div></section>'''


# ---------------------------------------------------------------------------
# Discovery Scout plans and Square checkout (READY FOR REVIEW, NOT LIVE)
# ---------------------------------------------------------------------------
# Prices and plan names come from the "Build all" Go of November 11, 2026
# (private repo Bridgett50/discovery-scout, app/pricing.py at commit ae8de65,
# and the Discovery Scout plan Doc, Section 18). Do not change a price here
# without a new Go from Bridgett.
#
# Payments: Square-hosted checkout links from the Loving Grace Technologies,
# LLC Square account (free Square plan). This static site never sees a card
# number and holds no Square credentials. Square payment links and
# subscription checkout links are public URLs, so they are safe to commit.
# No application ID, access token, or location ID belongs in this repo.
#
# Go-live switch. While CHECKOUT_OPEN is False:
#   - the plans and terms pages are built as noindex previews with a banner,
#   - every checkout button is disabled, even if a link is filled in,
#   - no existing page links to them and the sitemap does not list them,
#   - every existing page is byte-for-byte the same as before this change.
# Turning it on needs Bridgett's Go, the Square links below, and approved
# terms (see TERMS_APPROVED).
CHECKOUT_OPEN = False
TERMS_APPROVED = False  # the terms and refund wording below is a draft until Bridgett approves it

# Paste Square links here after they are created in the Loving Grace
# Technologies, LLC Square Dashboard. Leave "" for anything not on sale yet;
# an empty link shows "Not open yet" and no button.
SQUARE_LINKS = {
    "dfy": "",            # Done-for-you plan, $19 one-time payment link
    "concierge": "",      # Concierge planning, $49 one-time payment link
    "scout_month": "",    # Scout, $9 monthly subscription checkout link
    "scout_year": "",     # Scout, $79 yearly subscription checkout link
    "pro_month": "",      # Pro, $19 monthly subscription checkout link
    "pro_year": "",       # Pro, $149 yearly subscription checkout link
}
_SQUARE_HOSTS = ("https://square.link/u/", "https://checkout.square.site/")
for _k, _v in SQUARE_LINKS.items():
    if _v and not _v.startswith(_SQUARE_HOSTS):
        raise SystemExit(f"SQUARE_LINKS[{_k!r}] must be a Square-hosted checkout link, got {_v!r}")

DS_PLANS = [
    {"id": "free", "name": "Free", "price": "$0", "per": "", "kind": "free",
     "blurb": "Spot reports and a basic hunt plan.",
     "features": ["Spot reports: geology, area score with reasons, legal checklist, historic topo maps",
                  "Basic hunt plan: itinerary outline, gear list, nearest keep-what-you-find sites",
                  "A legal checklist for every hunt type"],
     "links": []},
    {"id": "dfy", "name": "Done-for-you plan", "price": "$19", "per": "per hunt plan", "kind": "one-time",
     "blurb": "One complete trip plan, prepared for you.",
     "features": ["Everything in Free",
                  "Full itinerary with drive-time, ticket, and fuel estimates",
                  "A filled-in landowner permission letter, when the land is private",
                  "Weather forecast and links to lodging and the site's own booking page",
                  "A printable trip packet"],
     "links": [("dfy", "Buy a $19 plan")]},
    {"id": "concierge", "name": "Concierge planning", "price": "$49", "per": "per trip", "kind": "one-time",
     "blurb": "Planning help from a person for one trip.",
     "features": ["Everything in the Done-for-you plan",
                  "We check the site's posted hours, prices, and rules shortly before your trip",
                  "Help getting ready to book: what to book, where, and when",
                  "Follow-up help with a permission letter for private land",
                  "You book and pay the dig site, guide, or lodging yourself. We do not book trips or take payment for anyone else"],
     "links": [("concierge", "Buy concierge planning, $49")]},
    {"id": "scout", "name": "Scout", "price": "$9", "per": "a month, or $79 a year", "kind": "subscription",
     "blurb": "For regular weekend hunters.",
     "features": ["Everything in Free", "3 done-for-you plans a month", "Saved spots and trip history"],
     "links": [("scout_month", "Scout monthly, $9"), ("scout_year", "Scout yearly, $79")]},
    {"id": "pro", "name": "Pro", "price": "$19", "per": "a month, or $149 a year", "kind": "subscription",
     "blurb": "Unlimited plans.",
     "features": ["Unlimited done-for-you plans",
                  "All hunt types, including meteorite, metal detecting of modern items, and expedition planning"],
     "links": [("pro_month", "Pro monthly, $19"), ("pro_year", "Pro yearly, $149")]},
]

DS_PREVIEW_BANNER = (
    '<div class="ds-preview" role="note"><div class="wrap"><strong>Preview only.</strong> '
    'Checkout is not open. Nothing on this page can be bought yet, and no card is collected.'
    '</div></div>'
)
TERMS_DRAFT_NOTE = (
    '<p class="ds-draft"><strong>Draft for approval.</strong> This wording has not been approved and is not in effect.</p>'
)

def _ds_buttons(plan):
    out = []
    for key, label in plan["links"]:
        url = SQUARE_LINKS.get(key, "")
        if CHECKOUT_OPEN and url:
            out.append(f'<a class="btn primary ds-buy" data-ds-buy href="{url}" rel="noopener" aria-disabled="true">{label}</a>')
        else:
            out.append(f'<span class="btn secondary ds-off" aria-disabled="true">{label}<small class="ds-soon">Not open yet</small></span>')
    return '<div class="btns ds-btns">' + "".join(out) + "</div>" if out else ""

def plans_body():
    cards = []
    for p in DS_PLANS:
        feats = "".join(f"<li>{f}</li>" for f in p["features"])
        per = f' <span class="ds-per">{p["per"]}</span>' if p["per"] else ""
        cards.append(
            f'<article class="card ds-plan" id="plan-{p["id"]}"><p class="caption">{p["kind"].replace("-", " ").title() if p["kind"] != "free" else "No payment"}</p>'
            f'<h3>{p["name"]}</h3><p class="ds-price">{p["price"]}{per}</p><p>{p["blurb"]}</p><ul>{feats}</ul>'
            f'{_ds_buttons(p)}</article>'
        )
    script = (
        "<script>\n"
        "(function () {\n"
        '  var box = document.getElementById("ds-agree");\n'
        '  var buys = document.querySelectorAll("[data-ds-buy]");\n'
        "  function sync() {\n"
        "    for (var i = 0; i < buys.length; i++) {\n"
        '      buys[i].setAttribute("aria-disabled", box && box.checked ? "false" : "true");\n'
        "    }\n"
        "  }\n"
        "  for (var i = 0; i < buys.length; i++) {\n"
        '    buys[i].addEventListener("click", function (e) {\n'
        "      if (!box || !box.checked) { e.preventDefault(); if (box) box.focus(); }\n"
        "    });\n"
        "  }\n"
        '  if (box) box.addEventListener("change", sync);\n'
        "  sync();\n"
        "})();\n"
        "</script>"
    )
    banner = "" if CHECKOUT_OPEN else DS_PREVIEW_BANNER
    return f'''{banner}
<div class="page-head"><div class="wrap"><h1><span class="gold">Discovery Scout</span> plans</h1><p>Online planning software for legal outdoor hunts, with optional planning help from a person. It does not guarantee a find.</p></div></div>
<section class="approach"><div class="wrap">
<p class="lead">Pick the plan that fits your trip. Payments go through Square&rsquo;s secure checkout for Loving Grace Technologies, LLC. Our site never sees your card number. Prices are in U.S. dollars.</p>
<div class="card ds-agree"><label><input type="checkbox" id="ds-agree"><span>I have read the <a href="discovery-scout-terms.html">Terms of Sale and Refund Policy</a>. I understand Discovery Scout is planning software and planning help, not a travel agency, and it does not guarantee any find.</span></label></div>
<div class="grid ds-grid">
{"".join(cards)}
</div>
<div class="card ds-notes">
<h3>Good to know</h3>
<ul>
<li>Discovery Scout is a planning tool. Area scores describe geology and documented sites. They are not a chance of finding anything.</li>
<li>We do not sell tickets, tours, permits, lodging, or gear. Anything you pay a dig site, guide, or hotel, you pay them directly, under their own terms. Loving Grace Technologies charges nothing on their behalf.</li>
<li>A plan does not give permission to enter land, dig, or collect. Check the site rules and collecting laws before you go.</li>
<li>Not for archaeological or artifact hunting. Metal detecting is for modern items only.</li>
<li>Questions before you buy: <a href="mailto:{EMAIL}?subject=Discovery%20Scout%20plans">{EMAIL}</a></li>
</ul>
</div>
<p style="margin-top:24px"><a class="more" href="discovery-scout.html">Back to Discovery Scout</a></p>
</div></section>
{script}'''

def terms_body():
    banner = "" if CHECKOUT_OPEN else DS_PREVIEW_BANNER
    draft = "" if TERMS_APPROVED else TERMS_DRAFT_NOTE
    return f'''{banner}
<div class="page-head"><div class="wrap"><h1><span class="gold">Terms of Sale</span> and Refund Policy</h1><p>Discovery Scout by Loving Grace Technologies, LLC</p></div></div>
<section><div class="wrap prose">
{draft}
<h2>Who you are buying from</h2>
<p>Discovery Scout is sold by Loving Grace Technologies, LLC, Grenada, Mississippi, United States. Payments are processed by Square for Loving Grace Technologies, LLC. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>What Discovery Scout is</h2>
<p>Discovery Scout is online planning software for legal outdoor hunts, such as gems, gold panning, fossils, shark teeth, meteorites, and metal detecting for modern items. Concierge planning is planning help from a person. Area scores describe geology and documented public sites. They are not a promise or a chance of finding anything.</p>
<h2>What Discovery Scout is not</h2>
<ul>
<li>It is not a travel agency. We do not book, sell, or resell tickets, tours, permits, lodging, transportation, or gear.</li>
<li>Dig sites, guides, parks, hotels, and stores are independent. You book and pay them directly, on their terms and refund rules. Loving Grace Technologies does not charge anything on their behalf and is not responsible for their prices, closures, or services.</li>
<li>It does not give permission to enter land, dig, or collect. You are responsible for following site rules, landowner wishes, and collecting laws.</li>
<li>It is not for archaeological or artifact hunting, or for taking cultural artifacts.</li>
</ul>
<h2>Plans and prices</h2>
<ul>
<li>Done-for-you plan: $19 per hunt plan, paid once.</li>
<li>Concierge planning: $49 per trip, paid once.</li>
<li>Scout: $9 a month or $79 a year, renews automatically until you cancel.</li>
<li>Pro: $19 a month or $149 a year, renews automatically until you cancel.</li>
</ul>
<p>Prices are in U.S. dollars. Any tax shown at checkout is added by Square.</p>
<h2>How a plan is delivered</h2>
<p>After you pay, we email you at the address you gave at checkout to collect your trip details (what you want to look for, where you are starting, your dates, and your party size). We deliver your plan by email within 3 business days of receiving those details.</p>
<h2>Subscriptions and cancelling</h2>
<p>Scout and Pro renew at the end of each month or year at the price you signed up for. You can cancel at any time with the manage-subscription link in your Square receipt email, or by emailing us. Cancelling stops the next renewal. You keep access until the end of the period you already paid for.</p>
<h2>Refund policy</h2>
<ul>
<li><strong>Before we start:</strong> if you ask before we begin your Done-for-you or Concierge plan, we refund the full amount.</li>
<li><strong>After delivery:</strong> if your plan has a factual mistake we made (for example, a wrong site, a closed site we listed as open, or a missing legal checklist), tell us within 14 days of delivery. We will correct it, or refund you if we cannot.</li>
<li><strong>Subscriptions:</strong> if you ask within 7 days of your first payment and have not received a done-for-you plan, we refund that first payment. Renewals are not refunded for partial periods, but cancelling stops the next charge.</li>
<li><strong>Not refundable by us:</strong> weather, site closures, finding nothing, or anything you paid to a dig site, guide, hotel, or store. Ask that business about its own refund rules.</li>
<li>Refunds go back to the card you paid with, through Square. Email <a href="mailto:{EMAIL}?subject=Discovery%20Scout%20refund">{EMAIL}</a> with your receipt.</li>
</ul>
<h2>Your safety</h2>
<p>Outdoor hunts can involve heat, water, weather, and rough ground. Plans are a starting point. Use your own judgment, follow posted rules, and change or cancel your trip if conditions are unsafe.</p>
<h2>Changes</h2>
<p>If we change these terms, the new version applies to purchases made after we post it. The date at the top of this page shows the latest version.</p>
<p><a class="more" href="discovery-scout-plans.html">Back to plans</a></p>
</div></section>'''

def thanks_body():
    banner = "" if CHECKOUT_OPEN else DS_PREVIEW_BANNER
    return f'''{banner}
<div class="page-head"><div class="wrap"><h1><span class="gold">Thank you</span></h1><p>Your Discovery Scout payment went through Square.</p></div></div>
<section><div class="wrap prose">
<div class="card">
<p>Square emails your receipt. We will email you at the address you gave at checkout to collect your trip details, then deliver your plan by email.</p>
<p style="margin-top:14px">Questions, changes, or a refund request: <a href="mailto:{EMAIL}?subject=Discovery%20Scout%20order">{EMAIL}</a>.</p>
<p style="margin-top:14px">Remember: you book and pay any dig site, guide, or lodging directly. Check site rules and collecting laws before you go.</p>
</div>
</div></section>'''

DS_CHECKOUT_HEAD = '<link rel="stylesheet" href="assets/checkout.css?v=20261112c">'
DS_NOINDEX = '<meta name="robots" content="noindex,nofollow">'


P = {}

P["index.html"] = (
    "Loving Grace Technologies | Where Consciousness Meets Technology",
    "Human-centered technology for government and commercial teams: workflow and AI automation, systems planning, websites, training, research, and small business consulting. Grenada, Mississippi.",
    f'''
<section class="hero" aria-labelledby="hero-title" style="padding:0"><div class="wrap">
<div class="divider" aria-hidden="true"></div>
<div class="copy">
<p class="eyebrow">Where Consciousness Meets Technology</p>
<h1 id="hero-title"><span class="gold">Technologies that protect consciousness</span><span class="l2">and expand human potential.</span></h1>
<p class="hero-lead">We design human-centered tools &mdash; workflow and AI systems, websites, training, research, and small business consulting &mdash; so people stay in charge of the work that matters.</p>
<div class="btns"><a class="btn primary" href="mailto:{EMAIL}">Start a conversation</a><a class="btn secondary" href="services.html">See our services</a></div>
</div>
<div class="art"><picture><source srcset="assets/hero-art.webp" type="image/webp"><img src="assets/hero-art.jpg" alt="" width="675" height="819"></picture></div>
</div></section>

<section class="approach" id="services"><div class="wrap">
<p class="caption">Services</p>
<h2>What we build and teach</h2><div class="rule"></div>
<p class="lead">Loving Grace Technologies is an R&amp;D company that also takes on selected client work. We help teams plan, build, and document technology &mdash; and we train people to implement it well.</p>
<div class="grid services-grid">
<div class="card">{ic("flow")}<h3>Workflow and AI automation</h3><p>AI-assisted workflow design so routine work is faster and easier to audit, with people still approving what matters.</p></div>
<div class="card">{ic("sys")}<h3>Computer systems planning</h3><p>Practical planning for the systems a team already has and the ones it needs next, including requirements, tool selection, and implementation maps.</p></div>
<div class="card">{ic("web")}<h3>Websites and web applications</h3><p>Design and build of websites and web apps for businesses and public-facing work, including custom product software.</p></div>
<div class="card">{ic("train")}<h3>AI implementation training</h3><p>We train teams to implement AI using systems we build, not off-the-shelf courses. Every engagement is custom-built for the work at hand.</p></div>
<div class="card">{ic("docs")}<h3>Documentation, evidence, and research</h3><p>Technical documentation, evidence and governance support, and research strategy for government and commercial teams.</p></div>
<div class="card">{ic("box")}<h3>Packout software</h3><p>Software for contents inventory, packout, storage, packback, condition documentation, and claims reporting.</p></div>
<div class="card">{ic("consult")}<h3>Small Business Consulting</h3><p>We help small businesses get ready for an AI-powered world. We look at how your business runs today, find where AI can save you time and money, and build a clear, practical plan to put it to work. We also help with the foundations around it: planning, registrations, and contracting readiness, so you&rsquo;re set up to grow.</p></div>
</div>
<p style="margin-top:28px"><a class="more" href="services.html">All services</a></p>
</div></section>

<section class="textured-tile approach" id="work"><div class="wrap">
<p class="caption">Products</p>
<h2>What we are building</h2><div class="rule"></div>
<p class="lead">Human-centered deep tech on one principle: our technology does real work, and people stay in charge of every decision that matters.</p>
<div class="grid">
<div class="card">{ic("agent")}<h3>Loving Grace Agent</h3><p>A self-hosted AI assistant with memory, skills, and computer use. It always asks before sending, paying, or deleting.</p><hr><a class="more" href="products.html#agent">Learn more about Loving Grace Agent</a></div>
<div class="card">{ic("seat")}<h3>Second Seat</h3><p>It turns what a small-business owner agrees to in a meeting into PayPal payments. AI drafts each payment, then a separate checker compares it against the owner&rsquo;s own words and blocks anything that doesn&rsquo;t match, like a changed bank account or an inflated amount. Nothing is paid until the owner approves it with one tap, and every payment keeps the quote it came from as its receipt.</p><hr><a class="more" href="https://youtu.be/1VJKjwJzRN0">Watch the demo</a></div>
<div class="card">{ic("music")}<h3>AI Music &amp; Studio Tools</h3><p>AI music and studio tools for blues and soul recordings, made to support the artist&rsquo;s own voice.</p><hr><a class="more" href="products.html#music">Learn more about AI Music &amp; Studio Tools</a></div>
<div class="card">{ic("scout")}<h3>Discovery Scout</h3><p>A planning tool for legal outdoor hunts. It uses commercially allowed open data, scores areas, and explains why. It does not guarantee a find. The public page is a waitlist, with nothing to buy.</p><hr><a class="more" href="discovery-scout.html">Learn more about Discovery Scout</a></div>
</div>
</div></section>

<section class="approach" id="projects"><div class="wrap">
<p class="caption">Selected projects</p>
<h2>Sites and software we have built</h2><div class="rule"></div>
<p class="lead">Screenshots from recent website and software builds. These are examples of work, not live links.</p>
{GALLERY}
</div></section>

<section class="textured-tile approach"><div class="wrap">
<h2>Our Approach</h2><div class="rule"></div>
<p class="lead">Rigorous inquiry, compassionate design. We work at the intersection of consciousness and technology with elegance, integrity, and precision.</p>
<div class="grid">
<div class="card">{ic("scale")}<h3>Ethical Intelligence</h3><p>Our tools draft and prepare. A person approves anything that is sent, paid, or deleted.</p></div>
<div class="card">{ic("key")}<h3>Luminous Intelligence</h3><p>Clear, grounded AI that explains its work. Self-hosted options keep files and memory on infrastructure you control.</p></div>
<div class="card">{ic("heart")}<h3>Human-Centered Innovation</h3><p>Refined, practical tools that small businesses, creators, government, and research teams can run and trust.</p></div>
</div>
</div></section>

<section class="band"><div class="wrap">
<h2>Scientific Rigor. Human Wisdom. Conscious Future.</h2>
<p>Engineering a more conscious world, together. Partnerships, pilots, research, and government collaboration are welcome.</p>
<a class="btn primary" href="mailto:{EMAIL}">Start a conversation</a>
</div></section>''',
)

P["services.html"] = (
    "Services | Loving Grace Technologies",
    "Workflow and AI automation, systems planning, websites, AI implementation training, documentation, research, packout software, and small business consulting from Loving Grace Technologies.",
    f'''
<div class="page-head"><div class="wrap"><h1><span class="gold">Our</span> Services</h1><p>An R&amp;D company that helps teams plan, build, document, and implement technology &mdash; with people still in charge.</p></div></div>
<section class="approach"><div class="wrap">
<article class="card product">{ic("flow")}<span class="caption">Automation</span><h2>Workflow and AI automation</h2>
<p>AI-assisted workflow design, intake, prompt systems, and approval workflows for repetitive tasks. We help structure document-heavy operations into clear processes and practical automation plans, with human review built into decisions.</p></article>
<article class="card product">{ic("sys")}<span class="caption">Planning</span><h2>Computer systems planning</h2>
<p>Requirements, tool selection, integration maps, and implementation documentation. We plan for the systems a team already has and the ones it needs next.</p></article>
<article class="card product">{ic("web")}<span class="caption">Web design and development</span><h2>Websites and web applications</h2>
<p>Design and build of websites and web apps for businesses, artists, and public-facing work, as well as custom product software. Selected examples appear on our Work page as screenshots.</p></article>
<article class="card product">{ic("train")}<span class="caption">Custom training</span><h2>AI implementation training</h2>
<p>We train teams to implement AI using systems we build, not off-the-shelf courses. Curriculum and sessions are custom-built around the tools, workflows, and approvals that team will actually use.</p></article>
<article class="card product">{ic("docs")}<span class="caption">Writing and research</span><h2>Documentation, evidence, and research strategy</h2>
<p>Operating procedures, runbooks, evidence matrices, decision records, review checkpoints, and source-backed research for government and commercial teams, including concept papers and proposal support.</p></article>
<article class="card product">{ic("box")}<span class="caption">Software</span><h2>Packout software</h2>
<p>Software for contents inventory, packout, storage, packback, condition documentation, and claims reporting. Loving Grace Technologies builds and supports the software.</p></article>
<article class="card product">{ic("consult")}<span class="caption">Consulting</span><h2>Small Business Consulting</h2>
<p>We help small businesses get ready for an AI-powered world. We look at how your business runs today, find where AI can save you time and money, and build a clear, practical plan to put it to work. We also help with the foundations around it: planning, registrations, and contracting readiness, so you&rsquo;re set up to grow.</p></article>
</div></section>''',
)

P["products.html"] = (
    "Work | Loving Grace Technologies",
    "Products and selected projects from Loving Grace Technologies, including Discovery Scout, Second Seat, packout software, and website builds.",
    f'''
<div class="page-head"><div class="wrap"><h1><span class="gold">Our</span> Work</h1><p>Products we are building, and selected websites and software already in the world.</p></div></div>
<section class="approach"><div class="wrap">
<article class="card product" id="agent">{ic("agent")}
<span class="caption">Self-hosted AI assistant</span>
<h2>Loving Grace Agent</h2>
<p>The Loving Grace Agent runs on your own server. It remembers context, learns new skills, and can use a computer to get tasks done.</p>
<ul><li>Memory that carries context across conversations</li><li>Skills it can add and reuse for repeat work</li><li>Computer use for browser and desktop tasks</li><li>Always asks before sending, paying, or deleting</li></ul>
</article>
<article class="card product" id="second-seat">{ic("seat")}
<span class="caption">PayPal payments</span>
<h2>Second Seat</h2>
<p>It turns what a small-business owner agrees to in a meeting into PayPal payments. AI drafts each payment, then a separate checker compares it against the owner&rsquo;s own words and blocks anything that doesn&rsquo;t match, like a changed bank account or an inflated amount. Nothing is paid until the owner approves it with one tap, and every payment keeps the quote it came from as its receipt.</p>
<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/1VJKjwJzRN0" title="Second Seat demo" loading="lazy" allow="accelerometer; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<p style="margin-top:12px"><a href="https://youtu.be/1VJKjwJzRN0">Watch the demo</a></p>
</article>
<article class="card product" id="music">{ic("music")}
<span class="caption">For blues and soul recordings</span>
<h2>AI Music &amp; Studio Tools</h2>
<p>Tools that help artists and producers work with their recordings, including stem separation, editing, and AI-assisted music creation. Built to support the artist&rsquo;s voice, and used only with the artist&rsquo;s permission.</p>
</article>
<article class="card product" id="discovery-scout">{ic("scout")}
<span class="caption">Waitlist</span>
<h2>Discovery Scout</h2>
<p>A planning tool for legal outdoor hunts. It uses commercially allowed open data (geology, land status, and documented public sites), scores areas, and explains the reasons. It covers gems, gold, fossils, shark teeth, meteorites, metal detecting of modern items only, and storm and expedition planning. It does not guarantee a find, and it is not for archaeological or artifact hunting.</p>
<p>The public page is a waitlist. Planned plan names are described there as coming soon. Nothing is for sale on that page, and this site does not offer a trial login or a checkout.</p>
<p><a class="more" href="discovery-scout.html">Learn more about Discovery Scout</a></p>
</article>
<article class="card product" id="presence">{ic("spark")}
<span class="caption">Research and development</span>
<h2>Loving Grace Presence</h2>
<p>Holographic presence research: technology that can extend how a person is represented, while the person keeps final authority. Work on this line has been invited to pitch on the NSF SBIR path, with Mississippi MS-FAST Phase 0 in progress. This is not an award.</p>
</article>
</div></section>
<section class="textured-tile approach" id="projects"><div class="wrap">
<p class="caption">Selected projects</p>
<h2>Sites and software we have built</h2><div class="rule"></div>
<p class="lead">Screenshots from recent website and software builds, including client sites and our packout software. These are examples of work, not live links.</p>
{GALLERY}
</div></section>''',
)

P["about.html"] = (
    "About | Loving Grace Technologies",
    "About Loving Grace Technologies, LLC, a human-centered technology company in Grenada, Mississippi.",
    f'''
<div class="page-head"><div class="wrap"><h1><span class="gold">About</span> Loving Grace</h1><p>Where Consciousness Meets Technology.</p></div></div>
<section><div class="wrap prose">
<div class="wordmark-banner"><picture><source srcset="assets/logo-primary-stacked.webp" type="image/webp"><img src="assets/logo-primary-stacked.jpg" alt="Loving Grace Technologies logo" width="900" height="788"></picture></div>
<p>Loving Grace Technologies is a Mississippi company building human-centered deep tech. We combine scientific rigor with human wisdom: tools that help people work, document, and decide with more clarity, and with compassion in the design.</p>
<p>We are an R&amp;D company. We also take on selected client work &mdash; systems planning, websites, custom software, AI implementation training, and small business consulting &mdash; always with people in charge of the decisions that matter.</p>

<div class="name-story">
<p class="caption">Our Name</p>
<h2>Machines of loving grace</h2><div class="rule"></div>
<p>Loving Grace Technologies takes its name from Richard Brautigan&rsquo;s 1967 poem &ldquo;All Watched Over by Machines of Loving Grace,&rdquo; and from Dario Amodei&rsquo;s later essay of the same title. Both imagine technology that watches over people with care, not control &mdash; a world where people, nature, and machines live in harmony, and humans keep final authority.</p>
<p>That is the standard we build to: tools that extend what a person can do, without taking away what only a person should decide.</p>
</div>

<h2>Company information</h2><div class="rule"></div>
<div class="card"><dl class="facts">
<dt>Legal name</dt><dd>Loving Grace Technologies, LLC</dd>
<dt>Location</dt><dd>Grenada, Mississippi, United States</dd>
<dt>Formed</dt><dd>June 2, 2026</dd>
<dt>SAM.gov</dt><dd>Active registration (activated July 10, 2026; renewal June 23, 2027)</dd>
<dt>UEI</dt><dd>U5D5QT7QLRQ5</dd>
<dt>CAGE code</dt><dd>222V5</dd>
<dt>NAICS</dt><dd>541512 Computer Systems Design Services<br>541720 Research and Development in the Social Sciences and Humanities<br>541990 All Other Professional, Scientific, and Technical Services</dd>
</dl></div>
</div></section>''',
)

P["contact.html"] = (
    "Contact | Loving Grace Technologies",
    "Contact Loving Grace Technologies by email.",
    f'''
<div class="page-head"><div class="wrap"><h1><span class="gold">Start a</span> conversation</h1><p>Tell us about the system, site, training, or consulting you need.</p></div></div>
<section><div class="wrap prose">
<div class="card">
<p>For partnerships, pilots, website or software work, training, small business consulting, press, or government and research collaboration, email us and we&rsquo;ll get back to you.</p>
<p style="margin:22px 0"><a class="btn primary" href="mailto:{EMAIL}">{EMAIL}</a></p>
<p>Loving Grace Technologies, LLC<br>Grenada, Mississippi, United States</p>
</div>
</div></section>''',
)

P["privacy.html"] = (
    "Privacy | Loving Grace Technologies",
    "Privacy policy for the Loving Grace Technologies website.",
    f'''
<div class="page-head"><div class="wrap"><h1><span class="gold">Privacy</span> Policy</h1><p>Last updated November 12, 2026</p></div></div>
<section><div class="wrap prose">
<p>This policy covers the public Loving Grace Technologies website, run by Loving Grace Technologies, LLC and hosted on GitHub Pages.</p>
<h2>What We Collect</h2>
<p>This website has no advertising and no analytics or tracking cookies. We do not sell personal information.</p>
<p>The Discovery Scout page has an email-only waitlist. Joining opens an email to us, or you can email us directly. If you send that message, we receive the address you include and use it only to tell you about Discovery Scout. We do not ask for a password, payment card, government identification, or home address. This site does not run a separate signup database.</p>
<p>If you email us, we receive your email address and whatever you choose to include, and we use it only to reply to you and, if you asked to join the waitlist, to keep that request.</p>
<h2>Hosting and Embedded Content</h2>
<p>Our hosting provider may keep standard server logs, such as IP address and browser type, to deliver and secure the site. Fonts are served by Google Fonts. The Work page embeds a YouTube video in privacy-enhanced mode; YouTube&rsquo;s own privacy policy applies when you play it.</p>
<h2>Our Products</h2>
<p>Our products are designed to ask for a person&rsquo;s approval before sending, paying, or deleting anything. Product-specific privacy terms are provided to customers separately.</p>
<h2>Contact</h2>
<p>Questions about privacy: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></section>''',
)

P["discovery-scout.html"] = (
    "Discovery Scout | Loving Grace Technologies",
    "Plan legal outdoor hunts with Discovery Scout. It scores areas from commercially allowed open data and explains why. Waitlist only. Nothing to buy here.",
    scout_body(),
)

P["404.html"] = (
    "Page not found | Loving Grace Technologies",
    "Page not found.",
    '<div class="page-head"><div class="wrap"><h1>Page not found</h1><p>That page doesn&rsquo;t exist. <a style="color:var(--pearl)" href="index.html">Go to the home page</a>.</p></div></div>',
)

P["discovery-scout-plans.html"] = (
    "Discovery Scout plans | Loving Grace Technologies",
    "Discovery Scout plans and prices: Free, Done-for-you $19, Concierge planning $49, Scout $9 a month or $79 a year, Pro $19 a month or $149 a year. Planning software, not a travel agency.",
    plans_body(),
)
P["discovery-scout-terms.html"] = (
    "Discovery Scout terms and refunds | Loving Grace Technologies",
    "Terms of sale and refund policy for Discovery Scout by Loving Grace Technologies, LLC.",
    terms_body(),
)
P["discovery-scout-thanks.html"] = (
    "Thank you | Discovery Scout",
    "Thank you for your Discovery Scout order.",
    thanks_body(),
)
CHECKOUT_PAGES = ["discovery-scout-plans.html", "discovery-scout-terms.html", "discovery-scout-thanks.html"]

if CHECKOUT_OPEN:
    if not TERMS_APPROVED:
        raise SystemExit("CHECKOUT_OPEN needs TERMS_APPROVED = True (Bridgett's Go on the terms and refund wording)")
    if not any(SQUARE_LINKS.values()):
        raise SystemExit("CHECKOUT_OPEN needs at least one Square link in SQUARE_LINKS")
    # Live wiring: the waitlist page and Work page point to the plans page,
    # and the privacy page names Square as the payment processor.
    t, d, b = P["discovery-scout.html"]
    b = b.replace("<a href=\"#waitlist\">Join the waitlist</a>. Nothing on this page is for sale.",
                  "<a href=\"discovery-scout-plans.html\">See plans and prices</a> or <a href=\"#waitlist\">join the waitlist</a>.")
    b = b.replace('<p class="caption">Not offered for purchase here</p>\n<h2>Planned plans</h2>', '<p class="caption">Plans</p>\n<h2>Plans</h2>')
    b = b.replace("These are names for plans we expect to offer later. They are not offered for purchase on this page. There is no checkout and no payment.",
                  "Prices, what each plan includes, and checkout are on the <a href=\"discovery-scout-plans.html\">plans page</a>.")
    b = b.replace("Joining the waitlist is free. This page does not take payment.", "Joining the waitlist is free.")
    b = b.replace("Joining is free, and it is not a purchase.", "Joining is free.")
    b = b.replace("This page is the public waitlist. It is not a login, and it does not open the working product.", "This page is the public waitlist and plan overview.")
    b = b.replace('<p class="caption">Coming soon</p>', '<p class="caption">Plan</p>')
    P["discovery-scout.html"] = (t, d.replace(" Waitlist only. Nothing to buy here.", " See plans and prices."), b)
    t, d, b = P["privacy.html"]
    b = b.replace("<h2>Hosting and Embedded Content</h2>",
                  "<h2>Payments</h2>\n<p>Discovery Scout purchases are processed by Square on Square&rsquo;s own checkout page. We do not see or store your full card number. Square shares with us your name, email, what you bought, and payment status so we can deliver your plan. Square&rsquo;s privacy notice applies to the checkout.</p>\n<h2>Hosting and Embedded Content</h2>")
    b = b.replace(" We do not ask for a password, payment card, government identification, or home address.", " The waitlist does not ask for a password, payment card, government identification, or home address.")
    P["privacy.html"] = (t, d, b)
    for fn in ("index.html", "products.html"):
        t, d, b = P[fn]
        b = b.replace(" The public page is a waitlist, with nothing to buy.", " See plans and prices on the Discovery Scout page.")
        b = b.replace("<p>The public page is a waitlist. Planned plan names are described there as coming soon. Nothing is for sale on that page, and this site does not offer a trial login or a checkout.</p>",
                      "<p>Plans and prices are on the <a href=\"discovery-scout-plans.html\">plans page</a>. Payments go through Square.</p>")
        P[fn] = (t, d, b)

from pathlib import Path
_ds_ld = discovery_ld()
if CHECKOUT_OPEN:
    _ds_ld = (_ds_ld.replace(" Waitlist only. Nothing to buy here.", " Plans and prices are on the plans page.")
                    .replace(" This page is a waitlist. Planned plans are not for sale here.", " Plans are sold through Square on the plans page."))
EXTRA_LD = {"discovery-scout.html": _ds_ld}
for fn, (t, d, b) in P.items():
    head = ""
    if fn in CHECKOUT_PAGES:
        head = DS_CHECKOUT_HEAD + ("" if CHECKOUT_OPEN and fn != "discovery-scout-thanks.html" else DS_NOINDEX)
    Path(fn).write_text(page(fn, t, d, b, EXTRA_LD.get(fn, ""), head), encoding="utf-8")

# Sitemap of public pages (not the 404 page)
SITEMAP_PAGES = ["index.html", "services.html", "products.html", "discovery-scout.html", "about.html", "contact.html", "privacy.html"]
if CHECKOUT_OPEN:
    SITEMAP_PAGES += ["discovery-scout-plans.html", "discovery-scout-terms.html"]
urls = []
for fn in SITEMAP_PAGES:
    loc = SITE if fn == "index.html" else SITE + fn
    urls.append(f"  <url><loc>{loc}</loc></url>")
Path("sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "\n".join(urls)
    + "\n</urlset>\n",
    encoding="utf-8",
)
Path("robots.txt").write_text(
    "User-agent: *\nAllow: /\n\nSitemap: " + SITE + "sitemap.xml\n",
    encoding="utf-8",
)
print("wrote", ", ".join(P), "sitemap.xml, robots.txt")
