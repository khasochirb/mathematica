"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { ArrowRight, BarChart3, Calculator, Sparkles, Target } from "lucide-react";
import { useEffect, useState } from "react";
import usePerformance from "@/lib/use-performance";
import { contextHref, contextLabel, contextProgressHref } from "@/lib/perf-context";
import { loadPlacement, type StoredPlacement } from "@/lib/placement-result";
import { useAuth } from "@/lib/auth-context";
import { useLang } from "@/lib/lang-context";
import useRefinementLoop, { useRecentlyMastered } from "@/lib/use-refinement-loop";
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
  personal_grade: { en: "Grade", mn: "Анги" },
  personal_focus: { en: "Focus on", mn: "Анхаарах" },
  personal_open: { en: "Open", mn: "Нээх" },
  empty_p: {
    en: "Progress, weak spots, and recommendations will show up here once you start learning.",
    mn: "Хичээл эхлүүлмэгц таны ахиц, сул талууд, зөвлөмж энд гарч ирнэ.",
  },
  empty_btn_primary: {
    en: "Explore courses",
    mn: "Хичээлүүдийг үзэх",
  },
  empty_btn_secondary: {
    en: "ЭЕШ practice",
    mn: "ЭЕШ дадлага",
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

  esh_section: { en: "ЭЕШ preparation", mn: "ЭЕШ бэлтгэл" },
  hubs_section: { en: "Exam prep", mn: "Шалгалтын бэлтгэл" },
  hubs_questions: { en: "questions", mn: "бодлого" },
  hubs_open: { en: "View progress", mn: "Прогресс харах" },
  courses_section: { en: "Courses", mn: "Хичээлүүд" },
  courses_checks: { en: "lesson checks", mn: "хичээлийн даалгавар" },
  courses_weakest: { en: "Weakest unit", mn: "Хамгийн сул нэгж" },
  courses_open: { en: "Open course", mn: "Курс нээх" },
  placement_section: { en: "Placement tests", mn: "Түвшин тогтоох тестүүд" },
  placement_level: { en: "Level", mn: "Түвшин" },
  placement_open: { en: "View plan", mn: "Төлөвлөгөө харах" },
};

// Placement namespaces the platform currently offers, with their course homes.
const PLACEMENT_NAMESPACES: { namespace: string; href: string; en: string; mn: string }[] = [
  { namespace: "grade6", href: "/math/6", en: "Grade 6", mn: "6-р анги" },
  { namespace: "grade7", href: "/math/7", en: "Grade 7", mn: "7-р анги" },
  { namespace: "grade8", href: "/math/8", en: "Grade 8", mn: "8-р анги" },
  { namespace: "grade9", href: "/math/9", en: "Grade 9", mn: "9-р анги" },
  { namespace: "grade10", href: "/math/10", en: "Grade 10", mn: "10-р анги" },
  { namespace: "grade11", href: "/math/11", en: "Grade 11", mn: "11-р анги" },
  { namespace: "grade12", href: "/math/12", en: "Grade 12", mn: "12-р анги" },
  { namespace: "geometry", href: "/math/geometry", en: "Geometry", mn: "Геометр" },
];

