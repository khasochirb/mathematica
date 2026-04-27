export const dynamic = "force-dynamic";

import { NextRequest, NextResponse } from "next/server";
import { createSupabaseClient } from "@/lib/supabase";
import { REFRESH_COOKIE_NAME, REFRESH_COOKIE_OPTIONS } from "@/lib/auth-cookies";

export async function POST(req: NextRequest) {
  const refreshToken = req.cookies.get(REFRESH_COOKIE_NAME)?.value;
  // 401 (was 400 pre-HttpOnly) so auth-context's runRefreshOnce treats
  // this as a logout-trigger like any other 4xx from this route.
  if (!refreshToken) {
    return NextResponse.json({ error: "Missing refresh token" }, { status: 401 });
  }

  const supabase = createSupabaseClient();
  const { data, error } = await supabase.auth.refreshSession({ refresh_token: refreshToken });

  if (error || !data.session) {
    return NextResponse.json({ error: error?.message ?? "Refresh failed" }, { status: 401 });
  }

  const res = NextResponse.json({
    data: {
      accessToken: data.session.access_token,
    },
  });
  // Rotate the cookie with the new refresh token. RTR makes the prior
  // refresh token invalid the moment Supabase issues this new one.
  res.cookies.set(REFRESH_COOKIE_NAME, data.session.refresh_token, REFRESH_COOKIE_OPTIONS);
  return res;
}
