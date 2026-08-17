"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import {
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
import {
  HubShell,
  HubHeader,
  HubProgressBanner,
  HubActionGrid,
  type HubActionCardDef,
} from "@/components/hub/HubKit";

// The ЭШ hub — THE reference hub design (see components/hub/HubKit.tsx:
// SAT and IB are built to look like this page, never the reverse).
// Content is Mongolian by design.
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
  // next-path back to progress, matching the test-gating pattern.
  const progressBannerHref = isAuthenticated
    ? "/analytics"
    : `/sign-in?next=${encodeURIComponent("/analytics")}`;

  // Free first (top-left where eyes land), Premium second.
  const actionCards: HubActionCardDef[] = [
    {
      href: "/practice/esh/test?type=previous",
      title: "Өмнө жилийн тестүүд",
      subtitle: "Шалгалт · 20 тест",
      icon: Archive,
      badge: { label: "Үнэгүй", tone: "accent" },
    },
    {
      href: "/practice/esh/test?type=premium",
      title: "Дадлага тестүүд",
      subtitle: "Premium · 14 тест · Түгжээтэй",
      icon: FileText,
      badge: { label: "Түгжээтэй", tone: "muted" },
    },
    {
      href: "/practice/esh/practice",
      title: "Сэдвээр дадлагажих",
      subtitle: "Сул талаа сайжруулах",
      icon: Target,
    },
    {
      href: "/practice/esh/topics",
      title: "Сэдвээр суралцах",
      subtitle: "ЭШ-ын сэдвүүд · Жингээр эрэмбэлсэн",
      icon: BookOpen,
    },
  ];

  return (
    <HubShell>
      <HubHeader
        eyebrow="ЭШ Математик"
        title="Математикийн дадлага"
        statsLine={
          <>
            <span className="tabular">{allTests.length}</span> тест ·{" "}
            <span className="tabular">{totalQuestions}</span> бодлого
          </>
        }
        aside={
          mounted && progress.totalTestsTaken > 0 ? (
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
          ) : undefined
        }
      />

      {/* Quick stats */}
      {mounted && progress.totalTestsTaken > 0 && (
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-px mb-10" style={{ background: "var(--line)" }}>
          {[
            { lbl: "Тест бодсон", v: progress.totalTestsTaken },
            { lbl: "Бодлого бодсон", v: progress.totalQuestionsAnswered },
            { lbl: "Энэ долоо хоногт", v: progress.weeklyActivity.thisWeek },
            { lbl: "Тэмдэглэсэн", v: progress.flaggedCount },
          ].map((s) => (
            <div key={s.lbl} className="p-5" style={{ background: "var(--bg)" }}>
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

      <HubProgressBanner
        href={progressBannerHref}
        icon={BarChart3}
        eyebrow="Ахиц"
        title="Гүйцэтгэлийн дэлгэрэнгүй"
        subtitle={
          mounted && progress.totalTestsTaken > 0
            ? `${progress.averageAccuracy}% дундаж · ${progress.totalTestsTaken} тест бодсон`
            : "Тест бодож эхлээд ахицаа хяна"
        }
        cta="Бүтнээр харах"
      />

      <HubActionGrid cards={actionCards} />

      {/* Coming Soon — aggregated roadmap surface. One block, per-feature
          waitlist source for conversion research. No routes. */}
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
              style={{ fontWeight: 400, fontSize: 20, letterSpacing: "-0.02em", color: "var(--fg)" }}
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
                    upgrade.open({ source: f.source, title, description: desc })
                  }
                  className="w-full text-left px-5 py-4 flex items-center gap-4 transition-colors hover:opacity-90"
                  style={{
                    background: "var(--bg)",
                    borderTop: i === 0 ? "none" : "1px solid var(--line)",
                  }}
                >
                  <span
                    className="w-9 h-9 rounded-md flex items-center justify-center shrink-0"
                    style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
                  >
                    <Icon className="w-4 h-4" />
                  </span>
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2">
                      <span className="text-[14px]" style={{ color: "var(--fg)" }}>
                        {title}
                      </span>
                      <ComingSoonBadge variant="inline" />
                    </div>
                    <p className="text-[12.5px] mt-0.5" style={{ color: "var(--fg-2)" }}>
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
          <div style={{ border: "1px solid var(--line)", borderRadius: 12, overflow: "hidden" }}>
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
                    <div className="mono tabular text-[11px] mt-0.5" style={{ color: "var(--fg-3)" }}>
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
    </HubShell>
  );
}
