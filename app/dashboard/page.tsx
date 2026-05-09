"use client";

import Link from "next/link";
import { ArrowRight, BarChart3, Calculator, Sparkles, Target } from "lucide-react";
import usePerformance from "@/lib/use-performance";
import useTestSession from "@/lib/use-test-session";
import { useAuth } from "@/lib/auth-context";
import { useLang } from "@/lib/lang-context";

const i18n = {
  eyebrow_dashboard: { en: "Dashboard", mn: "Хяналтын самбар" },
  greeting_friend: { en: "friend", mn: "найз" },
  subtitle_with_data: {
    en: "Track your progress below.",
    mn: "Ахиц амжилтаа доор харна уу.",
  },
  subtitle_no_data: {
    en: "Your stats will appear here once you start practicing.",
    mn: "Дадлага эхлэхэд таны үзүүлэлт энд гарна.",
  },
  empty_p: {
    en: "Topic-by-topic progress, weak spots, and recommendations show up here once you take a test.",
    mn: "Шалгалт өгсний дараа сэдэв тус бүрийн ахиц, сул талууд, зөвлөмж энд гарч ирнэ.",
  },
  empty_btn_primary: {
    en: "Start ЭЕШ practice",
    mn: "ЭЕШ дадлага эхлэх",
  },
  empty_btn_secondary: {
    en: "Past-year tests",
    mn: "Өмнөх жилийн шалгалт",
  },

  stat_total: { en: "Total problems", mn: "Нийт бодсон бодлого" },
  stat_accuracy: { en: "Accuracy", mn: "Зөв хариулсан хувь" },
  stat_tests: { en: "Tests completed", mn: "Дуусгасан тест" },
  stat_latest: { en: "Latest test", mn: "Сүүлийн тестийн дүн" },

  focus_eyebrow: {
    en: "Focus · weakest topic",
    mn: "Анхаарах сул сэдэв",
  },
  focus_btn_learn: { en: "Learn", mn: "Суралцах" },
  focus_btn_practice: { en: "Take a test", mn: "Шалгалт өгөх" },

  practice_eyebrow: { en: "Practice", mn: "Дадлага" },
  doing_well_p: {
    en: "No clear weak topic right now. Keep taking tests to confirm.",
    mn: "Одоогоор ямар нэг сэдэв тодорхой сул гэж гарсангүй. Илүү шалгалт өгч баталгаажуулцгаая.",
  },

  analytics_eyebrow: {
    en: "Detailed analytics",
    mn: "Дэлгэрэнгүй мэдээлэл",
  },
  analytics_h: { en: "Full report →", mn: "Бүрэн тайлан →" },
  analytics_p: {
    en: "Topic breakdown, test history, missed problems.",
    mn: "Сэдвийн задаргаа, шалгалтын түүх, алдсан бодлогууд.",
  },

  topics_eyebrow: { en: "Top topics", mn: "Гол сэдвүүд" },

  qa_practice_t: { en: "ЭЕШ practice", mn: "ЭЕШ дадлага" },
  qa_practice_s: { en: "Take a test", mn: "Шалгалт өгөх" },
  qa_learn_t: { en: "Study by topic", mn: "Сэдвээр суралцах" },
  qa_learn_s: { en: "Formulas, tips", mn: "Томьёо, зөвлөгөө" },
  qa_analytics_t: { en: "Full report", mn: "Бүрэн тайлан" },
  qa_analytics_s: { en: "Detailed analytics", mn: "Дэлгэрэнгүй харах" },
};