// Unit slugs read as titles: "probability-models" → "Probability models".
function humanizeSlug(slug: string): string {
  const s = slug.replace(/-/g, " ");
  return s.charAt(0).toUpperCase() + s.slice(1);
}

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
  // Per-section summaries: each course the student has touched, with stats
  // computed ONLY from that course's attempts. Accuracy never blends across
  // sections — that's the whole point of the context column.
  const contextSummaries = perf.getContextSummaries();
  const courseSummaries = contextSummaries.filter((s) => s.context.startsWith("course:"));
  // SAT/IB hub cards light up on the first recorded attempt in those
  // contexts — pre-wired now so shipping the first mock test needs no
  // dashboard work. Each card links out; depth lives in the hub.
  const examHubSummaries = contextSummaries.filter((s) => s.context === "sat" || s.context === "ib");
  // Placement results are device-local (localStorage) — load after mount to
  // keep server and client renders identical.
  const [placements, setPlacements] = useState<
    { namespace: string; href: string; en: string; mn: string; data: StoredPlacement }[]
  >([]);
  useEffect(() => {
    setPlacements(
      PLACEMENT_NAMESPACES.flatMap((ns) => {
        const data = loadPlacement(user?.id, ns.namespace);
        return data ? [{ ...ns, data }] : [];
      }),
    );
  }, [user?.id]);
  // Server-derived test sessions (cross-device-safe). Replaces the previous
  // local-only ts.getCompletedSessions() for stats display so a fresh-device
  // login still shows the correct "Tests completed" count and latest test.
  const testSessions = perf.getTestOnlySessions();

  const hasData = overall.total > 0 || testSessions.length > 0 || courseSummaries.length > 0;
  const userName = user?.displayName ?? "";

  const latestSession = testSessions[0];
  const latestPct = latestSession?.accuracy ?? null;
  // Weak-topic recommendation reads from TEST-mode server attempts only —
  // drill rows excluded so the focus card doesn't recommend the topic the
  // student happens to drill instead of the one they struggle with on tests.
  const testTopicStats = perf.getTestOnlyTopicStats();
  const hasQualifyingTests = perf.hasTestOnlyData();
  // §5: a topic mastered in the last 14 days is hidden from the weak-spot card
  // even if its accuracy still lags (stats trail the actual learning).
  const masteredTopics = useRecentlyMastered();
  const weakTopics = testTopicStats.filter((t) => t.accuracy < 70 && !masteredTopics.has(t.topic));
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
        <em className="serif-italic" style={{ color: "var(--accent)" }}>
          Судалж
        </em>{" "}
        эхэлцгээе.
      </>
    ) : (
      <>
        Start{" "}
        <em className="serif-italic" style={{ color: "var(--accent)" }}>
          exploring
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

          {/* Teacher-set personalization: grade badge + suggested focus.
              Only shown for provisioned accounts (grade/focus present).
              Everything stays fully explorable — this is a starting point. */}
          {(user?.grade || user?.focus) && (
            <div className="mt-4 flex flex-wrap items-center gap-2.5">
              {user?.grade && (
                <span
                  className="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[13px] font-medium"
                  style={{
                    background: "var(--accent-wash)",
                    border: "1px solid var(--accent-line)",
                    color: "var(--accent)",
                  }}
                >
                  {t("personal_grade")} · {user.grade}
                </span>
              )}
              {user?.focus && (
                <span
                  className="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[13px]"
                  style={{
                    background: "var(--bg-2)",
                    border: "1px solid var(--line)",
                    color: "var(--fg-2)",
                  }}
                >
                  <Target className="h-3.5 w-3.5" style={{ color: "var(--fg-2)" }} />
                  {t("personal_focus")}: {user.focus}
                  {user?.focusHref && (
                    <Link
                      href={user.focusHref}
                      className="ml-1 inline-flex items-center gap-0.5 font-medium"
                      style={{ color: "var(--accent)" }}
                    >
                      {t("personal_open")}
                      <ArrowRight className="h-3.5 w-3.5" />
                    </Link>
                  )}
                </span>
              )}
            </div>
          )}
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
              <Link href="/math" className="btn btn-primary">
                {t("empty_btn_primary")}
                <ArrowRight className="ml-1 h-3.5 w-3.5" />
              </Link>
              <Link href="/practice/esh" className="btn btn-line">
                {t("empty_btn_secondary")}
              </Link>
            </div>
          </section>
        ) : (
          <>
            {/* ЭЕШ section — every stat below this header is exam-context only */}
            <div className="eyebrow mt-8">{t("esh_section")}</div>
            {/* Stats grid */}
            <section
              className="grid gap-4 mt-3"
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
                        <span className="flex items-center gap-1.5" style={{ color: "var(--fg-1)" }}>
                          {tt.label}
                          {masteredTopics.has(tt.topic) && (
                            <span
                              className="mono uppercase"
                              style={{
                                fontSize: 9,
                                letterSpacing: "0.08em",
                                color: "var(--accent)",
                                border: "1px solid var(--accent-line)",
                                background: "var(--accent-wash)",
                                borderRadius: 4,
                                padding: "1px 5px",
                              }}
                            >
                              {lang === "mn" ? "Бүрэн эзэмшсэн" : "Mastered"}
                            </span>
                          )}
                        </span>
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

        {/* Exam hubs beyond ЭЕШ — SAT and IB, each in its own score
            language. Rendered only when the hub has activity. */}
        {examHubSummaries.length > 0 && (
          <section className="mt-8">
            <div className="eyebrow mb-3">{t("hubs_section")}</div>
            <div
              className="grid gap-4"
              style={{ gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))" }}
            >
              {examHubSummaries.map((s) => (
                <div key={s.context} className="card-edit p-5 flex flex-col gap-2">
                  <h3 className="serif" style={{ fontWeight: 400, fontSize: 20, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                    {contextLabel(s.context)}
                  </h3>
                  <p className="mono tabular text-[12px]" style={{ color: "var(--fg-3)" }}>
                    {s.correct}/{s.total} {t("hubs_questions")} · {s.accuracy}%
                  </p>
                  <div className="h-[3px] rounded-full overflow-hidden" style={{ background: "var(--bg-2)" }}>
                    <div
                      className="h-full rounded-full"
                      style={{
                        width: `${s.accuracy}%`,
                        background: s.accuracy >= 80 ? "var(--accent)" : s.accuracy >= 50 ? "var(--warn)" : "var(--danger)",
                      }}
                    />
                  </div>
                  <Link
                    href={contextProgressHref(s.context) ?? "/practice"}
                    className="mono text-[11px] uppercase mt-auto inline-flex items-center gap-1"
                    style={{ color: "var(--accent)", letterSpacing: "0.06em" }}
                  >
                    {t("hubs_open")}
                    <ArrowRight className="h-3 w-3" />
                  </Link>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Courses — one card per course the student has actually worked in.
            Stats are per-course only; the weakest unit routes straight back
            into the material. */}
        {courseSummaries.length > 0 && (
          <section className="mt-8">
            <div className="eyebrow mb-3">{t("courses_section")}</div>
            <div
              className="grid gap-4"
              style={{ gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))" }}
            >
              {courseSummaries.map((s) => {
                const unitStats = perf.getTopicStats(s.context);
                const weakestUnit = unitStats.find((u) => u.total >= 2) ?? unitStats[0];
                const href = contextHref(s.context) ?? "/math";
                return (
                  <div key={s.context} className="card-edit p-5 flex flex-col gap-2">
                    <h3 className="serif" style={{ fontWeight: 400, fontSize: 20, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                      {contextLabel(s.context)}
                    </h3>
                    <p className="mono tabular text-[12px]" style={{ color: "var(--fg-3)" }}>
                      {s.correct}/{s.total} {t("courses_checks")} · {s.accuracy}%
                    </p>
                    <div className="h-[3px] rounded-full overflow-hidden" style={{ background: "var(--bg-2)" }}>
                      <div
                        className="h-full rounded-full"
                        style={{
                          width: `${s.accuracy}%`,
                          background: s.accuracy >= 80 ? "var(--accent)" : s.accuracy >= 50 ? "var(--warn)" : "var(--danger)",
                        }}
                      />
                    </div>
                    {weakestUnit && weakestUnit.accuracy < 70 && (
                      <p className="text-[12px]" style={{ color: "var(--fg-2)" }}>
                        {t("courses_weakest")}:{" "}
                        <Link
                          href={`${href}/${weakestUnit.topic}`}
                          className="underline underline-offset-2"
                          style={{ color: "var(--accent)" }}
                        >
                          {humanizeSlug(weakestUnit.topic)}
                        </Link>{" "}
                        <span className="mono tabular" style={{ color: "var(--fg-3)" }}>
                          ({weakestUnit.accuracy}%)
                        </span>
                      </p>
                    )}
                    <Link
                      href={href}
                      className="mono text-[11px] uppercase mt-auto inline-flex items-center gap-1"
                      style={{ color: "var(--accent)", letterSpacing: "0.06em" }}
                    >
                      {t("courses_open")}
                      <ArrowRight className="h-3 w-3" />
                    </Link>
                  </div>
                );
              })}
            </div>
          </section>
        )}

        {/* Placement results — level per course, straight from the local
            placement store. A different instrument than accuracy, so it gets
            its own section rather than a merged number. */}
        {placements.length > 0 && (
          <section className="mt-8">
            <div className="eyebrow mb-3">{t("placement_section")}</div>
            <div
              className="grid gap-4"
              style={{ gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))" }}
            >
              {placements.map((p) => (
                <div key={p.namespace} className="card-edit p-5 flex flex-col gap-1.5">
                  <h3 className="serif" style={{ fontWeight: 400, fontSize: 18, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                    {lang === "mn" ? p.mn : p.en}
                  </h3>
                  <p className="text-[13px]" style={{ color: "var(--fg-1)" }}>
                    {t("placement_level")}: <span style={{ color: "var(--accent)" }}>{p.data.level}</span>
                    <span className="mono tabular ml-2 text-[12px]" style={{ color: "var(--fg-3)" }}>
                      {p.data.overallAccuracy}%
                    </span>
                  </p>
                  <Link
                    href={p.href}
                    className="mono text-[11px] uppercase mt-1 inline-flex items-center gap-1"
                    style={{ color: "var(--accent)", letterSpacing: "0.06em" }}
                  >
                    {t("placement_open")}
                    <ArrowRight className="h-3 w-3" />
                  </Link>
                </div>
              ))}
            </div>
          </section>
        )}
      </div>
    </div>
  );
}
