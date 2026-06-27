import MathText from "@/components/esh/MathText";
import EshFigure from "@/components/esh/EshFigure";
import type { LessonProblem } from "@/lib/lesson-types";

// One worked example: index, badges, optional figure, statement, teaching note, solution.
// Markup matches the original ЭЕШ worked-example card so render is identical across hubs.
export default function WorkedExampleCard({
  problem,
  index,
}: {
  problem: LessonProblem;
  index: number;
}) {
  return (
    <div className="card-edit p-5">
      <div className="flex items-center gap-2 mb-3">
        <span className="mono text-[10px]" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
          {String(index + 1).padStart(2, "0")}
        </span>
        {problem.badges?.map((b, i) => (
          <span
            key={i}
            className={b.mono ? "badge-edit mono" : "badge-edit"}
            style={{ background: "var(--bg-2)" }}
          >
            {b.text}
          </span>
        ))}
      </div>
      {problem.figure && <EshFigure {...problem.figure} />}
      <div className="q-math text-[15px] mb-3" style={{ color: "var(--fg)" }}>
        <MathText text={problem.statement} />
      </div>
      {problem.note && (
        <p className="text-[14px] leading-relaxed mb-3" style={{ color: "var(--fg-1)" }}>
          <MathText text={problem.note} />
        </p>
      )}
      <div
        className="q-math text-[14px] pt-3"
        style={{ color: "var(--fg-1)", borderTop: "1px solid var(--line)" }}
      >
        <MathText text={problem.solution} />
      </div>
    </div>
  );
}
