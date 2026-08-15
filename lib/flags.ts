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
  table: string;
  // A column the migration adds. Selecting it (HEAD, no rows) succeeds
  // once applied and fails with "column … does not exist" until then.
  column: string;
  /**
   * SEED migrations add no column, so the column probe cannot see them: 011
   * fills `skills` and `skill_prerequisites`, which both already existed and
   * were empty. For those the sentinel is a ROW COUNT instead — the table is
   * there either way, so "applied" means "has the rows it should".
   *
   * Still HEAD-only with `count: "exact"`: a number comes back, never a row,
   * so the endpoint stays safe to expose. `atLeast` rather than an exact
   * count because a later graph revision changes the total and this check
   * should keep answering "seeded", not go red on every re-author.
   */
  expectRows?: { atLeast: number; where?: { column: string; value: string } };
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
  {
    key: "migration_011_seed_esh_graph",
    migration: "011_seed_esh_graph.sql",
    table: "skills",
    column: "id",
    // 184 ЭЕШ skills ship in 011. The floor is deliberately well below that:
    // the question this answers is "did the seed run at all", and a graph
    // revision that merges two skills must not turn the flag red.
    expectRows: { atLeast: 150, where: { column: "hub", value: "esh" } },
  },
];

export type ProbeStatus = "applied" | "missing" | "unknown";

export interface ProbeResult {
  status: ProbeStatus;
  // The error's own code, carried through whenever the probe did not come
  // back clean. Always an enum — a SQLSTATE ("42703", "42P01") or a
  // PostgREST code ("PGRST204") — never a message, a value, or a row. This
  // is what turns an "unknown" from a shrug into something actionable: you
  // can tell "the service role can't see this table" (42501) from "no
  // network" without opening the dashboard.
  code?: string;
}

// Codes that mean the sentinel COLUMN is definitively absent, i.e. the
// migration has not taken effect. Two spellings, because PostgREST answers
// a HEAD select on a nonexistent column either from Postgres (SQLSTATE
// 42703) or from its own stale schema cache (PGRST204) depending on where
// the request dies — the original classifier only knew the first, which is
// why migration 008 read "unknown" on prod instead of a verdict.
const COLUMN_ABSENT = new Set(["42703", "PGRST204"]);

// Codes that mean the TABLE itself is unreachable. Deliberately NOT folded
// into "missing": every sentinel column is added by ALTER TABLE, so a
// vanished table is a much larger problem than an unapplied migration, and
// reporting it as "missing" would send the owner to the wrong runbook. It
// stays "unknown" — but the code rides along, so it is not a mystery.
const TABLE_ABSENT = new Set(["42P01", "PGRST205"]);

// Classify a PostgREST error from the sentinel select.
//   no error                       → the column exists → applied
//   42703 / PGRST204 / "does not exist" / "could not find the … column"
//                                  → the column is absent → missing
//   42P01 / PGRST205               → table unreachable → unknown (+code)
//   anything else                  → no env, network, auth → unknown (+code)
export function classifyProbe(error: { code?: string; message?: string } | null): ProbeResult {
  if (!error) return { status: "applied" };
  const code = error.code ?? "";
  const message = error.message ?? "";

  const columnAbsent =
    COLUMN_ABSENT.has(code) ||
    // PostgREST sometimes surfaces the prose without the code.
    /column .* does not exist/i.test(message) ||
    /could not find the '?[\w.]+'? column/i.test(message);
  if (columnAbsent && !TABLE_ABSENT.has(code)) return { status: "missing", code: code || undefined };

  return { status: "unknown", code: code || undefined };
}

// The states in which every flag is considered CLOSED. verify-flags.mjs
// exits non-zero unless each reported check equals its healthy value.
export const HEALTHY: Record<string, string> = {
  anthropic_api_key: "configured",
  migration_008_student_profiles: "applied",
  migration_009_attempts_context: "applied",
  migration_011_seed_esh_graph: "applied",
};

/**
 * Read a row-count probe. Separate from classifyProbe because the failure
 * modes differ: a column probe fails when the column is absent, a seed probe
 * succeeds structurally and still reports "missing" when the count is zero.
 * Splitting them keeps "the table isn't there" from being reported as "the
 * seed hasn't run", which would send Design to the wrong runbook.
 */
export function classifyRowProbe(
  error: { code?: string; message?: string } | null,
  count: number | null,
  atLeast: number,
): ProbeResult {
  if (error) return classifyProbe(error);
  if (count === null) return { status: "unknown", code: "no-count" };
  return count >= atLeast ? { status: "applied" } : { status: "missing" };
}
