import type { CapacitorConfig } from "@capacitor/cli";

// Capacitor native shell for Mongol Potential.
//
// Strategy: a thin WebView that loads the DEPLOYED site (server.url) rather than
// bundling a static export. This means the app is always up to date, reuses the
// exact web UI/logic/content, and the Phase-0 service worker handles offline
// caching inside the WebView. Auth cookies work as-is in a remote-origin
// WebView; the access token additionally persists to secure storage via the
// lib/api.ts token seam (@capacitor/preferences).
//
// Build/run/submit happens on a Mac (see README.md) — this file is authored in
// the repo so the config is version-controlled and reviewable.
const config: CapacitorConfig = {
  appId: "com.mongolpotential.app",
  appName: "Mongol Potential",
  // Minimal local shell; server.url takes over immediately at runtime.
  webDir: "www",
  server: {
    url: "https://www.mongolpotential.com",
    cleartext: false,
  },
  plugins: {
    SplashScreen: {
      launchAutoHide: true,
      backgroundColor: "#fbfaf8",
      showSpinner: false,
    },
  },
};

export default config;
