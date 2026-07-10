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
import Section2Problem from "@/components/esh/Section2Problem";
import TestTimer from "@/components/esh/TestTimer";
import QuestionNavigator from "@/components/esh/QuestionNavigator";
import useTestSession from "@/lib/use-test-session";
import useFlaggedQuestions from "@/lib/use-flagged-questions";
import usePerformance from "@/lib/use-performance";
import { getTestQuestions, getTestInfo } from "@/lib/esh-questions";
import type { Question } from "@/lib/esh-questions";
import {
  composeSlotAnswer,
  getTestSection2,
  gradeSection2Subproblem,
  hasSection2,
  parseSlotLabel,
} from "@/lib/esh-section2";
import type { Section2Item } from "@/lib/esh-section2";
import { useAuth } from "@/lib/auth-context";
import { useUpgradeModal } from "@/lib/upgrade-modal-context";

const TEST_DURATION_MS = 100 * 60 * 1000;

export default function TestRunnerPage() {
  const params = useParams();
  const searchParams = useSearchParams();
  const router = useRouter();
  const testKey = (params.testId as string).toUpperCase();
  const sessionId = searchParams.get("session") || "";

  const { isSubscribed, isLoading: authLoading } = useAuth();
  const upgrade = useUpgradeModal();
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
  const section2Items: Section2Item[] = useMemo(
    () => getTestSection2(testKey) ?? [],
    [testKey],
  );
  const testHasS2 = hasSection2(testKey);

  const session = mounted ? testSession.getSession(sessionId) : undefined;

  useEffect(() => {
    if (mounted && !session) {
      router.replace("/practice/esh/test");
    }
  }, [mounted, session, router]);

  // Guard against URL-bypass of the Premium gate.
  useEffect(() => {
    if (!mounted || authLoading) return;
    if (testInfo?.isPremium && !isSubscribed) {
      upgrade.open({
        source: "gated_legacy_tests",
        title: `${testInfo.label} — Premium`,
        description:
          "Нэмэлт дадлага тестүүд нь Premium багцад багтсан. Premium эхлэхэд и-мэйлээр мэдэгдэнэ.",
      });
      router.replace("/practice/esh/test");
    }
  }, [mounted, authLoading, testInfo, isSubscribed, upgrade, router]);

  const totalMcq = questions.length;

  // Section 2 collapses to ONE screen per problem (e.g. 2.1) with all
  // sub-parts (1)(2)(3) stacked together — matches the printed EYSH
  // paper. Compute the unique problem ids in source order.
  const section2ProblemIds = useMemo(() => {
    const seen: string[] = [];
    for (const item of section2Items) {
      if (!seen.includes(item.problem)) seen.push(item.problem);
    }
    return seen;
  }, [section2Items]);
  const section2ItemsByProblem = useMemo(() => {
    const map: Record<string, Section2Item[]> = {};
    for (const item of section2Items) {
      (map[item.problem] ??= []).push(item);
    }
    for (const id of Object.keys(map)) {
      map[id].sort((a, b) => a.subproblem - b.subproblem);
    }
    return map;
  }, [section2Items]);

  // Screen layout (no interstitial):
  //   0..totalMcq-1                                    → MCQs
  //   totalMcq..totalMcq+section2ProblemIds.length-1   → Part 2 problems
  const totalScreens =
    totalMcq + (testHasS2 ? section2ProblemIds.length : 0);

  const isSection2 =
    testHasS2 &&
    currentIndex >= totalMcq &&
    currentIndex < totalMcq + section2ProblemIds.length;
  const currentProblemIndex = isSection2 ? currentIndex - totalMcq : -1;
  const currentProblemId =
    isSection2 ? section2ProblemIds[currentProblemIndex] : undefined;
  const currentProblemItems = currentProblemId
    ? section2ItemsByProblem[currentProblemId]
    : undefined;
  const currentQuestion = !isSection2 ? questions[currentIndex] : undefined;

  const answers = session?.answers ?? {};
  const flagged = session?.flagged ?? [];
  const section2Answers = session?.section2Answers ?? {};

  const handleSelectAnswer = useCallback(
    (letter: string) => {
      if (!sessionId || !currentQuestion) return;
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

  // Section2Problem stacks multiple sub-parts on one screen, so the
  // change callback must include which item the slot belongs to —
  // slot labels can repeat across sub-parts (e.g. "a" exists in both
  // 2.1.1 and 2.1.2). Per-slot full-answer strings are decomposed
  // here into the per-letter digits useTestSession stores. Empty /
  // space sentinel positions become "" in the per-letter store.
  const handleSection2SlotChange = useCallback(
    (itemSource: string, slotLabel: string, fullAnswer: string) => {
      if (!sessionId) return;
      const { prefix, varPart } = parseSlotLabel(slotLabel);
      const varValue = fullAnswer.slice(prefix.length);
      for (let i = 0; i < varPart.length; i++) {
        const ch = varValue[i];
        const digit = ch && ch !== " " ? ch : "";
        testSession.setSection2Answer(
          sessionId,
          itemSource,
          varPart[i],
          digit,
        );
      }
    },
    [sessionId, testSession],
  );

  const handleNext = useCallback(() => {
    if (currentIndex < totalScreens - 1) setCurrentIndex((i) => i + 1);
  }, [currentIndex, totalScreens]);

  const handlePrev = useCallback(() => {
    if (currentIndex > 0) setCurrentIndex((i) => i - 1);
  }, [currentIndex]);

  // Handles the explicit-submit path AND the timer-expiry auto-submit.
  // 1. Marks the session completed (Part 1 score computed by the hook).
  // 2. Records each answered MCQ in the legacy performance store.
  // 3. If the test has Section 2 AND any letter answers were typed, posts
  //    the batch to /api/section2/attempts. Auth failures are swallowed
  //    (anon students still see their score on the results page via the
  //    client-side gradeSection2 path; the queue retry handles transient
  //    network errors).
  const handleSubmit = useCallback(async () => {
    const completed = testSession.completeSession(sessionId);
    if (completed) {
      for (const q of questions) {
        const answer = completed.answers[q.questionNumber];
        if (answer) {
          perf.recordAttempt({
            questionSource: q.source,
            topic: q.topic,
            subtopic: q.subtopic,
            selectedAnswer: answer,
            correctAnswer: q.answer,
            isCorrect: answer === q.answer,
            source: "test",
          });
        }
      }
    }

    // Section 2 fans into the main attempt stream too (client-graded, one
    // row per touched subproblem) so fill-in work feeds topic/skill
    // analytics and cross-device progress — not just its own table.
    if (testHasS2) {
      const s2Items = getTestSection2(testKey) ?? [];
      for (const item of s2Items) {
        const letters = section2Answers[item.source];
        if (!letters || Object.values(letters).every((v) => !v)) continue;
        const grade = gradeSection2Subproblem(item, letters);
        perf.recordAttempt({
          questionSource: item.source,
          topic: item.topic ?? "other",
          subtopic: item.subtopic ?? "",
          selectedAnswer: item.slots.map((s) => composeSlotAnswer(s, letters)).join(","),
          correctAnswer: item.slots.map((s) => s.answer).join(","),
          isCorrect: grade.correct,
          source: "test",
        });
      }
    }

    if (testHasS2 && Object.keys(section2Answers).length > 0) {
      try {
        await testSession.submitSection2Attempts(sessionId);
      } catch {
        // Auth failure (anon) or transient error — already queued by
        // submitSection2Attempts on throw. Section 1 is locked-in;
        // results page renders client-graded Section 2 score regardless.
      }
    }

    router.push(
      `/practice/esh/test/${testKey.toLowerCase()}/results?session=${sessionId}`,
    );
  }, [
    testSession,
    sessionId,
    router,
    testKey,
    questions,
    perf,
    testHasS2,
    section2Answers,
  ]);

  // Auto-submit on timer expiry. Wired via TestTimer's onExpiry.
  const handleAutoSubmit = useCallback(() => {
    setShowSubmitModal(false);
    handleSubmit();
  }, [handleSubmit]);

  const answeredCount = Object.keys(answers).length;
  const flaggedCount = flagged.length;
  const unansweredCount = totalMcq - answeredCount;

  // Section 2 unanswered list — a subproblem is "unanswered" iff any
  // slot's composed answer differs in length from its expected answer
  // (i.e. some variable letter is missing). Used in the submit modal.
  const unansweredSection2: Section2Item[] = useMemo(() => {
    if (!testHasS2) return [];
    return section2Items.filter((item) => {
      const letterMap = section2Answers[item.source] ?? {};
      for (const slot of item.slots) {
        const composed = composeSlotAnswer(slot, letterMap);
        if (composed.length !== slot.answer.length) return true;
      }
      return false;
    });
  }, [testHasS2, section2Items, section2Answers]);

  if (!mounted || !session) {
    return (
      <div
        className="min-h-screen pt-20 flex items-center justify-center"
        style={{ background: "var(--bg)" }}
      >
        <p
          className="mono text-[12px]"
          style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}
        >
          АЧААЛЛАЖ БАЙНА...
        </p>
      </div>
    );
  }

  // Defend against malformed currentIndex (e.g. on tests without
  // Section 2 but a stale URL). If we slipped past totalMcq on a
  // Part-1-only test, snap back to the last MCQ.
  if (!testHasS2 && currentIndex >= totalMcq && totalMcq > 0) {
    setCurrentIndex(totalMcq - 1);
    return null;
  }

  // Combined progress: count typed Part 1 answers + Part 2 subproblems
  // with at least one letter filled. interstitial doesn't count.
  const section2InProgress = testHasS2
    ? section2Items.filter((it) => {
        const letterMap = section2Answers[it.source] ?? {};
        return Object.values(letterMap).some((v) => v.length > 0);
      }).length
    : 0;
  const progressDenominator = testHasS2
    ? totalMcq + section2Items.length
    : totalMcq;
  const progressPct =
    progressDenominator === 0
      ? 0
      : ((answeredCount + section2InProgress) / progressDenominator) * 100;

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
              <div
                className="mono text-[10px] uppercase"
                style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}
              >
                {answeredCount}/{totalMcq} хариулсан
                {testHasS2 &&
                  ` · Х2 ${section2InProgress}/${section2Items.length}`}
                {flaggedCount > 0 && ` · ${flaggedCount} тэмдэглэсэн`}
              </div>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <TestTimer
              startTime={session.startedAt}
              durationMs={TEST_DURATION_MS}
              onExpiry={handleAutoSubmit}
            />

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
            {/* Screen body */}
            {currentQuestion && (
              <QuestionCard
                mode="test"
                question={currentQuestion}
                selectedAnswer={
                  answers[currentQuestion.questionNumber] || null
                }
                onSelectAnswer={handleSelectAnswer}
                isFlagged={flagged.includes(currentQuestion.questionNumber)}
                onToggleFlag={handleToggleFlag}
                questionIndex={currentIndex + 1}
              />
            )}
            {currentProblemItems && (
              <Section2Problem
                items={currentProblemItems}
                section2Answers={section2Answers}
                onAnswerChange={handleSection2SlotChange}
              />
            )}

            <div className="flex items-center justify-between mt-4">
              <button
                onClick={handlePrev}
                disabled={currentIndex === 0}
                className="btn btn-line text-[12px]"
                style={
                  currentIndex === 0
                    ? { opacity: 0.4, cursor: "not-allowed" }
                    : {}
                }
              >
                <ArrowLeft className="w-3.5 h-3.5 mr-1" />
                Өмнөх
              </button>

              <span
                className="mono tabular text-[11px]"
                style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}
              >
                {isSection2
                  ? `Хэсэг 2 · ${currentProblemId}`
                  : `${String(currentIndex + 1).padStart(2, "0")} / ${String(totalMcq).padStart(2, "0")}`}
              </span>

              <button
                onClick={handleNext}
                disabled={currentIndex === totalScreens - 1}
                className="btn btn-line text-[12px]"
                style={
                  currentIndex === totalScreens - 1
                    ? { opacity: 0.4, cursor: "not-allowed" }
                    : {}
                }
              >
                Дараах
                <ArrowRight className="w-3.5 h-3.5 ml-1" />
              </button>
            </div>
          </div>

          <div className="hidden lg:block w-64 shrink-0">
            <div className="sticky top-[140px]">
              <QuestionNavigator
                totalQuestions={totalMcq}
                currentIndex={currentIndex}
                answers={answers}
                flagged={flagged}
                onJumpTo={setCurrentIndex}
                section2Items={testHasS2 ? section2Items : undefined}
                section2Answers={section2Answers}
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
            className="absolute bottom-0 left-0 right-0 p-4 rounded-t-2xl max-h-[80vh] overflow-y-auto"
            style={{ background: "var(--bg-1)", borderTop: "1px solid var(--line)" }}
          >
            <QuestionNavigator
              totalQuestions={totalMcq}
              currentIndex={currentIndex}
              answers={answers}
              flagged={flagged}
              onJumpTo={(i) => {
                setCurrentIndex(i);
                setShowNav(false);
              }}
              section2Items={testHasS2 ? section2Items : undefined}
              section2Answers={section2Answers}
            />
          </div>
        </div>
      )}

      {/* Quit modal */}
      {showQuitModal && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center px-4"
          style={{
            background: "color-mix(in oklch, black 50%, transparent)",
            backdropFilter: "blur(8px)",
          }}
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
            <h3
              className="serif"
              style={{
                fontWeight: 400,
                fontSize: 22,
                letterSpacing: "-0.02em",
                color: "var(--fg)",
              }}
            >
              Шалгалтаас{" "}
              <em className="serif-italic" style={{ color: "var(--warn)" }}>
                гарах
              </em>{" "}
              уу?
            </h3>
            <p className="text-[13px] mt-3 mb-6" style={{ color: "var(--fg-2)" }}>
              Таны хариултууд хадгалагдана. Та дараа нь үргэлжлүүлж болно.
            </p>
            <div className="flex gap-2">
              <button
                onClick={() => setShowQuitModal(false)}
                className="btn btn-line flex-1"
              >
                Үргэлжлүүлэх
              </button>
              <button
                onClick={() => {
                  setShowQuitModal(false);
                  router.push("/practice/esh/test");
                }}
                className="btn flex-1"
                style={{
                  background:
                    "color-mix(in oklch, var(--warn) 14%, transparent)",
                  border:
                    "1px solid color-mix(in oklch, var(--warn) 30%, transparent)",
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
          style={{
            background: "color-mix(in oklch, black 50%, transparent)",
            backdropFilter: "blur(8px)",
          }}
        >
          <div
            className="card-edit p-6 max-w-sm w-full max-h-[80vh] overflow-y-auto"
            style={{ background: "var(--bg-1)" }}
          >
            <div className="flex items-center gap-3 mb-3">
              <div
                className="w-10 h-10 rounded-md flex items-center justify-center"
                style={{
                  background: "var(--accent-wash)",
                  border: "1px solid var(--accent-line)",
                  color: "var(--accent)",
                }}
              >
                <Send className="w-5 h-5" />
              </div>
              <div className="eyebrow">Дуусгах</div>
            </div>
            <h3
              className="serif"
              style={{
                fontWeight: 400,
                fontSize: 22,
                letterSpacing: "-0.02em",
                color: "var(--fg)",
              }}
            >
              Шалгалт{" "}
              <em className="serif-italic" style={{ color: "var(--accent)" }}>
                дуусгах
              </em>{" "}
              уу?
            </h3>

            <div className="space-y-2 mt-4 mb-6 text-[13px]">
              <div
                className="flex items-center justify-between"
                style={{ color: "var(--fg-2)" }}
              >
                <span>Хэсэг 1 хариулсан</span>
                <span className="mono tabular" style={{ color: "var(--accent)" }}>
                  {answeredCount}/{totalMcq}
                </span>
              </div>
              {testHasS2 && (
                <div
                  className="flex items-center justify-between"
                  style={{ color: "var(--fg-2)" }}
                >
                  <span>Хэсэг 2 хариулсан</span>
                  <span
                    className="mono tabular"
                    style={{ color: "var(--accent)" }}
                  >
                    {section2Items.length - unansweredSection2.length}/
                    {section2Items.length}
                  </span>
                </div>
              )}
              {unansweredCount > 0 && (
                <div
                  className="flex items-center gap-2 pt-1"
                  style={{ color: "var(--warn)" }}
                >
                  <AlertTriangle className="w-3.5 h-3.5" />
                  <span>{unansweredCount} бодлого хариулаагүй</span>
                </div>
              )}
              {testHasS2 && unansweredSection2.length > 0 && (
                <div className="pt-1" style={{ color: "var(--warn)" }}>
                  <div className="flex items-center gap-2 mb-1">
                    <AlertTriangle className="w-3.5 h-3.5" />
                    <span>Хэсэг 2-т хариулаагүй:</span>
                  </div>
                  <div className="ml-5 mono tabular text-[11px] flex flex-wrap gap-x-2 gap-y-0.5">
                    {unansweredSection2.map((it) => (
                      <span key={it.source}>
                        {it.problem} ({it.subproblem})
                      </span>
                    ))}
                  </div>
                </div>
              )}
              {flaggedCount > 0 && (
                <div
                  className="flex items-center gap-2 pt-1"
                  style={{ color: "var(--warn)" }}
                >
                  <Flag className="w-3.5 h-3.5" />
                  <span>{flaggedCount} бодлого тэмдэглэсэн</span>
                </div>
              )}
            </div>

            <div className="flex gap-2">
              <button
                onClick={() => setShowSubmitModal(false)}
                className="btn btn-line flex-1"
              >
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
