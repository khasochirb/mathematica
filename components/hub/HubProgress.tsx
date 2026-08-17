"use client";

import { useMemo, useState } from "react";
import Link from "next/link";
import {
  BarChart3,
  Check,
  ChevronDown,
  Target,
  TrendingDown,
  TrendingUp,
  X,
} from "lucide-react";
import BackButton from "@/components/BackButton";
import MathText from "@/components/esh/MathText";
import EshFigure from "@/components/esh/EshFigure";
import usePerformance from "@/lib/use-performance";
import { contextHref } from "@/lib/perf-context";
import { hubTopicLabel, HUB_NATIVE_METRIC_NOTE } from "@/lib/hub-analytics";
import {
  deriveTestRuns,
  RunQuestion,
  runMarks,
  runQuestionLabel,
  runTrend,
  TestRun,
} from "@/lib/test-history";
import { getSatQuestionBySource, getSatTest, listSatTests, scaledScoreEstimate } from "@/lib/sat-test";
import {
  getIbQuestionPartBySource,
  ibGradeEstimate,
  ibPaperSourcePrefix,
  listIbPracticeSets,
} from "@/lib/ib-test";
import { parseTestId } from "@/lib/test-history";

// The full analytics report for an exam hub (SAT / IB) — the same design as
// the ЭШ report at /analytics, deliberately: side-nav sections, a projected
// native score averaged over the most recent sittings, the score-trajectory
// graph, per-domain mastery, every sitting reviewable question by question
// with the full problem and solution, a recent-attempts feed, and the
// mistake bank.
//
// Reads ONLY its own context from the shared attempt stream — the same
// isolation rule as everywhere else. Sittings are reconstructed from the
// server-synced attempts (lib/test-history.ts), so everything here survives
// devices, logouts, and cleared browsers.

// Average the native metric over the most recent sittings so one lucky or
// unlucky paper doesn't swing the headline — mirrors the ЭШ projection.
const PROJECTION_WINDOW = 5;

interface Projection {
  value: string; // big headline number, e.g. "640" or "5"
  scale: string; // the scale it lives on, e.g. "/800" or "/7"
  label: string; // eyebrow phrase before the number
  window: number; // how many sittings fed it
}

function projectSat(runs: TestRun[]): Projection | null {
  // Only full 44-question sittings carry a defensible scaled score.
  const full = runs.filter((r) => r.total >= 44).slice(0, PROJECTION_WINDOW);
  if (full.length === 0) return null;
  const avg = full.reduce((a, r) => a + scaledScoreEstimate(r.correct), 0) / full.length;
  return {
    value: String(Math.round(avg / 10) * 10),
    scale: "/800",
    label: "Projected",
    window: full.length,
  };
}

function projectIb(runs: TestRun[]): Projection | null {
  const marked = runs
    .map((r) => runMarks(r))
    .filter((m): m is { earned: number; total: number } => m !== null && m.total > 0)
    .slice(0, PROJECTION_WINDOW);
  if (marked.length === 0) return null;
  const avgPct = marked.reduce((a, m) => a + (100 * m.earned) / m.total, 0) / marked.length;
  return {
    value: String(ibGradeEstimate(avgPct)),
    scale: "/7",
    label: "Predicted grade",
    window: marked.length,
  };
}

