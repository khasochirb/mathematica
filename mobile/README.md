# Mongol Potential — Mobile App (Capacitor)

This wraps the **deployed** web app (`https://www.mongolpotential.com`) in a
native iOS + Android shell so it can ship on the **App Store** and **Google
Play**. It reuses 100% of the website — same login, same courses, same
interactive lessons, same synced progress. Offline support comes from the PWA
service worker that already runs on the site.

Everything in this repo is the version-controlled config. The native builds
themselves are generated on your machine (they're gitignored: `ios/`,
`android/`, `node_modules/`, `www/`).

## What you need
- **A Mac** — required to build and submit the iOS app (Xcode). Android can be
  built on any OS with Android Studio, but you'll want the Mac for both.
- **Xcode** (Mac App Store) and **Android Studio** (developer.android.com).
- **Apple Developer Program** — $99/year (developer.apple.com/programs).
- **Google Play Developer** — $25 one-time (play.google.com/console).
- Node 18+ and this repo cloned locally.

## First-time setup (run on your Mac, from `mobile/`)
```bash
cd mobile
npm install
mkdir -p www && echo "<!doctype html><meta http-equiv=refresh content=0;url=https://www.mongolpotential.com>" > www/index.html
npx cap add ios
npx cap add android
npx cap sync
```
`www/` is a one-line placeholder; at runtime the shell loads the live site
(`server.url` in `capacitor.config.ts`), so the real UI is always the deployed
web app.

## Icons & splash (native — separate from the PWA icons)
```bash
# Put a 1024x1024 icon at mobile/assets/icon.png (copy of public/images/mp.png)
# and a splash at mobile/assets/splash.png (2732x2732, logo centered on #fbfaf8).
npx @capacitor/assets generate --iconBackgroundColor '#fbfaf8' --splashBackgroundColor '#fbfaf8'
npx cap sync
```

## Run / build
```bash
npx cap open ios       # opens Xcode → pick a simulator or device → Run
npx cap open android   # opens Android Studio → Run
```

## Deep links (open mongolpotential.com/... in the app)
The association files are already served from the website:
- iOS: `public/.well-known/apple-app-site-association` — replace `TEAMID` with
  your Apple Team ID (Xcode → Signing → Team), then enable **Associated Domains**
  (`applinks:www.mongolpotential.com`) in Xcode.
- Android: `public/.well-known/assetlinks.json` — replace the SHA-256 with your
  **app-signing** fingerprint (Play Console → App integrity), and add an
  intent-filter for `https://www.mongolpotential.com` in `AndroidManifest.xml`.
Redeploy the website after editing those two files, then verify with Apple's
AASA validator / Google's Statement List tester.

## Android hardware back button
Add once (e.g. in `www/index.html` or a small injected script) so back pops
WebView history instead of closing the app:
```js
import { App } from '@capacitor/app';
App.addListener('backButton', ({ canGoBack }) => {
  if (canGoBack) window.history.back(); else App.exitApp();
});
```

## Auth & sync — nothing to configure
Login and progress "just work": the shell loads the same site, so it uses the
same `/api/auth/*` routes and the same Supabase backend as the browser. The
access token additionally persists to secure storage via the token seam in
`lib/api.ts` (`@capacitor/preferences`, hydrated on boot in `lib/auth-context.tsx`).
The paid-upgrade CTA is automatically hidden inside the app (`useIsNativeShell`),
so there's no non-store billing surface for Apple to reject.

## Store submission checklist
**Both:** privacy policy (`/privacy`) + terms (`/terms`) are live — link them.
Fill Apple **App Privacy** / Google **Data Safety**: you collect an auth email,
learning progress, and anonymous analytics (`/api/events`).

**Apple:** lead the review notes with the *native value* — offline lessons
(service worker), native splash/icon, deep links — so it isn't rejected as
"just a website." Do **not** add any in-app purchase flow; the app is free.

**Google Play:** upload the signed AAB, complete content rating + Data Safety.

## Updating the app
Because the shell loads the live site, **content and feature updates ship by
deploying the website** — no new app build needed. You only rebuild/resubmit the
native app when changing the shell itself (icons, plugins, native config).
