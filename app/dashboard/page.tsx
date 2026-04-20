"use client";

import Link from "next/link";
import { ArrowRight, BarChart3, Calculator, Sparkles, Target } from "lucide-react";
import usePerformance from "@/lib/use-performance";
import useTestSession from "@/lib/use-test-session";
import { useAuth } from "@/lib/auth-context";

export default function DashboardPage() {
  const perf = usePerformance();
  const ts = useTestSession();
  const { user } = useAuth();

  const overall = perf.getOverallStats();
  const topicStats = perf.getTopicStats();
  const completed = ts.getCompletedSessions();

  const hasData = overall.total > 0 || completed.length > 0;
  const firstName = user?.displayName?.split(" ")[0] ?? "";

  const latestSession = completed[0];
  const latestPct = latestSession?.score?.accuracy ?? null;
  const weakTopics = topicStats.filter((t) => t.accuracy < 70 && t.total >= 3);
  const weakest = weakTopics.sort((a, b) => a.accuracy - b.accuracy)[0];

  return (
    <div className="min-h-screen pt-16" style={{ background: "var(--bg)" }}>
      <div className="max-w-5xl mx-auto px-6 md:px-10 py-10 md:py-12">
        {/* Welcome */}
        <section className="pb-7" style={{ borderBottom: "1px solid var(--line)" }}>
          <div className="eyebrow">Dashboard{firstName && ` · ${firstName}`}</div>
          <h1
            className="serif"
            style={{
              fontWeight: 400,
              fontSize: "clamp(40px, 5.5vw, 64px)",
              letterSpacing: "-0.04em",
              lineHeight: 0.98,
              margin: "8px 0 0",
              color: "var(--fg)",
            }}
          >
            Сайн уу, <em className="serif-italic" style={{ color: "var(--accent)" }}>{firstName || "найз"}</em>.
          </h1>
          <p className="mt-3 text-[15px]" style={{ color: "var(--fg-2)" }}>
            {hasData
              ? "Ахиц амжилтаа доор харна уу."
              : "Дадлага эхлэхэд таны үзүүлэлт энд гарна."}
          </p>
          <p className="mono mt-2" style={{ fontSize: 11, color: "var(--fg-3)", letterSpacing: "0.08em" }}>
            ON THIS DEVICE · ACCOUNT SYNC COMING SOON
          </p>
        </section>

        {!hasData ? (
          // Empty state
          <section className="mt-10 card-edit p-10 text-center">
            <div
              className="w-14 h-14 rounded-md flex items-center justify-center mx-auto mb-5"
              style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}
            >
              <Calculator className="h-6 w-6" />
            </div>
            <h2 className="serif" style={{ fontWeight: 400, fontSize: 28, letterSpacing: "-0.02em", color: "var(--fg)" }}>
              Эхний шалгалтаа <em className="serif-italic" style={{ color: "var(--accent)" }}>өгье</em>.
            </h2>
            <p className="text-[14px] mt-3 max-w-md mx-auto" style={{ color: "var(--fg-2)" }}>
              Шалгалт өгсний дараа сэдэв тус бүрийн ахиц, сул талууд, зөвлөмж энд гарч ирнэ.
            </p>
            <div className="flex flex-wrap justify-center gap-2 mt-6">
              <Link href="/practice/esh" className="btn btn-primary">
                ЭЕШ дадлага эхлэх
                <ArrowRight className="ml-1 h-3.5 w-3.5" />
              </Link>
              <Link href="/practice/esh/previous-years" className="btn btn-line">
                Өмнөх жилийн шалгалт
              </Link>
            </div>
          </section>
        ) : (
          <>
            {/* Stats grid */}
            <section
              className="grid gap-4 mt-8"
              style={{ gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))" }}
            >
              <div className="card-edit p-5">
                <div className="eyebrow">Total problems</div>
                <div className="serif tabular mt-2" style={{ fontSize: 40, letterSpacing: "-0.03em", lineHeight: 1, color: "var(--fg)" }}>
                  {overall.total}
                </div>
              </div>
              <div className="card-edit p-5">
                <div className="eyebrow">Accuracy</div>
                <div className="serif tabular mt-2" style={{ fontSize: 40, letterSpacing: "-0.03em", lineHeight: 1, color: "var(--accent)" }}>
                  {overall.accuracy}
                  <span className="mono ml-1" style={{ fontSize: 14, color: "var(--fg-3)" }}>%</span>
                </div>
              </div>
              <div className="card-edit p-5">
                <div className="eyebrow">Tests completed</div>
                <div className="serif tabular mt-2" style={{ fontSize: 40, letterSpacing: "-0.03em", lineHeight: 1, color: "var(--fg)" }}>
                  {completed.length}
                </div>
              </div>
              {latestPct !== null && (
                <div className="card-edit p-5">
                  <div className="eyebrow">Latest test</div>
                  <div className="serif tabular mt-2" style={{ fontSize: 40, letterSpacing: "-0.03em", lineHeight: 1, color: "var(--fg)" }}>
                    {latestPct}
                    <span className="mono ml-1" style={{ fontSize: 14, color: "var(--fg-3)" }}>%</span>
                  </div>
                </div>
              )}
            </section>

            {/* Focus row */}
            <section className="grid gap-4 mt-5" style={{ gridTemplateColumns: "minmax(0, 1.4fr) minmax(0, 1fr)" }}>
              {/* Weakest topic */}
              {weakest ? (
                <div
                  className="card-edit p-6"
                  style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
                >
                  <div className="eyebrow" style={{ color: "var(--accent)" }}>Focus · weakest topic</div>
                  <h3
                    className="serif mt-2"
                    style={{ fontWeight: 400, fontSize: 26, letterSpacing: "-0.02em", color: "var(--fg)" }}
                  >
                    {weakest.label}
                  </h3>
                  <p className="text-[14px] mt-2" style={{ color: "var(--fg-1)" }}>
                    Одоогийн үнэн зөв: <strong style={{ color: "var(--warn)" }}>{weakest.accuracy}%</strong>{" "}
                    ({weakest.correct}/{weakest.total}). Энэ сэдэв дээр илүү дасгал хийвэл оноо огцом нэмэгдэнэ.
                  </p>
                  <div className="flex flex-wrap gap-2 mt-5">
                    <Link href={`/practice/esh/learn/${weakest.topic}`} className="btn btn-primary">
                      Суралцах
                      <ArrowRight className="ml-1 h-3.5 w-3.5" />
                    </Link>
                    <Link href="/practice/esh" className="btn btn-line">
                      Шалгалт өгөх
                    </Link>
                  </div>
                </div>
              ) : (
                <div className="card-edit p-6">
                  <div className="eyebrow">Practice</div>
                  <h3
                    className="serif mt-2"
                    style={{ fontWeight: 400, fontSize: 26, letterSpacing: "-0.02em", color: "var(--fg)" }}
                  >
                    Сайн явж байна.
                  </h3>
                  <p className="text-[14px] mt-2" style={{ color: "var(--fg-1)" }}>
                    Одоогоор ямар нэг сэдэв тодорхой сул гэж гарсангүй. Илүү шалгалт өгч баталгаажуулцгаая.
                  </p>
                  <Link href="/practice/esh" className="btn btn-primary mt-5 self-start">
                    Шалгалт өгөх
                    <ArrowRight className="ml-1 h-3.5 w-3.5" />
                  </Link>
                </div>
              )}

              {/* Analytics link */}
              <Link href="/analytics" className="card-edit p-6 group" style={{ textDecoration: "none" }}>
                <div className="flex items-center gap-2 mb-2">
                  <BarChart3 className="h-4 w-4" style={{ color: "var(--fg-2)" }} />
                  <div className="eyebrow">Detailed analytics</div>
                </div>
                <h3
                  className="serif mt-2"
                  style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}
                >
                  Бүрэн тайлан →
                </h3>
                <p className="text-[13px] mt-2" style={{ color: "var(--fg-2)" }}>
                  Сэдвийн задаргаа, шалгалтын түүх, алдсан бодлогууд.
                </p>
              </Link>
            </section>

            {/* Topic strip */}
            {topicStats.length > 0 && (
              <section className="card-edit p-6 mt-5">
                <div className="flex items-center gap-2 mb-4">
                  <Target className="h-4 w-4" style={{ color: "var(--fg-2)" }} />
                  <div className="eyebrow">Top topics</div>
                </div>
                <div className="space-y-3">
                  {topicStats.slice(0, 5).map((t) => (
                    <div key={t.topic}>
                      <div className="flex items-baseline justify-between mb-1.5 text-sm">
                        <span style={{ color: "var(--fg-1)" }}>{t.label}</span>
                        <span className="mono tabular" style={{ color: "var(--fg-3)", fontSize: 12 }}>
                          {t.correct}/{t.total} · {t.accuracy}%
                        </span>
                      </div>
                      <div className="h-[3px] rounded-full overflow-hidden" style={{ background: "var(--bg-2)" }}>
                        <div
                          className="h-full rounded-full"
                          style={{
                            width: `${t.accuracy}%`,
                            background: t.accuracy >= 80 ? "var(--accent)" : t.accuracy >= 50 ? "var(--warn)" : "var(--danger)",
                          }}
                        />
                      </div>
                    </div>
                  ))}
                </div>
              </section>
            )}

            {/* Quick actions */}
            <section className="grid grid-cols-1 sm:grid-cols-3 gap-3 mt-5">
              <Link href="/practice/esh" className="card-edit p-5 flex items-center gap-3 group">
                <div
                  className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0"
                  style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
                >
                  <Calculator className="h-4 w-4" />
                </div>
                <div>
                  <p className="serif" style={{ fontWeight: 400, fontSize: 15, color: "var(--fg)" }}>ЭЕШ дадлага</p>
                  <p className="text-[12px]" style={{ color: "var(--fg-3)" }}>Шалгалт өгөх</p>
                </div>
              </Link>
              <Link href="/practice/esh/learn" className="card-edit p-5 flex items-center gap-3 group">
                <div
                  className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0"
                  style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
                >
                  <Sparkles className="h-4 w-4" />
                </div>
                <div>
                  <p className="serif" style={{ fontWeight: 400, fontSize: 15, color: "var(--fg)" }}>Сэдвээр суралцах</p>
                  <p className="text-[12px]" style={{ color: "var(--fg-3)" }}>Томьёо, зөвлөгөө</p>
                </div>
              </Link>
              <Link href="/analytics" className="card-edit p-5 flex items-center gap-3 group">
                <div
                  className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0"
                  style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
                >
                  <BarChart3 className="h-4 w-4" />
                </div>
                <div>
                  <p className="serif" style={{ fontWeight: 400, fontSize: 15, color: "var(--fg)" }}>Бүрэн тайлан</p>
                  <p className="text-[12px]" style={{ color: "var(--fg-3)" }}>Дэлгэрэнгүй анализ</p>
                </div>
              </Link>
            </section>
          </>
        )}
      </div>
    </div>
  );
}
