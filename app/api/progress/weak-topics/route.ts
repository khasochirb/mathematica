import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import { getAuthUser } from "@/lib/server-auth";
import { isSubscribed } from "@/lib/subscription";

export async function GET(req: NextRequest) {
  const user = await getAuthUser(req);
  if (!user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const subscribed = await isSubscribed(user.id);
  if (!subscribed) {
    return NextResponse.json(
      { error: "SUBSCRIPTION_REQUIRED" },
      { status: 402 }
    );
  }

  const admin = createAdminClient();

  const { data: rows, error } = await admin
    .from("topic_progress")
    .select("*, topics(name, slug)")
    .eq("user_id", user.id)
    .order("weakness_score", { ascending: false })
    .limit(5);

  if (error) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }

  const result = (rows ?? []).map((r) => ({
    topicId: r.topic_id,
    recentAccuracy: r.recent_accuracy,
    totalAttempts: r.total_attempts,
    currentDifficulty: r.current_difficulty,
    weaknessScore: r.weakness_score,
    topicXp: r.topic_xp,
    topicLevel: r.topic_level,
    nextReviewAt: r.next_review_at,
    topic: {
      name: (r as Record<string, unknown>).topics
        ? ((r as Record<string, unknown>).topics as { name: string; slug: string }).name
        : "",
      slug: (r as Record<string, unknown>).topics
        ? ((r as Record<string, unknown>).topics as { name: string; slug: string }).slug
        : "",
    },
  }));

  return NextResponse.json({ data: result });
}
