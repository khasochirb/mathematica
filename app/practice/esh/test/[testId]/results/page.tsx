"use client";

import { useState, useEffect, useMemo } from "react";
import { useParams, useSearchParams, useRouter } from "next/navigation";
import Link from "next/link";
import {
  ArrowLeft,
  Trophy,
  Clock,
  Target,
  Flag,
  ChevronDown,
  ChevronUp,
  RotateCcw,
  BookOpen,
  BarChart3,
  CheckCircle2,
  XCircle,
  Minus,
} from "lucide-react";
import QuestionCard from "@/components/esh/QuestionCard";
import TopicBreakdownChart from "@/components/esh/TopicBreakdownChart";
import useTestSession from "@/lib/use-test-session";
import { getTestQuestions, getTestInfo, TOPIC_LABELS } from "@/lib/esh-questions";
import type { Question } from "@/lib/esh-questions";

function formatDuration(ms: number): string {
  const totalSeconds = Math.floor(ms / 1000);
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  if (hours > 0) return `${hours} цаг ${minutes} мин`;
  return `${minutes} мин`;
}

type ViewFilter = "all" | "correct" | "incorrect" | "skipped" | "flagged";

export default function TestResultsPage() {
  const params = useParams();
  const searchParams = useSearchParams();
  const router = useRouter();
  const testKey = (params.testId as string).toUpperCase();
  const sessionId = searchParams.get("session") || "";

  const testSession = useTestSession();
  const [mounted, setMounted] = useState(false);
  const [expandedQuestions, setExpandedQuestions] = useState<Set<number>>(
    new Set(),
  );
  const [viewFilter, setViewFilter] = useState<ViewFilter>("all");

  useEffect(() => setMounted(true), []);

  const session = mounted ? testSession.getSession(sessionId) : undefined;
  const testInfo = getTestInfo(testKey);
  const questions: Question[] = useMemo(
    () => getTestQuestions(testKey),
    [testKey],
  );

  // Redirect if no valid completed session
  useEffect(() => {
    if (mounted && (!session || session.status !== "completed")) {
      router.replace("/practice/esh/test");
    }
  }, [mounted, session, router]);

  // Compute topic stats
  const topicStats = useMemo(() => {
    if (!session) return [];
    const map: Record<string, { correct: number; total: number }> = {};
    for (const q of questions) {
      if (!map[q.topic]) map[q.topic] = { correct: 0, total: 0 };
      map[q.topic].total++;
      const answer = session.answers[q.questionNumber];
      if (answer === q.answer) map[q.topic].correct++;
    }
    return Object.entries(map).map(([topic, { correct, total }]) => ({
      topic,
      correct,
      total,
      accuracy: total > 0 ? Math.round((correct / total) * 100) : 0,
    }));
  }, [session, questions]);

  const weakTopics = topicStats
    .filter((s) => s.accuracy < 50)
    .sort((a, b) => a.accuracy - b.accuracy);

  // Filtered questions
  const filteredQuestions = useMemo(() => {
    if (!session) return [];
    return questions.filter((q) => {
      const answer = session.answers[q.questionNumber];
      const isCorrect = answer === q.answer;
      const isSkipped = !answer;
      const isFlagged = session.flagged.includes(q.questionNumber);

      switch (viewFilter) {
        case "correct":
          return isCorrect;
        case "incorrect":
          return !isSkipped && !isCorrect;
        case "skipped":
          return isSkipped;
        case "flagged":
          return isFlagged;
        default:
          return true;
      }
    });
  }, [session, questions, viewFilter]);

  const toggleExpand = (qNum: number) => {
    setExpandedQuestions((prev) => {
      const next = new Set(prev);
      if (next.has(qNum)) next.delete(qNum);
      else next.add(qNum);
      return next;
    });
  };

  if (!mounted || !session || session.status !== "completed" || !session.score) {
    return (
      <div className="min-h-screen bg-surface-900 pt-20 flex items-center justify-center">
        <div className="text-gray-500">Ачааллаж байна...</div>
      </div>
    );
  }

  const score = session.score;
  const duration = session.completedAt
    ? session.completedAt - session.startedAt
    : 0;

  const filterButtons: { key: ViewFilter; label: string; count: number }[] = [
    { key: "all", label: "Бүгд", count: questions.length },
    { key: "correct", label: "Зөв", count: score.correct },
    { key: "incorrect", label: "Буруу", count: score.incorrect },
    { key: "skipped", label: "Хариулаагүй", count: score.skipped },
    {
      key: "flagged",
      label: "Тэмдэглэсэн",
      count: session.flagged.length,
    },
  ];

  return (
    <div className="min-h-screen bg-surface-900 pt-20 relative">
      <div className="absolute inset-0 bg-grid opacity-30" />
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8 relative">
        {/* Header */}
        <div className="flex items-center gap-3 mb-8">
          <Link
            href="/practice/esh/test"
            className="p-2 rounded-xl bg-white/[0.05] border border-white/[0.08] text-gray-400 hover:text-white hover:bg-white/[0.1] transition-colors"
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div>
            <h1 className="font-display text-xl font-bold text-white">
              {testInfo?.label || testKey} — Үр дүн
            </h1>
            <p className="text-sm text-gray-500">
              {new Date(session.completedAt!).toLocaleDateString("mn-MN", {
                year: "numeric",
                month: "long",
                day: "numeric",
              })}
            </p>
          </div>
        </div>

        {/* Score banner */}
        <div className="card-glass p-6 mb-6">
          <div className="flex flex-col sm:flex-row items-center gap-6">
            {/* Big score */}
            <div className="text-center">
              <div
                className={`text-5xl font-bold font-display ${
                  score.accuracy >= 80
                    ? "text-emerald-400"
                    : score.accuracy >= 50
                      ? "text-yellow-400"
                      : "text-red-400"
                }`}
              >
                {score.accuracy}%
              </div>
              <p className="text-sm text-gray-500 mt-1">
                {score.correct}/{score.total} зөв
              </p>
            </div>

            {/* Stats grid */}
            <div className="flex-1 grid grid-cols-2 sm:grid-cols-4 gap-3 w-full">
              <div className="text-center p-3 bg-emerald-500/10 border border-emerald-400/15 rounded-xl">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 mx-auto mb-1" />
                <p className="text-lg font-bold text-emerald-300">{score.correct}</p>
                <p className="text-[11px] text-gray-500">Зөв</p>
              </div>
              <div className="text-center p-3 bg-red-500/10 border border-red-400/15 rounded-xl">
                <XCircle className="w-4 h-4 text-red-400 mx-auto mb-1" />
                <p className="text-lg font-bold text-red-300">{score.incorrect}</p>
                <p className="text-[11px] text-gray-500">Буруу</p>
              </div>
              <div className="text-center p-3 bg-gray-500/10 border border-gray-400/15 rounded-xl">
                <Minus className="w-4 h-4 text-gray-400 mx-auto mb-1" />
                <p className="text-lg font-bold text-gray-300">{score.skipped}</p>
                <p className="text-[11px] text-gray-500">Хариулаагүй</p>
              </div>
              <div className="text-center p-3 bg-white/[0.04] border border-white/[0.08] rounded-xl">
                <Clock className="w-4 h-4 text-gray-400 mx-auto mb-1" />
                <p className="text-lg font-bold text-gray-300">
                  {formatDuration(duration)}
                </p>
                <p className="text-[11px] text-gray-500">Хугацаа</p>
              </div>
            </div>
          </div>
        </div>

        {/* Topic breakdown */}
        <div className="card-glass p-6 mb-6">
          <h2 className="font-display text-base font-bold text-white mb-4 flex items-center gap-2">
            <BarChart3 className="w-5 h-5 text-primary-400" />
            Сэдвийн задаргаа
          </h2>
          <TopicBreakdownChart stats={topicStats} />
        </div>

        {/* Weak topics recommendations */}
        {weakTopics.length > 0 && (
          <div className="card-glass p-5 mb-6 border-orange-400/15">
            <div className="flex items-start gap-3">
              <Target className="w-5 h-5 text-orange-400 shrink-0 mt-0.5" />
              <div>
                <h3 className="text-sm font-semibold text-orange-300 mb-1">
                  Анхаарах сэдвүүд
                </h3>
                <p className="text-sm text-gray-400">
                  {weakTopics
                    .map(
                      (s) =>
                        `${TOPIC_LABELS[s.topic] || s.topic} (${s.accuracy}%)`,
                    )
                    .join(", ")}
                </p>
                <Link
                  href="/practice/esh/practice"
                  className="inline-flex items-center gap-1.5 text-sm text-primary-400 hover:text-primary-300 font-medium mt-2 transition-colors"
                >
                  <BookOpen className="w-4 h-4" />
                  Эдгээр сэдвээр дадлага хийх
                </Link>
              </div>
            </div>
          </div>
        )}

        {/* Flagged questions summary */}
        {session.flagged.length > 0 && (
          <div className="card-glass p-5 mb-6 border-orange-400/10">
            <div className="flex items-start gap-3">
              <Flag className="w-5 h-5 text-orange-400 shrink-0 mt-0.5" />
              <div>
                <h3 className="text-sm font-semibold text-orange-300 mb-1">
                  Тэмдэглэсэн бодлогууд ({session.flagged.length})
                </h3>
                <p className="text-sm text-gray-400">
                  {(() => {
                    const flaggedTopics: Record<string, number> = {};
                    for (const qNum of session.flagged) {
                      const q = questions.find((x) => x.questionNumber === qNum);
                      if (q) {
                        flaggedTopics[q.topic] =
                          (flaggedTopics[q.topic] || 0) + 1;
                      }
                    }
                    const total = session.flagged.length;
                    return Object.entries(flaggedTopics)
                      .sort(([, a], [, b]) => b - a)
                      .map(
                        ([topic, count]) =>
                          `${TOPIC_LABELS[topic] || topic} ${Math.round((count / total) * 100)}%`,
                      )
                      .join(", ");
                  })()}
                </p>
              </div>
            </div>
          </div>
        )}

        {/* Action buttons */}
        <div className="flex flex-wrap gap-3 mb-8">
          <button
            onClick={() => {
              const id = testSession.startSession(testKey);
              router.push(
                `/practice/esh/test/${testKey.toLowerCase()}?session=${id}`,
              );
            }}
            className="flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-medium text-gray-400 bg-white/[0.05] border border-white/[0.08] hover:bg-white/[0.1] transition-colors"
          >
            <RotateCcw className="w-4 h-4" />
            Дахин бодох
          </button>
          <Link
            href="/practice/esh/practice"
            className="flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-medium text-gray-400 bg-white/[0.05] border border-white/[0.08] hover:bg-white/[0.1] transition-colors"
          >
            <Target className="w-4 h-4" />
            Сул сэдвээр дадлага хийх
          </Link>
          <Link
            href="/practice/esh"
            className="flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-medium text-gray-400 bg-white/[0.05] border border-white/[0.08] hover:bg-white/[0.1] transition-colors"
          >
            <ArrowLeft className="w-4 h-4" />
            Нүүр хуудас
          </Link>
        </div>

        {/* Question-by-question review */}
        <div className="card-glass p-6">
          <h2 className="font-display text-base font-bold text-white mb-4">
            Бодлогуудын задаргаа
          </h2>

          {/* Filter tabs */}
          <div className="flex flex-wrap gap-2 mb-4">
            {filterButtons.map((f) => (
              <button
                key={f.key}
                onClick={() => setViewFilter(f.key)}
                className={`px-3 py-1.5 rounded-full text-xs font-medium transition-all border ${
                  viewFilter === f.key
                    ? "bg-primary-500/20 text-primary-300 border-primary-400/30"
                    : "bg-white/[0.04] text-gray-500 border-white/[0.08] hover:bg-white/[0.08] hover:text-gray-300"
                }`}
              >
                {f.label} ({f.count})
              </button>
            ))}
          </div>

          {/* Question list */}
          <div className="space-y-2">
            {filteredQuestions.map((q) => {
              const answer = session.answers[q.questionNumber];
              const isCorrect = answer === q.answer;
              const isSkipped = !answer;
              const isFlagged = session.flagged.includes(q.questionNumber);
              const isExpanded = expandedQuestions.has(q.questionNumber);

              return (
                <div key={q.questionNumber}>
                  {/* Compact row */}
                  <button
                    onClick={() => toggleExpand(q.questionNumber)}
                    className="w-full flex items-center gap-3 px-4 py-3 rounded-xl bg-white/[0.03] border border-white/[0.06] hover:bg-white/[0.05] transition-all text-left"
                  >
                    <span className="w-7 h-7 rounded-full bg-white/[0.08] flex items-center justify-center text-xs font-bold text-gray-400 shrink-0">
                      {q.questionNumber}
                    </span>
                    <span className="flex-1 text-sm text-gray-400 truncate">
                      {TOPIC_LABELS[q.topic] || q.topic}
                      {q.subtopic && ` · ${q.subtopic}`}
                    </span>
                    {isFlagged && (
                      <Flag className="w-3.5 h-3.5 text-orange-400 shrink-0" />
                    )}
                    {isSkipped ? (
                      <span className="text-xs text-gray-500 font-medium px-2 py-0.5 rounded-full bg-gray-500/10">
                        —
                      </span>
                    ) : isCorrect ? (
                      <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                    ) : (
                      <XCircle className="w-4 h-4 text-red-400 shrink-0" />
                    )}
                    {isExpanded ? (
                      <ChevronUp className="w-4 h-4 text-gray-500" />
                    ) : (
                      <ChevronDown className="w-4 h-4 text-gray-500" />
                    )}
                  </button>

                  {/* Expanded: full question review */}
                  {isExpanded && (
                    <div className="mt-2 mb-2">
                      <QuestionCard
                        mode="review"
                        question={q}
                        selectedAnswer={answer || null}
                        isFlagged={isFlagged}
                      />
                    </div>
                  )}
                </div>
              );
            })}
          </div>

          {filteredQuestions.length === 0 && (
            <div className="text-center py-8 text-gray-500 text-sm">
              Энэ шүүлтүүрт бодлого олдсонгүй.
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
