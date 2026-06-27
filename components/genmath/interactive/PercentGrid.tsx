"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { type PercentGridConfig } from "@/lib/genmath-interactive";
import DecimalGridView from "@/components/genmath/interactive/DecimalGridView";

export default function PercentGrid({ config }: { config: PercentGridConfig }) {
  const { start = 0, color = "#e8913c" } = config;
  const [p, setP] = useState(Math.max(0, Math.min(100, Math.round(start))));
  const decimal = (p / 100).toFixed(2);

  const step = (d: number) => setP((v) => Math.max(0, Math.min(100, v + d)));

  const Stepper = ({ label, sub, d }: { label: string; sub: string; d: number }) => (
    <div className="flex items-center gap-2.5">
      <button
        type="button"
        onClick={() => step(-d)}
        disabled={p - d < 0}
        aria-label={`Less ${label}`}
        className="gm-press grid h-11 w-11 place-items-center rounded-full disabled:opacity-35"
        style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
      >
        <Minus className="h-4 w-4" />
      </button>
      <div className="text-center" style={{ minWidth: 64 }}>
        <div className="serif tabular" style={{ fontSize: 18, color: "var(--fg)" }}>{label}</div>
        <div className="text-[10px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>{sub}</div>
      </div>
      <button
        type="button"
        onClick={() => step(d)}
        disabled={p + d > 100}
        aria-label={`More ${label}`}
        className="gm-press grid h-11 w-11 place-items-center rounded-full disabled:opacity-35"
        style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
      >
        <Plus className="h-4 w-4" />
      </button>
    </div>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <DecimalGridView hundredths={p} color={color} />
      </div>
      <div className="mt-2 text-center text-[12px]" style={{ color: "var(--fg-2)" }}>
        100 squares = 100% = one whole
      </div>

      {/* percent = fraction = decimal */}
      <div className="mt-3 flex flex-wrap items-center justify-center gap-2.5">
        <span className="serif tabular rounded-lg px-3 py-1" style={{ fontSize: 24, background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)" }}>{p}%</span>
        <span style={{ color: "var(--fg-3)" }}>=</span>
        <span className="serif tabular" style={{ fontSize: 22, color: "var(--fg)" }}>{p}/100</span>
        <span style={{ color: "var(--fg-3)" }}>=</span>
        <span className="serif tabular" style={{ fontSize: 22, color: "var(--fg)" }}>{decimal}</span>
      </div>

      <div className="mt-4 flex flex-wrap items-center justify-center gap-x-6 gap-y-3">
        <Stepper label="ten" sub="+10%" d={10} />
        <Stepper label="one" sub="+1%" d={1} />
      </div>
    </div>
  );
}
