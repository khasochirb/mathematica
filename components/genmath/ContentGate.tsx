"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { ArrowLeft, Lock } from "lucide-react";
import { useAuth } from "@/lib/auth-context";

// Signed-in gate for course CONTENT (lessons, practice, tests, placement).
// Hubs and topic lists stay public so visitors can see what exists; opening
// the material itself requires an account. After signing in, `?next=` returns
// the learner to the exact page they tried to open.
export default function ContentGate({
  children,
  backHref,
  backLabel = "Back",
}: {
  children: React.ReactNode;
  backHref: string;
  backLabel?: string;
}) {
  const { isAuthenticated, loading } = useAuth();
  const pathname = usePathname();

  // While the session is being restored, hold a quiet placeholder so
  // signed-in users never see the lock flash.
  if (loading) {
    return (
      <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }} aria-busy="true" />
    );
  }

  if (!isAuthenticated) {
    const next = encodeURIComponent(pathname || backHref);
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center px-4" style={{ background: "var(--bg)" }}>
        <div className="card-edit p-8 text-center gm-step" style={{ maxWidth: 420 }}>
          <span className="mx-auto grid h-12 w-12 place-items-center rounded-full" style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)" }}>
            <Lock className="h-5 w-5" style={{ color: "var(--accent)" }} />
          </span>
          <h1 className="serif mt-4" style={{ fontWeight: 400, fontSize: 26, letterSpacing: "-0.02em", color: "var(--fg)" }}>
            Sign in to open this
          </h1>
          <p className="mt-2 text-[14px]" style={{ color: "var(--fg-2)", lineHeight: 1.55 }}>
            Lessons, practice sets, and tests are free with an account — signing in
            keeps your progress and placement in one place.
          </p>
          <div className="mt-5 flex flex-col gap-2">
            <Link href={`/sign-in?next=${next}`} className="btn btn-primary w-full">
              Sign in
            </Link>
            <Link href={`/sign-up`} className="btn btn-line w-full">
              Create a free account
            </Link>
          </div>
          <Link href={backHref} className="mt-4 inline-flex items-center gap-1.5 text-[13px]" style={{ color: "var(--fg-2)" }}>
            <ArrowLeft className="h-3.5 w-3.5" /> {backLabel}
          </Link>
        </div>
      </div>
    );
  }

  return <>{children}</>;
}
