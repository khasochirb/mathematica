# Ops Flags — the registry

An **ops flag** is an external dependency only the owner can complete —
a dashboard secret, a database migration, DNS, billing. Code that depends
on one ships dark (gracefully degraded) until the owner acts.

This file is the single source of truth for open flags. The protocol for
raising, tracking and closing them is `.claude/skills/ops-flags/SKILL.md`.
The mechanical check is:

```
npm run verify:flags -- https://www.mongolpotential.com     # owner machine
node scripts/verify-flags.mjs                               # against local dev
```

which reads `GET /api/health/flags` (secretless enums; also reachable from
remote Claude sessions via the Vercel MCP web fetch). Note: the endpoint
exists on prod only after the first deploy that includes it.

Rule zero: **a flag may only move to Resolved after its verification
passes.** "I set it" is not evidence; the probe output is.

---

## OPEN

### FLAG-002 — migration `008_student_profiles.sql` not applied

| | |
|---|---|
| **Since** | student provisioning shipped (task #103) |
| **Dormant** | `scripts/create-students.mjs` (teacher-provisioned accounts); grade/focus personalization in `/api/auth/me` |
| **Degradation** | Verified 2026-07-25: the ME route reads `select("*")` and falls back to `null` for the absent columns; the migration is purely additive (`ADD COLUMN IF NOT EXISTS`, nullable / defaulted), so applying it cannot affect existing rows or self-signup. |
| **Owner action** | ~2 minutes, below |
| **Verify** | After the health endpoint deploys: `verify:flags` shows `migration_008_student_profiles: applied`. Immediately after running the SQL, the verification query in step 3 returns 4 rows. |
| **Reading a non-`applied` result** | `missing` = the column is genuinely absent; run the runbook. `unknown` = the probe could not decide, and `verify:flags` prints the error code beside it: `42501` the service role cannot see `profiles` (a grants/RLS problem, not this migration), `42P01`/`PGRST205` the table itself is unreachable (larger than this flag — do not run the runbook), `no-client` no Supabase env in that environment. Checked 2026-07-26 on prod: reported `unknown`, which is why the code is now carried through. |

**Runbook**

1. Supabase dashboard → project → SQL Editor → New query.
2. Paste the entire contents of
   `supabase/migrations/008_student_profiles.sql` and Run.
   (Idempotent — safe to run twice.)
3. Verify in the same editor:
   ```sql
   select column_name from information_schema.columns
   where table_name = 'profiles'
     and column_name in ('grade','focus','focus_href','role','notes');
   ```
   Expect 5 rows.
4. Optional but recommended first: a snapshot via
   `scripts/backup-prod.sh` (needs `~/.mp-backup-env`).
5. Move this entry to Resolved with the date and the row count.

---

### FLAG-003 — `ADMIN_ACTIVATION_KEY` not set in Vercel (OPTIONAL)

| | |
|---|---|
| **Since** | Premium pricing launch (prices public, manual fulfillment) |
| **Dormant** | `POST /api/subscription/activate` — the curl one-liner that activates a paid account. Returns 503 while unset. |
| **Degradation** | None that blocks revenue: the primary runbook is the Supabase dashboard — set `profiles.is_subscribed = true` and `subscription_expires_at` for the buyer's row (their `user_id` is on the purchase request in `premium_waitlist`). The route is a convenience. |
| **Owner action** | Optional, ~2 min: Vercel → imathhub → Settings → Env Vars → add `ADMIN_ACTIVATION_KEY` = a long random string (e.g. `openssl rand -hex 24`), Production, Sensitive. Redeploy. |
| **Verify** | `curl -s -o /dev/null -w '%{http_code}' -X POST https://www.mongolpotential.com/api/subscription/activate` → **401** = key set (route armed) · **503** = unset (dashboard-only). |

**Security note:** before 2026-08-01 this route let any signed-in user
activate their own subscription (pre-pricing placeholder). It now requires
the admin key and is disabled without it.

---

## WATCH (not blocking, verified by the same endpoint)

*(none open — 009 confirmed applied, see Resolved)*

---

## RESOLVED

*(move entries here with date + verification evidence; never delete)*

### FLAG-001 — `ANTHROPIC_API_KEY` — RESOLVED

| | |
|---|---|
| **Resolved** | 2026-08-01 (owner set the key in Vercel + redeployed) |
| **Evidence** | `GET https://www.mongolpotential.com/api/health/flags` → `"anthropic_api_key":"configured"` (probe at 16:03 UTC). The AI tutor (`/api/tutor`) is live on production. |
| **Notes** | Prod at that moment ran pre-pricing code: flat `FREE_DAILY_AI_LIMIT` for all users. The tiered quota (3 free / 30 premium) and the Premium price cards ship with the next deploy of the working branch. Owner should also set a monthly spend limit in console.anthropic.com. On that deploy: move "AI багш" in the upgrade modal from "On the way" to "Unlocks today" (marked with a comment in lib/upgrade-modal-context.tsx). |

### migration `009_attempts_context` — APPLIED (was a WATCH item)

| | |
|---|---|
| **Resolved** | 2026-08-01, deploy `f2f5d07` |
| **Evidence** | `GET https://www.mongolpotential.com/api/health/flags` → `"migration_009_attempts_context":"applied"`. Belief (code-inspection + clean runtime errors, 2026-07-25) is now a mechanical fact from the probe. |
| **Consequence** | Attempts carry their `context` through the real column, not the no-column fallback — per-course analytics are trustworthy. |

---

## Session log

- **2026-08-05** — Probe after deploy `644ab67` (the Grade 3 year — 8 topics,
  40 lessons, a 48-form problem bank — plus the fix that made 23 authored
  practice figures actually render, 20 of which had been invisible in Grade 4
  production): `anthropic_api_key: configured`, `migration_009: applied`,
  `migration_008_student_profiles: unknown` (FLAG-002 unchanged — `unknown`,
  so read that flag's "Reading a non-`applied` result" row before acting).
  FLAG-003 still optional/unset. No migrations in the diff and no auth, API
  or env files touched, so nothing depended on either open flag. Prod
  verified: `/math/3` serves all eight topics with the paywall intact (first
  topic free, the rest Premium-locked) and `/math/problem-bank/3` serves its
  units with rendered math; runtime errors clean over the 2h window. Deploy
  went READY in 2m34s.
- **2026-08-04** — Probe after deploy `1244ae8` (per-unit problem banks for
  grades 4, 6, 7, 8, 10, 11 — 7,300 new problems, so every course on the
  /math ladder from Grade 4 to Grade 12 now has a bank; plus two rendering
  fixes to banks already in production, `money()` emitted outside math in
  integrated-3 and `.strip("$")` in precalculus explanations):
  `anthropic_api_key: configured`, `migration_009: applied`,
  `migration_008_student_profiles: unknown` (FLAG-002 unchanged — `unknown`,
  so read that flag's "Reading a non-`applied` result" row before acting).
  FLAG-003 still optional/unset. No migrations in the diff and nothing
  depended on either open flag. Prod verified: `/math/problem-bank/10` and
  `/math/problem-bank/4` both serve their unit lists and rendered math (no
  "not found", no error boundary); runtime errors clean over the 2h window.
  This deploy went READY in 2m41s, not the ~28 minutes the previous one
  took, despite adding ~156k lines of bank JSON — so that earlier stall was
  a one-off in Vercel's output propagation, not a property of the diff size.
  New permanent gate shipped with it: `verify-problembank.py` now fails any
  bank string carrying LaTeX outside `$...$`.
- **2026-08-04** — Probe after deploy `445b569` (two production bug fixes:
  the Grade 4/5 lesson back/finish buttons pointing into Grade 6, and
  /tutoring switching the whole site to Mongolian; plus the link-integrity
  and language gates): `anthropic_api_key: configured`,
  `migration_009: applied`, `migration_008_student_profiles: unknown`
  (FLAG-002 unchanged — `unknown`, so read that flag's "Reading a
  non-`applied` result" row before acting). FLAG-003 still optional/unset.
  No migrations in the diff and nothing depended on either open flag.
  Prod verified: `/math/5/multiplication-and-division` serves with its back
  arrow to `/math/5` and all five lessons inside Grade 5; runtime errors
  clean over the 2h window. NOTE: the production build sat in "Deploying
  outputs" for ~25 min after a 2-minute compile — not a failure, just slow
  propagation of the large static output; the same commit had already built
  READY as a branch preview. Browser walks of prod are not possible from the
  cloud sandbox (proxy denies CONNECT), so behavioural verification ran
  against a local production build of this exact commit: 2,140-page link
  crawl, 0 soft-404s, and the five-scenario language walk.

- **2026-07-25** — Registry created. Both flags' live prod status is not
  directly probeable from the cloud sandbox (proxy denies CONNECT to
  mongolpotential.com; the Vercel MCP fetch is GET-only and the health
  endpoint is not yet deployed). Status recorded per standing owner
  reports + code inspection; degradation paths verified in code; prod
  runtime errors clean over 7d.
- **2026-08-01** — First probe of the deployed health endpoint (via the
  Vercel MCP fetch, which reaches it fine): `anthropic_api_key: missing`
  (FLAG-001 still open), `migration_008_student_profiles: unknown`
  (FLAG-002 still open — `unknown`, not `missing`, so read it per that
  flag's "Reading a non-`applied` result" row before acting),
  `migration_009_attempts_context: applied` → 009 moved to Resolved.
  Nothing in deploy `f2f5d07` depended on either open flag.
- **2026-08-04** — Probe after deploy `dd4f479` (the /math course paywall:
  first topic of every course free, the rest Premium; Premium copy rewritten
  to lead with the courses): `anthropic_api_key: configured`,
  `migration_009: applied`, `migration_008_student_profiles: unknown`
  (FLAG-002 unchanged). FLAG-003 still optional/unset. No migrations in the
  diff. NOTE for whoever works FLAG-003: the paywall raises the value of
  `POST /api/subscription/activate` — it is now the one-step way to turn on
  a paying student's course access, so setting ADMIN_ACTIVATION_KEY is worth
  the two minutes it was not worth before. Prod runtime errors clean over
  the 1h window.
- **2026-08-04** — Probe after deploy `1ea78b4` (Grade 4 complete year with
  figures, Grade 5 Topic 8 + per-unit Grade 5 banks, navigator restyle;
  the mascot experiment was reverted before shipping): `anthropic_api_key:
  configured`, `migration_009: applied`, `migration_008_student_profiles:
  unknown` (FLAG-002 unchanged — `unknown`, so read that flag's
  "Reading a non-`applied` result" row before acting). FLAG-003 still
  optional/unset. Content-only deploy — no migrations in the diff, nothing
  depended on either open flag; prod runtime errors clean over the 2h window.
- **2026-08-03** — Probe after deploy `16e52d8` (Grade 5 topics 4–7:
  fractions, decimals, measurement, geometry): `anthropic_api_key:
  configured`, `migration_009: applied`, `migration_008_student_profiles:
  unknown` (FLAG-002 unchanged). FLAG-003 still optional/unset. Content-only
  deploy — no migrations, nothing depended on either open flag; prod runtime
  errors clean over the 3h window.
- **2026-08-03** — Probe after deploy `33d89b6` (IM3 bank + course exams,
  Grade 5 topics 1–3 opening the primary band): `anthropic_api_key:
  configured`, `migration_009: applied`, `migration_008_student_profiles:
  unknown` (FLAG-002 unchanged). FLAG-003 still optional/unset. Content-only
  deploy — no migrations, nothing depended on either open flag; prod runtime
  errors clean over the 2h window.
- **2026-08-02** — Probe after deploy `d055401` (IM3 units 7–8 + orphan
  repair): `anthropic_api_key: configured`, `migration_009: applied`,
  `migration_008_student_profiles: unknown` (FLAG-002 unchanged — read
  that flag's "Reading a non-`applied` result" row before acting).
  FLAG-003 still optional/unset. Nothing in this deploy depended on
  either open flag; prod runtime errors clean.
