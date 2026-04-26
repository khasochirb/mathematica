# Phases

Flat queue of what's next, grouped by phase. Keep tactical — if it feels like overhead, delete entries.

## In flight
- _(empty)_

## Next
- **Phase 8 defensive** — modal source-prefix guard, rename `getAllTests()`, badge styling audit.
- **Offline-logout UX** — when network is down, post-logout `window.location.href = "/"` lands on the offline dinosaur page. Sweep itself runs correctly (synchronous, completes before nav). Future: detect `!navigator.onLine` in the logout handler and show a "logged out — reconnect to continue" message instead of attempting navigation. Cosmetic; not a blocker.
- **P2** Dashboard greeting truncation — for `display_name = "Anon Migrate Test"` it renders "Сайн уу, Anon" (first word only). Probably a `display_name.split(' ')[0]` somewhere in the dashboard greeting component. Should render the full `display_name`.
- **P2** Dashboard renders "ON THIS DEVICE • ACCOUNT SYNC COMING SOON" anon-mode messaging despite a real authenticated user with synced attempts. Either a session-state bug or a stale prop. Undermines user trust in the sync; address before launch but not a data-integrity issue.

## Pre-launch blockers
- [x] ~~Verify Refresh Token Rotation enabled on prod Supabase~~ — verified ON, reuse interval 10s, detect-and-revoke compromised tokens enabled.

