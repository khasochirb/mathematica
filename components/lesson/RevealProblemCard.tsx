"use client";

import { useState } from "react";
import { Eye, EyeOff } from "lucide-react";
import MathText from "@/components/esh/MathText";
import type { LessonProblem } from "@/lib/lesson-types";

export interface RevealLabels {
  reveal: string;
  hide: string;
  revealAria: string;
  hideAria: string;
}

// A practice/try-it problem with a self-managed reveal toggle for its solution.
// Markup matches the original ЭЕШ try-it card; labels are passed in for i18n.
export default function RevealProblemCard({
  problem,
  index,
  labels,
}: {
  problem: LessonProblem;
  index: number;
  labels: RevealLabels;
}) {
  const [open, setOpen] = useState(false);
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
    </div>
  );
}
