"use client";

import { usePathname } from "next/navigation";
import RevealProblemCard, { type RevealLabels } from "@/components/lesson/RevealProblemCard";
import usePerformance from "@/lib/use-performance";
import { contextFromPathname } from "@/lib/perf-context";
import type { LessonProblem } from "@/lib/lesson-types";

// The course practice/test bank list, upgraded from pure self-check to
// self-GRADED: after revealing a solution the student reports whether they
// had it right, and that report lands in the attempt stream under the
// course's context. One usePerformance instance for the whole list — the
// cards stay dumb.
//
// Honesty note: these are self-reported, same trust model as flashcard
// grading. They live in course contexts only, so they can never touch the
// ЭЕШ exam stats.
export default function GradedProblemList({
  problems,
  labels,
  kind,
}: {
  problems: LessonProblem[];
  labels: RevealLabels;
  kind: "practice" | "test";
}) {
  const pathname = usePathname();
  const perf = usePerformance();

  const recordFor = (problem: LessonProblem) => (correct: boolean) => {
    const context = contextFromPathname(pathname ?? "");
    if (!context) return;
    const unit = (pathname ?? "").split("/").filter(Boolean)[2] ?? "";
    perf.recordAttempt({
      questionSource: `bank:${unit}/${problem.id}`,
      topic: unit,
      subtopic: kind,
      selectedAnswer: correct ? "self:correct" : "self:incorrect",
      correctAnswer: "self",
      isCorrect: correct,
      source: kind === "test" ? "test" : "drill",
      context,
    });
  };

  return (
    <div className="space-y-3">
      {problems.map((problem, i) => (
        <RevealProblemCard
          key={problem.id}
          problem={problem}
          index={i}
          labels={labels}
          onSelfGrade={recordFor(problem)}
        />
      ))}
    </div>
  );
}
