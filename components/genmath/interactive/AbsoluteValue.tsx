"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { type IntegerLineConfig } from "@/lib/genmath-interactive";
import IntegerLineView from "@/components/genmath/interactive/IntegerLineView";

export default function AbsoluteValue({ config }: { config: IntegerLineConfig }) {
  const { min, max, start, color = "#e8913c" } = config;
  const [v, setV] = useState(Math.max(min, Math.min(max, Math.round(start))));
  const abs = Math.abs(v);

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <IntegerLineView min={min} max={max} points={[{ value: v, label: String(v), color }]} highlightFromZero={v} />
      </div>

      <div className="mt-2 flex flex-wrap items-center justify-center gap-2.5">
        <span className="serif tabular" style={{ fontSize: 22, color: "var(--fg)" }}>|{v}|</span>
        <span style={{ color: "var(--fg-3)" }}>=</span>
        <span className="serif tabular rounded-lg px-3 py-1" style={{ fontSize: 22, background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)" }}>{abs}</span>
      </div>
      <div className="mt-1 text-center text-[12.5px]" style={{ color: "var(--fg-2)" }}>
        the distance from <b className="serif tabular" style={{ color: "var(--fg-1)" }}>{v}</b> to <b className="serif tabular" style={{ color: "var(--fg-1)" }}>0</b>
      </div>

      <div className="mt-4 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={() => setV((x) => Math.max(min, x - 1))}
          disabled={v <= min}
          aria-label="Move left"
          className="gm-press grid h-12 w-12 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <Minus className="h-5 w-5" />
        </button>
        <div className="text-center" style={{ minWidth: 56 }}>
          <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>move</div>
        </div>
        <button
          type="button"
          onClick={() => setV((x) => Math.min(max, x + 1))}
          disabled={v >= max}
          aria-label="Move right"
          className="gm-press grid h-12 w-12 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          <Plus className="h-5 w-5" />
        </button>
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        Move past zero — a number and its opposite are the <b style={{ color: "var(--fg-1)" }}>same distance</b> from 0.
      </div>
    </div>
  );
}
