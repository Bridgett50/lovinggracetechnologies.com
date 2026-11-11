# Generates the static pages. Run: python3 build.py
EMAIL="bridgettsanders50@lovinggracetechnologies.com"
SITE="https://lovinggracetechnologies.com/"
NAV=[("index.html","Home"),("products.html","Products"),("about.html","About"),("contact.html","Contact")]
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@500;600&family=Montserrat:wght@500&family=Sora:wght@500&display=swap" rel="stylesheet">'
ICONS={
 "agent":'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><path d="M12 10.6v2.8M10.6 12h2.8"/></svg>',
 "seat":'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="5" width="17" height="11" rx="2"/><path d="M9 20h6M12 16v4"/><path d="M8.5 11.2l2.2 2 4.8-4.6"/></svg>',
 "music":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 18V6l10-2v12"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="16.5" cy="16" r="2.5"/></svg>',
 "heart":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg>',
 "scale":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v16M7 20h10M5 7h14"/><path d="M5 7l-2.5 6a3 3 0 0 0 5 0L5 7zM19 7l-2.5 6a3 3 0 0 0 5 0L19 7z"/></svg>',
 "key":'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="8" cy="12" r="3.5"/><path d="M11.5 12H21M18 12v3M15 12v2"/></svg>',
 "spark":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v5M12 16v5M3 12h5M16 12h5M6 6l3 3M15 15l3 3M18 6l-3 3M9 15l-3 3"/></svg>',
}
def ic(k): return f'<div class="icon">{ICONS[k]}</div>'
def page(fn,title,desc,body):
    nav="".join(f'<li><a href="{h}"{" aria-current=page" if h==fn else ""}>{t}</a></li>' for h,t in NAV)
    return f'''<!doctype html>
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
<meta property="og:image" content="{SITE}assets/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" href="assets/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="assets/style.css?v=20261110d">
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
</div>
<div>
<nav aria-label="Footer"><a href="products.html">Products</a><a href="about.html">About</a><a href="contact.html">Contact</a><a href="privacy.html">Privacy</a></nav>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p>Grenada, Mississippi</p>
</div>
<div class="foot-bottom">
<p class="motto">Technology with purpose<span>&bull;</span>Intelligence with compassion<span>&bull;</span>Innovation with integrity</p>
<p>&copy; 2026 Loving Grace Technologies, LLC</p>
</div>
</div></footer>
</body>
</html>
'''
P={}
P["index.html"]=("Loving Grace Technologies | Conscious Systems. Human Futures.","Loving Grace Technologies: where consciousness meets technology. A self-hosted AI assistant, an AI meeting twin, and AI music and studio tools, built with human approval at the center.",f'''
<section class="hero" aria-labelledby="hero-title" style="padding:0"><div class="wrap">
<div class="divider" aria-hidden="true"></div>
<div class="copy">
<h1 id="hero-title"><span class="gold">Conscious Systems.</span><span class="l2">Human Futures.</span></h1>
<p class="tagline">Where <em>Consciousness</em> Meets <em>Technology</em>.</p>
<ul class="pillars"><li>Research</li><li>Innovation</li><li>Ethical Intelligence</li></ul>
<p class="hero-lead">We build technologies that protect consciousness and expand human potential.</p>
<div class="btns"><a class="btn primary" href="products.html">Explore our products</a><a class="btn secondary" href="contact.html">Get in touch</a></div>
</div>
<div class="art"><picture><source srcset="assets/hero-art.webp" type="image/webp"><img src="assets/hero-art.jpg" alt="" width="675" height="819"></picture></div>
</div></section>

<section class="approach"><div class="wrap">
<h2>What We Build</h2><div class="rule"></div>
<p class="lead">Human-centered deep tech: three product lines built on one principle. Our technology does real work, and people stay in charge of every decision that matters.</p>
<div class="grid">
<div class="card">{ic("agent")}<h3>Loving Grace Agent</h3><p>A self-hosted AI assistant with memory, skills, and computer use. It always asks before sending, paying, or deleting.</p><hr><a class="more" href="products.html#agent">Learn more</a></div>
<div class="card">{ic("seat")}<h3>Second Seat</h3><p>An AI meeting twin that captures what was agreed, drafts the follow-up work, and waits for human approval.</p><hr><a class="more" href="products.html#second-seat">Watch the demo</a></div>
<div class="card">{ic("music")}<h3>AI Music &amp; Studio Tools</h3><p>AI music and studio tools for blues and soul recordings, made to support the artist&rsquo;s own voice.</p><hr><a class="more" href="products.html#music">Learn more</a></div>
</div>
</div></section>

<section class="textured-tile approach"><div class="wrap">
<h2>Our Approach</h2><div class="rule"></div>
<p class="lead">Rigorous inquiry, compassionate design. We work at the intersection of consciousness and technology with elegance, integrity, and precision.</p>
<div class="grid">
<div class="card">{ic("scale")}<h3>Ethical Intelligence</h3><p>Our tools draft and prepare. A person approves anything that is sent, paid, or deleted.</p></div>
<div class="card">{ic("key")}<h3>Luminous Intelligence</h3><p>Clear, grounded AI that explains its work. Self-hosted options keep files and memory on infrastructure you control.</p></div>
<div class="card">{ic("heart")}<h3>Human-Centered Innovation</h3><p>Refined, practical tools that small businesses, creators, and researchers can run and trust.</p></div>
</div>
</div></section>

<section class="band"><div class="wrap">
<h2>Scientific Rigor. Human Wisdom. Conscious Future.</h2>
<p>Engineering a more conscious world, together. Partnerships, pilots, research, and government collaboration are welcome.</p>
<a class="btn primary" href="mailto:{EMAIL}">Email us</a>
</div></section>''')
P["products.html"]=("Products | Loving Grace Technologies","The Loving Grace Agent, Second Seat, and AI music and studio tools from Loving Grace Technologies.",f'''
<div class="page-head"><div class="wrap"><h1><span class="gold">Our</span> Products</h1><p>Human-centered deep tech that takes on real work and keeps a person in the loop.</p></div></div>
<section class="approach"><div class="wrap">
<article class="card product" id="agent">{ic("agent")}
<span class="caption">Self-hosted AI assistant</span>
<h2>Loving Grace Agent</h2>
<p>The Loving Grace Agent runs on your own server. It remembers context, learns new skills, and can use a computer to get tasks done.</p>
<ul><li>Memory that carries context across conversations</li><li>Skills it can add and reuse for repeat work</li><li>Computer use for browser and desktop tasks</li><li>Always asks before sending, paying, or deleting</li></ul>
</article>
<article class="card product" id="second-seat">{ic("seat")}
<span class="caption">AI meeting twin</span>
<h2>Second Seat</h2>
<p>Second Seat sits in on meetings, captures what was agreed, and drafts the follow-up work. Nothing goes out until a person reviews and approves it.</p>
<ul><li>Turns meeting decisions into draft tasks and messages</li><li>Human approval before any action is taken</li></ul>
<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/1VJKjwJzRN0" title="Second Seat demo" loading="lazy" allow="accelerometer; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<p style="margin-top:12px"><a href="https://youtu.be/1VJKjwJzRN0">Watch the Second Seat demo on YouTube</a></p>
</article>
<article class="card product" id="music">{ic("music")}
<span class="caption">For blues and soul recordings</span>
<h2>AI Music &amp; Studio Tools</h2>
<p>Tools that help artists and producers work with their recordings, including stem separation, editing, and AI-assisted music creation. Built to support the artist&rsquo;s voice, and used only with the artist&rsquo;s permission.</p>
</article>
</div></section>''')
P["about.html"]=("About | Loving Grace Technologies","About Loving Grace Technologies, LLC, a technology company in Grenada, Mississippi founded by Bridgett Sanders.",'''
<div class="page-head"><div class="wrap"><h1><span class="gold">About</span> Loving Grace</h1><p>Where Consciousness Meets Technology.</p></div></div>
<section><div class="wrap prose">
<div class="wordmark-banner"><picture><source srcset="assets/logo-primary-stacked.webp" type="image/webp"><img src="assets/logo-primary-stacked.jpg" alt="Loving Grace Technologies logo" width="900" height="788"></picture></div>
<p>Loving Grace Technologies, LLC is a technology company based in Grenada, Mississippi. We work at the intersection of consciousness and technology: sacred by design, scientific in method, and humane in every decision. We build technologies that protect consciousness and expand human potential.</p>
<p>The company was founded in 2026 by <strong>Bridgett Sanders</strong>, who leads product and engineering. Our work spans personal AI assistants, meeting automation, and creative tools for musicians, guided by rigorous inquiry and compassionate design.</p>
<h2>Company Information</h2><div class="rule"></div>
<div class="card"><dl class="facts">
<dt>Legal name</dt><dd>Loving Grace Technologies, LLC</dd>
<dt>Location</dt><dd>Grenada, Mississippi, United States</dd>
<dt>Founder</dt><dd>Bridgett Sanders</dd>
<dt>SAM.gov</dt><dd>Active registration</dd>
<dt>UEI</dt><dd>U5D5QT7QLRQ5</dd>
<dt>CAGE code</dt><dd>222V5</dd>
</dl></div>
</div></section>''')
P["contact.html"]=("Contact | Loving Grace Technologies","Contact Loving Grace Technologies.",f'''
<div class="page-head"><div class="wrap"><h1><span class="gold">Contact</span> Us</h1><p>We&rsquo;d love to hear from you.</p></div></div>
<section><div class="wrap prose">
<div class="card">
<p>For partnerships, pilots, press, or government and research collaboration, email us and we&rsquo;ll get back to you.</p>
<p style="margin:22px 0"><a class="btn primary" href="mailto:{EMAIL}">{EMAIL}</a></p>
<p>Loving Grace Technologies, LLC<br>Grenada, Mississippi, United States</p>
</div>
</div></section>''')
P["privacy.html"]=("Privacy | Loving Grace Technologies","Privacy policy for the Loving Grace Technologies website.",f'''
<div class="page-head"><div class="wrap"><h1><span class="gold">Privacy</span> Policy</h1><p>Last updated November 10, 2026</p></div></div>
<section><div class="wrap prose">
<p>This policy covers the website lovinggracetechnologies.com, run by Loving Grace Technologies, LLC.</p>
<h2>What We Collect</h2>
<p>This website has no sign-up forms, no advertising, and no analytics or tracking cookies. We do not sell personal information.</p>
<p>If you email us, we receive your email address and whatever you choose to include, and we use it only to reply to you.</p>
<h2>Hosting and Embedded Content</h2>
<p>Our hosting provider may keep standard server logs, such as IP address and browser type, to deliver and secure the site. Fonts are served by Google Fonts. The Products page embeds a YouTube video in privacy-enhanced mode; YouTube&rsquo;s own privacy policy applies when you play it.</p>
<h2>Our Products</h2>
<p>Our products are designed to ask for a person&rsquo;s approval before sending, paying, or deleting anything. Product-specific privacy terms are provided to customers separately.</p>
<h2>Contact</h2>
<p>Questions about privacy: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></section>''')
P["404.html"]=("Page not found | Loving Grace Technologies","Page not found.",'<div class="page-head"><div class="wrap"><h1>Page not found</h1><p>That page doesn&rsquo;t exist. <a style="color:var(--pearl)" href="index.html">Go to the home page</a>.</p></div></div>')
for fn,(t,d,b) in P.items(): open(fn,"w").write(page(fn,t,d,b))
