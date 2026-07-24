"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import {
  Check,
  ChevronDown,
  Flag,
  Target,
  Trash2,
  X,
} from "lucide-react";
import BackButton from "@/components/BackButton";
import TopicBreakdownChart from "@/components/esh/TopicBreakdownChart";
import useESHProgress from "@/lib/use-esh-progress";
import usePerformance from "@/lib/use-performance";
import useTestSession from "@/lib/use-test-session";
import useFlaggedQuestions from "@/lib/use-flagged-questions";
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

export default function ProgressPage() {
  const [mounted, setMounted] = useState(false);
  const [showClearConfirm, setShowClearConfirm] = useState(false);
  const [openEntry, setOpenEntry] = useState<Record<string, boolean>>({});
  const progress = useESHProgress();
  const perf = usePerformance();
  const testSession = useTestSession();
  const flaggedHook = useFlaggedQuestions();

  useEffect(() => setMounted(true), []);

  const handleClearAll = () => {
    perf.clearAll();
    testSession.clearAll();
    flaggedHook.clearAll();
    setShowClearConfirm(false);
  };

  if (!mounted) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <p className="mono text-[12px]" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>АЧААЛЛАЖ БАЙНА...</p>
      </div>
    );
  }

  const topicStats = progress.topicMastery.map((t) => ({
    topic: t.topic,
    correct: Math.round((t.accuracy * t.totalAttempts) / 100),
    total: t.totalAttempts,
    accuracy: t.accuracy,
  }));

  const overviewStats = [
    { value: `${progress.averageAccuracy}%`, label: "Дундаж оноо" },
    { value: String(progress.totalTestsTaken), label: "Тест бодсон" },
    { value: String(progress.totalQuestionsAnswered), label: "Бодлого бодсон" },
    { value: String(progress.weeklyActivity.thisWeek), label: "Энэ долоо хоногт" },
  ];

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-12">
        {/* Header */}
        <div className="flex items-center gap-3 mb-6">
          <BackButton fallback="/practice/esh" className="gm-press p-2 rounded-md" label="Буцах" />
          <div className="eyebrow flex-1">ЭЕШ · Прогресс</div>
          <button
            onClick={() => setShowClearConfirm(true)}
            className="flex items-center gap-1 mono text-[10px] uppercase transition-colors"
            style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}
          >
            <Trash2 className="w-3 h-3" /> Арилгах
          </button>
        </div>

        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(40px, 6vw, 64px)", letterSpacing: "-0.04em", lineHeight: 0.98, color: "var(--fg)" }}>
          Таны <em className="serif-italic" style={{ color: "var(--accent)" }}>прогресс</em>.
        </h1>

        {progress.totalTestsTaken === 0 && progress.totalQuestionsAnswered === 0 ? (
          <div className="card-edit p-12 text-center mt-8">
            <div className="eyebrow mb-3">Хоосон</div>
            <h2 className="serif" style={{ fontWeight: 400, fontSize: 26, letterSpacing: "-0.02em", color: "var(--fg)" }}>
              Мэдээлэл <em className="serif-italic" style={{ color: "var(--accent)" }}>байхгүй</em>.
            </h2>
            <p className="text-[14px] mt-3 mb-6" style={{ color: "var(--fg-2)" }}>
              Тест бодож эсвэл дадлага хийж эхлэхэд таны прогресс энд харагдана.
            </p>
            <div className="flex gap-2 justify-center">
              <Link href="/practice/esh/test?type=previous" className="btn btn-primary">
                Тест бодох
              </Link>
              <Link href="/practice/esh/practice" className="btn btn-line">
                Дадлага хийх
              </Link>
            </div>
          </div>
        ) : (
          <div className="space-y-6 mt-8">
            {perf.isOffline && (
              <div
                className="mono px-4 py-2 rounded-md text-[11px]"
                style={{
                  background: "color-mix(in oklch, var(--warn) 10%, transparent)",
                  border: "1px solid color-mix(in oklch, var(--warn) 25%, transparent)",
                  color: "var(--warn)",
                  letterSpacing: "0.04em",
                }}
              >
                Кэшнээс харуулж байна — холболт сэргээж байна…
              </div>
            )}
            {/* Overview */}
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
              {overviewStats.map((s, i) => (
                <div key={s.label} className="card-edit p-5">
                  <div className="mono text-[10px] mb-1" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                    {String(i + 1).padStart(2, "0")}
                  </div>
                  <p className="serif tabular" style={{ fontSize: 26, color: "var(--accent)", letterSpacing: "-0.02em" }}>
                    {s.value}
                  </p>
                  <p className="mono text-[10px] mt-1 uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                    {s.label}
                  </p>
                </div>
              ))}
            </div>

            {/* Score history */}
            {progress.scoreHistory.length > 0 && (
              <div className="card-edit p-5">
                <div className="eyebrow mb-4">Шалгалтын оноо</div>
                <div className="space-y-2">
                  {progress.scoreHistory.map((entry, i) => {
                    const color = entry.accuracy >= 80 ? "var(--accent)" : entry.accuracy >= 50 ? "var(--warn)" : "var(--danger)";
                    const entryKey = `${entry.testKey}@${entry.date}`;
                    const isOpen = !!openEntry[entryKey];
                    const hasDetail = !!entry.run && entry.run.questions.length > 0;
                    return (
                      <div key={i} className="rounded-md overflow-hidden" style={{ background: "var(--bg-2)" }}>
                        <button
                          className="w-full flex items-center gap-3 px-3 py-2.5 text-left"
                          onClick={() =>
                            hasDetail && setOpenEntry((o) => ({ ...o, [entryKey]: !o[entryKey] }))
                          }
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
                              <div className="h-full rounded-full transition-all" style={{ width: `${entry.accuracy}%`, background: color }} />
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
                                  style={{ background: q.isCorrect ? "transparent" : "color-mix(in oklch, var(--danger) 7%, transparent)" }}
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

            {/* Weak topics */}
            {progress.weakTopics.length > 0 && (
              <div
                className="card-edit p-5"
                style={{ background: "color-mix(in oklch, var(--warn) 6%, transparent)", borderColor: "color-mix(in oklch, var(--warn) 25%, transparent)" }}
              >
                <div className="flex items-start gap-3">
                  <Target className="w-5 h-5 shrink-0 mt-0.5" style={{ color: "var(--warn)" }} />
                  <div className="flex-1">
                    <div className="eyebrow mb-1" style={{ color: "var(--warn)" }}>Анхаарах сэдвүүд</div>
                    <p className="text-[13px]" style={{ color: "var(--fg-1)" }}>
                      {progress.weakTopics.map((t) => TOPIC_LABELS[t] || t).join(" · ")}
                    </p>
                    {/* Weak topic → the course material that repairs it.
                        This link-out is the whole point of the topic courses:
                        test result → labeled topic → exact units to study. */}
                    {/* Severity-graded routing: how weak decides WHERE to go.
                        Beginner → the course from its start; developing → the
                        exact units; strong → problem bank + unit tests;
                        near-mastery → just take more mock tests. */}
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
                                <Link href={target.primary.href} className="underline underline-offset-2" style={{ color: "var(--accent)" }}>
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
                                Бараг эзэмшсэн — дахиад нэг ЭЕШ тест бодоорой:{" "}
                                <Link href="/practice/esh/test?type=previous" className="underline underline-offset-2" style={{ color: "var(--accent)" }}>
                                  Тест сонгох
                                </Link>
                              </>
                            ) : (
                              <>
                                <Link href={target.primary.href} className="underline underline-offset-2" style={{ color: "var(--accent)" }}>
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

            {/* Weak skills — per-skill_tag accuracy across all attempts,
                each routed to the exact lessons that repair it. */}
            {perf.getWeakSkills().length > 0 && (
              <div className="card-edit p-5">
                <div className="eyebrow mb-3">Сул чадварууд — юуг үзэх вэ</div>
                <div className="space-y-3">
                  {perf.getWeakSkills().map((s) => {
                    const target = getSkillStudyTarget(s.tag);
                    return (
                      <div key={s.tag}>
                        <div className="flex items-baseline gap-2">
                          <span className="text-[13px]" style={{ color: "var(--fg)" }}>{s.label}</span>
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
            <div
              className="card-edit p-5"
              style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
            >
              <div className="eyebrow mb-2" style={{ color: "var(--accent)" }}>Зөвлөгөө</div>
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
        )}
      </div>

      {/* Clear confirmation modal */}
      {showClearConfirm && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center px-4"
          style={{ background: "color-mix(in oklch, var(--bg) 70%, black 30% / 60%)", backdropFilter: "blur(8px)" }}
        >
          <div className="card-edit p-6 max-w-sm w-full" style={{ background: "var(--bg-1)" }}>
            <div className="eyebrow mb-2">Баталгаажуулах</div>
            <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
              Бүх мэдээлэл <em className="serif-italic" style={{ color: "var(--danger)" }}>арилгах</em> уу?
            </h3>
            <p className="text-[13px] mt-3 mb-6" style={{ color: "var(--fg-2)" }}>
              Шалгалтын түүх, дадлагын мэдээлэл, тэмдэглэсэн бодлогууд бүгд арилна. Энэ үйлдлийг буцаах боломжгүй.
            </p>
            <div className="flex gap-2">
              <button onClick={() => setShowClearConfirm(false)} className="btn btn-line flex-1">
                Болих
              </button>
              <button
                onClick={handleClearAll}
                className="btn flex-1"
                style={{
                  background: "color-mix(in oklch, var(--danger) 18%, transparent)",
                  border: "1px solid color-mix(in oklch, var(--danger) 35%, transparent)",
                  color: "var(--danger)",
                }}
              >
                Арилгах
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
