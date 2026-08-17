# Migration numbering — read before you add one

Migrations are applied through the Supabase MCP, in filename order, by the
one chat that owns applying them (see THE DATABASE RULE in `CLAUDE.md`).
Filename order is the only ordering anyone has, which makes a duplicate
number genuinely dangerous: an operator working down the list sees two files
starting `011_` and applies one of them.

## There IS a ledger, and it does not record file numbers

```sql
select version, name from supabase_migrations.schema_migrations order by version;
```

Two things about it that matter here:

- It records only what was applied **through the MCP**. Anything pasted into
  the dashboard SQL editor by hand never reaches it, so `000`–`009` are
  largely absent and their absence is **not** evidence they never ran.
- It stores the migration's **name**, not its file number — `deletion_cascade`,
  not `013_deletion_cascade`. That is why renumbering a file prefix does not
  desync the ledger, and it is the real reason renaming an already-applied
  migration is safe in this repo.

For numbering specifically the ledger is the wrong tool; use
`git ls-tree --name-only origin/main supabase/migrations/`.

## This has already happened twice

Parallel sessions in August 2026 minted the same numbers twice over:

| number | file | stream | resolution |
|---|---|---|---|
| 010 | `010_skill_graph.sql` | design — creates `skills`, `skill_prerequisites`, `skill_state` | kept 010 |
| 010 | `010_profiles_column_grants.sql` | security audit | → `012_` |
| 011 | `011_seed_esh_graph.sql` | content — seeds the ЭЕШ graph | kept 011 |
| 011 | `011_deletion_cascade.sql` | security audit | → `013_` |
| 012 | `012_profiles_update_lockdown.sql` | design | → `016_` |
| 013 | `013_client_write_lockdown.sql` | design | → `017_` |

The security audit's four files moved to `012`–`015` on 2026-08-16; design's
two moved to `016`–`017` on 2026-08-17. Three of the audit's
(`013_deletion_cascade`, `014_revoke_client_writes`, and design's pair) were
already applied to production **under their old numbers** — harmless, per the
ledger note above. The end state was verified by probing production directly
rather than inferred; see the Resolved entries in `memory/flags.md`.

The 012/013 pair is worth reading twice: two chats independently wrote a
profiles lockdown and a client-write lockdown, gave them the same two
numbers, and applied both. `client_write_lockdown` and `revoke_client_writes`
landed **eight minutes apart** (ledger versions `20260815111017` and
`20260815111825`). The database survived because both were idempotent and
converged on the same end state. That was luck, not design.

## The rule

**Claim your number against `origin/main` at the moment you create the file,
and re-check before you merge** — a long-lived branch is exactly where this
goes wrong. If someone took your number while you were working, rename yours:
the file, the `-- NNN:` header line inside it, and every reference in
`memory/flags.md`, `docs/`, and code comments.

If a real migration runner is ever adopted (`supabase db push`, a
filename-keyed ledger), this rule inverts and applied files become immutable.
