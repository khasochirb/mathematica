"use client";

import { useMemo, useState } from "react";
import useScrollToTop from "@/lib/use-scroll-to-top";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Check, X, Layers, Flag } from "lucide-react";
import MathText from "@/components/esh/MathText";
import GeoDiagram from "@/components/genmath/interactive/GeoDiagram";
import TestTimer from "@/components/esh/TestTimer";
import { useAuth } from "@/lib/auth-context";
import {
  scoreExam,
  saveExamResult,
  type CourseExam,
  type ExamAnswers,
} from "@/lib/course-exam";

// A course exam is a SITTING, not a drill: no per-question feedback while the
// paper is open, free navigation between questions, and one submit. Feedback
// arrives all at once at the end, organised by unit — which is the whole
// reason to sit a full-course paper rather than more bank problems.

export default function ExamRunner({ exam }: { exam: CourseExam }) {
  const { user } = useAuth();
  const n = exam.questions.length;

  const [answers, setAnswers] = useState<ExamAnswers>(() => Array(n).fill(null));
  const [flagged, setFlagged] = useState<Set<number>>(() => new Set());
  // The sitting clock starts when the paper opens. meta.minutes is the real
  // allotment, not advice: TestTimer counts it down and auto-submits at zero,
  // so an exam can never run longer than its time limit.
  const [startedAt] = useState(() => Date.now());
  const [at, setAt] = useState(0);
  useScrollToTop(at);
  const [submitted, setSubmitted] = useState(false);

  const q = exam.questions[at];
  const answeredCount = answers.filter((a) => a !== null).length;
  const summary = useMemo(
    () => (submitted ? scoreExam(exam, answers) : null),
    [submitted, exam, answers],
  );

  function choose(i: number) {
    if (submitted) return;
    setAnswers((prev) => {
      const next = [...prev];
      next[at] = next[at] === i ? null : i; // tap again to clear
      return next;
    });
  }

  function toggleFlag() {
    setFlagged((prev) => {
      const next = new Set(prev);
      if (next.has(at)) next.delete(at);
      else next.add(at);
      return next;
    });
  }

  function submit() {
    const s = scoreExam(exam, answers);
    setSubmitted(true);
    setAt(0);
    if (user?.id) {
      saveExamResult(user.id, {
        examId: exam.meta.examId,
        course: exam.meta.course,
        correct: s.correct,
        total: s.total,
        takenAt: Date.now(),
      });
    }
  }

  // ---------------------------------------------------------------- results
  if (submitted && summary) {
    const pct = Math.round(summary.accuracy * 100);
    return (
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        <div className="eyebrow mb-2">{exam.meta.courseTitle}</div>
        <h1
          className="serif"
          style={{ fontWeight: 400, fontSize: "clamp(28px,4.5vw,44px)", letterSpacing: "-0.03em", color: "var(--fg)" }}
        >
          {exam.meta.label} — Result
        </h1>

        <div className="card-edit p-5 mt-6 mb-8">
          <div className="flex items-baseline gap-3">
            <span className="mono tabular" style={{ fontSize: 34, color: "var(--accent)" }}>
              {summary.correct}/{summary.total}
            </span>
            <span className="mono tabular" style={{ fontSize: 18, color: "var(--fg-2)" }}>
              {pct}%
            </span>
          </div>
          {summary.blank > 0 && (
            <p className="text-[13px] mt-2" style={{ color: "var(--fg-2)" }}>
              {summary.blank} question{summary.blank === 1 ? "" : "s"} left blank. Running out of
              time is a pacing problem, not a understanding problem — worth separating from the
              ones you answered wrong.
            </p>
          )}
        </div>

        <div className="eyebrow mb-3">By unit</div>
        <ul className="space-y-2 mb-8">
          {summary.units.map((u) => {
            const weak = summary.weakest.some((w) => w.unit === u.unit);
            return (
              <li
                key={u.unit}
                className="card-edit p-4 flex items-center justify-between gap-4"
                style={weak ? { borderColor: "var(--accent-line)" } : undefined}
              >
                <Link
                  href={`/math/${exam.meta.course}/${u.unit}`}
                  className="text-[15px] flex-1"
                  style={{ color: "var(--fg)", textDecoration: "none" }}
                >
                  {u.unitTitle}
                </Link>
                <span className="mono tabular text-[13px]" style={{ color: weak ? "var(--accent)" : "var(--fg-2)" }}>
                  {u.correct}/{u.total}
                </span>
              </li>
            );
          })}
        </ul>

        {summary.weakest.length > 0 && (
          <div className="card-edit p-5 mb-8" style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}>
            <div className="eyebrow mb-2" style={{ color: "var(--accent)" }}>
              Start here
            </div>
            <p className="text-[14px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
              Weakest first: <strong>{summary.weakest[0].unitTitle}</strong>. Re-read the unit, then
              drill it in the problem bank — that pairing fixes a unit faster than re-sitting the
              whole paper.
            </p>
            <div className="flex gap-3 mt-4 flex-wrap">
              <Link className="btn btn-primary" href={`/math/${exam.meta.course}/${summary.weakest[0].unit}`}>
                Review the unit
              </Link>
              <Link
                className="btn btn-line"
                href={`/math/problem-bank/${exam.meta.course}/${summary.weakest[0].unit}`}
              >
                Drill it
              </Link>
            </div>
          </div>
        )}

        <div className="eyebrow mb-3">Every question</div>
        <ol className="space-y-4">
          {exam.questions.map((eq, i) => {
            const a = answers[i];
            const ok = a === eq.correctIndex;
            return (
              <li key={eq.id} className="card-edit p-5">
                <div className="flex items-start gap-3 mb-2">
                  <span className="mono text-[11px] tabular mt-1" style={{ color: "var(--fg-3)", minWidth: 24 }}>
                    {String(i + 1).padStart(2, "0")}
                  </span>
                  <span className="flex-1 q-math">
                    <MathText text={eq.statement} />
                  </span>
                  {a === null ? (
                    <span className="mono text-[10px] uppercase mt-1" style={{ color: "var(--fg-3)" }}>
                      blank
                    </span>
                  ) : ok ? (
                    <Check className="w-4 h-4 mt-1" style={{ color: "var(--accent)" }} />
                  ) : (
                    <X className="w-4 h-4 mt-1" style={{ color: "var(--fg-2)" }} />
                  )}
                </div>
                {eq.geoFigure && (
                  <div className="my-3">
                    <GeoDiagram spec={eq.geoFigure} />
                  </div>
                )}
                <p className="text-[13px] mb-1" style={{ color: "var(--fg-2)" }}>
                  Correct answer: <span className="q-math"><MathText text={eq.options[eq.correctIndex]} /></span>
                </p>
                <p className="text-[13px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
                  <MathText text={eq.explanation} />
                </p>
              </li>
            );
          })}
        </ol>

        <div className="flex gap-3 mt-8 flex-wrap">
          <Link className="btn btn-line" href={`/math/${exam.meta.course}`}>
            Back to the course
          </Link>
        </div>
      </div>
    );
  }

  // ----------------------------------------------------------------- sitting
  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
      <div className="flex items-center gap-3 mb-4">
        <Link
          className="p-2 rounded-md transition-colors"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          href={`/math/${exam.meta.course}`}
        >
          <ArrowLeft className="w-4 h-4" />
        </Link>
        <div className="eyebrow">{exam.meta.label}</div>
      </div>

      <div className="flex items-center gap-4 mb-6 flex-wrap text-[12px]" style={{ color: "var(--fg-2)" }}>
        <span className="flex items-center gap-1.5">
          <Layers className="w-3.5 h-3.5" /> {exam.meta.unitsCovered} units
        </span>
        <TestTimer
          startTime={startedAt}
          durationMs={exam.meta.minutes * 60 * 1000}
          onExpiry={submit}
        />
        <span className="mono tabular">
          {answeredCount}/{n} answered
        </span>
      </div>

      {/* question navigator — free movement, so pacing is the student's call */}
      <div className="flex flex-wrap gap-1.5 mb-6">
        {exam.questions.map((_, i) => {
          const done = answers[i] !== null;
          const here = i === at;
          return (
            <button
              key={i}
              onClick={() => setAt(i)}
              aria-label={`Question ${i + 1}`}
              className="mono text-[10px] tabular rounded"
              style={{
                width: 26,
                height: 26,
                border: `1px solid ${here ? "var(--accent)" : "var(--line)"}`,
                background: done ? "var(--accent-wash)" : "transparent",
                color: here ? "var(--accent)" : "var(--fg-2)",
                fontWeight: here ? 700 : 400,
                outline: flagged.has(i) ? "2px solid var(--accent-line)" : undefined,
              }}
            >
              {i + 1}
            </button>
          );
        })}
      </div>

      <div className="card-edit p-6">
        <div className="flex items-center justify-between mb-3">
          <span className="eyebrow">
            Question {at + 1} · {q.unitTitle}
          </span>
          <button
            onClick={toggleFlag}
            className="flex items-center gap-1.5 mono text-[10px] uppercase px-2 py-1 rounded"
            style={{
              border: "1px solid var(--line)",
              color: flagged.has(at) ? "var(--accent)" : "var(--fg-3)",
            }}
          >
            <Flag className="w-3 h-3" /> {flagged.has(at) ? "Flagged" : "Flag"}
          </button>
        </div>

        <div className="q-math mb-4" style={{ fontSize: 16, color: "var(--fg)" }}>
          <MathText text={q.statement} />
        </div>

        {q.geoFigure && (
          <div className="mb-5">
            <GeoDiagram spec={q.geoFigure} />
          </div>
        )}

        <div className="space-y-2">
          {q.options.map((opt, i) => {
            const chosen = answers[at] === i;
            return (
              <button
                key={i}
                onClick={() => choose(i)}
                className="w-full text-left p-3 rounded-md transition-colors flex items-center gap-3"
                style={{
                  border: `1px solid ${chosen ? "var(--accent)" : "var(--line)"}`,
                  background: chosen ? "var(--accent-wash)" : "transparent",
                }}
              >
                <span
                  className="mono text-[11px] rounded-sm flex items-center justify-center flex-shrink-0"
                  style={{
                    width: 22,
                    height: 22,
                    border: `1px solid ${chosen ? "var(--accent)" : "var(--line)"}`,
                    color: chosen ? "var(--accent)" : "var(--fg-3)",
                  }}
                >
                  {"ABCD"[i]}
                </span>
                <span className="q-math" style={{ fontSize: 15, color: "var(--fg)" }}>
                  <MathText text={opt} />
                </span>
              </button>
            );
          })}
        </div>
      </div>

      <div className="flex items-center justify-between gap-3 mt-6">
        <button
          className="btn btn-line"
          onClick={() => setAt((i) => Math.max(0, i - 1))}
          disabled={at === 0}
          style={at === 0 ? { opacity: 0.4 } : undefined}
        >
          <ArrowLeft className="w-4 h-4" /> Previous
        </button>
        {at < n - 1 ? (
          <button className="btn btn-primary" onClick={() => setAt((i) => Math.min(n - 1, i + 1))}>
            Next <ArrowRight className="w-4 h-4" />
          </button>
        ) : (
          <button className="btn btn-primary" onClick={submit}>
            Submit exam
          </button>
        )}
      </div>

      {at === n - 1 && answeredCount < n && (
        <p className="text-[13px] mt-4" style={{ color: "var(--fg-2)" }}>
          {n - answeredCount} question{n - answeredCount === 1 ? "" : "s"} still blank. You can jump
          back using the numbers above before submitting.
        </p>
      )}
    </div>
  );
}
