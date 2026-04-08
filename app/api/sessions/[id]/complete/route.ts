import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import { getAuthUser } from "@/lib/server-auth";

export async function POST(
  req: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const user = await getAuthUser(req);
  if (!user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const { id: sessionId } = await params;
  const body = await req.json();
  const todayDate: string = body.todayDate;

  const admin = createAdminClient();

  // Fetch session
  const { data: session, error: sessErr } = await admin
    .from("practice_sessions")
    .select("*")
    .eq("id", sessionId)
    .eq("user_id", user.id)
    .single();

  if (sessErr || !session) {
    return NextResponse.json({ error: "Session not found" }, { status: 404 });
  }

  // Mark session completed
  await admin
    .from("practice_sessions")
    .update({ status: "completed", completed_at: new Date().toISOString() })
    .eq("id", sessionId);

  // Get profile for level info
  const { data: profile } = await admin
    .from("profiles")
    .select("global_xp, global_level")
    .eq("id", user.id)
    .single();

  const levelBefore = profile?.global_level ?? 1;
  const totalXp = profile?.global_xp ?? 0;
  const levelAfter = Math.floor(Math.sqrt(totalXp / 100)) + 1;

  // Update streak
  const { data: streak } = await admin
    .from("streaks")
    .select("*")
    .eq("user_id", user.id)
    .single();

  let currentStreak = 1;

  if (streak) {
    const lastDate = streak.last_activity_date;
    if (lastDate === todayDate) {
      // Already active today — no change
      currentStreak = streak.current_streak;
    } else {
      // Check if consecutive
      const last = new Date(lastDate);
      const today = new Date(todayDate);
      const diffDays = Math.round(
        (today.getTime() - last.getTime()) / (1000 * 60 * 60 * 24)
      );

      if (diffDays === 1) {
        currentStreak = streak.current_streak + 1;
      } else {
        currentStreak = 1;
      }

      const longestStreak = Math.max(streak.longest_streak, currentStreak);

      await admin
        .from("streaks")
        .update({
          current_streak: currentStreak,
          longest_streak: longestStreak,
          last_activity_date: todayDate,
          total_active_days: streak.total_active_days + 1,
        })
        .eq("user_id", user.id);
    }
  } else {
    // First ever session
    await admin.from("streaks").insert({
      user_id: user.id,
      current_streak: 1,
      longest_streak: 1,
      last_activity_date: todayDate,
      total_active_days: 1,
    });
  }

  // Check achievements
  const newAchievements: Array<{ slug: string; name: string; xpReward: number }> = [];

  const { data: allAchievements } = await admin
    .from("achievements")
    .select("*");

  const { data: userAchievements } = await admin
    .from("user_achievements")
    .select("achievement_id")
    .eq("user_id", user.id);

  const earnedIds = new Set((userAchievements ?? []).map((ua) => ua.achievement_id));

  for (const ach of allAchievements ?? []) {
    if (earnedIds.has(ach.id)) continue;

    let earned = false;

    switch (ach.slug) {
      case "first_problem":
        earned = session.total_questions >= 1;
        break;
      case "streak_3":
        earned = currentStreak >= 3;
        break;
      case "streak_7":
        earned = currentStreak >= 7;
        break;
      case "streak_30":
        earned = currentStreak >= 30;
        break;
      case "perfect_session":
        earned =
          session.total_questions >= 5 &&
          session.total_correct === session.total_questions;
        break;
      case "speed_demon": {
        // Average time per question under 15 seconds
        const { data: answers } = await admin
          .from("session_answers")
          .select("time_taken_ms")
          .eq("session_id", sessionId);
        if (answers && answers.length >= 5) {
          const avg =
            answers.reduce((s, a) => s + a.time_taken_ms, 0) / answers.length;
          earned = avg < 15000;
        }
        break;
      }
      case "century":
        // 100 total problems answered
        {
          const { count } = await admin
            .from("session_answers")
            .select("id", { count: "exact", head: true })
            .eq("user_id", user.id);
          earned = (count ?? 0) >= 100;
        }
        break;
    }

    if (earned) {
      await admin.from("user_achievements").insert({
        user_id: user.id,
        achievement_id: ach.id,
      });

      // Award achievement XP
      if (ach.xp_reward > 0) {
        const newXp = totalXp + ach.xp_reward;
        await admin
          .from("profiles")
          .update({
            global_xp: newXp,
            global_level: Math.floor(Math.sqrt(newXp / 100)) + 1,
          })
          .eq("id", user.id);
      }

      newAchievements.push({
        slug: ach.slug,
        name: ach.name,
        xpReward: ach.xp_reward,
      });
    }
  }

  const accuracyPct =
    session.total_questions > 0
      ? Math.round((session.total_correct / session.total_questions) * 100)
      : 0;

  return NextResponse.json({
    data: {
      sessionXp: session.session_xp,
      totalXp,
      levelBefore,
      levelAfter,
      leveledUp: levelAfter > levelBefore,
      currentStreak,
      newAchievements,
      totalCorrect: session.total_correct,
      totalQuestions: session.total_questions,
      accuracyPct,
    },
  });
}
