"use client";

import Link from "next/link";
import {
  ArrowRight,
  Calculator,
  Flame,
  Sparkles,
  BookOpen,
  BarChart3,
  Lock,
} from "lucide-react";
import { useAuth } from "@/lib/auth-context";
import usePerformance from "@/lib/use-performance";
import { TOPICS } from "@/lib/esh-questions";
import topicsData from "@/data/learn/topics.json";

export default function PracticePage() {
  const { user, loading: authLoading } = useAuth();
  const perf = usePerformance();

  if (authLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center pt-20" style={{ background: "var(--bg)" }}>
        <div className="text-center">
          <div
            className="w-8 h-8 border-2 rounded-full animate-spin mx-auto mb-4"
            style={{ borderColor: "var(--accent)", borderTopColor: "transparent" }}
          />
          <p className="mono text-[12px]" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>LOADING...</p>
        </div>
      </div>
    );
  }

  if (!user) {
    return (
      <div className="min-h-screen flex items-center justify-center pt-20 px-4 relative overflow-hidden" style={{ background: "var(--bg)" }}>
        <div
          className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[720px] h-[460px] pointer-events-none"
          style={{
            background: "radial-gradient(closest-side, color-mix(in oklch, var(--accent) 12%, transparent), transparent 70%)",
            filter: "blur(40px)",
          }}
        />
        <div className="text-center max-w-sm relative">
          <div
            className="w-14 h-14 rounded-md flex items-center justify-center mx-auto mb-5"
            style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}
          >
            <Lock className="h-6 w-6" />
          </div>
          <div className="eyebrow mb-2">Authentication required</div>
          <h2 className="serif" style={{ fontWeight: 400, fontSize: 32, letterSpacing: "-0.02em", color: "var(--fg)" }}>
            Sign in to <em className="serif-italic" style={{ color: "var(--accent)" }}>practice</em>.
          </h2>
          <p className="text-[14px] mt-3 mb-6" style={{ color: "var(--fg-2)" }}>
            Бүртгэл үүсгээд ЭЕШ математикийн бодлогуудыг бодож, ахицаа хянаарай.
          </p>
          <div className="flex flex-col gap-2">
            <Link href="/sign-up" className="btn btn-primary w-full">
              Бүртгүүлэх
            </Link>
            <Link href="/sign-in" className="btn btn-line w-full">
              Нэвтрэх
            </Link>
          </div>
        </div>
      </div>
    );
  }

  const firstName = user.displayName?.split(" ")[0] ?? "";
  const overall = perf.getOverallStats();

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        {/* Header */}
        <div className="eyebrow mb-3">Practice · Home</div>
        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(40px, 6vw, 64px)", letterSpacing: "-0.04em", lineHeight: 0.98, color: "var(--fg)" }}>
          Сайн уу,{" "}
          <em className="serif-italic" style={{ color: "var(--accent)" }}>
            {firstName || "найз"}
          </em>
          .
        </h1>
        <p className="serif mt-4 max-w-2xl" style={{ fontSize: 17, lineHeight: 1.55, color: "var(--fg-1)" }}>
          Өнөөдөр юунаас эхлэх вэ?
        </p>

        {/* ЭЕШ banner */}
        <Link
          href="/practice/esh"
          className="block mt-8 card-edit p-6 group"
          style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
        >
          <div className="flex items-center justify-between gap-4">
            <div className="flex items-center gap-4">
              <div
                className="w-12 h-12 rounded-md flex items-center justify-center flex-shrink-0"
                style={{ background: "var(--bg-1)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}
              >
                <Calculator className="h-5 w-5" />
              </div>
              <div>
                <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>Featured · ЭЕШ</div>
                <h2 className="serif" style={{ fontWeight: 400, fontSize: 24, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                  ЭЕШ Математик
                </h2>
                <p className="mono text-[11px] mt-1" style={{ color: "var(--fg-2)", letterSpacing: "0.04em" }}>
                  216 БОДЛОГО · 6 ТЕСТ · СЭДВЭЭР АНГИЛСАН
                </p>
              </div>
            </div>
            <ArrowRight className="h-5 w-5 flex-shrink-0" style={{ color: "var(--fg-3)" }} />
          </div>
        </Link>

        {/* Learning resources */}
        <div className="mt-10">
          <div className="eyebrow mb-3">Learning resources</div>
          <h2 className="serif mb-5" style={{ fontWeight: 400, fontSize: 28, letterSpacing: "-0.02em", color: "var(--fg)" }}>
            Хичээл <em className="serif-italic" style={{ color: "var(--accent)" }}>үзэх</em>.
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <Link
              href="/practice/esh/learn"
              className="card-edit p-5 flex items-start gap-3 group"
            >
              <div
                className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0"
                style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
              >
                <BookOpen className="h-4 w-4" />
              </div>
              <div className="min-w-0">
                <p className="serif" style={{ fontWeight: 400, fontSize: 16, color: "var(--fg)" }}>Сэдвээр суралцах</p>
                <p className="text-[12px] mt-0.5" style={{ color: "var(--fg-3)" }}>Томьёо, зөвлөгөө, видео</p>
              </div>
            </Link>

            <Link
              href="/practice/esh/previous-years"
              className="card-edit p-5 flex items-start gap-3 group"
            >
              <div
                className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0"
                style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
              >
                <Flame className="h-4 w-4" />
              </div>
              <div className="min-w-0">
                <p className="serif" style={{ fontWeight: 400, fontSize: 16, color: "var(--fg)" }}>Өмнөх жилийн шалгалт</p>
                <p className="text-[12px] mt-0.5" style={{ color: "var(--fg-3)" }}>2024–2025 ЭЕШ</p>
              </div>
            </Link>

            <div
              className="card-edit p-5 flex items-start gap-3 opacity-80"
              style={{ cursor: "default" }}
            >
              <div
                className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0"
                style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}
              >
                <Sparkles className="h-4 w-4" />
              </div>
              <div className="min-w-0">
                <div className="flex items-center gap-2">
                  <p className="serif" style={{ fontWeight: 400, fontSize: 16, color: "var(--fg)" }}>AI багш</p>
                  <span className="badge-edit" style={{ background: "var(--bg-2)" }}>Coming soon</span>
                </div>
                <p className="text-[12px] mt-0.5" style={{ color: "var(--fg-3)" }}>Алдсан бодлогоо тайлбартай дахин бодно</p>
              </div>
            </div>
          </div>
        </div>

        {/* Analytics quick link */}
        {overall.total > 0 && (
          <Link
            href="/analytics"
            className="block mt-6 card-edit p-5 group"
          >
            <div className="flex items-center justify-between gap-4">
              <div className="flex items-center gap-3">
                <div
                  className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0"
                  style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
                >
                  <BarChart3 className="h-4 w-4" />
                </div>
                <div>
                  <p className="serif" style={{ fontWeight: 400, fontSize: 16, color: "var(--fg)" }}>
                    Таны үзүүлэлт
                  </p>
                  <p className="text-[12px] mt-0.5" style={{ color: "var(--fg-3)" }}>
                    {overall.total} бодлого · {overall.accuracy}% зөв
                  </p>
                </div>
              </div>
              <ArrowRight className="h-4 w-4 flex-shrink-0" style={{ color: "var(--fg-3)" }} />
            </div>
          </Link>
        )}

        {/* Topics */}
        <div className="mt-10">
          <div className="eyebrow mb-3">Topics · Choose</div>
          <h2 className="serif mb-5" style={{ fontWeight: 400, fontSize: 32, letterSpacing: "-0.02em", color: "var(--fg)" }}>
            Сэдвээ <em className="serif-italic" style={{ color: "var(--accent)" }}>сонго</em>.
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
            {TOPICS.map((topic, i) => {
              const data = (topicsData as Record<string, { title: string; overview: string }>)[topic.value];
              return (
                <Link
                  key={topic.value}
                  href={`/practice/esh/learn/${topic.value}`}
                  className="card-edit p-5 group"
                >
                  <div className="flex items-start justify-between gap-3">
                    <div className="min-w-0">
                      <div className="mono text-[10px] mb-1.5" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                        {String(i + 1).padStart(2, "0")}
                      </div>
                      <h3 className="serif" style={{ fontWeight: 400, fontSize: 18, letterSpacing: "-0.01em", color: "var(--fg)" }}>
                        {data?.title ?? topic.label}
                      </h3>
                      {data?.overview && (
                        <p className="text-[12px] mt-1.5 line-clamp-2" style={{ color: "var(--fg-3)" }}>
                          {data.overview}
                        </p>
                      )}
                    </div>
                    <ArrowRight className="h-4 w-4 flex-shrink-0 mt-1" style={{ color: "var(--fg-3)" }} />
                  </div>
                </Link>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}
