import { readFileSync } from "node:fs";
import withSerwistInit from "@serwist/next";

// Primary-band renumber (2026-08-13): the band moved onto the ministry's
// grade labels, so every saved link into the old grade numbers is sent to
// where that exact content now lives. Generated from the spines by
// scripts/primary/build_renumber_redirects.py; asserted complete by
// scripts/verify-primary-renumber.test.ts.
const primaryRenumber = JSON.parse(
  readFileSync(new URL("./data/primary/renumber-redirects.json", import.meta.url), "utf-8"),
).redirects;

// Phase 0 unpublish (2026-08-14): IB, AP, the standalone topic courses and
// grades 6–7 leave navigation and go noindex, but every file stays in place —
// Same list the app reads through lib/unpublished.ts; this file cannot import
// TypeScript, hence the shared JSON. (IB, AP, the courses and grades 6–7 were
// republished on 2026-08-17 by deleting their lines from it — the whole point
// of unpublishing rather than deleting.)
const unpublishedPrefixes = JSON.parse(
  readFileSync(new URL("./data/unpublished-routes.json", import.meta.url), "utf-8"),
).prefixes;

// Service worker (PWA offline support). Compiles app/sw.ts → public/sw.js at
// build; disabled in `next dev` by default to avoid stale-cache confusion.
const withSerwist = withSerwistInit({
  swSrc: "app/sw.ts",
  swDest: "public/sw.js",
});

/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [],
  },
  async headers() {
    // Unpublished areas: noindex at the header, which covers every nested
    // route in one place and does not touch a single content file. `nofollow`
    // stops the crawler walking deeper from any link that survives.
    const noindex = unpublishedPrefixes.flatMap((prefix) => [
      {
        source: prefix,
        headers: [{ key: "X-Robots-Tag", value: "noindex, nofollow" }],
      },
      {
        source: `${prefix}/:path*`,
        headers: [{ key: "X-Robots-Tag", value: "noindex, nofollow" }],
      },
    ]);
    // The SW and manifest must never be long-cached, or users get stuck on a
    // stale service worker after a deploy. _next/static keeps its immutable
    // content-hashed caching (handled by Next).
    return [
      ...noindex,
      {
        source: "/sw.js",
        headers: [{ key: "Cache-Control", value: "public, max-age=0, must-revalidate" }],
      },
      {
        source: "/manifest.webmanifest",
        headers: [{ key: "Cache-Control", value: "public, max-age=0, must-revalidate" }],
      },
      {
        // iOS requires the Apple App Site Association (deep links) served as
        // application/json; the file has no extension so set it explicitly.
        source: "/.well-known/apple-app-site-association",
        headers: [{ key: "Content-Type", value: "application/json" }],
      },
    ];
  },
  async redirects() {
    return [
      ...primaryRenumber,
      { source: "/ai", destination: "/practice", permanent: false },
      { source: "/ai/:path*", destination: "/practice", permanent: false },
      { source: "/progress", destination: "/dashboard", permanent: false },
      { source: "/progress/:path*", destination: "/dashboard", permanent: false },
      { source: "/upgrade", destination: "/", permanent: false },
      { source: "/upgrade/:path*", destination: "/", permanent: false },
      // /practice/esh/previous-years folded into /practice/esh/test?type=previous
      // during the ЭЕШ Hub IA refactor. 301 (permanent: true) because the route
      // is gone for good — preserves any external bookmarks / search links.
      {
        source: "/practice/esh/previous-years",
        destination: "/practice/esh/test?type=previous",
        permanent: true,
      },
      // /courses used to be the ЭЕШ topic overview, back when the school-math
      // hub at /math was called "General Math". Now that /math IS "Courses",
      // the ЭЕШ overview lives inside its own hub and /courses would be a
      // confusing second name for it. 301 — the old path is gone for good.
      {
        source: "/courses",
        destination: "/practice/esh/topics",
        permanent: true,
      },
    ];
  },
};

export default withSerwist(nextConfig);
