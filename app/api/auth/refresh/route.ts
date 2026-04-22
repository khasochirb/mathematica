export const dynamic = "force-dynamic";

import { NextRequest, NextResponse } from "next/server";
import { createSupabaseClient } from "@/lib/supabase";

export async function POST(req: NextRequest) {
  const { refreshToken } = await req.json();
  if (!refreshToken || typeof refreshToken !== "string") {
    return NextResponse.json({ error: "Missing refresh token" }, { status: 400 });
  }

  const supabase = createSupabaseClient();
  const { data, error } = await supabase.auth.refreshSession({ refresh_token: refreshToken });

  if (error || !data.session) {
    return NextResponse.json({ error: error?.message ?? "Refresh failed" }, { status: 401 });
  }

  return NextResponse.json({
    data: {
      accessToken: data.session.access_token,
      refreshToken: data.session.refresh_token,
    },
  });
}
