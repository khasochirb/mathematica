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
    key: "migration_010_skill_graph",
    migration: "010_skill_graph.sql",
    table: "attempts",
    column: "skill_id",
  },
  {
    key: "migration_011_seed_esh_graph",
    migration: "011_seed_esh_graph.sql",
    table: "skills",
    column: "id",
    // 184 ЭЕШ skills ship in 011. The floor is deliberately well below that:
    // the question this answers is "did the seed run at all", and a graph
    // revision that merges two skills must not turn the flag red.
    expectRows: { atLeast: 150, where: { column: "hub", value: "eysh" } },
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
  // WHAT THE PROBE ACTUALLY SAW, present on every non-"applied" result.
  //
  // FLAG-010 is why this exists. On 17 Aug the endpoint answered
  // `"migration_011_seed_esh_graph":"missing"` about a table holding 184
  // rows, and the response carried no code and no evidence — so the verdict
  // was indistinguishable from a true negative, and the obvious next action
  // was to re-apply a migration that had already run. A bare verdict that
  // can be wrong is worse than no verdict, because it is actionable in the
  // wrong direction.
  //
  // With this, one GET separates the three explanations that all collapse
  // into "missing": the probe saw zero rows, or it saw plenty but the floor
  // is set wrong, or the filter matched nothing while the table is full.
  observed?: ProbeObservation;
}

export interface ProbeObservation {
  /** Rows the probe counted through its filter. null = no count came back. */
  rowCount?: number | null;
  /** The same count with the filter dropped — distinguishes an empty table
   *  from a filter that matches nothing. Only taken when the filtered count
   *  fell short, so the healthy path stays one request. */
  unfilteredRowCount?: number | null;
  /** The floor `rowCount` was compared against. */
  expectedAtLeast?: number;
  /** Raw PostgREST/Postgres message, verbatim and untruncated. Schema prose
   *  only — these sentinels probe table and column names, never user data,
   *  which is the same reasoning that already makes this endpoint public. */
  message?: string;
  table?: string;
  column?: string;
  /** e.g. "hub=eysh", or absent when the probe is unfiltered. */
  filter?: string;
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
  // The raw message rides along on every non-applied verdict. Migration 008
  // has been answering "unknown" with NO code at all, which tells the reader
  // nothing they can act on; whatever PostgREST is actually saying there is
  // the fastest way to the cause.
  const observed = message ? { message } : undefined;
  if (columnAbsent && !TABLE_ABSENT.has(code)) {
    return { status: "missing", code: code || undefined, observed };
  }

  return { status: "unknown", code: code || undefined, observed };
}

// The states in which every flag is considered CLOSED. verify-flags.mjs
// exits non-zero unless each reported check equals its healthy value.
export const HEALTHY: Record<string, string> = {
  anthropic_api_key: "configured",
  migration_008_student_profiles: "applied",
  migration_009_attempts_context: "applied",
  migration_010_skill_graph: "applied",
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
  observed: ProbeObservation = {},
): ProbeResult {
  // PASS/FAIL LOGIC IS UNCHANGED — deliberately. The instruction was to make
  // the probe honest first and fix what it reports second, so this still
  // says "missing" in exactly the cases it said "missing" before. All that
  // is new is that it now shows its working.
  const evidence: ProbeObservation = {
    ...observed,
    rowCount: count,
    expectedAtLeast: atLeast,
  };
  if (error) {
    const result = classifyProbe(error);
    return { ...result, observed: { ...evidence, message: error.message } };
  }
  if (count === null) {
    return { status: "unknown", code: "no-count", observed: evidence };
  }
  if (count >= atLeast) return { status: "applied" };
  return { status: "missing", observed: evidence };
}
