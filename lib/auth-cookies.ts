// Server-side constants for the HttpOnly refresh-token cookie.
//
// Centralized so the four routes that touch this cookie (login, register,
// refresh, logout) can't drift on attributes — drift would break cookie
// matching and the clear path would leave a stale cookie behind.
//
// Path is scoped to /api/auth so the cookie is only sent on auth routes,
// minimizing CSRF surface. Access token stays in a JS-readable cookie at
// path=/ and travels via Authorization header.

export const REFRESH_COOKIE_NAME = "mp_refresh_token";

export const REFRESH_COOKIE_OPTIONS = {
  httpOnly: true,
  secure: process.env.NODE_ENV === "production",
  sameSite: "lax" as const,
  path: "/api/auth",
  maxAge: 60 * 60 * 24 * 30, // 30 days = 2,592,000s, Supabase refresh-token default
};
