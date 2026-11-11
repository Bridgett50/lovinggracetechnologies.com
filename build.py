# Generates the static pages. Run: python3 build.py
EMAIL = "bridgettsanders50@lovinggracetechnologies.com"
# Canonical site is the custom domain. Apex A records point at GitHub Pages.
# www is not in DNS yet (Squarespace could not save that CNAME).
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
CSS_V = "20261110h"
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
}

def ic(k):
    return f'<div class="icon">{ICONS[k]}</div>'

def ldjson():
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Loving Grace Technologies, LLC",
        "legalName": "Loving Grace Technologies, LLC",
        "url": SITE,
        "email": EMAIL,
        "description": "Human-centered technology for government and commercial teams: workflow and AI automation, systems planning, websites, training, research, and small business consulting.",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Grenada",
            "addressRegion": "MS",
            "addressCountry": "US",
        },
        "areaServed": "US",
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
<nav aria-label="Footer"><a href="services.html">Services</a><a href="products.html">Work</a><a href="about.html">About</a><a href="contact.html">Contact</a><a href="privacy.html">Privacy</a></nav>
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

def page(fn, title, desc, body):
    nav = "".join(
        f'<li><a href="{h}"{" aria-current=page" if h == fn else ""}>{t}</a></li>'
        for h, t in NAV
    )
    path = "" if fn == "index.html" else fn
    return PAGE_TMPL.format(
        title=title, desc=desc, url=SITE + path, site=SITE,
        fonts=FONTS, css_v=CSS_V, ld=ldjson(), nav=nav, body=body, email=EMAIL,
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
<div class="card">{ic("agent")}<h3>Loving Grace Agent</h3><p>A self-hosted AI assistant with memory, skills, and computer use. It always asks before sending, paying, or deleting.</p><hr><a class="more" href="products.html#agent">Learn more</a></div>
<div class="card">{ic("seat")}<h3>Second Seat</h3><p>It turns what a small-business owner agrees to in a meeting into PayPal payments. AI drafts each payment, then a separate checker compares it against the owner&rsquo;s own words and blocks anything that doesn&rsquo;t match, like a changed bank account or an inflated amount. Nothing is paid until the owner approves it with one tap, and every payment keeps the quote it came from as its receipt.</p><hr><a class="more" href="https://youtu.be/1VJKjwJzRN0">Watch the demo</a></div>
<div class="card">{ic("music")}<h3>AI Music &amp; Studio Tools</h3><p>AI music and studio tools for blues and soul recordings, made to support the artist&rsquo;s own voice.</p><hr><a class="more" href="products.html#music">Learn more</a></div>
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
    "Products and selected projects from Loving Grace Technologies, including Second Seat, packout software, and website builds.",
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
<div class="page-head"><div class="wrap"><h1><span class="gold">Privacy</span> Policy</h1><p>Last updated November 10, 2026</p></div></div>
<section><div class="wrap prose">
<p>This policy covers the public Loving Grace Technologies website, run by Loving Grace Technologies, LLC and hosted on GitHub Pages.</p>
<h2>What We Collect</h2>
<p>This website has no sign-up forms, no advertising, and no analytics or tracking cookies. We do not sell personal information.</p>
<p>If you email us, we receive your email address and whatever you choose to include, and we use it only to reply to you.</p>
<h2>Hosting and Embedded Content</h2>
<p>Our hosting provider may keep standard server logs, such as IP address and browser type, to deliver and secure the site. Fonts are served by Google Fonts. The Work page embeds a YouTube video in privacy-enhanced mode; YouTube&rsquo;s own privacy policy applies when you play it.</p>
<h2>Our Products</h2>
<p>Our products are designed to ask for a person&rsquo;s approval before sending, paying, or deleting anything. Product-specific privacy terms are provided to customers separately.</p>
<h2>Contact</h2>
<p>Questions about privacy: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></section>''',
)

P["404.html"] = (
    "Page not found | Loving Grace Technologies",
    "Page not found.",
    '<div class="page-head"><div class="wrap"><h1>Page not found</h1><p>That page doesn&rsquo;t exist. <a style="color:var(--pearl)" href="index.html">Go to the home page</a>.</p></div></div>',
)

from pathlib import Path
for fn, (t, d, b) in P.items():
    Path(fn).write_text(page(fn, t, d, b), encoding="utf-8")

# Sitemap of public pages (not the 404 page)
SITEMAP_PAGES = ["index.html", "services.html", "products.html", "about.html", "contact.html", "privacy.html"]
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
