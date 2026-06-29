"use client";

import { useState } from "react";
import { Minus, Plus, Check, X } from "lucide-react";
import { type FactorPairsConfig } from "@/lib/genmath-interactive";

// Arrange n squares into rows of `cols`. When cols divides n evenly the squares
// fill a complete rectangle (cols × n/cols) — a factor pair. Otherwise the last
// row is short, showing cols is not a factor.
export default function FactorPairs({ config }: { config: FactorPairsConfig }) {
  const { n, color = "#e8913c" } = config;
  const [cols, setCols] = useState(1);
  const divides = n % cols === 0;
  const rows = Math.ceil(n / cols);
  const other = n / cols;
  const cell = Math.max(14, Math.min(28, Math.round(260 / cols)));

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <div style={{ display: "grid", gridTemplateColumns: `repeat(${cols}, ${cell}px)`, gap: 3 }}>
          {Array.from({ length: n }).map((_, i) => (
            <div
              key={i}
              style={{
                width: cell,
                height: cell,
                borderRadius: 4,
                background: divides ? color : `${color}99`,
                border: "1px solid rgba(0,0,0,0.12)",
              }}
            />
          ))}
        </div>
      </div>

      <div className="mt-3 text-center">
        {divides ? (
          <span className="inline-flex items-center gap-1.5 text-[14px]" style={{ color: "var(--fg-1)" }}>
            <Check className="h-4 w-4" style={{ color: "var(--accent)" }} />
            <b className="serif tabular">{cols} × {other} = {n}</b> — a factor pair
          </span>
        ) : (
          <span className="inline-flex items-center gap-1.5 text-[14px]" style={{ color: "var(--fg-1)" }}>
            <X className="h-4 w-4" style={{ color: "rgb(200,60,60)" }} />
            <span>{n} ÷ {cols} leaves a remainder — {cols} is not a factor</span>
          </span>
        )}
      </div>

      <div className="mt-4 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={() => setCols((c) => Math.max(1, c - 1))}
          disabled={cols <= 1}
          aria-label="Fewer columns"
          className="gm-press grid h-11 w-11 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <Minus className="h-4 w-4" />
        </button>
        <div className="text-center" style={{ minWidth: 96 }}>
          <div className="serif tabular" style={{ fontSize: 18, color: "var(--fg)" }}>{cols} wide</div>
          <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>columns</div>
        </div>
        <button
          type="button"
          onClick={() => setCols((c) => Math.min(n, c + 1))}
          disabled={cols >= n}
          aria-label="More columns"
          className="gm-press grid h-11 w-11 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          <Plus className="h-4 w-4" />
        </button>
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        A width that makes a <b style={{ color: "var(--fg-1)" }}>complete rectangle</b> is a factor of {n}.
      </div>
    </div>
  );
}
