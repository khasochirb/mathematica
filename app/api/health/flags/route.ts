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
  try {
    const admin = createAdminClient();
    // Seed migrations add no column, so their sentinel counts ROWS instead.
    // Still HEAD-only — a count comes back, never a row.
    if (s.expectRows) {
      let q = admin.from(s.table).select(s.column, { head: true, count: "exact" });
      if (s.expectRows.where) {
        q = q.eq(s.expectRows.where.column, s.expectRows.where.value);
      }
      const { error, count } = await q;
      return classifyRowProbe(error, count ?? null, s.expectRows.atLeast);
    }
    const { error } = await admin.from(s.table).select(s.column, { head: true, count: "exact" });
    return classifyProbe(error);
  } catch {
    // No SUPABASE env in this environment (e.g. a bare local checkout) —
    // can't tell either way.
    return { status: "unknown", code: "no-client" };
  }
}

export async function GET() {
  // `checks` stays a flat string map: scripts/verify-flags.mjs compares its
  // values against HEALTHY directly, so the diagnostics go beside it rather
  // than inside it.
  const checks: Record<string, string> = {
    anthropic_api_key: process.env.ANTHROPIC_API_KEY ? "configured" : "missing",
  };
  const details: Record<string, string> = {};

  for (const s of MIGRATION_SENTINELS) {
    const result = await probeMigration(s);
    checks[s.key] = result.status;
    if (result.code) details[s.key] = result.code;
  }

  return NextResponse.json(
    { generatedAt: new Date().toISOString(), checks, details },
    { headers: { "Cache-Control": "no-store" } },
  );
}
