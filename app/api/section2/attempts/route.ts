// Section 2 (Part 2) attempt persistence.
//
// POST /api/section2/attempts
//   Body: { sessionId, testKey, attempts: [{ source, slotAnswers }, ...] }
//
// GET /api/section2/attempts?sessionId=<id>&testKey=<key>
//   Returns the calling user's attempts for a single session, used by
//   the results page (S2.6) to render per-subproblem ✓/✗ + scores.
//
// Auth: Bearer JWT in Authorization header (same as other routes).
// 401 if missing/invalid; on POST the client may not claim correctness —
// server recomputes is_correct via gradeSection2Subproblem (S2.3 logic).
//
// Storage: section2_attempts table (migration 006). Re-submission
// within the same session (same user_id, test_key, problem,
// subproblem, session_id) overwrites via ON CONFLICT DO UPDATE.

export const dynamic = "force-dynamic";

import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import { getAuthUser } from "@/lib/server-auth";
import {
  getTestSection2,
  gradeSection2Subproblem,
} from "@/lib/esh-section2";

interface AttemptInput {
  source: string;
  slotAnswers: Record<string, string>;
}

interface RequestBody {
  sessionId: string;
  testKey: string;
  attempts: AttemptInput[];
}

function isStringMap(v: unknown): v is Record<string, string> {
  if (!v || typeof v !== "object" || Array.isArray(v)) return false;
  return Object.values(v).every((x) => typeof x === "string");
}

export async function POST(req: NextRequest) {
  const user = await getAuthUser(req);
  if (!user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  let body: RequestBody;
  try {
    body = (await req.json()) as RequestBody;
  } catch {
    return NextResponse.json(
      { error: "Invalid JSON body" },
      { status: 400 },
    );
  }

  const sessionId = (body.sessionId ?? "").trim();
  const testKey = (body.testKey ?? "").trim().toUpperCase();
  if (!sessionId) {
    return NextResponse.json(
      { error: "sessionId required" },
      { status: 400 },
    );
  }
  if (!testKey) {
    return NextResponse.json(
      { error: "testKey required" },
      { status: 400 },
    );
  }
  if (!Array.isArray(body.attempts)) {
    return NextResponse.json(
      { error: "attempts must be an array" },
      { status: 400 },
    );
  }

  const items = getTestSection2(testKey);
  if (!items) {
    return NextResponse.json(
      { error: `Unknown testKey: ${testKey}` },
      { status: 400 },
    );
  }

  const itemBySource = new Map(items.map((i) => [i.source, i]));

  const rows: Array<{
    user_id: string;
    test_key: string;
    problem: string;
    subproblem: number;
    slot_answers: Record<string, string>;
    is_correct: boolean;
    points_earned: number;
    points_max: number;
    session_id: string;
  }> = [];

  let totalEarned = 0;
  let totalMax = 0;

  for (const attempt of body.attempts) {
    if (!attempt || typeof attempt.source !== "string") {
      return NextResponse.json(
        { error: "each attempt requires a string `source`" },
        { status: 400 },
      );
    }
    const item = itemBySource.get(attempt.source);
    if (!item) {
      return NextResponse.json(
        { error: `Unknown source: ${attempt.source}` },
        { status: 400 },
      );
    }
    const slotAnswers = attempt.slotAnswers ?? {};
    if (!isStringMap(slotAnswers)) {
      return NextResponse.json(
        {
          error: `attempt.slotAnswers for ${attempt.source} must be a string→string map`,
        },
        { status: 400 },
      );
    }
    const grade = gradeSection2Subproblem(item, slotAnswers);
    rows.push({
      user_id: user.id,
      test_key: testKey,
      problem: item.problem,
      subproblem: item.subproblem,
      slot_answers: slotAnswers,
      is_correct: grade.correct,
      points_earned: grade.pointsEarned,
      points_max: grade.pointsMax,
      session_id: sessionId,
    });
    totalEarned += grade.pointsEarned;
    totalMax += grade.pointsMax;
  }

  if (rows.length === 0) {
    return NextResponse.json({
      data: { ok: true, attempts: 0, totalEarned: 0, totalMax: 0 },
    });
  }

  const admin = createAdminClient();
  const { error } = await admin.from("section2_attempts").upsert(rows, {
    onConflict: "user_id,test_key,problem,subproblem,session_id",
  });

  if (error) {
    return NextResponse.json(
      { error: error.message ?? "Database write failed" },
      { status: 500 },
    );
  }

  return NextResponse.json({
    data: {
      ok: true,
      attempts: rows.length,
      totalEarned,
      totalMax,
    },
  });
}

export async function GET(req: NextRequest) {
  const user = await getAuthUser(req);
  if (!user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const url = new URL(req.url);
  const sessionId = (url.searchParams.get("sessionId") ?? "").trim();
  const testKey = (url.searchParams.get("testKey") ?? "").trim().toUpperCase();
  if (!sessionId) {
    return NextResponse.json(
      { error: "sessionId required" },
      { status: 400 },
    );
  }

  const admin = createAdminClient();
  let query = admin
    .from("section2_attempts")
    .select(
      "test_key, problem, subproblem, slot_answers, is_correct, points_earned, points_max",
    )
    .eq("user_id", user.id)
    .eq("session_id", sessionId);
  if (testKey) query = query.eq("test_key", testKey);

  const { data, error } = await query;
  if (error) {
    return NextResponse.json(
      { error: error.message ?? "Database read failed" },
      { status: 500 },
    );
  }

  return NextResponse.json({ data: { attempts: data ?? [] } });
}
