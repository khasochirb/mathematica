"use client";

import { useState } from "react";
import { RotateCcw } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { type PatternGrowConfig } from "@/lib/genmath-interactive";

// A growing visual pattern, revealed one stage at a time — the raw material of
// inductive reasoning. Watch a few stages, feel the rule coming, then read the
// conjecture the pattern suggests.
//   odds:     L-shaped layers of 1, 3, 5, 7… dots build a perfect square —
//             "the first n odd numbers sum to n²".
//   doubling: dots double each stage — "stage n holds 2^(n−1) dots".
export default function PatternGrow({ config }: { config: PatternGrowConfig }) {
  const { pattern, maxSteps = pattern === "odds" ? 5 : 5 } = config;
  const [n, setN] = useState(1);
  const done = n >= maxSteps;

  const layerColor = (k: number) => (k % 2 === 1 ? GEO_ACCENT : GEO_BLUE);

  // --- odds: n×n dot square, layer k = the k-th L-shaped gnomon (2k−1 dots)
  const cell = 26;
  const oddsGrid = (
    <div className="flex justify-center">
      <div style={{ display: "grid", gridTemplateColumns: `repeat(${maxSteps}, ${cell}px)`, gap: 4 }}>
        {Array.from({ length: maxSteps }).map((_, r) =>
          Array.from({ length: maxSteps }).map((_, c) => {
            const k = Math.max(r, c) + 1; // which gnomon layer this cell belongs to
            const visible = k <= n;
            return (
              <div
                key={`${r}-${c}`}
                style={{
                  width: cell,
                  height: cell,
                  borderRadius: "50%",
                  background: visible ? layerColor(k) : "var(--bg-2)",
                  border: "1px solid var(--line)",
                  opacity: visible ? 1 : 0.45,
                  transition: "background 160ms ease",
                }}
              />
            );
          })
        )}
      </div>
    </div>
  );

  // --- doubling: rows of dots, stage k has 2^(k−1)
  const doublingRows = (
    <div className="flex flex-col items-center gap-2">
      {Array.from({ length: n }).map((_, i) => (
        <div key={i} className="flex flex-wrap justify-center gap-1.5" style={{ maxWidth: 300 }}>
          {Array.from({ length: Math.pow(2, i) }).map((_, j) => (
            <span key={j} style={{ width: 14, height: 14, borderRadius: "50%", background: layerColor(i + 1), display: "inline-block" }} />
          ))}
        </div>
      ))}
    </div>
  );

  const added = pattern === "odds" ? 2 * n - 1 : Math.pow(2, n - 1);
  const total = pattern === "odds" ? n * n : Math.pow(2, n) - 1;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      {pattern === "odds" ? oddsGrid : doublingRows}

      {/* running table */}
      <div className="mt-4 overflow-x-auto">
        <table className="mx-auto text-center" style={{ borderCollapse: "collapse" }}>
          <thead>
            <tr>
              <th className="px-2.5 py-1 text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)", borderBottom: "1px solid var(--line)" }}>stage</th>
              {Array.from({ length: n }).map((_, i) => (
                <th key={i} className="serif tabular px-2.5 py-1 text-[13px]" style={{ color: "var(--fg-2)", borderBottom: "1px solid var(--line)" }}>{i + 1}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            <tr>
              <td className="px-2.5 py-1 text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>{pattern === "odds" ? "new dots" : "dots"}</td>
              {Array.from({ length: n }).map((_, i) => (
                <td key={i} className="serif tabular px-2.5 py-1 text-[14px]" style={{ color: i + 1 === n ? "var(--accent)" : "var(--fg)" }}>
                  {pattern === "odds" ? 2 * (i + 1) - 1 : Math.pow(2, i)}
                </td>
              ))}
            </tr>
            {pattern === "odds" && (
              <tr>
                <td className="px-2.5 py-1 text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>total</td>
                {Array.from({ length: n }).map((_, i) => (
                  <td key={i} className="serif tabular px-2.5 py-1 text-[14px]" style={{ color: i + 1 === n ? "var(--accent)" : "var(--fg)" }}>
                    {(i + 1) * (i + 1)}
                  </td>
                ))}
              </tr>
            )}
          </tbody>
        </table>
      </div>

      <div className="mt-3 rounded-xl p-3 text-center text-[14px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        {pattern === "odds" ? (
          <>
            Stage {n}: added <b className="serif tabular" style={{ color: "var(--accent)" }}>{added}</b> dots → total{" "}
            <b className="serif tabular" style={{ color: "var(--accent)" }}>{total} = {n}²</b>
          </>
        ) : (
          <>
            Stage {n}: <b className="serif tabular" style={{ color: "var(--accent)" }}>{added}</b> dots — double the stage before
          </>
        )}
        {done && (
          <div className="mt-1.5 text-[13px]" style={{ color: "var(--fg-2)" }}>
            {pattern === "odds"
              ? "Conjecture: the first n odd numbers always add up to n². (The pattern suggests it — proving it comes later.)"
              : "Conjecture: each stage doubles — stage n has 2ⁿ⁻¹ dots. Suggested, not yet proven."}
          </div>
        )}
      </div>

      <div className="mt-4 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={() => setN(1)}
          disabled={n === 1}
          aria-label="Reset pattern"
          className="gm-press inline-flex items-center gap-1.5 rounded-full px-4 py-2.5 text-[14px] disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <RotateCcw className="h-4 w-4" /> Reset
        </button>
        <button
          type="button"
          onClick={() => setN((v) => Math.min(maxSteps, v + 1))}
          disabled={done}
          className="gm-press rounded-full px-5 py-2.5 text-[14px] disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          Next stage
        </button>
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        Watch enough stages and a rule <b style={{ color: "var(--fg-1)" }}>suggests itself</b> — that's inductive reasoning.
      </div>
    </div>
  );
}
