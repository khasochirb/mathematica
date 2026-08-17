# Status — Design and structure

Owns routes, nav, migrations, schema. Never touches lesson/problem content.

Write **only this file**; read all four. Newest entry at the top. Format is
the template in `CLAUDE.md` § "End every session with this".

---

## 2026-08-16 09:43 UTC

**Did:** Problem bank made Premium-only and answer-first (commit, then check
— no solution shown before an answer); bank results feed the ratings card as
credit-only evidence, so a wrong answer never deducts; Phase 0 landed
(per-question timing wired, IB/AP/topic courses and grades 6–7 unpublished,
nav collapsed to ЭЕШ · SAT · Tutoring · About, five-tab contract enforced);
applied migrations `010_skill_graph`, `012_profiles_update_lockdown`,
`013_client_write_lockdown`; fixed the upgrade modal, which could not be
scrolled or closed.

**Landed where:** branch `claude/problem-bank-premium-design-osj7de`; the
bank + Phase 0 work merged to main via PR #4; `010`, `012`, `013` applied to
production and present in the ledger.

**Blocked on:** nothing. `011_seed_esh_graph.sql` has landed on main, so
item 5 (folding grades 8–12 into the ЭЕШ hub as foundation skills) is
unblocked and is the next piece of work.

**Others should know:**
- **Migration numbers 012 and 013 are double-booked.** This branch carries
  `012_profiles_update_lockdown.sql` and `013_client_write_lockdown.sql`;
  `origin/main` carries the security audit's `012_profiles_column_grants.sql`
  and `013_deletion_cascade.sql`. Both sets are already applied to
  production — the database is fine, the filenames are not. Mine get
  renumbered before this branch merges. Do not take 016 or 017.
- The `profiles` free-premium hole is closed: a student could set their own
  `subscription_status`. RLS gated the row, never the column; the fix was to
  revoke the privilege, not to write a better policy. Same shape was found
  and closed on `daily_problem_counts` (the AI quota, real money) and
  `streaks`. TRUNCATE is revoked from `anon` and `authenticated`
  schema-wide.
- `skill_state` is server-write only by construction: RLS on, select-own
  policy, no write policy at all.
- Tailwind's `content` globs now include `lib/`. They did not, and every
  Tailwind class in `lib/upgrade-modal-context.tsx` was silently purged. If
  you add a component outside `app/` or `components/`, check the globs.
- Known and unresolved, owner's call: `attempts` DELETE-own lets a student
  erase wrong answers (privacy right vs mastery integrity).
