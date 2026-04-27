export const dynamic = "force-dynamic";

import { NextRequest, NextResponse } from "next/server";
import { createSupabaseClient } from "@/lib/supabase";

export async function POST(req: NextRequest) {
  const { email } = await req.json();

  if (typeof email !== "string" || email.length === 0 || email.length > 320) {
    return NextResponse.json({ error: "Invalid email." }, { status: 400 });
  }

  const supabase = createSupabaseClient();
  const { error } = await supabase.auth.resend({
    type: "signup",
    email,
    options: { emailRedirectTo: `${req.nextUrl.origin}/sign-in?confirmed=true` },
  });

  if (error) {
    // Propagate Supabase's status (typically 429 for the per-email 60s
    // limit) and message verbatim so the client can surface it. The
    // contract guard in apiCall handles the !res.ok case.
    // Note: error.status ?? 400 falls back to 400 when status is missing,
    // which can mask 5xx-class failures (Supabase outage, network hiccup
    // surfaced through the SDK without a status). If 4xx-disguised
    // outages show up in production, revisit by inspecting err shape.
    return NextResponse.json(
      { error: error.message },
      { status: error.status ?? 400 },
    );
  }

  return NextResponse.json({ data: { ok: true } });
}
