// Edge middleware: per-IP rate limiting on the abuse-prone auth endpoints.
// Runs before the route handler; on limit-exceeded it returns 429 and the
// handler never executes. Everything else passes straight through untouched.
//
// Scope is deliberately narrow (login/register/resend) — the brute-force /
// spam targets. Frequently-polled auth routes (/api/auth/me, /refresh,
// /logout) are intentionally NOT limited: legit clients hit them on every
// mount and token rotation, and they aren't credential oracles.

import { NextRequest, NextResponse } from "next/server";
import { checkAuthRateLimit } from "@/lib/rate-limit";

export const config = {
  matcher: ["/api/auth/login", "/api/auth/register", "/api/auth/resend", "/api/tutor"],
};

export async function middleware(req: NextRequest) {
  // Vercel populates req.ip; x-forwarded-for is the fallback (first hop is the
  // client). "unknown" only happens off-platform (local dev) — acceptable,
  // since the limiter is a no-op there without Upstash configured anyway.
  const ip =
    req.ip ??
    req.headers.get("x-forwarded-for")?.split(",")[0]?.trim() ??
    "unknown";

  let result;
  try {
    result = await checkAuthRateLimit(req.nextUrl.pathname, ip);
  } catch (err) {
    // Redis hiccup / network error → fail OPEN so a store outage can't lock
    // every student out of logging in. Log (no PII) and let the request pass.
    console.warn("[rate-limit] check failed, allowing request:", (err as Error)?.message);
    return NextResponse.next();
  }

  if (!result.configured || result.ok) {
    return NextResponse.next();
  }

  const retryAfter = Math.max(1, Math.ceil((result.reset - Date.now()) / 1000));
  // Bilingual, MN-first (primary audience); the client surfaces `error`
  // verbatim via apiCall's contract guard.
  return NextResponse.json(
    {
      error: `Хэт олон удаа оролдлоо. ${retryAfter} секундын дараа дахин оролдоно уу. — Too many attempts. Try again in ${retryAfter}s.`,
    },
    {
      status: 429,
      headers: {
        "Retry-After": String(retryAfter),
        "X-RateLimit-Limit": String(result.limit),
        "X-RateLimit-Remaining": String(result.remaining),
        "X-RateLimit-Reset": String(result.reset),
      },
    },
  );
}
