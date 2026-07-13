import withSerwistInit from "@serwist/next";

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
    // The SW and manifest must never be long-cached, or users get stuck on a
    // stale service worker after a deploy. _next/static keeps its immutable
    // content-hashed caching (handled by Next).
    return [
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
    ];
  },
};

export default withSerwist(nextConfig);
