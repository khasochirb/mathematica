"use client";

import { useState } from "react";
import { Minus, Plus, Check } from "lucide-react";
import {
  type ProportionBuilderConfig,
  proportionMissing,
} from "@/lib/genmath-interactive";

function TokenChips({
  count,
  color,
  glyph,
}: {
  count: number;
  color: string;
  glyph?: string;
}) {
  return (
    <div className="flex flex-wrap content-start gap-1.5" style={{ minHeight: 52 }}>
      {Array.from({ length: count }).map((_, i) => (
        <span
          key={i}
          className="gm-pop grid place-items-center rounded-lg"
          style={{
            width: 26,
            height: 26,
            background: color,
            border: "1px solid rgba(0,0,0,0.10)",
            fontSize: 13,
            lineHeight: 1,
            animationDelay: `${(i % 12) * 28}ms`,
            boxShadow: "0 1px 2px rgba(0,0,0,0.08)",
          }}
        >
          {glyph ?? ""}
        </span>
      ))}
    </div>
  );
}

export default function ProportionBuilder({ config }: { config: ProportionBuilderConfig }) {
  const { aLabel, bLabel, a, b, knownSide, knownValue, tokenA, tokenB } = config;

  const base = knownSide === "a" ? a : b;
  const maxK = Math.round(knownValue / base);

  const [k, setK] = useState(1);

  const scaledA = a * k;
  const scaledB = b * k;
  const knownScaled = knownSide === "a" ? scaledA : scaledB;
  const missingScaled = knownSide === "a" ? scaledB : scaledA;
  const missingToken = knownSide === "a" ? tokenB : tokenA;
  const missingLabel = knownSide === "a" ? bLabel : aLabel;
  const knownToken = knownSide === "a" ? tokenA : tokenB;
  const knownLabel = knownSide === "a" ? aLabel : bLabel;

  const answer = proportionMissing(a, b, knownSide, knownValue);
  const isExact = k === maxK;
  const isOver = k > maxK;

  const dec = () => setK((v) => Math.max(1, v - 1));
  const inc = () => setK((v) => Math.min(maxK, v + 1));

  return (
    <div
      className="rounded-2xl p-4 sm:p-5"
      style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}
    >
      {/* Base ratio banner */}
      <div
        className="mb-4 rounded-xl px-3 py-2.5 text-center text-[13px]"
        style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
      >
        Base ratio:{" "}
        <span className="serif tabular" style={{ fontSize: 15, color: "var(--fg)" }}>
          {a} {aLabel} : {b} {bLabel}
        </span>
      </div>

      {/* Two quantity panels */}
      <div className="grid grid-cols-2 gap-3">
        {/* A side */}
        <div
          className="rounded-xl p-3"
          style={{
            background: "var(--bg-2)",
            border: isExact && knownSide === "a"
              ? "2px solid #3fb27f"
              : "1px solid var(--line)",
            transition: "border-color .25s ease",
          }}
        >
          <div className="flex items-baseline gap-2">
            <span
              className="serif tabular"
              style={{
                fontSize: 30,
                lineHeight: 1,
                color: isExact && knownSide !== "a" ? "#3fb27f" : "var(--fg)",
                transition: "color .2s",
              }}
            >
              {knownSide === "b" && !isExact ? "?" : scaledA}
            </span>
            <span className="text-[12px]" style={{ color: "var(--fg-2)" }}>
              {tokenA.plural}
            </span>
          </div>
          <div className="mt-2.5">
            <TokenChips
              count={knownSide === "a" || isExact ? scaledA : 0}
              color={tokenA.color}
              glyph={tokenA.glyph}
            />
          </div>
        </div>

        {/* B side */}
        <div
          className="rounded-xl p-3"
          style={{
            background: "var(--bg-2)",
            border: isExact && knownSide === "b"
              ? "2px solid #3fb27f"
              : "1px solid var(--line)",
            transition: "border-color .25s ease",
          }}
        >
          <div className="flex items-baseline gap-2">
            <span
              className="serif tabular"
              style={{
                fontSize: 30,
                lineHeight: 1,
                color: isExact && knownSide !== "b" ? "#3fb27f" : "var(--fg)",
                transition: "color .2s",
              }}
            >
              {knownSide === "a" && !isExact ? "?" : scaledB}
            </span>
            <span className="text-[12px]" style={{ color: "var(--fg-2)" }}>
              {tokenB.plural}
            </span>
          </div>
          <div className="mt-2.5">
            <TokenChips
              count={knownSide === "b" || isExact ? scaledB : 0}
              color={tokenB.color}
              glyph={tokenB.glyph}
            />
          </div>
        </div>
      </div>

      {/* Scale factor stepper */}
      <div className="mt-4 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={dec}
          disabled={k <= 1}
          aria-label="Decrease scale"
          className="gm-press grid h-12 w-12 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <Minus className="h-5 w-5" />
        </button>

        <div className="text-center" style={{ minWidth: 96 }}>
          <div className="serif tabular" style={{ fontSize: 26, lineHeight: 1, color: "var(--fg)" }}>
            ×{k}
          </div>
          <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>
            scale
          </div>
        </div>

        <button
          type="button"
          onClick={inc}
          disabled={k >= maxK}
          aria-label="Increase scale"
          className="gm-press grid h-12 w-12 place-items-center rounded-full disabled:opacity-35"
          style={{
            background: "var(--accent)",
            border: "1px solid var(--accent)",
            color: "var(--accent-ink, #fff)",
          }}
        >
          <Plus className="h-5 w-5" />
        </button>
      </div>

      {/* Known-side progress nudge / success */}
      <div
        className="gm-fade mt-4 rounded-xl p-3 text-center text-[13px]"
        style={{
          background: isExact ? "rgba(63,178,127,0.10)" : "var(--bg-2)",
          border: isExact ? "1px solid #3fb27f" : "1px solid var(--line)",
          color: isExact ? "#2f9e6e" : "var(--fg-2)",
          transition: "background .3s ease, border-color .3s ease, color .3s ease",
        }}
      >
        {isExact ? (
          <span className="inline-flex items-center justify-center gap-2 font-medium">
            <Check className="h-4 w-4" />
            {knownLabel} = {knownValue} — so you need{" "}
            <strong className="serif tabular" style={{ fontSize: 16, color: "#2f9e6e" }}>
              {answer} {missingToken.plural}
            </strong>
          </span>
        ) : (
          <>
            <span style={{ color: "var(--fg)" }}>
              {knownLabel} is now{" "}
              <span className="serif tabular" style={{ fontSize: 15, color: "var(--fg)" }}>
                {knownScaled}
              </span>
            </span>
            {" — "}aim for{" "}
            <span className="serif tabular" style={{ fontSize: 15, color: "var(--accent)" }}>
              {knownValue}
            </span>
          </>
        )}
      </div>
    </div>
  );
}
