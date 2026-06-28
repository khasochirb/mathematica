"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { type IntegerLineConfig } from "@/lib/genmath-interactive";
import IntegerLineView from "@/components/genmath/interactive/IntegerLineView";

export default function IntegerLine({ config }: { config: IntegerLineConfig }) {
  const { min, max, start, color = "#e8913c" } = config;
  const [v, setV] = useState(Math.max(min, Math.min(max, Math.round(start))));
  const sign = v > 0 ? "positive" : v < 0 ? "negative" : "zero";

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <IntegerLineView min={min} max={max} points={[{ value: v, label: String(v), color }]} />
      </div>

      <div className="mt-2 flex flex-wrap items-center justify-center gap-2.5">
        <span className="serif tabular rounded-lg px-3 py-1" style={{ fontSize: 24, background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)" }}>{v}</span>
        <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
          is {sign === "zero" ? <b style={{ color: "var(--fg-1)" }}>zero</b> : <>a <b style={{ color: "var(--fg-1)" }}>{sign}</b> integer</>}
        </span>
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
        <div className="text-center" style={{ minWidth: 64 }}>
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
        Left of zero is <b style={{ color: "var(--fg-1)" }}>negative</b>; right of zero is <b style={{ color: "var(--fg-1)" }}>positive</b>.
      </div>
    </div>
  );
}
