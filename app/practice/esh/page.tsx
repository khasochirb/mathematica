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
import useESHProgress from "@/lib/use-esh-progress";
import {
  getAllTests,
  getAllQuestions,
  getPreviousYearTests,
} from "@/lib/esh-questions";

export default function ESHHubPage() {
  const [mounted, setMounted] = useState(false);
  const progress = useESHProgress();

  useEffect(() => setMounted(true), []);

  const allTests = getAllTests();
  const totalQuestions = getAllQuestions().length;
  const previousYearTests = getPreviousYearTests();

  const sections = [
    {
      href: "/practice/esh/test",
      eyebrow: "01 · ШАЛГАЛТ",
      title: "Дадлага шалгалт",
      desc: "Шалгалтын горимд цагтай бодоорой",
      icon: FileText,
      meta: (
        <>
          <span className="mono tabular">{allTests.length} тест</span>
          {mounted && progress.totalTestsTaken > 0 && (
            <>
              <span style={{ color: "var(--fg-3)" }}>·</span>
              <span className="mono tabular" style={{ color: "var(--accent)" }}>
                {progress.totalTestsTaken} бодсон
              </span>
            </>
          )}
        </>
      ),
    },
    {
      href: "/practice/esh/practice",
      eyebrow: "02 · БОДЛОГО",
      title: "Дадлага бодлого",
      desc: "Сэдвээр дадлага хийж, сул талаа сайжруул",
      icon: Target,
      meta: (
        <>
          <span className="mono tabular">{totalQuestions} бодлого</span>
          {mounted && progress.weakTopics.length > 0 && (
            <>
              <span style={{ color: "var(--fg-3)" }}>·</span>
              <span className="mono tabular" style={{ color: "var(--warn)" }}>
                {progress.weakTopics.length} сул сэдэв
              </span>
            </>
          )}
        </>
      ),
    },
    {
      href: "/practice/esh/learn",
      eyebrow: "03 · СУРАЛЦАХ",
      title: "Суралцах",
      desc: "Сэдвээр унших материал, томьёо, видео хичээл",
      icon: BookOpen,
      meta: <span className="mono tabular">10 сэдэв</span>,
    },
    {
      href: "/practice/esh/progress",
      eyebrow: "04 · ПРОГРЕСС",
      title: "Прогресс",
      desc: "Оноогоо хяна, ахицаа хар",
      icon: BarChart3,
      meta:
        mounted && progress.totalTestsTaken > 0 ? (
          <span className="mono tabular">{progress.averageAccuracy}% дундаж</span>
        ) : (
          <span style={{ color: "var(--fg-3)" }}>Мэдээлэл байхгүй</span>
        ),
    },
    {
      href: "/practice/esh/previous-years",
      eyebrow: "05 · ӨМНӨХ ЖИЛҮҮД",
      title: "Өмнөх жилийн шалгалтууд",
      desc: "2024, 2025 оны бодит ЭЕШ — нэвтэрсэн хэрэглэгчдэд үнэгүй",
      icon: Archive,
      meta: (
        <>
          <span className="mono tabular">{previousYearTests.length} тест</span>
          <span style={{ color: "var(--fg-3)" }}>·</span>
          <span className="mono tabular" style={{ color: "var(--accent)" }}>
            Үнэгүй
          </span>
        </>
      ),
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

        {/* Section cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {sections.map((s) => {
            const Icon = s.icon;
            return (
              <Link key={s.href} href={s.href} className="card-edit p-6 group block">
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
                <div className="eyebrow mb-2">{s.eyebrow}</div>
                <h2
                  className="serif mb-1.5"
                  style={{
                    fontWeight: 400,
                    fontSize: 24,
                    letterSpacing: "-0.02em",
                    color: "var(--fg)",
                  }}
                >
                  {s.title}
                </h2>
                <p className="text-[13px] mb-4" style={{ color: "var(--fg-2)" }}>
                  {s.desc}
                </p>
                <div
                  className="flex items-center gap-2 text-[12px] pt-3"
                  style={{ borderTop: "1px solid var(--line)", color: "var(--fg-2)" }}
                >
                  {s.meta}
                </div>
              </Link>
            );
          })}
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
