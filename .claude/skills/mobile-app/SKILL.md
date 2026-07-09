---
name: mobile-app
description: >
  Operating manual for building the Mongol Potential mobile app (iOS +
  Android) from the existing Next.js web app. Read this before scaffolding
  any mobile project, choosing a framework, or wiring the app to the API.
  Covers the architecture decision (wrap vs rebuild), the recommended path,
  the API/auth/content contracts the app must honor, and per-path checklists.
---

# Mongol Potential Mobile App — Operating Manual

This is the plan for shipping Mongol Potential as a phone app on the App
Store and Google Play. It is written against the ACTUAL codebase as of
this commit, so the numbers and contracts below are real, not aspirational.

**The one-line answer:** the web app is ~91% client-rendered React with a
clean token-auth REST API and self-contained JSON content. **Wrap it, do
not rebuild it.** Ship a PWA first (days), then a Capacitor native shell
for the stores (weeks). A React Native rewrite would throw away ~104
interactive lesson widgets, the KaTeX math renderer, the whole design
system, and every hub/lesson/test/placement screen — months of work for a
worse result. §1 justifies this; if you disagree, read §1 before doing
anything else.

---

## 1. The architecture decision (read this first)

Three ways to put an existing web app on phones:

| Path | What you reuse | What you rebuild | Effort | Store presence |
|---|---|---|---|---|
| **A. PWA** (installable web app) | 100% of the app | nothing | days | "Add to Home Screen"; Android via Play (TWA), iOS install is manual |
| **B. Capacitor / native WebView shell** | 100% of the UI + logic | a thin native wrapper, native auth storage, push, deep links | 1–3 weeks | Real App Store + Play listings |
| **C. React Native / Expo rewrite** | API + content JSON only | every screen, all ~104 widgets, KaTeX, design system, navigation | 3–9 months | Real listings; fully native feel |

**Why the codebase points hard at A→B and away from C:**

- **72 of 79 pages are client components** (`"use client"`). The 7 server
  pages are static marketing/legal (`blog`, `terms`, `privacy`) and thin
  coming-soon wrappers (`sat`, `ib`, `ap`, `esh/loop`). There is almost no
  server-rendering to lose in a wrap.
- **The interactive lesson engine is ~104 widget kinds**
  (`lib/genmath-interactive.ts`) plus the geometry primitives — number
  lines, coordinate grids, algebra tiles, balance scales, 3-D solids,
  circle/arc/transversal diagrams, etc. Every one is a bespoke React/SVG
  component. Reimplementing these in React Native is the single biggest
  cost on the platform and buys nothing the WebView doesn't already give.
- **Math is rendered with KaTeX** (`components/esh/MathText.tsx`). KaTeX is
  a DOM/CSS renderer; there is no drop-in RN equivalent. In a wrap it just
  works; in RN you fight it forever.
- **The backend is already an app-ready REST API** (§3) with Bearer-token
  auth (§4). Nothing about the API assumes a browser. A native shell talks
  to the same endpoints the web app does.
- **Content is 138 self-contained JSON files (~8.4 MB)** bundled statically
  (§5) — trivially shippable offline in a wrap, and format-agnostic if you
  ever do go native.

