// Unit test for the auth rate-limit middleware decision logic. The Upstash
// call is mocked, so this exercises MY branches: 429 when over limit,
// pass-through when under, and pass-through when the limiter is unconfigured.
import { describe, it, expect, vi, beforeEach } from "vitest";

// Mock the limiter module the middleware imports. Each test overrides the
// resolved value before calling the middleware.
const checkAuthRateLimit = vi.fn();
vi.mock("@/lib/rate-limit", () => ({
  checkAuthRateLimit: (...args: unknown[]) => checkAuthRateLimit(...args),
}));

// Imported after the mock is registered.
import { NextRequest } from "next/server";
import { middleware } from "../middleware";

function loginReq() {
  return new NextRequest("http://localhost/api/auth/login", {
    method: "POST",
    headers: { "x-forwarded-for": "203.0.113.7" },
  });
}

describe("auth rate-limit middleware", () => {
  beforeEach(() => checkAuthRateLimit.mockReset());

  it("returns 429 with Retry-After when the IP is over the limit", async () => {
    checkAuthRateLimit.mockResolvedValue({
      ok: false,
      limit: 10,
      remaining: 0,
      reset: Date.now() + 30_000,
      configured: true,
    });
    const res = await middleware(loginReq());
    expect(res.status).toBe(429);
    const retry = Number(res.headers.get("Retry-After"));
    expect(retry).toBeGreaterThan(0);
    expect(retry).toBeLessThanOrEqual(30);
    expect(res.headers.get("X-RateLimit-Limit")).toBe("10");
    const body = await res.json();
    expect(body.error).toMatch(/Too many attempts|олон удаа/);
  });

  it("passes through (not 429) when under the limit", async () => {
    checkAuthRateLimit.mockResolvedValue({
      ok: true,
      limit: 10,
      remaining: 9,
      reset: Date.now() + 60_000,
      configured: true,
    });
    const res = await middleware(loginReq());
    expect(res.status).not.toBe(429);
    expect(res.headers.get("x-middleware-next")).toBe("1");
  });

  it("passes through when the limiter is unconfigured (fail-open)", async () => {
    checkAuthRateLimit.mockResolvedValue({
      ok: true,
      limit: 10,
      remaining: 10,
      reset: Date.now(),
      configured: false,
    });
    const res = await middleware(loginReq());
    expect(res.status).not.toBe(429);
    expect(res.headers.get("x-middleware-next")).toBe("1");
  });

  // The store-outage fail-open path (limiter throws → middleware catches →
  // passes through) is verified at runtime instead: pointing UPSTASH_* at an
  // unreachable host, /api/auth/login still reaches the handler (never 429)
  // and the middleware logs "check failed, allowing request". A unit case is
  // omitted because a throwing spy trips vitest's error attribution even when
  // the code under test catches the error.
});
