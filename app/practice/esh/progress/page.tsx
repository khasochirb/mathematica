"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import {
  ArrowLeft,
  Flag,
  Target,
  Trash2,
} from "lucide-react";
import TopicBreakdownChart from "@/components/esh/TopicBreakdownChart";
import useESHProgress from "@/lib/use-esh-progress";
import usePerformance from "@/lib/use-performance";
import useTestSession from "@/lib/use-test-session";
import useFlaggedQuestions from "@/lib/use-flagged-questions";
import { TOPIC_LABELS } from "@/lib/esh-questions";

export default function ProgressPage() {
  const [mounted, setMounted] = useState(false);
  const [showClearConfirm, setShowClearConfirm] = useState(false);
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
          <Link
            href="/practice/esh"
            className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
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
              <Link href="/practice/esh/test" className="btn btn-primary">
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
                    return (
                      <div
                        key={i}
                        className="flex items-center gap-3 px-3 py-2.5 rounded-md"
                        style={{ background: "var(--bg-2)" }}
                      >
                        <span
                          className="mono tabular w-9 h-7 rounded flex items-center justify-center text-[11px]"
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
                  href="/practice/esh/test"
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
