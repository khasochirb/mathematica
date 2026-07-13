/// <reference lib="webworker" />
// Service worker source (compiled to public/sw.js by @serwist/next at build).
// Makes the installed app work offline: the app shell + all _next/static assets
// are precached, and since course/lesson JSON is statically imported into the JS
// bundle (lib/genmath-lessons.ts), lessons render offline for free once cached.
//
// SECURITY: auth and any non-GET request are NetworkOnly — tokens, logins, and
// refreshes must NEVER be served from cache (users are minors; see the
// cybersecurity manual). API GETs are network-first so a cold/offline launch can
// still show last-known progress.

import { defaultCache } from "@serwist/next/worker";
import type { PrecacheEntry, SerwistGlobalConfig } from "serwist";
import { NetworkFirst, NetworkOnly, Serwist } from "serwist";

declare global {
  interface WorkerGlobalScope extends SerwistGlobalConfig {
    __SW_MANIFEST: (PrecacheEntry | string)[] | undefined;
  }
}

declare const self: ServiceWorkerGlobalScope;

const serwist = new Serwist({
  precacheEntries: self.__SW_MANIFEST,
  skipWaiting: true,
  clientsClaim: true,
  navigationPreload: true,
  runtimeCaching: [
    // Never cache auth or any mutating request — always hit the network.
    {
      matcher: ({ url, request }) =>
        request.method !== "GET" || url.pathname.startsWith("/api/auth"),
      handler: new NetworkOnly(),
    },
    // Other API GETs: network-first with a short timeout, so offline/cold
    // launches fall back to the last successful response.
    {
      matcher: ({ url, request }) =>
        request.method === "GET" && url.pathname.startsWith("/api/"),
      handler: new NetworkFirst({ cacheName: "api-get", networkTimeoutSeconds: 5 }),
    },
    // Next static assets, fonts, images, precache navigation — Serwist defaults.
    ...defaultCache,
  ],
});

serwist.addEventListeners();
