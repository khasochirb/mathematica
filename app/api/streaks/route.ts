import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import { getAuthUser } from "@/lib/server-auth";

export async function GET(req: NextRequest) {
  const user = await getAuthUser(req);
  if (!user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const admin = createAdminClient();

  const { data: streak } = await admin
    .from("streaks")
    .select("*")
    .eq("user_id", user.id)
    .single();

  if (!streak) {
    // Create default streak row
    const { data: newStreak } = await admin
      .from("streaks")
      .insert({
        user_id: user.id,
        current_streak: 0,
        longest_streak: 0,
        total_active_days: 0,
        streak_freeze_count: 3,
      })
      .select("*")
      .single();

    return NextResponse.json({
      data: {
        currentStreak: newStreak?.current_streak ?? 0,
        longestStreak: newStreak?.longest_streak ?? 0,
        lastActivityDate: newStreak?.last_activity_date ?? null,
        streakFreezeCount: newStreak?.streak_freeze_count ?? 3,
        totalActiveDays: newStreak?.total_active_days ?? 0,
      },
    });
  }

  return NextResponse.json({
    data: {
      currentStreak: streak.current_streak,
      longestStreak: streak.longest_streak,
      lastActivityDate: streak.last_activity_date ?? null,
      streakFreezeCount: streak.streak_freeze_count,
      totalActiveDays: streak.total_active_days,
    },
  });
}
