"use client";

import { Suspense, useEffect, useMemo, useState } from "react";
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { Eye, EyeOff } from "lucide-react";
import Image from "next/image";
import { api, setToken } from "@/lib/api";
import { useAuth } from "@/lib/auth-context";

const inputStyle: React.CSSProperties = {
  width: "100%",
  padding: "10px 12px",
  fontSize: 14,
  background: "var(--bg-1)",
  border: "1px solid var(--line)",
  borderRadius: 8,
  color: "var(--fg)",
  outline: "none",
  transition: "border-color .15s var(--ease), background .15s var(--ease)",
};

const LOCKOUT_KEY = "mp-resend-lockout-until";
const LOCKOUT_MS = 60_000;

type BannerState =
  | { kind: "none" }
  | { kind: "confirmed" }
  | { kind: "expired"; email: string }
  | { kind: "error"; message: string }
  | { kind: "session_expired" }
  | { kind: "resend_sent" };

function SignInInner() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const { refresh } = useAuth();
  const [form, setForm] = useState({ email: "", password: "" });
  const [showPw, setShowPw] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Derive initial banner state from URL params.
  // Precedence: confirmed > error_code > error > session_expired.
  const initialBanner = useMemo<BannerState>(() => {
    if (searchParams.get("confirmed") === "true") return { kind: "confirmed" };
    const errorCode = searchParams.get("error_code");
    if (errorCode === "otp_already_used") return { kind: "confirmed" }; // treat as success
    if (errorCode === "otp_expired") {
      return { kind: "expired", email: searchParams.get("email") ?? "" };
    }
    const errorMsg = searchParams.get("error");
    if (errorMsg) {
      try {
        return { kind: "error", message: decodeURIComponent(errorMsg) };
      } catch {
        return { kind: "error", message: errorMsg };
      }
    }
    if (searchParams.get("reason") === "session_expired") {
      return { kind: "session_expired" };
    }
    return { kind: "none" };
  }, [searchParams]);

  const [bannerOverride, setBannerOverride] = useState<BannerState | null>(null);
  const banner = bannerOverride ?? initialBanner;

  // Resend form state (only used when banner.kind === 'expired')
  const [resendEmail, setResendEmail] = useState(
    initialBanner.kind === "expired" ? initialBanner.email : ""
  );
  const [resendLoading, setResendLoading] = useState(false);
  const [resendError, setResendError] = useState("");
  const [lockoutRemaining, setLockoutRemaining] = useState(0);

  // Lockout countdown — shares localStorage key with /sign-up/check-email
  // (cross-tab so a user can't bypass rate limit by opening a second tab)
  useEffect(() => {
    if (typeof window === "undefined") return;
    const tick = () => {
      const until = Number(localStorage.getItem(LOCKOUT_KEY) ?? 0);
      const remaining = Math.max(0, Math.ceil((until - Date.now()) / 1000));
      setLockoutRemaining(remaining);
    };
    tick();
    const id = window.setInterval(tick, 1000);
    return () => window.clearInterval(id);
  }, []);

  async function handleResend(e: React.FormEvent) {
    e.preventDefault();
    if (lockoutRemaining > 0 || resendLoading) return;
    setResendLoading(true);
    setResendError("");
    try {
      await api.auth.resend({ email: resendEmail });
      localStorage.setItem(LOCKOUT_KEY, String(Date.now() + LOCKOUT_MS));
      setBannerOverride({ kind: "resend_sent" });
    } catch (err) {
      setResendError(err instanceof Error ? err.message : "Couldn't resend. Try again.");
    } finally {
      setResendLoading(false);
    }
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError("");
    try {
      const res = await api.auth.login(form);
      setToken(res.accessToken);
      await refresh();
      router.push("/dashboard");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Invalid email or password.");
    } finally {
      setLoading(false);
    }
  }

  // Form login error takes precedence over URL-driven banners.
  const showLoginError = !!error;

  return (
    <div
      className="min-h-screen flex items-center justify-center px-4 pt-20 pb-12 relative overflow-hidden"
      style={{ background: "var(--bg)" }}
    >
      <div
        className="absolute top-1/3 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[720px] h-[460px] pointer-events-none"
        style={{
          background:
            "radial-gradient(closest-side, color-mix(in oklch, var(--accent) 14%, transparent), transparent 70%)",
          filter: "blur(40px)",
        }}
      />

      <div className="w-full max-w-md relative">
        <div className="text-center mb-8">
          <Link href="/" className="inline-flex items-center gap-2.5 group">
            <span className="inline-block w-2 h-2 rounded-sm" style={{ background: "var(--accent)" }} />
            <Image src="/images/mp.png" alt="Mongol Potential" width={32} height={32} className="rounded-md" />
            <span className="font-semibold text-[15px] tracking-tight" style={{ color: "var(--fg)" }}>
              Mongol Potential
            </span>
          </Link>
        </div>

        <div className="card-edit p-8">
          <div className="mb-6">
            <div className="eyebrow mb-2">Account · Sign In</div>
            <h1
              className="serif"
              style={{ fontWeight: 400, fontSize: 32, letterSpacing: "-0.02em", color: "var(--fg)" }}
            >
              Welcome <em className="serif-italic" style={{ color: "var(--accent)" }}>back</em>.
            </h1>
            <p className="mt-1.5 text-[13px]" style={{ color: "var(--fg-2)" }}>
              Log in to your account to continue practicing.
            </p>
          </div>

          {/* Login form error — highest precedence */}
          {showLoginError && (
            <div
              className="mb-5 p-3 rounded-md text-[13px]"
              style={{
                background: "rgba(239, 68, 68, 0.10)",
                border: "1px solid rgba(239, 68, 68, 0.30)",
                color: "var(--danger)",
              }}
            >
              {error}
            </div>
          )}

          {/* Confirmed (or otp_already_used, treated the same) */}
          {!showLoginError && banner.kind === "confirmed" && (
            <div
              className="mb-5 p-3 rounded-md text-[13px]"
              style={{
                background: "var(--accent-wash)",
                border: "1px solid var(--accent-line)",
                color: "var(--fg-2)",
              }}
            >
              Email confirmed — sign in below.
            </div>
          )}

          {/* After successful resend */}
          {!showLoginError && banner.kind === "resend_sent" && (
            <div
              className="mb-5 p-3 rounded-md text-[13px]"
              style={{
                background: "var(--accent-wash)",
                border: "1px solid var(--accent-line)",
                color: "var(--fg-2)",
              }}
            >
              Confirmation email sent. Check your inbox.
            </div>
          )}

          {/* Expired link — amber + inline resend form */}
          {!showLoginError && banner.kind === "expired" && (
            <div
              className="mb-5 p-3 rounded-md text-[13px]"
              style={{
                background: "color-mix(in oklch, var(--warn) 10%, transparent)",
                border: "1px solid color-mix(in oklch, var(--warn) 30%, transparent)",
                color: "var(--warn)",
              }}
            >
              <p className="mb-3">Your confirmation link expired. Enter your email to resend.</p>
              <form onSubmit={handleResend} className="space-y-2">
                <input
                  type="email"
                  required
                  value={resendEmail}
                  onChange={(e) => setResendEmail(e.target.value)}
                  placeholder="you@example.com"
                  style={{ ...inputStyle, fontSize: 13 }}
                  disabled={resendLoading || lockoutRemaining > 0}
                />
                <button
                  type="submit"
                  disabled={resendLoading || lockoutRemaining > 0 || !resendEmail}
                  className="btn btn-primary w-full"
                  style={{
                    padding: "8px 12px",
                    fontSize: 13,
                    opacity: resendLoading || lockoutRemaining > 0 || !resendEmail ? 0.6 : 1,
                  }}
                >
                  {resendLoading
                    ? "Sending…"
                    : lockoutRemaining > 0
                    ? `Resend in ${lockoutRemaining}s`
                    : "Resend confirmation"}
                </button>
                {resendError && (
                  <p className="text-[12px]" style={{ color: "var(--danger)" }}>
                    {resendError}
                  </p>
                )}
              </form>
            </div>
          )}

          {/* Generic error from URL */}
          {!showLoginError && banner.kind === "error" && (
            <div
              className="mb-5 p-3 rounded-md text-[13px]"
              style={{
                background: "rgba(239, 68, 68, 0.10)",
                border: "1px solid rgba(239, 68, 68, 0.30)",
                color: "var(--danger)",
              }}
            >
              {banner.message}
            </div>
          )}

          {/* Session expired (existing behavior) */}
          {!showLoginError && banner.kind === "session_expired" && (
            <div
              className="mb-5 p-3 rounded-md text-[13px]"
              style={{
                background: "color-mix(in oklch, var(--warn) 10%, transparent)",
                border: "1px solid color-mix(in oklch, var(--warn) 30%, transparent)",
                color: "var(--warn)",
              }}
            >
              Your session expired. Please sign in again.
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label
                className="block mono text-[11px] mb-1.5"
                style={{ color: "var(--fg-3)", letterSpacing: "0.08em", textTransform: "uppercase" }}
              >
                Email
              </label>
              <input
                type="email"
                required
                autoFocus
                value={form.email}
                onChange={(e) => setForm({ ...form, email: e.target.value })}
                placeholder="you@example.com"
                style={inputStyle}
              />
            </div>
            <div>
              <label
                className="block mono text-[11px] mb-1.5"
                style={{ color: "var(--fg-3)", letterSpacing: "0.08em", textTransform: "uppercase" }}
              >
                Password
              </label>
              <div className="relative">
                <input
                  type={showPw ? "text" : "password"}
                  required
                  value={form.password}
                  onChange={(e) => setForm({ ...form, password: e.target.value })}
                  placeholder="Your password"
                  style={{ ...inputStyle, paddingRight: 40 }}
                />
                <button
                  type="button"
                  onClick={() => setShowPw(!showPw)}
                  className="absolute right-3 top-1/2 -translate-y-1/2 transition-colors"
                  style={{ color: "var(--fg-3)" }}
                  aria-label={showPw ? "Hide password" : "Show password"}
                >
                  {showPw ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
                </button>
              </div>
            </div>
            <button
              type="submit"
              disabled={loading}
              className="btn btn-primary w-full"
              style={{ padding: "11px 14px", opacity: loading ? 0.6 : 1 }}
            >
              {loading ? "Logging in..." : "Log In"}
            </button>
          </form>

          <p className="mt-6 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
            Don&apos;t have an account?{" "}
            <Link href="/sign-up" style={{ color: "var(--accent)" }}>
              Sign up free
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}

export default function SignInPage() {
  return (
    <Suspense fallback={null}>
      <SignInInner />
    </Suspense>
  );
}
