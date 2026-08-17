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

  // THE RESULT IS CHECKED. It used to be discarded — `await admin.from(...)`
  // with nothing destructured — so the route answered `success: true` whether
  // the row landed or not, and the modal showed its confirmation either way.
  // A Premium purchase request is the most valuable thing this site collects;
  // it must not be possible for one to disappear while the buyer is told it
  // arrived. If this insert fails the caller now hears about it and can try
  // again or phone instead.
  const { error } = await admin
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

  if (error) {
    // Logged with the source but never the email: the address is the lead and
    // logs are not where leads should live.
    console.error("[waitlist] upsert failed", { source, code: error.code, message: error.message });
    return NextResponse.json({ error: "Could not save your request" }, { status: 500 });
  }

  return NextResponse.json({ data: { success: true } });
}
