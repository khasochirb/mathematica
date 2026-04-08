"use client";

import { useState, useEffect, useRef, Suspense } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { Lightbulb, ChevronRight, CheckCircle, XCircle, ArrowRight } from "lucide-react";
import { api, type Problem, type AnswerResult } from "@/lib/api";
import { cn } from "@/lib/utils";

function SessionContent() {
  const router = useRouter();
  const params = useSearchParams();
  const sessionId = params.get("sessionId") ?? "";
  const topicId = params.get("topicId") ?? "";

  const [problem, setProblem] = useState<Problem | null>(null);
  const [answer, setAnswer] = useState("");
  const [selectedOption, setSelectedOption] = useState<string | null>(null);
  const [result, setResult] = useState<AnswerResult | null>(null);
  const [hintIndex, setHintIndex] = useState(-1);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [questionCount, setQuestionCount] = useState(0);
  const [correctCount, setCorrectCount] = useState(0);
  const [totalXp, setTotalXp] = useState(0);
  const startTime = useRef(Date.now());

  useEffect(() => {
    if (!sessionId || !topicId) {
      router.replace("/practice");
      return;
    }
    loadNextProblem();
  }, []);

  async function loadNextProblem() {
    setLoading(true);
    setResult(null);
    setAnswer("");
    setSelectedOption(null);
    setHintIndex(-1);
    startTime.current = Date.now();
    try {
      const p = await api.problems.next(topicId, sessionId);
      setProblem(p);
    } catch {
      router.replace("/practice");
    } finally {
      setLoading(false);
    }
  }

  async function submitAnswer() {
    if (!problem) return;
    const userAnswer = problem.answerType === "MCQ" ? (selectedOption ?? "") : answer;
    if (!userAnswer.trim()) return;
    setSubmitting(true);
    try {
      const res = await api.answers.submit({
        sessionId,
        problemId: problem.id,
        userAnswer,
        timeTakenMs: Date.now() - startTime.current,
        hintsUsed: hintIndex + 1,
      });
      setResult(res);
      setQuestionCount((c) => c + 1);
      if (res.isCorrect) setCorrectCount((c) => c + 1);
      setTotalXp((x) => x + Math.max(0, res.xpDelta));
    } catch (err: unknown) {
      if (err instanceof Error && err.message?.includes("DAILY_LIMIT_REACHED")) {
        router.push("/upgrade");
        return;
      }
    } finally {
      setSubmitting(false);
    }
  }

  async function finishSession() {
    try {
      const today = new Date().toISOString().split("T")[0];
      const sr = await api.sessions.complete(sessionId, today);
      router.push(
        `/practice/result?correct=${sr.totalCorrect}&total=${sr.totalQuestions}&xp=${sr.sessionXp}&leveledUp=${sr.leveledUp}`
      );
    } catch {
      router.replace("/practice");
    }
  }

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center pt-16">
        <div className="text-center">
          <div className="w-8 h-8 border-2 border-primary-600 border-t-transparent rounded-full animate-spin mx-auto mb-3" />
          <p className="text-gray-400 text-sm">Loading problem...</p>
        </div>
      </div>
    );
  }

  if (!problem) return null;

  const showHint = hintIndex >= 0 && problem.hints[hintIndex];

  return (
    <div className="min-h-screen bg-gray-50 pt-20">
      <div className="max-w-2xl mx-auto px-4 sm:px-6 py-8">
        {/* Header */}
        <div className="flex items-center justify-between mb-6">
          <div>
            <p className="text-xs text-gray-400 font-medium uppercase tracking-wide">
              Problem {questionCount + 1}
            </p>
            <p className="text-sm font-semibold text-gray-700 mt-0.5">
              Difficulty {problem.difficulty}/5 ·{" "}
              {problem.answerType === "MCQ" ? "Multiple Choice" : "Free Response"}
            </p>
          </div>
          <div className="flex items-center gap-3">
            <span className="text-sm font-bold text-yellow-600">+{totalXp} XP</span>
            <button
              onClick={finishSession}
              className="text-sm text-gray-400 hover:text-gray-600 transition-colors"
            >
              End session
            </button>
          </div>
        </div>

        {/* Progress bar */}
        <div className="h-1.5 bg-gray-200 rounded-full mb-8 overflow-hidden">
          <div
            className="h-full bg-primary-600 rounded-full transition-all duration-500"
            style={{ width: `${Math.min(100, (questionCount / 10) * 100)}%` }}
          />
        </div>

        {/* Problem card */}
        <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-6 mb-4">
          <p className="text-gray-900 font-medium leading-relaxed text-base mb-6">
            {problem.question}
          </p>

          {/* MCQ options */}
          {problem.answerType === "MCQ" && problem.options && (
            <div className="grid grid-cols-1 gap-2">
              {problem.options.map((opt, i) => {
                const letter = String.fromCharCode(65 + i);
                const isSelected = selectedOption === opt;
                const isCorrect = result?.correctAnswer === opt;
                const isWrong = result && isSelected && !result.isCorrect;
                return (
                  <button
                    key={opt}
                    disabled={!!result}
                    onClick={() => !result && setSelectedOption(opt)}
                    className={cn(
                      "flex items-center gap-3 px-4 py-3 rounded-xl border text-left transition-all text-sm font-medium",
                      isCorrect && result
                        ? "bg-green-50 border-green-300 text-green-800"
                        : isWrong
                        ? "bg-red-50 border-red-200 text-red-700"
                        : isSelected
                        ? "bg-primary-50 border-primary-400 text-primary-800"
                        : "border-gray-200 text-gray-700 hover:border-primary-300 hover:bg-primary-50"
                    )}
                  >
                    <span className={cn(
                      "w-7 h-7 rounded-lg flex items-center justify-center text-xs font-bold flex-shrink-0",
                      isCorrect && result ? "bg-green-100 text-green-700" :
                      isWrong ? "bg-red-100 text-red-600" :
                      isSelected ? "bg-primary-100 text-primary-700" :
                      "bg-gray-100 text-gray-500"
                    )}>
                      {letter}
                    </span>
                    {opt}
                  </button>
                );
              })}
            </div>
          )}

          {/* Numeric / text input */}
          {problem.answerType !== "MCQ" && !result && (
            <input
              type={problem.answerType === "NUMERIC" ? "number" : "text"}
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && submitAnswer()}
              placeholder="Enter your answer..."
              className="w-full px-4 py-3 border border-gray-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
              autoFocus
            />
          )}
        </div>

        {/* Hint */}
        {showHint && (
          <div className="bg-amber-50 border border-amber-200 rounded-xl p-4 mb-4 text-sm text-amber-800">
            <p className="font-semibold mb-1">Hint {hintIndex + 1}</p>
            <p>{problem.hints[hintIndex]}</p>
          </div>
        )}

        {/* Result feedback */}
        {result && (
          <div
            className={cn(
              "rounded-xl p-4 mb-4 text-sm",
              result.isCorrect
                ? "bg-green-50 border border-green-200 text-green-800"
                : "bg-red-50 border border-red-200 text-red-800"
            )}
          >
            <div className="flex items-center gap-2 font-semibold mb-1">
              {result.isCorrect ? (
                <>
                  <CheckCircle className="h-4 w-4" /> Correct! +{result.xpDelta} XP
                </>
              ) : (
                <>
                  <XCircle className="h-4 w-4" /> Incorrect — the answer was{" "}
                  <strong>{result.correctAnswer}</strong>
                </>
              )}
            </div>
            {result.explanation && (
              <p className="text-sm opacity-80 mt-1">{result.explanation}</p>
            )}
          </div>
        )}

        {/* Actions */}
        <div className="flex items-center justify-between">
          <div className="flex gap-2">
            {!result && problem.hints.length > 0 && (
              <button
                onClick={() => setHintIndex((i) => Math.min(i + 1, problem.hints.length - 1))}
                disabled={hintIndex >= problem.hints.length - 1}
                className="flex items-center gap-1.5 px-3 py-2 text-sm text-amber-600 hover:bg-amber-50 rounded-lg transition-colors disabled:opacity-40"
              >
                <Lightbulb className="h-4 w-4" />
                {hintIndex === -1 ? "Get a hint" : "Next hint"}
              </button>
            )}
          </div>

          {result ? (
            <button onClick={loadNextProblem} className="btn-primary py-2.5 px-6 text-sm">
              Next Problem
              <ChevronRight className="ml-1 h-4 w-4" />
            </button>
          ) : (
            <button
              onClick={submitAnswer}
              disabled={submitting || (problem.answerType === "MCQ" ? !selectedOption : !answer.trim())}
              className="btn-primary py-2.5 px-6 text-sm disabled:opacity-50"
            >
              {submitting ? "Checking..." : "Submit"}
              <ArrowRight className="ml-1 h-4 w-4" />
            </button>
          )}
        </div>
      </div>
    </div>
  );
}

export default function SessionPage() {
  return (
    <Suspense>
      <SessionContent />
    </Suspense>
  );
}
