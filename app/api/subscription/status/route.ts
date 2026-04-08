import { NextRequest, NextResponse } from "next/server";
import { getAuthUser } from "@/lib/server-auth";
import { isSubscribed, getDailyCount, FREE_DAILY_LIMIT } from "@/lib/subscription";

export async function GET(req: NextRequest) {
  const user = await getAuthUser(req);
  if (!user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const [subscribed, dailyCount] = await Promise.all([
    isSubscribed(user.id),
    getDailyCount(user.id),
  ]);

  return NextResponse.json({
    data: {
      isSubscribed: subscribed,
      dailyProblemsUsed: dailyCount,
      dailyProblemsLimit: FREE_DAILY_LIMIT,
      remainingToday: subscribed
        ? null
        : Math.max(0, FREE_DAILY_LIMIT - dailyCount),
    },
  });
}
