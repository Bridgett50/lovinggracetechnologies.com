/* God Knew Her Name March on Washington — service worker.
   Registered from march pages; its scope is this directory only.
   Caches public march pages and assets for offline reading.
   Form submissions (POST) and private data are never cached. */
var CACHE = "gkn-march-v1";
var CORE = [
  "./",
  "./index.html",
  "./offline.html",
  "./manifest.webmanifest",
  "./styles/brand-tokens.css",
  "./styles/march.css",
  "./assets/namefold.svg",
  "./assets/icons/icon-192.png",
  "./about/",
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
        if (key.indexOf("gkn-march-") === 0 && key !== CACHE) {
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
  if (request.mode === "navigate") {
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
