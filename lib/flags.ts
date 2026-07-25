// Ops flags — external dependencies that only the owner can complete
// (dashboard secrets, database migrations, DNS, billing). The registry of
// open flags lives in memory/flags.md; the protocol in
// .claude/skills/ops-flags/SKILL.md. This module is the MECHANICAL half:
// the sentinels /api/health/flags probes so "is this flag still open?" is
// a request, not a memory.
//
// Pure — no env access, no supabase import. The route does the I/O; this
// file decides what to probe and how to read the result, so the reading
// can be unit-tested.

export interface MigrationSentinel {
  // Key in the health payload, e.g. "migration_008_student_profiles".
  key: string;
  // The migration file this stands in for (supabase/migrations/…).
  migration: string;
  // A column the migration adds. Selecting it (HEAD, no rows) succeeds
  // once applied and fails with "column … does not exist" until then.
  table: string;
  column: string;
}

// One sentinel per migration whose applied-state has ever been in doubt.
// Append when a new migration ships; never remove — a green check on an
// old migration costs one HEAD request and keeps the ledger honest.
export const MIGRATION_SENTINELS: MigrationSentinel[] = [
  {
    key: "migration_008_student_profiles",
    migration: "008_student_profiles.sql",
    table: "profiles",
    column: "grade",
  },
  {
    key: "migration_009_attempts_context",
    migration: "009_attempts_context.sql",
    table: "attempts",
    column: "context",
  },
];

export type ProbeStatus = "applied" | "missing" | "unknown";

// Classify a PostgREST error from the sentinel select.
//   no error            → the column exists → migration applied
//   42703 / "does not exist" → the column is absent → migration missing
//   anything else       → can't tell (no env, network, auth) → unknown
export function classifyProbe(error: { code?: string; message?: string } | null): ProbeStatus {
  if (!error) return "applied";
  const code = error.code ?? "";
  const message = error.message ?? "";
  if (code === "42703" || /column .* does not exist/i.test(message)) return "missing";
  return "unknown";
}

// The states in which every flag is considered CLOSED. verify-flags.mjs
// exits non-zero unless each reported check equals its healthy value.
export const HEALTHY: Record<string, string> = {
  anthropic_api_key: "configured",
  migration_008_student_profiles: "applied",
  migration_009_attempts_context: "applied",
};
