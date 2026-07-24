"use client";

import { useMemo, useState } from "react";
import Link from "next/link";
import { BarChart3, Check, ChevronDown, Target, TrendingDown, TrendingUp, X } from "lucide-react";
import BackButton from "@/components/BackButton";
import MathText from "@/components/esh/MathText";
import EshFigure from "@/components/esh/EshFigure";
import usePerformance from "@/lib/use-performance";
import { contextHref } from "@/lib/perf-context";
import { hubTopicLabel, HUB_NATIVE_METRIC_NOTE } from "@/lib/hub-analytics";
import { deriveTestRuns, RunQuestion, runMarks, runTrend, TestRun } from "@/lib/test-history";
import { getSatQuestionBySource, getSatTest, listSatTests, scaledScoreEstimate } from "@/lib/sat-test";
import {
  getIbQuestionPartBySource,
  ibGradeEstimate,
  ibPaperSourcePrefix,
  listIbPracticeSets,
} from "@/lib/ib-test";
import { parseTestId } from "@/lib/test-history";

// The exam-hub progress page (SAT / IB). Reads ONLY its own context from
// the shared attempt stream — the same isolation rule as everywhere else.
// Every completed mock sitting is reconstructed from the server-synced
// attempts (lib/test-history.ts), so the history survives devices,
// logouts, and cleared browsers: score trend, per-sitting native metric
// (scaled score / marks + grade), domain breakdown, and a per-question
// right/wrong review of every sitting.
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
  const hubHome = contextHref(context) ?? "/practice";
  const hasData = overall.total > 0;

  const runs = useMemo(() => deriveTestRuns(perf.attempts, context), [perf.attempts, context]);
  const trend = runTrend(runs);

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

  const latestNative = runs.map(nativeSummary).find((s) => s !== null) ?? null;

  const fmtDate = (t: number) =>
    new Date(t).toLocaleDateString("en-US", { month: "short", day: "numeric" });

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        <div className="flex items-center gap-3 mb-6">
          {/* History-back: this page is reachable from both the dashboard and
              the hub, so back must return to whichever the student came from. */}
          <BackButton fallback={hubHome} className="gm-press p-2 rounded-md" />
          <div className="eyebrow flex-1">{title} · Progress</div>
        </div>

        <h1
          className="serif"
          style={{ fontWeight: 400, fontSize: "clamp(36px, 6vw, 56px)", letterSpacing: "-0.04em", lineHeight: 1.0, color: "var(--fg)" }}
        >
          Your {title} <em className="serif-italic" style={{ color: "var(--accent)" }}>progress</em>.
        </h1>

        {!hasData ? (
          <section className="card-edit p-8 mt-8 text-center">
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
          </section>
        ) : (
          <>
            {/* Overview — this hub's numbers only, in this hub's language */}
            <section
              className="grid gap-4 mt-8"
              style={{ gridTemplateColumns: "repeat(auto-fit, minmax(160px, 1fr))" }}
            >
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
            </section>

            {/* Native metric: the latest sitting's score in this hub's own
                units, or a written promise until the first full sitting. */}
            <section className="card-edit p-5 mt-5" style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}>
              <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>
                {latestNative ? "Latest sitting" : "Native score"}
              </div>
              {latestNative ? (
                <div className="serif tabular" style={{ fontSize: 32, letterSpacing: "-0.03em", color: "var(--fg)" }}>
                  {latestNative}
                </div>
              ) : (
                <p className="text-[13px]" style={{ color: "var(--fg-1)" }}>
                  {HUB_NATIVE_METRIC_NOTE[context]}
                </p>
              )}
            </section>

            {/* Score history + tendency across sittings */}
            {runs.length > 0 && (
              <section className="card-edit p-6 mt-5">
                <div className="flex items-center gap-2 mb-4">
                  <div className="eyebrow flex-1">Score history</div>
                  {trend && (
                    <span
                      className="mono text-[10px] uppercase px-1.5 py-0.5 rounded inline-flex items-center gap-1"
                      style={{
                        letterSpacing: "0.08em",
                        border: "1px solid var(--line)",
                        color: trend === "improving" ? "var(--accent)" : trend === "declining" ? "var(--danger)" : "var(--fg-3)",
                      }}
                    >
                      {trend === "improving" ? <TrendingUp className="h-3 w-3" /> : trend === "declining" ? <TrendingDown className="h-3 w-3" /> : null}
                      {trend}
                    </span>
                  )}
                </div>
                <div className="space-y-2">
                  {[...runs].sort((a, b) => a.finishedAt - b.finishedAt).map((r) => {
                    const color = r.accuracy >= 80 ? "var(--accent)" : r.accuracy >= 50 ? "var(--warn)" : "var(--danger)";
                    return (
                      <div key={r.runKey} className="flex items-center gap-3 px-3 py-2.5 rounded-md" style={{ background: "var(--bg-2)" }}>
                        <span className="text-[12px] w-40 truncate shrink-0" style={{ color: "var(--fg-1)" }}>
                          {runLabel(r)}
                        </span>
                        <div className="flex-1">
                          <div className="h-[3px] rounded-full overflow-hidden" style={{ background: "var(--bg-1)" }}>
                            <div className="h-full rounded-full" style={{ width: `${r.accuracy}%`, background: color }} />
                          </div>
                        </div>
                        <span className="serif tabular w-12 text-right" style={{ fontSize: 15, color }}>
                          {r.accuracy}%
                        </span>
                        <span className="mono text-[10px] w-14 text-right" style={{ color: "var(--fg-3)" }}>
                          {fmtDate(r.finishedAt)}
                        </span>
                      </div>
                    );
                  })}
                </div>
              </section>
            )}

            {/* Domain / component breakdown */}
            {topicStats.length > 0 && (
              <section className="card-edit p-6 mt-5">
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
              </section>
            )}

            {/* Every sitting, expandable to per-question right/wrong */}
            {runs.length > 0 && (
              <section className="mt-6">
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
              </section>
            )}
          </>
        )}
      </div>
    </div>
  );
}

// One question inside an expanded sitting. Collapsed, it's the terse
// right/wrong row the student already knew ("M1 · Q7 · you: D · key: C");
// expanded, it resolves the FULL problem from the registry by source id —
// statement, figure, options with the correct one highlighted (SAT) or the
// part statement, official answer, markscheme, and worked solution (IB) —
// so the whole problem is reviewable from the dashboard, not just the score.
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
