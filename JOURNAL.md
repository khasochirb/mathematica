# Session journal

Reverse-chronological log of major work sessions. Each entry captures the arc — what shipped, what was decided, what surfaced, what's deferred — in tighter form than commit messages alone. PHASES.md holds the queue; this holds the narrative.

## 2026-05-07 — Practice-test answer-key audit, Part 1 fixes

Hand-audited 504 questions across the 14 paid practice tests (test1a–test7b). Full per-test reports at `/Users/khasochir/Desktop/outputs/audit-results/`. Shipped Part 1 (6 deterministic fixes); Part 2 (9 items) and Part 3 (3 solution-prose rewrites) await Khas's input. No auth/code paths touched — pure JSON data edits.

**Shipped (Part 1):**
- **Test-2A-Q7** — slope question. `(√3, √6)` and `(2, 4√2)` → slope `= (4√2 − √6)/(2 − √3)`. Rationalized = `5√2 + 2√6`. Stored D was `(5√2 + 2√6)/2` — off by factor of 2. Option A `(√6 − 4√2)/(√3 − 2)` is the same value as the un-rationalized form (sign-flip of numerator and denominator). Corrected answer to A, solution rewritten to show the sign-flip and note rationalized value.
- **Test-2A-Q27** — `M = [[1,2],[0,1]]`, `M³ = [[1,6],[0,1]]`. Solution prose computed this correctly but final letter said B (which was `[[3,8],[0,3]]`). Corrected letter to C.
- **Test-2B-Q17** — α = 12 radians. `12 mod 2π ≈ 5.72 ∈ (3π/2, 2π)` → quadrant IV → answer D. Stored A (Q1) wrong; old solution's "subtract 2π twice to get −0.57 = Q1" reasoning is mathematically wrong (−0.57 rad is co-terminal with 5.72 rad which is in Q4, not Q1). Corrected answer to D, solution rewritten.
- **Test-5A-Q34** — discrete probability. Σ_{x=2}^6 (1/4)^(x−1) = 341/1024, so k = 683/1024 = **2732/4096**. Stored option A was `2731/4096` (off-by-one). Option text fixed; stored answer letter A unchanged.
- **Test-4B-Q31** — Venn-diagram MCQ. Options C and E were textually identical (`\overline{A} \cap B`). E rewritten to `\overline{A} \cup B` as a plausible distractor. Stored answer C unchanged.
- **Test-7B-Q21** — power-simplification MCQ. Options B and D were textually identical (`x^{1/3}`). D rewritten to `x^{2/9}` (a plausible mid-step result for the simplification). Stored answer A unchanged.

**Pending Khas's decision (Part 2 — surfaced in chat reply, NOT auto-fixed):**
- **Test-2A-Q2** — denominator `5⁴` produces `3²⁶/5⁴`, not in any option. Either change question denominator to `3⁹` (then C is correct) or change stored answer to E (None). Solution prose silently uses `/3⁹`.
- **Test-2A-Q13** — hexagon area is `1+√2`. Verified via shoelace coordinates. None of A–E match (stored C = `1 + √2/2`). Add `1+√2` as an option, or revise question geometry.
- **Test-2A-Q26** — P(1 boy + 1 girl from 14B+7G picking 2) = `7/15`, not stored 7/30 (off by factor of 2 — likely ordered/unordered confusion). Add 7/15 as option, or rephrase question so 7/30 becomes correct.
- **Test-2A-Q6** — exponent transcribed as `3/4 − 2 = -5/4` doesn't lead to the Vieta values the solution uses (`x²−x−20=0` gives stored 41). Question text appears corrupted; need original exponent.
- **Test-3B-Q15** — statements I and III textually identical (both `3^(2x)`). If I and III are the same, answer should be D (I and III), not stored B (only III). Need original statement I.
- **Test-1B-Q28** — "to nearest tenth" requested but stored A = `√5` (exact form). Strict reading would prefer D = 2.2. Lenient or strict?
- **Test-7A / Test-7B** — both numbered Q2–Q37 (36 questions, no Q1). Intentional gap or renumbering needed?
- **Test-2A-Q22** — options C and D both render `2^(10^(13^(20^y)))`. Stored D correct mathematically, but which option to change and to what?
- **Test-3B-Q20** — options C and D both render `\log_3 (1/(xy^(1/3)))`. Stored C correct, but which option to change?

