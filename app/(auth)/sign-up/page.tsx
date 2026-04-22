"use client";

import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
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

const labelStyle: React.CSSProperties = {
  display: "block",
  fontSize: 11,
  color: "var(--fg-3)",
  letterSpacing: "0.08em",
  textTransform: "uppercase",
  marginBottom: 6,
  fontFamily: "var(--font-mono), ui-monospace, monospace",
};

export default function SignUpPage() {
  const router = useRouter();
  const { refresh } = useAuth();
  const [form, setForm] = useState({
    displayName: "",
    username: "",
    email: "",
    password: "",
  });
  const [showPw, setShowPw] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError("");
    try {
      const res = await api.auth.register(form);
      setToken(res.accessToken);
      await refresh();
      router.push("/dashboard");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Could not create account. Please try again.");
    } finally {
      setLoading(false);
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
            <span className="badge-edit badge-accent mb-3 inline-flex">Free to join</span>
            <h1
              className="serif mt-3"
              style={{ fontWeight: 400, fontSize: 32, letterSpacing: "-0.02em", color: "var(--fg)" }}
            >
              Create your <em className="serif-italic" style={{ color: "var(--accent)" }}>account</em>.
            </h1>
            <p className="mt-1.5 text-[13px]" style={{ color: "var(--fg-2)" }}>
              Start practicing math for free today.
            </p>
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

          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="grid grid-cols-2 gap-3">
              <div>
                <label style={labelStyle}>Full name</label>
                <input
                  type="text"
                  required
                  autoFocus
                  value={form.displayName}
                  onChange={(e) => setForm({ ...form, displayName: e.target.value })}
                  placeholder="Bolor-Erdene"
                  style={inputStyle}
                />
              </div>
              <div>
                <label style={labelStyle}>Username</label>
                <input
                  type="text"
                  required
                  value={form.username}
                  onChange={(e) => setForm({ ...form, username: e.target.value.toLowerCase().replace(/\s/g, "") })}
                  placeholder="bolorer"
                  style={inputStyle}
                />
              </div>
            </div>
            <div>
              <label style={labelStyle}>Email</label>
              <input
                type="email"
                required
                value={form.email}
                onChange={(e) => setForm({ ...form, email: e.target.value })}
                placeholder="you@example.com"
                style={inputStyle}
              />
            </div>
            <div>
              <label style={labelStyle}>Password</label>
              <div className="relative">
                <input
                  type={showPw ? "text" : "password"}
                  required
                  minLength={8}
                  value={form.password}
                  onChange={(e) => setForm({ ...form, password: e.target.value })}
                  placeholder="At least 8 characters"
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
              {loading ? "Creating account..." : "Create Account"}
            </button>
          </form>

          <p className="mt-6 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
            Already have an account?{" "}
            <Link href="/sign-in" style={{ color: "var(--accent)" }}>
              Log in
            </Link>
          </p>
        </div>

        <p className="mt-4 text-center mono text-[11px]" style={{ color: "var(--fg-3)", letterSpacing: "0.04em" }}>
          By signing up, you agree to our{" "}
          <Link href="/terms" className="underline" style={{ color: "var(--fg-2)" }}>
            Terms
          </Link>{" "}
          and{" "}
          <Link href="/privacy" className="underline" style={{ color: "var(--fg-2)" }}>
            Privacy
          </Link>
          .
        </p>
      </div>
    </div>
  );
}
