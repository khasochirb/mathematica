export const dynamic = "force-dynamic";

import { NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import {
  MIGRATION_SENTINELS,
  classifyProbe,
  classifyRowProbe,
  type MigrationSentinel,
  type ProbeResult,
} from "@/lib/flags";

// Ops-flags health check — the mechanical half of memory/flags.md.
//
// Reports, as enums only (never values, never rows):
//   anthropic_api_key            "configured" | "missing"
//   migration_<nnn>_<name>       "applied" | "missing" | "unknown"
//
// Two sentinel shapes: DDL migrations probe for a COLUMN they add, seed
// migrations (011) probe for a ROW COUNT, because they add no column.
//
// plus a `details` map carrying the error CODE (an enum such as "42501" or
// "PGRST205") for any migration probe that did not come back "applied", so
// an "unknown" says why it could not decide instead of just shrugging.
//
// Why it exists: the two chronic ops flags (tutor key, migration 008) lived
// only in chat summaries and deploy-report reminders, so "is it still open?"
// was a memory. This endpoint makes it a GET — checkable by the owner with
// curl, by scripts/verify-flags.mjs, and by remote Claude sessions through
// the Vercel MCP web fetch (whose sandbox cannot reach prod directly).
//
// Safe to expose unauthenticated: whether the tutor is enabled is already
// observable (the tutor button returns a friendly 503), and whether an
// additive migration has run is schema metadata, not data. The migration
// probe uses HEAD so no table rows ever transit.

async function probeMigration(s: MigrationSentinel): Promise<ProbeResult> {
  const where = s.expectRows?.where;
  const site = {
    table: s.table,
    column: s.column,
    filter: where ? `${where.column}=${where.value}` : undefined,
  };
  try {
    const admin = createAdminClient();
    // Seed migrations add no column, so their sentinel counts ROWS instead.
    // Still HEAD-only — a count comes back, never a row.
    if (s.expectRows) {
      let q = admin.from(s.table).select(s.column, { head: true, count: "exact" });
      if (where) q = q.eq(where.column, where.value);
      const { error, count } = await q;
      const result = classifyRowProbe(error, count ?? null, s.expectRows.atLeast, site);

      // Only when the filtered count fell short: ask again without the
      // filter. "0 of 184 matched hub=eysh" and "the table is empty" are the
      // same verdict and completely different problems, and FLAG-010 is
      // exactly a case where the verdict was believed and the distinction
      // was never available. One extra HEAD, on the failure path only.
      if (result.status !== "applied" && where) {
        const { count: total, error: totalError } = await admin
          .from(s.table)
          .select(s.column, { head: true, count: "exact" });
        return {
          ...result,
          observed: {
            ...result.observed,
            unfilteredRowCount: totalError ? null : total ?? null,
          },
        };
      }
      return result;
    }
    const { error } = await admin.from(s.table).select(s.column, { head: true, count: "exact" });
    const result = classifyProbe(error);
    if (result.status === "applied") return result;
    return { ...result, observed: { ...result.observed, ...site } };
  } catch (err) {
    // No SUPABASE env in this environment (e.g. a bare local checkout) —
    // can't tell either way. The thrown message is carried too: "no-client"
    // alone cannot distinguish a missing env var from a malformed URL.
    return {
      status: "unknown",
      code: "no-client",
      observed: { ...site, message: err instanceof Error ? err.message : String(err) },
    };
  }
}

export async function GET() {
  // `checks` stays a flat string map: scripts/verify-flags.mjs compares its
  // values against HEALTHY directly, so the diagnostics go beside it rather
  // than inside it.
  const checks: Record<string, string> = {
    anthropic_api_key: process.env.ANTHROPIC_API_KEY ? "configured" : "missing",
  };
  // `details` used to be a flat key→code map. It is now key→object, because a
  // code alone could not explain FLAG-010: the endpoint said "missing" about a
  // table holding 184 rows and offered nothing to contradict it. Consumers
  // that only read `checks` (scripts/verify-flags.mjs) are unaffected — this
  // is why the diagnostics were kept beside `checks` and not inside it.
  const details: Record<string, Record<string, unknown>> = {};

  for (const s of MIGRATION_SENTINELS) {
    const result = await probeMigration(s);
    checks[s.key] = result.status;
    const entry: Record<string, unknown> = {};
    if (result.code) entry.code = result.code;
    if (result.observed) Object.assign(entry, result.observed);
    // An "applied" verdict needs no defence; anything else must show its
    // working, even if all it can say is which table it looked at.
    if (result.status !== "applied") {
      entry.migration = s.migration;
      if (Object.keys(entry).length > 0) details[s.key] = entry;
    } else if (Object.keys(entry).length > 0) {
      details[s.key] = entry;
    }
  }

  return NextResponse.json(
    { generatedAt: new Date().toISOString(), checks, details },
    { headers: { "Cache-Control": "no-store" } },
  );
}