**Pending Khas's decision (Part 3 — solution-prose rewrites, ship now or defer):**
- **Test-2B-Q2** — solution mid-step has `(8²)⁴ = 2¹²` (should be 2²⁴), final answer 2²³ correct.
- **Test-2B-Q6** — solution first uses wrong Vieta values (`ab=−12` → 28), then self-corrects to 52.
- **Test-3A-Q22** — solution talks about "average -2.5" but stored answer 0.5 is the median.

**Out of scope (NOT touched):**
- 28 AMBIGUOUS questions reference images/graphs/tables not present in the JSON dump. Stored answers may be correct given the missing visuals. Defer to a separate image-data-restoration workstream.
- All test1a, test1b, test4a, test5b, test6a, test6b items not flagged are confirmed clean.

**Audit findings worth noting:**
- **5 of the 7 DEFINITE answer-key errors are in test2a alone.** That test should be re-vetted in full — having 5/36 stored answers wrong is unusually high; suggests systematic transcription issues that may have repeated elsewhere undetected.
- **Question-quality issues (duplicate options, corrupted text, missing options) cluster in test2a/test3b.** Same possible-systematic-cause story.

**Working-relationship note:**
- I (Claude) initially started editing in `~/mathematica` instead of the live `~/Desktop/mathematica2` folder during a prior session. No data lost (user pulled the commits in cleanly), but caught early this session via `git remote -v` + reflog cross-check. Memory updated so future sessions land on the right folder.

---

## 2026-04-27 — Pre-launch hardening, day 2

Three blockers shipped to prod, two P2 dashboard fixes shipped, PHASES.md cleanup, last technical blocker investigated and closed. End-of-day status: all technical blockers resolved or closed. Remaining work for soft launch is Phase B (legal baseline, content polish, landing page rewrite, no-signup test path, marketing assets).

**Shipped:**
- **HttpOnly refresh token cookie** (commit `eea7b31`, Option A scope). Refresh token moved from JS-readable cookie to server-set HttpOnly + Secure (prod) + SameSite=Lax + Path=/api/auth + Max-Age=2592000. New `/api/auth/logout` route added since JS can't clear HttpOnly cookies. Cookie attributes centralized in [lib/auth-cookies.ts](lib/auth-cookies.ts) — single source of truth for the four routes that touch the cookie, since attribute drift would silently break cookie matching at the clear site. **Access token deliberately NOT migrated** (Option B considered and rejected; reasoning under Design decisions below).
- **Topic + subtopic canonicalization at the DB write boundary** (commit `7284839`). `canonicalizeTopic` validates against the 10 canonical English keys, falls back to `"other"` for unknowns. `canonicalizeSubtopic` is shape-normalizing only (trim + lowercase + collapse whitespace) and preserves Cyrillic. Hooked into `toServerRow` in [lib/use-performance.ts](lib/use-performance.ts) so all four DB write paths get canonicalization for free. Verification script at [scripts/verify-canonicalize.ts](scripts/verify-canonicalize.ts) (19/19 pass), runnable via `npm run verify:canonicalize`. Stopgap until the repo gets a real test framework (Vitest setup logged as a separate P3). One-time data-cleanup SQL ran via Supabase web SQL editor on both environments — staging: 12 distinct subtopics with `Вектор` + `вектор` collapsed into a single `вектор` row; prod: 7 distinct subtopics with `Стандарт хэлбэр` + `стандарт хэлбэр` collapsed into a single `стандарт хэлбэр` row.
- **Dashboard + practice + analytics P2 fixes** (commit `249a4a9`). `displayName.split(" ")[0]` truncated multi-word names ("Anon Migrate Test" → "Anon"); switched to full `displayName` at all four render sites with consts renamed `firstName` → `userName`. Stale "ON THIS DEVICE · ACCOUNT SYNC COMING SOON" copy from before Tier 2 server-sync deleted from dashboard and analytics — line was actively misleading users about whether their data was being saved.
- **PHASES.md status corrections** (commit `e4a95f3`). Topic-migration status updated from pending to verified; HttpOnly entry clarified as Option A scope (refresh token only, by design) so the decision isn't relitigated next session.
- **PHASES.md staleness sweep** (commit `57f13ad`). Three already-resolved P2s moved out of `## Next`: dashboard greeting truncation + dashboard "ON THIS DEVICE" → Recently shipped; apex+www redirect allowlist → Ops notes (reframed as documentation, not pending work).

