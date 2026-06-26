"use client";

import { useState } from "react";
import { RotateCcw, Check } from "lucide-react";
import { type FractionSimplifyConfig } from "@/lib/genmath-interactive";
import FractionBar from "@/components/genmath/interactive/FractionBar";

// Smallest factor > 1 that divides both, or 1 if already in simplest form.
function smallestCommonFactor(a: number, b: number): number {
  const lim = Math.min(a, b);
  for (let d = 2; d <= lim; d++) {
    if (a % d === 0 && b % d === 0) return d;
  }
  return 1;
}

export default function FractionSimplify({ config }: { config: FractionSimplifyConfig }) {
  const { num: num0, den: den0, color = "#3fb27f" } = config;
  const [num, setNum] = useState(num0);
  const [den, setDen] = useState(den0);

  const factor = smallestCommonFactor(num, den);
  const simplest = factor === 1;

  const combine = () => {
    if (factor > 1) {
      setNum(num / factor);
      setDen(den / factor);
    }
  };
  const reset = () => {
    setNum(num0);
    setDen(den0);
  };
  const changed = num !== num0 || den !== den0;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <FractionBar num={num} den={den} color={color} />
      <div className="mt-2 text-center text-[12px]" style={{ color: "var(--fg-2)" }}>
        {den} pieces, {num} shaded
      </div>

      {/* readout */}
      <div className="mt-3 flex items-center justify-center gap-2">
        <span className="serif tabular" style={{ fontSize: 24, color: simplest ? "var(--accent)" : "var(--fg)" }}>
          {num}/{den}
        </span>
        {simplest && changed && (
          <span className="gm-pop inline-flex items-center gap-1 rounded-full px-2.5 py-0.5 text-[12px] font-medium" style={{ background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)" }}>
            <Check className="h-3.5 w-3.5" /> simplest form
          </span>
        )}
      </div>

      {/* status line */}
      <div className="mt-2 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        {simplest ? (
          <>No number divides {num} and {den} — you cannot make bigger pieces.</>
        ) : (
          <>Both {num} and {den} can be divided by <b style={{ color: "var(--fg-1)" }}>{factor}</b> — merge the pieces.</>
        )}
      </div>

      {/* controls */}
      <div className="mt-4 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={combine}
          disabled={simplest}
          className="gm-press inline-flex items-center gap-2 rounded-full px-5 py-3 text-[14px] font-medium disabled:opacity-35"
          style={{ background: simplest ? "var(--bg-2)" : "var(--accent)", color: simplest ? "var(--fg-2)" : "var(--accent-ink, #fff)", border: "1px solid var(--accent)" }}
        >
          Merge into bigger pieces {!simplest && `(÷${factor})`}
        </button>
        {changed && (
          <button
            type="button"
            onClick={reset}
            aria-label="Reset"
            className="gm-press grid h-11 w-11 place-items-center rounded-full"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <RotateCcw className="h-4 w-4" />
          </button>
        )}
      </div>
    </div>
  );
}
