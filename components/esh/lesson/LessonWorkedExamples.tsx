"use client";

import WorkedExampleCard from "@/components/lesson/WorkedExampleCard";
import { type Lesson, resolveWorkedExamples } from "@/lib/esh-lessons";
import type { LessonProblem } from "@/lib/lesson-types";

const TIER_LABEL: Record<string, string> = { easy: "хялбар", medium: "дунд", hard: "хүнд" };

// ЭЕШ adapter: resolves worked examples from the question bank and maps each
// into the shared LessonProblem shape, then renders via the shared card.
export default function LessonWorkedExamples({ lesson }: { lesson: Lesson }) {
  const examples = resolveWorkedExamples(lesson);
  return (
    <div className="space-y-3">
      {examples.map(({ question, teachingNote }, i) => {
        const badges: LessonProblem["badges"] = [];
        if (question.difficulty_tier) {
          badges.push({ text: TIER_LABEL[question.difficulty_tier] ?? question.difficulty_tier });
        }
        if (question.skill_tag) {
          badges.push({ text: question.skill_tag, mono: true });
        }
        const problem: LessonProblem = {
          id: question.source,
          statement: question.body,
          solution: question.solution,
          note: teachingNote,
          badges,
          figure: question.figure,
        };
        return <WorkedExampleCard key={question.source} problem={problem} index={i} />;
      })}
    </div>
  );
}
