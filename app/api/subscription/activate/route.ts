export const dynamic = "force-dynamic";

import { NextRequest, NextResponse } from "next/server";
import { timingSafeEqual } from "node:crypto";
import { createAdminClient } from "@/lib/supabase";

// ADMIN-ONLY premium activation — the manual-fulfillment half of the v1
// payment flow (prices in lib/pricing.ts, purchase requests in
// premium_waitlist). The owner verifies the bank transfer, then activates
// the account here (or directly in the Supabase dashboard, which this route
// merely automates).
//
// HISTORY: this route used to activate the CALLER's own subscription with no
// payment check — any signed-in student could grant themselves Premium. That
// was a placeholder from before prices existed; now that Premium is a paid
// product it requires the ADMIN_ACTIVATION_KEY secret. With the env var
// unset the route is disabled entirely (503) and the dashboard runbook is
// the only path — nothing else depends on the secret.
//
// Usage:
//   curl -X POST https://www.mongolpotential.com/api/subscription/activate \
//     -H "x-admin-key: $ADMIN_ACTIVATION_KEY" -H "Content-Type: application/json" \
//     -d '{"userId":"<uuid from premium_waitlist>","months":1,"paymentRef":"khan-2026-08-01"}'
//   (or {"username":"..."} instead of userId)

function keyMatches(provided: string | null, expected: string): boolean {
  if (!provided) return false;
  const a = Buffer.from(provided);
  const b = Buffer.from(expected);
  if (a.length !== b.length) return false;
  return timingSafeEqual(a, b);
}

export async function POST(req: NextRequest) {
  const expected = process.env.ADMIN_ACTIVATION_KEY;
  if (!expected) {
    return NextResponse.json(
      { error: "Activation endpoint is disabled (no ADMIN_ACTIVATION_KEY set)." },
      { status: 503 },
    );
  }
  if (!keyMatches(req.headers.get("x-admin-key"), expected)) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const body = await req.json().catch(() => null);
  const userId = typeof body?.userId === "string" ? body.userId : null;
  const username = typeof body?.username === "string" ? body.username : null;
  const months = Number.isInteger(body?.months) && body.months >= 1 && body.months <= 24
    ? (body.months as number)
    : null;
  const paymentRef = typeof body?.paymentRef === "string" ? body.paymentRef : null;

  if ((!userId && !username) || !months) {
    return NextResponse.json(
      { error: "Body must include months (1–24) and userId or username." },
      { status: 400 },
    );
  }

  const admin = createAdminClient();

  // Resolve the target profile. username is unique, so either key is exact.
  const query = admin.from("profiles").select("id, username");
  const { data: profile } = userId
    ? await query.eq("id", userId).single()
    : await query.eq("username", username as string).single();
  if (!profile) {
    return NextResponse.json({ error: "No such user." }, { status: 404 });
  }

  const expiresAt = new Date();
  expiresAt.setMonth(expiresAt.getMonth() + months);

  const { error } = await admin
    .from("profiles")
    .update({
      is_subscribed: true,
      subscription_expires_at: expiresAt.toISOString(),
    })
    .eq("id", profile.id);
  if (error) {
    return NextResponse.json({ error: "Update failed." }, { status: 500 });
  }

  await admin.from("subscription_events").insert({
    user_id: profile.id,
    event_type: "subscribed",
    expires_at: expiresAt.toISOString(),
    payment_ref: paymentRef,
  });

  return NextResponse.json({
    data: { success: true, username: profile.username, expiresAt },
  });
}
