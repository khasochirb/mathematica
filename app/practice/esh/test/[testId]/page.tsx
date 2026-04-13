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

  // Redirect if no valid session
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
      // Also record each answer in the legacy performance system
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
      <div className="min-h-screen bg-surface-900 pt-20 flex items-center justify-center">
        <div className="text-gray-500">Ачааллаж байна...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-surface-900 flex flex-col">
      {/* Top bar - positioned below site header (h-16 = 64px) */}
      <div className="fixed top-16 left-0 right-0 z-30 bg-surface-900/95 backdrop-blur-sm border-b border-white/[0.06]">
        <div className="max-w-7xl mx-auto px-4 h-14 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <button
              onClick={() => setShowQuitModal(true)}
              className="p-1.5 rounded-lg text-gray-500 hover:text-white hover:bg-white/[0.08] transition-colors"
              title="Буцах"
            >
              <ChevronLeft className="w-5 h-5" />
            </button>
            <div>
              <h1 className="font-display text-sm font-bold text-white">
                {testInfo?.label || testKey}
              </h1>
              <p className="text-[11px] text-gray-500">
                {answeredCount}/{questions.length} хариулсан
                {flaggedCount > 0 && ` · ${flaggedCount} тэмдэглэсэн`}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <TestTimer startTime={session.startedAt} />

            {/* Mobile nav toggle */}
            <button
              onClick={() => setShowNav(!showNav)}
              className="lg:hidden p-1.5 rounded-lg text-gray-500 hover:text-white hover:bg-white/[0.08] transition-colors"
            >
              {showNav ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>

            <button
              onClick={() => setShowSubmitModal(true)}
              className="btn-primary text-sm px-4 py-1.5 flex items-center gap-1.5"
            >
              <Send className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">Дуусгах</span>
            </button>
          </div>
        </div>

        {/* Progress bar */}
        <div className="h-0.5 bg-white/[0.04]">
          <div
            className="h-full bg-primary-500/60 transition-all duration-300"
            style={{
              width: `${(answeredCount / questions.length) * 100}%`,
            }}
          />
        </div>
      </div>

      {/* Main content - offset for site header (64px) + test bar (60px) */}
      <div className="flex-1 pt-[124px]">
        <div className="max-w-7xl mx-auto px-4 py-6 flex gap-6">
          {/* Question area */}
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

            {/* Navigation buttons */}
            <div className="flex items-center justify-between mt-4">
              <button
                onClick={handlePrev}
                disabled={currentIndex === 0}
                className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-medium transition-all ${
                  currentIndex === 0
                    ? "text-gray-600 cursor-not-allowed"
                    : "text-gray-400 bg-white/[0.05] border border-white/[0.08] hover:bg-white/[0.1] hover:text-white"
                }`}
              >
                <ArrowLeft className="w-4 h-4" />
                Өмнөх
              </button>

              <span className="text-sm text-gray-500">
                {currentIndex + 1} / {questions.length}
              </span>

              <button
                onClick={handleNext}
                disabled={currentIndex === questions.length - 1}
                className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-medium transition-all ${
                  currentIndex === questions.length - 1
                    ? "text-gray-600 cursor-not-allowed"
                    : "text-gray-400 bg-white/[0.05] border border-white/[0.08] hover:bg-white/[0.1] hover:text-white"
                }`}
              >
                Дараах
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>

          {/* Desktop navigator sidebar */}
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
            className="absolute inset-0 bg-black/40"
            onClick={() => setShowNav(false)}
          />
          <div className="absolute bottom-0 left-0 right-0 bg-surface-900 border-t border-white/[0.08] p-4 rounded-t-2xl">
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

      {/* Quit confirmation modal */}
      {showQuitModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm px-4">
          <div className="card-glass p-6 max-w-sm w-full">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-xl bg-yellow-500/20 flex items-center justify-center">
                <AlertTriangle className="w-5 h-5 text-yellow-400" />
              </div>
              <h3 className="font-display font-bold text-white">
                Шалгалтаас гарах уу?
              </h3>
            </div>

            <p className="text-sm text-gray-400 mb-6">
              Таны хариултууд хадгалагдана. Та дараа нь үргэлжлүүлж болно.
            </p>

            <div className="flex gap-3">
              <button
                onClick={() => setShowQuitModal(false)}
                className="flex-1 px-4 py-2.5 rounded-xl text-sm font-medium text-gray-400 bg-white/[0.05] border border-white/[0.08] hover:bg-white/[0.1] transition-colors"
              >
                Үргэлжлүүлэх
              </button>
              <button
                onClick={() => {
                  setShowQuitModal(false);
                  router.push("/practice/esh/test");
                }}
                className="flex-1 px-4 py-2.5 rounded-xl text-sm font-medium text-yellow-400 bg-yellow-500/10 border border-yellow-400/20 hover:bg-yellow-500/20 transition-colors"
              >
                Гарах
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Submit confirmation modal */}
      {showSubmitModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm px-4">
          <div className="card-glass p-6 max-w-sm w-full">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-xl bg-primary-500/20 flex items-center justify-center">
                <Send className="w-5 h-5 text-primary-400" />
              </div>
              <h3 className="font-display font-bold text-white">
                Шалгалт дуусгах уу?
              </h3>
            </div>

            <div className="space-y-2 mb-6 text-sm">
              <div className="flex items-center justify-between text-gray-400">
                <span>Хариулсан</span>
                <span className="text-primary-300 font-medium">
                  {answeredCount}/{questions.length}
                </span>
              </div>
              {unansweredCount > 0 && (
                <div className="flex items-center gap-2 text-yellow-400">
                  <AlertTriangle className="w-4 h-4" />
                  <span>{unansweredCount} бодлого хариулаагүй байна</span>
                </div>
              )}
              {flaggedCount > 0 && (
                <div className="flex items-center gap-2 text-orange-400">
                  <Flag className="w-4 h-4" />
                  <span>{flaggedCount} бодлого тэмдэглэсэн</span>
                </div>
              )}
            </div>

            <div className="flex gap-3">
              <button
                onClick={() => setShowSubmitModal(false)}
                className="flex-1 px-4 py-2.5 rounded-xl text-sm font-medium text-gray-400 bg-white/[0.05] border border-white/[0.08] hover:bg-white/[0.1] transition-colors"
              >
                Буцах
              </button>
              <button
                onClick={() => {
                  setShowSubmitModal(false);
                  handleSubmit();
                }}
                className="flex-1 btn-primary text-sm py-2.5"
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
