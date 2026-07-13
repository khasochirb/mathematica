// Per-IP rate limiting for the abuse-prone auth endpoints (login, register,
// resend). Backed by Upstash Redis (serverless, edge-compatible) so the
// counter is SHARED across every Vercel region and serverless instance — an
// in-memory limiter would reset on each cold start and never coordinate
// across the fleet, so a distributed brute-force would slip through.
//
// FAIL-OPEN by design: if the Upstash env vars aren't set, every check passes
// (with a one-time server warning). This keeps auth fully working before the
// store is provisioned; adding the two env vars later activates limiting with
// zero code change. Availability of login wins over the marginal protection a
// half-configured limiter would give.
//
// Configure in Vercel project env (and .env.local for dev):
//   UPSTASH_REDIS_REST_URL, UPSTASH_REDIS_REST_TOKEN
// (Vercel → Storage → Upstash Redis provisions both automatically.)

import { Ratelimit } from "@upstash/ratelimit";
import { Redis } from "@upstash/redis";

export type RateLimitResult = {
  ok: boolean;
  limit: number;
  remaining: number;
  reset: number; // epoch ms when the window frees up
  configured: boolean; // false → limiter is a no-op (env not set)
};

// Sliding-window budget PER IP PER ROUTE. Login is loosest so a real user
// fumbling a password a few times is never blocked, while credential-stuffing
// (which needs dozens of tries) is throttled hard. Register/resend are
// tighter — they create accounts / send email, so their abuse is costlier.
const WINDOW = "60 s" as const;
const LIMITS: Record<string, number> = {
  "/api/auth/login": 10,
  "/api/auth/register": 5,
  "/api/auth/resend": 5,
  // AI tutor: per-IP burst guard in front of the per-student daily quota the
  // route itself enforces (FREE_DAILY_AI_LIMIT). A student never sends 15
  // questions in a minute; a script does.
  "/api/tutor": 15,
};
const DEFAULT_LIMIT = 10;

let redis: Redis | null = null;
const limiters = new Map<number, Ratelimit>();
let warned = false;

function getRedis(): Redis | null {
  const url = process.env.UPSTASH_REDIS_REST_URL;
  const token = process.env.UPSTASH_REDIS_REST_TOKEN;
  if (!url || !token) {
    if (!warned) {
      // Config warning only — no PII, safe for Vercel logs.
      console.warn(
        "[rate-limit] UPSTASH_REDIS_REST_URL/TOKEN not set — auth rate limiting is DISABLED (fail-open).",
      );
      warned = true;
    }
    return null;
  }
  if (!redis) redis = new Redis({ url, token });
  return redis;
}

function limiterFor(limit: number, r: Redis): Ratelimit {
  let rl = limiters.get(limit);
  if (!rl) {
    rl = new Ratelimit({
      redis: r,
      limiter: Ratelimit.slidingWindow(limit, WINDOW),
      prefix: "mp-auth-rl",
      analytics: false,
    });
    limiters.set(limit, rl);
  }
  return rl;
}

// Checks (and decrements) the caller's budget for `pathname`. The key is
// `pathname:ip`, so each route keeps a separate budget per IP even when two
// routes share the same numeric limit.
export async function checkAuthRateLimit(
  pathname: string,
  ip: string,
): Promise<RateLimitResult> {
  const limit = LIMITS[pathname] ?? DEFAULT_LIMIT;
  const r = getRedis();
  if (!r) {
    return { ok: true, limit, remaining: limit, reset: Date.now(), configured: false };
  }
  const res = await limiterFor(limit, r).limit(`${pathname}:${ip}`);
  return {
    ok: res.success,
    limit: res.limit,
    remaining: res.remaining,
    reset: res.reset,
    configured: true,
  };
}
