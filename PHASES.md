# Phases

Flat queue of what's next, grouped by phase. Keep tactical — if it feels like overhead, delete entries.

## In flight
- _(empty)_

## Next
- **Phase 8 defensive** — modal source-prefix guard, rename `getAllTests()`, badge styling audit.
- **Offline-logout UX** — when network is down, post-logout `window.location.href = "/"` lands on the offline dinosaur page. Sweep itself runs correctly (synchronous, completes before nav). Future: detect `!navigator.onLine` in the logout handler and show a "logged out — reconnect to continue" message instead of attempting navigation. Cosmetic; not a blocker.
- **P2** Dashboard greeting truncation — for `display_name = "Anon Migrate Test"` it renders "Сайн уу, Anon" (first word only). Probably a `display_name.split(' ')[0]` somewhere in the dashboard greeting component. Should render the full `display_name`.
- **P2** Dashboard renders "ON THIS DEVICE • ACCOUNT SYNC COMING SOON" anon-mode messaging despite a real authenticated user with synced attempts. Either a session-state bug or a stale prop. Undermines user trust in the sync; address before launch but not a data-integrity issue.
- **P2** Prod URL Configuration must include both apex AND www domains. Vercel canonicalizes `mongolpotential.com` → `www.mongolpotential.com`, so `req.nextUrl.origin` returns the www version. Discovered 2026-04-27 during P1 prod smoke when first signup landed at the bare Site URL with `#access_token=...` (Supabase fallback for redirect_to mismatch). Resolved same-day by adding `https://www.mongolpotential.com/**` to the Redirect URLs allowlist; both apex and www now allowlisted. Document this so future redirect-using flows (password reset, email change, OAuth callback) don't repeat the diagnosis cycle.
- **P2** Confirmation email template uses auto-sign-in `{{ .ConfirmationURL }}` token. Per the locked P1 design, post-confirmation should land on `/sign-in?confirmed=true` without auto-sign-in, but Supabase appends `#access_token=...&refresh_token=...` to the redirect because the default template uses `{{ .ConfirmationURL }}`. UX-correct because our sign-in page ignores the hash and renders the manual-sign-in form, but the URL clutter is ugly. Fix in the eventual email-template-customization PR by switching to `{{ .TokenHash }}` with `type=email`.
- **P2** Token-reuse error returns in URL hash, not query string. Supabase redirects re-clicked confirmation links to `?confirmed=true#error=access_denied&error_code=otp_expired`. Our sign-in banner code reads only `useSearchParams` (query string), so the hash error is invisible to the precedence logic; the user sees the confirmed-success banner regardless. Currently produces correct UX (the user IS confirmed), but if Supabase ever moves these errors into the query string the `confirmed > error_code` precedence would mask real errors. P3-level robustness concern, logging as P2 for visibility.

## Pre-launch blockers
- [x] ~~Verify Refresh Token Rotation enabled on prod Supabase~~ — verified ON, reuse interval 10s, detect-and-revoke compromised tokens enabled.
- [ ] Topic value normalization migration (mixed Cyrillic/English)
- [ ] Migrate `mp_token` + `mp_refresh_token` to HttpOnly + Secure cookies (requires server-side route changes)
- [ ] Investigate long-running session → GoTrueClient instance accumulation under token-keyed memo