Recommendation: **do A now, then B.** Treat C as a multi-quarter project
you only start if the WebView experience proves genuinely insufficient
(it won't for a content + practice app).

---

## 2. The recommended path, in order

### Phase 0 — Make the web app installable (PWA). Ship this first.

Smallest possible step that puts an icon on a phone and runs offline.

1. Add a **web app manifest** (`app/manifest.ts` in the App Router):
   name, short_name, `start_url: "/"`, `display: "standalone"`,
   `background_color`/`theme_color` matched to the site's `--bg`/`--accent`,
   and icons at 192/512 (maskable + any). None exists today — grep found no
   `manifest`/`sw.js`/`next-pwa`.
2. Add **viewport + theme + apple-web-app** metadata to `app/layout.tsx`
   (currently absent): `viewport: { width, initialScale, viewportFit:
   "cover" }`, `themeColor`, and `appleWebApp: { capable: true, statusBarStyle,
   title }` so iOS treats it as a standalone app.
3. Add a **service worker** for offline + caching. Use `next-pwa` (or
   `@serwist/next`) — it generates the SW at build. Cache strategy:
   - App shell + `_next/static/*` → precache (cache-first).
   - Content JSON is already in the JS bundle (static imports), so it's
     covered by the shell precache — lessons work offline for free.
   - API GETs (`/api/progress`, `/api/streaks`, …) → network-first with a
     short cache fallback; never cache auth or POST.
4. Verify with Lighthouse PWA audit + a real install on iOS Safari and
   Android Chrome. Ship. This alone gives most of the "app" value.

### Phase 1 — Wrap in Capacitor for the stores.

When you need real App Store / Play listings, push notifications, or a
native splash/icon.

1. `npm i @capacitor/core @capacitor/cli && npx cap init`. Add iOS +
   Android platforms.
2. **Point the shell at the deployed site**, don't bundle a static export.
   The app is server-backed (API routes live on Vercel), so the cleanest
   wrap loads `https://www.mongolpotential.com` (or a dedicated
   `app.` origin) in the Capacitor WebView with the service worker doing
   offline caching. Set `server.url` in `capacitor.config.ts`, or ship a
   thin local bundle that immediately navigates to the remote origin.
   - Alternative (fully offline-first): `next build` with a mostly-static
     export of the client pages and keep ONLY `/api/*` remote. Feasible
     because 72/79 pages are client components, but it's more plumbing;
     do it only if offline-first is a hard requirement. Start with the
     remote-URL wrap.
3. Replace the web token cookies with **native secure storage** (§4) — this
   is the one real code change a wrap needs.
4. Add native concerns: splash screen + adaptive icon, status-bar styling
   to match theme, deep links / universal links (§7), and push (§8).
5. Build, test on device/simulator, submit. See §9 for store gotchas
   (especially Apple's rules on web-wrapped apps and external payments).

---

## 3. The API contract the app consumes

The backend is Next.js route handlers under `app/api/`. Base URL is the
deployed origin; the app sends `Authorization: Bearer <access token>` on
authed calls. Responses are a `{ data }` envelope on success and
`{ error }` with a non-2xx status on failure — mirror `lib/api.ts`'s
`apiCall` unwrapping exactly (it throws `json.error` on non-2xx and on any
2xx body missing `data`).

Endpoints today (`app/api/**/route.ts`):

- **Auth**: `POST /api/auth/register`, `POST /api/auth/login`,
  `GET /api/auth/me`, `POST /api/auth/refresh`, `POST /api/auth/logout`,
  `POST /api/auth/resend`.
- **Practice/progress**: `POST /api/sessions`,
  `POST /api/sessions/[id]/complete`, `POST /api/answers`,
  `GET /api/progress`, `GET /api/progress/weak-topics`,
  `GET /api/streaks`, `GET /api/achievements`, `GET /api/topics`,
  `GET /api/problems/next`.
- **ЭЕШ Section 2**: `POST /api/section2/attempts`.
- **Refinement loop**: `/api/refinement-loop` (miss → mastery state machine).
- **Subscription**: `GET /api/subscription/status`,
  `POST /api/subscription/activate`.
- **Misc**: `POST /api/events` (analytics), `POST /api/waitlist`.

Rules for the app:
- **Reuse `lib/api.ts` verbatim where possible.** It is plain
  `fetch` + Bearer header + envelope handling — no browser-only APIs except
  cookie access (which you replace, §4). In a WebView wrap it runs
  unchanged; in any native client, port its shapes 1:1.
- The `User` type and all response types live in `lib/api.ts` — treat it as
  the API's typed client and single source of truth. Don't re-derive shapes.
- Content gating is subscription-aware server-side; the app must send the
  token so the server returns the right pool (`isSubscribed` in `/me`).

## 4. Auth & token storage (the one real change a wrap needs)

Web token model (`lib/api.ts`, `lib/auth-cookies.ts`, `lib/auth-context.tsx`):
- **Access token** `mp_token`: JS-readable cookie, `path=/`, 7-day, sent as
  `Authorization: Bearer`. Refreshed proactively when <10 min to expiry.
- **Refresh token** `mp_refresh_token`: HttpOnly cookie, `path=/api/auth`,
  30-day (Supabase default), rotated on every `/api/auth/refresh`.
- Refresh flow: on 4xx → logout+redirect; on 5xx/network → keep session.

In a WebView wrap pointed at the remote origin, **cookies just work** — the
web flow runs as-is, and this is the fastest path. Harden it for native:

- Prefer **`@capacitor/preferences` or a secure-storage plugin** over
  cookies for the access token, so a killed WebView doesn't lose the
  session and the token survives cold starts. Bridge it into the same
  `getMpToken`/`setToken`/`clearToken` seam in `lib/api.ts` (those three
  functions are the ONLY token I/O — swap their bodies, nothing else
  changes).
- The HttpOnly refresh cookie can't be read by JS by design; in a pure
  native client (path C) you'd instead store the Supabase refresh token in
  the OS keychain and call `/api/auth/refresh` with it in the body — but
  that requires a small server change to accept a body token. For a wrap,
  leave the cookie flow intact.
- **Never** log tokens, never put them in analytics events, never bundle
  the `SUPABASE_SERVICE_ROLE_KEY` — that is server-only and must never
  reach the app binary. The app only ever holds a user access token.

## 5. Content delivery

- 138 JSON files, ~8.4 MB total (`data/genmath` 6.9M, `data/questions`
  1.5M, `data/learn` 28K). Lessons/tests are **statically imported** into
  the bundle (82 static imports in `lib/genmath-lessons.ts`), so in a wrap
  they ship inside the app and render offline with zero API calls.
- Figures (ЭЕШ) are PNGs in `public/section1-figures` +
  `public/section2-figures` (~3 MB) — precache them in the service worker
  if you want offline ЭЕШ tests.
- **Do not fork the content into an app-specific format.** The web build is
  the source of truth; the wrap consumes the same bundle. If content grows
  large enough to hurt install size, move to on-demand fetch of the JSON
  from the origin (they're already discrete files) with SW caching — but
  8.4 MB is fine to ship today.
- Math renders through `components/esh/MathText.tsx` (KaTeX). Its CSS
  (`katex/dist/katex.min.css`) must be present — it is, via the existing
  imports; verify fonts load in the WebView (they're in `_next/static`).

## 6. i18n

- Language is `mp_lang` in `localStorage` (`lib/lang-context.tsx`), values
  `en` | `mn`. **Content language is a property of the hub, not the toggle**
  (ЭЕШ = Mongolian content; General Math = per-topic EN/MN mirror; SAT/IB
  hubs = English) — see `memory/expansion-vision.md` §4.7. The app inherits
  this for free in a wrap.
- In a WebView, `localStorage` persists, so the language choice survives.
  If you move to secure storage for auth, leave `mp_lang` in localStorage —
  it's not sensitive.
- Set the app's store listing + native shell language to match the primary
  audience (Mongolian first).

## 7. Deep links & navigation

- The app's URL structure IS its navigation: `/math/<grade>/<topic>/<lesson>`,
  `/math/geometry/<unit>/<lesson>`, `/practice/esh/test/<testId>`,
  `/dashboard`, etc. In a wrap these already work.
- Configure **universal links (iOS)** and **App Links (Android)** so
  `https://www.mongolpotential.com/...` opens the app, not the browser —
  needed for the student-account email links and for sharing lesson URLs.
- `ContentGate` (`components/genmath/ContentGate.tsx`) already handles
  "signed-out → sign-in with `?next=` return". Deep links into gated
  content route through it unchanged.
- Handle the Android hardware back button (Capacitor `App` plugin) to pop
  WebView history instead of closing the app.

## 8. Push notifications (Phase 1+)

- No push infra exists today. Add via Capacitor Push (APNs + FCM). Natural
  triggers already have server signals: **streaks** (`/api/streaks` — daily
  reminder to keep the streak), **refinement loop** (a due drill),
  placement follow-ups. Wire these server-side to a push send when you add
  the infra; the app just registers its device token to a new endpoint.
- Respect quiet hours and let users opt out — a study-reminder app that
  over-notifies gets uninstalled.

## 9. Store submission gotchas

- **Apple: a pure web wrapper can be rejected** ("app is just a website")
  unless it delivers native value — so lead with offline content, push
  notifications, and a native splash/icon/nav, not an empty WebView.
- **Payments**: the product is free today (`memory/expansion-vision.md`
  §4.5). If you ever add paid tiers, in-app digital purchases must use
  Apple/Google billing (30% cut) — do NOT ship the web Stripe/Jotform flow
  inside the app for digital goods, or it's a rejection. Keep any paid
  upgrade out of the app binary until this is designed. The current
  `/api/subscription/*` + "Upgrade to Premium" web CTA must be hidden or
  routed to store billing inside the app.
- Provide privacy policy + terms (already at `/privacy`, `/terms`) and fill
  the App Privacy / Data Safety questionnaires (auth email, progress data,
  analytics events).
- Icons/splash from a single source via `@capacitor/assets`.

## 10. What NOT to do

- **Don't rebuild the UI in React Native** to start. §1. The widget +
  KaTeX cost is the whole ballgame.
- **Don't fork the content or the API client.** One source of truth
  (`lib/api.ts`, `data/**`, `lib/genmath-lessons.ts`); the app consumes it.
- **Don't ship the service-role key or any server secret** in the app.
- **Don't bundle a paid-upgrade purchase flow** that bypasses store billing.
- **Don't reimplement auth.** Reuse the token flow; only swap the 3-function
  storage seam (§4).
- **Don't block on offline-first.** Remote-URL wrap + SW caching ships far
  sooner than a static export; add deeper offline later if needed.

## 11. Ship checklist

**Phase 0 (PWA):**
```
[ ] app/manifest.ts (name, icons 192/512 maskable, standalone, theme colors)
[ ] layout.tsx viewport + themeColor + appleWebApp metadata
[ ] service worker (next-pwa/serwist): precache shell + static; network-first API GET
[ ] Figures precached if offline ЭЕШ wanted
[ ] Lighthouse PWA audit green; real install tested iOS Safari + Android Chrome
[ ] Deploy; verify offline lesson load
```

**Phase 1 (Capacitor native shell):**
```
[ ] cap init; iOS + Android platforms added
[ ] Loads deployed origin (or app. subdomain) in WebView
[ ] Access token moved to secure storage via the getMpToken/setToken/clearToken seam
[ ] Refresh flow verified (proactive refresh, 4xx→logout, 5xx→keep)
[ ] Splash + adaptive icon + status-bar theme (@capacitor/assets)
[ ] Universal links / App Links for mongolpotential.com
[ ] Android hardware back button handled
[ ] Paid-upgrade CTA hidden or routed to store billing (if any paid tier exists)
[ ] Privacy/Data-Safety questionnaires; policy + terms linked
[ ] Push (optional this phase): device registration + a real trigger (streaks)
[ ] Tested on physical iOS + Android device; submitted to both stores
```

## 12. Known constraints carried from the platform

- Free-for-launch pricing (`memory/expansion-vision.md` §4.5) — nothing is
  gated behind payment today, which keeps store review simple. Revisit §9
  billing rules only when a paid tier is designed.
- Supabase is the auth + data backend; the app never talks to Supabase
  directly, only through `/api/*`. (Direct Supabase access from the app is
  possible via the anon key + RLS, but routing through the existing API
  keeps one contract — prefer it.)
- GitHub access + deploys are scoped to `khasochirb/mathematica`; the
  mobile shell is a separate concern from the web deploy (Vercel `main`).
  Decide early whether the app lives in this repo (a `mobile/` or
  `capacitor/` dir) or its own repo — a `mobile/` dir in this repo keeps
  the API client and content in reach without a submodule.
