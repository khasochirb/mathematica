"use client";

import { useState, useEffect, useMemo, useCallback } from "react";
import Link from "next/link";
import {
  ArrowLeft,
  Target,
  BookOpen,
  Flag,
  Shuffle,
  Play,
  CheckCircle2,
  XCircle,
  RotateCcw,
  ChevronRight,
} from "lucide-react";
import QuestionCard from "@/components/esh/QuestionCard";
import TopicBreakdownChart from "@/components/esh/TopicBreakdownChart";
import usePerformance from "@/lib/use-performance";
import useFlaggedQuestions from "@/lib/use-flagged-questions";
import {
  getAllQuestions,
  getQuestionsByTopic,
  getQuestionBySource,
  getSimilarQuestions,
  TOPICS,
  TOPIC_LABELS,
} from "@/lib/esh-questions";
import type { Question } from "@/lib/esh-questions";

type PracticeMode = "weak" | "topic" | "flagged" | "mixed";
type PracticeState = "setup" | "active" | "results";

function shuffleArray<T>(arr: T[]): T[] {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

export default function PracticePage() {
  const [mounted, setMounted] = useState(false);
  const [state, setState] = useState<PracticeState>("setup");
  const [mode, setMode] = useState<PracticeMode>("weak");
  const [topicFilter, setTopicFilter] = useState("");
  const [practiceQuestions, setPracticeQuestions] = useState<Question[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [results, setResults] = useState<
    Record<string, { selected: string; correct: string; isCorrect: boolean }>
  >({});

  const perf = usePerformance();
  const flaggedHook = useFlaggedQuestions();

  useEffect(() => setMounted(true), []);

  const weakTopics = perf.getWeakTopics();
  const allQuestions = useMemo(() => getAllQuestions(), []);

  const generateQuestions = useCallback(
    (selectedMode: PracticeMode, selectedTopic: string): Question[] => {
      let pool: Question[] = [];

      switch (selectedMode) {
        case "weak":
          pool = allQuestions.filter((q) => weakTopics.includes(q.topic));
          break;
        case "topic":
          pool = selectedTopic
            ? getQuestionsByTopic(selectedTopic)
            : allQuestions;
          break;
        case "flagged":
          pool = flaggedHook.flagged
            .filter((f) => !f.resolved)
            .map((f) => getQuestionBySource(f.questionSource))
            .filter(Boolean) as Question[];
          break;
        case "mixed":
          pool = allQuestions;
          break;
      }

      // Filter out already correctly answered (for weak/mixed modes)
      if (selectedMode === "weak" || selectedMode === "mixed") {
        const correctSources = new Set(
          perf.attempts
            .filter((a) => a.isCorrect)
            .map((a) => a.questionSource),
        );
        const unanswered = pool.filter((q) => !correctSources.has(q.source));
        if (unanswered.length >= 10) pool = unanswered;
      }

      return shuffleArray(pool).slice(0, 10);
    },
    [allQuestions, weakTopics, flaggedHook.flagged, perf.attempts],
  );

  const handleStart = () => {
    const questions = generateQuestions(mode, topicFilter);
    if (questions.length === 0) return;
    setPracticeQuestions(questions);
    setCurrentIndex(0);
    setResults({});
    setState("active");
  };

  const handleAnswer = (
    questionSource: string,
    topic: string,
    subtopic: string,
    difficulty: number,
    selected: string,
    correct: string,
    isCorrect: boolean,
  ) => {
    perf.recordAttempt({
      questionSource,
      topic,
      subtopic,
      difficulty,
      selectedAnswer: selected,
      correctAnswer: correct,
      isCorrect,
    });
    setResults((prev) => ({
      ...prev,
      [questionSource]: { selected, correct, isCorrect },
    }));

    // Auto-advance after a short delay
    setTimeout(() => {
      if (currentIndex < practiceQuestions.length - 1) {
        setCurrentIndex((i) => i + 1);
      } else {
        setState("results");
      }
    }, 1500);
  };

  const correctCount = Object.values(results).filter((r) => r.isCorrect).length;
  const totalAnswered = Object.keys(results).length;

  // Compute topic stats for results
  const practiceTopicStats = useMemo(() => {
    const map: Record<string, { correct: number; total: number }> = {};
    for (const q of practiceQuestions) {
      const r = results[q.source];
      if (!map[q.topic]) map[q.topic] = { correct: 0, total: 0 };
      map[q.topic].total++;
      if (r?.isCorrect) map[q.topic].correct++;
    }
    return Object.entries(map).map(([topic, { correct, total }]) => ({
      topic,
      correct,
      total,
      accuracy: total > 0 ? Math.round((correct / total) * 100) : 0,
    }));
  }, [practiceQuestions, results]);

  const modes: {
    key: PracticeMode;
    label: string;
    desc: string;
    icon: typeof Target;
    color: string;
  }[] = [
    {
      key: "weak",
      label: "Сул сэдвээр",
      desc: "Сул сэдвүүдийн бодлогууд",
      icon: Target,
      color: "text-orange-400 bg-orange-500/15",
    },
    {
      key: "topic",
      label: "Сэдвээр",
      desc: "Нэг сэдвийн бодлогууд",
      icon: BookOpen,
      color: "text-primary-400 bg-primary-500/15",
    },
    {
      key: "flagged",
      label: "Тэмдэглэсэн",
      desc: `${flaggedHook.getUnresolvedCount()} бодлого`,
      icon: Flag,
      color: "text-orange-400 bg-orange-500/15",
    },
    {
      key: "mixed",
      label: "Холимог",
      desc: "Бүх сэдвээс санамсаргүй",
      icon: Shuffle,
      color: "text-cyan-400 bg-cyan-500/15",
    },
  ];

  if (!mounted) {
    return (
      <div className="min-h-screen bg-surface-900 pt-20 flex items-center justify-center">
        <div className="text-gray-500">Ачааллаж байна...</div>
      </div>
    );
  }

  // RESULTS STATE
  if (state === "results") {
    return (
      <div className="min-h-screen bg-surface-900 pt-20 relative">
        <div className="absolute inset-0 bg-grid opacity-30" />
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8 relative">
          <div className="text-center mb-8">
            <div
              className={`text-5xl font-bold font-display mb-2 ${
                correctCount / practiceQuestions.length >= 0.8
                  ? "text-emerald-400"
                  : correctCount / practiceQuestions.length >= 0.5
                    ? "text-yellow-400"
                    : "text-red-400"
              }`}
            >
              {correctCount}/{practiceQuestions.length}
            </div>
            <p className="text-gray-500">
              {Math.round((correctCount / practiceQuestions.length) * 100)}% зөв
            </p>
          </div>

          {/* Topic breakdown */}
          {practiceTopicStats.length > 0 && (
            <div className="card-glass p-5 mb-6">
              <h3 className="font-display text-sm font-bold text-white mb-3">
                Сэдвийн задаргаа
              </h3>
              <TopicBreakdownChart stats={practiceTopicStats} />
            </div>
          )}

          {/* Question summary */}
          <div className="card-glass p-5 mb-6">
            <h3 className="font-display text-sm font-bold text-white mb-3">
              Бодлогууд
            </h3>
            <div className="space-y-2">
              {practiceQuestions.map((q, i) => {
                const r = results[q.source];
                return (
                  <div
                    key={q.source}
                    className="flex items-center gap-3 px-3 py-2 rounded-lg bg-white/[0.03]"
                  >
                    <span className="text-xs font-bold text-gray-500 w-5">
                      {i + 1}
                    </span>
                    <span className="text-sm text-gray-400 flex-1 truncate">
                      {TOPIC_LABELS[q.topic] || q.topic}
                    </span>
                    {r?.isCorrect ? (
                      <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                    ) : r ? (
                      <XCircle className="w-4 h-4 text-red-400" />
                    ) : (
                      <span className="text-xs text-gray-600">—</span>
                    )}
                  </div>
                );
              })}
            </div>
          </div>

          {/* Actions */}
          <div className="flex flex-wrap gap-3">
            <button
              onClick={() => {
                handleStart();
              }}
              className="flex items-center gap-2 btn-primary text-sm px-5 py-2.5"
            >
              <RotateCcw className="w-4 h-4" />
              Дахин дадлага хийх
            </button>
            <button
              onClick={() => setState("setup")}
              className="flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-medium text-gray-400 bg-white/[0.05] border border-white/[0.08] hover:bg-white/[0.1] transition-colors"
            >
              Горим сонгох
            </button>
            <Link
              href="/practice/esh"
              className="flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-medium text-gray-400 bg-white/[0.05] border border-white/[0.08] hover:bg-white/[0.1] transition-colors"
            >
              <ArrowLeft className="w-4 h-4" />
              Нүүр хуудас
            </Link>
          </div>
        </div>
      </div>
    );
  }

  // ACTIVE STATE
  if (state === "active") {
    const currentQ = practiceQuestions[currentIndex];
    const isLast = currentIndex === practiceQuestions.length - 1;
    const answered = currentQ.source in results;

    return (
      <div className="min-h-screen bg-surface-900 pt-20 relative">
        <div className="absolute inset-0 bg-grid opacity-30" />
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8 relative">
          {/* Progress */}
          <div className="flex items-center justify-between mb-4">
            <span className="text-sm text-gray-500">
              {currentIndex + 1} / {practiceQuestions.length}
            </span>
            <span className="text-sm text-gray-500">
              {correctCount} зөв
            </span>
          </div>
          <div className="h-1 bg-white/[0.06] rounded-full mb-6 overflow-hidden">
            <div
              className="h-full bg-primary-500/60 transition-all duration-300 rounded-full"
              style={{
                width: `${((currentIndex + (answered ? 1 : 0)) / practiceQuestions.length) * 100}%`,
              }}
            />
          </div>

          <QuestionCard
            key={currentQ.source}
            mode="instant"
            question={currentQ}
            onAnswer={handleAnswer}
          />

          {/* Navigation for skipping */}
          <div className="flex justify-between mt-4">
            <button
              onClick={() => {
                if (currentIndex > 0) setCurrentIndex((i) => i - 1);
              }}
              disabled={currentIndex === 0}
              className={`text-sm px-4 py-2 rounded-xl transition-all ${
                currentIndex === 0
                  ? "text-gray-600 cursor-not-allowed"
                  : "text-gray-400 hover:text-white"
              }`}
            >
              Өмнөх
            </button>
            {answered && !isLast && (
              <button
                onClick={() => setCurrentIndex((i) => i + 1)}
                className="text-sm text-primary-400 hover:text-primary-300 flex items-center gap-1"
              >
                Дараах <ChevronRight className="w-4 h-4" />
              </button>
            )}
            {answered && isLast && (
              <button
                onClick={() => setState("results")}
                className="btn-primary text-sm px-5 py-2"
              >
                Үр дүн харах
              </button>
            )}
          </div>
        </div>
      </div>
    );
  }

  // SETUP STATE
  return (
    <div className="min-h-screen bg-surface-900 pt-20 relative">
      <div className="absolute inset-0 bg-grid opacity-30" />
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8 relative">
        {/* Header */}
        <div className="flex items-center gap-3 mb-8">
          <Link
            href="/practice/esh"
            className="p-2 rounded-xl bg-white/[0.05] border border-white/[0.08] text-gray-400 hover:text-white hover:bg-white/[0.1] transition-colors"
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div>
            <h1 className="font-display text-xl font-bold text-white">
              Дадлага бодлого
            </h1>
            <p className="text-sm text-gray-500">
              Горим сонгоод 10 бодлого бод
            </p>
          </div>
        </div>

        {/* Mode selection */}
        <div className="space-y-3 mb-6">
          {modes.map((m) => {
            const Icon = m.icon;
            const isSelected = mode === m.key;
            const isDisabled =
              (m.key === "weak" && weakTopics.length === 0) ||
              (m.key === "flagged" && flaggedHook.getUnresolvedCount() === 0);

            return (
              <button
                key={m.key}
                onClick={() => !isDisabled && setMode(m.key)}
                disabled={isDisabled}
                className={`w-full flex items-center gap-4 p-4 rounded-xl border transition-all text-left ${
                  isDisabled
                    ? "opacity-40 cursor-not-allowed border-white/[0.05]"
                    : isSelected
                      ? "bg-white/[0.06] border-primary-400/30"
                      : "bg-white/[0.02] border-white/[0.08] hover:bg-white/[0.05]"
                }`}
              >
                <div
                  className={`w-10 h-10 rounded-xl flex items-center justify-center ${m.color}`}
                >
                  <Icon className="w-5 h-5" />
                </div>
                <div className="flex-1">
                  <p className="text-sm font-medium text-white">{m.label}</p>
                  <p className="text-xs text-gray-500">{m.desc}</p>
                </div>
                {isSelected && (
                  <div className="w-5 h-5 rounded-full bg-primary-500 flex items-center justify-center">
                    <CheckCircle2 className="w-3.5 h-3.5 text-white" />
                  </div>
                )}
              </button>
            );
          })}
        </div>

        {/* Topic filter (for "topic" mode) */}
        {mode === "topic" && (
          <div className="mb-6">
            <p className="text-sm text-gray-400 mb-3">Сэдэв сонгох:</p>
            <div className="flex flex-wrap gap-2">
              {TOPICS.map((t) => (
                <button
                  key={t.value}
                  onClick={() =>
                    setTopicFilter(topicFilter === t.value ? "" : t.value)
                  }
                  className={`px-3 py-1.5 rounded-full text-xs font-medium transition-all border ${
                    topicFilter === t.value
                      ? "bg-primary-500/20 text-primary-300 border-primary-400/30"
                      : "bg-white/[0.04] text-gray-500 border-white/[0.08] hover:bg-white/[0.08] hover:text-gray-300"
                  }`}
                >
                  {t.label}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Weak topics info */}
        {mode === "weak" && weakTopics.length > 0 && (
          <div className="card-glass p-4 mb-6 border-orange-400/10">
            <p className="text-sm text-gray-400">
              <span className="text-orange-400 font-medium">Сул сэдвүүд: </span>
              {weakTopics.map((t) => TOPIC_LABELS[t] || t).join(", ")}
            </p>
          </div>
        )}

        {/* Start button */}
        <button
          onClick={handleStart}
          className="w-full btn-primary text-sm py-3 flex items-center justify-center gap-2"
        >
          <Play className="w-4 h-4" />
          Эхлэх
        </button>
      </div>
    </div>
  );
}