## Launch trigger items
Items that must be done **before any public launch announcement OR first paying user, whichever comes first**. **Hard rules**, not "when I get around to it."
- [ ] **Upgrade Supabase prod to Pro plan ($25/mo)** — sole backup plan and rate-limit fix. Free plan has zero backups + 3/hour signup rate limit; Pro upgrade resolves both simultaneously at one click: 7-day daily automated backups, no rate limit. Manual pg_dump setup was explored and rejected (workflow friction too high for a non-daily-terminal user — `nano` + URI/password wrangling burned ~45 min before the cost/value didn't pencil out). Optional pre-upgrade: check Supabase for Startups program (https://supabase.com/startups) for credits.

## Carried risks (Free-tier deferral until Pro upgrade)
Both risks resolve simultaneously at Pro upgrade — no partial fix available. No active mitigation in place; explicitly accepting these for pre-launch only.
- **Risk A — survival risk: zero backups.** A corrupted or dropped DB = total data loss with no recovery. Probability low pre-launch (no real user traffic, no concurrent edits). Impact high. The script at [scripts/backup-prod.sh](scripts/backup-prod.sh) stays in the repo for opportunistic manual snapshots before risky migrations — not an ongoing weekly backup. Pro upgrade is the production backup plan.
- **Risk B — growth risk: 3/hour signup rate limit.** Launch traffic burst will silently fail signups beyond the cap — a launch-day wave means most new visitors can't create accounts. Probability rises sharply at launch (essentially certain on launch day if any meaningful traffic), impact = lost users at the worst possible moment. **This is the bigger growth concern**; backup risk is the bigger survival concern. Both gate behind the same upgrade.
- [ ] Topic value normalization migration (mixed Cyrillic/English)
- [ ] Migrate `mp_token` + `mp_refresh_token` to HttpOnly + Secure cookies (requires server-side route changes)
- [ ] Investigate long-running session → GoTrueClient instance accumulation under token-keyed memo
- [ ] Reconcile sign-up vs sign-in email validators. Sign-up rejects `.local` TLDs with "Email address is invalid"; sign-in accepts them. Either loosen sign-up to match sign-in, or add a staging-mode allowlist so iterative testing doesn't require real domains.
- [ ] **P1** Sign-up route returns broken response shape when Supabase requires email confirmation. [app/api/auth/register/route.ts:19-23](app/api/auth/register/route.ts#L19-L23) returns `200 { error: "Account created — please check your email..." }` with no `data` field. [lib/api.ts:55-60](lib/api.ts#L55-L60) `apiCall` treats 200 as success, returns `json.data` (undefined), and the sign-up page crashes with `Cannot read properties of undefined (reading 'accessToken')`. Surfaced during 005 trigger smoke testing. Prod uses email confirmation → this WILL bite real users on launch.

  **Design (locked, ready for implementation):**
  1. Route returns `200 { data: { needsConfirmation: true, email } }`. `api.auth.register` return type becomes a discriminated union: `{ user, accessToken, refreshToken } | { needsConfirmation: true; email }`.
  2. New page [app/(auth)/sign-up/check-email/page.tsx](app/(auth)/sign-up/check-email/page.tsx) — matches /sign-in /sign-up visual language; shows the email; primary CTA "Resend confirmation email" with 60s lockout countdown matching Supabase's resend rate limit; secondary "Wrong email? Sign up again" link. "Didn't get it? Check spam" copy appears AFTER first resend, not preemptively (don't seed doubt before the user has actually checked their inbox).
  3. New route [app/api/auth/resend/route.ts](app/api/auth/resend/route.ts) wraps `supabase.auth.resend({ type: 'signup', email })`. Returns Supabase status mapped sensibly (4xx for rate limit so client shows a real error, not the swallowed-undefined pattern).
  4. Post-confirmation lands on `/sign-in?confirmed=true` with a green banner. Not auto-sign-in — that would be nicer UX (-1 click) but +1 route and +1 failure surface; promote to auto-sign-in post-launch if friction shows up.
  5. Sign-in page banner pattern extends to handle: `?confirmed=true` (green success), `?error_code=otp_expired` (amber + [Resend] button with email input), `?error_code=otp_already_used` (info banner — treat as success since the user IS confirmed), generic `?error=...` catchall (red).
  6. Email validator parity: accept the Supabase-imposed `.local` TLD constraint (server-side validator, can't loosen client-side). Improve form error message to surface Supabase's actual response text instead of swallowing it. Folded into this PR since we're in the auth surface anyway.

  **Scope: one PR.** Pieces are coupled by the same flow; staging the work would mean re-running the rate-limit-burning sign-up flow multiple times.

  **Bonus concerns captured during design:**
  - **apiCall runtime guard**: [lib/api.ts:55-60](lib/api.ts#L55-L60) does `return json.data as T` without checking `data` exists. This fragility is what made the P1 bug manifest as a confusing client crash instead of a loud error. Add `if (!('data' in json)) throw new Error(json.error ?? 'Malformed response')` so future contract drift fails loud, not silent. Defensive guard, not part of the P1 fix proper but worth bundling.
  - **Staging-first Site URL config**: when configuring Supabase Authentication → URL Configuration (Site URL + Redirect URLs), apply to staging first, smoke-test the full email confirmation flow end-to-end, only then mirror to prod. Order matters because misconfigured Site URL breaks the email link silently — easier to catch on staging where we expect to debug.
  - **Email template branding (deferred)**: Supabase ships default templates ("Confirm your email" with their branding). For launch we'd want branded templates with our copy. Out of scope for the P1 fix; revisit at launch readiness as a separate small task.

## Ops notes
- Supabase free-tier signup rate limit is 3/hour — bit us mid-2.4 smoke testing. If it bites again pre-launch, bump via Auth settings or provision test users through the dashboard.
- Push + confirm green Vercel build after every tier commit, even on feature branches. 2.3.5 added `useSearchParams()` to `/sign-in` without a Suspense boundary and it slipped past local typecheck because it only fails at prerender-time. Pushing early surfaces build-only issues before they stack up.
- Local dev env recovery: `.env.local` should always exist locally and point at staging. If lost, reconstruct from `.env.staging.local` with `sed -E 's/^SUPABASE_URL=/NEXT_PUBLIC_SUPABASE_URL=/; s/^SUPABASE_ANON_KEY=/NEXT_PUBLIC_SUPABASE_ANON_KEY=/' .env.staging.local > .env.local`. Both files are gitignored under `.env*.local` (verified clean — neither in git history). Never `vercel env pull` to populate local dev: that points local at prod Supabase, conflating environments and risking prod-data mutation during smoke tests.

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
- **Profiles auto-create trigger** — Postgres `on_auth_user_created` trigger inserts a placeholder profile row (username `u_<uuid>`, display_name email-local-part) on every `auth.users` insert. Closes FK 23503 for users provisioned outside the sign-up form. Register route changed INSERT→UPDATE to overwrite the placeholder with form values. Migration 005 also backfills existing orphans. Smoke 4/4 on staging, prod cutover green (commit `aaf6d6a`).
- **Prod service role key rotation** — moved off legacy JWT-based keys to the new `sb_publishable_*` / `sb_secret_*` system. Zero-downtime path: new keys generated, Vercel env updated, prod verified working, legacy keys disabled in Supabase. Leaked legacy service_role key from earlier chat history is now invalid.
- **2.5** Logout cleanup — sweep `mongol-potential-performance:*` + `mongol-potential-attempts-queue:*` (and incidentally `anon-migrated:*`) keys on both manual logout and session-expired auto-logout. Smoke 4/4: manual logout, account handoff, session-expired path (both tokens corrupted), offline write+logout.
- **2.4** Anon → signup migration (client UUIDs + upsert onConflict DO NOTHING, 2000 cap, focus-retry)
- **2.3.5** Token refresh with rotation, buffer gate, transient-error handling — commit `19cd946`
- **2.3** Attempts read path (Supabase-first with localStorage merge + offline fallback)
- **2.2.5** Token-keyed Supabase client memoization (fixes GoTrueClient instance leak)
- **2.2** Attempts write path (optimistic write + queue-on-failure + flush on focus)
