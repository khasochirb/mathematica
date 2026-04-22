# Phases

Flat queue of what's next, grouped by phase. Keep tactical — if it feels like overhead, delete entries.

## In flight
- **2.5** logout cleanup — clear `mongol-potential-performance:*` + `mongol-potential-attempts-queue:*` keys on logout to prevent stale per-user data on shared devices. Sweeps the `anon-migrated:*` flags too — harmless because re-login finds an empty anon bucket and migration short-circuits. Covers the TODO breadcrumb in [lib/auth-context.tsx](lib/auth-context.tsx) logout().

## Next
- **Phase 8 defensive** — modal source-prefix guard, rename `getAllTests()`, badge styling audit.

## Pre-launch blockers
- [ ] Rotate prod Supabase service role key (was exposed in chat history)
- [ ] Verify Refresh Token Rotation enabled on prod Supabase (currently staging-only)
- [ ] Verify backups enabled on prod Supabase
- [ ] Topic value normalization migration (mixed Cyrillic/English)
- [ ] Migrate `mp_token` + `mp_refresh_token` to HttpOnly + Secure cookies (requires server-side route changes)
- [ ] Investigate long-running session → GoTrueClient instance accumulation under token-keyed memo
- [ ] Auto-create `profiles` row on `auth.users` insert via Postgres trigger (Supabase `on_auth_user_created` template). Without it, any user provisioned outside the app's sign-up form (dashboard, future OAuth, admin scripts) fails `attempts` writes with FK 23503. Reproducer: Supabase dashboard → Add User → any attempt write errors.
- [ ] Reconcile sign-up vs sign-in email validators. Sign-up rejects `.local` TLDs with "Email address is invalid"; sign-in accepts them. Either loosen sign-up to match sign-in, or add a staging-mode allowlist so iterative testing doesn't require real domains.

## Ops notes
- Supabase free-tier signup rate limit is 3/hour — bit us mid-2.4 smoke testing. If it bites again pre-launch, bump via Auth settings or provision test users through the dashboard.

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

## Recently shipped
- **2.4** Anon → signup migration (client UUIDs + upsert onConflict DO NOTHING, 2000 cap, focus-retry)
- **2.3.5** Token refresh with rotation, buffer gate, transient-error handling — commit `19cd946`
- **2.3** Attempts read path (Supabase-first with localStorage merge + offline fallback)
- **2.2.5** Token-keyed Supabase client memoization (fixes GoTrueClient instance leak)
- **2.2** Attempts write path (optimistic write + queue-on-failure + flush on focus)
