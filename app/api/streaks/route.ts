import { NextResponse } from "next/server";

export async function GET() {
  return NextResponse.json({
    data: {
      currentStreak: 0,
      longestStreak: 0,
      lastActivityDate: null,
      streakFreezeCount: 0,
      totalActiveDays: 0,
    },
  });
}
