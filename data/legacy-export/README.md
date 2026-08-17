# Legacy table export — pre-drop safety net

`topics-and-problems.json` is a full export of the two **non-empty** legacy
tables that Phase 0 plans to drop, taken from the production project
(`gsvfcnfbrzysaiiwgchf`) on 2026-08-14, **before** any drop was written or run.

| table | rows exported |
|---|---|
| `topics` | 13 |
| `problems` | 20 |

The export is validated on write: counts match, ids are unique, and every
problem's `topic_id` resolves inside the file — so it is self-contained and
can be re-seeded without the live database.

Reproduce with `export.sql` against the production project.

## Why this exists

`topics` and `problems` are **not empty**, and Supabase `list_tables` reported
`0` rows for both. Those are stale planner estimates and they were wrong — the
real `count(*)` is above. Anything destructive in this area must re-run a real
`count(*)` immediately beforehand rather than trusting table metadata.

## Status

- [x] Exported and committed (this file)
- [ ] `problems` handed to Stream B to check against the new skill graph
- [ ] Only then: drop `topics` and `problems`

`practice_sessions`, `session_answers` and `topic_progress` were verified at
**0 rows** and need no export.
