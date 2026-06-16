// Refinement-loop session persistence (Phase 3c).
//
// GET  /api/refinement-loop            → the caller's active loop (completed_at
//                                        IS NULL, most recent) or { data: null }.
// POST /api/refinement-loop            → upsert one session row (by id). Body is
//                                        a RefinementLoopSession (camelCase).
//
// Per design §2 the server row is the durable source of truth; the client runs
// the reducer (lib/refinement-loop-machine) and persists snapshots, with a
// localStorage cache for offline resilience. This route therefore PERSISTS
// client-computed state — it does not re-run the machine — but it never trusts
// the client's identity: user_id is always overwritten with the authenticated
// user, and `state` is validated against the known set. RLS on the table is the
// defense-in-depth backstop.
//
// Auth: Bearer JWT (same as the section2 / attempts routes). 401 if missing.

export const dynamic = "force-dynamic";

import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import { getAuthUser } from "@/lib/server-auth";
import { LOOP_STATES, type RefinementLoopSession } from "@/lib/refinement-loop";
import { rowToSession, sessionToRow, type LoopRow } from "@/lib/refinement-loop-row";

const ROW_COLUMNS =
  "id, user_id, triggered_at, triggered_source, triggered_question, skill_tag, topic, " +
  "state, state_updated_at, similar_attempts, mini_test_questions, mini_test_score, " +
  "drill_attempts, drill_streak, retest_questions, retest_score, completed_at, exit_reason, meta";

export async function GET(req: NextRequest) {
  const user = await getAuthUser(req);
  if (!user) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  const admin = createAdminClient();

  // ?scope=completed → recent completed loops (for the §5 recently-mastered
  // dashboard suppression). Default → the single active loop (for resume).
  if (new URL(req.url).searchParams.get("scope") === "completed") {
    const { data, error } = await admin
      .from("refinement_loop_sessions")
      .select("topic, exit_reason, completed_at")
      .eq("user_id", user.id)
      .not("completed_at", "is", null)
      .order("completed_at", { ascending: false })
      .limit(50);
    if (error) {
      return NextResponse.json({ error: error.message ?? "Database read failed" }, { status: 500 });
    }
    const loops = (data ?? []).map((r) => {
      const row = r as { topic: string; exit_reason: string | null; completed_at: string | null };
      return { topic: row.topic, exitReason: row.exit_reason, completedAt: row.completed_at };
    });
    return NextResponse.json({ data: loops });
  }

  const { data, error } = await admin
    .from("refinement_loop_sessions")
    .select(ROW_COLUMNS)
    .eq("user_id", user.id)
    .is("completed_at", null)
    .order("state_updated_at", { ascending: false })
    .limit(1);

  if (error) {
    return NextResponse.json({ error: error.message ?? "Database read failed" }, { status: 500 });
  }
  const row = (data ?? [])[0] as unknown as LoopRow | undefined;
  return NextResponse.json({ data: row ? rowToSession(row) : null });
}

export async function POST(req: NextRequest) {
  const user = await getAuthUser(req);
  if (!user) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  let body: RefinementLoopSession;
  try {
    body = (await req.json()) as RefinementLoopSession;
  } catch {
    return NextResponse.json({ error: "Invalid JSON body" }, { status: 400 });
  }

  if (!body || typeof body.id !== "string" || !body.id) {
    return NextResponse.json({ error: "session id required" }, { status: 400 });
  }
  if (!LOOP_STATES.includes(body.state)) {
    return NextResponse.json({ error: `invalid state: ${body.state}` }, { status: 400 });
  }

  // Never trust the client's identity — bind the row to the authenticated user.
  const row = sessionToRow({ ...body, userId: user.id });

  const admin = createAdminClient();
  const { data, error } = await admin
    .from("refinement_loop_sessions")
    .upsert(row, { onConflict: "id" })
    .select(ROW_COLUMNS)
    .single();

  if (error) {
    return NextResponse.json({ error: error.message ?? "Database write failed" }, { status: 500 });
  }
  return NextResponse.json({ data: rowToSession(data as unknown as LoopRow) });
}