## Launch trigger items
Items that must be done **before any public launch announcement OR first paying user, whichever comes first**. **Hard rules**, not "when I get around to it."
- [ ] **Upgrade Supabase prod to Pro plan ($25/mo)** — sole backup plan and rate-limit fix. Free plan has zero backups + 3/hour signup rate limit; Pro upgrade resolves both simultaneously at one click: 7-day daily automated backups, no rate limit. Manual pg_dump setup was explored and rejected (workflow friction too high for a non-daily-terminal user — `nano` + URI/password wrangling burned ~45 min before the cost/value didn't pencil out). Optional pre-upgrade: check Supabase for Startups program (https://supabase.com/startups) for credits.

## Carried risks (Free-tier deferral until Pro upgrade)
Both risks resolve simultaneously at Pro upgrade — no partial fix available. No active mitigation in place; explicitly accepting these for pre-launch only.
- **Risk A — survival risk: zero backups.** A corrupted or dropped DB = total data loss with no recovery. Probability low pre-launch (no real user traffic, no concurrent edits). Impact high. The script at [scripts/backup-prod.sh](scripts/backup-prod.sh) stays in the repo for opportunistic manual snapshots before risky migrations — not an ongoing weekly backup. Pro upgrade is the production backup plan.
- **Risk B — growth risk: 3/hour signup rate limit.** Launch traffic burst will silently fail signups beyond the cap — a launch-day wave means most new visitors can't create accounts. Probability rises sharply at launch (essentially certain on launch day if any meaningful traffic), impact = lost users at the worst possible moment. **This is the bigger growth concern**; backup risk is the bigger survival concern. Both gate behind the same upgrade.

## Ops notes
- Supabase free-tier signup rate limit is 3/hour — bit us mid-2.4 smoke testing. If it bites again pre-launch, bump via Auth settings or provision test users through the dashboard.
- Push + confirm green Vercel build after every tier commit, even on feature branches. 2.3.5 added `useSearchParams()` to `/sign-in` without a Suspense boundary and it slipped past local typecheck because it only fails at prerender-time. Pushing early surfaces build-only issues before they stack up.
- Local dev env recovery: `.env.local` should always exist locally and point at staging. If lost, reconstruct from `.env.staging.local` with `sed -E 's/^SUPABASE_URL=/NEXT_PUBLIC_SUPABASE_URL=/; s/^SUPABASE_ANON_KEY=/NEXT_PUBLIC_SUPABASE_ANON_KEY=/' .env.staging.local > .env.local`. Both files are gitignored under `.env*.local` (verified clean — neither in git history). Never `vercel env pull` to populate local dev: that points local at prod Supabase, conflating environments and risking prod-data mutation during smoke tests.
- **Staging/prod Supabase Auth config parity.** 2026-04-27: discovered staging had Confirm email OFF while prod had it ON; P1 contract bug never surfaced in staging tests because the no-session branch never fired. Resolved by enabling Confirm email on staging during P1 step 5. **Discipline going forward: any auth-config change to prod is made on staging first, with config parity verified before staging tests are considered representative.**

## Tier 3 (post-server-sync)
- **3.1** Projected score scale (weighted avg last 5 tests)
- **3.3** Pre-filtered practice routing (`?topic=X&mode=topic`)
- **3.4** Dashboard audit-then-delta
- **3.5** Progress page restructure
- **3.7** Logo / wordmark polish

## Phase 2 (landing + funnel)
- Landing page rewrite (drop "2σ confidence band", mark AI as Coming Soon)
- No-signup test path
- One-line reassurance about 2026 format change
- **Marketing assets via Claude Design** (Anthropic Labs product, launched ~1 week ago) — generate Instagram/FB posters, Telegram channel banner, one-pager, branded email confirmation template reference. Prerequisites: P1 contract bug fixed (clean auth flow to point at), landing page rewrite drafted (settled brand voice to brief from). Onboarding plan: point Claude Design at the mathematica repo for design tokens, web-capture mongolpotential.com for realized look, upload logo asset. Time estimate: ~2-3 hours for first batch of social assets.

## Recently shipped
- **P1 sign-up email confirmation flow** — closes the contract bug where `200 { error }` from confirmation-required signups crashed the client on `accessToken` access. Six-step PR: apiCall runtime guard, new `/api/auth/resend` route + `api.auth.resend` wrapper, new `/sign-up/check-email` page (Suspense-wrapped, primary "Resend" with 60s cross-tab lockout via localStorage), `/sign-in` banner pattern extended to handle `?confirmed=true` (success), `?error_code=otp_expired` (amber + inline resend form), `?error_code=otp_already_used` (treat as success), generic `?error=` catchall, register-route response shape → discriminated union with `emailRedirectTo` + profile-UPDATE-above-session (closes the data-loss gap where confirmation-required signups would lose form-supplied username/displayName to trigger placeholder), sign-up page Suspense split + email pre-fill from `?email=` + `"needsConfirmation" in res` discriminator branch. Verified end-to-end on staging (5/5 smoke) and prod (signup + magic link + confirmed banner + sign-in + token reuse), with 3 follow-up P2s logged from prod discovery (apex+www redirect allowlist, ConfirmationURL hash clutter, hash-vs-query error handling).
- **Sign-up email validator parity (closed, no change required).** Supabase server-side rejects `.local` and other RFC-questionable formats with `Email address "x" is invalid`. Sign-in accepts them because it doesn't re-validate. The error already propagates cleanly to the form. No code-side fix exists without disabling Supabase's validator (not advisable). For dev/test addresses, use the dashboard "Add User" path. Originally logged as a pre-launch blocker; closing as misframed.
- **Profiles auto-create trigger** — Postgres `on_auth_user_created` trigger inserts a placeholder profile row (username `u_<uuid>`, display_name email-local-part) on every `auth.users` insert. Closes FK 23503 for users provisioned outside the sign-up form. Register route changed INSERT→UPDATE to overwrite the placeholder with form values. Migration 005 also backfills existing orphans. Smoke 4/4 on staging, prod cutover green (commit `aaf6d6a`).
- **Prod service role key rotation** — moved off legacy JWT-based keys to the new `sb_publishable_*` / `sb_secret_*` system. Zero-downtime path: new keys generated, Vercel env updated, prod verified working, legacy keys disabled in Supabase. Leaked legacy service_role key from earlier chat history is now invalid.
- **2.5** Logout cleanup — sweep `mongol-potential-performance:*` + `mongol-potential-attempts-queue:*` (and incidentally `anon-migrated:*`) keys on both manual logout and session-expired auto-logout. Smoke 4/4: manual logout, account handoff, session-expired path (both tokens corrupted), offline write+logout.
- **2.4** Anon → signup migration (client UUIDs + upsert onConflict DO NOTHING, 2000 cap, focus-retry)
- **2.3.5** Token refresh with rotation, buffer gate, transient-error handling — commit `19cd946`
- **2.3** Attempts read path (Supabase-first with localStorage merge + offline fallback)
- **2.2.5** Token-keyed Supabase client memoization (fixes GoTrueClient instance leak)
- **2.2** Attempts write path (optimistic write + queue-on-failure + flush on focus)
