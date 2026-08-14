# Pre-drop archive — legacy v1 practice tables (2026-08-14)

Snapshot of the two **non-empty** tables in the five-table drop set, taken
from production (`mongolpotential`, project `gsvfcnfbrzysaiiwgchf`)
immediately before the drop migration.

## Why this exists

Supabase `list_tables` reported all five drop candidates as **0 rows**.
That was wrong. `topics` held 13 rows and `problems` held 20.

The cause: these tables have never been vacuumed or analyzed, so
`pg_class.reltuples = -1` and `pg_stat_user_tables.n_live_tup = 0`. Any
tool that reads those statistics — including `list_tables` — reports an
empty table. **Planner estimates are not evidence for destructive
decisions.** Only `count(*)` is.

Verified `count(*)` at archive time:

| table | real `count(*)` | planner estimate | `n_live_tup` |
|---|---|---|---|
| practice_sessions | 0 | -1 | 0 |
| session_answers | 0 | -1 | 0 |
| topic_progress | 0 | -1 | 0 |
| **topics** | **13** | -1 | 0 |
| **problems** | **20** | -1 | 0 |

## Integrity

The export is checksum-verified against production, not eyeballed.

| file | rows | md5 (see below) |
|---|---|---|
| `topics.json` | 13 | `c4c749085bbf83ad8966a2d1950c8d90` |
| `problems.json` | 20 | `a650dd61d5ee2e614cac6fb113fef13b` |

Checksums are over pipe-joined significant fields, sorted by `id::text`:

- topics: `id|name|slug|parent_id(or '-')|display_order`
- problems: `id|topic_id|difficulty|answer_type|correct_answer|question`

Reproduce in the database:

```sql
select md5(string_agg(id::text||'|'||name||'|'||slug||'|'||
       coalesce(parent_id::text,'-')||'|'||display_order, E'\n' order by id::text))
from public.topics;

select md5(string_agg(id::text||'|'||topic_id::text||'|'||difficulty||'|'||
       answer_type||'|'||correct_answer||'|'||question, E'\n' order by id::text))
from public.problems;
```

## What this data is

The original April 2026 seed content for the v1 adaptive-practice
prototype: a 5-parent / 8-child topic taxonomy and 20 Mongolian maths
problems with answers, hints and explanations. All rows share
`created_at = 2026-04-08T09:51:22.827982+00`, i.e. a single seed insert.

It is **not** the content the live site serves. Current content is served
from JSON/TS in the repo (`data/`, `lib/genmath-data/`, `lib/esh-*`), and
`problems.correct_answer` here is the answer key for the retired
prototype only.

`data/learn/topics.json` is a different, unrelated dataset (a formula and
study-guide reference keyed by slug, no UUIDs) — it is not an export of
this table and does not supersede this archive.

## Schema

DDL is already preserved in git: `supabase/migrations/001_initial_schema.sql`
(`topics` at line 6, `problems` at line 16). No schema is captured here.

## Restoring

Re-create the tables from `001_initial_schema.sql`, then insert these
rows. Insert `topics` before `problems` (FK `problems.topic_id → topics.id`),
and within `topics` insert the five `a0000000-…` parents before the eight
`b0000000-…` children (self-FK `topics.parent_id → topics.id`).
