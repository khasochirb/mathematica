export const dynamic = "force-dynamic";

import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import { getAuthUser } from "@/lib/server-auth";

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export async function POST(req: NextRequest) {
  const body = await req.json().catch(() => null);
  const email = typeof body?.email === "string" ? body.email.trim().toLowerCase() : "";
  const source = typeof body?.source === "string" ? body.source : "unknown";
  const interestedExams = Array.isArray(body?.interestedExams)
    ? (body.interestedExams as unknown[]).filter((s) => typeof s === "string")
    : [];

  if (!EMAIL_RE.test(email)) {
    return NextResponse.json({ error: "Invalid email" }, { status: 400 });
  }

  const user = await getAuthUser(req);
  const admin = createAdminClient();

  await admin
    .from("premium_waitlist")
    .upsert(
      {
        email,
        source,
        interested_exams: interestedExams,
        user_id: user?.id ?? null,
      },
      { onConflict: "email,source" },
    );

  return NextResponse.json({ data: { success: true } });
}
