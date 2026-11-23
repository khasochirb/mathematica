"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { ArrowLeft, Lock } from "lucide-react";
import { useAuth } from "@/lib/auth-context";
import { useLang } from "@/lib/lang-context";
import { accessFor } from "@/lib/course-access";

// The gate every course CONTENT route passes through (lessons, practice,
// tests, placement, problem bank). ONE lock: sign-in. Anonymous readers must
// have an account, so progress and placement have somewhere to live. The
// site is free (owner decision 2026-11-23), so every signed-in user is
// entitled to everything — there is no Premium wall any more
// (policy: lib/course-access.ts).
//
// `courseKey` / `topicSlug` / `free` are still accepted so routes keep
// declaring what they open; they no longer change the verdict.
export default function ContentGate({
  children,
  backHref,
  backLabel,
}: {
  children: React.ReactNode;
  backHref: string;
  backLabel?: string;
  /** The /math segment for this course — "5", "integrated-3", "algebra-1". */
  courseKey?: string;
  /** The topic/unit slug being opened. */
  topicSlug?: string;
  /** Content that is free by nature (placement tests, samplers). */
  free?: boolean;
}) {
  const { isAuthenticated, loading } = useAuth();
  const { lang } = useLang();
  const pathname = usePathname();
  const mn = lang === "mn";
  const backText = backLabel
    ? mn
      ? mnBackLabel(backLabel)
      : backLabel
    : mn
      ? "Буцах"
      : "Back";

  // While the session is being restored, hold a quiet placeholder so
  // signed-in users never see the lock flash.
  if (loading) {
    return (
      <div
        className="min-h-screen pt-20"
        style={{ background: "var(--bg)" }}
        aria-busy="true"
      />
    );
  }

  const verdict = accessFor({ isAuthenticated });

  if (verdict === "open") return <>{children}</>;

  const next = encodeURIComponent(pathname || backHref);

  return (
    <GateCard
      backHref={backHref}
      backLabel={backText}
      title={mn ? "Нэвтэрч ороод үзнэ үү" : "Sign in to open this"}
      body={
        mn
          ? "Энэ сэдэв үнэгүй — бүртгэлтэй бол ахиц, түвшингээ нэг дор хадгална."
          : "This topic is free — signing in keeps your progress and placement in one place."
      }
      actions={
        <>
          <Link
            href={`/sign-in?next=${next}`}
            className="btn btn-primary w-full"
          >
            {mn ? "Нэвтрэх" : "Sign in"}
          </Link>
          <Link href="/sign-up" className="btn btn-line w-full">
            {mn ? "Үнэгүй бүртгүүлэх" : "Create a free account"}
          </Link>
        </>
      }
    />
  );
}

function GateCard({
  title,
  body,
  actions,
  backHref,
  backLabel,
}: {
  title: string;
  body: string;
  actions: React.ReactNode;
  backHref: string;
  backLabel: string;
}) {
  return (
    <div
      className="min-h-screen pt-20 flex items-center justify-center px-4"
      style={{ background: "var(--bg)" }}
    >
      <div
        className="card-edit p-8 text-center gm-step"
        style={{ maxWidth: 420 }}
      >
        <span
          className="mx-auto grid h-12 w-12 place-items-center rounded-full"
          style={{
            background: "var(--accent-wash)",
            border: "1px solid var(--accent-line)",
          }}
        >
          <Lock className="h-5 w-5" style={{ color: "var(--accent)" }} />
        </span>
        <h1
          className="serif mt-4"
          style={{
            fontWeight: 400,
            fontSize: 26,
            letterSpacing: "-0.02em",
            color: "var(--fg)",
          }}
        >
          {title}
        </h1>
        <p
          className="mt-2 text-[14px]"
          style={{ color: "var(--fg-2)", lineHeight: 1.55 }}
        >
          {body}
        </p>
        <div className="mt-5 flex flex-col gap-2">{actions}</div>
        <Link
          href={backHref}
          className="mt-4 inline-flex items-center gap-1.5 text-[13px]"
          style={{ color: "var(--fg-2)" }}
        >
          <ArrowLeft className="h-3.5 w-3.5" /> {backLabel}
        </Link>
      </div>
    </div>
  );
}

// Pages pass their back link in English ("Back to topic", "Back to Grade 7").
// The set is small and fixed, so it is mapped here rather than at 40 call
// sites; anything unrecognised falls back to a plain «Буцах».
function mnBackLabel(en: string): string {
  if (en === "Back to topic") return "Сэдэв рүү буцах";
  if (en === "Back to Courses") return "Курсууд руу буцах";
  if (en === "Back to Geometry") return "Геометр рүү буцах";
  const grade = /^Back to Grade (\d+)$/.exec(en);
  if (grade) return `${grade[1]}-р анги руу буцах`;
  return "Буцах";
}