**Investigation closures:**
- **GoTrueClient instance accumulation** — closed without fix. Code audit identified the token-keyed memo in [lib/supabase.ts](lib/supabase.ts) `createAuthedSupabaseClient` as the predicted leak source: each token rotation creates a new GoTrueClient sharing the default `storageKey`, registering alongside the old one. Browser repro on staging showed zero warnings during 30-second click-through — consistent with prediction (warning would only fire after a ~50-minute token rotation, not initial load + casual nav). Worst-case ~few KB memory across a multi-hour session. Cosmetic, not a resource issue. Three mitigation directions captured in code-audit notes if user-impacting symptoms ever surface (per-token `storageKey`, single-client-with-`setSession`, single-client-with-header-rotation).

**Design decisions captured:**
- **Option A vs Option B for cookie HttpOnly migration**: chose A (refresh only). Reasoning: refresh token is the high-value asset (long-lived, mints new access tokens); access token has 1-hour TTL + rotates on every refresh via RTR (small XSS blast radius); Option B requires rewriting `lib/use-performance.ts` direct-Supabase calls + adds attempt-write latency for marginal security gain.
- **sessionStorage → localStorage for resend lockout**: sessionStorage was per-tab so a user could open a second tab to bypass the rate limit entirely. Switched to localStorage; trade-off accepted since the 60s window is short.
- **Topic canonicalization at write boundary, NOT in source files**: defensive layer that protects the DB even if source JSONs stay messy or become messy again later. Source JSON cleanup deferred to content polish phase as P3.
- **Move-UPDATE-above-session in P1 register route** (caught during yesterday's step 5 review, but worth re-noting): without this, confirmation-required signups would have lost form-supplied username/displayName to the trigger placeholder on first login. Silent prod data loss avoided.

**Production discoveries logged as P2/P3:**
- **P2** apex+www redirect allowlist required: Vercel canonicalizes `mongolpotential.com` → `www.mongolpotential.com`, so `req.nextUrl.origin` returns the www form. Without `https://www.mongolpotential.com/**` in the Supabase Redirect URLs allowlist, redirect_to mismatch causes Supabase to fall back to the bare Site URL with `#access_token=...`. Resolved same-day; documented in Ops notes for future redirect-using flows.
- **P2** ConfirmationURL email template appends auto-sign-in tokens to the redirect hash. UX-correct (sign-in page ignores the hash, renders manual sign-in form) but ugly. Fix in eventual email-template-customization PR with `{{ .TokenHash }}` + `type=email`.
- **P2** Token-reuse errors return in URL hash, not query string. Sign-in banner reads only `useSearchParams` (query string) so hash errors are invisible to precedence logic. Currently produces correct UX incidentally. Robustness concern: if Supabase ever moves these errors into query string, `confirmed > error_code` precedence would mask real errors.

**Configuration drifts caught:**
- Staging/prod email-confirmation toggle parity: staging had Confirm email OFF while prod had it ON; P1 contract bug never surfaced in staging tests because the no-session branch never fired. Resolved during P1 step 5 verification by enabling Confirm email on staging. Discipline note added to PHASES.md Ops: any auth-config change to prod is made on staging first.
- Prod URL Configuration mid-deploy: pre-merge checklist initially appeared unchecked when the work had been done; recovered via screenshot-based re-verification before push.

**Working-relationship calibration notes** (operational, not blame):
- claude.ai workflow terminology slipped twice. First: "feature branch + PR + preview" language when this repo is direct-to-main throughout. Second: "push to main for staging deployment, don't deploy to prod yet" — but push to main IS prod deployment in this workflow. Both caught before push.
- claude.ai twice claimed work was undone that was actually done — prod URL Configuration items 1-3 marked unchecked when they had been verified earlier in the session; topic-migration SQL marked pending when it had been run via the Supabase web SQL editor (outside the terminal session, so not in commit history). Re-confirmed accurately from screenshot/SQL evidence before acting.
- Operational discipline going forward: cross-check claude.ai claims about already-done work against file evidence, screenshot evidence, and SQL output on long sessions. Workflow shorthand ("PR", "preview", "merge") is fine as conversational language but worth confirming intent on workflow-shaping moves.

**Pre-launch blocker status: all technical blockers resolved or closed.**
- ✅ Prod service role key rotation
- ✅ Auto-create profiles trigger
- ✅ RTR verified
- ✅ P1 contract bug fix
- ✅ Both P2 dashboard bugs
- ✅ Topic + subtopic canonicalization
- ✅ HttpOnly auth tokens (Option A — refresh only, by design)
- ✅ GoTrueClient instance accumulation (closed, cosmetic-only)

**Carry-forward references worth verifying before next related work:**
Tier 3 items in PHASES.md `## Tier 3 (post-server-sync)` — status unclear from this session, may have shipped quietly or may be unfinished:
- 3.1 Projected score scale (weighted avg last 5 tests)
- 3.2 Recent accuracy *(referenced in handoff but not in current PHASES.md — verify whether it shipped quietly or was renumbered)*
- 3.3 Pre-filtered practice routing (`?topic=X&mode=topic`)
- 3.5 Progress page restructure
- 3.7 Logo / wordmark polish

(PHASES.md additionally lists 3.4 dashboard audit-then-delta which wasn't in the carry-forward note; worth reconciling.)

**Vercel deploys this session:** `eea7b31` (HttpOnly refresh token), `7284839` (topic canonicalization), `249a4a9` (dashboard P2 fixes), `e4a95f3` (PHASES corrections), `57f13ad` (PHASES staleness sweep), plus this commit (GoTrueClient closure + journal). All green.

**Next session pickup:** Phase B begins. Likely starts with legal baseline scope decision (Terms / Privacy / Cookie policy minimums for a Mongolian launch) and the landing page rewrite.

## 2026-04-27 — P1 contract bug shipped to prod

**Shipped:**
- **P1 sign-up email confirmation flow** (commit `331804a`, 7 files / +465/-39). Closes the contract bug where `200 { error }` from confirmation-required signups crashed the sign-up page on `accessToken` access. Six-step implementation: apiCall runtime guard, new `/api/auth/resend` route + page UI with 60s cross-tab lockout via localStorage, new `/sign-up/check-email` page, `/sign-in` banner pattern extended for `?confirmed=true` / `?error_code=otp_expired` (with inline resend form) / `?error_code=otp_already_used` / generic catchall, register-route response shape → discriminated union with `emailRedirectTo` + profile-UPDATE-above-session, sign-up Suspense split + email pre-fill + discriminator branch. Email validator polish closed as misframed (no custom regex existed; Supabase server-side rejects, error text already propagates cleanly).
- **PHASES.md cleanup** (commit `7802df3`). Pre-merge checklist deleted post-prod-smoke; three new P2s logged from prod discovery; Recently shipped P1 entry updated with prod verification.

**Smoke test arc:**
- Staging 5/5: four URL-banner tests on `/sign-in` (hand-crafted URLs, 0 signup slots) + real signup A end-to-end with profile-row verification.
- Prod end-to-end: signup → check-email page → real magic-link click → confirmed banner → sign-in → dashboard. Plus token-reuse test (re-clicked confirmed link, banner rendered correctly). Test users cleaned up.
- **Rate budget actuals**: planned 2 of 3 hourly slots, actual was higher across both environments. Staging signup A v1 was burned discovering Confirm email was OFF on staging (no-session branch never fired). Prod signup #1 was burned discovering apex/www redirect mismatch (Vercel canonicalizes apex → www; redirect_to allowlist needed both forms).

**Two design-pass catches worth highlighting:**
- **Move-UPDATE-above-session.** Caught during step 5 review by re-reading the profiles trigger SQL — recognized that the trigger writes placeholder values meant to be overwritten by the register route's UPDATE, but the original step 5 design exited on the needsConfirmation branch BEFORE reaching the UPDATE. Would have been silent prod data loss: confirmation-required signups' form-supplied username/displayName dropped on the floor; users land post-confirmation with `u_<uuid>` / email-prefix placeholders and no recovery path.
- **sessionStorage → localStorage for resend lockout.** Originally implemented with sessionStorage on the framing of "annoying-not-broken multi-tab edge case." Cross-tab smoke during step 4 surfaced that sessionStorage is per-tab — a user could open a second tab and bypass the rate limit entirely. Switched to localStorage with the trade-off accepted: lockout persists across browser restarts (acceptable since the 60s window is short and aligns with Supabase's actual server-side limit).

**Production discoveries logged as P2:**
- **Apex+www redirect allowlist required.** Vercel canonicalizes `mongolpotential.com` → `www.mongolpotential.com`, so `req.nextUrl.origin` returns the www form. First prod signup landed at bare Site URL with `#access_token=...` (Supabase fallback for redirect_to mismatch). Resolved same-day by adding `https://www.mongolpotential.com/**` to the Redirect URLs allowlist; both apex and www now allowlisted. Documented for future redirect-using flows (password reset, email change, OAuth callback).
- **ConfirmationURL email template appends auto-sign-in tokens to redirect hash.** Per locked design, post-confirmation should land on `/sign-in?confirmed=true` without auto-sign-in, but Supabase's default `{{ .ConfirmationURL }}` token appends `#access_token=...&refresh_token=...`. UX-correct because our sign-in page ignores the hash and renders the manual sign-in form, but ugly. Fix in the email-template-customization PR with `{{ .TokenHash }}` + `type=email`.
- **Token-reuse errors return in URL hash, not query string.** Sign-in banner reads only `useSearchParams` (query string), so hash errors are invisible to the precedence logic. Currently produces correct UX incidentally (re-clicked confirmation = user IS confirmed = confirmed-banner is the right thing). Robustness concern: if Supabase ever moves these errors into the query string, `confirmed > error_code` precedence would mask real errors. P3-level, logged P2 for visibility.

**Staging/prod auth config drift finding:**
- Staging had Confirm email OFF while prod had it ON. P1 contract bug never surfaced in staging tests because the no-session branch never fired — staging always returned an immediate session. Resolved during step 5 verification by enabling Confirm email on staging.
- **Going-forward discipline** (now in PHASES.md Ops notes): any auth-config change to prod is made on staging first, AND any test expected to exercise a specific code branch verifies the staging config is set up to fire that branch.

**Working-relationship calibration notes** (operational, not blame):
- claude.ai workflow terminology slipped to "feature branch + PR + preview" mid-session when this repo has been direct-to-main for the entire arc. Caught before the push, no harm. Worth noting that "PR" / "merge" language has been ambient throughout — usable as shorthand but worth confirming intent on workflow-shaping moves.
- claude.ai twice claimed work was undone that was already done — the prod URL Configuration items 1–3 were marked unchecked in the pre-merge checklist when they had been verified earlier in the session. Re-confirmed accurately from chat-history screenshots before the push. Operational note for next session's handoff: cross-check claims about completion state against file/screenshot evidence on long sessions.
- Original commit message body conflated "prod traffic exposed the bug" with "discovered during pre-launch hardening." There is no real prod traffic yet; the bug surfaced during pre-launch review, not from a real-user incident. Caught in the amend cycle and corrected.

**Pre-launch blocker status post-P1:**
- ✅ Prod service role key rotation
- ✅ Auto-create profiles trigger
- ✅ RTR verified
- ✅ P1 contract bug fix
- ⏳ HttpOnly cookie migration for `mp_token` + `mp_refresh_token` (server-route changes required)
- ⏳ Topic value normalization migration (mixed Cyrillic/English)
- ⏳ GoTrueClient instance accumulation investigation

**P2 backlog as of end of session:**
- Apex+www redirect allowlist (resolved, kept for record)
- ConfirmationURL hash clutter (rolls into email-template-customization PR)
- Hash-vs-query banner precedence robustness
- Dashboard greeting truncation
- Anon-mode messaging on authed dashboard

**Vercel deploys this session:** `331804a` (P1 PR), `7802df3` (PHASES cleanup). Both green.

## 2026-04-26 — Pre-launch hardening, day 1

**Shipped:**
- **Prod Supabase service role key rotation** via the new `sb_publishable_*` / `sb_secret_*` system. Zero-downtime path: new keys generated, Vercel env updated, prod verified, legacy JWT-based keys disabled. Leaked legacy service_role key from earlier chat history is now invalid.
- **Profiles auto-create trigger** end-to-end on staging + prod (commit `aaf6d6a`). Closes the FK 23503 gap for users provisioned outside the sign-up form (Supabase dashboard "Add User", future OAuth, admin scripts). Migration 005 = trigger + handle_new_user() function (SECURITY DEFINER, locked search_path) + idempotent backfill. Register route changed from INSERT→UPDATE since the trigger now creates the row first inside the same transaction. 4/4 staging smoke pass: dashboard add-user, attempts insert (no FK 23503), form sign-up overwrites placeholder, anon migration preserves 3 attempts with original timestamps. Prod cutover green (timed migration apply against Vercel-Ready window).

**Verified:**
- **RTR on prod**: Refresh Token Rotation toggle ON, reuse interval 10s, detect-and-revoke compromised tokens enabled.

**Designed (ready for implementation tomorrow):**
- **P1 sign-up email confirmation contract bug.** Six design decisions locked + three bonus concerns captured (see PHASES.md P1 entry). Implementation tomorrow starts with a plan outline (file changes, smoke test sequence, staging-first Site URL config order) before any code.

**Deferred:**
- **Supabase Pro upgrade** ($25/mo). Free-tier carried risks documented explicitly (zero backups = survival risk; 3/hr signup rate limit = growth risk). Hard launch trigger: before public launch announcement OR first paying user, whichever comes first.
- **Manual weekly pg_dump backup setup**. Workflow friction too high (~45 min wrestling with `nano` + URI handling) for a non-daily-terminal user. Pro upgrade is the production backup plan; the script at `scripts/backup-prod.sh` stays in the repo for opportunistic snapshots before risky migrations.

**Surfaced during this session:**
- **P1**: sign-up route/client contract bug (designed today; implementing tomorrow)
- **P2**: dashboard greeting truncation — `display_name = "Anon Migrate Test"` renders "Сайн уу, Anon" (probably `display_name.split(' ')[0]` somewhere)
- **P2**: dashboard renders "ON THIS DEVICE • ACCOUNT SYNC COMING SOON" anon-mode messaging despite an authed user with synced attempts

**Vercel deploys this session:** `378f86a` (Suspense fix), `d9bdf1c` (Step 2.5 logout cleanup), `aaf6d6a` (profiles trigger), `10fb784` (PHASES.md update post-trigger). All green.

**Tomorrow's pickup**: P1 implementation. Plan outline → 5 min review → code.
