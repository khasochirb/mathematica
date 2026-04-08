import { NextRequest, NextResponse } from "next/server";
import { getAuthUser } from "@/lib/server-auth";
import { createAdminClient } from "@/lib/supabase";

export async function POST(req: NextRequest) {
  const user = await getAuthUser(req);
  if (!user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const { months = 1, paymentRef } = await req.json();

  const admin = createAdminClient();
  const expiresAt = new Date();
  expiresAt.setMonth(expiresAt.getMonth() + months);

  await admin
    .from("profiles")
    .update({
      is_subscribed: true,
      subscription_expires_at: expiresAt.toISOString(),
    })
    .eq("id", user.id);

  await admin.from("subscription_events").insert({
    user_id: user.id,
    event_type: "subscribed",
    expires_at: expiresAt.toISOString(),
    payment_ref: paymentRef ?? null,
  });

  return NextResponse.json({ data: { success: true, expiresAt } });
}
