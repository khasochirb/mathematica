"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { type PercentBarConfig } from "@/lib/genmath-interactive";
import PercentBarView from "@/components/genmath/interactive/PercentBarView";

export default function PercentBar({ config }: { config: PercentBarConfig }) {
  const { whole, start = 0, color = "#e8913c" } = config;
  const [p, setP] = useState(Math.max(0, Math.min(100, Math.round(start))));
  const value = Math.round((p / 100) * whole * 100) / 100;
  const fmt = (x: number) => (Number.isInteger(x) ? String(x) : x.toFixed(2).replace(/0+$/, "").replace(/\.$/, ""));

  const step = (d: number) => setP((v) => Math.max(0, Math.min(100, v + d)));

  const Stepper = ({ d, sub }: { d: number; sub: string }) => (
    <div className="flex items-center gap-2.5">
      <button
        type="button"
        onClick={() => step(-d)}
        disabled={p - d < 0}
        aria-label={`Less ${sub}`}
        className="gm-press grid h-11 w-11 place-items-center rounded-full disabled:opacity-35"
        style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
      >
        <Minus className="h-4 w-4" />
      </button>
      <div className="text-center" style={{ minWidth: 48 }}>
        <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>{sub}</div>
      </div>
      <button
        type="button"
        onClick={() => step(d)}
        disabled={p + d > 100}
        aria-label={`More ${sub}`}
        className="gm-press grid h-11 w-11 place-items-center rounded-full disabled:opacity-35"
        style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
      >
        <Plus className="h-4 w-4" />
      </button>
    </div>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-6" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <PercentBarView whole={whole} percent={p} color={color} />
      </div>

      <div className="mt-4 flex flex-wrap items-center justify-center gap-2">
        <span className="serif tabular rounded-lg px-3 py-1" style={{ fontSize: 20, background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)" }}>{p}%</span>
        <span className="text-[15px]" style={{ color: "var(--fg-2)" }}>of</span>
        <span className="serif tabular" style={{ fontSize: 20, color: "var(--fg)" }}>{fmt(whole)}</span>
        <span style={{ color: "var(--fg-3)" }}>=</span>
        <span className="serif tabular" style={{ fontSize: 22, color: "var(--fg)" }}>{fmt(value)}</span>
      </div>

      <div className="mt-4 flex flex-wrap items-center justify-center gap-x-6 gap-y-3">
        <Stepper d={10} sub="±10%" />
        <Stepper d={5} sub="±5%" />
      </div>
    </div>
  );
}
