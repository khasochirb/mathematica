export const dynamic = "force-dynamic";

import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import { getAuthUser } from "@/lib/server-auth";

export async function GET(req: NextRequest) {
  const user = await getAuthUser(req);
  if (!user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const { searchParams } = new URL(req.url);
  const topicId = searchParams.get("topicId");
  const sessionId = searchParams.get("sessionId");

  if (!topicId || !sessionId) {
    return NextResponse.json(
      { error: "topicId and sessionId are required" },
      { status: 400 }
    );
  }

  const admin = createAdminClient();

  // Get user's current difficulty for this topic
  const { data: progress } = await admin
    .from("topic_progress")
    .select("current_difficulty")
    .eq("user_id", user.id)
    .eq("topic_id", topicId)
    .single();

  const difficulty = progress?.current_difficulty ?? 1;

  // Get problem IDs the user answered correctly in last 20 answers (to avoid repeats)
  const { data: recentCorrect } = await admin
    .from("session_answers")
    .select("problem_id")
    .eq("user_id", user.id)
    .eq("is_correct", true)
    .order("created_at", { ascending: false })
    .limit(20);

  const excludeIds = (recentCorrect ?? []).map((r) => r.problem_id);

  // Fetch candidate problems at the target difficulty
  let query = admin
    .from("problems")
    .select("id, topic_id, difficulty, question, question_meta, answer_type, options, hints, explanation")
    .eq("topic_id", topicId)
    .eq("difficulty", difficulty);

  if (excludeIds.length > 0) {
    // Supabase doesn't have "not in" directly, so we filter after fetch
  }

  const { data: candidates } = await query.limit(50);

  const filtered = (candidates ?? []).filter(
    (p) => !excludeIds.includes(p.id)
  );

  // Fallback: if no problems at exact difficulty, try any difficulty for this topic
  let pool = filtered.length > 0 ? filtered : (candidates ?? []);
  if (pool.length === 0) {
    const { data: fallback } = await admin
      .from("problems")
      .select("id, topic_id, difficulty, question, question_meta, answer_type, options, hints, explanation")
      .eq("topic_id", topicId)
      .limit(50);
    pool = (fallback ?? []).filter((p) => !excludeIds.includes(p.id));
    if (pool.length === 0) pool = fallback ?? [];
  }

  if (pool.length === 0) {
    return NextResponse.json(
      { error: "No problems available for this topic" },
      { status: 404 }
    );
  }

  const pick = pool[Math.floor(Math.random() * pool.length)];

  // Strip correct_answer — it's not in the select, but strip explanation too
  return NextResponse.json({
    data: {
      id: pick.id,
      topicId: pick.topic_id,
      difficulty: pick.difficulty,
      question: pick.question,
      questionMeta: pick.question_meta,
      answerType: pick.answer_type,
      options: pick.options,
      hints: pick.hints ?? [],
      explanation: null,
    },
  });
}