export default function HubProgress({
  context,
  title,
  comingSoonCopy,
}: {
  context: "sat" | "ib";
  title: string;
  comingSoonCopy: string;
}) {
  const perf = usePerformance();
  const [openRun, setOpenRun] = useState<Record<string, boolean>>({});
  const overall = perf.getOverallStats(context);
  const topicStats = perf.getTopicStats(context);
  const hubHome = contextHref(context) ?? "/practice/esh";
  const hasData = overall.total > 0;

  const runs = useMemo(() => deriveTestRuns(perf.attempts, context), [perf.attempts, context]);
  const trend = runTrend(runs);
  const projection = context === "sat" ? projectSat(runs) : projectIb(runs);

  // Recent attempts and the mistake bank — this hub's context only.
  const contextAttempts = useMemo(
    () => perf.attempts.filter((a) => (a.context ?? "esh") === context),
    [perf.attempts, context],
  );
  const recentAttempts = useMemo(() => contextAttempts.slice(-15).reverse(), [contextAttempts]);
  const mistakes = useMemo(
    () => contextAttempts.filter((a) => !a.isCorrect).slice().reverse(),
    [contextAttempts],
  );
  const MISTAKES_PER_PAGE = 20;
  const [mistakePage, setMistakePage] = useState(0);
  const mistakeTotalPages = Math.max(1, Math.ceil(mistakes.length / MISTAKES_PER_PAGE));
  const safeMistakePage = Math.min(mistakePage, mistakeTotalPages - 1);
  const pagedMistakes = mistakes.slice(
    safeMistakePage * MISTAKES_PER_PAGE,
    (safeMistakePage + 1) * MISTAKES_PER_PAGE,
  );

  // testId (source prefix) → display label, from the registries so run
  // rows read "SAT Math Practice Test 3", not "SAT-P3".
  const runLabels = useMemo(() => {
    const map: Record<string, string> = {};
    if (context === "sat") {
      for (const m of listSatTests()) {
        const t = getSatTest(m.testId);
        const prefix = t ? parseTestId(t.module1[0]?.source ?? "") : null;
        if (prefix) map[prefix] = m.label;
      }
    } else {
      for (const set of listIbPracticeSets()) {
        for (const p of set.papers) {
          const prefix = ibPaperSourcePrefix(p.testId, p.paper);
          if (prefix) map[prefix] = `${set.label} · Paper ${p.paper}`;
        }
      }
    }
    return map;
  }, [context]);

  const runLabel = (r: TestRun) => runLabels[r.testId] ?? r.testId;

  // The hub's native metric for one sitting: SAT → estimated scaled score
  // (full 44-question sittings only); IB → self-awarded marks + grade.
  const nativeSummary = (r: TestRun): string | null => {
    if (context === "sat") {
      return r.total >= 44 ? `≈${scaledScoreEstimate(r.correct)}/800` : null;
    }
    const marks = runMarks(r);
    if (!marks) return null;
    return `${marks.earned}/${marks.total} marks · grade ≈${ibGradeEstimate((100 * marks.earned) / marks.total)}`;
  };

  const fmtDate = (t: number) =>
    new Date(t).toLocaleDateString("en-US", { month: "short", day: "numeric" });

  const trajectory = useMemo(
    () =>
      [...runs]
        .sort((a, b) => a.finishedAt - b.finishedAt)
        .map((r) => ({ ts: r.finishedAt, pct: r.accuracy, key: r.runKey })),
    [runs],
  );

  const NAV = [
    { label: "Overview", id: "overview" },
    { label: "Score trajectory", id: "test-history" },
    { label: "By domain", id: "topic-mastery" },
    { label: "Every sitting", id: "sittings" },
    { label: "Recent attempts", id: "recent-attempts" },
    { label: "Mistake bank", id: "mistakes" },
  ];

  return (
    <div
      className="grid min-h-[calc(100vh-64px)] pt-16 grid-cols-1 md:grid-cols-[minmax(0,240px)_minmax(0,1fr)]"
      style={{ background: "var(--bg)" }}
    >
      {/* Side nav — same shape as the ЭШ report. Buttons scroll without
          touching the URL, so browser-back leaves the page instead of
          replaying every scroll jump. */}
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
        <h5 className="eyebrow mb-2.5 px-2">Sections</h5>
        {NAV.map((s) => (
          <button
            key={s.id}
            type="button"
            onClick={() => document.getElementById(s.id)?.scrollIntoView({ behavior: "smooth", block: "start" })}
            className="block w-full text-left px-2.5 py-2 text-[13px] rounded-md"
            style={{ color: "var(--fg-1)" }}
          >
            {s.label}
          </button>
        ))}
        <h5 className="eyebrow mb-2.5 px-2 mt-5">Actions</h5>
        <Link href={hubHome} className="block px-2.5 py-2 text-[13px] rounded-md" style={{ color: "var(--fg-1)" }}>
          {title} hub
        </Link>
        <Link href="/dashboard" className="block px-2.5 py-2 text-[13px] rounded-md" style={{ color: "var(--fg-1)" }}>
          Dashboard
        </Link>
      </aside>

      {/* Main */}
      <section className="px-6 md:px-10 py-9 md:py-12 min-w-0">
        <div className="mb-5">
          <BackButton fallback={hubHome} className="gm-press p-2 rounded-md" />
        </div>

        {/* Head — projected native score, like the ЭШ /800 headline. */}
        <div
          id="overview"
          className="flex items-end justify-between flex-wrap gap-6 pb-7"
          style={{ borderBottom: "1px solid var(--line)", scrollMarginTop: 80 }}
        >
          <div>
            <div className="eyebrow">{title} · Analytics</div>
            <h1
              className="serif"
              style={{
                fontWeight: 400,
                fontSize: "clamp(40px, 5vw, 56px)",
                letterSpacing: "-0.03em",
                margin: "8px 0 0",
                lineHeight: 1,
                color: "var(--fg)",
              }}
            >
              {projection ? (
                <>
                  {projection.label} {projection.value}
                  <span className="mono" style={{ color: "var(--fg-3)", fontSize: 28, letterSpacing: 0 }}>
                    {projection.scale}
                  </span>
                </>
              ) : hasData ? (
                <>Your {title} progress</>
              ) : (
                <>No {title} tests yet</>
              )}
            </h1>
            {projection ? (
              <div className="mt-2.5 text-[13px]" style={{ color: "var(--fg-2)" }}>
                Rolling average of your last {projection.window} sitting{projection.window === 1 ? "" : "s"}
              </div>
            ) : hasData ? (
              <div className="mt-2.5 text-[13px]" style={{ color: "var(--fg-2)" }}>
                {HUB_NATIVE_METRIC_NOTE[context]}
              </div>
            ) : null}
          </div>
          <div className="flex gap-2 items-center">
            <Link href={hubHome} className="btn btn-primary">
              Take a test
            </Link>
          </div>
        </div>

        {!hasData ? (
          <div className="card-edit p-10 mt-7 text-center" style={{ borderStyle: "dashed" }}>
            <BarChart3 className="mx-auto h-8 w-8" style={{ color: "var(--fg-3)" }} />
            <p className="serif mt-4" style={{ fontSize: 20, color: "var(--fg)" }}>
              No {title} practice data yet.
            </p>
            <p className="text-[13px] mt-2 mx-auto" style={{ color: "var(--fg-2)", maxWidth: "44ch" }}>
              {comingSoonCopy}
            </p>
            <Link href={hubHome} className="btn btn-primary mt-6 inline-flex">
              Back to the {title} hub
            </Link>
          </div>
        ) : (
          <>
            {/* Overview cards */}
            <div className="grid gap-4 mt-7" style={{ gridTemplateColumns: "repeat(auto-fit, minmax(160px, 1fr))" }}>
              <div className="card-edit p-5">
                <div className="eyebrow">Questions</div>
                <div className="serif tabular mt-2" style={{ fontSize: 36, letterSpacing: "-0.03em", color: "var(--fg)" }}>
                  {overall.total}
                </div>
              </div>
              <div className="card-edit p-5">
                <div className="eyebrow">Accuracy</div>
                <div className="serif tabular mt-2" style={{ fontSize: 36, letterSpacing: "-0.03em", color: "var(--accent)" }}>
                  {overall.accuracy}%
                </div>
              </div>
              <div className="card-edit p-5">
                <div className="eyebrow">Mock sittings</div>
                <div className="serif tabular mt-2" style={{ fontSize: 36, letterSpacing: "-0.03em", color: "var(--fg)" }}>
                  {runs.length}
                </div>
              </div>
              <div className="card-edit p-5">
                <div className="eyebrow">Mistakes to review</div>
                <div
                  className="serif tabular mt-2"
                  style={{ fontSize: 36, letterSpacing: "-0.03em", color: mistakes.length ? "var(--warn)" : "var(--fg)" }}
                >
                  {mistakes.length}
                </div>
              </div>
            </div>

            {/* Trajectory — the tendency graph, drawn from real sittings. */}
            <div id="test-history" className="card-edit overflow-hidden mt-5" style={{ scrollMarginTop: 80 }}>
              <div className="px-5 py-4 flex items-center justify-between" style={{ borderBottom: "1px solid var(--line)" }}>
                <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                  Score trajectory · {trajectory.length} test{trajectory.length === 1 ? "" : "s"}
                </h3>
                {trend && (
                  <span
                    className="mono text-[10px] uppercase px-1.5 py-0.5 rounded inline-flex items-center gap-1"
                    style={{
                      letterSpacing: "0.08em",
                      border: "1px solid var(--line)",
                      color:
                        trend === "improving" ? "var(--accent)" : trend === "declining" ? "var(--danger)" : "var(--fg-3)",
                    }}
                  >
                    {trend === "improving" ? (
                      <TrendingUp className="h-3 w-3" />
                    ) : trend === "declining" ? (
                      <TrendingDown className="h-3 w-3" />
                    ) : null}
                    {trend}
                  </span>
                )}
              </div>
              <div className="p-5">
                {trajectory.length === 0 ? (
                  <div className="text-[13px] py-10 text-center" style={{ color: "var(--fg-2)" }}>
                    Complete a mock test and your trajectory appears here.
                  </div>
                ) : (
                  (() => {
                    const W = 720;
                    const H = 260;
                    const padL = 50;
                    const padR = 20;
                    const padT = 26;
                    const padB = 36;
                    const innerW = W - padL - padR;
                    const innerH = H - padT - padB;
                    const n = trajectory.length;
                    const xFor = (i: number) => padL + (n === 1 ? innerW / 2 : (i / (n - 1)) * innerW);
                    const yFor = (pct: number) => padT + innerH - (pct / 100) * innerH;
                    const linePath = trajectory
                      .map((p, i) => `${i === 0 ? "M" : "L"}${xFor(i).toFixed(1)},${yFor(p.pct).toFixed(1)}`)
                      .join(" ");
                    const areaPath = `${linePath} L${xFor(n - 1).toFixed(1)},${(padT + innerH).toFixed(1)} L${xFor(0).toFixed(1)},${(padT + innerH).toFixed(1)} Z`;
                    return (
                      <svg viewBox={`0 0 ${W} ${H}`} width="100%" height={H}>
                        <defs>
                          <linearGradient id={`hubtrend-${context}`} x1="0" x2="0" y1="0" y2="1">
                            <stop offset="0%" stopColor="var(--accent)" stopOpacity="0.25" />
                            <stop offset="100%" stopColor="var(--accent)" stopOpacity="0" />
                          </linearGradient>
                        </defs>
                        {[0, 25, 50, 75, 100].map((pct) => (
                          <g key={pct}>
                            <line x1={padL} x2={W - padR} y1={yFor(pct)} y2={yFor(pct)} stroke="var(--line)" strokeWidth={1} />
                            <text x={padL - 8} y={yFor(pct) + 4} textAnchor="end" fontSize={11} fill="var(--fg-3)">
                              {pct}%
                            </text>
                          </g>
                        ))}
                        <path d={areaPath} fill={`url(#hubtrend-${context})`} />
                        <path d={linePath} fill="none" stroke="var(--accent)" strokeWidth={2} />
                        {trajectory.map((p, i) => (
                          <g key={p.key}>
                            <circle cx={xFor(i)} cy={yFor(p.pct)} r={4} fill="var(--accent)" />
                            <text x={xFor(i)} y={yFor(p.pct) - 10} textAnchor="middle" fontSize={11} fill="var(--fg-2)">
                              {p.pct}%
                            </text>
                            <text x={xFor(i)} y={H - 10} textAnchor="middle" fontSize={10} fill="var(--fg-3)">
                              {fmtDate(p.ts)}
                            </text>
                          </g>
                        ))}
                      </svg>
                    );
                  })()
                )}
              </div>
            </div>

            {/* Domain / component breakdown */}
            {topicStats.length > 0 && (
              <div id="topic-mastery" className="card-edit p-6 mt-5" style={{ scrollMarginTop: 80 }}>
                <div className="flex items-center gap-2 mb-4">
                  <Target className="h-4 w-4" style={{ color: "var(--fg-2)" }} />
                  <div className="eyebrow">By domain</div>
                </div>
                <div className="space-y-3">
                  {topicStats.map((tt) => (
                    <div key={tt.topic}>
                      <div className="flex items-baseline justify-between mb-1.5 text-sm">
                        <span style={{ color: "var(--fg-1)" }}>{hubTopicLabel(context, tt.topic)}</span>
                        <span className="mono tabular" style={{ color: "var(--fg-3)", fontSize: 12 }}>
                          {tt.correct}/{tt.total} · {tt.accuracy}%
                        </span>
                      </div>
                      <div className="h-[3px] rounded-full overflow-hidden" style={{ background: "var(--bg-2)" }}>
                        <div
                          className="h-full rounded-full"
                          style={{
                            width: `${tt.accuracy}%`,
                            background:
                              tt.accuracy >= 80 ? "var(--accent)" : tt.accuracy >= 50 ? "var(--warn)" : "var(--danger)",
                          }}
                        />
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Every sitting, expandable to per-question review with the full
                problem and its solution. */}
            {runs.length > 0 && (
              <div id="sittings" className="mt-6" style={{ scrollMarginTop: 80 }}>
                <div className="eyebrow mb-3">Every sitting — question by question</div>
                <div className="space-y-2">
                  {runs.map((r) => {
                    const isOpen = !!openRun[r.runKey];
                    const native = nativeSummary(r);
                    return (
                      <div key={r.runKey} className="card-edit overflow-hidden">
                        <button
                          className="w-full flex items-center gap-3 p-4 text-left"
                          onClick={() => setOpenRun((o) => ({ ...o, [r.runKey]: !o[r.runKey] }))}
                          aria-expanded={isOpen}
                        >
                          <span className="text-sm flex-1" style={{ color: "var(--fg-1)" }}>
                            {runLabel(r)}
                            <span style={{ color: "var(--fg-3)" }}> · {fmtDate(r.finishedAt)}</span>
                          </span>
                          <span className="mono text-xs tabular" style={{ color: "var(--fg-3)" }}>
                            {r.correct}/{r.total}
                            {native ? ` · ${native}` : ""}
                          </span>
                          <ChevronDown
                            className="h-4 w-4 shrink-0 transition-transform"
                            style={{ color: "var(--fg-3)", transform: isOpen ? "rotate(180deg)" : "none" }}
                          />
                        </button>
                        {isOpen && (
                          <div className="px-4 pb-4 border-t pt-3" style={{ borderColor: "var(--line)" }}>
                            <div className="space-y-1.5">
                              {r.questions.map((q) => (
                                <SittingQuestion key={q.source} context={context} q={q} />
                              ))}
                            </div>
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

            {/* Recent attempts */}
            {recentAttempts.length > 0 && (
              <div id="recent-attempts" className="card-edit overflow-hidden mt-6" style={{ scrollMarginTop: 80 }}>
                <div className="px-5 py-4" style={{ borderBottom: "1px solid var(--line)" }}>
                  <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                    Recent attempts
                  </h3>
                </div>
                <div className="p-3">
                  {recentAttempts.map((a, i) => (
                    <div
                      key={`${a.questionSource}-${a.timestamp}-${i}`}
                      className="flex items-center gap-3 px-2 py-2 text-[13px] rounded-md"
                      style={{ background: i % 2 ? "transparent" : "var(--bg-1)" }}
                    >
                      {a.isCorrect ? (
                        <Check className="h-3.5 w-3.5 shrink-0" style={{ color: "var(--accent)" }} />
                      ) : (
                        <X className="h-3.5 w-3.5 shrink-0" style={{ color: "var(--danger)" }} />
                      )}
                      <span className="mono w-24 shrink-0" style={{ color: "var(--fg-2)" }}>
                        {runQuestionLabel(a.questionSource)}
                      </span>
                      <span className="truncate flex-1" style={{ color: "var(--fg-1)" }}>
                        {hubTopicLabel(context, a.topic)}
                      </span>
                      <span className="mono text-[11px] shrink-0" style={{ color: "var(--fg-3)" }}>
                        {fmtDate(a.timestamp)}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Mistake bank — every wrong answer, expandable to the full
                problem with its solution, newest first. */}
            {mistakes.length > 0 && (
              <div id="mistakes" className="card-edit overflow-hidden mt-6" style={{ scrollMarginTop: 80 }}>
                <div className="px-5 py-4 flex items-baseline justify-between" style={{ borderBottom: "1px solid var(--line)" }}>
                  <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                    Mistake bank · {mistakes.length}
                  </h3>
                  <span className="text-[12px]" style={{ color: "var(--fg-3)" }}>
                    Re-solve these until they stop appearing.
                  </span>
                </div>
                <div className="p-3 space-y-1.5">
                  {pagedMistakes.map((a, i) => (
                    <SittingQuestion
                      key={`${a.questionSource}-${a.timestamp}-${i}`}
                      context={context}
                      q={{
                        source: a.questionSource,
                        label: runQuestionLabel(a.questionSource),
                        selected: a.selectedAnswer,
                        correctAnswer: a.correctAnswer,
                        isCorrect: false,
                      }}
                    />
                  ))}
                  {mistakeTotalPages > 1 && (
                    <div className="flex items-center justify-between pt-3 px-1">
                      <button
                        type="button"
                        className="btn btn-line"
                        style={{ fontSize: 12, padding: "7px 14px", opacity: safeMistakePage === 0 ? 0.5 : 1 }}
                        disabled={safeMistakePage === 0}
                        onClick={() => setMistakePage((p) => Math.max(0, p - 1))}
                      >
                        Previous
                      </button>
                      <span className="mono" style={{ fontSize: 11, color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                        Page {safeMistakePage + 1} of {mistakeTotalPages}
                      </span>
                      <button
                        type="button"
                        className="btn btn-line"
                        style={{
                          fontSize: 12,
                          padding: "7px 14px",
                          opacity: safeMistakePage === mistakeTotalPages - 1 ? 0.5 : 1,
                        }}
                        disabled={safeMistakePage === mistakeTotalPages - 1}
                        onClick={() => setMistakePage((p) => Math.min(mistakeTotalPages - 1, p + 1))}
                      >
                        Next
                      </button>
                    </div>
                  )}
                </div>
              </div>
            )}
          </>
        )}
      </section>
    </div>
  );
}

// One question row. Collapsed, it's the terse right/wrong line the student
// already knew ("M1 · Q7 · you: D · key: C"); expanded, it resolves the FULL
// problem from the registry by source id — statement, figure, options with
// the correct one highlighted (SAT) or the part statement, official answer,
// markscheme, and worked solution (IB) — so the whole problem is reviewable
// from the report, not just the score. Shared by the sitting review and the
// mistake bank.
function SittingQuestion({ context, q }: { context: "sat" | "ib"; q: RunQuestion }) {
  const [open, setOpen] = useState(false);
  const resolved =
    context === "sat" ? getSatQuestionBySource(q.source) : getIbQuestionPartBySource(q.source);

  // IB rows record marks as "earned/max" strings (selected "3/4", key
  // "4/4"); SAT rows record the letter/SPR value the student entered.
  const ibEarned = q.selected.includes("/") ? q.selected.split("/")[0] : q.selected || "0";
  const ibMax = q.correctAnswer.split("/")[1] ?? q.correctAnswer;
  const summary =
    context === "sat"
      ? `${q.selected === "" ? "blank" : `you: ${q.selected}`}${
          q.correctAnswer ? ` · key: ${q.correctAnswer}` : ""
        }`
      : `${ibEarned}/${ibMax} marks`;

  return (
    <div
      className="rounded-md overflow-hidden"
      style={{ background: q.isCorrect ? "transparent" : "color-mix(in oklch, var(--danger) 6%, transparent)" }}
    >
      <button
        className="w-full flex items-center gap-2 text-[13px] px-2 py-1.5 text-left"
        onClick={() => setOpen((o) => !o)}
        aria-expanded={open}
        disabled={!resolved}
      >
        {q.isCorrect ? (
          <Check className="h-3.5 w-3.5 shrink-0" style={{ color: "var(--accent)" }} />
        ) : (
          <X className="h-3.5 w-3.5 shrink-0" style={{ color: "var(--danger)" }} />
        )}
        <span className="mono w-20 shrink-0" style={{ color: "var(--fg-2)" }}>
          {q.label}
        </span>
        <span className="mono text-[12px] truncate flex-1" style={{ color: "var(--fg-3)" }}>
          {summary}
        </span>
        {resolved && (
          <ChevronDown
            className="h-3.5 w-3.5 shrink-0 transition-transform"
            style={{ color: "var(--fg-3)", transform: open ? "rotate(180deg)" : "none" }}
          />
        )}
      </button>

      {open && resolved && context === "sat" && "body" in resolved && (
        <div className="px-3 pb-3">
          <div className="text-[13px]" style={{ color: "var(--fg)", lineHeight: 1.7 }}>
            <MathText text={resolved.body} />
          </div>
          {resolved.figure && (
            <div className="mt-3 max-w-xs">
              <EshFigure
                src={resolved.figure.src}
                alt_en={resolved.figure.alt_en}
                alt_mn={resolved.figure.alt_en}
                width={resolved.figure.width}
                height={resolved.figure.height}
              />
            </div>
          )}
          {resolved.format === "mcq" && resolved.options ? (
            <div className="mt-3 space-y-1.5">
              {Object.entries(resolved.options).map(([letter, text]) => {
                const isKey = letter === resolved.answer;
                const isWrongPick = !isKey && letter === q.selected;
                return (
                  <div
                    key={letter}
                    className="text-[13px] rounded-md px-3 py-1.5"
                    style={{
                      border: "1px solid",
                      borderColor: isKey ? "var(--accent-line)" : isWrongPick ? "var(--danger)" : "var(--line)",
                      background: isKey ? "var(--accent-wash)" : "transparent",
                      color: "var(--fg-1)",
                    }}
                  >
                    <span className="mono mr-2" style={{ color: isKey ? "var(--accent)" : "var(--fg-3)" }}>
                      {letter}
                    </span>
                    <MathText text={text} />
                    {isKey ? (
                      <span className="mono text-[10px] ml-2" style={{ color: "var(--accent)" }}>
                        ✓ correct
                      </span>
                    ) : isWrongPick ? (
                      <span className="mono text-[10px] ml-2" style={{ color: "var(--danger)" }}>
                        your answer
                      </span>
                    ) : null}
                  </div>
                );
              })}
            </div>
          ) : (
            <div
              className="mt-3 text-[13px] rounded-md px-3 py-1.5"
              style={{ border: "1px solid var(--accent-line)", background: "var(--accent-wash)", color: "var(--fg-1)" }}
            >
              <span className="mono mr-2" style={{ color: "var(--accent)" }}>
                answer
              </span>
              {(resolved.acceptedAnswers ?? []).join(" or ")}
            </div>
          )}
          <div className="text-[13px] mt-3 pt-3 border-t" style={{ borderColor: "var(--line)", color: "var(--fg-1)", lineHeight: 1.7 }}>
            <MathText text={resolved.solution} />
          </div>
        </div>
      )}

      {open && resolved && context === "ib" && "part" in resolved && (
        <div className="px-3 pb-3">
          {resolved.question.contextIntro && (
            <div className="text-[13px]" style={{ color: "var(--fg-2)", lineHeight: 1.7 }}>
              <MathText text={resolved.question.contextIntro} />
            </div>
          )}
          {resolved.question.figure && (
            <div className="mt-3 max-w-xs">
              <EshFigure
                src={resolved.question.figure.src}
                alt_en={resolved.question.figure.alt_en}
                alt_mn={resolved.question.figure.alt_en}
                width={resolved.question.figure.width}
                height={resolved.question.figure.height}
              />
            </div>
          )}
          <div className="flex items-baseline gap-2 mt-2">
            <span className="mono text-[12px]" style={{ color: "var(--accent)" }}>
              ({resolved.part.label})
            </span>
            <div className="text-[13px] flex-1" style={{ color: "var(--fg-1)", lineHeight: 1.7 }}>
              <MathText text={resolved.part.body} />
            </div>
            <span className="mono text-[11px] shrink-0" style={{ color: "var(--fg-3)" }}>
              [{resolved.part.marks}]
            </span>
          </div>
          <div
            className="rounded-md px-3 py-2 mt-2 text-[13px]"
            style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--fg)" }}
          >
            <MathText text={resolved.part.answer} />
          </div>
          <div className="mt-3 space-y-1">
            {resolved.part.markscheme.map((m, i) => (
              <div key={i} className="flex items-start gap-2 text-[12px]">
                <span
                  className="mono shrink-0 rounded px-1.5 py-0.5 text-[10px] mt-0.5"
                  style={{ border: "1px solid var(--line)", color: "var(--accent)" }}
                >
                  {m.mark}
                </span>
                <span style={{ color: "var(--fg-1)" }}>
                  <MathText text={m.note} />
                </span>
              </div>
            ))}
          </div>
          <div className="text-[13px] mt-3 pt-3 border-t" style={{ borderColor: "var(--line)", color: "var(--fg-1)", lineHeight: 1.7 }}>
            <MathText text={resolved.part.solution} />
          </div>
        </div>
      )}
    </div>
  );
}
