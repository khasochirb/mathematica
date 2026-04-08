import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import { getAuthUser } from "@/lib/server-auth";

export async function POST(req: NextRequest) {
  const user = await getAuthUser(req);
  if (!user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const body = await req.json();
  const mode: string = body.mode ?? "practice";
  const topicIds: string[] | undefined = body.topicIds;

  const admin = createAdminClient();

  // Create session
  const { data: session, error: sessionErr } = await admin
    .from("practice_sessions")
    .insert({ user_id: user.id, mode })
    .select("id")
    .single();

  if (sessionErr || !session) {
    return NextResponse.json(
      { error: sessionErr?.message ?? "Failed to create session" },
      { status: 500 }
    );
  }

  // Fetch first problem — pick from requested topics or any topic
  let problemQuery = admin
    .from("problems")
    .select("id, topic_id, difficulty, question, question_meta, answer_type, options, hints, explanation");

  if (topicIds && topicIds.length > 0) {
    problemQuery = problemQuery.in("topic_id", topicIds);
  }

  const { data: problems } = await problemQuery.limit(50);

  let firstProblem = null;
  if (problems && problems.length > 0) {
    const pick = problems[Math.floor(Math.random() * problems.length)];
    firstProblem = {
      id: pick.id,
      topicId: pick.topic_id,
      difficulty: pick.difficulty,
      question: pick.question,
      questionMeta: pick.question_meta,
      answerType: pick.answer_type,
      options: pick.options,
      hints: pick.hints ?? [],
      explanation: null, // strip explanation
    };
  }

  return NextResponse.json({
    data: { sessionId: session.id, firstProblem },
  });
}
