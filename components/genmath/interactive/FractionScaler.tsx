"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { type FractionScalerConfig } from "@/lib/genmath-interactive";
import FractionBar from "@/components/genmath/interactive/FractionBar";

export default function FractionScaler({ config }: { config: FractionScalerConfig }) {
  const { num, den, maxSplit, color = "#e8913c" } = config;
  const [n, setN] = useState(1);
  const sNum = num * n;
  const sDen = den * n;

  const dec = () => setN((v) => Math.max(1, v - 1));
  const inc = () => setN((v) => Math.min(maxSplit, v + 1));

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      {/* the bar — shaded width never changes, only the number of pieces */}
      <FractionBar num={sNum} den={sDen} color={color} />

      <div className="mt-2 text-center text-[12px]" style={{ color: "var(--fg-2)" }}>
        {n === 1 ? "the whole, in " + den + " pieces" : `each piece split into ${n} → ${sDen} pieces`}
      </div>

      {/* equivalence readout */}
      <div className="mt-3 flex items-center justify-center gap-3">
        <span className="serif tabular" style={{ fontSize: 22, color: "var(--fg)" }}>
          {num}/{den}
        </span>
        <span style={{ color: "var(--fg-3)" }}>=</span>
        <span
          className="serif tabular rounded-lg px-3 py-1"
          style={{ fontSize: 22, background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)" }}
        >
          {sNum}/{sDen}
        </span>
      </div>

      {/* stepper */}
      <div className="mt-4 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={dec}
          disabled={n <= 1}
          aria-label="Fewer pieces"
          className="gm-press grid h-12 w-12 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <Minus className="h-5 w-5" />
        </button>
        <div className="text-center" style={{ minWidth: 110 }}>
          <div className="serif tabular" style={{ fontSize: 22, color: "var(--fg)" }}>
            × {n}
          </div>
          <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>
            top &amp; bottom
          </div>
        </div>
        <button
          type="button"
          onClick={inc}
          disabled={n >= maxSplit}
          aria-label="More pieces"
          className="gm-press grid h-12 w-12 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          <Plus className="h-5 w-5" />
        </button>
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        Same shaded amount — just more pieces. That is an <b style={{ color: "var(--fg-1)" }}>equivalent fraction</b>.
      </div>
    </div>
  );
}
