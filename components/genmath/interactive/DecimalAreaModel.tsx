"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { type DecimalAreaConfig } from "@/lib/genmath-interactive";
import DecimalAreaView from "@/components/genmath/interactive/DecimalAreaView";

export default function DecimalAreaModel({ config }: { config: DecimalAreaConfig }) {
  const { a: a0, b: b0, color = "#e8913c" } = config;
  const [a, setA] = useState(Math.max(1, Math.min(9, Math.round(a0 * 10))));
  const [b, setB] = useState(Math.max(1, Math.min(9, Math.round(b0 * 10))));
  const overlap = a * b;
  const product = (overlap / 100).toFixed(2);

  const Stepper = ({ label, val, set, sub }: { label: string; val: number; set: (f: (v: number) => number) => void; sub: string }) => (
    <div className="flex items-center gap-2">
      <button
        type="button"
        onClick={() => set((v) => Math.max(1, v - 1))}
        disabled={val <= 1}
        aria-label={`Less ${label}`}
        className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35"
        style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
      >
        <Minus className="h-4 w-4" />
      </button>
      <div className="text-center" style={{ minWidth: 56 }}>
        <div className="serif tabular" style={{ fontSize: 18, color: "var(--fg)" }}>{(val / 10).toFixed(1)}</div>
        <div className="text-[10px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>{sub}</div>
      </div>
      <button
        type="button"
        onClick={() => set((v) => Math.min(9, v + 1))}
        disabled={val >= 9}
        aria-label={`More ${label}`}
        className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35"
        style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
      >
        <Plus className="h-4 w-4" />
      </button>
    </div>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <DecimalAreaView aTenths={a} bTenths={b} color={color} />
      </div>

      <div className="mt-3 flex flex-wrap items-center justify-center gap-2.5">
        <span className="serif tabular" style={{ fontSize: 22, color: "var(--fg)" }}>{(a / 10).toFixed(1)}</span>
        <span style={{ color: "var(--fg-3)" }}>×</span>
        <span className="serif tabular" style={{ fontSize: 22, color: "var(--fg)" }}>{(b / 10).toFixed(1)}</span>
        <span style={{ color: "var(--fg-3)" }}>=</span>
        <span className="serif tabular rounded-lg px-3 py-1" style={{ fontSize: 22, background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)" }}>{product}</span>
      </div>

      <div className="mt-1 text-center text-[12px]" style={{ color: "var(--fg-2)" }}>
        the overlap is <b style={{ color: "var(--fg-1)" }}>{overlap}</b> of 100 squares = {product}
      </div>

      <div className="mt-4 flex flex-wrap items-center justify-center gap-x-6 gap-y-3">
        <Stepper label="width" val={a} set={setA} sub="across" />
        <Stepper label="height" val={b} set={setB} sub="up" />
      </div>
    </div>
  );
}
