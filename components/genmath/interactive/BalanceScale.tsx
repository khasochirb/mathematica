"use client";

import { useState } from "react";
import { RotateCcw } from "lucide-react";
import { type BalanceScaleConfig } from "@/lib/genmath-interactive";

// A pan balance that models a one-step equation. The two pans stay level because
// the sides are equal. Doing the same thing to both sides keeps the balance:
//  - add mode:  x + b = rhs  →  "remove b from both"  →  x = rhs − b
//  - mul mode:  a·x = rhs    →  "split both into a groups"  →  x = rhs ÷ a
export default function BalanceScale({ config }: { config: BalanceScaleConfig }) {
  const { mode, coef = 1, b = 0, rhs, color = "#e8913c" } = config;
  const [solved, setSolved] = useState(false);

  const answer = mode === "add" ? rhs - b : Math.round(rhs / coef);
  const actionLabel = mode === "add" ? `Subtract ${b} from both sides` : `Divide both sides by ${coef}`;
  const equation = mode === "add"
    ? `x + ${b} = ${rhs}`
    : `${coef === 1 ? "" : coef}x = ${rhs}`;

  const XBox = () => (
    <span className="serif grid place-items-center" style={{ width: 40, height: 30, borderRadius: 6, background: color, color: "#fff", fontStyle: "italic", fontSize: 15 }}>x</span>
  );
  const Weight = () => (
    <span style={{ width: 18, height: 18, borderRadius: "50%", background: "var(--fg-2)", display: "inline-block" }} />
  );

  // What sits on each pan, depending on mode and whether we've solved.
  let leftXs = 0, leftWeights = 0, rightWeights = 0;
  if (mode === "add") {
    leftXs = 1;
    leftWeights = solved ? 0 : b;
    rightWeights = solved ? rhs - b : rhs;
  } else {
    leftXs = solved ? 1 : coef;
    rightWeights = solved ? Math.round(rhs / coef) : rhs;
  }

  const Pan = ({ xs, weights }: { xs: number; weights: number }) => (
    <div className="flex-1 rounded-xl p-2.5 flex flex-wrap items-center justify-center gap-1.5" style={{ minHeight: 56, background: "var(--bg-2)", border: "1px solid var(--line)" }}>
      {Array.from({ length: xs }).map((_, i) => <XBox key={`x${i}`} />)}
      {Array.from({ length: weights }).map((_, i) => <Weight key={`w${i}`} />)}
    </div>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="text-center serif tabular" style={{ fontSize: 20, color: "var(--fg)" }}>{equation}</div>

      {/* Beam + pans */}
      <div className="mt-4 flex items-stretch gap-3">
        <Pan xs={leftXs} weights={leftWeights} />
        <div className="grid place-items-center px-1">
          <span className="serif" style={{ fontSize: 22, color: "var(--fg-3)" }}>=</span>
        </div>
        <Pan xs={0} weights={rightWeights} />
      </div>
      {/* Fulcrum */}
      <div className="mt-1 flex justify-center">
        <div style={{ width: 0, height: 0, borderLeft: "10px solid transparent", borderRight: "10px solid transparent", borderBottom: "12px solid var(--line)" }} />
      </div>

      <div className="mt-3 flex items-center justify-center gap-2 text-[12px]" style={{ color: "var(--fg-3)" }}>
        <span className="inline-flex items-center gap-1.5"><span style={{ width: 14, height: 11, borderRadius: 3, background: color, display: "inline-block" }} /> = x (unknown)</span>
        <span className="inline-flex items-center gap-1.5"><span style={{ width: 12, height: 12, borderRadius: "50%", background: "var(--fg-2)", display: "inline-block" }} /> = 1</span>
      </div>

      <div className="mt-4 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={() => setSolved(false)}
          disabled={!solved}
          aria-label="Reset"
          className="gm-press inline-flex items-center gap-1.5 rounded-full px-4 py-2.5 text-[14px] disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <RotateCcw className="h-4 w-4" /> Reset
        </button>
        <button
          type="button"
          onClick={() => setSolved(true)}
          disabled={solved}
          className="gm-press rounded-full px-5 py-2.5 text-[14px] disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          {actionLabel}
        </button>
      </div>

      {solved && (
        <div className="mt-4 rounded-xl p-3 text-center text-[15px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
          <b className="serif tabular" style={{ color: "var(--accent)" }}>x = {answer}</b>
        </div>
      )}

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        Do the <b style={{ color: "var(--fg-1)" }}>same thing to both sides</b> and the balance is kept.
      </div>
    </div>
  );
}
