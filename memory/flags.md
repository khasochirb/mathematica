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

### FLAG-008 — migration `015_attempts_server_delete.sql` not applied (SECURITY)

| | |
|---|---|
| **Raised** | 2026-08-14 security audit (branch `claude/website-security-audit-qb8ceu`) |
| **Priority** | MEDIUM-HIGH — a grade-integrity hole. `attempts` still carries `attempts_delete_own` plus the full default grant, so the browser deletes rows itself over PostgREST with the student's own JWT and **writes its own filter**. `delete().eq("user_id", me).eq("is_correct", false)` removes only the wrong answers, leaving a perfect record and inflating accuracy, mastery, the weakness model, the ratings card and the predicted grade — the numbers a parent is shown and pays for. |
| **SEQUENCING — read before applying** | **Apply only AFTER the deploy containing `/api/attempts/erase` is live.** Safe in one direction only: applying it early loses no data, it just makes the old bundle's "clear my data" button fail (the panel reports the failure rather than claiming success) until the new code ships. |
| **Ships dark?** | Yes. The replacement route works whether or not the migration is applied — it holds the service-role client, which RLS and these grants do not affect. The migration only removes the *old* path. |
| **Degradation** | None once the deploy is live. `SELECT` and `INSERT` are deliberately unchanged; whole-scope erase stays available through the route. |
| **Sentinel** | None. Adds no column and no rows, so neither the column probe nor the row-count probe of `lib/flags.ts` can see it. Known gap, same as the other grant migrations — the manual probe below is a one-line SQL. |
| **Verify** | The SQL in runbook step 3 below. Expect exactly 2 rows: `INSERT`, `SELECT`. Probed 2026-08-16: returns `DELETE, INSERT, REFERENCES, SELECT, TRIGGER, UPDATE` for BOTH `authenticated` and `anon` — unapplied. |

**Runbook**

