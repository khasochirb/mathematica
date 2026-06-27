import MathText from "@/components/esh/MathText";
import type { LessonFact } from "@/lib/lesson-types";

// A formula / key-fact card: title, formula, plain-language explanation.
export default function FactCard({ fact }: { fact: LessonFact }) {
  return (
    <div className="card-edit p-5">
      <p className="serif mb-2" style={{ fontWeight: 400, fontSize: 14, color: "var(--accent)" }}>
        {fact.title}
      </p>
      <div className="q-math text-[15px] mb-2" style={{ color: "var(--fg)" }}>
        <MathText text={fact.latex} />
      </div>
      <p className="text-[13px] leading-relaxed" style={{ color: "var(--fg-2)" }}>
        <MathText text={fact.explanation} />
      </p>
    </div>
  );
}
