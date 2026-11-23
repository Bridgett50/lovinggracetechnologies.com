#!/usr/bin/env python3
"""Serve the Loving Grace site. Password-protect /lateral.

GitHub Pages cannot check a password. This process can. The membership page
is rendered here, after the password matches, so there is no lateral.html
for a static host to publish.

The password is the LATERAL_PASSWORD environment variable. Never put a
password in this file. This repository is public, so anyone who can read
the repository can read the page copy below. The check protects the URL
only when this server is the host.

Bind: 0.0.0.0 and the PORT environment variable (Render sets PORT).
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import mimetypes
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

ROOT = Path(__file__).resolve().parent
EMAIL = "bridgettsanders50@lovinggracetechnologies.com"
SESSION_MSG = b"lateral-session-v1"
COOKIE = "lateral_session"
MAX_BODY = 8192
MAX_PASSWORD = 1024

mimetypes.add_type("image/webp", ".webp")
mimetypes.add_type("image/x-icon", ".ico")
mimetypes.add_type("text/plain", ".txt")

ALLOWED_SUFFIXES = {
    ".html", ".css", ".js", ".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg",
    ".ico", ".xml", ".txt", ".webmanifest", ".json", ".pdf", ".woff", ".woff2",
}


def configured_password() -> str:
    """Return the host password, or empty when the section must stay closed."""
    return os.environ.get("LATERAL_PASSWORD", "").strip()


def passwords_match(provided: str, expected: str) -> bool:
    if not expected:
        return False
    provided = provided[:MAX_PASSWORD]
    actual = hashlib.sha256(provided.encode("utf-8")).digest()
    wanted = hashlib.sha256(expected.encode("utf-8")).digest()
    return hmac.compare_digest(actual, wanted)


def session_token(password: str) -> str:
    return hmac.new(password.encode("utf-8"), SESSION_MSG, hashlib.sha256).hexdigest()


def cookie_matches(header: str | None, password: str) -> bool:
    if not password or not header:
        return False
    token = ""
    for part in header.split(";"):
        part = part.strip()
        if part.startswith(COOKIE + "="):
            token = part.split("=", 1)[1].strip()
    if not token:
        return False
    return hmac.compare_digest(token, session_token(password))


def basic_password(header: str | None) -> str | None:
    """Return the Basic-auth password, or None when the header is absent."""
    if not header:
        return None
    scheme, _, rest = header.partition(" ")
    if scheme.lower() != "basic" or not rest:
        return ""
    try:
        decoded = base64.b64decode(rest.strip(), validate=True).decode("utf-8")
    except (ValueError, UnicodeDecodeError):
        return ""
    if ":" not in decoded:
        return ""
    return decoded.split(":", 1)[1][:MAX_PASSWORD]


def request_path(raw: str) -> str:
    path = unquote(urlsplit(raw).path or "/")
    if path != "/" and path.endswith("/"):
        path = path[:-1] or "/"
    return path


def is_lateral(path: str) -> bool:
    return path == "/lateral" or path == "/lateral.html" or path.startswith("/lateral/")


def cookie_header(token: str, max_age: int, secure: bool) -> str:
    parts = [
        f"{COOKIE}={token}",
        "HttpOnly",
        "SameSite=Lax",
        "Path=/",
        f"Max-Age={max_age}",
    ]
    if secure:
        parts.append("Secure")
    return "; ".join(parts)


def layout(title: str, description: str, body: str) -> str:
    nav = "".join(
        f'<li><a href="{href}">{label}</a></li>'
        for href, label in (
            ("index.html", "Home"),
            ("services.html", "Services"),
            ("products.html", "Work"),
            ("articles.html", "Articles"),
            ("research.html", "Research"),
            ("about.html", "About"),
            ("contact.html", "Contact"),
        )
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="googlebot" content="noindex, nofollow">
<meta name="referrer" content="no-referrer">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#CDCED6">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" href="assets/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com" referrerpolicy="no-referrer">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin referrerpolicy="no-referrer">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@500;600&family=Montserrat:wght@500&family=Quicksand:wght@600&display=swap" rel="stylesheet" referrerpolicy="no-referrer">
<link rel="stylesheet" href="assets/style.css?v=20261123-review">
<style>
.sr{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}}
.gate{{max-width:32rem}}
</style>
<script src="assets/navigation.js?v=20261122-lateral" defer></script>
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
<header class="site"><div class="wrap">
<a class="brand" href="index.html" aria-label="Loving Grace Technologies home"><picture><source srcset="assets/logo-horizontal.webp" type="image/webp"><img src="assets/logo-horizontal.jpg" alt="Loving Grace Technologies" width="900" height="309"></picture></a>
<button class="nav-toggle" type="button" aria-controls="site-navigation" aria-expanded="false" hidden>Menu</button>
<nav id="site-navigation" aria-label="Main"><ul>{nav}</ul></nav>
</div></header>
<main id="content">
{body}
</main>
<footer class="site"><div class="wrap">
<div>
<div class="wordmark" aria-label="Loving Grace Technologies"><span class="loving">Loving</span> <span class="grace">Grace</span><small>TECHNOLOGIES</small></div>
<p class="sig">Sacred by design. Powered by innovation. Guided by grace.</p>
<p class="sig" style="font-size:14px;margin-top:10px;max-width:28rem">Named for a simple idea: machines should watch over people with grace, and people should remain in charge.</p>
</div>
<div>
<nav aria-label="Footer"><a href="services.html">Services</a><a href="products.html">Work</a><a href="articles.html">Articles</a><a href="research.html">Research</a><a href="discovery-scout.html">Discovery Scout</a><a href="about.html">About</a><a href="contact.html">Contact</a><a href="assets/Loving-Grace-Technologies-Capability-Statement.pdf" download="Loving-Grace-Technologies-Capability-Statement.pdf">Download Capability Statement (PDF)</a><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a><a href="refund-policy.html">Refunds</a></nav>
<nav aria-label="Follow"><a href="https://www.facebook.com/profile.php?id=61596476147014" rel="noopener noreferrer">Facebook</a><a href="https://www.linkedin.com/company/lovinggracetech/" rel="noopener noreferrer">LinkedIn</a><a href="https://www.youtube.com/channel/UCUEiHKR74F2YdL1z71B6aQQ" rel="noopener noreferrer">YouTube</a></nav>
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


def gate_page(closed: bool, rejected: bool) -> str:
    if closed:
        message = "<p>This section is closed until its password is set on the host.</p>"
        form = ""
    else:
        alert = ""
        if rejected:
            alert = '<p class="joined" role="alert">That password was not recognized.</p>'
        message = "<p>Enter the password to continue. This address is not linked from the public site.</p>"
        form = f"""{alert}