1. Confirm production runs a build containing `/api/attempts/erase`. If not, **stop** — see SEQUENCING.
2. Supabase dashboard → SQL Editor → paste `supabase/migrations/015_attempts_server_delete.sql` → Run. (Idempotent.)
3. Verify in the same editor:
   ```sql
   select privilege_type from information_schema.role_table_grants
   where grantee = 'authenticated' and table_schema = 'public'
     and table_name = 'attempts'
   order by privilege_type;
   ```
   Expect exactly 2 rows: `INSERT`, `SELECT`. (Before the migration this also
   returns `DELETE` — that is the hole — plus `UPDATE`, `REFERENCES` and
   `TRIGGER` from Supabase's default grant.)
4. Smoke-test: sign in as a test account, erase one scope, confirm the panel reports success and the rows are gone.
5. Move to Resolved with the date and the 2-row result.

---

### FLAG-004 — migration `011_seed_esh_graph.sql` not applied

| | |
|---|---|
| **Raised** | 2026-08-15 |
| **Owner action** | Apply `supabase/migrations/011_seed_esh_graph.sql` in Supabase. Design owns applying it; this session owns generating it. |
| **What it seeds** | 184 ЭЕШ skills + 367 prerequisite edges into `skills` and `skill_prerequisites`. Both tables already exist and were empty (owner-confirmed 2026-08-15). |
| **Blocks** | Everything downstream of the graph — adaptive placement, recommendations, mastery, score prediction. Design is blocked on it now. |
| **Ships dark?** | Yes. Nothing in the app reads `skills` yet, so an unapplied migration changes no behaviour; it just leaves the graph invisible to other agents. |
| **Sentinel** | `migration_011_seed_esh_graph` in `lib/flags.ts`. This is the first ROW-COUNT sentinel: 011 adds no column, so the usual column probe would report "applied" against an empty table. It counts `skills` rows with `hub='eysh'` and wants ≥150 (184 ship; the floor sits low so a later graph revision does not turn it red). |
| **Verify** | `npm run verify:flags -- https://www.mongolpotential.com`, or `GET /api/health/flags` → `"migration_011_seed_esh_graph":"applied"`. |
| **Notes** | DATA ONLY — no DDL. The tables come from Stream A's `010_skill_graph.sql`, which deliberately left 011 free for this seed. Skills are UPSERTED and never deleted, because 010 defines `skill_state.skill_id REFERENCES skills(id) ON DELETE CASCADE` — a delete-then-insert (which this file originally used) would wipe every student's mastery state on a re-run, and `attempts.skill_id` references it too, without cascade. Edges are cleared and rewritten, since nothing references `skill_prerequisites`. `name_mn` is excluded from the upsert so a Phase-3 Mongolian pass survives re-seeding. Opens with a schema assertion naming any missing column, closes with post-conditions (≥184 skills, 367 edges, no dangling endpoints) inside the transaction. |
| **Schema corrections found by reading 010** | Two, both fatal, neither guessable: the hub value is `'eysh'` (a CHECK constraint, not `'esh'`), and the edge column is `requires_id` (not `prereq_skill_id`). Confirmed against `origin/claude/problem-bank-premium-design-osj7de`. |

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

### Four tables still carry the default `GRANT ALL`, protected only by absent policies

Probed 2026-08-16. `attempts`, `section2_attempts`, `refinement_loop_sessions`,
`events` and `premium_waitlist` all still grant
`DELETE, INSERT, REFERENCES, SELECT, TRIGGER, UPDATE` to **both** `anon` and
`authenticated` — Supabase's default `GRANT ALL ON ALL TABLES`.

Nothing here is exploitable today: `events` and `premium_waitlist` have zero
policies (RLS fail-closed), and the verbs with no matching policy are
default-denied on the others. But this is exactly the "correct by accident"
shape §0 of `docs/security/data-access-model.md` warns about — one future
`CREATE POLICY ... FOR UPDATE` silently opens a write path, because the grant
behind it was never narrowed. `015` fixes `attempts`; the other four want the
same treatment in a follow-up migration.

Also noted: every policy on `attempts`, `section2_attempts`,
`refinement_loop_sessions`, `subscription_events` and `user_achievements` is
still `TO public` rather than `TO authenticated`. Safe only because
`auth.uid()` is NULL for `anon` and `NULL = user_id` is NULL — correct, but by
accident rather than by statement.

---

## RESOLVED

*(move entries here with date + verification evidence; never delete)*

### FLAG-005 — migration `012_profiles_column_grants.sql` — RESOLVED

| | |
|---|---|
| **Raised** | 2026-08-14 — live privilege escalation: any signed-in student could PATCH their own `profiles` row through PostgREST and set `is_subscribed = true`, inflate `global_xp`/`global_level`, or overwrite teacher-set `grade`/`focus`. RLS limits the row, not the columns. |
| **Resolved** | 2026-08-16, probed directly against production (project `gsvfcnfbrzysaiiwgchf`) |
| **Evidence** | `role_column_grants` for `grantee='authenticated', table='profiles', privilege='UPDATE'` → **0 rows**. `role_table_grants` for `profiles` → `anon: REFERENCES,SELECT,TRIGGER` and `authenticated: REFERENCES,SELECT,TRIGGER`. No UPDATE at table or column level: the hole is closed. |
| **Applied STRICTER than the file** | The migration grants UPDATE on three safe columns (`username`, `display_name`, `avatar_url`); production has **no** UPDATE grant at all. So the original runbook's "expect exactly 3 rows" is wrong against the live database — it returns 0. Recorded here rather than silently reconciled, because the two are not the same state. |
| **Live consequence** | Policy `profiles_update_own` (UPDATE, `{authenticated}`) still exists but is inert without a grant — the belt with no braces, harmless but misleading to a future reader. If self-service profile editing is ever built, it needs the three column grants back; today no browser code updates `profiles`, so nothing is broken. |

### FLAG-006 — migration `013_deletion_cascade.sql` — RESOLVED

| | |
|---|---|
| **Raised** | 2026-08-14 — 6 of 19 production accounts could not be deleted at all. Six tables referenced `profiles` with `ON DELETE NO ACTION`, so deleting the auth user cascaded into `profiles` and was refused with SQLSTATE 23503, failing partway and leaving the account inconsistent. |
| **Resolved** | 2026-08-16, probed directly against production |
| **Evidence** | Every FK pointing at `profiles(id)` now reads: `attempts` CASCADE · `daily_problem_counts` CASCADE · `events` **SET NULL** · `premium_waitlist` CASCADE · `refinement_loop_sessions` CASCADE · `section2_attempts` CASCADE · `skill_state` CASCADE · `streaks` CASCADE · `subscription_events` CASCADE · `user_achievements` CASCADE. **Zero `NO ACTION` remain.** |
| **Note** | `skill_state` (Stream A's `010_skill_graph.sql`) already cascades correctly, so the graph work did not reintroduce the defect. `events` is SET NULL by design — de-identified analytics survives, the person does not. |

### FLAG-007 — migration `014_revoke_client_writes.sql` — RESOLVED

| | |
|---|---|
| **Raised** | 2026-08-14 — four tables were writable from the browser with the public anon key: `daily_problem_counts` (reset the AI-tutor quota and spend the owner's Anthropic budget without limit), `streaks`, `user_achievements`, `subscription_events` (forge the billing audit log). |
| **Resolved** | 2026-08-16, probed directly against production |
| **Evidence** | `role_table_grants` → all four tables show `authenticated: SELECT` and **nothing at all for `anon`**. Surviving policies are read-only: `daily_counts_select_own`, `streaks_select_own`, `user_achievements_select`, `sub_events_select`. No INSERT/UPDATE policy remains on any of the four. |
| **Note** | Production's policy names differ from the file's (`daily_counts_select_own` vs the repo's `daily_counts_select`), so this was applied via an equivalent rewrite rather than the file verbatim. The end state matches what the migration intends; re-running the file would be a harmless no-op. |

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

- **2026-08-14** — THE OWED PROBE, RUN. Vercel MCP is back, so the debt from
  the two deploys below is settled: both production deployments are `READY`
  (`5f8e3c4` → `dpl_FYP8K71YAgKYnbSANmVWMBdFRYTA`, `6c2f25a` →
  `dpl_AkFqsExk7G6hEam3jG2bMmWRFeWA`, the current production). Flag probe:
  `GET /api/health/flags` → `anthropic_api_key: configured`,
  `migration_009_attempts_context: applied`,
  `migration_008_student_profiles: unknown` (unchanged, its own row above).
  Route check on the renumber that shipped in `5f8e3c4`:
  `/math/2/numbers-to-1000` serves the Grade 2 unit, 200, five lessons — the
  ministry labels are live on production. Flag state is verified again; the
  gap ran from `b113b96` to here.
- **2026-08-13** — Deploy `6c2f25a` pushed to main (grade 4 re-figured: the
  band's figure vocabulary extracted to scripts/primary/figures.py, lineGraph
  and clockFace renderers added, 80 figures across its 40 lessons, and
  `verify:figure-first` making the rule mechanical). POST-DEPLOY PROBE NOT
  RUN — the Vercel MCP server is DISCONNECTED for this session (it 502'd for
  ~15 min, then dropped entirely), and direct curl to prod is proxy-blocked
  by design. Confirmed instead: main is at `6c2f25a` via GitHub MCP, and
  Vercel auto-deploys main. NOTE ON THE PUSH: main had moved under us —
  PR #4 (problem bank Premium-gating) merged at `5038570` mid-session — so
  this went out as a REBASE onto it, never a force-push over someone else's
  work, with the whole gate re-run against the merged tree (709 tests, up
  from 669, because their tests came along). Content-only diff: no
  migrations, no auth or API surface, nothing depending on an open flag.
  OWED, NOW TWO DEPLOYS DEEP: probe `5f8e3c4` AND `6c2f25a` when the Vercel
  connection returns; flag state has been unverified since `b113b96`.
- **2026-08-13** — Deploy `5f8e3c4` pushed to main (primary band renumbered
  onto the ministry's grade labels + the redirect map that keeps old links
  working, real bar-chart/pictograph figures, the Baga curriculum as data
  and its 108-objective audit). POST-DEPLOY PROBE NOT RUN: the Vercel MCP
  transport returned Cloudflare 502s continuously for ~15 minutes
  (`zone: api.anthropic.com`, i.e. the gateway in front of the MCP server,
  not Vercel), and direct curl to prod is proxy-blocked by design, so
  neither the deployment state nor `/api/health/flags` could be read from
  this session. What IS confirmed: main is at `5f8e3c4` (GitHub MCP, which
  stayed up), Vercel auto-deploys main, and the full local gate was green
  including a route walk proving the redirects on a production build.
  Nothing in the diff touches migrations, auth or API surface, so no open
  flag was in its path. NEXT SESSION: run the probe for `5f8e3c4` and log
  it here — flag state is unverified since `b113b96` until then.
- **2026-08-13** — Probe after deploy `b113b96` (the ministry-strand gate:
  each ЭЕШ course's main topic is now checked against the strand А/492
  assigns its sections, with the three deliberate exceptions named in the
  test; plus the previous deploy's flag-log entry): `anthropic_api_key:
  configured`, `migration_009: applied`, `migration_008_student_profiles:
  unknown` (FLAG-002 unchanged — read that flag's "Reading a non-`applied`
  result" row before acting). FLAG-003 still optional/unset. Test- and
  docs-only diff: no user-visible surface, no migrations, no auth or API
  touched, nothing depended on either open flag; prod runtime errors clean
  over the 2h window.
- **2026-08-12** — Probe after deploy `a039c21` (the public ЭЕШ Study by
  Topic page rebuilt on the five-main-topic structure with measured exam
  weights; /practice hub grid grouped the same way): `anthropic_api_key:
  configured`, `migration_009: applied`, `migration_008: unknown`
  (FLAG-002 unchanged), FLAG-003 still optional/unset. Content-only, no
  migrations; prod runtime errors clean. Verified on prod HTML: 5 domain
  headers, 14 course links, no legacy leftovers. LESSON for future
  sessions: "restructure the topics section" touched THREE surfaces
  (/practice/esh/topics — the public one, /practice/esh/learn — auth-
  walled, /practice — auth-walled); the first pass hit only the walled
  one and the owner rightly reported the change missing. Enumerate every
  surface listing the same taxonomy BEFORE declaring a restructure done,
  and when work is finished but undeployed, say so in the FIRST line of
  the report, not the last.
- **2026-08-12** — Probe after deploy `c8b31a1` (the ЭЕШ learn hub re-cut
  onto five MAIN topics — the ministry's strands — with the 14 courses as
  their subtopics, and every past-paper/Premium question normalized to a
  canonical subtopic so it carries both marks): `anthropic_api_key:
  configured`, `migration_009: applied`, `migration_008_student_profiles:
  unknown` (FLAG-002 unchanged — `unknown`, so read that flag's "Reading a
  non-`applied` result" row before acting). FLAG-003 still optional/unset.
  No migrations in the diff, no auth or API surface touched, nothing
  depended on either open flag; prod runtime errors clean over the 2h
  window. Verified by fetching the shipped page chunk and confirming the
  domain-grouped renderers are in it, since both surfaces are client-only.
- **2026-08-12** — Probe after deploy `4c147d0` (three commits: the ЭЕШ hub
  aligned to the ministry curriculum А/492 with the standard checked in as
  data, Vectors & Matrices units 7-8 closing the last six CORE objective
  gaps, and an IM course-exam rebuild): `anthropic_api_key: configured`,
  `migration_009: applied`, `migration_008_student_profiles: unknown`
  (FLAG-002 unchanged — `unknown`, so read that flag's "Reading a
  non-`applied` result" row before acting). FLAG-003 still optional/unset.
  Content-only deploy — no migrations in the diff, no auth or API surface
  touched, nothing depended on either open flag; prod runtime errors clean
  over the 2h window. NOTE: `verify:exams` had been RED on main since
  `e9f7da9` — the IM2 papers did not cover the measurement unit that landed
  with it, while claiming in their own intro to span every unit. Caught in
  this deploy's pre-flight and fixed before shipping. The lesson is that a
  gate whose inputs are generated (banks -> exams) can go red from a change
  that never touches it, so pre-flight must run the WHOLE matrix, not the
  gates the diff appears to touch.
- **2026-08-11** — Probe after deploy `4a37fb8` (13 commits: the SAT hub
  rebuilt on the College Board's 20 official subtopics, its bank re-cut to
  match, the four CCSS coverage gaps closed in Integrated Math 1-3, and all
  three IM banks doubled to twelve forms per unit): `anthropic_api_key:
  configured`, `migration_009: applied`, `migration_008_student_profiles:
  unknown` (FLAG-002 unchanged — still `unknown`, so read that flag's
  "Reading a non-`applied` result" row before acting). FLAG-003 still
  optional/unset. Content, build-scripts and course wiring only: no
  migrations, auth, API, env or middleware files in the diff, so nothing
  depended on either open flag. Prod verified: `/practice/sat/learn` serves
  all four domains with the weightings and no SOON badges;
  `/practice/sat/bank` serves all twenty subtopics with per-unit counts
  matching the local build exactly (144, 144, 144, 144, 180, 144, 102, 133,
  144, 135, 102, 133, 144, 144, 100, 88, 88, 108, 130, 144 = 2,595); and
  `/math/integrated-2` serves nine units with the new Geometric Measurement
  & Modelling at 08 and Probability moved to 09. Runtime errors clean over
  the 1h window. Build 2m57s (166k lines of new content JSON — the
  type-check phase dominates), alias immediate.

- **2026-08-06** — Probe after deploys `3f1086a` and `fab8f8e` (the IB
  Applications & Interpretation SL course — 39 lessons across all five
  syllabus topics, 424 interactive steps, 291 problems and 1,163 sympy
  checks, plus the title fix below): `anthropic_api_key: configured`,
  `migration_009: applied`, `migration_008_student_profiles: unknown`
  (FLAG-002 unchanged — still `unknown`, so read that flag's "Reading a
  non-`applied` result" row before acting). FLAG-003 still optional/unset.
  Content, build-scripts and course wiring only: no migrations, auth, API,
  env or middleware files in the diff, so nothing depended on either open
  flag. Prod verified: `/math/ib-ai-sl` serves all five topics with Topic 1
  free and 2–5 Premium-locked, and
  `/math/ib-ai-sl/statistics-and-probability` serves all eleven lesson
  links. Runtime errors clean over the 3h window. Build 2m37s, alias
  immediate — no propagation lag this time, unlike the large-bank deploys.
  TWO DEPLOYS, deliberately: reading the prod HTML during verification
  caught two lesson titles containing `$...$`. Titles are interpolated as
  PLAIN TEXT by the course hub, the unit page and the catalog — none of
  them route a title through MathText — so students briefly saw
  "Hypothesis Tests: $\chi^2$ and $t$" verbatim. `fab8f8e` rewrote both
  titles as prose and added a verify:genmath rule rejecting any unit or
  lesson title containing a math delimiter. Lesson for the next reader:
  the render-safety checks all assume MathText is in the path; fields
  rendered raw need their own rule.

- **2026-08-05** — Probe after deploy `9115452` (the six-forms-per-unit
  expansion — 250 new problem-bank forms and ~7,600 new problems, taking
  every unit of all 25 banks to six collections; 894 → 1,144 forms and
  23,500 → 31,144 variants): `anthropic_api_key: configured`,
  `migration_009: applied`, `migration_008_student_profiles: unknown`
  (FLAG-002 unchanged — `unknown`, so read that flag's "Reading a
  non-`applied` result" row before acting). FLAG-003 still
  optional/unset. Content + build-script only: no migrations in the diff
  and no auth, API, env or component files touched, so nothing depended
  on either open flag. Prod verified: `/math/problem-bank/prob-stats`
  serves all twelve units at 72 problems each,
  `/math/problem-bank/geometry/surface-area-and-volume` — the unit that
  had ONE collection before this deploy — now serves all six with
  rendered math, and `/practice/ib/bank` reports SL 30 forms / 1,022
  problems and HL 30 forms / 1,013 problems. Runtime errors clean over
  the 3h window.
  NOTE for the next reader: `/math/problem-bank/ib-hl` and `/ib-sl`
  return a genuine 404 and always have — `build_problembank.py` sets
  `courseLadder: slug not in HUB_BANKS`, so the three hub banks (sat,
  ib-sl, ib-hl) live under their exam hubs instead. Not a regression.
  This deploy took 2m27s to build but ~10 min more in output
  propagation, consistent with the large-bank deploys before it.
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

## Resolved

### FLAG-004 — migration `010_skill_graph.sql` — RESOLVED 2026-08-14

Applied to production after Security's sign-off, together with the
`011_profiles_update_lockdown.sql` security fix (applied first, by priority).

Verified immediately after: `skills` / `skill_prerequisites` / `skill_state`
exist; `practice_sessions`, `session_answers` and `topic_progress` are gone
(all three re-checked at 0 rows by the migration's own runtime guard);
`attempts` carries `skill_id`, `confidence`, `session_kind`, `mode`; all 93
rows backfilled to `session_kind='practice_test'`, `mode='test'`, **0 rows
left NULL**; `skill_state` holds no INSERT/UPDATE/DELETE grant for `anon` or
`authenticated`, so it is server-write only as the architecture requires.

`topics` (13 rows) and `problems` (20 rows) were deliberately NOT dropped —
exported to `data/legacy-export/`, and `problems` still goes to Stream B.

Two security migrations landed alongside it, both applied and verified:
`016_profiles_update_lockdown.sql` (the free-premium hole) and
`017_client_write_lockdown.sql` (the same shape on `daily_problem_counts`
and `streaks`, plus TRUNCATE revoked from `anon`/`authenticated`
schema-wide). Neither leaves an open flag — there is nothing for the owner
to do. `011` is intentionally unused locally: it is reserved for Stream B's
`011_seed_esh_graph.sql`.
