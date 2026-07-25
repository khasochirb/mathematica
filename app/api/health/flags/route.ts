export const dynamic = "force-dynamic";

import { NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import { MIGRATION_SENTINELS, classifyProbe, type ProbeStatus } from "@/lib/flags";

// Ops-flags health check — the mechanical half of memory/flags.md.
//
// Reports, as enums only (never values, never rows):
//   anthropic_api_key            "configured" | "missing"
//   migration_<nnn>_<name>       "applied" | "missing" | "unknown"
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

async function probeMigration(table: string, column: string): Promise<ProbeStatus> {
  try {
    const admin = createAdminClient();
    const { error } = await admin.from(table).select(column, { head: true, count: "exact" });
    return classifyProbe(error);
  } catch {
    // No SUPABASE env in this environment (e.g. a bare local checkout) —
    // can't tell either way.
    return "unknown";
  }
}

export async function GET() {
  const checks: Record<string, string> = {
    anthropic_api_key: process.env.ANTHROPIC_API_KEY ? "configured" : "missing",
  };

  for (const s of MIGRATION_SENTINELS) {
    checks[s.key] = await probeMigration(s.table, s.column);
  }

  return NextResponse.json(
    { generatedAt: new Date().toISOString(), checks },
    { headers: { "Cache-Control": "no-store" } },
  );
}
