"use client";

import { useState, useEffect, useRef, Suspense } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { Lightbulb, ChevronRight, CheckCircle, XCircle, ArrowRight } from "lucide-react";
import { api, type Problem, type AnswerResult } from "@/lib/api";

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
  const [, setCorrectCount] = useState(0);
  const [totalXp, setTotalXp] = useState(0);
  const startTime = useRef(Date.now());

  useEffect(() => {
    if (!sessionId || !topicId) {
      router.replace("/practice");
      return;
    }
    loadNextProblem();
    // eslint-disable-next-line react-hooks/exhaustive-deps
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
      <div className="min-h-screen flex items-center justify-center pt-20" style={{ background: "var(--bg)" }}>
        <div className="text-center">
          <div
            className="w-8 h-8 border-2 rounded-full animate-spin mx-auto mb-3"
            style={{ borderColor: "var(--accent)", borderTopColor: "transparent" }}
          />
          <p className="mono text-[12px]" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>
            LOADING PROBLEM...
          </p>
        </div>
      </div>
    );
  }

  if (!problem) return null;

  const showHint = hintIndex >= 0 && problem.hints[hintIndex];
  const progressPct = Math.min(100, (questionCount / 10) * 100);

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-2xl mx-auto px-4 sm:px-6 py-8">
        {/* Header */}
        <div className="flex items-center justify-between mb-5">
          <div>
            <div className="eyebrow mb-1">Problem · {String(questionCount + 1).padStart(2, "0")}</div>
            <p className="mono text-[11px]" style={{ color: "var(--fg-2)", letterSpacing: "0.04em" }}>
              DIFFICULTY {problem.difficulty}/5 · {problem.answerType === "MCQ" ? "MCQ" : "FREE RESPONSE"}
            </p>
          </div>
          <div className="flex items-center gap-4">
            <div className="flex items-baseline gap-1">
              <span className="serif tabular" style={{ fontSize: 22, color: "var(--accent)", letterSpacing: "-0.02em" }}>
                +{totalXp}
              </span>
              <span className="mono text-[10px]" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>XP</span>
            </div>
            <button
              onClick={finishSession}
              className="mono text-[11px] uppercase transition-colors"
              style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}
            >
              End session
            </button>
          </div>
        </div>

        {/* Progress */}
        <div className="h-[3px] rounded-full mb-8 overflow-hidden" style={{ background: "var(--bg-2)" }}>
          <div
            className="h-full rounded-full transition-all duration-500"
            style={{ width: `${progressPct}%`, background: "var(--accent)" }}
          />
        </div>

        {/* Problem card */}
        <div className="card-edit p-6 mb-4">
          <p className="serif" style={{ fontWeight: 400, fontSize: 19, lineHeight: 1.5, color: "var(--fg)" }}>
            {problem.question}
          </p>

          {problem.answerType === "MCQ" && problem.options && (
            <div className="grid grid-cols-1 gap-2 mt-6">
              {problem.options.map((opt, i) => {
                const letter = String.fromCharCode(65 + i);
                const isSelected = selectedOption === opt;
                const isCorrect = result?.correctAnswer === opt;
                const isWrong = result && isSelected && !result.isCorrect;
                let bg = "var(--bg-1)";
                let border = "var(--line)";
                let color = "var(--fg)";
                if (result && isCorrect) {
                  bg = "var(--accent-wash)";
                  border = "var(--accent-line)";
                  color = "var(--accent)";
                } else if (isWrong) {
                  bg = "color-mix(in oklch, var(--danger) 10%, transparent)";
                  border = "color-mix(in oklch, var(--danger) 30%, transparent)";
                  color = "var(--danger)";
                } else if (isSelected) {
                  bg = "var(--accent-wash)";
                  border = "var(--accent-line)";
                }
                return (
                  <button
                    key={opt}
                    disabled={!!result}
                    onClick={() => !result && setSelectedOption(opt)}
                    className="flex items-center gap-3 px-4 py-3 rounded-md text-left transition-all text-[14px]"
                    style={{ background: bg, border: `1px solid ${border}`, color }}
                  >
                    <span
                      className="mono w-6 h-6 rounded flex items-center justify-center text-[11px] flex-shrink-0"
                      style={{
                        background: result && isCorrect ? "var(--bg-1)" : "var(--bg-2)",
                        border: `1px solid ${border}`,
                        letterSpacing: "0.04em",
                      }}
                    >
                      {letter}
                    </span>
                    <span>{opt}</span>
                  </button>
                );
              })}
            </div>
          )}

          {problem.answerType !== "MCQ" && !result && (
            <input
              type={problem.answerType === "NUMERIC" ? "number" : "text"}
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && submitAnswer()}
              placeholder="Enter your answer..."
              className="w-full mt-6 outline-none"
              style={{
                padding: "10px 12px",
                fontSize: 14,
                background: "var(--bg-1)",
                border: "1px solid var(--line)",
                borderRadius: 8,
                color: "var(--fg)",
              }}
              autoFocus
            />
          )}
        </div>

        {showHint && (
          <div
            className="rounded-md p-4 mb-4 text-[13px]"
            style={{
              background: "color-mix(in oklch, var(--warn) 8%, transparent)",
              border: "1px solid color-mix(in oklch, var(--warn) 25%, transparent)",
              color: "var(--warn)",
            }}
          >
            <p className="mono text-[10px] uppercase mb-1" style={{ letterSpacing: "0.08em", opacity: 0.8 }}>
              Hint {hintIndex + 1}
            </p>
            <p>{problem.hints[hintIndex]}</p>
          </div>
        )}

        {result && (
          <div
            className="rounded-md p-4 mb-4 text-[13px]"
            style={{
              background: result.isCorrect
                ? "var(--accent-wash)"
                : "color-mix(in oklch, var(--danger) 8%, transparent)",
              border: `1px solid ${result.isCorrect ? "var(--accent-line)" : "color-mix(in oklch, var(--danger) 25%, transparent)"}`,
              color: result.isCorrect ? "var(--accent-ink)" : "var(--danger)",
            }}
          >
            <div className="flex items-center gap-2 mb-1">
              {result.isCorrect ? <CheckCircle className="h-4 w-4" /> : <XCircle className="h-4 w-4" />}
              <span className="mono text-[11px] uppercase" style={{ letterSpacing: "0.06em" }}>
                {result.isCorrect ? `CORRECT · +${result.xpDelta} XP` : "INCORRECT"}
              </span>
            </div>
            {!result.isCorrect && (
              <p className="text-[13px]">
                The answer was <strong className="mono">{result.correctAnswer}</strong>
              </p>
            )}
            {result.explanation && (
              <p className="text-[13px] mt-1" style={{ opacity: 0.85 }}>{result.explanation}</p>
            )}
          </div>
        )}

        <div className="flex items-center justify-between">
          <div className="flex gap-2">
            {!result && problem.hints.length > 0 && (
              <button
                onClick={() => setHintIndex((i) => Math.min(i + 1, problem.hints.length - 1))}
                disabled={hintIndex >= problem.hints.length - 1}
                className="flex items-center gap-1.5 px-3 py-2 mono text-[11px] uppercase rounded-md transition-colors disabled:opacity-40"
                style={{ color: "var(--warn)", letterSpacing: "0.06em" }}
              >
                <Lightbulb className="h-3.5 w-3.5" />
                {hintIndex === -1 ? "Get a hint" : "Next hint"}
              </button>
            )}
          </div>

          {result ? (
            <button onClick={loadNextProblem} className="btn btn-primary">
              Next problem
              <ChevronRight className="ml-1 h-3.5 w-3.5" />
            </button>
          ) : (
            <button
              onClick={submitAnswer}
              disabled={submitting || (problem.answerType === "MCQ" ? !selectedOption : !answer.trim())}
              className="btn btn-primary"
              style={{ opacity: submitting ? 0.6 : 1 }}
            >
              {submitting ? "Checking..." : "Submit"}
              <ArrowRight className="ml-1 h-3.5 w-3.5" />
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
