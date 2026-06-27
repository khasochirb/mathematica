"use client";

import { useState } from "react";
import { ArrowRight, RotateCcw } from "lucide-react";
import { type DecimalDivideConfig, divideShift } from "@/lib/genmath-interactive";

const fmt = (x: number) => x.toFixed(6).replace(/0+$/, "").replace(/\.$/, "");

export default function DecimalShiftDivide({ config }: { config: DecimalDivideConfig }) {
  const { dividend, divisor, color = "#e8913c" } = config;
  const { shifts, scaledDividend, scaledDivisor, quotient } = divideShift(dividend, divisor);
  const [step, setStep] = useState(0); // 0..shifts shifts, then reveal
  const [revealed, setRevealed] = useState(false);

  const f = Math.pow(10, step);
  const curDividend = Math.round(dividend * f * 1e6) / 1e6;
  const curDivisor = Math.round(divisor * f * 1e6) / 1e6;
  const divisorWhole = step >= shifts;

  const Pair = ({ a, b, accent }: { a: number; b: number; accent?: boolean }) => (
    <span className="serif tabular" style={{ fontSize: 26, color: accent ? color : "var(--fg)" }}>
      {fmt(a)} <span style={{ color: "var(--fg-3)" }}>÷</span> {fmt(b)}
    </span>
  );

  return (
    <div className="rounded-2xl p-5 sm:p-6" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex flex-wrap items-center justify-center gap-3">
        <Pair a={curDividend} b={curDivisor} />
        {revealed && (
          <span className="gm-fade flex items-center gap-2">
            <span style={{ color: "var(--fg-3)" }}>=</span>
            <span className="serif tabular rounded-lg px-3 py-1" style={{ fontSize: 26, background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)" }}>
              {fmt(quotient)}
            </span>
          </span>
        )}
      </div>

      <div className="mt-2 text-center text-[12.5px]" style={{ color: "var(--fg-2)" }}>
        {divisorWhole
          ? revealed
            ? `the divisor is whole — divide normally`
            : `the divisor ${fmt(curDivisor)} is a whole number — ready to divide`
          : `multiply both by 10 to make the divisor whole`}
      </div>

      <div className="mt-4 flex justify-center gap-2.5">
        {!divisorWhole ? (
          <button
            type="button"
            onClick={() => setStep((s) => Math.min(shifts, s + 1))}
            className="gm-press inline-flex items-center gap-2 rounded-full px-5 py-2.5 text-[14px]"
            style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
          >
            Shift both ×10 <ArrowRight className="h-4 w-4" />
          </button>
        ) : !revealed ? (
          <button
            type="button"
            onClick={() => setRevealed(true)}
            className="gm-press inline-flex items-center gap-2 rounded-full px-5 py-2.5 text-[14px]"
            style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
          >
            Divide
          </button>
        ) : (
          <button
            type="button"
            onClick={() => { setStep(0); setRevealed(false); }}
            className="gm-press inline-flex items-center gap-1.5 rounded-full px-4 py-2 text-[13px]"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <RotateCcw className="h-3.5 w-3.5" /> Reset
          </button>
        )}
      </div>

      {revealed && (
        <div className="gm-fade mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
          Scaling both by the same amount keeps the answer the same:{" "}
          <b className="serif tabular" style={{ color: "var(--fg-1)" }}>
            {fmt(dividend)} ÷ {fmt(divisor)} = {fmt(scaledDividend)} ÷ {fmt(scaledDivisor)} = {fmt(quotient)}
          </b>
        </div>
      )}
    </div>
  );
}
