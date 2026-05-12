"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import {
  ArrowLeft,
  FileText,
  Target,
  BookOpen,
  BarChart3,
  ChevronRight,
  Archive,
} from "lucide-react";
import ComingSoonBadge from "@/components/ComingSoonBadge";
import useESHProgress from "@/lib/use-esh-progress";
import {
  getTestsForUser,
  getQuestionsForUser,
} from "@/lib/esh-questions";
import { useAuth } from "@/lib/auth-context";
import {
  COMING_SOON_FEATURES,
  useUpgradeModal,
} from "@/lib/upgrade-modal-context";
import { useLang } from "@/lib/lang-context";

export default function ESHHubPage() {
  const [mounted, setMounted] = useState(false);
  const progress = useESHProgress();
  const { isAuthenticated, isSubscribed } = useAuth();
  const upgrade = useUpgradeModal();
  const { lang } = useLang();

  useEffect(() => setMounted(true), []);

  const allTests = getTestsForUser(isSubscribed);
  const totalQuestions = getQuestionsForUser(isSubscribed).length;

  // Anonymous click on the progress banner falls through to sign-in with a
  // next-path back to progress, matching the 5a/5b/5c gating pattern.
  const progressBannerHref = isAuthenticated
    ? "/practice/esh/progress"
    : `/sign-in?next=${encodeURIComponent("/practice/esh/progress")}`;

  // Free first (top-left where eyes land), Premium second. The reorder is
  // the bigger funnel win — users used to click "Дадлага тестүүд" expecting
  // free access, hit the locked screen, and bounce. Now the free
  // past-papers card gets first-card visibility.
  const actionCards: Array<{
    href: string;
    title: string;
    subtitle: string;
    icon: typeof FileText;
    badge?: "free" | "locked";
  }> = [
    {
      href: "/practice/esh/test?type=previous",
      title: "Өмнө жилийн тестүүд",
      subtitle: "Бодит шалгалт · 20 тест",
      icon: Archive,
      badge: "free",
    },
    {
      href: "/practice/esh/test?type=premium",
      title: "Дадлага тестүүд",
      subtitle: "Premium · 14 тест · Түгжээтэй",
      icon: FileText,
      badge: "locked",
    },
    {
      href: "/practice/esh/practice",
      title: "Сэдвээр дадлагажих",
      subtitle: "Сул талаа сайжруулах",
      icon: Target,
    },
    {
      href: "/practice/esh/learn",
      title: "Суралцах",
      subtitle: "Сэдвийн материал, томьёо",
      icon: BookOpen,
    },
  ];

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div
          className="flex items-end justify-between gap-3 mb-10 pb-6"
          style={{ borderBottom: "1px solid var(--line)" }}
        >
          <div className="flex items-end gap-4">
            <Link
              href="/practice"
              className="btn btn-ghost"
              style={{ padding: "8px 10px" }}
              aria-label="Back"
            >
              <ArrowLeft className="w-4 h-4" />
            </Link>
            <div>
              <div className="eyebrow mb-1.5">ЭЕШ Математик</div>
              <h1
                className="serif"
                style={{
                  fontWeight: 400,
                  fontSize: "clamp(32px, 4vw, 44px)",
                  letterSpacing: "-0.03em",
                  lineHeight: 1,
                  color: "var(--fg)",
                }}
              >
                Математикийн дадлага
              </h1>
              <p className="mono mt-2 text-[12px]" style={{ color: "var(--fg-2)" }}>
                <span className="tabular">{allTests.length}</span> тест ·{" "}
                <span className="tabular">{totalQuestions}</span> бодлого
              </p>
            </div>
          </div>
          {mounted && progress.totalTestsTaken > 0 && (
            <div className="text-right">
              <div className="eyebrow">ДУНДАЖ</div>
              <div
                className="serif tabular"
                style={{
                  fontSize: 44,
                  letterSpacing: "-0.03em",
                  lineHeight: 1,
                  color:
                    progress.averageAccuracy >= 80
                      ? "var(--accent)"
                      : progress.averageAccuracy >= 50
                        ? "var(--warn)"
                        : "var(--danger)",
                  marginTop: 4,
                }}
              >
                {progress.averageAccuracy}%
              </div>
            </div>
          )}
        </div>

        {/* Quick stats */}
        {mounted && progress.totalTestsTaken > 0 && (
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-px mb-10" style={{ background: "var(--line)" }}>
            {[
              { lbl: "Тест бодсон", v: progress.totalTestsTaken },
              { lbl: "Бодлого бодсон", v: progress.totalQuestionsAnswered },
              { lbl: "Энэ долоо хоногт", v: progress.weeklyActivity.thisWeek },
              { lbl: "Тэмдэглэсэн", v: progress.flaggedCount },
            ].map((s) => (
              <div
                key={s.lbl}
                className="p-5"
                style={{ background: "var(--bg)" }}
              >
                <div className="eyebrow">{s.lbl}</div>
                <div
                  className="serif tabular mt-2"
                  style={{ fontSize: 28, letterSpacing: "-0.02em", color: "var(--fg)" }}
                >
                  {s.v}
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Recommendation banner */}
        {mounted && progress.practiceRecommendation && (
          <div
            className="mb-10 p-5 flex gap-3 items-start"
            style={{
              background: "var(--accent-wash)",
              border: "1px solid var(--accent-line)",
              borderRadius: 12,
            }}
          >
            <span className="badge-edit badge-accent">ЗӨВЛӨГӨӨ</span>
            <p className="serif text-[15px] leading-snug" style={{ color: "var(--fg-1)" }}>
              {progress.practiceRecommendation}
            </p>
          </div>
        )}

        {/* Progress banner — visually distinct destination, not an action card.
            Full-width, accent-tinted, links to /practice/esh/progress (or /sign-in
            for anonymous). Sits above the 2x2 action grid. */}
        <Link
          href={progressBannerHref}
          className="block mb-4 p-5 group transition-colors"
          style={{
            background: "var(--bg-1)",
            border: "1px solid var(--accent-line)",
            borderRadius: 12,
          }}
        >
          <div className="flex items-center gap-4">
            <div
              className="w-11 h-11 rounded-md flex items-center justify-center shrink-0"
              style={{
                background: "var(--accent-wash)",
                border: "1px solid var(--accent-line)",
                color: "var(--accent)",
              }}
            >
              <BarChart3 className="w-5 h-5" />
            </div>
            <div className="flex-1 min-w-0">
              <div className="eyebrow" style={{ color: "var(--accent)" }}>
                Ахиц
              </div>
              <h2
                className="serif mt-1"
                style={{
                  fontWeight: 400,
                  fontSize: 22,
                  letterSpacing: "-0.02em",
                  color: "var(--fg)",
                  lineHeight: 1.1,
                }}
              >
                Гүйцэтгэлийн дэлгэрэнгүй
              </h2>
              <p
                className="text-[13px] mt-1"
                style={{ color: "var(--fg-2)" }}
              >
                {mounted && progress.totalTestsTaken > 0
                  ? `${progress.averageAccuracy}% дундаж · ${progress.totalTestsTaken} тест бодсон`
                  : "Тест бодож эхлээд ахицаа хяна"}
              </p>
            </div>
            <span
              className="mono text-[11px] uppercase shrink-0 hidden sm:inline-flex items-center gap-1"
              style={{ color: "var(--accent)", letterSpacing: "0.06em" }}
            >
              Бүтнээр харах
              <ChevronRight className="w-3.5 h-3.5 transition-transform group-hover:translate-x-0.5" />
            </span>
            <ChevronRight
              className="w-5 h-5 sm:hidden transition-transform group-hover:translate-x-0.5"
              style={{ color: "var(--accent)" }}
            />
          </div>
        </Link>

        {/* 2x2 action card grid — equal-weight cards, 2 cols on desktop,
            1-col stack on mobile. */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {actionCards.map((c) => {
            const Icon = c.icon;
            return (
              <Link key={c.href} href={c.href} className="card-edit p-6 group block">
                <div className="flex items-start justify-between mb-4">
                  <div
                    className="w-10 h-10 rounded-md flex items-center justify-center"
                    style={{
                      background: "var(--bg-2)",
                      border: "1px solid var(--line)",
                      color: "var(--accent)",
                    }}
                  >
                    <Icon className="w-4 h-4" />
                  </div>
                  <ChevronRight
                    className="w-4 h-4 transition-transform group-hover:translate-x-0.5"
                    style={{ color: "var(--fg-3)" }}
                  />
                </div>
                <div className="flex items-center gap-2 mb-1.5 flex-wrap">
                  <h2
                    className="serif"
                    style={{
                      fontWeight: 400,
                      fontSize: 22,
                      letterSpacing: "-0.02em",
                      color: "var(--fg)",
                      lineHeight: 1.1,
                    }}
                  >
                    {c.title}
                  </h2>
                  {c.badge === "free" && (
                    <span
                      className="mono text-[10px] uppercase px-2 py-0.5 rounded-full"
                      style={{
                        background: "color-mix(in oklch, var(--accent) 14%, transparent)",
                        color: "var(--accent)",
                        letterSpacing: "0.08em",
                      }}
                    >
                      Үнэгүй
                    </span>
                  )}
                  {c.badge === "locked" && (
                    <span
                      className="mono text-[10px] uppercase px-2 py-0.5 rounded-full"
                      style={{
                        background: "var(--bg-2)",
                        border: "1px solid var(--line)",
                        color: "var(--fg-3)",
                        letterSpacing: "0.08em",
                      }}
                    >
                      Түгжээтэй
                    </span>
                  )}
                </div>
                <p className="text-[13px]" style={{ color: "var(--fg-2)" }}>
                  {c.subtitle}
                </p>
              </Link>
            );
          })}
        </div>

        {/* Coming Soon — aggregated roadmap surface. One block, five features,
            per-feature waitlist source for conversion research. No routes. */}
        <div
          className="mt-12 rounded-xl overflow-hidden"
          style={{ border: "1px solid var(--line)" }}
        >
          <div
            className="px-5 py-4 flex items-center justify-between gap-3"
            style={{ background: "var(--bg-1)", borderBottom: "1px solid var(--line)" }}
          >
            <div>
              <div className="eyebrow">Удахгүй</div>
              <h3
                className="serif mt-1"
                style={{
                  fontWeight: 400,
                  fontSize: 20,
                  letterSpacing: "-0.02em",
                  color: "var(--fg)",
                }}
              >
                Бэлдэж буй боломжууд
              </h3>
            </div>
            <ComingSoonBadge />
          </div>
          <ul>
            {COMING_SOON_FEATURES.map((f, i) => {
              const Icon = f.icon;
              const title = lang === "mn" ? f.title.mn : f.title.en;
              const desc = lang === "mn" ? f.desc.mn : f.desc.en;
              return (
                <li key={f.key}>
                  <button
                    type="button"
                    onClick={() =>
                      upgrade.open({
                        source: f.source,
                        title,
                        description: desc,
                      })
                    }
                    className="w-full text-left px-5 py-4 flex items-center gap-4 transition-colors hover:opacity-90"
                    style={{
                      background: "var(--bg)",
                      borderTop: i === 0 ? "none" : "1px solid var(--line)",
                    }}
                  >
                    <span
                      className="w-9 h-9 rounded-md flex items-center justify-center shrink-0"
                      style={{
                        background: "var(--bg-2)",
                        border: "1px solid var(--line)",
                        color: "var(--fg-2)",
                      }}
                    >
                      <Icon className="w-4 h-4" />
                    </span>
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center gap-2">
                        <span
                          className="text-[14px]"
                          style={{ color: "var(--fg)" }}
                        >
                          {title}
                        </span>
                        <ComingSoonBadge variant="inline" />
                      </div>
                      <p
                        className="text-[12.5px] mt-0.5"
                        style={{ color: "var(--fg-2)" }}
                      >
                        {desc}
                      </p>
                    </div>
                    <span
                      className="mono text-[10px] uppercase shrink-0"
                      style={{ color: "var(--accent)", letterSpacing: "0.08em" }}
                    >
                      Мэдэгдэх →
                    </span>
                  </button>
                </li>
              );
            })}
          </ul>
        </div>

        {/* Recent test results */}
        {mounted && progress.completedSessions.length > 0 && (
          <div className="mt-12">
            <div className="eyebrow mb-4">Сүүлийн шалгалтууд</div>
            <div
              style={{
                border: "1px solid var(--line)",
                borderRadius: 12,
                overflow: "hidden",
              }}
            >
              {progress.completedSessions.slice(0, 5).map((s, i) => (
                <Link
                  key={s.id}
                  href={`/practice/esh/test/${s.testKey.toLowerCase()}/results?session=${s.id}`}
                  className="flex items-center gap-4 px-5 py-3.5 transition-colors hover:opacity-90"
                  style={{
                    background: "var(--bg-1)",
                    borderTop: i === 0 ? "none" : "1px solid var(--line)",
                  }}
                >
                  <span
                    className="badge-edit"
                    style={{
                      minWidth: 44,
                      justifyContent: "center",
                      color: "var(--accent)",
                      borderColor: "var(--accent-line)",
                      background: "var(--accent-wash)",
                    }}
                  >
                    {s.testKey}
                  </span>
                  <div className="flex-1 min-w-0">
                    <div className="text-[14px]" style={{ color: "var(--fg)" }}>
                      Тест {s.testKey}
                    </div>
                    {s.completedAt && (
                      <div
                        className="mono tabular text-[11px] mt-0.5"
                        style={{ color: "var(--fg-3)" }}
                      >
                        {new Date(s.completedAt).toLocaleDateString("mn-MN")}
                      </div>
                    )}
                  </div>
                  <span
                    className="serif tabular"
                    style={{
                      fontSize: 18,
                      letterSpacing: "-0.01em",
                      color:
                        (s.score?.accuracy || 0) >= 80
                          ? "var(--accent)"
                          : (s.score?.accuracy || 0) >= 50
                            ? "var(--warn)"
                            : "var(--danger)",
                    }}
                  >
                    {s.score?.accuracy || 0}%
                  </span>
                  <ChevronRight className="w-4 h-4" style={{ color: "var(--fg-3)" }} />
                </Link>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
