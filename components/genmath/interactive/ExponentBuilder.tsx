"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { type ExponentBuilderConfig } from "@/lib/genmath-interactive";

// Shows a power as repeated multiplication: pick a base and an exponent, and the
// expansion base × base × … (exponent copies) and its value appear. Makes "the
// exponent counts how many times the base is multiplied" concrete.
export default function ExponentBuilder({ config }: { config: ExponentBuilderConfig }) {
  const { base: b0, exp: e0, minBase = 2, maxBase = 6, minExp = 1, maxExp = 5, color = "#e8913c" } = config;
  const [base, setBase] = useState(b0);
  const [exp, setExp] = useState(e0);
  const value = Math.pow(base, exp);

  const Stepper = ({ label, val, set, lo, hi }: { label: string; val: number; set: (f: (v: number) => number) => void; lo: number; hi: number }) => (
    <div className="flex items-center gap-2">
      <button
        type="button"
        onClick={() => set((v) => Math.max(lo, v - 1))}
        disabled={val <= lo}
        aria-label={`Decrease ${label}`}
        className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35"
        style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
      >
        <Minus className="h-4 w-4" />
      </button>
      <div className="serif tabular text-center" style={{ minWidth: 36, fontSize: 20, color: "var(--fg)" }}>{val}</div>
      <button
        type="button"
        onClick={() => set((v) => Math.min(hi, v + 1))}
        disabled={val >= hi}
        aria-label={`Increase ${label}`}
        className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35"
        style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
      >
        <Plus className="h-4 w-4" />
      </button>
    </div>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      {/* Power notation */}
      <div className="flex items-end justify-center gap-1">
        <span className="serif tabular" style={{ fontSize: 40, color: "var(--fg)", lineHeight: 1 }}>{base}</span>
        <span className="serif tabular" style={{ fontSize: 24, color: "var(--accent)", lineHeight: 1, position: "relative", top: -14 }}>{exp}</span>
      </div>
      <div className="mt-1 text-center text-[12px]" style={{ color: "var(--fg-3)" }}>
        base <b style={{ color: "var(--fg-2)" }}>{base}</b>, exponent <b style={{ color: "var(--accent)" }}>{exp}</b>
      </div>

      {/* Expansion */}
      <div className="mt-4 flex flex-wrap items-center justify-center gap-1.5">
        {Array.from({ length: exp }).map((_, i) => (
          <span key={i} className="flex items-center gap-1.5">
            <span
              className="serif tabular grid place-items-center"
              style={{ width: 38, height: 38, borderRadius: 8, background: color, color: "#fff", fontSize: 16 }}
            >
              {base}
            </span>
            {i < exp - 1 && <span style={{ color: "var(--fg-3)" }}>×</span>}
          </span>
        ))}
      </div>

      <div className="mt-4 rounded-xl p-3 text-center text-[15px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        <span className="serif tabular">{base}</span>
        <sup className="serif tabular" style={{ fontSize: "0.7em", color: "var(--accent)" }}>{exp}</sup>
        {" = "}
        <span className="serif tabular">{Array.from({ length: exp }).map(() => base).join(" × ")}</span>
        {" = "}
        <b className="serif tabular" style={{ color: "var(--accent)" }}>{value.toLocaleString("en-US")}</b>
      </div>

      <div className="mt-4 flex items-center justify-around gap-3">
        <div className="text-center">
          <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>base</div>
          <div className="mt-1"><Stepper label="base" val={base} set={setBase} lo={minBase} hi={maxBase} /></div>
        </div>
        <div className="text-center">
          <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>exponent</div>
          <div className="mt-1"><Stepper label="exponent" val={exp} set={setExp} lo={minExp} hi={maxExp} /></div>
        </div>
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        The exponent tells you <b style={{ color: "var(--fg-1)" }}>how many times</b> to multiply the base.
      </div>
    </div>
  );
}
