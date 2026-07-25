---
name: ops-flags
description: >
  Protocol for external dependencies only the owner can complete —
  dashboard secrets, database migrations, DNS, billing. Read when adding
  a migration or a feature that needs a secret, when a deploy report
  must list open flags, when asked about the AI-tutor key or migration
  state, or when closing a flag. Registry: memory/flags.md. Mechanical
  check: /api/health/flags via npm run verify:flags.
---

# Ops Flags — Operating Manual & Protocol

How this project handles **external dependencies only the owner can
complete**: dashboard secrets, database migrations, DNS, billing,
third-party console actions. These cannot be finished from a coding
session, so without a protocol they rot as "owner reminders" repeated at
the end of every summary — which is exactly what happened to the AI-tutor
key and migration 008 for months. This skill exists so that never happens
again.

## Definitions

- **Flag**: a named, tracked external dependency with a graceful-
  degradation story, an owner runbook, and a mechanical verification.
- **Registry**: `memory/flags.md` — the single source of truth. A flag
  that exists only in chat, a commit message, or a deploy report does
  not exist.
- **Probe**: the mechanical check that decides a flag's state. For this
  project: `GET /api/health/flags` (secretless enums), consumed by
  `npm run verify:flags` and readable from remote Claude sessions via
  the Vercel MCP web fetch (the sandbox proxy blocks direct egress to
  prod — never assume curl can reach production).

## The five rules

1. **Ship dark, never broken.** Any feature behind a flag must degrade
   gracefully with the dependency absent: a friendly 503, a null
   fallback, a hidden entry point. The degradation path is part of the
   feature's definition of done and is verified in code, not assumed.
   (Reference implementations: `app/api/tutor/route.ts` checks the key
   *before* auth so the degraded state is even probeable from outside;
   `app/api/auth/me` reads `select("*")` so absent columns become null.)
2. **Every flag gets a probe on the day it is raised.** Add a sentinel
   to `lib/flags.ts` (migrations: a column the migration adds; secrets:
   an env presence check) and its healthy value to `HEALTHY` in both
   `lib/flags.ts` and `scripts/verify-flags.mjs`. If a flag cannot be
   probed mechanically, say so in the registry entry and state the best
   manual probe — but treat that as a defect to fix.
3. **Every flag gets a runbook the owner can execute in minutes.**
   Exact click-path, exact SQL (idempotent, pasted inline or pointed at
   the migration file), the verification command, and what output means
   done. The owner should never have to reconstruct context.
4. **Closed means the probe passed.** A flag moves to Resolved only
   with the date and the probe output pasted in. "It was set" is not
   evidence.
5. **Open flags surface at every deploy.** The release-deploy pre-flight
   reads the registry; the deploy report lists open flags and, when a
   shipped change *depends* on one, states the sequencing (e.g.
   "migration first, verified, then code deploy" — see release-deploy
   §Database changes).

## Lifecycle

```
RAISE ──► TRACK ──► SURFACE ──► VERIFY ──► CLOSE
```

- **RAISE** — the moment code that needs an external dependency is
  written: add the registry entry (what's dormant, degradation evidence,
  runbook, verify command) and the probe sentinel, in the same commit
  as the feature.
- **TRACK** — the entry lives under OPEN in `memory/flags.md`. Believed-
  but-unproven states go under WATCH (e.g. a migration applied
  out-of-band) until the probe confirms them.
- **SURFACE** — deploy reports and session wrap-ups link the registry
  instead of restating reminders. One line: "open flags: FLAG-001,
  FLAG-002 (memory/flags.md)".
- **VERIFY** — `npm run verify:flags -- <base-url>` (owner machine or
  CI), or fetch `/api/health/flags` through the Vercel MCP from a cloud
  session. Migrations can additionally be confirmed with the
  information_schema query in the runbook.
- **CLOSE** — move the entry to Resolved with date + evidence. Keep the
  sentinel in `lib/flags.ts` forever: a green check on an old flag costs
  one HEAD request and keeps the ledger honest.

## Migrations, specifically

- Migrations do NOT auto-apply on deploy (release-deploy §Database
  changes). Every new file in `supabase/migrations/` therefore raises a
  flag automatically — same commit, per rule 2, with a sentinel column.
- Write migrations idempotent (`IF NOT EXISTS`, guarded updates) so the
  runbook is always "paste the whole file, run, run again if unsure".
- Purely additive migrations (new nullable columns, new tables with
  RLS) may ship dark ahead of application. Anything destructive or
  behavior-changing must be sequenced: applied and verified BEFORE the
  dependent code deploys.
- Snapshot first for anything risky: `scripts/backup-prod.sh`.

## Secrets, specifically

- Never ask the owner to paste a secret into chat, a commit, or a file
  in the repo. The runbook points at the provider console (create) and
  the Vercel dashboard (store, marked Sensitive).
- Vercel env changes take effect on the NEXT deployment — the runbook
  must say so, or the owner will verify too early and read a false
  "still missing".
- The probe checks *presence*, never value: `Boolean(process.env.X)`
  server-side, surfaced as an enum.

## Current state

See `memory/flags.md`. As of 2026-07-25: FLAG-001 (tutor key) and
FLAG-002 (migration 008) OPEN with runbooks; migration 009 under WATCH.
