"use client";

import { useState, useEffect, useMemo } from "react";
import { useParams, useSearchParams, useRouter } from "next/navigation";
import Link from "next/link";
import {
  ArrowLeft,
  Target,
  Flag,
  ChevronDown,
  ChevronUp,
  RotateCcw,
  BookOpen,
  CheckCircle2,
  XCircle,
} from "lucide-react";
import QuestionCard from "@/components/esh/QuestionCard";
import SimilarQuestionsPanel from "@/components/esh/SimilarQuestionsPanel";
import TopicBreakdownChart from "@/components/esh/TopicBreakdownChart";
import Section2Results from "@/components/esh/Section2Results";
import useTestSession from "@/lib/use-test-session";
import { getTestQuestions, getTestInfo, TOPIC_LABELS } from "@/lib/esh-questions";
import type { Question } from "@/lib/esh-questions";
import { hasSection2, getTestSection2, gradeSection2 } from "@/lib/esh-section2";
import { useAuth } from "@/lib/auth-context";
import { useUpgradeModal } from "@/lib/upgrade-modal-context";

function formatDuration(ms: number): string {
  const totalSeconds = Math.floor(ms / 1000);
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  if (hours > 0) return `${hours}ц ${minutes}м`;
  return `${minutes}м`;
}

type ViewFilter = "all" | "correct" | "incorrect" | "skipped" | "flagged";

