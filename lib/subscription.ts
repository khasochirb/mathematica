import { createAdminClient } from "./supabase";

// Reserved for future AI-generated problem gating. Not currently enforced —
// past-paper content is free with no cap.
export const FREE_DAILY_AI_LIMIT = 10;

/** Check if user is an active subscriber */
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
