"use client";

import { useState } from "react";
import { Plus, Minus } from "lucide-react";
import {
  type RatioTableConfig,
  simplifyRatio,
  formatRatio,
} from "@/lib/genmath-interactive";

// A single column in the table: top value (tokenA) over bottom value (tokenB).
function RatioColumn({
  k,
  a,
  b,
  colorA,
  colorB,
  isNew,
}: {
  k: number;
  a: number;
  b: number;
  colorA: string;
  colorB: string;
  isNew: boolean;
}) {
  return (
    <div
      className={`flex shrink-0 flex-col items-center gap-1 ${isNew ? "gm-pop" : ""}`}
      style={{ minWidth: 68 }}
    >
      {/* Multiplier label */}
      <div
        className="rounded-full px-2 py-0.5 text-[11px] font-medium uppercase tracking-wide"
        style={{
          background: "var(--accent-wash)",
          color: "var(--accent)",
          border: "1px solid var(--accent-line)",
        }}
      >
        ×{k}
      </div>

      {/* Top value (tokenA) */}
      <div
        className="grid w-full place-items-center rounded-xl py-3"
        style={{
          background: colorA + "22",
          border: `1.5px solid ${colorA}55`,
          minHeight: 56,
        }}
      >
        <span
          className="serif tabular"
          style={{ fontSize: 26, lineHeight: 1, color: "var(--fg)" }}
        >
          {a}
        </span>
      </div>

      {/* Divider line — visually separates the two rows */}
      <div style={{ height: 2, width: "70%", background: "var(--line)", borderRadius: 1 }} />

      {/* Bottom value (tokenB) */}
      <div
        className="grid w-full place-items-center rounded-xl py-3"
        style={{
          background: colorB + "22",
          border: `1.5px solid ${colorB}55`,
          minHeight: 56,
        }}
      >
        <span
          className="serif tabular"
          style={{ fontSize: 26, lineHeight: 1, color: "var(--fg)" }}
        >
          {b}
        </span>
      </div>
    </div>
  );
}

export default function RatioTable({ config }: { config: RatioTableConfig }) {
  const [visibleCols, setVisibleCols] = useState(1);
  const { a, b, tokenA, tokenB, maxCols } = config;
  const [sa, sb] = simplifyRatio(a, b);

  const canAdd = visibleCols < maxCols;
  const canRemove = visibleCols > 1;

  return (
    <div
      className="rounded-2xl p-4 sm:p-5"
      style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}
    >
      {/* Row labels */}
      <div className="mb-2 flex items-stretch gap-2">
        {/* Label column — fixed, left-anchored */}
        <div className="flex shrink-0 flex-col gap-1" style={{ minWidth: 72 }}>
          {/* spacer for the ×k badge */}
          <div style={{ height: 24 }} />

          {/* tokenA label */}
          <div
            className="flex items-center justify-end rounded-xl px-2 py-3"
            style={{
              background: "var(--bg-2)",
              border: "1px solid var(--line)",
              minHeight: 56,
              gap: 6,
            }}
          >
            <span
              className="grid shrink-0 place-items-center rounded-md text-[13px]"
              style={{
                width: 22,
                height: 22,
                background: tokenA.color,
                border: "1px solid rgba(0,0,0,0.10)",
              }}
            >
              {tokenA.glyph ?? ""}
            </span>
            <span
              className="text-right text-[12px] leading-tight"
              style={{ color: "var(--fg-2)" }}
            >
              {tokenA.plural}
            </span>
          </div>

          {/* divider spacer */}
          <div style={{ height: 10 }} />

          {/* tokenB label */}
          <div
            className="flex items-center justify-end rounded-xl px-2 py-3"
            style={{
              background: "var(--bg-2)",
              border: "1px solid var(--line)",
              minHeight: 56,
              gap: 6,
            }}
          >
            <span
              className="grid shrink-0 place-items-center rounded-md text-[13px]"
              style={{
                width: 22,
                height: 22,
                background: tokenB.color,
                border: "1px solid rgba(0,0,0,0.10)",
              }}
            >
              {tokenB.glyph ?? ""}
            </span>
            <span
              className="text-right text-[12px] leading-tight"
              style={{ color: "var(--fg-2)" }}
            >
              {tokenB.plural}
            </span>
          </div>
        </div>

        {/* Scrollable columns */}
        <div className="min-w-0 flex-1 overflow-x-auto">
          <div className="flex gap-2 pb-1" style={{ minWidth: "max-content" }}>
            {Array.from({ length: visibleCols }).map((_, i) => {
              const k = i + 1;
              return (
                <RatioColumn
                  key={k}
                  k={k}
                  a={a * k}
                  b={b * k}
                  colorA={tokenA.color}
                  colorB={tokenB.color}
                  isNew={k === visibleCols && k > 1}
                />
              );
            })}
          </div>
        </div>
      </div>

      {/* Controls: − remove / + add column */}
      <div className="mt-3 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={() => setVisibleCols((v) => Math.max(1, v - 1))}
          disabled={!canRemove}
          aria-label="Remove column"
          className="gm-press grid h-11 w-11 place-items-center rounded-full disabled:opacity-30"
          style={{
            background: "var(--bg-2)",
            border: "1px solid var(--line)",
            color: "var(--fg-2)",
          }}
        >
          <Minus className="h-4 w-4" />
        </button>

        <button
          type="button"
          onClick={() => setVisibleCols((v) => Math.min(maxCols, v + 1))}
          disabled={!canAdd}
          aria-label="Add column"
          className="gm-press flex items-center gap-2 rounded-full px-5 py-2.5 text-[14px] font-medium disabled:opacity-30"
          style={{
            background: "var(--accent)",
            color: "var(--accent-ink, #fff)",
            border: "1px solid var(--accent)",
            minHeight: 44,
          }}
        >
          <Plus className="h-4 w-4" />
          add column
        </button>
      </div>

      {/* Ratio readout */}
      <div
        className="mt-4 flex flex-wrap items-center justify-center gap-2 rounded-xl p-3 text-center"
        style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}
      >
        <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
          Every column shows the same ratio
        </span>
        <span
          className="serif tabular"
          style={{ fontSize: 20, color: "var(--fg)", letterSpacing: "-0.01em" }}
        >
          {formatRatio(a, b)}
        </span>
        {(sa !== a || sb !== b) && (
          <span
            className="rounded-full px-2.5 py-0.5 text-[12px]"
            style={{
              background: "var(--accent-wash)",
              color: "var(--accent)",
              border: "1px solid var(--accent-line)",
            }}
          >
            = {formatRatio(sa, sb)} simplified
          </span>
        )}
      </div>
    </div>
  );
}
