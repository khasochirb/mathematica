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

### FLAG-011 — migration `018_contact_messages.sql` not applied (LEAD LOSS)

| | |
|---|---|
| **Raised** | 2026-08-17, Build |
| **Status** | **OPEN — blocking the contact form** |
| **What** | `018_contact_messages.sql` creates the table the contact form now writes to. It is written, gated and committed, but **not applied**: `apply_migration` through the Supabase MCP returns `MCP tool call requires approval`, and this session is non-interactive so no prompt can reach the owner. |
| **Owner action** | Grant MCP approval (claude.ai connector settings, or `/mcp` in an interactive session) so Build can apply it — Build owns migrations per CLAUDE.md. Applying it by hand in the dashboard also works but skips the ledger; prefer the MCP. |
| **Until then** | **Do not deploy the contact-form wiring.** With the table absent the route returns 500 and the form shows "Could not send your message. Please email or call us instead." That is honest — and strictly better than the silent discard it replaces — but it is a visibly broken form. The two ship together or not at all. |
| **Verify** | `select count(*) from contact_messages;` succeeds (0 rows is correct), and the migration's own post-conditions ran: 10 columns, RLS enabled, no `anon`/`authenticated` grants. |
| **Notes** | Row holds a sender's name, email and message body, so `user_id` CASCADEs on account deletion and the table is registered in `SERVER_USER_TABLES` (`lib/data-erase.ts`). The security stream's `verify-account-delete-inventory` gate caught the first draft, which used `SET NULL` and would have left the personal data behind after an erase. |

### FLAG-009 — `ADMIN_DELETION_KEY` not set in Vercel (PRIVACY)

| | |
|---|---|
| **Raised** | 2026-08-16, with the account-deletion route |
| **What it unlocks** | The **guardian path** on `POST /api/account/delete`. With the key set, the owner can delete a student's account on a parent's request by sending `x-admin-deletion-key` plus `{ userId, confirm: "DELETE" }`. Without it that path returns 503 and only the student's own password-authenticated deletion works. |
| **Why it matters before September** | The intake is minors with guardians. A parent asking for their child's data to be erased will usually not have the student's password, and teacher-provisioned accounts make that more likely, not less. Self-service deletion alone does not make a deletion request honourable on demand. |
| **Ships dark?** | Yes, and fail-closed: with the variable unset the admin path does not exist rather than degrading to something weaker. Self-service deletion is unaffected. |
| **Owner action** | ~2 min: Vercel → imathhub → Settings → Environment Variables → add `ADMIN_DELETION_KEY` = a long random string (`openssl rand -hex 32`), Production, Sensitive. Redeploy. |
| **Do NOT reuse `ADMIN_ACTIVATION_KEY`** | Different power, different blast radius. Activation grants a subscription; this one erases a child's academic record irreversibly. One key for both means anyone who can do the harmless thing can do the unrecoverable one. |
| **Verify** | `curl -s -o /dev/null -w '%{http_code}' -X POST https://www.mongolpotential.com/api/account/delete -H 'content-type: application/json' -H 'x-admin-deletion-key: wrong' -d '{"confirm":"DELETE","userId":"00000000-0000-0000-0000-000000000000"}'` → **401** = key set (path armed, wrong key rejected) · **503** = unset (self-service only). Note both are safe to run: neither deletes anything. |

---

### FLAG-010 — `/api/health/flags` reports a FALSE `missing` for 011

| | |
|---|---|
| **Raised** | 2026-08-17, immediately after seeding 011 |
| **Priority** | MEDIUM — nothing user-facing, but a lying probe is worse than no probe. The next session to read this endpoint will conclude the ЭЕШ graph is unseeded and may re-apply it. The re-run is safe (upserts, never deletes) but the wrong conclusion is not. |
| **Symptom** | `skills` holds 184 rows with `hub='eysh'`; the sentinel wants ≥150; the endpoint answers `missing` with an EMPTY `details` map, so it is not even reporting a code. |
| **Ruled out on the database side** | Row count 184 (as superuser AND under `set role` for `service_role`, `anon` and `authenticated` — all three read it). RLS on with a permissive `skills_select_all` SELECT policy. `service_role` has SELECT and `rolbypassrls=true`. No duplicate `skills` table in another schema. `notify pgrst, 'reload schema'` issued; no change. The deployed build is `a532ae4` and its `lib/flags.ts` carries the right sentinel (`table: skills`, `column: id`, `where hub='eysh'`, `atLeast: 150`) — its sibling `migration_010_skill_graph` sentinel only exists in that build and reports `applied`, which also proves the app is pointed at THIS project. |
| **Also unexplained, same shape** | `migration_008_student_profiles` reports `unknown` with no code. Per `classifyProbe` that means an error object with a falsy `code` and a message matching none of the patterns. Both failing probes are on `profiles`/`skills`; both passing ones are on `attempts`. That split is the strongest lead. |
| **Why it was not diagnosed further** | The exact PostgREST call could not be reproduced from a Claude cloud session: the sandbox proxy answers 403 to CONNECT for both `www.mongolpotential.com` and `*.supabase.co`, so the only view of the probe is its own verdict. |
| **Next step** | Make the probe honest before making it right: have the route put the observed count (and the raw PostgREST `message`, not just `code`) into `details` for any non-`applied` result. One small change to `app/api/health/flags/route.ts`; the answer will be in the next response. |

### FLAG-004 — `011_seed_esh_graph.sql` APPLIED 2026-08-17 — probe disagrees, see FLAG-010

