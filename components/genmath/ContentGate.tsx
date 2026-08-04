"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { ArrowLeft, Lock, Sparkles } from "lucide-react";
import { useAuth } from "@/lib/auth-context";
import { useUpgradeModal } from "@/lib/upgrade-modal-context";
import { useLang } from "@/lib/lang-context";
import { accessFor, isTopicFree } from "@/lib/course-access";

// The gate every course CONTENT route passes through (lessons, practice,
// tests, placement). Two locks, in order:
//
//   1. Sign-in — anonymous readers must have an account, so progress and
//      placement have somewhere to live.
//   2. Premium — every course opens its FIRST topic free; the rest needs a
//      subscription (policy: lib/course-access.ts).
//
// Pass `courseKey` + `topicSlug` to arm the Premium lock. Omit them (or pass
// `free`) for content that is free by nature — placement tests, hub pages.
// A route that forgets them still requires sign-in, so the failure mode is
// "too open by one tier", never "content leaks to anonymous visitors";
// lib/course-access.test.ts asserts every content route passes them.
export default function ContentGate({
  children,
  backHref,
  backLabel = "Back",
  courseKey,
  topicSlug,
  free,
}: {
  children: React.ReactNode;
  backHref: string;
  backLabel?: string;
  /** The /math segment for this course — "5", "integrated-3", "algebra-1". */
  courseKey?: string;
  /** The topic/unit slug being opened. */
  topicSlug?: string;
  /** Force-free content (placement tests, samplers). Overrides the policy. */
  free?: boolean;
}) {
  const { isAuthenticated, isSubscribed, loading } = useAuth();
  const { open: openUpgrade } = useUpgradeModal();
  const { lang } = useLang();
  const pathname = usePathname();
  const mn = lang === "mn";

  // While the session is being restored, hold a quiet placeholder so
  // signed-in users never see the lock flash.
  if (loading) {
    return (
      <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }} aria-busy="true" />
    );
  }

  const isFree =
    free ?? (courseKey && topicSlug ? isTopicFree(courseKey, topicSlug) : true);
  const verdict = accessFor({ isAuthenticated, isSubscribed, free: isFree });

  if (verdict === "open") return <>{children}</>;

  const next = encodeURIComponent(pathname || backHref);

  if (verdict === "sign-in") {
    return (
      <GateCard
        backHref={backHref}
        backLabel={backLabel}
        title={mn ? "Нэвтэрч ороод үзнэ үү" : "Sign in to open this"}
        body={
          mn
            ? "Энэ сэдэв үнэгүй — бүртгэлтэй бол ахиц, түвшингээ нэг дор хадгална."
            : "This topic is free — signing in keeps your progress and placement in one place."
        }
        actions={
          <>
            <Link href={`/sign-in?next=${next}`} className="btn btn-primary w-full">
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

  // Premium lock. Anonymous readers get sign-in first (an account is the
  // cheaper next step, and the upgrade flow needs one anyway).
  return (
    <GateCard
      premium
      backHref={backHref}
      backLabel={backLabel}
      title={mn ? "Энэ хэсэг Премиумд нээлттэй" : "This one is Premium"}
      body={
        mn
          ? "Хичээл бүрийн эхний сэдэв үнэгүй. Үлдсэн сэдэв, дасгал, шалгалтыг Премиум эрхээр нээнэ."
          : "The first topic of every course is free. Premium opens the rest — every topic, its practice sets and its tests."
      }
      actions={
        isAuthenticated ? (
          <button
            onClick={() => openUpgrade({ source: "course_content_lock" })}
            className="btn btn-primary w-full inline-flex items-center justify-center gap-1.5"
          >
            <Sparkles className="h-3.5 w-3.5" />
            {mn ? "Премиум болох" : "Unlock with Premium"}
          </button>
        ) : (
          <>
            <Link href={`/sign-in?next=${next}`} className="btn btn-primary w-full">
              {mn ? "Нэвтрэх" : "Sign in"}
            </Link>
            <Link href="/sign-up" className="btn btn-line w-full">
              {mn ? "Үнэгүй бүртгүүлэх" : "Create a free account"}
            </Link>
          </>
        )
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
  premium = false,
}: {
  title: string;
  body: string;
  actions: React.ReactNode;
  backHref: string;
  backLabel: string;
  premium?: boolean;
}) {
  return (
    <div
      className="min-h-screen pt-20 flex items-center justify-center px-4"
      style={{ background: "var(--bg)" }}
    >
      <div className="card-edit p-8 text-center gm-step" style={{ maxWidth: 420 }}>
        <span
          className="mx-auto grid h-12 w-12 place-items-center rounded-full"
          style={{
            background: premium ? "color-mix(in oklch, var(--warn) 12%, transparent)" : "var(--accent-wash)",
            border: `1px solid ${premium ? "color-mix(in oklch, var(--warn) 40%, transparent)" : "var(--accent-line)"}`,
          }}
        >
          <Lock
            className="h-5 w-5"
            style={{ color: premium ? "var(--warn, #d89620)" : "var(--accent)" }}
          />
        </span>
        <h1
          className="serif mt-4"
          style={{ fontWeight: 400, fontSize: 26, letterSpacing: "-0.02em", color: "var(--fg)" }}
        >
          {title}
        </h1>
        <p className="mt-2 text-[14px]" style={{ color: "var(--fg-2)", lineHeight: 1.55 }}>
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
