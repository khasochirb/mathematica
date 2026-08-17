# Status — Website security audit

Owns RLS specs, policy review, audits. Never applies migrations (see THE
DATABASE RULE in `CLAUDE.md`) and never touches app logic.

Write **only this file**; read all four. Newest entry at the top. Format is
the template in `CLAUDE.md` § "End every session with this".

---

## 2026-08-17 04:07 UTC

**Did:** Moved attempt deletion behind the server (`POST /api/attempts/erase`
— client names a scope, server derives the row filter) and applied
`015_attempts_server_delete`, which drops `attempts_delete_own` and revokes
the grant; built account deletion (`POST /api/account/delete`) with a
post-delete residual sweep over all 11 user-scoped tables; renumbered this
stream's migrations out of the 010/011 collision into 012–015 and wrote
`supabase/migrations/NUMBERING.md`; probed every grant and policy in the
public schema against production and rebuilt `memory/flags.md` on evidence.

**Landed where:** branch `claude/website-security-audit-qb8ceu`, merged to
main and deployed twice at the owner's request (`3c1dd9b`, then `02aeedd`).
`015_attempts_server_delete` applied to production and in the ledger
(`20260816060028`).

**Blocked on:** nothing. Owner owes FLAG-009 (`ADMIN_DELETION_KEY`).

**Others should know:**

- **I crossed two lanes, on the owner's explicit instruction, and you should
  know rather than discover it.** I applied a migration (THE DATABASE RULE
  says only Design does that) and I wrote app logic (two API routes plus a
  settings panel). The owner asked for both directly, in those words. Flagging
  it per rule 2 — `attempts_server_delete` in the ledger is a teammate, not
  drift. If the rule should hold even against a direct owner instruction, say
  so and I will hand migrations over instead.

- **Design: your "known and unresolved, owner's call" item is closed.**
  `attempts` DELETE-own is gone. The resolution was not to remove the
  student's right to erase, but to take the *filter* away from the client: the
  browser could write `.eq("is_correct", false)` and delete only its wrong
  answers, which is a mastery-integrity hole, not a privacy feature. The route
  accepts a scope NAME only and applies it whole. Privacy right kept,
  curation removed.

- **Design: your `012`/`013` renumbering plan works, and I stayed off 016/017.**
  This stream now owns `012_profiles_column_grants`, `013_deletion_cascade`,
  `014_revoke_client_writes`, `015_attempts_server_delete`. Highest number
  taken is 015.

- **Design: `012_profiles_column_grants.sql` was never applied and is now
  redundant — your `profiles_update_lockdown` did that job, and did it
  harder.** Production has NO update grant on `profiles` at any column; my
  file would grant three (`username`, `display_name`, `avatar_url`). The
  registry records the discrepancy rather than pretending they match. Your
  call whether to delete my file or keep it as documentation — but note the
  live consequence: `profiles_update_own` still exists as a policy with no
  grant behind it. Inert today, and exactly the shape rule 4 warns about if
  someone re-grants later.

- **QA: there is a new build gate.**
  `scripts/verify-account-delete-inventory.test.ts` parses the migrations and
  fails if one adds a table referencing `profiles(id)` that is not in
  `SERVER_USER_TABLES` (`lib/data-erase.ts`). Deletion can only verify what it
  knows to look at, so a missing table means an erasure request silently skips
  it. If your migration trips this, add the table to the list — do not weaken
  the test.

- **Everyone: three legacy tables are in the repo but not in the database.**
  `practice_sessions`, `session_answers` and `topic_progress` are still
  created by migration 001 and were dropped from production out-of-band.
  Consequence beyond deletion: `/api/answers`, `/api/sessions`,
  `/api/progress` and `/api/problems/next` all reference them and are
  **already broken against production**. There is no DROP migration, so the
  schema is not reproducible from scratch past that point. Design owns routes
  and schema, so this is yours; I recorded it in `LEGACY_DROPPED_TABLES` and
  the spec rather than writing a destructive DROP unasked.

- **Everyone: four tables still carry Supabase's default `GRANT ALL` for both
  `anon` and `authenticated`** — `section2_attempts`,
  `refinement_loop_sessions`, `events`, `premium_waitlist`. Nothing is
  reachable today (no policies behind those verbs; `events` and
  `premium_waitlist` have no policies at all), but it is the correct-by-
  accident shape. One is sharper: `refinement_loop_sessions` has a live
  `UPDATE` policy `TO public` *and* the grant, so a student can rewrite their
  own loop rows from the browser right now, and those progress columns feed
  mastery. Migration 007 made the table mutable deliberately, so this wants a
  decision, not a reflex. Details in the WATCH entry of `memory/flags.md`.

- **Everyone: `memory/flags.md` was rebuilt against production, not memory.**
  Four flags moved to Resolved with probe output pasted in (012 grants, 013
  cascade, 014 client writes, 015 attempts delete). If you are about to report
  one of these as outstanding, re-probe first — the registry had been stale in
  both directions.
