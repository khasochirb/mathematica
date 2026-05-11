"use client";

import React, { useMemo, useState } from "react";
import Link from "next/link";
import usePerformance from "@/lib/use-performance";
import useTestSession from "@/lib/use-test-session";
import { useAuth } from "@/lib/auth-context";
import { useLang } from "@/lib/lang-context";
import { getTestInfo, TOPIC_LABELS } from "@/lib/esh-questions";

type Lang = "mn" | "en";

const i18n = {
  // Side nav
  nav_sections:   { en: "Sections",          mn: "Хэсгүүд" },
  nav_overview:   { en: "Overview",          mn: "Тойм" },
  nav_topic:      { en: "Topic mastery",     mn: "Сэдвийн эзэмшил" },
  nav_history:    { en: "Test history",      mn: "Тестийн түүх" },
  nav_recent:     { en: "Recent attempts",   mn: "Сүүлийн дасгалууд" },
  nav_mistakes:   { en: "Mistakes",          mn: "Алдаа" },
  nav_actions:    { en: "Quick actions",     mn: "Шуурхай үйлдэл" },
  nav_take_eesh:  { en: "Take an ЭЕШ test",  mn: "ЭЕШ тест өгөх" },
  nav_prev:       { en: "Previous year tests", mn: "Өмнөх жилийн тестүүд" },
  nav_hub:        { en: "Practice hub",      mn: "Дадлагын төв" },

  // Head
  head_eyebrow:   { en: "Performance analytics", mn: "Дэлгэрэнгүй мэдээлэл" },
  head_projected: { en: "Projected",         mn: "Таамагласан" },
  head_no_tests:  { en: "No tests yet",      mn: "Одоогоор тест байхгүй" },
  cta_eesh:       { en: "Take an ЭЕШ test",  mn: "ЭЕШ тест өгөх" },
  cta_prev:       { en: "Previous years",    mn: "Өмнөх жилүүд" },

  // Empty state
  empty_eye:      { en: "Get started",       mn: "Эхлэх" },
  empty_t:        { en: "Take a test to see your analytics.", mn: "Тест өгснөөр дэлгэрэнгүй мэдээллээ үзнэ үү." },
  empty_s:        { en: "Your projected score, weak topics, and mistakes show up here as soon as you complete a test.",
                    mn: "Тестээ дуусгасны дараа таамагласан оноо, сул сэдэв, алдааны жагсаалт энд харагдана." },
  empty_cta1:     { en: "Start an ЭЕШ test", mn: "ЭЕШ тест эхлэх" },
  empty_cta2:     { en: "Previous year tests", mn: "Өмнөх жилийн тестүүд" },

  // KPI band
  kpi_projected:  { en: "Projected ЭЕШ score", mn: "Таамагласан ЭЕШ оноо" },
  kpi_basis_pre:  { en: "Based on your last", mn: "Сүүлийн" },
  kpi_basis_post: { en: "tests",              mn: "тестийн дундаж" },
  kpi_basis_one:  { en: "test",               mn: "тест" },
  kpi_basis_avg:  { en: "avg",                mn: "дундаж" },
  kpi_accuracy:   { en: "Overall accuracy", mn: "Зөв хариулсан хувь" },
  kpi_correct:    { en: "correct",          mn: "зөв" },
  kpi_acc_scope:  { en: "across all attempts", mn: "бүх дасгалын дундаж" },
  kpi_tests:      { en: "Tests completed",  mn: "Дуусгасан тест" },
  kpi_tests_scope:{ en: "includes retries", mn: "давталттай" },
  kpi_no_tests:   { en: "No completed tests yet", mn: "Дуусгасан тест байхгүй" },
  kpi_latest:     { en: "Latest",           mn: "Сүүлд" },
  kpi_weak:       { en: "Weak topics",      mn: "Сул сэдэв" },
  kpi_weak_scope: { en: "under 70% accuracy", mn: "70%-аас доош" },
  kpi_lowest:     { en: "Lowest",           mn: "Хамгийн бага" },
  kpi_none_weak:  { en: "Nothing under 70%", mn: "70%-аас доош сэдэв алга" },
  kpi_weak_no_tests: { en: "Take a test to surface weak topics", mn: "Шалгалт өгсний дараа сул сэдвүүд гарах болно" },

  // Trajectory
  traj_h:         { en: "Score trajectory", mn: "Онооны өсөлт" },
  traj_legend:    { en: "Accuracy %",       mn: "Зөв хариулсан хувь" },
  traj_empty:     { en: "Complete a test to plot your trajectory.",
                    mn: "Графикийг үзэхийн тулд тест дуусгана уу." },

  // Recommendations
  rec_eye:        { en: "Recommended next", mn: "Дараагийнх" },
  rec_focus:      { en: "Focus on",         mn: "Анхаарлаа төвлөрүүлэх сэдэв:" },
  rec_first:      { en: "Take your first ЭЕШ test.", mn: "Анхны ЭЕШ тестээ өгөөрэй." },
  rec_solid:      { en: "You're solid across the board.", mn: "Бүх сэдэв дээр сайн байна." },
  rec_no_data:    { en: "We'll start tracking weak topics and trends as soon as you complete one.",
                    mn: "Тестээ дуусгасны дараа сул сэдэв, чиглэлийг бид хянаж эхэлнэ." },
  rec_no_tests_h: { en: "Take a practice test and check back.",
                    mn: "Шалгалт өгөөд эргэж очоорой." },
  rec_no_tests_p: { en: "The recommendation surfaces based on test results.",
                    mn: "Шалгалтын үр дүн дээр үндэслэсэн зөвлөмж эндээс гарах болно." },
  rec_pacing:     { en: "Try a previous year test to confirm exam-day pacing.",
                    mn: "Шалгалтын хурдаа шалгахын тулд өмнөх жилийн тест хийгээрэй." },
  rec_attempt:    { en: "attempt",          mn: "дасгал" },
  rec_practice:   { en: "Practice",         mn: "Дадлага" },
  rec_try_prev:   { en: "Try a previous year test →", mn: "Өмнөх жилийн тест хийх →" },

  // Topic mastery
  tm_h:           { en: "Topic mastery",    mn: "Сэдвийн эзэмшил" },
  tm_tracked:     { en: "tracked",          mn: "хянагдсан" },
  tm_attempts:    { en: "ATTEMPTS",         mn: "ДАСГАЛ" },
  tm_empty:       { en: "No attempts recorded yet.", mn: "Дасгал бүртгэгдээгүй." },
  tm_col_topic:   { en: "Topic",            mn: "Сэдэв" },
  tm_col_mastery: { en: "Mastery",          mn: "Эзэмшил" },
  tm_col_pct:     { en: "%",                mn: "%" },
  tm_col_attempts:{ en: "Attempts",         mn: "Дасгал" },
  tm_col_trend:   { en: "Recent trend",     mn: "Сүүлийн хандлага" },

  // Recent tests
  recent_h:       { en: "Recent tests",     mn: "Сүүлийн тестүүд" },
  recent_take:    { en: "TAKE ANOTHER →",   mn: "ӨӨР ТЕСТ ӨГӨХ →" },
  recent_empty:   { en: "No completed tests yet.", mn: "Дуусгасан тест байхгүй." },
  recent_correct: { en: "correct",          mn: "зөв" },
  recent_skipped: { en: "skipped",          mn: "хариулаагүй" },
  recent_review:  { en: "REVIEW",           mn: "ҮЗЭХ" },

  // Mistake library
  mist_h:         { en: "Mistake library",  mn: "Алдааны сан" },
  mist_recent:    { en: "MOST RECENT FIRST", mn: "СҮҮЛИЙН АЛДАА ЭХЭНДЭЭ" },
  mist_offline:   { en: "Showing cached data — reconnecting…", mn: "Хадгалсан өгөгдлийг үзүүлж байна — холбогдож байна…" },
  mist_empty:     { en: "No incorrect attempts yet — keep going.", mn: "Алдсан дасгал байхгүй — Үргэлжлүүл." },
  mist_col_q:     { en: "Question",         mn: "Бодлого" },
  mist_col_topic: { en: "Topic",            mn: "Сэдэв" },
  mist_col_yours: { en: "Your answer",      mn: "Таны хариу" },
  mist_col_correct:{ en: "Correct",         mn: "Зөв" },
  mist_col_when:  { en: "When",             mn: "Хэзээ" },
  mist_prev:      { en: "← Previous",       mn: "← Өмнөх" },
  mist_next:      { en: "Next →",           mn: "Дараах →" },
  mist_page:      { en: "PAGE",             mn: "ХУУДАС" },
  mist_of:        { en: "OF",               mn: "/" },

  // Trend arrows
  trend_flat:     { en: "flat",             mn: "тогтвортой" },

  // Relative-time
  rel_just_now:   { en: "just now",         mn: "одоо" },
  rel_min:        { en: "m ago",            mn: "м өмнө" },
  rel_hr:         { en: "h ago",            mn: "ц өмнө" },
  rel_day:        { en: "d ago",            mn: "ө өмнө" },
} as const;

