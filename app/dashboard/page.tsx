"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { ArrowRight, BarChart3, Calculator, Sparkles, Target } from "lucide-react";
import usePerformance from "@/lib/use-performance";
import { useAuth } from "@/lib/auth-context";
import { useLang } from "@/lib/lang-context";
import useRefinementLoop from "@/lib/use-refinement-loop";
import { getAllQuestions } from "@/lib/esh-questions";

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
  focus_btn_master: { en: "Master this topic", mn: "Бүрэн эзэмших" },

  practice_eyebrow: { en: "Practice", mn: "Дадлага" },
  doing_well_p: {
    en: "No clear weak topic right now. Keep taking tests to confirm.",
    mn: "Одоогоор ямар нэг сэдэв тодорхой сул гэж гарсангүй. Илүү шалгалт өгч баталгаажуулцгаая.",
  },
  no_tests_eyebrow: { en: "Get started", mn: "Эхлэх" },
  no_tests_h: {
    en: "Take a practice test and check back.",
    mn: "Шалгалт өгөөд эргэж очоорой.",
  },
  no_tests_p: {
    en: "The recommendation surfaces based on test results.",
    mn: "Шалгалтын үр дүн дээр үндэслэсэн зөвлөмж эндээс гарах болно.",
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
  const { user } = useAuth();
  const { lang } = useLang();
  const t = (key: keyof typeof i18n) => i18n[key][lang === "mn" ? "mn" : "en"];

  const router = useRouter();
  const loop = useRefinementLoop();
  // §3c: start a refinement loop on the easiest still-unsolved question in a topic.
  const startTopicLoop = (topic: string) => {
    const solved = new Set(perf.attempts.filter((a) => a.isCorrect).map((a) => a.questionSource));
    const inTopic = getAllQuestions().filter((q) => q.topic === topic);
    const unsolved = inTopic.filter((q) => !solved.has(q.source));
    const pickFrom = unsolved.length > 0 ? unsolved : inTopic;
    const entry = pickFrom
      .slice()
      .sort((a, b) => a.difficulty - b.difficulty || a.source.localeCompare(b.source))[0];
    if (!entry) return;
    loop.start({
      triggeredSource: "dashboard_weak_topic",
      triggeredQuestion: entry.source,
      skillTag: entry.skill_tag ?? null,
      topic,
    });
    router.push("/practice/esh/loop");
  };

  const overall = perf.getOverallStats();
  const topicStats = perf.getTopicStats();
  // Server-derived test sessions (cross-device-safe). Replaces the previous
  // local-only ts.getCompletedSessions() for stats display so a fresh-device
  // login still shows the correct "Tests completed" count and latest test.
  const testSessions = perf.getTestOnlySessions();

  const hasData = overall.total > 0 || testSessions.length > 0;
  const userName = user?.displayName ?? "";

  const latestSession = testSessions[0];
  const latestPct = latestSession?.accuracy ?? null;
  // Weak-topic recommendation reads from TEST-mode server attempts only —
  // drill rows excluded so the focus card doesn't recommend the topic the
  // student happens to drill instead of the one they struggle with on tests.
  const testTopicStats = perf.getTestOnlyTopicStats();
  const hasQualifyingTests = perf.hasTestOnlyData();
  const weakTopics = testTopicStats.filter((t) => t.accuracy < 70);
  const weakest = weakTopics[0]; // already sorted asc by accuracy

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
                  {testSessions.length}
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

            {/* Focus row — single column on mobile/tablet so the weak-topic
                 card (or empty-state copy) gets full width and Mongolian
                 phrases don't wrap word-per-line. */}
            <section className="grid gap-4 mt-5 grid-cols-1 md:grid-cols-[minmax(0,1.4fr)_minmax(0,1fr)]">
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
                    <button
                      type="button"
                      onClick={() => startTopicLoop(weakest.topic)}
                      className="btn btn-primary"
                    >
                      <Target className="mr-1 h-3.5 w-3.5" />
                      {t("focus_btn_master")}
                    </button>
                    <Link
                      href={`/practice/esh/learn/${weakest.topic}`}
                      className="btn btn-line"
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
                  <div className="eyebrow">
                    {hasQualifyingTests ? t("practice_eyebrow") : t("no_tests_eyebrow")}
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
                    {hasQualifyingTests ? doingWellHeading : t("no_tests_h")}
                  </h3>
                  <p className="text-[14px] mt-2" style={{ color: "var(--fg-1)" }}>
                    {hasQualifyingTests ? t("doing_well_p") : t("no_tests_p")}
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
