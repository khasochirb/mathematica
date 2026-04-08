import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import { getAuthUser } from "@/lib/server-auth";
import { isSubscribed, getDailyCount, incrementDailyCount, FREE_DAILY_LIMIT } from "@/lib/subscription";

function checkAnswer(
  userAnswer: string,
  correctAnswer: string,
  answerType: string
): boolean {
  const ua = userAnswer.trim();
  const ca = correctAnswer.trim();

  if (answerType === "NUMERIC") {
    const uNum = parseFloat(ua);
    const cNum = parseFloat(ca);
    if (isNaN(uNum) || isNaN(cNum)) return false;
    return Math.abs(uNum - cNum) < 0.001;
  }

  if (answerType === "NUMERIC_RANGE") {
    const uNum = parseFloat(ua);
    const cNum = parseFloat(ca);
    if (isNaN(uNum) || isNaN(cNum)) return false;
    return Math.abs(uNum - cNum) < 0.5;
  }

  // MCQ or TEXT — case-insensitive
  return ua.toLowerCase() === ca.toLowerCase();
}

export async function POST(req: NextRequest) {
  const user = await getAuthUser(req);
  if (!user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const body = await req.json();
  const {
    sessionId,
    problemId,
    userAnswer,
    timeTakenMs,
    hintsUsed = 0,
  }: {
    sessionId: string;
    problemId: string;
    userAnswer: string;
    timeTakenMs: number;
    hintsUsed?: number;
  } = body;

  if (!sessionId || !problemId || userAnswer === undefined || !timeTakenMs) {
    return NextResponse.json({ error: "Missing required fields" }, { status: 400 });
  }

  // Free tier daily limit check
  const subscribed = await isSubscribed(user.id);
  if (!subscribed) {
    const dailyCount = await getDailyCount(user.id);
    if (dailyCount >= FREE_DAILY_LIMIT) {
      return NextResponse.json(
        { error: "DAILY_LIMIT_REACHED", limit: FREE_DAILY_LIMIT },
        { status: 402 }
      );
    }
  }

  const admin = createAdminClient();

  // Fetch the problem
  const { data: problem, error: probErr } = await admin
    .from("problems")
    .select("correct_answer, answer_type, topic_id, difficulty, explanation")
    .eq("id", problemId)
    .single();

  if (probErr || !problem) {
    return NextResponse.json({ error: "Problem not found" }, { status: 404 });
  }

  const isCorrect = checkAnswer(userAnswer, problem.correct_answer, problem.answer_type);

  // Insert session_answer
  await admin.from("session_answers").insert({
    session_id: sessionId,
    problem_id: problemId,
    user_id: user.id,
    user_answer: userAnswer,
    is_correct: isCorrect,
    time_taken_ms: timeTakenMs,
    hints_used: hintsUsed,
  });

  // Update practice_sessions counters
  const { data: session } = await admin
    .from("practice_sessions")
    .select("total_correct, total_questions, session_xp")
    .eq("id", sessionId)
    .single();

  if (session) {
    await admin
      .from("practice_sessions")
      .update({
        total_questions: session.total_questions + 1,
        total_correct: session.total_correct + (isCorrect ? 1 : 0),
      })
      .eq("id", sessionId);
  }

  // Calculate XP
  let xpDelta = 0;
  if (isCorrect) {
    xpDelta = 10 + problem.difficulty * 5 - hintsUsed * 2;
    if (xpDelta < 1) xpDelta = 1;
  }

  // Update or create topic_progress
  const topicId = problem.topic_id;
  const { data: tp } = await admin
    .from("topic_progress")
    .select("*")
    .eq("user_id", user.id)
    .eq("topic_id", topicId)
    .single();

  if (tp) {
    const newTotal = tp.total_attempts + 1;
    const newCorrect = tp.correct_attempts + (isCorrect ? 1 : 0);

    // Calculate recent accuracy from last 10 answers for this topic
    const { data: recent } = await admin
      .from("session_answers")
      .select("is_correct")
      .eq("user_id", user.id)
      .in(
        "problem_id",
        // Get problem IDs for this topic — join via subquery workaround
        (
          await admin.from("problems").select("id").eq("topic_id", topicId)
        ).data?.map((p) => p.id) ?? []
      )
      .order("created_at", { ascending: false })
      .limit(10);

    const recentCorrectCount = (recent ?? []).filter((r) => r.is_correct).length;
    const recentAccuracy = recent && recent.length > 0 ? recentCorrectCount / recent.length : 0;

    // Adjust difficulty based on last 5
    const last5 = (recent ?? []).slice(0, 5);
    const last5Accuracy = last5.length > 0
      ? last5.filter((r) => r.is_correct).length / last5.length
      : 0;

    let newDifficulty = tp.current_difficulty;
    if (last5.length >= 5 && last5Accuracy > 0.8 && newDifficulty < 5) {
      newDifficulty += 1;
    } else if (last5.length >= 5 && last5Accuracy < 0.4 && newDifficulty > 1) {
      newDifficulty -= 1;
    }

    const newTopicXp = tp.topic_xp + xpDelta;
    const newTopicLevel = Math.floor(Math.sqrt(newTopicXp / 100)) + 1;

    await admin
      .from("topic_progress")
      .update({
        total_attempts: newTotal,
        correct_attempts: newCorrect,
        recent_accuracy: recentAccuracy,
        weakness_score: 1 - recentAccuracy,
        current_difficulty: newDifficulty,
        topic_xp: newTopicXp,
        topic_level: newTopicLevel,
      })
      .eq("user_id", user.id)
      .eq("topic_id", topicId);
  } else {
    // First attempt for this topic
    await admin.from("topic_progress").insert({
      user_id: user.id,
      topic_id: topicId,
      total_attempts: 1,
      correct_attempts: isCorrect ? 1 : 0,
      recent_accuracy: isCorrect ? 1 : 0,
      weakness_score: isCorrect ? 0 : 1,
      current_difficulty: 1,
      topic_xp: xpDelta,
      topic_level: 1,
    });
  }

  // Update global XP on profile
  if (xpDelta > 0) {
    const { data: profile } = await admin
      .from("profiles")
      .select("global_xp")
      .eq("id", user.id)
      .single();

    const newGlobalXp = (profile?.global_xp ?? 0) + xpDelta;
    const newGlobalLevel = Math.floor(Math.sqrt(newGlobalXp / 100)) + 1;

    await admin
      .from("profiles")
      .update({ global_xp: newGlobalXp, global_level: newGlobalLevel })
      .eq("id", user.id);

    // Also update session XP
    if (session) {
      await admin
        .from("practice_sessions")
        .update({ session_xp: session.session_xp + xpDelta })
        .eq("id", sessionId);
    }
  }

  // Increment daily count for free users
  if (!subscribed) {
    await incrementDailyCount(user.id);
  }

  return NextResponse.json({
    data: {
      isCorrect,
      correctAnswer: problem.correct_answer,
      explanation: problem.explanation ?? null,
      xpDelta,
    },
  });
}