| | |
|---|---|
| **Raised** | 2026-08-15 |
| **Owner action** | DONE. Applied to production 2026-08-17 by Design (THE DATABASE RULE), on the owner's instruction. |
| **Verified by row count, not by the file existing** | `select count(*) from skills` → **184**; `select count(*) from skill_prerequisites` → **367**. Also checked beyond the counts, because the SQL had to be retyped through a tool parameter and a mistyped weight would seed a wrong graph silently: `md5(string_agg(id order by id))` = `332919b9f7c0bee9c5875547aba1eddc` and `md5(string_agg(skill_id||'>'||requires_id order by skill_id, requires_id))` = `58cdc43a41defba848a7fd37346aff2a`, both matching the same hashes computed from the file on disk. `sum(exam_weight)`=99.8983, `sum(strength)`=316.4, `sum(typical_difficulty)`=505, `sum(display_order)`=5257 — all matching. 0 dangling edges, 0 self-edges, 0 rows with `hub<>'eysh'`, `name_mn` NULL on all 184 (Phase 3 writes it). The file's own post-conditions ran and did not raise. `skill_state` was empty before and after, so no learner state was at risk. |
| **What it seeds** | 184 ЭЕШ skills + 367 prerequisite edges into `skills` and `skill_prerequisites`. Both tables already exist and were empty (owner-confirmed 2026-08-15). |
| **Blocks** | Everything downstream of the graph — adaptive placement, recommendations, mastery, score prediction. Design is blocked on it now. |
| **Ships dark?** | Yes. Nothing in the app reads `skills` yet, so an unapplied migration changes no behaviour; it just leaves the graph invisible to other agents. |
| **Sentinel** | `migration_011_seed_esh_graph` in `lib/flags.ts`. This is the first ROW-COUNT sentinel: 011 adds no column, so the usual column probe would report "applied" against an empty table. It counts `skills` rows with `hub='eysh'` and wants ≥150 (184 ship; the floor sits low so a later graph revision does not turn it red). |
| **Verify** | ⚠️ The endpoint still answers `"migration_011_seed_esh_graph":"missing"` after the seed. That is a PROBE defect, not an unapplied migration — see FLAG-010. Trust the row counts above; per CLAUDE.md rule 1 the count is the verification, and re-running the seed on the strength of the endpoint would be acting on a false negative. |
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

Probed 2026-08-16, **re-checked after `015` was applied the same day.**
`section2_attempts`, `refinement_loop_sessions`, `events` and
`premium_waitlist` still grant
`DELETE, INSERT, REFERENCES, SELECT, TRIGGER, UPDATE` to **both** `anon` and
`authenticated` — Supabase's default `GRANT ALL ON ALL TABLES`.
(`attempts` was the fifth; `015` narrowed it to `INSERT, SELECT` for
`authenticated` and nothing for `anon`, so it is off this list.)

Nothing here is exploitable today: `events` and `premium_waitlist` have zero
policies (RLS fail-closed), and the verbs with no matching policy are
default-denied on the others. But this is exactly the "correct by accident"
shape §0 of `docs/security/data-access-model.md` warns about — one future
`CREATE POLICY ... FOR UPDATE` silently opens a write path, because the grant
behind it was never narrowed. `015` is the template; the other four want the
same treatment in a follow-up migration.

One of the four is more than theoretical. `refinement_loop_sessions` has a
live `UPDATE` policy `TO public` (`refinement_loops_update_own`) **and** the
update grant, so a student can rewrite their own loop rows directly from the
browser today. Migration 007 made that table mutable by design and the API
route drives the state machine, so this is not a hole in the same sense as the
others — but the loop's progress columns feed mastery, which puts it on the
wrong side of Rule 2. Worth deciding deliberately rather than inheriting.

Also noted: every policy on `attempts`, `section2_attempts`,
`refinement_loop_sessions`, `subscription_events` and `user_achievements` is
still `TO public` rather than `TO authenticated`. Safe only because
`auth.uid()` is NULL for `anon` and `NULL = user_id` is NULL — correct, but by
accident rather than by statement.

---

## RESOLVED

*(move entries here with date + verification evidence; never delete)*

### FLAG-008 — migration `015_attempts_server_delete.sql` — RESOLVED

| | |
|---|---|
| **Raised** | 2026-08-14 — a grade-integrity hole. `attempts` carried `attempts_delete_own` plus the default `GRANT ALL`, so the browser deleted rows itself over PostgREST with the student's own JWT and **wrote its own filter**. `delete().eq("user_id", me).eq("is_correct", false)` removes only the wrong answers, leaving a perfect record and inflating accuracy, mastery, the weakness model, the ratings card and the predicted grade. |
| **Resolved** | 2026-08-16, applied and probed against production |
| **Sequencing honoured** | The deploy went first, as required. Production was confirmed to be serving the build containing the replacement route — `GET /api/attempts/erase` returned **405 Method Not Allowed** (route present, POST-only; a missing route would 404) on deployment `dpl_9KsdJYeD6C87QiBwTjpmsSD6eXMB`, main @ `3c1dd9b`, state READY — and only then was the migration applied. |
| **Evidence** | Grants: `authenticated` → **`INSERT, SELECT`** and `anon` → **no row at all**. Policies on `attempts`: `attempts_insert_own` (INSERT), `attempts_select_own` (SELECT) — `attempts_delete_own` is gone. Both locks are in place: the policy is dropped so RLS default-denies DELETE, and the grant is revoked so a future permissive policy cannot re-open it alone. |
| **Replacement** | `POST /api/attempts/erase` — takes a scope NAME, derives the predicate server-side, applies it with `user_id` = the JWT subject, then re-counts and refuses to report success on a non-zero residual. |

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
