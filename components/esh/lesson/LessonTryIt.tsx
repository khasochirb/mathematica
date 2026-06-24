"use client";

import Link from "next/link";
import { ArrowRight } from "lucide-react";
import RevealProblemCard from "@/components/lesson/RevealProblemCard";
import { type Lesson, selectTryItQuestions } from "@/lib/esh-lessons";
import { getFreeQuestions } from "@/lib/esh-questions";

const LABELS = { reveal: "Шийд", hide: "Нуух", revealAria: "Шийд харах", hideAria: "Шийдийг нуух" };

// ЭЕШ adapter: pulls try-it questions from the free question bank by skill_tag,
// renders each via the shared reveal card, plus the "practice more" deep-link.
export default function LessonTryIt({ lesson }: { lesson: Lesson }) {
  const pool = getFreeQuestions();
  const questions = selectTryItQuestions(lesson, pool);

  return (
    <div className="space-y-3">
      {questions.map((q, i) => (
        <RevealProblemCard
          key={q.source}
          index={i}
          problem={{ id: q.source, statement: q.body, solution: q.solution }}
          labels={LABELS}
        />
      ))}

      <Link
        href={`/practice/esh/practice?topic=${lesson.tryIt.topic}&mode=topic`}
        className="card-edit p-5 flex items-center gap-4 group"
        style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
      >
        <div className="flex-1">
          <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>Цааш нь</div>
          <p className="serif" style={{ fontWeight: 400, fontSize: 18, color: "var(--fg)" }}>
            Энэ сэдвээр <em className="serif-italic" style={{ color: "var(--accent)" }}>илүү дадлага</em> хийх
          </p>
        </div>
        <ArrowRight className="w-5 h-5 flex-shrink-0" style={{ color: "var(--accent)" }} />
      </Link>
    </div>
  );
}
