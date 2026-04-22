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
  getQuestionsForUser,
  getQuestionsByTopicForUser,
  getQuestionBySource,
  getTestInfo,
  TOPICS,
  TOPIC_LABELS,
} from "@/lib/esh-questions";
import type { Question } from "@/lib/esh-questions";
import { useAuth } from "@/lib/auth-context";
import { useUpgradeModal } from "@/lib/upgrade-modal-context";
import { Sparkles } from "lucide-react";

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
  const { isSubscribed } = useAuth();
  const upgrade = useUpgradeModal();

  useEffect(() => setMounted(true), []);

  const weakTopics = perf.getWeakTopics();
  const allQuestions = useMemo(
    () => getQuestionsForUser(isSubscribed),
    [isSubscribed],
  );

  const generateQuestions = useCallback(
    (selectedMode: PracticeMode, selectedTopic: string): Question[] => {
      let pool: Question[] = [];

      switch (selectedMode) {
        case "weak":
          pool = allQuestions.filter((q) => weakTopics.includes(q.topic));
          break;
        case "topic":
          pool = selectedTopic
            ? getQuestionsByTopicForUser(selectedTopic, isSubscribed)
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
    [allQuestions, isSubscribed, weakTopics, flaggedHook.flagged, perf.attempts, perf],
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
    selected: string,
    correct: string,
    isCorrect: boolean,
  ) => {
    perf.recordAttempt({
      questionSource,
      topic,
      subtopic,
      selectedAnswer: selected,
      correctAnswer: correct,
      isCorrect,
    });
    setResults((prev) => ({
      ...prev,
      [questionSource]: { selected, correct, isCorrect },
    }));

    setTimeout(() => {
      if (currentIndex < practiceQuestions.length - 1) {
        setCurrentIndex((i) => i + 1);
      } else {
        setState("results");
      }
    }, 1500);
  };

  const correctCount = Object.values(results).filter((r) => r.isCorrect).length;

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
  }[] = [
    { key: "weak", label: "Сул сэдвээр", desc: "Сул сэдвүүдийн бодлогууд", icon: Target },
    { key: "topic", label: "Сэдвээр", desc: "Нэг сэдвийн бодлогууд", icon: BookOpen },
    { key: "flagged", label: "Тэмдэглэсэн", desc: `${flaggedHook.getUnresolvedCount()} бодлого`, icon: Flag },
    { key: "mixed", label: "Холимог", desc: "Бүх сэдвээс санамсаргүй", icon: Shuffle },
  ];

  if (!mounted) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <p className="mono text-[12px]" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>
          АЧААЛЛАЖ БАЙНА...
        </p>
      </div>
    );
  }

  // RESULTS
  if (state === "results") {
    const pct = Math.round((correctCount / practiceQuestions.length) * 100);
    const pctColor = pct >= 80 ? "var(--accent)" : pct >= 50 ? "var(--warn)" : "var(--danger)";
    return (
      <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-12">
          <div className="text-center mb-10">
            <div className="eyebrow mb-3">Дадлага · Үр дүн</div>
            <div
              className="serif tabular"
              style={{ fontSize: "clamp(64px, 10vw, 110px)", color: pctColor, letterSpacing: "-0.04em", lineHeight: 1 }}
            >
              {correctCount}<span style={{ color: "var(--fg-3)" }}>/{practiceQuestions.length}</span>
            </div>
            <p className="mono text-[12px] mt-3 uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
              {pct}% зөв
            </p>
          </div>

          {practiceTopicStats.length > 0 && (
            <div className="card-edit p-5 mb-4">
              <div className="eyebrow mb-3">Сэдвийн задаргаа</div>
              <TopicBreakdownChart stats={practiceTopicStats} />
            </div>
          )}

          <div className="card-edit p-2 mb-6">
            <div className="px-4 py-3" style={{ borderBottom: "1px solid var(--line)" }}>
              <div className="eyebrow">Бодлогууд</div>
            </div>
            {practiceQuestions.map((q, i) => {
              const r = results[q.source];
              return (
                <div
                  key={q.source}
                  className="flex items-center gap-3 px-4 py-2.5"
                  style={{ borderBottom: i < practiceQuestions.length - 1 ? "1px solid var(--line)" : "none" }}
                >
                  <span className="mono tabular text-[11px] w-6" style={{ color: "var(--fg-3)" }}>
                    {String(i + 1).padStart(2, "0")}
                  </span>
                  <span className="text-[13px] flex-1 truncate" style={{ color: "var(--fg-2)" }}>
                    {TOPIC_LABELS[q.topic] || q.topic}
                  </span>
                  {r?.isCorrect ? (
                    <CheckCircle2 className="w-4 h-4" style={{ color: "var(--accent)" }} />
                  ) : r ? (
                    <XCircle className="w-4 h-4" style={{ color: "var(--danger)" }} />
                  ) : (
                    <span className="mono text-[11px]" style={{ color: "var(--fg-3)" }}>—</span>
                  )}
                </div>
              );
            })}
          </div>

          <div className="flex flex-wrap gap-2">
            <button onClick={handleStart} className="btn btn-primary">
              <RotateCcw className="mr-1 w-3.5 h-3.5" />
              Дахин дадлага
            </button>
            <button onClick={() => setState("setup")} className="btn btn-line">
              Горим сонгох
            </button>
            <Link href="/practice/esh" className="btn btn-ghost">
              <ArrowLeft className="mr-1 w-3.5 h-3.5" />
              Нүүр
            </Link>
          </div>
        </div>
      </div>
    );
  }

  // ACTIVE
  if (state === "active") {
    const currentQ = practiceQuestions[currentIndex];
    const isLast = currentIndex === practiceQuestions.length - 1;
    const answered = currentQ.source in results;
    const progressPct = ((currentIndex + (answered ? 1 : 0)) / practiceQuestions.length) * 100;

    return (
      <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-8 pb-12">
          <div className="flex items-center justify-between mb-3">
            <span className="mono text-[11px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>
              {String(currentIndex + 1).padStart(2, "0")} / {String(practiceQuestions.length).padStart(2, "0")}
            </span>
            <span className="mono text-[11px] uppercase" style={{ color: "var(--accent)", letterSpacing: "0.06em" }}>
              {correctCount} зөв
            </span>
          </div>
          <div className="h-[3px] rounded-full mb-6 overflow-hidden" style={{ background: "var(--bg-2)" }}>
            <div
              className="h-full transition-all duration-300 rounded-full"
              style={{ width: `${progressPct}%`, background: "var(--accent)" }}
            />
          </div>

          <QuestionCard
            key={currentQ.source}
            mode="instant"
            question={currentQ}
            onAnswer={handleAnswer}
            solutionsLocked={
              !isSubscribed &&
              !!getTestInfo(`${currentQ.testNumber}${currentQ.testVariant}`)
                ?.solutionsRequirePremium
            }
            // KEEP IN SYNC with solutionsRequirePremium flags in lib/esh-questions.ts.
            onSolutionUpgrade={() =>
              upgrade.open({
                source: "gated_full_solutions",
                title: "Алхам алхмаар бодолт",
                description:
                  "2024 ба 2025 оны бүх шалгалтын бодолт үнэгүй. Бусад жилийн бүрэн бодолт Premium эхлэхэд нээгдэнэ.",
              })
            }
          />

          <div className="flex justify-between mt-4">
            <button
              onClick={() => {
                if (currentIndex > 0) setCurrentIndex((i) => i - 1);
              }}
              disabled={currentIndex === 0}
              className="mono text-[11px] uppercase px-4 py-2 transition-colors disabled:opacity-30"
              style={{ color: "var(--fg-2)", letterSpacing: "0.06em" }}
            >
              ← Өмнөх
            </button>
            {answered && !isLast && (
              <button
                onClick={() => setCurrentIndex((i) => i + 1)}
                className="mono text-[11px] uppercase px-4 py-2 flex items-center gap-1"
                style={{ color: "var(--accent)", letterSpacing: "0.06em" }}
              >
                Дараах <ChevronRight className="w-3.5 h-3.5" />
              </button>
            )}
            {answered && isLast && (
              <button onClick={() => setState("results")} className="btn btn-primary">
                Үр дүн харах
              </button>
            )}
          </div>
        </div>
      </div>
    );
  }

  // SETUP
  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-12">
        {/* Header */}
        <div className="flex items-center gap-3 mb-6">
          <Link
            href="/practice/esh"
            className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">ЭЕШ · Дадлага</div>
        </div>

        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(40px, 6vw, 64px)", letterSpacing: "-0.04em", lineHeight: 0.98, color: "var(--fg)" }}>
          10 бодлогын <em className="serif-italic" style={{ color: "var(--accent)" }}>дадлага</em>.
        </h1>
        <p className="serif mt-4 max-w-2xl" style={{ fontSize: 17, lineHeight: 1.55, color: "var(--fg-1)" }}>
          Горим сонгоод эхлээрэй.
        </p>

        {/* Mode selection */}
        <div className="space-y-2 mt-8 mb-6">
          {modes.map((m, i) => {
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
                className="card-edit w-full flex items-center gap-4 p-4 text-left transition-all"
                style={
                  isDisabled
                    ? { opacity: 0.4, cursor: "not-allowed" }
                    : isSelected
                    ? { background: "var(--accent-wash)", borderColor: "var(--accent-line)" }
                    : {}
                }
              >
                <span
                  className="mono tabular text-[10px] flex-shrink-0"
                  style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}
                >
                  {String(i + 1).padStart(2, "0")}
                </span>
                <div
                  className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0"
                  style={{
                    background: isSelected ? "var(--bg-1)" : "var(--bg-2)",
                    border: `1px solid ${isSelected ? "var(--accent-line)" : "var(--line)"}`,
                    color: isSelected ? "var(--accent)" : "var(--fg-2)",
                  }}
                >
                  <Icon className="w-4 h-4" />
                </div>
                <div className="flex-1">
                  <p className="serif" style={{ fontWeight: 400, fontSize: 16, color: "var(--fg)" }}>{m.label}</p>
                  <p className="text-[12px]" style={{ color: "var(--fg-3)" }}>{m.desc}</p>
                </div>
                {isSelected && (
                  <CheckCircle2 className="w-4 h-4 flex-shrink-0" style={{ color: "var(--accent)" }} />
                )}
              </button>
            );
          })}
        </div>

        {/* Topic filter */}
        {mode === "topic" && (
          <div className="mb-6">
            <div className="eyebrow mb-3">Сэдэв сонгох</div>
            <div className="flex flex-wrap gap-1.5">
              {TOPICS.map((t) => {
                const isActive = topicFilter === t.value;
                return (
                  <button
                    key={t.value}
                    onClick={() => setTopicFilter(isActive ? "" : t.value)}
                    className="badge-edit transition-all"
                    style={
                      isActive
                        ? { background: "var(--accent-wash)", borderColor: "var(--accent-line)", color: "var(--accent)" }
                        : { background: "var(--bg-2)" }
                    }
                  >
                    {t.label}
                  </button>
                );
              })}
            </div>
          </div>
        )}

        {/* Weak topics info */}
        {mode === "weak" && weakTopics.length > 0 && (
          <div
            className="card-edit p-4 mb-6"
            style={{ background: "color-mix(in oklch, var(--warn) 6%, transparent)", borderColor: "color-mix(in oklch, var(--warn) 25%, transparent)" }}
          >
            <div className="eyebrow mb-2" style={{ color: "var(--warn)" }}>Сул сэдвүүд</div>
            <p className="text-[13px]" style={{ color: "var(--fg-1)" }}>
              {weakTopics.map((t) => TOPIC_LABELS[t] || t).join(" · ")}
            </p>
          </div>
        )}

        {!isSubscribed && (
          <button
            type="button"
            onClick={() =>
              upgrade.open({
                source: "gated_study_pool",
                title: "Илүү олон бодлого — Premium",
                description:
                  "Premium багц нь 14 нэмэлт дадлага тестийн 500+ бодлогыг сэдвээр дадлага хийх санд нэмдэг.",
              })
            }
            className="card-edit w-full flex items-center gap-3 p-4 mb-4 text-left"
            style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
          >
            <Sparkles className="w-4 h-4 flex-shrink-0" style={{ color: "var(--accent)" }} />
            <div className="flex-1">
              <p className="text-[13px]" style={{ color: "var(--fg)" }}>
                <strong>Premium</strong> — 14 нэмэлт тест, 500+ бодлогыг сандаа нэм
              </p>
              <p className="mono text-[11px] mt-0.5" style={{ color: "var(--fg-2)", letterSpacing: "0.04em" }}>
                Мэдэгдэл авах
              </p>
            </div>
          </button>
        )}

        <button onClick={handleStart} className="btn btn-primary w-full">
          <Play className="mr-1 w-3.5 h-3.5" />
          Эхлэх
        </button>
      </div>
    </div>
  );
}
