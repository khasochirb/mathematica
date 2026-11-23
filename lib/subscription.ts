import { createAdminClient } from "./supabase";

// Daily AI question quota, shared by /api/tutor and the AI placement. The
// site is free for everyone (owner decision 2026-11-23), so there is ONE
// allowance for every signed-in student — the one that used to be Premium's.
// It is a HARD daily cap, so the worst-case Anthropic spend per student per
// day is bounded: roughly limit × ~₮90 per question at typical usage.
export const DAILY_AI_LIMIT = 30;

/**
 * Whether the profile carries an active subscription record. Nothing gates on
 * this any more; it stays so /api/subscription/status can still report the
 * account's recorded state (subscriptions activated before 2026-11-23 remain
 * in the database untouched).
 */
export async function isSubscribed(userId: string): Promise<boolean> {
  const admin = createAdminClient();
  const { data } = await admin
    .from("profiles")
    .select("is_subscribed, subscription_expires_at")
    .eq("id", userId)
    .single();

  if (!data?.is_subscribed) return false;
  if (!data.subscription_expires_at) return true; // no expiry = lifetime
  return new Date(data.subscription_expires_at) > new Date();
}

/** Get how many problems this user has done today (UTC+8 / Ulaanbaatar) */
export async function getDailyCount(userId: string): Promise<number> {
  const admin = createAdminClient();
  const today = getTodayUB();
  const { data } = await admin
    .from("daily_problem_counts")
    .select("count")
    .eq("user_id", userId)
    .eq("date", today)
    .single();
  return data?.count ?? 0;
}

/** Increment daily count */
export async function incrementDailyCount(userId: string): Promise<void> {
  const admin = createAdminClient();
  const today = getTodayUB();
  await admin.rpc("increment_daily_count", {
    p_user_id: userId,
    p_date: today,
  });
}

/** Today's date in Ulaanbaatar time (UTC+8) */
function getTodayUB(): string {
  const now = new Date();
  const ub = new Date(now.getTime() + 8 * 60 * 60 * 1000);
  return ub.toISOString().split("T")[0];
}
