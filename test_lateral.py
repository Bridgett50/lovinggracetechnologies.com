"""Server-side checks for the private LATERAL section.

The password used here is a test value. It is not the site password.
Production reads LATERAL_PASSWORD from the environment and this file
must never contain that value.
"""

from __future__ import annotations

import os
import threading
import unittest
import urllib.error
import urllib.request
from pathlib import Path

import serve

ROOT = Path(__file__).resolve().parent
TEST_PASSWORD = "test-password-not-real"


def fetch(port, path, method="GET", data=None, headers=None, opener=None):
    url = f"http://127.0.0.1:{port}{path}"
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    open_fn = opener.open if opener else urllib.request.urlopen
    try:
        with open_fn(req, timeout=5) as resp:
            return resp.status, dict(resp.headers), resp.read()
    except urllib.error.HTTPError as err:
        return err.code, dict(err.headers), err.read()


class LateralServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ["LATERAL_PASSWORD"] = TEST_PASSWORD
        cls.httpd = serve.ThreadingHTTPServer(("127.0.0.1", 0), serve.Handler)
        cls.port = cls.httpd.server_address[1]
        cls.thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def setUp(self):
        os.environ["LATERAL_PASSWORD"] = TEST_PASSWORD

    def test_gate_hides_the_teaser(self):
        status, headers, body = fetch(self.port, "/lateral")
        text = body.decode()
        self.assertEqual(status, 401)
        self.assertIn("noindex", text)
        self.assertIn('type="password"', text)
        self.assertEqual(headers.get("X-Robots-Tag"), "noindex, nofollow")
        self.assertIn("private", headers.get("Cache-Control", ""))
        self.assertNotIn("The power to leave", text)
        self.assertNotIn("not insurance", text.lower())
        self.assertNotIn("$", text)
        self.assertNotIn("<select", text)

    def test_wrong_password_does_not_open_or_set_a_cookie(self):
        status, headers, body = fetch(
            self.port,
            "/lateral",
            method="POST",
            data=b"password=nope",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        text = body.decode()
        self.assertEqual(status, 401)
        self.assertIn("not recognized", text)
        self.assertNotIn("The power to leave", text)
        self.assertNotIn("Set-Cookie", headers)

    def test_correct_password_sets_a_session_and_shows_the_teaser(self):
        import http.client

        conn = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        conn.request(
            "POST",
            "/lateral",
            f"password={TEST_PASSWORD}",
            {"Content-Type": "application/x-www-form-urlencoded"},
        )
        posted = conn.getresponse()
        posted.read()
        self.assertEqual(posted.status, 303)
        self.assertEqual(posted.getheader("Location"), "/lateral")
        cookie = posted.getheader("Set-Cookie")
        self.assertIn("HttpOnly", cookie)
        self.assertIn(f"{serve.COOKIE}=", cookie)
        conn.request("GET", "/lateral", headers={"Cookie": cookie.split(";", 1)[0]})
        opened = conn.getresponse()
        page = opened.read().decode()
        self.assertEqual(opened.status, 200)
        self.assertIn("LATERAL by Loving Grace", page)
        self.assertIn("The power to leave, on your own terms, without stepping down.", page)
        self.assertIn("protection that helps you move forward without stepping down when life changes suddenly", page)
        self.assertIn("LATERAL is not insurance", page)
        self.assertIn("Coverage is not yet offered", page)
        self.assertIn("Register interest", page)
        self.assertIn("mailto:", page)
        self.assertIn('content="noindex, nofollow"', page)
        self.assertNotIn("$", page)
        self.assertNotIn("<select", page)
        self.assertNotIn("formsubmit", page.lower())
        self.assertNotIn("square.link", page.lower())
        self.assertNotIn("checkout", page.lower())
        self.assertNotIn("Sovereign", page)
        self.assertNotIn("budget", page.lower())
        conn.close()

    def test_basic_auth_opens_the_page(self):
        token = __import__("base64").b64encode(b"lateral:" + TEST_PASSWORD.encode()).decode()
        status, _, body = fetch(self.port, "/lateral", headers={"Authorization": f"Basic {token}"})
        self.assertEqual(status, 200)
        self.assertIn("The power to leave", body.decode())

    def test_logout_locks_the_section_again(self):
        import http.client

        conn = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        conn.request(
            "POST",
            "/lateral",
            f"password={TEST_PASSWORD}",
            {"Content-Type": "application/x-www-form-urlencoded"},
        )
        posted = conn.getresponse()
        posted.read()
        cookie = posted.getheader("Set-Cookie").split(";", 1)[0]
        conn.request("POST", "/lateral/logout", headers={"Cookie": cookie})
        locked = conn.getresponse()
        body = locked.read().decode()
        # 303, then the next GET is the gate.
        self.assertEqual(locked.status, 303)
        conn.request("GET", "/lateral", headers={"Cookie": locked.getheader("Set-Cookie").split(";", 1)[0]})
        follow = conn.getresponse()
        text = follow.read().decode()
        conn.close()
        self.assertEqual(follow.status, 401)
        self.assertNotIn("The power to leave", text)
        self.assertNotIn("The power to leave", body)

    def test_unset_password_stays_closed_with_no_copy(self):
        os.environ["LATERAL_PASSWORD"] = "   "
        try:
            status, _, body = fetch(self.port, "/lateral/")
            text = body.decode()
            self.assertEqual(status, 503)
            self.assertIn("closed", text.lower())
            self.assertNotIn("The power to leave", text)
            self.assertNotIn('type="password"', text)
            status, _, body = fetch(
                self.port,
                "/lateral",
                method="POST",
                data=f"password={TEST_PASSWORD}".encode(),
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            self.assertEqual(status, 503)
            self.assertNotIn("The power to leave", body.decode())
        finally:
            os.environ["LATERAL_PASSWORD"] = TEST_PASSWORD

    def test_public_pages_are_served_unchanged_and_server_source_is_not(self):
        status, _, body = fetch(self.port, "/")
        self.assertEqual(status, 200)
        self.assertEqual(body, (ROOT / "index.html").read_bytes())
        status, _, body = fetch(self.port, "/services")
        self.assertEqual(status, 200)
        self.assertIn(b"Services", body)
        self.assertEqual(body, (ROOT / "services.html").read_bytes())
        status, _, _ = fetch(self.port, "/serve.py")
        self.assertEqual(status, 404)
        status, _, _ = fetch(self.port, "/assets/../serve.py")
        self.assertEqual(status, 404)
        status, _, body = fetch(self.port, "/assets/style.css")
        self.assertEqual(status, 200)
        self.assertIn(b"--gold-1", body)
        status, _, body = fetch(self.port, "/healthz")
        self.assertEqual(status, 200)
        self.assertEqual(body, b"ok\n")

    def test_repo_does_not_publish_a_static_lateral_page_or_a_password(self):
        self.assertFalse((ROOT / "lateral.html").exists())
        source = (ROOT / "serve.py").read_text(encoding="utf-8")
        self.assertNotIn("Sovereign", source)
        self.assertNotIn("$", source)
        self.assertNotIn('LATERAL_PASSWORD =', source)
        self.assertNotIn("<select", source)
        rendered = "\n".join(
            path.read_text(encoding="utf-8", errors="ignore")
            for path in ROOT.glob("*.html")
        )
        self.assertNotIn("/lateral", rendered)
        self.assertNotIn(">LATERAL<", rendered)
        robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
        self.assertIn("Disallow: /lateral", robots)
        self.assertIn("Disallow: /serve.py", robots)
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        self.assertNotIn("lateral", sitemap.lower())
        nav = (ROOT / "build.py").read_text(encoding="utf-8").split("NAV = [", 1)[1].split("]", 1)[0]
        self.assertNotIn("lateral", nav.lower())
        blueprint = (ROOT / "render.yaml").read_text(encoding="utf-8")
        self.assertIn("LATERAL_PASSWORD", blueprint)
        self.assertIn("sync: false", blueprint)
        self.assertNotIn("generateValue", blueprint)


if __name__ == "__main__":
    unittest.main()
