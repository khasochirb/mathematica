"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { ArrowRight, BarChart3, Calculator, ChevronDown, ChevronUp, Sparkles, Target } from "lucide-react";
import { useEffect, useState } from "react";
import usePerformance from "@/lib/use-performance";
import { contextHref, contextLabel, contextProgressHref } from "@/lib/perf-context";
import { loadPlacement, type StoredPlacement } from "@/lib/placement-result";
import { useAuth } from "@/lib/auth-context";
import { useLang } from "@/lib/lang-context";
import useRefinementLoop, { useRecentlyMastered } from "@/lib/use-refinement-loop";
import { getAllQuestions } from "@/lib/esh-questions";
import { courseTotalLessons } from "@/lib/genmath-lessons";
import { hubTopicLabel } from "@/lib/hub-analytics";

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

  // Unified module cards — one vocabulary for every section of the platform
  // (courses, ЭЕШ, SAT, IB) so the dashboard reads the same no matter what
  // mix a student is working on.
  continue_p: {
    en: "Pick up where you left off",
    mn: "Тасалсан газраасаа үргэлжлүүлээрэй",
  },
  continue_btn: { en: "Continue", mn: "Үргэлжлүүлэх" },
  learning_section: { en: "Your learning", mn: "Таны сургалт" },
  tag_course: { en: "Course", mn: "Курс" },
  tag_exam: { en: "Exam prep", mn: "Шалгалтын бэлтгэл" },
  esh_test: { en: "test", mn: "тест" },
  esh_tests: { en: "tests", mn: "тест" },
  questions: { en: "problems", mn: "бодлого" },
  courses_checks: { en: "lesson checks", mn: "хичээлийн даалгавар" },
  courses_lessons: { en: "lessons", mn: "хичээл" },
  weakest_unit: { en: "Weakest unit", mn: "Хамгийн сул нэгж" },
  weakest_topic: { en: "Weakest topic", mn: "Хамгийн сул сэдэв" },
  focus_btn_master: { en: "Master this topic", mn: "Бүрэн эзэмших" },
  open: { en: "Open", mn: "Нээх" },
  details: { en: "Details", mn: "Дэлгэрэнгүй" },

  // Inline analysis panel — expands under the module grid when a badge's
  // "Details" is tapped. Stays on the dashboard (no navigation, no confusing
  // back button); the "Full report" card inside is the only off-page door.
  analysis_eyebrow: { en: "Analysis", mn: "Шинжилгээ" },
  hide: { en: "Hide", mn: "Хаах" },
  units_eyebrow: { en: "Top units", mn: "Гол нэгжүүд" },
  stat_lessons: { en: "Lessons", mn: "Хичээл" },
  stat_checks: { en: "Lesson checks", mn: "Хичээлийн даалгавар" },
  stat_total: { en: "Total problems", mn: "Нийт бодсон бодлого" },
  stat_accuracy: { en: "Accuracy", mn: "Зөв хариулсан хувь" },
  stat_tests: { en: "Tests completed", mn: "Дуусгасан тест" },
  stat_latest: { en: "Latest test", mn: "Сүүлийн тестийн дүн" },
  focus_eyebrow: { en: "Focus · weakest topic", mn: "Анхаарах сул сэдэв" },
  focus_btn_learn: { en: "Learn", mn: "Суралцах" },
  focus_btn_practice: { en: "Take a test", mn: "Шалгалт өгөх" },
  focus_well_eyebrow: { en: "Focus", mn: "Анхаарах" },
  focus_well_h: { en: "You're solid across the board.", mn: "Бүх сэдэв дээр сайн байна." },
  focus_well_p: {
    en: "No clear weak topic right now. Keep taking tests to confirm.",
    mn: "Одоогоор тодорхой сул сэдэв алга. Илүү шалгалт өгч баталгаажуулцгаая.",
  },
  topics_eyebrow: { en: "Top topics", mn: "Гол сэдвүүд" },
  mastered_badge: { en: "Mastered", mn: "Бүрэн эзэмшсэн" },
  analytics_eyebrow: { en: "Detailed analytics", mn: "Дэлгэрэнгүй мэдээлэл" },
  analytics_h: { en: "Full report", mn: "Бүрэн тайлан" },
  analytics_p: {
    en: "Score trajectory, topic breakdown, test history, and your mistake bank.",
    mn: "Онооны өсөлт, сэдвийн задаргаа, шалгалтын түүх, алдааны сан.",
  },
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

  // Per-section summaries: one entry per context the student has touched
  // (esh, each course, sat, ib), stats computed ONLY from that context's
  // attempts, sorted by most-recent activity. This IS the dashboard: every
  // entry renders as the same module card, so a student mixing courses,
  // ЭЕШ prep, and SAT sees one uniform, scannable grid — never one section
  // dominating the others.
  const contextSummaries = perf.getContextSummaries();
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

  const hasData = contextSummaries.length > 0 || testSessions.length > 0;
  const userName = user?.displayName ?? "";

  // Weak-topic recommendation reads from TEST-mode server attempts only —
  // drill rows excluded so the focus card doesn't recommend the topic the
  // student happens to drill instead of the one they struggle with on tests.
  const testTopicStats = perf.getTestOnlyTopicStats();
  // §5: a topic mastered in the last 14 days is hidden from the weak-spot card
  // even if its accuracy still lags (stats trail the actual learning).
  const masteredTopics = useRecentlyMastered();
  const weakTopics = testTopicStats.filter((t) => t.accuracy < 70 && !masteredTopics.has(t.topic));
  const weakest = weakTopics[0]; // already sorted asc by accuracy — ЭЕШ card only

  const hasQualifyingTests = perf.hasTestOnlyData();

  // Which module's analysis panel is expanded inline under the grid.
  // null = untouched (auto-open the most recently active module once data
  // loads); "" = user collapsed everything. The panel never navigates —
  // depth lives on the dashboard itself, so "back" always behaves.
  const [expanded, setExpanded] = useState<string | null>(null);
  const firstContext = contextSummaries[0]?.context;
  useEffect(() => {
    if (firstContext) setExpanded((cur) => (cur === null ? firstContext : cur));
  }, [firstContext]);
  const expandedSummary = contextSummaries.find((s) => s.context === expanded);

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
            </div>
          </section>
        ) : (
          <>
            {/* Continue strip — the single most recently active module, one
                obvious next click. Only shown when the student juggles more
                than one module; with a single module its card IS the CTA. */}
            {contextSummaries.length > 1 && (
              <section
                className="card-edit p-5 mt-8 flex flex-wrap items-center justify-between gap-3"
                style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
              >
                <div>
                  <div className="eyebrow" style={{ color: "var(--accent)" }}>
                    {t("continue_p")}
                  </div>
                  <p
                    className="serif mt-1"
                    style={{ fontWeight: 400, fontSize: 24, letterSpacing: "-0.02em", color: "var(--fg)" }}
                  >
                    {contextLabel(contextSummaries[0].context)}
                  </p>
                </div>
                <Link
                  href={contextHref(contextSummaries[0].context) ?? "/math"}
                  className="btn btn-primary"
                >
                  {t("continue_btn")}
                  <ArrowRight className="ml-1 h-3.5 w-3.5" />
                </Link>
              </section>
            )}

            {/* One identical card per module the student works in — course,
                ЭЕШ, SAT, IB — newest activity first. Same shape everywhere:
                what it is, how far along, accuracy, weakest spot, one Open
                link. Depth lives in each module's own progress page. */}
            <section className="mt-8">
              <div className="eyebrow mb-3">{t("learning_section")}</div>
              <div
                className="grid gap-4"
                style={{ gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))" }}
              >
                {contextSummaries.map((s) => {
                  const isCourse = s.context.startsWith("course:");
                  const isEsh = s.context === "esh";
                  const isExpanded = expanded === s.context;
                  const openHref = contextHref(s.context) ?? "/math";
                  // Course progress bar — lessons worked / total.
                  const lessonsTotal = isCourse ? courseTotalLessons(s.context) : null;
                  const lessonsWorked = isCourse ? perf.getLessonsWorked(s.context) : 0;
                  const progressPct =
                    lessonsTotal && lessonsTotal > 0
                      ? Math.min(100, Math.round((lessonsWorked / lessonsTotal) * 100))
                      : 0;
                  const unitStats = isCourse ? perf.getTopicStats(s.context) : [];
                  const weakestUnit = isCourse
                    ? (unitStats.find((u) => u.total >= 2) ?? unitStats[0])
                    : undefined;
                  const metric = isEsh
                    ? `${testSessions.length} ${t(testSessions.length === 1 ? "esh_test" : "esh_tests")} · ${s.total} ${t("questions")} · ${s.accuracy}%`
                    : isCourse
                      ? `${s.correct}/${s.total} ${t("courses_checks")} · ${s.accuracy}%`
                      : `${s.total} ${t("questions")} · ${s.accuracy}%`;
                  return (
                    <div
                      key={s.context}
                      className="card-edit p-5 flex flex-col gap-2"
                      style={isExpanded ? { borderColor: "var(--accent)" } : undefined}
                    >
                      <div className="eyebrow">{isCourse ? t("tag_course") : t("tag_exam")}</div>
                      <h3
                        className="serif"
                        style={{ fontWeight: 400, fontSize: 20, letterSpacing: "-0.02em", color: "var(--fg)" }}
                      >
                        {contextLabel(s.context)}
                      </h3>
                      {isCourse && lessonsTotal !== null && lessonsTotal > 0 && (
                        <div>
                          <p className="mono tabular text-[12px]" style={{ color: "var(--fg-2)" }}>
                            {lessonsWorked} / {lessonsTotal} {t("courses_lessons")} · {progressPct}%
                          </p>
                          <div
                            className="h-[5px] rounded-full overflow-hidden mt-1.5"
                            style={{ background: "var(--bg-2)" }}
                          >
                            <div
                              className="h-full rounded-full"
                              style={{ width: `${progressPct}%`, background: "var(--accent)" }}
                            />
                          </div>
                        </div>
                      )}
                      <p className="mono tabular text-[12px] mt-0.5" style={{ color: "var(--fg-3)" }}>
                        {metric}
                      </p>
                      <div className="h-[3px] rounded-full overflow-hidden" style={{ background: "var(--bg-2)" }}>
                        <div
                          className="h-full rounded-full"
                          style={{
                            width: `${s.accuracy}%`,
                            background:
                              s.accuracy >= 80
                                ? "var(--accent)"
                                : s.accuracy >= 50
                                  ? "var(--warn)"
                                  : "var(--danger)",
                          }}
                        />
                      </div>
                      {isCourse && weakestUnit && weakestUnit.accuracy < 70 && (
                        <p className="text-[12px]" style={{ color: "var(--fg-2)" }}>
                          {t("weakest_unit")}:{" "}
                          <Link
                            href={`${openHref}/${weakestUnit.topic}`}
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
                      {isEsh && weakest && (
                        <p className="text-[12px]" style={{ color: "var(--fg-2)" }}>
                          {t("weakest_topic")}:{" "}
                          <Link
                            href={`/practice/esh/learn/${weakest.topic}`}
                            className="underline underline-offset-2"
                            style={{ color: "var(--accent)" }}
                          >
                            {weakest.label}
                          </Link>{" "}
                          <span className="mono tabular" style={{ color: "var(--fg-3)" }}>
                            ({weakest.accuracy}%)
                          </span>
                        </p>
                      )}
                      <div className="mt-auto pt-1 flex flex-wrap items-center gap-x-4 gap-y-1.5">
                        <Link
                          href={openHref}
                          className="mono text-[11px] uppercase inline-flex items-center gap-1"
                          style={{ color: "var(--accent)", letterSpacing: "0.06em" }}
                        >
                          {t("open")}
                          <ArrowRight className="h-3 w-3" />
                        </Link>
                        <button
                          type="button"
                          onClick={() => setExpanded(isExpanded ? "" : s.context)}
                          className="mono text-[11px] uppercase inline-flex items-center gap-1"
                          style={{
                            color: isExpanded ? "var(--accent)" : "var(--fg-3)",
                            letterSpacing: "0.06em",
                          }}
                        >
                          {isExpanded ? t("hide") : t("details")}
                          {isExpanded ? (
                            <ChevronUp className="h-3 w-3" />
                          ) : (
                            <ChevronDown className="h-3 w-3" />
                          )}
                        </button>
                        {isEsh && weakest && (
                          <button
                            type="button"
                            onClick={() => startTopicLoop(weakest.topic)}
                            className="mono text-[11px] uppercase inline-flex items-center gap-1"
                            style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}
                          >
                            <Target className="h-3 w-3" />
                            {t("focus_btn_master")}
                          </button>
                        )}
                      </div>
                    </div>
                  );
                })}
              </div>

              {/* Inline analysis panel — the expanded badge's full analysis,
                  right here on the dashboard. Never navigates, so the back
                  button never strands the student on a hub page. */}
              {expandedSummary &&
                (() => {
                  const s = expandedSummary;
                  const isCourse = s.context.startsWith("course:");
                  const isEsh = s.context === "esh";
                  const openHref = contextHref(s.context) ?? "/math";
                  const pOverall = perf.getOverallStats(s.context);
                  const pTopics = perf.getTopicStats(s.context);
                  const pSessions = isCourse ? [] : perf.getTestOnlySessions(s.context);
                  const pLatest = pSessions[0]?.accuracy ?? null;
                  const lessonsTotal = isCourse ? courseTotalLessons(s.context) : null;
                  const lessonsWorked = isCourse ? perf.getLessonsWorked(s.context) : 0;
                  const stripLabel = (topic: string, label: string) =>
                    isEsh ? label : isCourse ? humanizeSlug(topic) : hubTopicLabel(s.context, topic);
                  const stripHref = (topic: string) =>
                    isEsh ? `/practice/esh/learn/${topic}` : isCourse ? `${openHref}/${topic}` : null;
                  // Full report: ЭЕШ → /analytics (projected score, trajectory,
                  // mistake bank); SAT/IB → their progress pages. Courses have
                  // no deeper page — this panel IS their analytics.
                  const reportHref = isEsh ? "/analytics" : contextProgressHref(s.context);
                  const tiles: { lbl: string; val: string; suffix: string; accent?: boolean }[] =
                    isCourse
                      ? [
                          ...(lessonsTotal && lessonsTotal > 0
                            ? [{ lbl: t("stat_lessons"), val: `${lessonsWorked}`, suffix: ` / ${lessonsTotal}` }]
                            : []),
                          { lbl: t("stat_checks"), val: `${pOverall.total}`, suffix: "" },
                          { lbl: t("stat_accuracy"), val: `${pOverall.accuracy}`, suffix: "%", accent: true },
                        ]
                      : [
                          { lbl: t("stat_total"), val: `${pOverall.total}`, suffix: "" },
                          { lbl: t("stat_accuracy"), val: `${pOverall.accuracy}`, suffix: "%", accent: true },
                          { lbl: t("stat_tests"), val: `${pSessions.length}`, suffix: "" },
                          ...(pLatest !== null
                            ? [{ lbl: t("stat_latest"), val: `${pLatest}`, suffix: "%" }]
                            : []),
                        ];
                  return (
                    <div
                      className="card-edit p-5 md:p-6 mt-4"
                      style={{ borderColor: "var(--accent-line)" }}
                    >
                      <div className="eyebrow mb-4" style={{ color: "var(--accent)" }}>
                        {contextLabel(s.context)} · {t("analysis_eyebrow")}
                      </div>

                      {/* Stat tiles */}
                      <div
                        className="grid gap-3"
                        style={{ gridTemplateColumns: "repeat(auto-fit, minmax(140px, 1fr))" }}
                      >
                        {tiles.map((tile) => (
                          <div
                            key={tile.lbl}
                            className="rounded-lg p-4"
                            style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}
                          >
                            <div className="eyebrow">{tile.lbl}</div>
                            <div
                              className="serif tabular mt-1.5"
                              style={{
                                fontSize: 34,
                                lineHeight: 1,
                                letterSpacing: "-0.03em",
                                color: tile.accent ? "var(--accent)" : "var(--fg)",
                              }}
                            >
                              {tile.val}
                              {tile.suffix && (
                                <span className="mono ml-1" style={{ fontSize: 15, color: "var(--fg-3)" }}>
                                  {tile.suffix}
                                </span>
                              )}
                            </div>
                          </div>
                        ))}
                      </div>

                      {/* Focus (ЭЕШ weakest topic) + topic/unit breakdown */}
                      <div
                        className="grid gap-3 mt-3"
                        style={{ gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))" }}
                      >
                        {isEsh &&
                          (weakest ? (
                            <div
                              className="rounded-lg p-5"
                              style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)" }}
                            >
                              <div className="eyebrow">{t("focus_eyebrow")}</div>
                              <h3
                                className="serif mt-2"
                                style={{ fontWeight: 400, fontSize: 24, letterSpacing: "-0.02em", color: "var(--fg)" }}
                              >
                                {weakest.label}
                              </h3>
                              <p className="text-[13px] mt-1.5" style={{ color: "var(--fg-1)" }}>
                                {lang === "mn"
                                  ? `Одоогийн зөв хариу: ${weakest.accuracy}% (${weakest.correct}/${weakest.total}). Дадлага хийж түвшингээ өсгөөрэй.`
                                  : `Current accuracy: ${weakest.accuracy}% (${weakest.correct}/${weakest.total}). More practice will lift it.`}
                              </p>
                              <div className="flex flex-wrap gap-2 mt-4">
                                <button
                                  type="button"
                                  onClick={() => startTopicLoop(weakest.topic)}
                                  className="btn btn-primary"
                                >
                                  <Target className="h-3.5 w-3.5" />
                                  {t("focus_btn_master")}
                                </button>
                                <Link href={`/practice/esh/learn/${weakest.topic}`} className="btn btn-line">
                                  {t("focus_btn_learn")}
                                </Link>
                                <Link href="/practice/esh" className="btn btn-line">
                                  {t("focus_btn_practice")}
                                </Link>
                              </div>
                            </div>
                          ) : (
                            <div
                              className="rounded-lg p-5"
                              style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}
                            >
                              <div className="eyebrow">{t("focus_well_eyebrow")}</div>
                              <h3
                                className="serif mt-2"
                                style={{ fontWeight: 400, fontSize: 24, letterSpacing: "-0.02em", color: "var(--fg)" }}
                              >
                                {hasQualifyingTests ? t("focus_well_h") : t("focus_btn_practice")}
                              </h3>
                              <p className="text-[13px] mt-1.5" style={{ color: "var(--fg-1)" }}>
                                {t("focus_well_p")}
                              </p>
                              <div className="mt-4">
                                <Link href="/practice/esh" className="btn btn-primary">
                                  {t("focus_btn_practice")}
                                  <ArrowRight className="ml-1 h-3.5 w-3.5" />
                                </Link>
                              </div>
                            </div>
                          ))}

                        {pTopics.length > 0 && (
                          <div
                            className="rounded-lg p-5"
                            style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}
                          >
                            <div className="flex items-center gap-2 mb-4">
                              <Sparkles className="h-3.5 w-3.5" style={{ color: "var(--fg-2)" }} />
                              <div className="eyebrow">
                                {isCourse ? t("units_eyebrow") : t("topics_eyebrow")}
                              </div>
                            </div>
                            <div className="space-y-3">
                              {pTopics.slice(0, 5).map((tt) => {
                                const href = stripHref(tt.topic);
                                const label = stripLabel(tt.topic, tt.label);
                                return (
                                  <div key={tt.topic}>
                                    <div className="flex items-baseline justify-between gap-2 text-[13px] mb-1">
                                      <span style={{ color: "var(--fg)" }}>
                                        {href ? (
                                          <Link
                                            href={href}
                                            className="underline underline-offset-2 decoration-[color:var(--line)]"
                                          >
                                            {label}
                                          </Link>
                                        ) : (
                                          label
                                        )}
                                        {isEsh && masteredTopics.has(tt.topic) && (
                                          <span
                                            className="mono uppercase ml-2"
                                            style={{ fontSize: 9, letterSpacing: "0.08em", color: "var(--accent)" }}
                                          >
                                            {t("mastered_badge")}
                                          </span>
                                        )}
                                      </span>
                                      <span className="mono tabular" style={{ color: "var(--fg-3)", fontSize: 12 }}>
                                        {tt.correct}/{tt.total} · {tt.accuracy}%
                                      </span>
                                    </div>
                                    <div
                                      className="h-[3px] rounded-full overflow-hidden"
                                      style={{ background: "var(--bg-3)" }}
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
                                );
                              })}
                            </div>
                          </div>
                        )}
                      </div>

                      {/* Full report — ЭЕШ: projected score, trajectory graph,
                          test history, mistake bank on /analytics. */}
                      {reportHref && reportHref !== openHref && (
                        <Link
                          href={reportHref}
                          className="rounded-lg p-5 mt-3 flex items-center justify-between gap-4 group"
                          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", display: "flex" }}
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
                              <BarChart3 className="h-5 w-5" />
                            </div>
                            <div>
                              <h3
                                className="serif"
                                style={{ fontWeight: 400, fontSize: 20, letterSpacing: "-0.02em", color: "var(--fg)" }}
                              >
                                {t("analytics_h")}
                              </h3>
                              {isEsh && (
                                <p className="text-[13px] mt-0.5" style={{ color: "var(--fg-2)" }}>
                                  {t("analytics_p")}
                                </p>
                              )}
                            </div>
                          </div>
                          <ArrowRight className="h-5 w-5 shrink-0" style={{ color: "var(--accent)" }} />
                        </Link>
                      )}
                    </div>
                  );
                })()}
            </section>
          </>
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
