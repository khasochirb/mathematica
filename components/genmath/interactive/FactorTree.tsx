"use client";

import { useState } from "react";
import { CornerDownRight, RotateCcw } from "lucide-react";
import { type FactorTreeConfig } from "@/lib/genmath-interactive";

function isPrime(n: number): boolean {
  if (n < 2) return false;
  for (let d = 2; d * d <= n; d++) if (n % d === 0) return false;
  return true;
}
function smallestPrimeFactor(n: number): number {
  for (let d = 2; d * d <= n; d++) if (n % d === 0) return d;
  return n;
}

// Peel off the smallest prime factor repeatedly: 24 = 2×12, 12 = 2×6, 6 = 2×3.
type Split = { cur: number; p: number; rem: number };
function buildSplits(n: number): { splits: Split[]; primes: number[] } {
  const splits: Split[] = [];
  let cur = n;
  while (cur > 1 && !isPrime(cur)) {
    const p = smallestPrimeFactor(cur);
    const rem = cur / p;
    splits.push({ cur, p, rem });
    cur = rem;
  }
  const primes = splits.map((s) => s.p);
  if (cur > 1) primes.push(cur); // final prime
  return { splits, primes };
}

// Group repeated primes into base^exponent for the tidy final answer.
function asPowers(primes: number[]): { base: number; exp: number }[] {
  const counts = new Map<number, number>();
  for (const p of primes) counts.set(p, (counts.get(p) ?? 0) + 1);
  return Array.from(counts.entries())
    .sort((a, b) => a[0] - b[0])
    .map(([base, exp]) => ({ base, exp }));
}

// A factor tree that peels one prime at a time. Tap "Split once" to break the
// current number into its smallest prime factor and what's left, until only
// primes remain — then the prime factorization assembles at the bottom.
export default function FactorTree({ config }: { config: FactorTreeConfig }) {
  const { n, color = "#e8913c" } = config;
  const { splits, primes } = buildSplits(n);
  const [shown, setShown] = useState(0);
  const done = shown >= splits.length;

  const Prime = ({ v }: { v: number }) => (
    <span
      className="serif tabular grid place-items-center"
      style={{ width: 34, height: 34, borderRadius: "50%", background: color, color: "#fff", fontSize: 15 }}
    >
      {v}
    </span>
  );
  const Composite = ({ v }: { v: number }) => (
    <span
      className="serif tabular grid place-items-center"
      style={{ minWidth: 36, height: 34, padding: "0 8px", borderRadius: 8, background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)", fontSize: 15 }}
    >
      {v}
    </span>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex flex-col items-center gap-2">
        {/* Root */}
        <div className="flex items-center gap-2">
          {isPrime(n) ? <Prime v={n} /> : <Composite v={n} />}
          <span className="text-[12px]" style={{ color: "var(--fg-3)" }}>start</span>
        </div>

        {/* Revealed splits, indented like a cascading tree */}
        {splits.slice(0, shown).map((s, i) => {
          const remIsPrime = isPrime(s.rem);
          return (
            <div key={i} className="flex items-center gap-2" style={{ paddingLeft: i * 14 }}>
              <CornerDownRight className="h-4 w-4" style={{ color: "var(--fg-3)" }} />
              <Prime v={s.p} />
              <span style={{ color: "var(--fg-3)" }}>×</span>
              {remIsPrime ? <Prime v={s.rem} /> : <Composite v={s.rem} />}
            </div>
          );
        })}
      </div>

      {/* Controls */}
      <div className="mt-4 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={() => setShown(0)}
          disabled={shown === 0}
          aria-label="Reset tree"
          className="gm-press inline-flex items-center gap-1.5 rounded-full px-4 py-2.5 text-[14px] disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <RotateCcw className="h-4 w-4" /> Reset
        </button>
        <button
          type="button"
          onClick={() => setShown((v) => Math.min(splits.length, v + 1))}
          disabled={done}
          className="gm-press inline-flex items-center gap-1.5 rounded-full px-5 py-2.5 text-[14px] disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          Split once
        </button>
      </div>

      {/* Final answer */}
      {done && (
        <div className="mt-4 rounded-xl p-3 text-center text-[15px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
          <span className="serif tabular">{n}</span> ={" "}
          <span className="serif tabular" style={{ color: "var(--accent)" }}>{primes.join(" × ")}</span>
          {primes.length !== new Set(primes).size && (
            <>
              {" "}={" "}
              <span className="serif tabular" style={{ color: "var(--accent)" }}>
                {asPowers(primes).map((t, idx) => (
                  <span key={t.base}>
                    {idx > 0 && " × "}
                    {t.base}
                    {t.exp > 1 && <sup style={{ fontSize: "0.7em" }}>{t.exp}</sup>}
                  </span>
                ))}
              </span>
            </>
          )}
        </div>
      )}

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        {done
          ? "Every number at the ends is prime — that's the prime factorization."
          : "Keep splitting off the smallest prime until only primes are left."}
      </div>
    </div>
  );
}
