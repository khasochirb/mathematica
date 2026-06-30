"use client";

import { useState } from "react";
import { type EvaluatorConfig } from "@/lib/genmath-interactive";

// A substitution machine. Drag the slider to choose a value for the variable and
// watch the expression a·x + b get its value: the variable is replaced
// everywhere, then the arithmetic is done. Makes "evaluate = plug in and
// compute" tangible.
function fmtExpr(a: number, b: number, name: string): string {
  const aPart = a === 1 ? name : `${a}${name}`;
  if (b === 0) return aPart;
  return `${aPart} ${b < 0 ? "−" : "+"} ${Math.abs(b)}`;
}

export default function Evaluator({ config }: { config: EvaluatorConfig }) {
  const { a, b, varName = "x", min = 0, max = 10, start, color = "#e8913c" } = config;
  const [v, setV] = useState(start ?? min);
  const value = a * v + b;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="text-center serif tabular" style={{ fontSize: 26, color: "var(--fg)" }}>
        {fmtExpr(a, b, varName)}
      </div>

      {/* Substitution line */}
      <div className="mt-4 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <div className="text-[13px]" style={{ color: "var(--fg-2)" }}>
          when <span className="serif" style={{ fontStyle: "italic", color: "var(--accent)" }}>{varName}</span> ={" "}
          <b className="serif tabular" style={{ color: "var(--accent)" }}>{v}</b>
        </div>
        <div className="mt-2 serif tabular" style={{ fontSize: 18, color: "var(--fg)" }}>
          {a === 1 ? "" : `${a} × `}
          <span style={{ color: "var(--accent)" }}>{v}</span>
          {b === 0 ? "" : b < 0 ? ` − ${Math.abs(b)}` : ` + ${b}`}
          {" = "}
          <b style={{ color: "var(--accent)" }}>{value}</b>
        </div>
      </div>

      {/* Slider */}
      <div className="mt-4">
        <input
          type="range"
          min={min}
          max={max}
          value={v}
          onChange={(e) => setV(Number(e.target.value))}
          aria-label={`Value of ${varName}`}
          className="w-full"
          style={{ accentColor: color }}
        />
        <div className="mt-1 flex justify-between text-[11px]" style={{ color: "var(--fg-3)" }}>
          <span>{varName} = {min}</span>
          <span>{varName} = {max}</span>
        </div>
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        <b style={{ color: "var(--fg-1)" }}>Substitute</b> the value for {varName}, then do the arithmetic.
      </div>
    </div>
  );
}
