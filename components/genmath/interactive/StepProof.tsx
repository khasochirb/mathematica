"use client";

import { useState } from "react";
import { RotateCcw, Check } from "lucide-react";
import MathText from "@/components/esh/MathText";
import { type StepProofConfig } from "@/lib/genmath-interactive";

// A two-column proof revealed one row at a time: statement on the left, the
// reason that justifies it underneath. The gentle on-ramp to deduction —
// introduced at the end of Unit 1 and the workhorse of Unit 2 onward.
export default function StepProof({ config }: { config: StepProofConfig }) {
  const { given, prove, rows } = config;
  const [shown, setShown] = useState(0);
  const done = shown >= rows.length;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      {/* Given / Prove header */}
      <div className="flex flex-col gap-2">
        <div className="rounded-xl px-4 py-2.5" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
          <span className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>Given&nbsp;&nbsp;</span>
          <span className="q-math text-[14px]" style={{ color: "var(--fg)" }}>
            <MathText text={given} />
          </span>
        </div>
        <div className="rounded-xl px-4 py-2.5" style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)" }}>
          <span className="text-[11px] uppercase tracking-wide" style={{ color: "var(--accent)" }}>Prove&nbsp;&nbsp;</span>
          <span className="q-math text-[14px]" style={{ color: "var(--fg)" }}>
            <MathText text={prove} />
          </span>
        </div>
      </div>

      {/* Revealed rows */}
      <div className="mt-4 flex flex-col gap-2.5">
        {rows.slice(0, shown).map((row, i) => {
          const isCurrent = i === shown - 1;
          return (
            <div
              key={i}
              className="rounded-xl px-4 py-3"
              style={{
                background: "var(--bg-2)",
                border: isCurrent ? "1px solid var(--accent)" : "1px solid var(--line)",
              }}
            >
              <div className="flex items-start gap-3">
                <span
                  className="mt-0.5 grid h-6 w-6 flex-shrink-0 place-items-center rounded-full text-[11px]"
                  style={{ background: "var(--accent-wash)", color: "var(--accent)" }}
                >
                  {i + 1}
                </span>
                <div className="min-w-0">
                  <div className="q-math text-[14px]" style={{ color: "var(--fg)" }}>
                    <MathText text={row.statement} />
                  </div>
                  <div className="mt-1 text-[12.5px]" style={{ color: "var(--fg-2)", fontStyle: "italic" }}>
                    <MathText text={row.reason} />
                  </div>
                </div>
              </div>
            </div>
          );
        })}
        {shown === 0 && (
          <div className="rounded-xl px-4 py-5 text-center text-[13px]" style={{ border: "1px dashed var(--line)", color: "var(--fg-3)" }}>
            Each step states a fact — and names the <i>reason</i> we know it.
          </div>
        )}
      </div>

      {/* Controls */}
      <div className="mt-4 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={() => setShown(0)}
          disabled={shown === 0}
          aria-label="Reset proof"
          className="gm-press inline-flex items-center gap-1.5 rounded-full px-4 py-2.5 text-[14px] disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <RotateCcw className="h-4 w-4" /> Reset
        </button>
        <button
          type="button"
          onClick={() => setShown((v) => Math.min(rows.length, v + 1))}
          disabled={done}
          className="gm-press inline-flex items-center gap-1.5 rounded-full px-5 py-2.5 text-[14px] disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          Next step
        </button>
      </div>

      {done && (
        <div className="mt-3 flex items-center justify-center gap-1.5 text-[14px]" style={{ color: "var(--accent)" }}>
          <Check className="h-4 w-4" /> Proof complete <span className="serif">∎</span>
        </div>
      )}
    </div>
  );
}
