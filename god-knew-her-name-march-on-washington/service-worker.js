/* God Knew Her Name March on Washington — service worker.
   Registered from march pages; its scope is this directory only.
   Caches public march pages and assets for offline reading.
   Form submissions (POST) and private data are never cached.
   v2 (Nov 27, 2026): new cache name so browsers install this worker and
   drop the v1 cache; documents are network-first (fresh copy wins,
   cache is the offline fallback); static assets stay cache-first
   under the current cache name.
   v3 (Nov 27, 2026): cache bumped in the same commit as the Toni Green
   page, the four-day schedule and the donation wiring, per the standing
   rule that every design publish bumps the cache version.
   v4 (Nov 27, 2026): cache bumped in the same commit as the About page
   band reorder (The Song opens the page; the 30th Anniversary moves to
   its background position before Event Status).
   v5 (Nov 27, 2026): cache bumped in the same commit as the Event
   Leadership listing update.
   v6 (Nov 27, 2026): cache bumped in the same build as the Attend page
   ticket rebuild, the new For Artists page, the homepage master-message
   block and the Transportation form's two new fields.
   v7 (Nov 27, 2026): cache bumped in the same commit as the homepage
   lead-magnet subscribe block and the new guide page (the guide page
   itself stays out of the CORE precache list below).
   v9 (Nov 28, 2026): cache bumped after restoring the pre-restructure
   site so browsers drop the v8 cache. */
var CACHE = "gkn-march-v9";
var CORE = [
  "./",
  "./index.html",
  "./offline.html",
  "./manifest.webmanifest",
  "./styles/brand-tokens.css",
  "./styles/march.css",
  "./assets/phoenix-tree.png",
  "./assets/icons/icon-192.png",
  "./about/",
  "./toni-green/",
  "./for-artists/",
  "./schedule/",
  "./attend/",
  "./churches/",
  "./organizations/",
  "./states/",
  "./transportation/",
  "./volunteer/",
  "./marshals/",
  "./donate/",
  "./sponsors/",
  "./media/",
  "./accessibility/",
  "./updates/",
  "./faq/",
  "./contact/",
  "./merchandise/"
];

self.addEventListener("install", function (event) {
  event.waitUntil(
    caches.open(CACHE).then(function (cache) {
      return cache.addAll(CORE);
    }).then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener("activate", function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.map(function (key) {
        if (key !== CACHE) {
          return caches.delete(key);
        }
        return null;
      }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener("fetch", function (event) {
  var request = event.request;
  if (request.method !== "GET") { return; }
  var sameOrigin = new URL(request.url).origin === self.location.origin;
  if (request.mode === "navigate" || request.destination === "document") {
    event.respondWith(
      fetch(request).then(function (response) {
        var copy = response.clone();
        caches.open(CACHE).then(function (cache) { cache.put(request, copy); });
        return response;
      }).catch(function () {
        return caches.match(request).then(function (hit) {
          return hit || caches.match("./offline.html");
        });
      })
    );
    return;
  }
  event.respondWith(
    caches.match(request).then(function (hit) {
      if (hit) { return hit; }
      return fetch(request).then(function (response) {
        if (sameOrigin && response.ok) {
          var copy = response.clone();
          caches.open(CACHE).then(function (cache) { cache.put(request, copy); });
        }
        return response;
      });
    })
  );
});
