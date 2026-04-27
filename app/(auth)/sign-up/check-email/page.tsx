"use client";

import { Suspense, useEffect, useState } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import Image from "next/image";
import { api } from "@/lib/api";

const LOCKOUT_KEY = "mp-resend-lockout-until";
const LOCKOUT_MS = 60_000;

function CheckEmailInner() {
  const searchParams = useSearchParams();
  const email = searchParams.get("email") ?? "";

  const [now, setNow] = useState<number>(() => Date.now());
  const [lockoutUntil, setLockoutUntil] = useState<number>(0);
  const [resending, setResending] = useState(false);
  const [error, setError] = useState("");
  const [successMsg, setSuccessMsg] = useState("");
  const [hasResent, setHasResent] = useState(false);

  // Restore an in-progress lockout if the user reloads or comes back to
  // this tab. localStorage (not sessionStorage) so the lockout shares
  // across tabs — prevents a user from bypassing the rate limit by
  // opening a second tab.
  useEffect(() => {
    const stored = localStorage.getItem(LOCKOUT_KEY);
    if (!stored) return;
    const ts = Number(stored);
    if (!Number.isNaN(ts) && ts > Date.now()) setLockoutUntil(ts);
  }, []);

  // Tick once per second only while a lockout is active.
  useEffect(() => {
    if (lockoutUntil <= now) return;
    const id = setInterval(() => setNow(Date.now()), 1000);
    return () => clearInterval(id);
  }, [lockoutUntil, now]);

  const secondsLeft = Math.max(0, Math.ceil((lockoutUntil - now) / 1000));
  const inLockout = secondsLeft > 0;

  async function handleResend() {
    if (!email || inLockout || resending) return;
    setError("");
    setSuccessMsg("");
    setResending(true);
    try {
      await api.auth.resend({ email });
      const until = Date.now() + LOCKOUT_MS;
      localStorage.setItem(LOCKOUT_KEY, String(until));
      setLockoutUntil(until);
      setHasResent(true);
      setSuccessMsg("Confirmation email sent again. Check your inbox.");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Couldn't resend. Try again in a moment.");
    } finally {
      setResending(false);
    }
  }

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
            <div className="eyebrow mb-2">Account · Confirm Email</div>
            <h1
              className="serif"
              style={{ fontWeight: 400, fontSize: 32, letterSpacing: "-0.02em", color: "var(--fg)" }}
            >
              Almost <em className="serif-italic" style={{ color: "var(--accent)" }}>there</em>.
            </h1>
            {email ? (
              <p className="mt-1.5 text-[13px]" style={{ color: "var(--fg-2)" }}>
                We sent a confirmation link to{" "}
                <strong style={{ color: "var(--fg)" }}>{email}</strong>. Click it to activate your account.
              </p>
            ) : (
              <p className="mt-1.5 text-[13px]" style={{ color: "var(--fg-2)" }}>
                We don&apos;t know which email to confirm.{" "}
                <Link href="/sign-up" style={{ color: "var(--accent)" }}>
                  Sign up again
                </Link>
                .
              </p>
            )}
          </div>

          {error && (
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
          {successMsg && (
            <div
              className="mb-5 p-3 rounded-md text-[13px]"
              style={{
                background: "var(--accent-wash)",
                border: "1px solid var(--accent-line)",
                color: "var(--fg-2)",
              }}
            >
              {successMsg}
              {hasResent && (
                <div className="mt-1 text-[12px]" style={{ color: "var(--fg-3)" }}>
                  Didn&apos;t get it? Check your spam folder.
                </div>
              )}
            </div>
          )}

          {email && (
            <button
              type="button"
              onClick={handleResend}
              disabled={inLockout || resending}
              className="btn btn-primary w-full"
              style={{ padding: "11px 14px", opacity: inLockout || resending ? 0.6 : 1 }}
            >
              {inLockout
                ? `Resend in ${secondsLeft}s`
                : resending
                ? "Sending..."
                : "Resend confirmation email"}
            </button>
          )}

          <p className="mt-6 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
            Wrong email?{" "}
            <Link href="/sign-up" style={{ color: "var(--accent)" }}>
              Sign up again
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}

export default function CheckEmailPage() {
  return (
    <Suspense fallback={null}>
      <CheckEmailInner />
    </Suspense>
  );
}
