"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowRight, Eye, EyeOff } from "lucide-react";
import MathText from "@/components/esh/MathText";
import { type Lesson, selectTryItQuestions } from "@/lib/esh-lessons";
import { getQuestionsByTopicForUser } from "@/lib/esh-questions";

export default function LessonTryIt({ lesson }: { lesson: Lesson }) {
  const pool = getQuestionsByTopicForUser(lesson.tryIt.topic, false);
  const questions = selectTryItQuestions(lesson, pool);
  const [revealed, setRevealed] = useState<Record<string, boolean>>({});

  return (
    <div className="space-y-3">
      {questions.map((q, i) => {
        const open = !!revealed[q.source];
        return (
          <div key={q.source} className="card-edit p-5">
            <div className="flex items-start justify-between gap-3">
              <div className="q-math text-[15px]" style={{ color: "var(--fg)" }}>
                <span className="mono text-[11px] mr-2" style={{ color: "var(--fg-3)" }}>
                  {String(i + 1).padStart(2, "0")}
                </span>
                <MathText text={q.body} />
              </div>
              <button
                type="button"
                onClick={() => setRevealed((r) => ({ ...r, [q.source]: !open }))}
                className="btn btn-line flex-shrink-0 text-[12px]"
                aria-label={open ? "Шийдийг нуух" : "Шийд харах"}
              >
                {open ? <EyeOff className="mr-1 h-3.5 w-3.5" /> : <Eye className="mr-1 h-3.5 w-3.5" />}
                {open ? "Нуух" : "Шийд"}
              </button>
            </div>
            {open && (
              <div className="q-math text-[14px] mt-3 pt-3" style={{ color: "var(--fg-1)", borderTop: "1px solid var(--line)" }}>
                <MathText text={q.solution} />
              </div>
            )}
          </div>
        );
      })}

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