export default function TestResultsPage() {
  const params = useParams();
  const searchParams = useSearchParams();
  const router = useRouter();
  const testKey = (params.testId as string).toUpperCase();
  const sessionId = searchParams.get("session") || "";

  const testSession = useTestSession();
  const { user, isSubscribed } = useAuth();
  const upgrade = useUpgradeModal();
  const [mounted, setMounted] = useState(false);
  const [expandedQuestions, setExpandedQuestions] = useState<Set<number>>(new Set());
  const [viewFilter, setViewFilter] = useState<ViewFilter>("all");

  useEffect(() => setMounted(true), []);

  const session = mounted ? testSession.getSession(sessionId) : undefined;
  const testInfo = getTestInfo(testKey);
  const questions: Question[] = useMemo(() => getTestQuestions(testKey), [testKey]);
  const solutionsLocked = !isSubscribed && !!testInfo?.solutionsRequirePremium;

  useEffect(() => {
    if (mounted && (!session || session.status !== "completed")) {
      router.replace("/practice/esh/test");
    }
  }, [mounted, session, router]);

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

  const filteredQuestions = useMemo(() => {
    if (!session) return [];
    return questions.filter((q) => {
      const answer = session.answers[q.questionNumber];
      const isCorrect = answer === q.answer;
      const isSkipped = !answer;
      const isFlagged = session.flagged.includes(q.questionNumber);

      switch (viewFilter) {
        case "correct": return isCorrect;
        case "incorrect": return !isSkipped && !isCorrect;
        case "skipped": return isSkipped;
        case "flagged": return isFlagged;
        default: return true;
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
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <p className="mono text-[12px]" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>АЧААЛЛАЖ БАЙНА...</p>
      </div>
    );
  }

  const score = session.score;
  const duration = session.completedAt ? session.completedAt - session.startedAt : 0;

  // Integrated overall score across Section 1 (MCQ) + Section 2 (fill-ins).
  // Official ЭЕШ scoring: 72 pts max from Section 1 (2 pts × 36 MCQs) + 28 pts
  // max from Section 2 (4 problems @ 7 pts) = 100 pts total. For tests without
  // Section 2 (legacy 1A-7B), the headline falls back to 72-max framing.
  const section1Earned = score.correct * 2;
  const section1Max = score.total * 2;
  const section2Items = getTestSection2(testKey) ?? [];
  const section2HasContent = section2Items.length > 0;
  const section2Grade = section2HasContent
    ? gradeSection2(section2Items, session.section2Answers ?? {})
    : { totalEarned: 0, totalMax: 0, perSubproblem: [] };

  // Per-letter counts for the Section 2 stat cards. Mirrors the
  // gradeSection2Subproblem internal walk so the headline cards and the
  // per-subproblem grades reflect the same numbers. Skipped = letter slot
  // left empty by the student; wrong = filled but not matching.
  let s2CorrectLetters = 0;
  let s2WrongLetters = 0;
  let s2SkippedLetters = 0;
  if (section2HasContent) {
    const answersBySource = session.section2Answers ?? {};
    for (const item of section2Items) {
      const letterAnswers = answersBySource[item.source] ?? {};
      for (const slot of item.slots) {
        // parseSlotLabel mirrored inline (avoid the extra import here).
        const match = /^(\d*)([A-Za-z]+)$/.exec(slot.label);
        const prefix = match?.[1] ?? "";
        const varPart = match?.[2] ?? slot.label;
        const correctDigits = slot.answer.slice(prefix.length).split("");
        for (let i = 0; i < varPart.length; i++) {
          const letter = varPart[i];
          const userDigit = letterAnswers[letter] ?? "";
          const correctDigit = correctDigits[i] ?? "";
          if (userDigit === "") s2SkippedLetters++;
          else if (userDigit === correctDigit) s2CorrectLetters++;
          else s2WrongLetters++;
        }
      }
    }
  }

  const totalEarned = section1Earned + section2Grade.totalEarned;
  const totalMax = section1Max + section2Grade.totalMax;
  const totalPct = totalMax > 0 ? Math.round((totalEarned / totalMax) * 100) : 0;
  const scoreColor = totalPct >= 80 ? "var(--accent)" : totalPct >= 50 ? "var(--warn)" : "var(--danger)";

  const filterButtons: { key: ViewFilter; label: string; count: number }[] = [
    { key: "all", label: "Бүгд", count: questions.length },
    { key: "correct", label: "Зөв", count: score.correct },
    { key: "incorrect", label: "Буруу", count: score.incorrect },
    { key: "skipped", label: "Хариулаагүй", count: score.skipped },
    { key: "flagged", label: "Тэмдэглэсэн", count: session.flagged.length },
  ];

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-12">
        {/* Header */}
        <div className="flex items-center gap-3 mb-6">
          <Link
            href="/practice/esh/test"
            className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div>
            <div className="eyebrow">{testInfo?.label || testKey} · Үр дүн</div>
            <p className="mono text-[10px] mt-0.5 uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>
              {new Date(session.completedAt!).toLocaleDateString("mn-MN", {
                year: "numeric",
                month: "long",
                day: "numeric",
              })}
            </p>
          </div>
        </div>

        {/* Score banner */}
        <div className="card-edit p-8 mb-6">
          <div className="flex flex-col sm:flex-row items-center gap-8">
            <div className="text-center">
              <div className="eyebrow mb-2">Оноо</div>
              <div
                className="serif tabular"
                style={{ fontSize: "clamp(72px, 12vw, 120px)", color: scoreColor, letterSpacing: "-0.04em", lineHeight: 1 }}
              >
                {totalEarned}<span className="mono text-[24px]" style={{ color: "var(--fg-3)" }}>/{totalMax}</span>
              </div>
              <p className="mono text-[11px] mt-2 uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                {totalPct}% нийт
              </p>
              <p className="mono text-[11px] mt-1 uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>
                {section1Earned}/{section1Max} Хэсэг 1
                {section2HasContent && (
                  <> · {section2Grade.totalEarned}/{section2Grade.totalMax} Хэсэг 2</>
                )}
              </p>
            </div>

            <div className="flex-1 w-full flex flex-col gap-3">
              {/* Section 1 stat row — always shown */}
              <div>
                <div className="eyebrow mb-1.5" style={{ color: "var(--fg-3)" }}>
                  Хэсэг 1
                </div>
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
                  {[
                    { value: score.correct, label: "Зөв", color: "var(--accent)" },
                    { value: score.incorrect, label: "Буруу", color: "var(--danger)" },
                    { value: score.skipped, label: "Хариулаагүй", color: "var(--fg-2)" },
                    { value: formatDuration(duration), label: "Хугацаа", color: "var(--fg-2)" },
                  ].map((s) => (
                    <div
                      key={s.label}
                      className="text-center p-3 rounded-md"
                      style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}
                    >
                      <p className="serif tabular" style={{ fontSize: 22, color: s.color, letterSpacing: "-0.02em" }}>
                        {s.value}
                      </p>
                      <p className="mono text-[10px] mt-0.5 uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>
                        {s.label}
                      </p>
                    </div>
                  ))}
                </div>
              </div>

              {/* Section 2 stat row — letter-level counts, only when Section 2 exists */}
              {section2HasContent && (
                <div>
                  <div className="eyebrow mb-1.5" style={{ color: "var(--fg-3)" }}>
                    Хэсэг 2
                  </div>
                  <div className="grid grid-cols-3 gap-2">
                    {[
                      { value: s2CorrectLetters, label: "Зөв", color: "var(--accent)" },
                      { value: s2WrongLetters, label: "Буруу", color: "var(--danger)" },
                      { value: s2SkippedLetters, label: "Хариулаагүй", color: "var(--fg-2)" },
                    ].map((s) => (
                      <div
                        key={s.label}
                        className="text-center p-3 rounded-md"
                        style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}
                      >
                        <p className="serif tabular" style={{ fontSize: 22, color: s.color, letterSpacing: "-0.02em" }}>
                          {s.value}
                        </p>
                        <p className="mono text-[10px] mt-0.5 uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>
                          {s.label}
                        </p>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Topic breakdown */}
        <div className="card-edit p-5 mb-4">
          <div className="eyebrow mb-4">Сэдвийн задаргаа</div>
          <TopicBreakdownChart stats={topicStats} />
        </div>

        {/* Weak topics */}
        {weakTopics.length > 0 && (
          <div
            className="card-edit p-5 mb-4"
            style={{ background: "color-mix(in oklch, var(--warn) 6%, transparent)", borderColor: "color-mix(in oklch, var(--warn) 25%, transparent)" }}
          >
            <div className="flex items-start gap-3">
              <Target className="w-5 h-5 shrink-0 mt-0.5" style={{ color: "var(--warn)" }} />
              <div className="flex-1">
                <div className="eyebrow mb-1" style={{ color: "var(--warn)" }}>Анхаарах сэдвүүд</div>
                <p className="text-[13px]" style={{ color: "var(--fg-1)" }}>
                  {weakTopics.map((s) => `${TOPIC_LABELS[s.topic] || s.topic} (${s.accuracy}%)`).join(" · ")}
                </p>
                <Link
                  href="/practice/esh/practice"
                  className="mono text-[11px] uppercase mt-3 inline-flex items-center gap-1.5"
                  style={{ color: "var(--accent)", letterSpacing: "0.06em" }}
                >
                  <BookOpen className="w-3 h-3" />
                  Дадлага хийх
                </Link>
              </div>
            </div>
          </div>
        )}

        {/* Flagged */}
        {session.flagged.length > 0 && (
          <div className="card-edit p-5 mb-4">
            <div className="flex items-start gap-3">
              <Flag className="w-5 h-5 shrink-0 mt-0.5" style={{ color: "var(--warn)" }} />
              <div className="flex-1">
                <div className="eyebrow mb-1">Тэмдэглэсэн · {session.flagged.length}</div>
                <p className="text-[13px]" style={{ color: "var(--fg-2)" }}>
                  {(() => {
                    const flaggedTopics: Record<string, number> = {};
                    for (const qNum of session.flagged) {
                      const q = questions.find((x) => x.questionNumber === qNum);
                      if (q) flaggedTopics[q.topic] = (flaggedTopics[q.topic] || 0) + 1;
                    }
                    const total = session.flagged.length;
                    return Object.entries(flaggedTopics)
                      .sort(([, a], [, b]) => b - a)
                      .map(([topic, count]) => `${TOPIC_LABELS[topic] || topic} ${Math.round((count / total) * 100)}%`)
                      .join(" · ");
                  })()}
                </p>
              </div>
            </div>
          </div>
        )}

        {/* Actions */}
        <div className="flex flex-wrap gap-2 mb-8">
          <button
            onClick={() => {
              const id = testSession.startSession(testKey);
              router.push(`/practice/esh/test/${testKey.toLowerCase()}?session=${id}`);
            }}
            className="btn btn-line"
          >
            <RotateCcw className="mr-1 w-3.5 h-3.5" />
            Дахин бодох
          </button>
          <Link href="/practice/esh/practice" className="btn btn-line">
            <Target className="mr-1 w-3.5 h-3.5" />
            Сул сэдвээр дадлага
          </Link>
          <Link href="/practice/esh" className="btn btn-ghost">
            <ArrowLeft className="mr-1 w-3.5 h-3.5" />
            Нүүр
          </Link>
        </div>

        {/* Question review */}
        <div className="card-edit p-5">
          <div className="eyebrow mb-4">Бодлогуудын задаргаа</div>

          <div className="flex flex-wrap gap-1.5 mb-4">
            {filterButtons.map((f) => {
              const isActive = viewFilter === f.key;
              return (
                <button
                  key={f.key}
                  onClick={() => setViewFilter(f.key)}
                  className="badge-edit transition-all"
                  style={
                    isActive
                      ? { background: "var(--accent-wash)", borderColor: "var(--accent-line)", color: "var(--accent)" }
                      : { background: "var(--bg-2)" }
                  }
                >
                  {f.label} <span className="mono tabular ml-1" style={{ opacity: 0.7 }}>{f.count}</span>
                </button>
              );
            })}
          </div>

          <div className="space-y-2">
            {filteredQuestions.map((q) => {
              const answer = session.answers[q.questionNumber];
              const isCorrect = answer === q.answer;
              const isSkipped = !answer;
              const isFlagged = session.flagged.includes(q.questionNumber);
              const isExpanded = expandedQuestions.has(q.questionNumber);

              return (
                <div key={q.questionNumber}>
                  <button
                    onClick={() => toggleExpand(q.questionNumber)}
                    className="w-full flex items-center gap-3 px-4 py-3 rounded-md transition-all text-left"
                    style={{
                      background: "var(--bg-2)",
                      border: "1px solid var(--line)",
                    }}
                  >
                    <span
                      className="mono tabular w-7 h-7 rounded flex items-center justify-center text-[11px] shrink-0"
                      style={{
                        background: "var(--bg-1)",
                        border: "1px solid var(--line)",
                        color: "var(--fg-2)",
                      }}
                    >
                      {q.questionNumber}
                    </span>
                    <span className="flex-1 text-[13px] truncate" style={{ color: "var(--fg-2)" }}>
                      {TOPIC_LABELS[q.topic] || q.topic}
                      {q.subtopic && ` · ${q.subtopic}`}
                    </span>
                    {isFlagged && <Flag className="w-3.5 h-3.5 shrink-0" style={{ color: "var(--warn)" }} />}
                    {isSkipped ? (
                      <span className="mono text-[11px]" style={{ color: "var(--fg-3)" }}>—</span>
                    ) : isCorrect ? (
                      <CheckCircle2 className="w-4 h-4 shrink-0" style={{ color: "var(--accent)" }} />
                    ) : (
                      <XCircle className="w-4 h-4 shrink-0" style={{ color: "var(--danger)" }} />
                    )}
                    {isExpanded ? (
                      <ChevronUp className="w-4 h-4" style={{ color: "var(--fg-3)" }} />
                    ) : (
                      <ChevronDown className="w-4 h-4" style={{ color: "var(--fg-3)" }} />
                    )}
                  </button>

                  {isExpanded && (
                    <div className="mt-2 mb-2">
                      <QuestionCard
                        mode="review"
                        question={q}
                        selectedAnswer={answer || null}
                        isFlagged={isFlagged}
                        solutionsLocked={solutionsLocked}
                        onSolutionUpgrade={upgrade.openSolutionUpgrade}
                      />
                      {!isSkipped && !isCorrect && (
                        <SimilarQuestionsPanel question={q} />
                      )}
                    </div>
                  )}
                </div>
              );
            })}
          </div>

          {filteredQuestions.length === 0 && (
            <div className="text-center py-8">
              <p className="mono text-[11px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>
                Энэ шүүлтүүрт бодлого олдсонгүй
              </p>
            </div>
          )}
        </div>

        {hasSection2(testKey) && (
          <Section2Results
            testKey={testKey}
            sessionId={sessionId}
            localAnswers={session.section2Answers ?? {}}
            isAuthed={!!user}
          />
        )}
      </div>
    </div>
  );
}
