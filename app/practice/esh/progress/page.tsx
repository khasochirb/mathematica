"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import {
  ArrowLeft,
  BarChart3,
  Trophy,
  Target,
  Zap,
  Flame,
  Flag,
  TrendingUp,
  TrendingDown,
  Trash2,
  FileText,
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
      <div className="min-h-screen bg-surface-900 pt-20 flex items-center justify-center">
        <div className="text-gray-500">Ачааллаж байна...</div>
      </div>
    );
  }

  const topicStats = progress.topicMastery.map((t) => ({
    topic: t.topic,
    correct: Math.round((t.accuracy * t.totalAttempts) / 100),
    total: t.totalAttempts,
    accuracy: t.accuracy,
  }));

  return (
    <div className="min-h-screen bg-surface-900 pt-20 relative">
      <div className="absolute inset-0 bg-grid opacity-30" />
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8 relative">
        {/* Header */}
        <div className="flex items-center gap-3 mb-8">
          <Link
            href="/practice/esh"
            className="p-2 rounded-xl bg-white/[0.05] border border-white/[0.08] text-gray-400 hover:text-white hover:bg-white/[0.1] transition-colors"
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="flex-1">
            <h1 className="font-display text-xl font-bold text-white">
              Прогресс
            </h1>
            <p className="text-sm text-gray-500">
              Таны сурсан бүхнийг хянах
            </p>
          </div>
          <button
            onClick={() => setShowClearConfirm(true)}
            className="flex items-center gap-1 text-xs text-gray-500 hover:text-red-400 transition-colors"
          >
            <Trash2 className="w-3.5 h-3.5" /> Арилгах
          </button>
        </div>

        {progress.totalTestsTaken === 0 && progress.totalQuestionsAnswered === 0 ? (
          <div className="card-glass p-12 text-center">
            <BarChart3 className="w-12 h-12 text-gray-600 mx-auto mb-4" />
            <h2 className="font-display text-lg font-bold text-white mb-2">
              Мэдээлэл байхгүй байна
            </h2>
            <p className="text-sm text-gray-500 mb-6">
              Тест бодож эсвэл дадлага хийж эхлэхэд таны прогресс энд харагдана.
            </p>
            <div className="flex gap-3 justify-center">
              <Link
                href="/practice/esh/test"
                className="btn-primary text-sm px-6 py-2.5"
              >
                Тест бодох
              </Link>
              <Link
                href="/practice/esh/practice"
                className="px-6 py-2.5 rounded-xl text-sm font-medium text-gray-400 bg-white/[0.05] border border-white/[0.08] hover:bg-white/[0.1] transition-colors"
              >
                Дадлага хийх
              </Link>
            </div>
          </div>
        ) : (
          <div className="space-y-6">
            {/* Overview stats */}
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
              <div className="card-glass p-4 text-center">
                <Trophy className="w-5 h-5 text-yellow-400 mx-auto mb-1.5" />
                <p className="text-2xl font-bold text-white">
                  {progress.averageAccuracy}%
                </p>
                <p className="text-[11px] text-gray-500">Дундаж оноо</p>
              </div>
              <div className="card-glass p-4 text-center">
                <FileText className="w-5 h-5 text-primary-400 mx-auto mb-1.5" />
                <p className="text-2xl font-bold text-white">
                  {progress.totalTestsTaken}
                </p>
                <p className="text-[11px] text-gray-500">Тест бодсон</p>
              </div>
              <div className="card-glass p-4 text-center">
                <Zap className="w-5 h-5 text-yellow-400 mx-auto mb-1.5" />
                <p className="text-2xl font-bold text-white">
                  {progress.totalQuestionsAnswered}
                </p>
                <p className="text-[11px] text-gray-500">Бодлого бодсон</p>
              </div>
              <div className="card-glass p-4 text-center">
                <Flame className="w-5 h-5 text-orange-400 mx-auto mb-1.5" />
                <p className="text-2xl font-bold text-white">
                  {progress.weeklyActivity.thisWeek}
                </p>
                <p className="text-[11px] text-gray-500">Энэ долоо хоногт</p>
              </div>
            </div>

            {/* Score trend */}
            {progress.scoreHistory.length > 0 && (
              <div className="card-glass p-6">
                <h2 className="font-display text-base font-bold text-white mb-4 flex items-center gap-2">
                  <TrendingUp className="w-5 h-5 text-primary-400" />
                  Шалгалтын оноо
                </h2>
                <div className="space-y-3">
                  {progress.scoreHistory.map((entry, i) => (
                    <div
                      key={i}
                      className="flex items-center gap-3 px-3 py-2.5 bg-white/[0.03] rounded-xl"
                    >
                      <span className="w-8 h-8 rounded-lg bg-primary-500/15 flex items-center justify-center text-xs font-bold text-primary-300">
                        {entry.testKey}
                      </span>
                      <div className="flex-1">
                        <div className="h-2 bg-white/[0.06] rounded-full overflow-hidden">
                          <div
                            className={`h-full rounded-full transition-all ${
                              entry.accuracy >= 80
                                ? "bg-emerald-500"
                                : entry.accuracy >= 50
                                  ? "bg-yellow-500"
                                  : "bg-red-500"
                            }`}
                            style={{ width: `${entry.accuracy}%` }}
                          />
                        </div>
                      </div>
                      <span
                        className={`text-sm font-bold w-12 text-right ${
                          entry.accuracy >= 80
                            ? "text-emerald-400"
                            : entry.accuracy >= 50
                              ? "text-yellow-400"
                              : "text-red-400"
                        }`}
                      >
                        {entry.accuracy}%
                      </span>
                      <span className="text-xs text-gray-600 w-20 text-right">
                        {new Date(entry.date).toLocaleDateString("mn-MN", {
                          month: "short",
                          day: "numeric",
                        })}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Topic mastery */}
            {topicStats.length > 0 && (
              <div className="card-glass p-6">
                <h2 className="font-display text-base font-bold text-white mb-4 flex items-center gap-2">
                  <BarChart3 className="w-5 h-5 text-primary-400" />
                  Сэдвийн эзэмшилт
                </h2>
                <TopicBreakdownChart stats={topicStats} />
              </div>
            )}

            {/* Weak topics */}
            {progress.weakTopics.length > 0 && (
              <div className="card-glass p-5 border-orange-400/10">
                <div className="flex items-start gap-3">
                  <Target className="w-5 h-5 text-orange-400 shrink-0 mt-0.5" />
                  <div>
                    <h3 className="text-sm font-semibold text-orange-300 mb-1">
                      Анхаарах сэдвүүд
                    </h3>
                    <p className="text-sm text-gray-400">
                      {progress.weakTopics
                        .map((t) => TOPIC_LABELS[t] || t)
                        .join(", ")}
                    </p>
                    <Link
                      href="/practice/esh/practice"
                      className="inline-flex items-center gap-1 text-sm text-primary-400 hover:text-primary-300 font-medium mt-2 transition-colors"
                    >
                      <Target className="w-3.5 h-3.5" />
                      Дадлага хийх
                    </Link>
                  </div>
                </div>
              </div>
            )}

            {/* Flagged questions */}
            {progress.flaggedCount > 0 && (
              <div className="card-glass p-5 border-orange-400/10">
                <div className="flex items-start gap-3">
                  <Flag className="w-5 h-5 text-orange-400 shrink-0 mt-0.5" />
                  <div>
                    <h3 className="text-sm font-semibold text-orange-300 mb-1">
                      Тэмдэглэсэн бодлогууд ({progress.flaggedCount})
                    </h3>
                    <p className="text-sm text-gray-400">
                      Эдгээр бодлогуудыг давтан шийдвэрлэхийг зөвлөж байна.
                    </p>
                    <Link
                      href="/practice/esh/practice"
                      className="inline-flex items-center gap-1 text-sm text-primary-400 hover:text-primary-300 font-medium mt-2 transition-colors"
                    >
                      <Flag className="w-3.5 h-3.5" />
                      Тэмдэглэсэн бодлого бодох
                    </Link>
                  </div>
                </div>
              </div>
            )}

            {/* Recommendation */}
            <div className="card-glass p-5 border-primary-400/10">
              <p className="text-sm text-gray-300">
                <span className="text-primary-400 font-medium">Зөвлөгөө: </span>
                {progress.practiceRecommendation}
              </p>
              {progress.suggestedNextTest && (
                <Link
                  href={`/practice/esh/test`}
                  className="inline-flex items-center gap-1 text-sm text-primary-400 hover:text-primary-300 font-medium mt-2 transition-colors"
                >
                  Тест {progress.suggestedNextTest} бодох
                </Link>
              )}
            </div>
          </div>
        )}
      </div>

      {/* Clear confirmation modal */}
      {showClearConfirm && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm px-4">
          <div className="card-glass p-6 max-w-sm w-full">
            <h3 className="font-display font-bold text-white mb-2">
              Бүх мэдээлэл арилгах уу?
            </h3>
            <p className="text-sm text-gray-400 mb-6">
              Шалгалтын түүх, дадлагын мэдээлэл, тэмдэглэсэн бодлогууд бүгд
              арилна. Энэ үйлдлийг буцаах боломжгүй.
            </p>
            <div className="flex gap-3">
              <button
                onClick={() => setShowClearConfirm(false)}
                className="flex-1 px-4 py-2.5 rounded-xl text-sm font-medium text-gray-400 bg-white/[0.05] border border-white/[0.08] hover:bg-white/[0.1] transition-colors"
              >
                Болих
              </button>
              <button
                onClick={handleClearAll}
                className="flex-1 px-4 py-2.5 rounded-xl text-sm font-medium text-white bg-red-500/20 border border-red-400/30 hover:bg-red-500/30 transition-colors"
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
