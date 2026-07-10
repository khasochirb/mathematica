"use client";

import { useState } from "react";
import { Check, Eye, EyeOff, X } from "lucide-react";
import MathText from "@/components/esh/MathText";
import { useLang } from "@/lib/lang-context";
import type { LessonProblem } from "@/lib/lesson-types";

export interface RevealLabels {
  reveal: string;
  hide: string;
  revealAria: string;
  hideAria: string;
}

const SELF_GRADE = {
  en: { ask: "Did you solve it correctly?", yes: "Got it right", no: "Missed it", thanks_right: "Recorded — nice work.", thanks_wrong: "Recorded — this one counts toward your weak spots." },
  mn: { ask: "Та зөв бодсон уу?", yes: "Зөв бодсон", no: "Алдсан", thanks_right: "Бүртгэлээ — сайн байна.", thanks_wrong: "Бүртгэлээ — энэ сул талдаа тооцогдоно." },
};

// A practice/try-it problem with a self-managed reveal toggle for its solution.
// Markup matches the original ЭЕШ try-it card; labels are passed in for i18n.
//
// When `onSelfGrade` is provided, revealing the solution asks the student to
// self-grade ("worked example" reveals never do — pass no handler there).
// The answer fires once and is reported up for the attempt stream.
export default function RevealProblemCard({
  problem,
  index,
  labels,
  onSelfGrade,
}: {
  problem: LessonProblem;
  index: number;
  labels: RevealLabels;
  onSelfGrade?: (correct: boolean) => void;
}) {
  const [open, setOpen] = useState(false);
  const [graded, setGraded] = useState<boolean | null>(null);
  const { lang } = useLang();
  const G = SELF_GRADE[lang === "mn" ? "mn" : "en"];

  const grade = (correct: boolean) => {
    if (graded !== null) return;
    setGraded(correct);
    onSelfGrade?.(correct);
  };

  return (
    <div className="card-edit p-5">
      <div className="flex items-start justify-between gap-3">
        <div className="q-math text-[15px]" style={{ color: "var(--fg)" }}>
          <span className="mono text-[11px] mr-2" style={{ color: "var(--fg-3)" }}>
            {String(index + 1).padStart(2, "0")}
          </span>
          <MathText text={problem.statement} />
        </div>
        <button
          type="button"
          onClick={() => setOpen((v) => !v)}
          className="btn btn-line flex-shrink-0 text-[12px]"
          aria-label={open ? labels.hideAria : labels.revealAria}
        >
          {open ? <EyeOff className="mr-1 h-3.5 w-3.5" /> : <Eye className="mr-1 h-3.5 w-3.5" />}
          {open ? labels.hide : labels.reveal}
        </button>
      </div>
      {open && (
        <div
          className="q-math text-[14px] mt-3 pt-3"
          style={{ color: "var(--fg-1)", borderTop: "1px solid var(--line)" }}
        >
          <MathText text={problem.solution} />
        </div>
      )}
      {open && onSelfGrade && (
        <div className="mt-3 pt-3" style={{ borderTop: "1px solid var(--line)" }}>
          {graded === null ? (
            <div className="flex flex-wrap items-center gap-2">
              <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
                {G.ask}
              </span>
              <button
                type="button"
                onClick={() => grade(true)}
                className="gm-press inline-flex items-center gap-1 rounded-full px-3 py-1.5 text-[12px]"
                style={{ background: "rgba(63,178,127,0.12)", border: "1px solid rgba(63,178,127,0.5)", color: "#2f9e6e" }}
              >
                <Check className="h-3.5 w-3.5" /> {G.yes}
              </button>
              <button
                type="button"
                onClick={() => grade(false)}
                className="gm-press inline-flex items-center gap-1 rounded-full px-3 py-1.5 text-[12px]"
                style={{ background: "rgba(215,80,63,0.08)", border: "1px solid rgba(215,80,63,0.4)", color: "rgb(200,60,60)" }}
              >
                <X className="h-3.5 w-3.5" /> {G.no}
              </button>
            </div>
          ) : (
            <p className="text-[12px]" style={{ color: "var(--fg-3)" }}>
              {graded ? G.thanks_right : G.thanks_wrong}
            </p>
          )}
        </div>
      )}
    </div>
  );
}
