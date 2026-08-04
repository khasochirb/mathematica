"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { Clock, Layers, FileText, Check, Lock } from "lucide-react";
import { useAuth } from "@/lib/auth-context";
import { useUpgradeModal } from "@/lib/upgrade-modal-context";
import { isExamFree } from "@/lib/course-access";
import { loadExamResult, type CourseExam, type ExamResult } from "@/lib/course-exam";

// The list of a course's exams, with each paper's last score if the student
// has sat it. Client-side because results live in account-keyed localStorage,
// the same place the placement results do — a score written and never read
// back is the feature only half-built.

export default function ExamList({ course, exams }: { course: string; exams: CourseExam[] }) {
  const { user, isSubscribed } = useAuth();
  const { open: openUpgrade } = useUpgradeModal();
  const [results, setResults] = useState<Record<string, ExamResult | null>>({});

  useEffect(() => {
    if (!user?.id) {
      setResults({});
      return;
    }
    const next: Record<string, ExamResult | null> = {};
    for (const e of exams) next[e.meta.examId] = loadExamResult(user.id, e.meta.examId);
    setResults(next);
  }, [user?.id, exams]);

  return (
    <ol className="space-y-3">
      {exams.map((e, i) => {
        const r = results[e.meta.examId];
        const pct = r ? Math.round((r.correct / r.total) * 100) : null;
        // Paper 1 is the free sample; the rest are Premium.
        const locked = !isSubscribed && !isExamFree(e.meta.examId);
        const inner = (
          <>
              <span
                className="mono text-[11px] flex-shrink-0 tabular mt-1"
                style={{ color: "var(--accent)", letterSpacing: "0.04em", minWidth: 24 }}
              >
                {String(i + 1).padStart(2, "0")}
              </span>
              <span className="flex-1 min-w-0">
                <span
                  className="serif block"
                  style={{ fontWeight: 400, fontSize: 18, letterSpacing: "-0.01em", color: "var(--fg)" }}
                >
                  {e.meta.label}
                </span>
                <span className="flex gap-4 mt-2 text-[12px] flex-wrap" style={{ color: "var(--fg-2)" }}>
                  <span className="flex items-center gap-1.5">
                    <FileText className="w-3.5 h-3.5" /> {e.meta.totalQuestions} questions
                  </span>
                  <span className="flex items-center gap-1.5">
                    <Layers className="w-3.5 h-3.5" /> {e.meta.unitsCovered} units
                  </span>
                  <span className="flex items-center gap-1.5">
                    <Clock className="w-3.5 h-3.5" /> ~{e.meta.minutes} min
                  </span>
                </span>
              </span>
              {r ? (
                <span className="flex flex-col items-end flex-shrink-0 mt-1">
                  <span className="mono tabular text-[13px]" style={{ color: "var(--accent)" }}>
                    {r.correct}/{r.total}
                  </span>
                  <span className="mono text-[10px] tabular" style={{ color: "var(--fg-3)" }}>
                    {pct}%
                  </span>
                  <span className="flex items-center gap-1 mono text-[9px] uppercase mt-1" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                    <Check className="w-2.5 h-2.5" /> Sat
                  </span>
                </span>
              ) : (
                <span
                  className="mono text-[10px] uppercase mt-1 flex-shrink-0"
                  style={{ color: "var(--accent)", letterSpacing: "0.08em" }}
                >
                  Start
                </span>
              )}
          </>
        );
        return (
          <li key={e.meta.examId}>
            {locked ? (
              <button
                type="button"
                onClick={() => openUpgrade({ source: "course_exam_lock" })}
                className="card-edit p-5 flex items-start gap-4 transition-colors relative w-full text-left"
              >
                <span
                  className="absolute top-3 right-3 inline-flex items-center gap-1 mono uppercase rounded-full px-1.5 py-[2px]"
                  style={{
                    fontSize: 9,
                    letterSpacing: "0.08em",
                    background: "color-mix(in oklch, var(--warn) 12%, transparent)",
                    border: "1px solid color-mix(in oklch, var(--warn) 40%, transparent)",
                    color: "var(--warn, #d89620)",
                  }}
                >
                  <Lock style={{ width: 9, height: 9 }} /> Premium
                </span>
                <span className="flex items-start gap-4 flex-1" style={{ opacity: 0.55 }}>
                  {inner}
                </span>
              </button>
            ) : (
              <Link
                className="card-edit p-5 flex items-start gap-4 transition-colors"
                style={{ textDecoration: "none" }}
                href={`/math/${course}/exam/${e.meta.examId}`}
              >
                {inner}
              </Link>
            )}
          </li>
        );
      })}
    </ol>
  );
}
