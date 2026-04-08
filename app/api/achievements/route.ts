import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import { getAuthUser } from "@/lib/server-auth";

export async function GET(req: NextRequest) {
  const user = await getAuthUser(req);
  if (!user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const admin = createAdminClient();

  // Fetch all achievements
  const { data: achievements, error } = await admin
    .from("achievements")
    .select("*")
    .order("category", { ascending: true });

  if (error) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }

  // Fetch user's earned achievements
  const { data: userAchievements } = await admin
    .from("user_achievements")
    .select("achievement_id, earned_at")
    .eq("user_id", user.id);

  const earnedMap = new Map(
    (userAchievements ?? []).map((ua) => [ua.achievement_id, ua.earned_at])
  );

  const result = (achievements ?? []).map((a) => ({
    id: a.id,
    slug: a.slug,
    name: a.name,
    description: a.description,
    iconKey: a.icon_key,
    xpReward: a.xp_reward,
    category: a.category,
    threshold: a.threshold,
    earned: earnedMap.has(a.id),
    earnedAt: earnedMap.get(a.id) ?? null,
  }));

  return NextResponse.json({ data: result });
}