function formatRelative(ts: number, lang: Lang): string {
  const diff = Date.now() - ts;
  const min = Math.floor(diff / 60_000);
  if (min < 1) return i18n.rel_just_now[lang];
  if (min < 60) return `${min}${i18n.rel_min[lang]}`;
  const hr = Math.floor(min / 60);
  if (hr < 24) return `${hr}${i18n.rel_hr[lang]}`;
  const day = Math.floor(hr / 24);
  if (day < 7) return `${day}${i18n.rel_day[lang]}`;
  const d = new Date(ts);
  return d.toLocaleDateString(lang === "mn" ? "mn-MN" : undefined, { month: "short", day: "numeric" });
}

function formatTime(ts: number): string {
  const d = new Date(ts);
  return d.toLocaleTimeString(undefined, { hour: "2-digit", minute: "2-digit" });
}

function trendArrow(delta: number, lang: Lang): { text: string; color: string } {
  if (delta > 1) return { text: `▲ +${delta}`, color: "var(--accent)" };
  if (delta < -1) return { text: `▼ ${delta}`, color: "var(--warn)" };
  return { text: `∼ ${i18n.trend_flat[lang]}`, color: "var(--fg-2)" };
}

export default function AnalyticsPage() {
  const perf = usePerformance();
  const ts = useTestSession();
  const { user } = useAuth();
  const { lang } = useLang();
  const langKey: Lang = lang === "mn" ? "mn" : "en";
  const t = (key: keyof typeof i18n) => i18n[key][langKey];

  const overall = perf.getOverallStats();
  const topicStats = perf.getTopicStats();
  // Server-derived test sessions: time-clustered groups of test-mode attempts,
  // synced via Supabase so they survive a fresh-device login. Drives the
  // "Tests completed" count, projection, trajectory, and Recent tests list.
  const testSessions = perf.getTestOnlySessions();
  // Local sessions are still used to look up Review links and Section 2
  // metadata that only lives in localStorage. On a fresh device this list
  // is empty — testSessions covers the cross-device displays.
  const localSessions = ts.getCompletedSessions();
  const incorrectAttempts = useMemo(
    () => perf.attempts.filter((a) => !a.isCorrect).slice().reverse(),
    [perf.attempts],
  );

  const MISTAKES_PER_PAGE = 20;
  const [mistakePage, setMistakePage] = useState(0);
  const mistakeTotalPages = Math.max(1, Math.ceil(incorrectAttempts.length / MISTAKES_PER_PAGE));
  const safeMistakePage = Math.min(mistakePage, mistakeTotalPages - 1);
  const paginatedMistakes = incorrectAttempts.slice(
    safeMistakePage * MISTAKES_PER_PAGE,
    (safeMistakePage + 1) * MISTAKES_PER_PAGE,
  );

  const hasData = overall.total > 0 || testSessions.length > 0;

  const latestServerSession = testSessions[0];
  const latestPct = latestServerSession?.accuracy ?? null;
  // Project from the rolling average of the most recent N completed tests
  // (capped at PROJECTION_WINDOW). Reads from server-derived sessions so a
  // fresh-device login still surfaces the user's projected score. Averaging
  // across sessions smooths out single-test variance — one bad test no
  // longer drags it down, one lucky test no longer inflates. Floor at 400
  // to match the ЭЕШ 400–800 reporting scale.
  const PROJECTION_WINDOW = 5;
  const recentN = Math.min(testSessions.length, PROJECTION_WINDOW);
  const recentAvgPct = testSessions.length
    ? testSessions.slice(0, PROJECTION_WINDOW).reduce((a, s) => a + s.accuracy, 0) / recentN
    : null;
  const projected = recentAvgPct !== null ? Math.min(800, Math.max(400, Math.round(recentAvgPct * 8))) : null;

  // Weak-topic recommendation reads from TEST-mode server attempts only —
  // drill-mode rows (source="drill") and legacy rows (source IS NULL) are
  // excluded so a student who drills Algebra heavily doesn't get told
  // "Algebra is your weakness" when their real weakness shows on tests.
  // No minimum-attempts threshold per directive: a single low-accuracy
  // topic on one test is a real signal worth surfacing.
  const testTopicStats = perf.getTestOnlyTopicStats();
  const hasQualifyingTests = perf.hasTestOnlyData();
  const weakTopics = testTopicStats.filter((t) => t.accuracy < 70);

  // Build score trajectory from server-derived test sessions, oldest → newest.
  // Cross-device-safe — reads from synced attempts table.
  const trajectory = useMemo(() => {
    return testSessions
      .slice()
      .reverse()
      .map((s) => ({
        ts: s.completedAt,
        pct: s.accuracy,
        testKey: s.testKey,
      }));
  }, [testSessions]);

  // Topic deltas: compare last 5 attempts vs prior attempts per topic.
  const topicTrends = useMemo(() => {
    const map: Record<string, { recent: number[]; prior: number[] }> = {};
    for (const a of perf.attempts) {
      if (!map[a.topic]) map[a.topic] = { recent: [], prior: [] };
    }
    for (const tk of Object.keys(map)) {
      const tAttempts = perf.attempts.filter((a) => a.topic === tk);
      const split = Math.max(0, tAttempts.length - 5);
      map[tk].prior = tAttempts.slice(0, split).map((a) => (a.isCorrect ? 1 : 0));
      map[tk].recent = tAttempts.slice(split).map((a) => (a.isCorrect ? 1 : 0));
    }
    const out: Record<string, number> = {};
    for (const [topic, { recent, prior }] of Object.entries(map)) {
      if (recent.length === 0 || prior.length === 0) {
        out[topic] = 0;
        continue;
      }
      const r = (recent.reduce((a, b) => a + b, 0) / recent.length) * 100;
      const p = (prior.reduce((a, b) => a + b, 0) / prior.length) * 100;
      out[topic] = Math.round(r - p);
    }
    return out;
  }, [perf.attempts]);

  const displayTopics = topicStats.map((s) => {
    const delta = topicTrends[s.topic] ?? 0;
    const arrow = trendArrow(delta, langKey);
    return {
      topic: s.topic,
      label: TOPIC_LABELS[s.topic] || s.label,
      accuracy: s.accuracy,
      total: s.total,
      trend: arrow.text,
      trendColor: arrow.color,
      weak: s.accuracy < 50,
    };
  });

  const displayName = user?.displayName || (langKey === "mn" ? "Сурагч" : "Student");

  return (
    <div className="grid min-h-[calc(100vh-64px)] pt-16 grid-cols-1 md:grid-cols-[minmax(0,240px)_minmax(0,1fr)]" style={{ background: "var(--bg)" }}>
      {/* Side nav */}
      <aside
        className="hidden md:block sticky overflow-y-auto"
        style={{
          top: 64,
          alignSelf: "start",
          height: "calc(100vh - 64px)",
          padding: "24px 18px",
          borderRight: "1px solid var(--line)",
        }}
      >
        <h5 className="eyebrow mb-2.5 px-2">{t("nav_sections")}</h5>
        {[
          { label: t("nav_overview"), href: "#overview" },
          { label: t("nav_topic"), href: "#topic-mastery" },
          { label: t("nav_history"), href: "#test-history" },
          { label: t("nav_recent"), href: "#recent-attempts" },
          { label: t("nav_mistakes"), href: "#mistakes" },
        ].map((s) => (
          <a key={s.href} href={s.href} className="block px-2.5 py-2 text-[13px] rounded-md" style={{ color: "var(--fg-1)" }}>
            {s.label}
          </a>
        ))}

        <h5 className="eyebrow mb-2.5 px-2 mt-5">{t("nav_actions")}</h5>
        <Link href="/practice/esh" className="block px-2.5 py-2 text-[13px] rounded-md" style={{ color: "var(--fg-1)" }}>
          {t("nav_take_eesh")}
        </Link>
        <Link href="/practice/esh/test?type=previous" className="block px-2.5 py-2 text-[13px] rounded-md" style={{ color: "var(--fg-1)" }}>
          {t("nav_prev")}
        </Link>
        <Link href="/practice" className="block px-2.5 py-2 text-[13px] rounded-md" style={{ color: "var(--fg-1)" }}>
          {t("nav_hub")}
        </Link>
      </aside>

      {/* Main */}
      <section className="px-6 md:px-10 py-9 md:py-12 min-w-0">
        {/* Head */}
        <div id="overview" className="flex items-end justify-between flex-wrap gap-6 pb-7" style={{ borderBottom: "1px solid var(--line)" }}>
          <div>
            <div className="eyebrow">{t("head_eyebrow")}</div>
            <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(40px, 5vw, 56px)", letterSpacing: "-0.03em", margin: "8px 0 0", lineHeight: 1, color: "var(--fg)" }}>
              {projected !== null ? (
                <>
                  {t("head_projected")} {projected}
                  <span className="mono" style={{ color: "var(--fg-3)", fontSize: 28, letterSpacing: 0 }}>/800</span>
                </>
              ) : (
                <>{t("head_no_tests")}</>
              )}
            </h1>
            <div className="mt-2.5 text-[13px]" style={{ color: "var(--fg-2)" }}>
              <strong style={{ color: "var(--fg)" }}>{displayName}</strong>
            </div>
          </div>
          <div className="flex gap-2 items-center">
            <Link href="/practice/esh" className="btn btn-line">{t("cta_eesh")}</Link>
            <Link href="/practice/esh/test?type=previous" className="btn btn-primary">{t("cta_prev")}</Link>
          </div>
        </div>

        {!hasData && (
          <div
            className="card-edit p-10 mt-7 text-center"
            style={{ borderStyle: "dashed" }}
          >
            <div className="eyebrow" style={{ color: "var(--accent)" }}>{t("empty_eye")}</div>
            <h2 className="serif mt-2" style={{ fontWeight: 400, fontSize: 28, letterSpacing: "-0.02em", color: "var(--fg)" }}>
              {t("empty_t")}
            </h2>
            <p className="mt-2 mb-5 text-[14px]" style={{ color: "var(--fg-2)" }}>
              {t("empty_s")}
            </p>
            <div className="flex gap-3 justify-center">
              <Link href="/practice/esh" className="btn btn-primary">{t("empty_cta1")}</Link>
              <Link href="/practice/esh/test?type=previous" className="btn btn-line">{t("empty_cta2")}</Link>
            </div>
          </div>
        )}

        {hasData && (
          <>
            {/* KPI band: 1 col mobile, 2 col tablet, 4 col desktop.
                On mobile the projection card spans full width (single column
                anyway); on tablet it spans both columns of row 1; on desktop
                it returns to a single column with the original 1.4fr weighting. */}
            <div className="mt-7 grid card-edit overflow-hidden grid-cols-1 sm:grid-cols-2 lg:grid-cols-[minmax(0,1.4fr)_minmax(0,1fr)_minmax(0,1fr)_minmax(0,1fr)]">
              <div
                className="p-7 sm:col-span-2 lg:col-span-1 border-b lg:border-b-0 lg:border-r"
                style={{ borderColor: "var(--line)" }}
              >
                <div className="eyebrow mb-2.5" style={{ wordBreak: "break-word" }}>{t("kpi_projected")}</div>
                <div className="serif tabular" style={{ fontWeight: 400, fontSize: 72, letterSpacing: "-0.04em", lineHeight: 0.95, color: "var(--fg)" }}>
                  {projected ?? "—"}
                  {projected !== null && (
                    <sup className="mono ml-1" style={{ fontSize: 20, color: "var(--fg-3)", verticalAlign: "top" }}>/800</sup>
                  )}
                </div>
                <div className="mono mt-3" style={{ fontSize: 11, color: "var(--fg-2)", letterSpacing: "0.04em" }}>
                  {recentAvgPct !== null
                    ? `${t("kpi_basis_pre")} ${recentN} ${recentN === 1 ? t("kpi_basis_one") : t("kpi_basis_post")} · ${t("kpi_basis_avg")} ${Math.round(recentAvgPct)}%`
                    : t("kpi_no_tests")}
                </div>
                {trajectory.length >= 2 && (
                  <svg viewBox="0 0 400 80" preserveAspectRatio="none" width="100%" height="80" style={{ marginTop: 16 }}>
                    {(() => {
                      const max = 100;
                      const min = 0;
                      const w = 400;
                      const h = 80;
                      const pts = trajectory.map((p, i) => {
                        const x = (i / Math.max(1, trajectory.length - 1)) * w;
                        const y = h - ((p.pct - min) / (max - min)) * (h - 8) - 4;
                        return { x, y };
                      });
                      const d = pts.map((p, i) => `${i === 0 ? "M" : "L"}${p.x.toFixed(1)},${p.y.toFixed(1)}`).join(" ");
                      const area = `${d} L${w},${h} L0,${h} Z`;
                      return (
                        <>
                          <defs>
                            <linearGradient id="k1" x1="0" x2="0" y1="0" y2="1">
                              <stop offset="0" stopColor="var(--accent)" stopOpacity={0.25} />
                              <stop offset="1" stopColor="var(--accent)" stopOpacity={0} />
                            </linearGradient>
                          </defs>
                          <path d={area} fill="url(#k1)" />
                          <path d={d} fill="none" stroke="var(--accent)" strokeWidth={1.5} />
                        </>
                      );
                    })()}
                  </svg>
                )}
              </div>
              {[
                { key: "accuracy" as const, lbl: t("kpi_accuracy"), val: `${overall.accuracy}`, suffix: "%" },
                { key: "tests" as const, lbl: t("kpi_tests"), val: `${testSessions.length}`, suffix: "" },
                { key: "weak" as const, lbl: t("kpi_weak"), val: `${weakTopics.length}`, suffix: ` / ${testTopicStats.length || 0}` },
              ].map((s, i) => {
                // Per-breakpoint border rules (line color from --line):
                // - mobile (1 col): border-b between rows, none on last
                // - tablet (2 col, projection above): accuracy & tests share row,
                //   accuracy gets border-r, weak gets border-t (col-span-2 below)
                // - desktop (4 col, all inline): all three get border-r except last
                const cls = [
                  "p-7",
                  i < 2 && "border-b sm:border-b-0", // mobile only divider
                  i === 0 && "sm:border-r", // accuracy gets right divider on tablet
                  i === 2 && "sm:col-span-2 sm:border-t lg:col-span-1 lg:border-t-0", // weak full-width row on tablet
                  i < 2 && "lg:border-r", // accuracy/tests get right divider on desktop
                ]
                  .filter(Boolean)
                  .join(" ");
                return (
                  <div key={s.key} className={cls} style={{ borderColor: "var(--line)" }}>
                    <div className="eyebrow mb-2.5" style={{ wordBreak: "break-word" }}>{s.lbl}</div>
                    <div className="serif tabular" style={{ fontSize: 44, lineHeight: 1, letterSpacing: "-0.03em", color: "var(--fg)" }}>
                      {s.val}
                      {s.suffix && <span className="mono ml-1" style={{ fontSize: 20, color: "var(--fg-3)" }}>{s.suffix}</span>}
                    </div>
                    <div className="mono mt-3" style={{ fontSize: 11, color: "var(--fg-2)", letterSpacing: "0.04em", overflowWrap: "anywhere" }}>
                      {s.key === "accuracy"
                        ? `${overall.correct}/${overall.total} ${t("kpi_correct")} · ${t("kpi_acc_scope")}`
                        : s.key === "tests"
                          ? latestServerSession
                            ? `${t("kpi_latest")}: ${latestPct}% · ${formatRelative(latestServerSession.completedAt, langKey)} · ${t("kpi_tests_scope")}`
                            : t("kpi_no_tests")
                          : !hasQualifyingTests
                            ? t("kpi_weak_no_tests")
                            : weakTopics.length > 0
                              ? `${t("kpi_lowest")}: ${TOPIC_LABELS[weakTopics[0].topic] || weakTopics[0].topic} · ${t("kpi_weak_scope")}`
                              : t("kpi_none_weak")}
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Row 1: Score trajectory + Recommendations — stacks on mobile/tablet,
                 side-by-side on desktop. */}
            <div className="grid gap-5 mt-5 grid-cols-1 lg:grid-cols-[minmax(0,1.4fr)_minmax(0,1fr)]">
              <div id="test-history" className="card-edit overflow-hidden">
                <div className="px-5 py-4 flex items-center justify-between" style={{ borderBottom: "1px solid var(--line)" }}>
                  <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                    {t("traj_h")} · {trajectory.length} {langKey === "mn" ? "тест" : (trajectory.length === 1 ? "test" : "tests")}
                  </h3>
                  <div className="mono uppercase flex gap-3" style={{ fontSize: 11, color: "var(--fg-2)", letterSpacing: "0.08em" }}>
                    <span><span className="inline-block mr-1.5" style={{ width: 8, height: 8, background: "var(--accent)", borderRadius: 2 }} />{t("traj_legend")}</span>
                  </div>
                </div>
                <div className="p-5">
                  {trajectory.length === 0 && (
                    <div className="text-[13px] py-10 text-center" style={{ color: "var(--fg-2)" }}>
                      {t("traj_empty")}
                    </div>
                  )}
                  {trajectory.length > 0 && (
                    (() => {
                      const W = 720;
                      const H = 300;
                      const padL = 50;
                      const padR = 20;
                      const padT = 30;
                      const padB = 40;
                      const innerW = W - padL - padR;
                      const innerH = H - padT - padB;
                      const n = trajectory.length;
                      const xFor = (i: number) =>
                        padL + (n === 1 ? innerW / 2 : (i / (n - 1)) * innerW);
                      const yFor = (pct: number) =>
                        padT + innerH - (pct / 100) * innerH;
                      const linePath = trajectory
                        .map((p, i) => `${i === 0 ? "M" : "L"}${xFor(i).toFixed(1)},${yFor(p.pct).toFixed(1)}`)
                        .join(" ");
                      const areaPath = `${linePath} L${xFor(n - 1).toFixed(1)},${(padT + innerH).toFixed(1)} L${xFor(0).toFixed(1)},${(padT + innerH).toFixed(1)} Z`;
                      return (
                        <svg viewBox={`0 0 ${W} ${H}`} width="100%" height={H}>
                          <defs>
                            <linearGradient id="band2" x1="0" x2="0" y1="0" y2="1">
                              <stop offset="0" stopColor="var(--accent)" stopOpacity={0.22} />
                              <stop offset="1" stopColor="var(--accent)" stopOpacity={0} />
                            </linearGradient>
                          </defs>
                          <g stroke="var(--line)" strokeWidth={1}>
                            {[0, 25, 50, 75, 100].map((v) => (
                              <line key={v} x1={padL} y1={yFor(v)} x2={W - padR} y2={yFor(v)} />
                            ))}
                          </g>
                          <g fontFamily="var(--font-mono)" fontSize="10" fill="var(--fg-3)">
                            {[0, 25, 50, 75, 100].map((v) => (
                              <text key={v} x={padL - 8} y={yFor(v) + 3} textAnchor="end">{v}%</text>
                            ))}
                          </g>
                          <path d={areaPath} fill="url(#band2)" />
                          <path d={linePath} fill="none" stroke="var(--accent)" strokeWidth={2} />
                          <g fill="var(--fg)">
                            {trajectory.map((p, i) => (
                              <circle key={i} cx={xFor(i)} cy={yFor(p.pct)} r={3.5} />
                            ))}
                          </g>
                          <g fontFamily="var(--font-mono)" fontSize="10" fill="var(--fg-3)">
                            {trajectory.map((p, i) => {
                              if (n > 8 && i % Math.ceil(n / 8) !== 0 && i !== n - 1) return null;
                              const d = new Date(p.ts);
                              const lbl = d.toLocaleDateString(langKey === "mn" ? "mn-MN" : undefined, { month: "short", day: "numeric" });
                              return (
                                <text key={i} x={xFor(i)} y={H - 12} textAnchor="middle">{lbl}</text>
                              );
                            })}
                          </g>
                        </svg>
                      );
                    })()
                  )}
                </div>
              </div>

              <div className="grid gap-5" style={{ alignContent: "start" }}>
                <div
                  className="card-edit p-6"
                  style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
                >
                  <div className="eyebrow" style={{ color: "var(--accent)" }}>{t("rec_eye")}</div>
                  <h4 className="serif mt-1.5" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--accent)" }}>
                    {weakTopics.length > 0
                      ? `${t("rec_focus")} ${TOPIC_LABELS[weakTopics[0].topic] || weakTopics[0].topic}.`
                      : !hasQualifyingTests
                        ? t("rec_no_tests_h")
                        : t("rec_solid")}
                  </h4>
                  <p className="mt-2 mb-4 text-sm" style={{ color: "var(--fg-1)" }}>
                    {weakTopics.length > 0
                      ? (langKey === "mn"
                          ? `Та ${weakTopics.length} сул сэдэв дээр ${weakTopics[0].accuracy}% байна. Дадлага хийгээд таамагласан оноогоо өсгөөрэй.`
                          : `You're at ${weakTopics[0].accuracy}% on ${weakTopics.length} weak topic${weakTopics.length === 1 ? "" : "s"}. Drill them to lift your projected score.`)
                      : !hasQualifyingTests
                        ? t("rec_no_tests_p")
                        : t("rec_pacing")}
                  </p>
                  <div className="grid gap-2">
                    {weakTopics.slice(0, 3).map((t) => (
                      <div
                        key={t.topic}
                        className="grid items-center gap-3 px-3 py-2.5 rounded-lg text-[13px]"
                        style={{
                          background: "var(--bg-1)",
                          border: "1px solid var(--line)",
                          gridTemplateColumns: "1fr auto",
                        }}
                      >
                        <div>
                          <div style={{ color: "var(--fg)" }}>{TOPIC_LABELS[t.topic] || t.label}</div>
                          <div className="eyebrow" style={{ fontSize: 10 }}>
                            {t.accuracy}% · {t.total} {i18n.rec_attempt[langKey]}{langKey === "en" && t.total !== 1 ? "s" : ""}
                          </div>
                        </div>
                        <Link
                          href={`/practice/esh/learn/${t.topic}`}
                          className="btn btn-line"
                          style={{ fontSize: 12, padding: "7px 12px" }}
                        >
                          {i18n.rec_practice[langKey]}
                        </Link>
                      </div>
                    ))}
                    {weakTopics.length === 0 && (
                      <Link
                        href="/practice/esh/test?type=previous"
                        className="btn btn-primary"
                        style={{ fontSize: 12, padding: "9px 12px" }}
                      >
                        {i18n.rec_try_prev[langKey]}
                      </Link>
                    )}
                  </div>
                </div>
              </div>
            </div>

            {/* Row 2: Topic mastery */}
            <div id="topic-mastery" className="card-edit overflow-hidden mt-5">
              <div className="px-5 py-4 flex items-center justify-between" style={{ borderBottom: "1px solid var(--line)" }}>
                <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                  {t("tm_h")} · {displayTopics.length} {t("tm_tracked")}
                </h3>
                <span className="mono" style={{ fontSize: 11, color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                  {overall.total} {t("tm_attempts")}
                </span>
              </div>
              {displayTopics.length === 0 ? (
                <div className="p-8 text-[13px] text-center" style={{ color: "var(--fg-2)" }}>
                  {t("tm_empty")}
                </div>
              ) : (
                <table className="w-full" style={{ borderCollapse: "collapse" }}>
                  <thead>
                    <tr style={{ background: "var(--bg-2)" }}>
                      {[t("tm_col_topic"), t("tm_col_mastery"), t("tm_col_pct"), t("tm_col_attempts"), t("tm_col_trend"), ""].map((h) => (
                        <th
                          key={h}
                          className="mono uppercase text-left"
                          style={{
                            padding: "12px 18px",
                            fontSize: 10,
                            letterSpacing: "0.1em",
                            color: "var(--fg-3)",
                            fontWeight: 500,
                            borderBottom: "1px solid var(--line)",
                          }}
                        >
                          {h}
                        </th>
                      ))}
                    </tr>
                  </thead>
                  <tbody>
                    {displayTopics.map((t) => (
                      <tr key={t.topic} style={{ borderBottom: "1px solid var(--line)" }}>
                        <td style={{ padding: "12px 18px", fontSize: 13, color: "var(--fg)", fontWeight: 500 }}>{t.label}</td>
                        <td style={{ padding: "12px 18px" }}>
                          <span style={{ display: "inline-block", width: 160, height: 4, borderRadius: 99, background: "var(--bg-3)", overflow: "hidden" }}>
                            <span
                              style={{
                                display: "block",
                                height: "100%",
                                width: `${t.accuracy}%`,
                                background: t.weak ? "var(--warn)" : "var(--accent)",
                              }}
                            />
                          </span>
                        </td>
                        <td className="mono tabular" style={{ padding: "12px 18px", fontSize: 13, textAlign: "right", width: 48, color: t.weak ? "var(--warn)" : "var(--fg-1)" }}>
                          {t.accuracy}
                        </td>
                        <td className="mono tabular" style={{ padding: "12px 18px", fontSize: 13, color: "var(--fg-2)" }}>
                          {t.total}
                        </td>
                        <td className="mono" style={{ padding: "12px 18px", fontSize: 11, color: t.trendColor }}>
                          {t.trend}
                        </td>
                        <td style={{ padding: "12px 18px", fontSize: 12 }}>
                          <Link href={`/practice/esh/learn/${t.topic}`} style={{ color: "var(--accent)" }}>{i18n.rec_practice[langKey]} →</Link>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}
            </div>

            {/* Row 3: Recent test history */}
            <div id="recent-attempts" className="card-edit overflow-hidden mt-5">
              <div className="px-5 py-4 flex items-center justify-between" style={{ borderBottom: "1px solid var(--line)" }}>
                <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                  {t("recent_h")}
                </h3>
                <Link href="/practice/esh" className="mono" style={{ fontSize: 11, color: "var(--accent)", letterSpacing: "0.08em" }}>{t("recent_take")}</Link>
              </div>
              {testSessions.length === 0 ? (
                <div className="p-8 text-[13px] text-center" style={{ color: "var(--fg-2)" }}>
                  {t("recent_empty")}
                </div>
              ) : (
                <div>
                  {testSessions.slice(0, 8).map((s, i) => {
                    const info = getTestInfo(s.testKey);
                    // Try to match a local session for the Review link. On a
                    // fresh device this returns undefined and we degrade the
                    // row to display-only (no Review).
                    const localMatch = localSessions.find(
                      (ls) =>
                        ls.testKey === s.testKey &&
                        Math.abs((ls.completedAt ?? ls.startedAt) - s.completedAt) < 60_000,
                    );
                    return (
                      <div
                        key={`${s.testKey}-${s.completedAt}`}
                        className="grid items-center gap-3.5 px-5 py-3.5 text-[13px]"
                        style={{
                          gridTemplateColumns: "100px 1fr auto auto",
                          borderBottom: i < Math.min(7, testSessions.length - 1) ? "1px solid var(--line)" : "none",
                        }}
                      >
                        <span className="mono" style={{ fontSize: 11, color: "var(--fg-3)", letterSpacing: "0.05em" }}>
                          {formatRelative(s.completedAt, langKey)}
                          <br />
                          <span style={{ fontSize: 10 }}>{formatTime(s.completedAt)}</span>
                        </span>
                        <span style={{ color: "var(--fg)" }}>
                          <span
                            className="inline-block mr-2"
                            style={{ width: 8, height: 8, borderRadius: 99, background: s.accuracy >= 70 ? "var(--accent)" : s.accuracy >= 50 ? "var(--fg-2)" : "var(--warn)", verticalAlign: 1 }}
                          />
                          <strong>{info?.label || s.testKey}</strong>
                          <span style={{ color: "var(--fg-2)" }}>
                            {" · "}{s.correct}/{s.total} {t("recent_correct")}
                          </span>
                        </span>
                        <span className="mono tabular" style={{ fontSize: 13, color: s.accuracy >= 70 ? "var(--accent)" : s.accuracy >= 50 ? "var(--fg-1)" : "var(--warn)" }}>
                          {s.accuracy}%
                        </span>
                        {localMatch ? (
                          <Link
                            href={`/practice/esh/test/${s.testKey.toLowerCase()}/results?session=${localMatch.id}`}
                            className="mono"
                            style={{ fontSize: 11, color: "var(--accent)", letterSpacing: "0.05em" }}
                          >
                            {t("recent_review")}
                          </Link>
                        ) : (
                          <span />
                        )}
                      </div>
                    );
                  })}
                </div>
              )}
            </div>

            {/* Mistake library */}
            <div id="mistakes" className="card-edit overflow-hidden mt-5">
              <div className="px-5 py-4 flex items-center justify-between" style={{ borderBottom: "1px solid var(--line)" }}>
                <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                  {t("mist_h")} · {incorrectAttempts.length}
                </h3>
                <span className="mono" style={{ fontSize: 11, color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                  {t("mist_recent")}
                </span>
              </div>
              {perf.isOffline && (
                <div
                  className="mono px-5 py-2 text-[11px]"
                  style={{
                    background: "color-mix(in oklch, var(--warn) 10%, transparent)",
                    borderBottom: "1px solid var(--line)",
                    color: "var(--warn)",
                    letterSpacing: "0.04em",
                  }}
                >
                  {t("mist_offline")}
                </div>
              )}
              {incorrectAttempts.length === 0 ? (
                <div className="p-8 text-[13px] text-center" style={{ color: "var(--fg-2)" }}>
                  {t("mist_empty")}
                </div>
              ) : (
                <>
                  <table className="w-full" style={{ borderCollapse: "collapse" }}>
                    <thead>
                      <tr style={{ background: "var(--bg-2)" }}>
                        {[t("mist_col_q"), t("mist_col_topic"), t("mist_col_yours"), t("mist_col_correct"), t("mist_col_when"), ""].map((h) => (
                          <th
                            key={h}
                            className="mono uppercase text-left"
                            style={{
                              padding: "12px 18px",
                              fontSize: 10,
                              letterSpacing: "0.1em",
                              color: "var(--fg-3)",
                              fontWeight: 500,
                              borderBottom: "1px solid var(--line)",
                            }}
                          >
                            {h}
                          </th>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {paginatedMistakes.map((m, i) => (
                        <tr key={`${m.questionSource}-${m.timestamp}-${i}`} style={{ borderBottom: "1px solid var(--line)" }}>
                          <td className="mono" style={{ padding: "12px 18px", fontSize: 12, color: "var(--fg)", fontWeight: 500 }}>{m.questionSource}</td>
                          <td style={{ padding: "12px 18px", fontSize: 13, color: "var(--fg-2)" }}>{TOPIC_LABELS[m.topic] || m.topic}</td>
                          <td className="mono" style={{ padding: "12px 18px", fontSize: 13, color: "var(--danger)" }}>{m.selectedAnswer || "—"}</td>
                          <td className="mono" style={{ padding: "12px 18px", fontSize: 13, color: "var(--accent)" }}>{m.correctAnswer}</td>
                          <td className="mono" style={{ padding: "12px 18px", fontSize: 12, color: "var(--fg-3)" }}>{formatRelative(m.timestamp, langKey)}</td>
                          <td style={{ padding: "12px 18px", fontSize: 12 }}>
                            <Link href={`/practice/esh/learn/${m.topic}`} style={{ color: "var(--accent)" }}>{i18n.rec_practice[langKey]} →</Link>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                  {mistakeTotalPages > 1 && (
                    <div
                      className="px-5 py-4 flex items-center justify-between gap-3"
                      style={{ borderTop: "1px solid var(--line)" }}
                    >
                      <button
                        type="button"
                        className="btn btn-line"
                        style={{ fontSize: 12, padding: "7px 14px", opacity: safeMistakePage === 0 ? 0.5 : 1 }}
                        disabled={safeMistakePage === 0}
                        onClick={() => setMistakePage((p) => Math.max(0, p - 1))}
                      >
                        {t("mist_prev")}
                      </button>
                      <span className="mono" style={{ fontSize: 11, color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                        {t("mist_page")} {safeMistakePage + 1} {t("mist_of")} {mistakeTotalPages}
                      </span>
                      <button
                        type="button"
                        className="btn btn-line"
                        style={{ fontSize: 12, padding: "7px 14px", opacity: safeMistakePage === mistakeTotalPages - 1 ? 0.5 : 1 }}
                        disabled={safeMistakePage === mistakeTotalPages - 1}
                        onClick={() => setMistakePage((p) => Math.min(mistakeTotalPages - 1, p + 1))}
                      >
                        {t("mist_next")}
                      </button>
                    </div>
                  )}
                </>
              )}
            </div>
          </>
        )}
      </section>
    </div>
  );
}
