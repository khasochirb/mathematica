"use client";

import { useState } from "react";
import { type PrimeExplorerConfig } from "@/lib/genmath-interactive";

// All factors of n, in order.
function factorsOf(n: number): number[] {
  const out: number[] = [];
  for (let d = 1; d <= n; d++) if (n % d === 0) out.push(d);
  return out;
}

// A grid of numbers 2..max. Primes (exactly two factors) glow in the accent
// colour, composites stay muted, so the "thinning out" of primes is visible at
// a glance. Tap any number to see its factor list and the prime/composite
// verdict — the definition made concrete.
export default function PrimeExplorer({ config }: { config: PrimeExplorerConfig }) {
  const { max, start, color = "#e8913c" } = config;
  const [sel, setSel] = useState(Math.min(Math.max(2, start), max));

  const factors = factorsOf(sel);
  const isPrime = sel >= 2 && factors.length === 2;
  const isComposite = sel >= 2 && factors.length > 2;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <div style={{ display: "grid", gridTemplateColumns: "repeat(7, 34px)", gap: 5 }}>
          {Array.from({ length: max - 1 }).map((_, i) => {
            const n = i + 2;
            const prime = factorsOf(n).length === 2;
            const active = n === sel;
            return (
              <button
                key={n}
                type="button"
                onClick={() => setSel(n)}
                aria-label={`Inspect ${n}`}
                className="gm-press grid place-items-center serif tabular"
                style={{
                  width: 34,
                  height: 34,
                  borderRadius: 7,
                  fontSize: 14,
                  background: prime ? color : "var(--bg-2)",
                  color: prime ? "#fff" : "var(--fg-2)",
                  border: active ? "2px solid var(--fg)" : "1px solid var(--line)",
                  transition: "transform 120ms ease",
                }}
              >
                {n}
              </button>
            );
          })}
        </div>
      </div>

      <div className="mt-3 flex items-center justify-center gap-2 text-[12px]" style={{ color: "var(--fg-3)" }}>
        <span className="inline-flex items-center gap-1.5">
          <span style={{ width: 12, height: 12, borderRadius: 3, background: color, display: "inline-block" }} />
          prime
        </span>
        <span className="inline-flex items-center gap-1.5">
          <span style={{ width: 12, height: 12, borderRadius: 3, background: "var(--bg-2)", border: "1px solid var(--line)", display: "inline-block" }} />
          composite
        </span>
      </div>

      <div className="mt-4 rounded-xl p-3.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <div className="text-[13px]" style={{ color: "var(--fg-2)" }}>
          Factors of <b className="serif tabular" style={{ color: "var(--fg)" }}>{sel}</b>:
        </div>
        <div className="mt-2 flex flex-wrap justify-center gap-1.5">
          {factors.map((f) => (
            <span
              key={f}
              className="serif tabular grid place-items-center"
              style={{
                minWidth: 30,
                height: 30,
                padding: "0 8px",
                borderRadius: 7,
                fontSize: 14,
                background: "var(--bg-1)",
                border: "1px solid var(--line)",
                color: "var(--fg)",
              }}
            >
              {f}
            </span>
          ))}
        </div>
        <div className="mt-3 text-[14px]" style={{ color: "var(--fg-1)" }}>
          {isPrime && (
            <span>
              <b style={{ color: "var(--accent)" }}>Prime</b> — exactly <b className="tabular">2</b> factors: 1 and itself.
            </span>
          )}
          {isComposite && (
            <span>
              <b style={{ color: "var(--fg)" }}>Composite</b> — <b className="tabular">{factors.length}</b> factors, more than 2.
            </span>
          )}
        </div>
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        Tap any number. <b style={{ color: "var(--fg-1)" }}>Exactly two factors</b> means prime; more than two means composite.
      </div>
    </div>
  );
}
