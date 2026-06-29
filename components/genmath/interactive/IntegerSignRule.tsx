"use client";

import { useState } from "react";
import { type IntegerSignRuleConfig } from "@/lib/genmath-interactive";

// Flip each factor's sign and watch the result's sign follow the rule:
// same signs → positive, different signs → negative (for both × and ÷).
export default function IntegerSignRule({ config }: { config: IntegerSignRuleConfig }) {
  const { a, b, op, color = "#e8913c" } = config;
  const ma = Math.abs(a);
  const mb = Math.abs(b);
  const [sa, setSa] = useState(a < 0 ? -1 : 1);
  const [sb, setSb] = useState(b < 0 ? -1 : 1);

  const valA = sa * ma;
  const valB = sb * mb;
  const result = op === "mul" ? valA * valB : valA / valB;
  const same = sa === sb;
  const opSym = op === "mul" ? "×" : "÷";
  const show = (v: number) => (v < 0 ? `(${v})` : `${v}`);

  const Toggle = ({ sign, set, mag }: { sign: number; set: (f: (s: number) => number) => void; mag: number }) => (
    <button
      type="button"
      onClick={() => set((s) => -s)}
      className="gm-press serif tabular rounded-xl px-4 py-2"
      style={{ fontSize: 24, background: "var(--bg-2)", border: "1px solid var(--line)", color: sign < 0 ? "#3b82f6" : "var(--fg)" }}
      aria-label="Flip sign"
    >
      {sign < 0 ? `−${mag}` : mag}
    </button>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-6" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex flex-wrap items-center justify-center gap-3">
        <Toggle sign={sa} set={setSa} mag={ma} />
        <span className="serif" style={{ fontSize: 22, color: "var(--fg-3)" }}>{opSym}</span>
        <Toggle sign={sb} set={setSb} mag={mb} />
        <span className="serif" style={{ fontSize: 22, color: "var(--fg-3)" }}>=</span>
        <span className="serif tabular rounded-lg px-3 py-1.5" style={{ fontSize: 24, background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)" }}>
          {result}
        </span>
      </div>

      <div className="mt-3 text-center text-[14px]">
        <span className="rounded-full px-3 py-1" style={{ background: same ? "rgba(22,163,74,0.12)" : "rgba(59,130,246,0.12)", color: same ? "#16a34a" : "#3b82f6" }}>
          {same ? "same signs → positive" : "different signs → negative"}
        </span>
      </div>

      <div className="mt-3 text-center text-[12.5px]" style={{ color: "var(--fg-2)" }}>
        Tap a number to flip its sign. The digits {opSym === "×" ? "multiply" : "divide"} the same way;
        only the <b style={{ color: "var(--fg-1)" }}>sign</b> changes.
      </div>
    </div>
  );
}
