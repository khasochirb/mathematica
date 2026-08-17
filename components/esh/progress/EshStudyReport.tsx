"use client";

// The ЭШ study report — everything the hub's progress page used to own that
// the dashboard report did not: per-sitting question-by-question review, the
// topic breakdown chart, severity-graded study routing, weak-skill routing,
// flagged questions, and the next-test recommendation.
//
// It lives as a component because ЭШ used to have TWO progress pages — the
// dashboard report at /analytics and this one at /practice/esh/progress —
// while SAT and IB each had one page reached from two doors. Moving this block
// into /analytics makes ЭШ match: one report, two entry points.
//
// Mongolian throughout, like the rest of the ЭШ hub: the language is a
// property of the hub, not of the site toggle (memory/expansion-vision.md §4.7).

import { useState } from "react";
import Link from "next/link";
import { Check, ChevronDown, Flag, Target, X } from "lucide-react";
import TopicBreakdownChart from "@/components/esh/TopicBreakdownChart";
import useESHProgress from "@/lib/use-esh-progress";
import usePerformance from "@/lib/use-performance";
import { TOPIC_LABELS, getTestInfo } from "@/lib/esh-questions";
import { getStudyTarget } from "@/lib/exam-study-map";
import { getSkillStudyTarget } from "@/lib/skill-study-map";
import { eshSeverity, BAND_LABELS, type Band } from "@/lib/ratings";

const BAND_COLOR: Record<Band, string> = {
  beginner: "var(--danger)",
  developing: "var(--warn)",
  strong: "var(--accent)",
  mastery: "var(--accent)",
};

