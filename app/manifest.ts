import type { MetadataRoute } from "next";

// Web App Manifest — served by Next at /manifest.webmanifest and auto-linked
// from every page. This is what makes the site installable ("Add to Home
// Screen") as a standalone app on iOS and Android.
//
// Colors must be hex (a manifest cannot parse the oklch() the theme uses).
// Values below are the light --bg from app/globals.css converted to sRGB —
// the app defaults to the light theme for new users, so the splash/chrome
// match a fresh launch with no dark flash.
export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "Mongol Potential",
    short_name: "Mongol Potential",
    description:
      "World-class math education for Mongolian students — courses, interactive lessons, and ЭЕШ/SAT/IB practice.",
    start_url: "/",
    scope: "/",
    display: "standalone",
    orientation: "portrait",
    lang: "mn",
    dir: "ltr",
    background_color: "#fbfaf8",
    theme_color: "#fbfaf8",
    categories: ["education"],
    icons: [
      { src: "/icons/icon-192.png", sizes: "192x192", type: "image/png", purpose: "any" },
      { src: "/icons/icon-512.png", sizes: "512x512", type: "image/png", purpose: "any" },
      { src: "/icons/maskable-192.png", sizes: "192x192", type: "image/png", purpose: "maskable" },
      { src: "/icons/maskable-512.png", sizes: "512x512", type: "image/png", purpose: "maskable" },
    ],
  };
}