<form class="contact-form" method="post" action="/lateral" autocomplete="on">
<div class="sr">
<label for="lateral-user">Section</label>
<input id="lateral-user" name="username" type="text" autocomplete="username" value="LATERAL" readonly>
</div>
<div class="field">
<label for="lateral-password">Password</label>
<input id="lateral-password" name="password" type="password" autocomplete="current-password" autocapitalize="off" spellcheck="false" maxlength="500" required autofocus>
</div>
<button class="btn primary" type="submit">Continue</button>
</form>"""
    body = f"""
<div class="page-head"><div class="wrap">
<p class="caption" style="color:var(--gold-1)">Private</p>
<h1><span class="gold">LATERAL</span></h1>
<p>Loving Grace Technologies</p>
</div></div>
<section><div class="wrap">
<div class="card gate">
{message}
{form}
</div>
</div></section>"""
    return layout(
        "Private section | Loving Grace Technologies",
        "Private section. A password is required.",
        body,
    )


def membership_page() -> str:
    """Teaser only. This file is in a public repository, so it does not describe how LATERAL works."""
    body = f"""
<div class="page-head"><div class="wrap">
<p class="caption" style="color:var(--gold-1)">Private draft</p>
<h1><span class="gold">LATERAL</span> by Loving Grace</h1>
<p>The power to leave, on your own terms, without stepping down.</p>
</div></div>
<section class="band" style="padding:40px 0" aria-labelledby="not-insurance">
<div class="wrap">
<p class="caption" style="color:var(--gold-1)">Read this first</p>
<h2 id="not-insurance">LATERAL is not insurance</h2>
<p>Coverage is not yet offered. This page is a private draft. It is not a policy, it does not promise a payment or a payout, and there is nothing to buy here.</p>
</div>
</section>
<section class="approach"><div class="wrap prose">
<p class="caption">LATERAL</p>
<h2>Move forward, without stepping down</h2>
<div class="rule"></div>
<p class="lead">LATERAL is protection that helps you move forward without stepping down when life changes suddenly. It is private and white-glove.</p>
</div></section>
<section class="approach" id="interest" aria-labelledby="interest-title"><div class="wrap">
<h2 id="interest-title">Register interest</h2>
<div class="rule"></div>
<div class="card waitlist">
<p id="interest-sent" class="joined" tabindex="-1" role="status" hidden>Your email app should open with the note filled in. Send that message to finish. This is not a purchase. If no email app opens, use the link under the form.</p>
<p id="interest-help">Leave a note if you want to hear when LATERAL opens. This is a waitlist. It is free. It is not an application for coverage, and it is not a payment. Loving Grace Technologies will use what you send only to reply about LATERAL.</p>
<form class="contact-form" id="lateral-interest" action="mailto:{EMAIL}?subject=LATERAL%20interest" method="post" enctype="text/plain">
<div class="field">
<label for="interest-name">Name</label>
<input id="interest-name" name="name" type="text" autocomplete="name" maxlength="100" required>
</div>
<div class="field">
<label for="interest-email">Email</label>
<input id="interest-email" name="email" type="email" autocomplete="email" inputmode="email" autocapitalize="none" spellcheck="false" maxlength="254" required aria-describedby="interest-help">
</div>
<div class="field">
<label for="interest-note">Note</label>
<textarea id="interest-note" name="note" rows="5" maxlength="2000" placeholder="Optional."></textarea>
</div>
<button class="btn primary" type="submit">Register interest</button>
</form>
<p class="hint">If the form does not open an email app, email <a href="mailto:{EMAIL}?subject=LATERAL%20interest">{EMAIL}</a> with the subject &ldquo;LATERAL interest&rdquo;. No payment is taken.</p>
<form method="post" action="/lateral/logout" style="margin-top:22px">
<button class="btn secondary" type="submit">Lock this section</button>
</form>
</div>
<script>
(function () {{
  var form = document.getElementById("lateral-interest");
  if (!form) return;
  form.addEventListener("submit", function (event) {{
    event.preventDefault();
    if (!form.reportValidity()) return;
    var name = document.getElementById("interest-name").value.trim();
    var email = document.getElementById("interest-email").value.trim();
    var note = document.getElementById("interest-note").value.trim();
    var body = "LATERAL interest. This is not a purchase and not a request for coverage.\\n\\nName: " + name + "\\nEmail: " + email + "\\nNote: " + note;
    var status = document.getElementById("interest-sent");
    if (status) {{ status.hidden = false; status.focus(); }}
    window.location.href = "mailto:{EMAIL}?subject=" + encodeURIComponent("LATERAL interest") + "&body=" + encodeURIComponent(body);
  }});
}})();
</script>
</div></section>"""
    return layout(
        "LATERAL by Loving Grace",
        "Private draft of LATERAL by Loving Grace. Protection that helps you move forward without stepping down when life changes suddenly. Not insurance. Coverage is not offered. Nothing on this page is for sale.",
        body,
    )


class Handler(BaseHTTPRequestHandler):
    server_version = "LovingGrace"
    sys_version = ""

    def log_message(self, fmt: str, *args) -> None:
        # Request line only. The password is never accepted on the query string.
        super().log_message(fmt, *args)

    def _secure(self) -> bool:
        proto = (self.headers.get("X-Forwarded-Proto") or "").split(",")[0].strip().lower()
        if proto == "https":
            return True
        return (self.headers.get("X-Forwarded-Ssl") or "").lower() == "on"

    def _authorized(self, password: str) -> bool:
        if not password:
            return False
        basic = basic_password(self.headers.get("Authorization"))
        if basic is not None and passwords_match(basic, password):
            return True
        return cookie_matches(self.headers.get("Cookie"), password)

    def _send_bytes(self, status: int, body: bytes, content_type: str, extra: list[tuple[str, str]] | None = None) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        for key, value in extra or []:
            self.send_header(key, value)
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _send_html(self, status: int, html: str, set_cookie: str | None = None) -> None:
        extra = [
            ("Cache-Control", "private, no-store"),
            ("X-Robots-Tag", "noindex, nofollow"),
            ("Referrer-Policy", "no-referrer"),
        ]
        if set_cookie:
            extra.append(("Set-Cookie", set_cookie))
        self._send_bytes(status, html.encode("utf-8"), "text/html; charset=utf-8", extra)

    def _content_length(self) -> int:
        raw = self.headers.get("Content-Length") or "0"
        try:
            length = int(raw)
        except ValueError:
            return -1
        return length

    def _read_form(self) -> dict[str, list[str]]:
        length = self._content_length()
        if length < 0 or length > MAX_BODY:
            return {}
        raw = self.rfile.read(length).decode("utf-8", "replace") if length else ""
        return parse_qs(raw, keep_blank_values=True)

    def _posted_password(self) -> str:
        fields = self._read_form()
        values = fields.get("password") or [""]
        return values[0][:MAX_PASSWORD]

    def _gate(self, closed: bool, rejected: bool) -> None:
        self._send_html(503 if closed else 401, gate_page(closed, rejected))

    def _serve_lateral_get(self) -> None:
        password = configured_password()
        if not password:
            self._gate(True, False)
            return
        if self._authorized(password):
            self._send_html(200, membership_page())
            return
        self._gate(False, False)

    def _serve_login(self) -> None:
        password = configured_password()
        if not password:
            self._read_form()
            self._gate(True, False)
            return
        if passwords_match(self._posted_password(), password):
            self.send_response(303)
            self.send_header("Location", "/lateral")
            self.send_header("Content-Length", "0")
            self.send_header("Cache-Control", "private, no-store")
            self.send_header("X-Robots-Tag", "noindex, nofollow")
            self.send_header("Set-Cookie", cookie_header(session_token(password), 1209600, self._secure()))
            self.end_headers()
            return
        self._gate(False, True)

    def _serve_logout(self) -> None:
        # Discard any posted body so the connection stays in a known state.
        length = self._content_length()
        if 0 < length <= MAX_BODY:
            self.rfile.read(length)
        self.send_response(303)
        self.send_header("Location", "/lateral")
        self.send_header("Content-Length", "0")
        self.send_header("Cache-Control", "private, no-store")
        self.send_header("Set-Cookie", cookie_header("", 0, self._secure()))
        self.end_headers()

    def do_HEAD(self) -> None:
        self.do_GET()

    def do_GET(self) -> None:
        path = request_path(self.path)
        if path == "/healthz":
            self._send_bytes(200, b"ok\n", "text/plain; charset=utf-8", [("Cache-Control", "no-store")])
            return
        if is_lateral(path):
            self._serve_lateral_get()
            return
        self._serve_static(path)

    def do_POST(self) -> None:
        path = request_path(self.path)
        if path == "/lateral/logout":
            self._serve_logout()
            return
        if path == "/lateral":
            self._serve_login()
            return
        self.send_error(405)

    def _static_file(self, path: str) -> Path | None:
        rel = path.lstrip("/")
        if not rel:
            rel = "index.html"
        if any(part.startswith(".") for part in Path(rel).parts):
            return None
        candidate = (ROOT / rel).resolve()
        try:
            candidate.relative_to(ROOT)
        except ValueError:
            return None
        if candidate.is_dir():
            candidate = (candidate / "index.html").resolve()
        if candidate.suffix == "" and not candidate.is_file():
            html = candidate.with_suffix(".html")
            if html.is_file():
                candidate = html
        if not candidate.is_file():
            return None
        if candidate.suffix.lower() not in ALLOWED_SUFFIXES:
            return None
        if candidate.name.startswith("."):
            return None
        return candidate

    def _serve_static(self, path: str) -> None:
        target = self._static_file(path)
        status = 200
        if target is None:
            target = ROOT / "404.html"
            status = 404
            if not target.is_file():
                self._send_bytes(404, b"Not found\n", "text/plain; charset=utf-8")
                return
        data = target.read_bytes()
        content_type = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        if content_type.startswith("text/") or content_type in {"application/javascript", "image/svg+xml", "application/json"}:
            content_type += "; charset=utf-8"
        self._send_bytes(status, data, content_type)

    def send_error(self, code: int, message: str | None = None, explain: str | None = None) -> None:
        body = (message or "Error").encode("utf-8")
        self._send_bytes(code, body, "text/plain; charset=utf-8")


def main() -> None:
    port = int(os.environ.get("PORT", "8000"))
    server = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    print(f"listening on 0.0.0.0:{port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
