"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Check } from "lucide-react";
import MathText from "@/components/esh/MathText";
import WorkedExampleCard from "@/components/lesson/WorkedExampleCard";
import RevealProblemCard from "@/components/lesson/RevealProblemCard";
import StepProgress from "@/components/genmath/interactive/StepProgress";
import QuantityScaler from "@/components/genmath/interactive/QuantityScaler";
import OrderFlip from "@/components/genmath/interactive/OrderFlip";
import CompareToggle from "@/components/genmath/interactive/CompareToggle";
import TapQuestion from "@/components/genmath/interactive/TapQuestion";
import { type GenMathLesson } from "@/lib/genmath-lessons";
import { type InteractiveStep, getLessonProblem } from "@/lib/genmath-interactive";

const REVEAL = { reveal: "Show solution", hide: "Hide", revealAria: "Show solution", hideAria: "Hide solution" };

function StepHeader({ eyebrow, title }: { eyebrow?: string; title: string }) {
  return (
    <div className="mb-4">
      {eyebrow && (
        <div className="eyebrow mb-1.5" style={{ color: "var(--accent)" }}>
          {eyebrow}
        </div>
      )}
      <h2
        className="serif"
        style={{ fontWeight: 400, fontSize: "clamp(24px, 5vw, 34px)", lineHeight: 1.08, letterSpacing: "-0.03em", color: "var(--fg)" }}
      >
        {title}
      </h2>
    </div>
  );
}

function StepBody({ lesson, step }: { lesson: GenMathLesson; step: InteractiveStep }) {
  switch (step.kind) {
    case "concept":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <p className="font-sans" style={{ fontSize: 17, lineHeight: 1.6, color: "var(--fg-1)" }}>
            <MathText text={step.body} />
          </p>
        </>
      );
    case "scaler":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <QuantityScaler config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "orderFlip":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <OrderFlip config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "compareToggle":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <CompareToggle config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "tapQuestion":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <TapQuestion
            prompt={step.prompt}
            options={step.options}
            correctIndex={step.correctIndex}
            explanation={step.explanation}
          />
        </>
      );
    case "worked": {
      const p = getLessonProblem(lesson, step.problemId);
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          {p ? <WorkedExampleCard problem={p} index={0} /> : null}
        </>
      );
    }
    case "tryIt": {
      const p = getLessonProblem(lesson, step.problemId);
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          {p ? <RevealProblemCard problem={p} index={0} labels={REVEAL} /> : null}
        </>
      );
    }
    case "recap":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <ul className="space-y-2.5">
            {step.points.map((pt, i) => (
              <li key={i} className="flex items-start gap-2.5">
                <span
                  className="mt-0.5 grid h-5 w-5 flex-shrink-0 place-items-center rounded-full"
                  style={{ background: "var(--accent-wash)", color: "var(--accent)" }}
                >
                  <Check className="h-3 w-3" />
                </span>
                <span className="font-sans" style={{ fontSize: 16, lineHeight: 1.5, color: "var(--fg-1)" }}>
                  <MathText text={pt} />
                </span>
              </li>
            ))}
          </ul>
        </>
      );
  }
}

export default function LessonPlayer({
  lesson,
  topicSlug,
  topicTitle,
}: {
  lesson: GenMathLesson;
  topicSlug: string;
  topicTitle: string;
}) {
  const steps = lesson.interactive?.steps ?? [];
  const [i, setI] = useState(0);
  const total = steps.length;
  const isLast = i >= total - 1;
  const topicHref = `/math/6/${topicSlug}`;

  if (total === 0) return null;

  return (
    <div className="flex min-h-screen flex-col pt-20" style={{ background: "var(--bg)" }}>
      {/* Top bar: exit + lesson title + progress */}
      <div
        className="sticky top-16 z-10"
        style={{ background: "var(--bg)", borderBottom: "1px solid var(--line)" }}
      >
        <div className="mx-auto max-w-2xl px-4 py-3 sm:px-6">
          <div className="mb-2.5 flex items-center gap-3">
            <Link
              href={topicHref}
              aria-label="Exit lesson"
              className="gm-press grid h-8 w-8 place-items-center rounded-md"
              style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
            >
              <ArrowLeft className="h-4 w-4" />
            </Link>
            <div className="min-w-0">
              <div className="eyebrow truncate">General Math · Grade 6 · {topicTitle}</div>
              <div className="serif truncate" style={{ fontSize: 15, color: "var(--fg)" }}>
                {lesson.title}
              </div>
            </div>
            <span className="mono ml-auto text-[11px]" style={{ color: "var(--fg-3)" }}>
              {i + 1}/{total}
            </span>
          </div>
          <StepProgress total={total} current={i} onJump={(j) => setI(j)} />
        </div>
      </div>

      {/* Step content (re-keyed so it animates in on every step change) */}
      <main className="flex-1">
        <div key={i} className="gm-step mx-auto max-w-2xl px-4 py-8 sm:px-6">
          <StepBody lesson={lesson} step={steps[i]} />
        </div>
      </main>

      {/* Bottom nav */}
      <div
        className="sticky bottom-0 z-10"
        style={{ background: "var(--bg)", borderTop: "1px solid var(--line)" }}
      >
        <div className="mx-auto flex max-w-2xl items-center gap-3 px-4 py-3 sm:px-6">
          <button
            type="button"
            onClick={() => setI((v) => Math.max(0, v - 1))}
            disabled={i === 0}
            className="gm-press inline-flex items-center gap-1.5 rounded-full px-4 py-3 text-[14px] disabled:opacity-35"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
          >
            <ArrowLeft className="h-4 w-4" /> Back
          </button>
          {isLast ? (
            <Link
              href={topicHref}
              className="gm-press ml-auto inline-flex items-center gap-1.5 rounded-full px-6 py-3 text-[14px]"
              style={{ background: "var(--accent)", color: "var(--accent-ink, #fff)" }}
            >
              <Check className="h-4 w-4" /> Finish lesson
            </Link>
          ) : (
            <button
              type="button"
              onClick={() => setI((v) => Math.min(total - 1, v + 1))}
              className="gm-press ml-auto inline-flex items-center gap-1.5 rounded-full px-6 py-3 text-[14px]"
              style={{ background: "var(--accent)", color: "var(--accent-ink, #fff)" }}
            >
              Continue <ArrowRight className="h-4 w-4" />
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
