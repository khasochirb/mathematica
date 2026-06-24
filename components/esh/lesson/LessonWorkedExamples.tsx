"use client";

import MathText from "@/components/esh/MathText";
import EshFigure from "@/components/esh/EshFigure";
import { type Lesson, resolveWorkedExamples } from "@/lib/esh-lessons";

const TIER_LABEL: Record<string, string> = { easy: "хялбар", medium: "дунд", hard: "хүнд" };

export default function LessonWorkedExamples({ lesson }: { lesson: Lesson }) {
  const examples = resolveWorkedExamples(lesson);
  return (
    <div className="space-y-3">
      {examples.map(({ question, teachingNote }, i) => (
        <div key={question.source} className="card-edit p-5">
          <div className="flex items-center gap-2 mb-3">
            <span className="mono text-[10px]" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
              {String(i + 1).padStart(2, "0")}
            </span>
            {question.difficulty_tier && (
              <span className="badge-edit" style={{ background: "var(--bg-2)" }}>
                {TIER_LABEL[question.difficulty_tier] ?? question.difficulty_tier}
              </span>
            )}
            <span className="badge-edit mono" style={{ background: "var(--bg-2)" }}>
              {question.skill_tag}
            </span>
          </div>
          {question.figure && <EshFigure {...question.figure} />}
          <div className="q-math text-[15px] mb-3" style={{ color: "var(--fg)" }}>
            <MathText text={question.body} />
          </div>
          {teachingNote && (
            <p className="text-[14px] leading-relaxed mb-3" style={{ color: "var(--fg-1)" }}>
              <MathText text={teachingNote} />
            </p>
          )}
          <div className="q-math text-[14px] pt-3" style={{ color: "var(--fg-1)", borderTop: "1px solid var(--line)" }}>
            <MathText text={question.solution} />
          </div>
        </div>
      ))}
    </div>
  );
}
