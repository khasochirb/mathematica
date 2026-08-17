# Migration numbering — read before you add one

Migrations here are applied **by hand** in the Supabase dashboard, in
filename order. There is no ledger table recording what ran, so the
filenames are the only ordering anyone has. That makes a duplicate number
genuinely dangerous: an operator working down the list sees two files
starting `011_` and applies one of them.

## This has already happened once

Three sessions worked in parallel in August 2026 and two of them minted the
same numbers:

| number | file | stream |
|---|---|---|
| 010 | `010_skill_graph.sql` | Stream A (branch `claude/problem-bank-premium-design-osj7de`) — creates `skills`, `skill_prerequisites`, `skill_state` |
| 010 | `010_profiles_column_grants.sql` | security audit — **renamed to `012_`** |
| 011 | `011_seed_esh_graph.sql` | design/content — seeds the ЭЕШ graph |
| 011 | `011_deletion_cascade.sql` | security audit — **renamed to `013_`** |

The security audit's four files were renumbered to `012`–`015` on 2026-08-16
to clear the collision. Two of them (`012`, `013`, `014`) were already applied
to production **under their old numbers**; the rename changes the repo's
record, not the database. The end state was verified directly against
production rather than inferred — see the Resolved entries in
`memory/flags.md` for the probe output.

Note also that `010_skill_graph.sql` is applied on production but its **file
is not on `main`** — it lives on Stream A's branch. `011_seed_esh_graph.sql`
depends on it. Do not conclude from `ls` that 010 is missing from the
database.

## The rule

**Claim your number against `origin/main` at the moment you create the file,
and if you are working on a long-lived branch, re-check before you merge.**
`git ls-tree --name-only origin/main supabase/migrations/` is the check.
If someone took your number while you were working, rename yours — including
the `-- NNN:` header line inside the file and every reference to it in
`memory/flags.md`, `docs/`, and code comments.

Renaming an already-applied migration is acceptable *here* precisely because
the database has no filename-keyed ledger. If that ever changes — a real
migration runner, `supabase db push`, a `schema_migrations` table — this rule
inverts and applied files must become immutable.