export default function DashboardPage() {
  const perf = usePerformance();
  const ts = useTestSession();
  const { user } = useAuth();
  const { lang } = useLang();
  const t = (key: keyof typeof i18n) => i18n[key][lang === "mn" ? "mn" : "en"];

  const overall = perf.getOverallStats();
  const topicStats = perf.getTopicStats();
  const completed = ts.getCompletedSessions();

  const hasData = overall.total > 0 || completed.length > 0;
  const userName = user?.displayName ?? "";

  const latestSession = completed[0];
  const latestPct = latestSession?.score?.accuracy ?? null;
  const weakTopics = topicStats.filter((t) => t.accuracy < 70 && t.total >= 3);
  const weakest = weakTopics.sort((a, b) => a.accuracy - b.accuracy)[0];

  const greeting =
    lang === "mn" ? (
      <>
        Сайн уу,{" "}
        <em className="serif-italic" style={{ color: "var(--accent)" }}>
          {userName || t("greeting_friend")}
        </em>
        .
      </>
    ) : (
      <>
        Hello,{" "}
        <em className="serif-italic" style={{ color: "var(--accent)" }}>
          {userName || t("greeting_friend")}
        </em>
        .
      </>
    );

  const emptyHeading =
    lang === "mn" ? (
      <>
        Эхний шалгалтаа{" "}
        <em className="serif-italic" style={{ color: "var(--accent)" }}>
          өгье
        </em>
        .
      </>
    ) : (
      <>
        Take your first{" "}
        <em className="serif-italic" style={{ color: "var(--accent)" }}>
          test
        </em>
        .
      </>
    );

  const doingWellHeading =
    lang === "mn" ? "Сайн явж байна." : "Doing well.";

  // Focus banner sentence — interpolates accuracy + (correct/total).
  const focusBanner = weakest && (
    <>
      {lang === "mn" ? "Одоогийн үнэлгээ " : "Current accuracy: "}
      <strong style={{ color: "var(--warn)" }}>{weakest.accuracy}%</strong>{" "}
      ({weakest.correct}/{weakest.total}){lang === "mn" ? " " : ". "}
      {lang === "mn"
        ? "Энэ сэдвээр илүү их дадлага хийх хэрэгтэй байна."
        : "More practice on this topic will move your score the most."}
    </>
  );

  return (
    <div className="min-h-screen pt-16" style={{ background: "var(--bg)" }}>
      <div className="max-w-5xl mx-auto px-6 md:px-10 py-10 md:py-12">
        {/* Welcome */}
        <section className="pb-7" style={{ borderBottom: "1px solid var(--line)" }}>
          <div className="eyebrow">
            {t("eyebrow_dashboard")}
            {userName && ` · ${userName}`}
          </div>
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
            {greeting}
          </h1>
          <p className="mt-3 text-[15px]" style={{ color: "var(--fg-2)" }}>
            {hasData ? t("subtitle_with_data") : t("subtitle_no_data")}
          </p>
        </section>

        {!hasData ? (
          // Empty state
          <section className="mt-10 card-edit p-10 text-center">
            <div
              className="w-14 h-14 rounded-md flex items-center justify-center mx-auto mb-5"
              style={{
                background: "var(--accent-wash)",
                border: "1px solid var(--accent-line)",
                color: "var(--accent)",
              }}
            >
              <Calculator className="h-6 w-6" />
            </div>
            <h2
              className="serif"
              style={{
                fontWeight: 400,
                fontSize: 28,
                letterSpacing: "-0.02em",
                color: "var(--fg)",
              }}
            >
              {emptyHeading}
            </h2>
            <p className="text-[14px] mt-3 max-w-md mx-auto" style={{ color: "var(--fg-2)" }}>
              {t("empty_p")}
            </p>
            <div className="flex flex-wrap justify-center gap-2 mt-6">
              <Link href="/practice/esh" className="btn btn-primary">
                {t("empty_btn_primary")}
                <ArrowRight className="ml-1 h-3.5 w-3.5" />
              </Link>
              <Link href="/practice/esh/test?type=previous" className="btn btn-line">
                {t("empty_btn_secondary")}
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
                <div className="eyebrow">{t("stat_total")}</div>
                <div
                  className="serif tabular mt-2"
                  style={{
                    fontSize: 40,
                    letterSpacing: "-0.03em",
                    lineHeight: 1,
                    color: "var(--fg)",
                  }}
                >
                  {overall.total}
                </div>
              </div>
              <div className="card-edit p-5">
                <div className="eyebrow">{t("stat_accuracy")}</div>
                <div
                  className="serif tabular mt-2"
                  style={{
                    fontSize: 40,
                    letterSpacing: "-0.03em",
                    lineHeight: 1,
                    color: "var(--accent)",
                  }}
                >
                  {overall.accuracy}
                  <span className="mono ml-1" style={{ fontSize: 14, color: "var(--fg-3)" }}>
                    %
                  </span>
                </div>
              </div>
              <div className="card-edit p-5">
                <div className="eyebrow">{t("stat_tests")}</div>
                <div
                  className="serif tabular mt-2"
                  style={{
                    fontSize: 40,
                    letterSpacing: "-0.03em",
                    lineHeight: 1,
                    color: "var(--fg)",
                  }}
                >
                  {completed.length}
                </div>
              </div>
              {latestPct !== null && (
                <div className="card-edit p-5">
                  <div className="eyebrow">{t("stat_latest")}</div>
                  <div
                    className="serif tabular mt-2"
                    style={{
                      fontSize: 40,
                      letterSpacing: "-0.03em",
                      lineHeight: 1,
                      color: "var(--fg)",
                    }}
                  >
                    {latestPct}
                    <span className="mono ml-1" style={{ fontSize: 14, color: "var(--fg-3)" }}>
                      %
                    </span>
                  </div>
                </div>
              )}
            </section>

            {/* Focus row */}
            <section
              className="grid gap-4 mt-5"
              style={{ gridTemplateColumns: "minmax(0, 1.4fr) minmax(0, 1fr)" }}
            >
              {/* Weakest topic */}
              {weakest ? (
                <div
                  className="card-edit p-6"
                  style={{
                    background: "var(--accent-wash)",
                    borderColor: "var(--accent-line)",
                  }}
                >
                  <div className="eyebrow" style={{ color: "var(--accent)" }}>
                    {t("focus_eyebrow")}
                  </div>
                  <h3
                    className="serif mt-2"
                    style={{
                      fontWeight: 400,
                      fontSize: 26,
                      letterSpacing: "-0.02em",
                      color: "var(--fg)",
                    }}
                  >
                    {weakest.label}
                  </h3>
                  <p className="text-[14px] mt-2" style={{ color: "var(--fg-1)" }}>
                    {focusBanner}
                  </p>
                  <div className="flex flex-wrap gap-2 mt-5">
                    <Link
                      href={`/practice/esh/learn/${weakest.topic}`}
                      className="btn btn-primary"
                    >
                      {t("focus_btn_learn")}
                      <ArrowRight className="ml-1 h-3.5 w-3.5" />
                    </Link>
                    <Link href="/practice/esh" className="btn btn-line">
                      {t("focus_btn_practice")}
                    </Link>
                  </div>
                </div>
              ) : (
                <div className="card-edit p-6">
                  <div className="eyebrow">{t("practice_eyebrow")}</div>
                  <h3
                    className="serif mt-2"
                    style={{
                      fontWeight: 400,
                      fontSize: 26,
                      letterSpacing: "-0.02em",
                      color: "var(--fg)",
                    }}
                  >
                    {doingWellHeading}
                  </h3>
                  <p className="text-[14px] mt-2" style={{ color: "var(--fg-1)" }}>
                    {t("doing_well_p")}
                  </p>
                  <Link href="/practice/esh" className="btn btn-primary mt-5 self-start">
                    {t("focus_btn_practice")}
                    <ArrowRight className="ml-1 h-3.5 w-3.5" />
                  </Link>
                </div>
              )}

              {/* Analytics link */}
              <Link
                href="/analytics"
                className="card-edit p-6 group"
                style={{ textDecoration: "none" }}
              >
                <div className="flex items-center gap-2 mb-2">
                  <BarChart3 className="h-4 w-4" style={{ color: "var(--fg-2)" }} />
                  <div className="eyebrow">{t("analytics_eyebrow")}</div>
                </div>
                <h3
                  className="serif mt-2"
                  style={{
                    fontWeight: 400,
                    fontSize: 22,
                    letterSpacing: "-0.02em",
                    color: "var(--fg)",
                  }}
                >
                  {t("analytics_h")}
                </h3>
                <p className="text-[13px] mt-2" style={{ color: "var(--fg-2)" }}>
                  {t("analytics_p")}
                </p>
              </Link>
            </section>

            {/* Topic strip */}
            {topicStats.length > 0 && (
              <section className="card-edit p-6 mt-5">
                <div className="flex items-center gap-2 mb-4">
                  <Target className="h-4 w-4" style={{ color: "var(--fg-2)" }} />
                  <div className="eyebrow">{t("topics_eyebrow")}</div>
                </div>
                <div className="space-y-3">
                  {topicStats.slice(0, 5).map((tt) => (
                    <div key={tt.topic}>
                      <div className="flex items-baseline justify-between mb-1.5 text-sm">
                        <span style={{ color: "var(--fg-1)" }}>{tt.label}</span>
                        <span
                          className="mono tabular"
                          style={{ color: "var(--fg-3)", fontSize: 12 }}
                        >
                          {tt.correct}/{tt.total} · {tt.accuracy}%
                        </span>
                      </div>
                      <div
                        className="h-[3px] rounded-full overflow-hidden"
                        style={{ background: "var(--bg-2)" }}
                      >
                        <div
                          className="h-full rounded-full"
                          style={{
                            width: `${tt.accuracy}%`,
                            background:
                              tt.accuracy >= 80
                                ? "var(--accent)"
                                : tt.accuracy >= 50
                                  ? "var(--warn)"
                                  : "var(--danger)",
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
                  style={{
                    background: "var(--bg-2)",
                    border: "1px solid var(--line)",
                    color: "var(--fg-2)",
                  }}
                >
                  <Calculator className="h-4 w-4" />
                </div>
                <div>
                  <p className="serif" style={{ fontWeight: 400, fontSize: 15, color: "var(--fg)" }}>
                    {t("qa_practice_t")}
                  </p>
                  <p className="text-[12px]" style={{ color: "var(--fg-3)" }}>
                    {t("qa_practice_s")}
                  </p>
                </div>
              </Link>
              <Link
                href="/practice/esh/learn"
                className="card-edit p-5 flex items-center gap-3 group"
              >
                <div
                  className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0"
                  style={{
                    background: "var(--bg-2)",
                    border: "1px solid var(--line)",
                    color: "var(--fg-2)",
                  }}
                >
                  <Sparkles className="h-4 w-4" />
                </div>
                <div>
                  <p className="serif" style={{ fontWeight: 400, fontSize: 15, color: "var(--fg)" }}>
                    {t("qa_learn_t")}
                  </p>
                  <p className="text-[12px]" style={{ color: "var(--fg-3)" }}>
                    {t("qa_learn_s")}
                  </p>
                </div>
              </Link>
              <Link href="/analytics" className="card-edit p-5 flex items-center gap-3 group">
                <div
                  className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0"
                  style={{
                    background: "var(--bg-2)",
                    border: "1px solid var(--line)",
                    color: "var(--fg-2)",
                  }}
                >
                  <BarChart3 className="h-4 w-4" />
                </div>
                <div>
                  <p className="serif" style={{ fontWeight: 400, fontSize: 15, color: "var(--fg)" }}>
                    {t("qa_analytics_t")}
                  </p>
                  <p className="text-[12px]" style={{ color: "var(--fg-3)" }}>
                    {t("qa_analytics_s")}
                  </p>
                </div>
              </Link>
            </section>
          </>
        )}
      </div>
    </div>
  );
}