export default function EshStudyReport() {
  const progress = useESHProgress();
  const perf = usePerformance();
  const [openEntry, setOpenEntry] = useState<Record<string, boolean>>({});

  const topicStats = progress.topicMastery.map((t) => ({
    topic: t.topic,
    correct: Math.round((t.accuracy * t.totalAttempts) / 100),
    total: t.totalAttempts,
    accuracy: t.accuracy,
  }));

  const weakSkills = perf.getWeakSkills();

  const hasAnything =
    progress.scoreHistory.length > 0 ||
    topicStats.length > 0 ||
    progress.weakTopics.length > 0 ||
    weakSkills.length > 0 ||
    progress.flaggedCount > 0;

  if (!hasAnything) return null;

  return (
    <div className="space-y-6 mt-8" id="esh-study" style={{ scrollMarginTop: 80 }}>
      {/* Score history — every sitting, expandable to the question level. */}
      {progress.scoreHistory.length > 0 && (
        <div className="card-edit p-5">
          <div className="eyebrow mb-4">Шалгалтын оноо</div>
          <div className="space-y-2">
            {progress.scoreHistory.map((entry, i) => {
              const color =
                entry.accuracy >= 80 ? "var(--accent)" : entry.accuracy >= 50 ? "var(--warn)" : "var(--danger)";
              const entryKey = `${entry.testKey}@${entry.date}`;
              const isOpen = !!openEntry[entryKey];
              const hasDetail = !!entry.run && entry.run.questions.length > 0;
              return (
                <div key={i} className="rounded-md overflow-hidden" style={{ background: "var(--bg-2)" }}>
                  <button
                    className="w-full flex items-center gap-3 px-3 py-2.5 text-left"
                    onClick={() => hasDetail && setOpenEntry((o) => ({ ...o, [entryKey]: !o[entryKey] }))}
                    aria-expanded={isOpen}
                    style={{ cursor: hasDetail ? "pointer" : "default" }}
                  >
                    <span
                      className="mono tabular w-9 h-7 rounded flex items-center justify-center text-[11px] shrink-0"
                      style={{
                        background: "var(--bg-1)",
                        border: "1px solid var(--line)",
                        color: "var(--fg)",
                        letterSpacing: "0.04em",
                      }}
                    >
                      {entry.testKey}
                    </span>
                    <div className="flex-1">
                      <div className="h-[3px] rounded-full overflow-hidden" style={{ background: "var(--bg-1)" }}>
                        <div
                          className="h-full rounded-full transition-all"
                          style={{ width: `${entry.accuracy}%`, background: color }}
                        />
                      </div>
                    </div>
                    <span className="serif tabular w-12 text-right" style={{ fontSize: 16, color }}>
                      {entry.accuracy}%
                    </span>
                    <span className="mono text-[10px] w-16 text-right" style={{ color: "var(--fg-3)" }}>
                      {new Date(entry.date).toLocaleDateString("mn-MN", { month: "short", day: "numeric" })}
                    </span>
                    {hasDetail && (
                      <ChevronDown
                        className="h-3.5 w-3.5 shrink-0 transition-transform"
                        style={{ color: "var(--fg-3)", transform: isOpen ? "rotate(180deg)" : "none" }}
                      />
                    )}
                  </button>
                  {isOpen && entry.run && (
                    <div className="px-3 pb-3 border-t pt-2" style={{ borderColor: "var(--line)" }}>
                      <div className="grid gap-1" style={{ gridTemplateColumns: "repeat(auto-fill, minmax(220px, 1fr))" }}>
                        {entry.run.questions.map((q) => (
                          <div
                            key={q.source}
                            className="flex items-center gap-1.5 text-[12px] rounded px-1.5 py-0.5"
                            style={{
                              background: q.isCorrect ? "transparent" : "color-mix(in oklch, var(--danger) 7%, transparent)",
                            }}
                          >
                            {q.isCorrect ? (
                              <Check className="h-3 w-3 shrink-0" style={{ color: "var(--accent)" }} />
                            ) : (
                              <X className="h-3 w-3 shrink-0" style={{ color: "var(--danger)" }} />
                            )}
                            <span className="mono w-10 shrink-0" style={{ color: "var(--fg-2)" }}>
                              {q.label}
                            </span>
                            <span className="mono truncate" style={{ color: "var(--fg-3)" }}>
                              {q.selected === "" ? "—" : q.selected}
                              {!q.isCorrect && q.correctAnswer ? ` → ${q.correctAnswer}` : ""}
                            </span>
                          </div>
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

      {/* Topic mastery */}
      {topicStats.length > 0 && (
        <div className="card-edit p-5">
          <div className="eyebrow mb-4">Сэдвийн эзэмшилт</div>
          <TopicBreakdownChart stats={topicStats} />
        </div>
      )}

      {/* Weak topics → the course material that repairs them. This link-out is
          the whole point of the topic courses: test result → labeled topic →
          exact units to study. Severity decides WHERE: beginner → the course
          from its start; developing → the exact units; strong → problem bank
          and unit tests; near-mastery → just take more mock tests. */}
      {progress.weakTopics.length > 0 && (
        <div
          className="card-edit p-5"
          style={{
            background: "color-mix(in oklch, var(--warn) 6%, transparent)",
            borderColor: "color-mix(in oklch, var(--warn) 25%, transparent)",
          }}
        >
          <div className="flex items-start gap-3">
            <Target className="w-5 h-5 shrink-0 mt-0.5" style={{ color: "var(--warn)" }} />
            <div className="flex-1">
              <div className="eyebrow mb-1" style={{ color: "var(--warn)" }}>
                Анхаарах сэдвүүд
              </div>
              <p className="text-[13px]" style={{ color: "var(--fg-1)" }}>
                {progress.weakTopics.map((t) => TOPIC_LABELS[t] || t).join(" · ")}
              </p>
              <div className="mt-3 space-y-2">
                {progress.weakTopics.slice(0, 3).map((t) => {
                  const target = getStudyTarget(t);
                  if (!target) return null;
                  const stat = topicStats.find((s) => s.topic === t);
                  const sev = stat ? eshSeverity(stat.accuracy, stat.total) : null;
                  return (
                    <div key={t} className="text-[12px]" style={{ color: "var(--fg-2)" }}>
                      <span style={{ color: "var(--fg-1)" }}>{TOPIC_LABELS[t] || t}</span>
                      {sev && (
                        <span
                          className="mono ml-1.5 rounded-full px-1.5 py-0.5 text-[10px]"
                          style={{ border: "1px solid var(--line)", color: BAND_COLOR[sev] }}
                        >
                          {BAND_LABELS[sev].mn}
                          {stat && <span className="tabular"> · {stat.accuracy}%</span>}
                        </span>
                      )}
                      {": "}
                      {sev === "beginner" ? (
                        <>
                          Суурийг нь курсээс эхлээрэй —{" "}
                          <Link
                            href={target.primary.href}
                            className="underline underline-offset-2"
                            style={{ color: "var(--accent)" }}
                          >
                            {target.primary.label}
                          </Link>
                        </>
                      ) : sev === "strong" ? (
                        <>
                          Бага зэрэг дутуу байна — Бодлогын сангийн Level 2–3 болон нэгжийн тестээр батжуулаарай:{" "}
                          <Link href="/math/problem-bank" className="underline underline-offset-2" style={{ color: "var(--accent)" }}>
                            Бодлогын сан
                          </Link>
                        </>
                      ) : sev === "mastery" ? (
                        <>
                          Бараг эзэмшсэн — дахиад нэг ЭШ тест бодоорой:{" "}
                          <Link
                            href="/practice/esh/test?type=previous"
                            className="underline underline-offset-2"
                            style={{ color: "var(--accent)" }}
                          >
                            Тест сонгох
                          </Link>
                        </>
                      ) : (
                        <>
                          <Link
                            href={target.primary.href}
                            className="underline underline-offset-2"
                            style={{ color: "var(--accent)" }}
                          >
                            {target.primary.label}
                          </Link>
                          {target.links.slice(0, 2).map((l) => (
                            <span key={l.href}>
                              {" · "}
                              <Link href={l.href} className="underline underline-offset-2" style={{ color: "var(--accent)" }}>
                                {l.label}
                              </Link>
                            </span>
                          ))}
                        </>
                      )}
                    </div>
                  );
                })}
              </div>
              <Link
                href="/practice/esh/practice"
                className="mono text-[11px] uppercase mt-3 inline-flex items-center gap-1"
                style={{ color: "var(--accent)", letterSpacing: "0.06em" }}
              >
                <Target className="w-3 h-3" />
                Дадлага хийх
              </Link>
            </div>
          </div>
        </div>
      )}

      {/* Weak skills — per-skill_tag accuracy across all attempts, each routed
          to the exact lessons that repair it. */}
      {weakSkills.length > 0 && (
        <div className="card-edit p-5">
          <div className="eyebrow mb-3">Сул чадварууд — юуг үзэх вэ</div>
          <div className="space-y-3">
            {weakSkills.map((s) => {
              const target = getSkillStudyTarget(s.tag);
              return (
                <div key={s.tag}>
                  <div className="flex items-baseline gap-2">
                    <span className="text-[13px]" style={{ color: "var(--fg)" }}>
                      {s.label}
                    </span>
                    <span className="mono text-[11px] tabular" style={{ color: "var(--warn)" }}>
                      {s.correct}/{s.total}
                    </span>
                  </div>
                  {target && (
                    <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
                      {[target.primary, ...target.links.slice(0, 1)].map((l, i) => (
                        <span key={l.href}>
                          {i > 0 && " · "}
                          <Link href={l.href} className="underline underline-offset-2" style={{ color: "var(--accent)" }}>
                            {l.label}
                          </Link>
                        </span>
                      ))}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Flagged */}
      {progress.flaggedCount > 0 && (
        <div className="card-edit p-5">
          <div className="flex items-start gap-3">
            <Flag className="w-5 h-5 shrink-0 mt-0.5" style={{ color: "var(--warn)" }} />
            <div className="flex-1">
              <div className="eyebrow mb-1">Тэмдэглэсэн · {progress.flaggedCount}</div>
              <p className="text-[13px]" style={{ color: "var(--fg-2)" }}>
                Эдгээр бодлогуудыг давтан шийдвэрлэхийг зөвлөж байна.
              </p>
              <Link
                href="/practice/esh/practice"
                className="mono text-[11px] uppercase mt-3 inline-flex items-center gap-1"
                style={{ color: "var(--accent)", letterSpacing: "0.06em" }}
              >
                <Flag className="w-3 h-3" />
                Тэмдэглэсэн бодлого бодох
              </Link>
            </div>
          </div>
        </div>
      )}

      {/* Recommendation */}
      <div className="card-edit p-5" style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}>
        <div className="eyebrow mb-2" style={{ color: "var(--accent)" }}>
          Зөвлөгөө
        </div>
        <p className="serif" style={{ fontSize: 16, lineHeight: 1.5, color: "var(--fg)" }}>
          {progress.practiceRecommendation}
        </p>
        {progress.suggestedNextTest && (
          <Link
            href={`/practice/esh/test?type=${getTestInfo(progress.suggestedNextTest)?.isPremium ? "premium" : "previous"}`}
            className="mono text-[11px] uppercase mt-3 inline-flex items-center gap-1"
            style={{ color: "var(--accent)", letterSpacing: "0.06em" }}
          >
            Тест {progress.suggestedNextTest} бодох →
          </Link>
        )}
      </div>
    </div>
  );
}
