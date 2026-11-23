export const dynamic = "force-dynamic";

import { NextRequest, NextResponse } from "next/server";
import { getAuthUser } from "@/lib/server-auth";
import {
  isSubscribed,
  getDailyCount,
  DAILY_AI_LIMIT,
} from "@/lib/subscription";

export async function GET(req: NextRequest) {
  const user = await getAuthUser(req);
  if (!user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const [subscribed, dailyCount] = await Promise.all([
    isSubscribed(user.id),
    getDailyCount(user.id),
  ]);

  // One allowance for everyone since the site went free (2026-11-23);
  // isSubscribed is reported as the account's recorded state only.
  const limit = DAILY_AI_LIMIT;
  return NextResponse.json({
    data: {
      isSubscribed: subscribed,
      dailyProblemsUsed: dailyCount,
      dailyProblemsLimit: limit,
      remainingToday: Math.max(0, limit - dailyCount),
    },
  });
}
