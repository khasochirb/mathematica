"use client";

import { useState, useEffect, useCallback, useMemo } from "react";
import { useParams, useSearchParams, useRouter } from "next/navigation";
import {
  ArrowLeft,
  ArrowRight,
  ChevronLeft,
  Send,
  Flag,
  AlertTriangle,
  Menu,
  X,
} from "lucide-react";
import QuestionCard from "@/components/esh/QuestionCard";
import TestTimer from "@/components/esh/TestTimer";
import QuestionNavigator from "@/components/esh/QuestionNavigator";
import useTestSession from "@/lib/use-test-session";
import useFlaggedQuestions from "@/lib/use-flagged-questions";
import usePerformance from "@/lib/use-performance";
import { getTestQuestions, getTestInfo } from "@/lib/esh-questions";
import type { Question } from "@/lib/esh-questions";

export default function TestRunnerPage() {
  const params = useParams();
  const searchParams = useSearchParams();
  const router = useRouter();
  const testKey = (params.testId as string).toUpperCase();
  const sessionId = searchParams.get("session") || "";

  const testSession = useTestSession();
  const flaggedHook = useFlaggedQuestions();
  const perf = usePerformance();

  const [currentIndex, setCurrentIndex] = useState(0);
  const [showNav, setShowNav] = useState(false);
  const [showSubmitModal, setShowSubmitModal] = useState(false);
  const [showQuitModal, setShowQuitModal] = useState(false);
  const [mounted, setMounted] = useState(false);

  useEffect(() => setMounted(true), []);

  const testInfo = getTestInfo(testKey);
  const questions: Question[] = useMemo(
    () => getTestQuestions(testKey),
    [testKey],
  );
  const session = mounted ? testSession.getSession(sessionId) : undefined;

  useEffect(() => {
    if (mounted && !session) {
      router.replace("/practice/esh/test");
    }
  }, [mounted, session, router]);

  const currentQuestion = questions[currentIndex];
  const answers = session?.answers || {};
  const flagged = session?.flagged || [];

  const handleSelectAnswer = useCallback(
    (letter: string) => {
      if (!sessionId) return;
      testSession.setAnswer(sessionId, currentQuestion.questionNumber, letter);
    },
    [sessionId, testSession, currentQuestion],
  );

  const handleToggleFlag = useCallback(() => {
    if (!sessionId || !currentQuestion) return;
    testSession.toggleFlag(sessionId, currentQuestion.questionNumber);
    flaggedHook.toggleFlag(
      currentQuestion.source,
      testKey,
      currentQuestion.topic,
      currentQuestion.difficulty,
      sessionId,
    );
  }, [sessionId, testSession, flaggedHook, currentQuestion, testKey]);

  const handleNext = useCallback(() => {
    if (currentIndex < questions.length - 1) {
      setCurrentIndex((i) => i + 1);
    }
  }, [currentIndex, questions.length]);

  const handlePrev = useCallback(() => {
    if (currentIndex > 0) {
      setCurrentIndex((i) => i - 1);
    }
  }, [currentIndex]);

  const handleSubmit = useCallback(() => {
    const completed = testSession.completeSession(sessionId);
    if (completed) {
      for (const q of questions) {
        const answer = completed.answers[q.questionNumber];
        if (answer) {
          perf.recordAttempt({
            questionSource: q.source,
            topic: q.topic,
            subtopic: q.subtopic,
            difficulty: q.difficulty,
            selectedAnswer: answer,
            correctAnswer: q.answer,
            isCorrect: answer === q.answer,
          });
        }
      }
    }
    router.push(
      `/practice/esh/test/${testKey.toLowerCase()}/results?session=${sessionId}`,
    );
  }, [testSession, sessionId, router, testKey, questions, perf]);

  const answeredCount = Object.keys(answers).length;
  const flaggedCount = flagged.length;
  const unansweredCount = questions.length - answeredCount;

  if (!mounted || !session || !currentQuestion) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <p className="mono text-[12px]" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>АЧААЛЛАЖ БАЙНА...</p>
      </div>
    );
  }

  const progressPct = (answeredCount / questions.length) * 100;

  return (
    <div className="min-h-screen flex flex-col" style={{ background: "var(--bg)" }}>
      {/* Top bar */}
      <div
        className="fixed top-16 left-0 right-0 z-30"
        style={{
          background: "color-mix(in oklch, var(--bg) 92%, transparent)",
          backdropFilter: "blur(8px)",
          borderBottom: "1px solid var(--line)",
        }}
      >
        <div className="max-w-7xl mx-auto px-4 h-14 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <button
              onClick={() => setShowQuitModal(true)}
              className="p-1.5 rounded-md transition-colors"
              style={{ color: "var(--fg-3)" }}
              title="Буцах"
            >
              <ChevronLeft className="w-5 h-5" />
            </button>
            <div>
              <div className="serif" style={{ fontSize: 14, color: "var(--fg)" }}>
                {testInfo?.label || testKey}
              </div>
              <div className="mono text-[10px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>
                {answeredCount}/{questions.length} хариулсан
                {flaggedCount > 0 && ` · ${flaggedCount} тэмдэглэсэн`}
              </div>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <TestTimer startTime={session.startedAt} />

            <button
              onClick={() => setShowNav(!showNav)}
              className="lg:hidden p-1.5 rounded-md transition-colors"
              style={{ color: "var(--fg-3)" }}
            >
              {showNav ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>

            <button
              onClick={() => setShowSubmitModal(true)}
              className="btn btn-primary text-[12px] px-3 py-1.5"
            >
              <Send className="w-3 h-3 mr-1" />
              <span className="hidden sm:inline">Дуусгах</span>
            </button>
          </div>
        </div>

        <div className="h-[2px]" style={{ background: "var(--bg-2)" }}>
          <div
            className="h-full transition-all duration-300"
            style={{ width: `${progressPct}%`, background: "var(--accent)" }}
          />
        </div>
      </div>

      <div className="flex-1 pt-[124px]">
        <div className="max-w-7xl mx-auto px-4 py-6 flex gap-6">
          <div className="flex-1 max-w-3xl">
            <QuestionCard
              mode="test"
              question={currentQuestion}
              selectedAnswer={answers[currentQuestion.questionNumber] || null}
              onSelectAnswer={handleSelectAnswer}
              isFlagged={flagged.includes(currentQuestion.questionNumber)}
              onToggleFlag={handleToggleFlag}
              questionIndex={currentIndex + 1}
            />

            <div className="flex items-center justify-between mt-4">
              <button
                onClick={handlePrev}
                disabled={currentIndex === 0}
                className="btn btn-line text-[12px]"
                style={currentIndex === 0 ? { opacity: 0.4, cursor: "not-allowed" } : {}}
              >
                <ArrowLeft className="w-3.5 h-3.5 mr-1" />
                Өмнөх
              </button>

              <span className="mono tabular text-[11px]" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>
                {String(currentIndex + 1).padStart(2, "0")} / {String(questions.length).padStart(2, "0")}
              </span>

              <button
                onClick={handleNext}
                disabled={currentIndex === questions.length - 1}
                className="btn btn-line text-[12px]"
                style={currentIndex === questions.length - 1 ? { opacity: 0.4, cursor: "not-allowed" } : {}}
              >
                Дараах
                <ArrowRight className="w-3.5 h-3.5 ml-1" />
              </button>
            </div>
          </div>

          <div className="hidden lg:block w-64 shrink-0">
            <div className="sticky top-[140px]">
              <QuestionNavigator
                totalQuestions={questions.length}
                currentIndex={currentIndex}
                answers={answers}
                flagged={flagged}
                onJumpTo={setCurrentIndex}
              />
            </div>
          </div>
        </div>
      </div>

      {/* Mobile navigator overlay */}
      {showNav && (
        <div className="fixed inset-0 z-30 lg:hidden">
          <div
            className="absolute inset-0"
            style={{ background: "color-mix(in oklch, black 40%, transparent)" }}
            onClick={() => setShowNav(false)}
          />
          <div
            className="absolute bottom-0 left-0 right-0 p-4 rounded-t-2xl"
            style={{ background: "var(--bg-1)", borderTop: "1px solid var(--line)" }}
          >
            <QuestionNavigator
              totalQuestions={questions.length}
              currentIndex={currentIndex}
              answers={answers}
              flagged={flagged}
              onJumpTo={(i) => {
                setCurrentIndex(i);
                setShowNav(false);
              }}
            />
          </div>
        </div>
      )}

      {/* Quit modal */}
      {showQuitModal && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center px-4"
          style={{ background: "color-mix(in oklch, black 50%, transparent)", backdropFilter: "blur(8px)" }}
        >
          <div className="card-edit p-6 max-w-sm w-full" style={{ background: "var(--bg-1)" }}>
            <div className="flex items-center gap-3 mb-3">
              <div
                className="w-10 h-10 rounded-md flex items-center justify-center"
                style={{
                  background: "color-mix(in oklch, var(--warn) 14%, transparent)",
                  border: "1px solid color-mix(in oklch, var(--warn) 30%, transparent)",
                  color: "var(--warn)",
                }}
              >
                <AlertTriangle className="w-5 h-5" />
              </div>
              <div className="eyebrow">Баталгаажуулах</div>
            </div>
            <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
              Шалгалтаас <em className="serif-italic" style={{ color: "var(--warn)" }}>гарах</em> уу?
            </h3>
            <p className="text-[13px] mt-3 mb-6" style={{ color: "var(--fg-2)" }}>
              Таны хариултууд хадгалагдана. Та дараа нь үргэлжлүүлж болно.
            </p>
            <div className="flex gap-2">
              <button onClick={() => setShowQuitModal(false)} className="btn btn-line flex-1">
                Үргэлжлүүлэх
              </button>
              <button
                onClick={() => {
                  setShowQuitModal(false);
                  router.push("/practice/esh/test");
                }}
                className="btn flex-1"
                style={{
                  background: "color-mix(in oklch, var(--warn) 14%, transparent)",
                  border: "1px solid color-mix(in oklch, var(--warn) 30%, transparent)",
                  color: "var(--warn)",
                }}
              >
                Гарах
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Submit modal */}
      {showSubmitModal && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center px-4"
          style={{ background: "color-mix(in oklch, black 50%, transparent)", backdropFilter: "blur(8px)" }}
        >
          <div className="card-edit p-6 max-w-sm w-full" style={{ background: "var(--bg-1)" }}>
            <div className="flex items-center gap-3 mb-3">
              <div
                className="w-10 h-10 rounded-md flex items-center justify-center"
                style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}
              >
                <Send className="w-5 h-5" />
              </div>
              <div className="eyebrow">Дуусгах</div>
            </div>
            <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
              Шалгалт <em className="serif-italic" style={{ color: "var(--accent)" }}>дуусгах</em> уу?
            </h3>

            <div className="space-y-2 mt-4 mb-6 text-[13px]">
              <div className="flex items-center justify-between" style={{ color: "var(--fg-2)" }}>
                <span>Хариулсан</span>
                <span className="mono tabular" style={{ color: "var(--accent)" }}>
                  {answeredCount}/{questions.length}
                </span>
              </div>
              {unansweredCount > 0 && (
                <div className="flex items-center gap-2" style={{ color: "var(--warn)" }}>
                  <AlertTriangle className="w-3.5 h-3.5" />
                  <span>{unansweredCount} бодлого хариулаагүй</span>
                </div>
              )}
              {flaggedCount > 0 && (
                <div className="flex items-center gap-2" style={{ color: "var(--warn)" }}>
                  <Flag className="w-3.5 h-3.5" />
                  <span>{flaggedCount} бодлого тэмдэглэсэн</span>
                </div>
              )}
            </div>

            <div className="flex gap-2">
              <button onClick={() => setShowSubmitModal(false)} className="btn btn-line flex-1">
                Буцах
              </button>
              <button
                onClick={() => {
                  setShowSubmitModal(false);
                  handleSubmit();
                }}
                className="btn btn-primary flex-1"
              >
                Дуусгах
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
