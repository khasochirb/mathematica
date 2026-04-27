export const dynamic = "force-dynamic";

import { NextResponse } from "next/server";
import { REFRESH_COOKIE_NAME, REFRESH_COOKIE_OPTIONS } from "@/lib/auth-cookies";

// Clears the HttpOnly refresh-token cookie. JS can't clear HttpOnly cookies,
// so this route exists specifically for that purpose. Idempotent — always
// returns 200 even if no cookie was present, so retries from the client are
// safe.
export async function POST() {
  const res = NextResponse.json({ data: { ok: true } });
  res.cookies.set(REFRESH_COOKIE_NAME, "", { ...REFRESH_COOKIE_OPTIONS, maxAge: 0 });
  return res;
}
