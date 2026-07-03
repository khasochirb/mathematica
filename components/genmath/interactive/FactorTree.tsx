"use client";

import { useState } from "react";
import { RotateCcw } from "lucide-react";
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

// Peel off the smallest prime factor repeatedly: 24 → 2×12, 12 → 2×6, 6 → 2×3.
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
  if (cur > 1) primes.push(cur);
  return { splits, primes };
}

function asPowers(primes: number[]): { base: number; exp: number }[] {
  const counts = new Map<number, number>();
  for (const p of primes) counts.set(p, (counts.get(p) ?? 0) + 1);
  return Array.from(counts.entries())
    .sort((a, b) => a[0] - b[0])
    .map(([base, exp]) => ({ base, exp }));
}

// A real branching factor tree: the number sits at the top, and each "Split
// once" breaks the current number into two children joined by branches — its
// smallest prime (circled, on the left) and what's left (on the right). The
// right child keeps splitting until every leaf is prime, so the split is
// something you SEE happen, not a list you have to decode.
type TNode = { x: number; y: number; v: number; prime: boolean; revealAt: number };
type TEdge = { x1: number; y1: number; x2: number; y2: number; revealAt: number };

export default function FactorTree({ config }: { config: FactorTreeConfig }) {
  const { n, color = "#e8913c" } = config;
  const { splits, primes } = buildSplits(n);
  const [shown, setShown] = useState(0);
  const done = shown >= splits.length;

  // layout: the composite "spine" drifts down-right; each prime leaf hangs
  // down-left of its parent.
  const dx = 34, dy = 62, topY = 26, r = 18;
  const rootX = dx + 24;
  const nodes: TNode[] = [{ x: rootX, y: topY, v: n, prime: isPrime(n), revealAt: 0 }];
  const edges: TEdge[] = [];
  let px = rootX, py = topY;
  for (let i = 0; i < splits.length; i++) {
    const s = splits[i];
    const leafX = px - dx, leafY = py + dy;
    const childX = px + dx, childY = py + dy;
    edges.push({ x1: px, y1: py, x2: leafX, y2: leafY, revealAt: i + 1 });
    edges.push({ x1: px, y1: py, x2: childX, y2: childY, revealAt: i + 1 });
    nodes.push({ x: leafX, y: leafY, v: s.p, prime: true, revealAt: i + 1 });
    nodes.push({ x: childX, y: childY, v: s.rem, prime: isPrime(s.rem), revealAt: i + 1 });
    px = childX; py = childY;
  }
  const W = px + dx + 24;
  const H = py + r + 22;

  const Node = ({ nd }: { nd: TNode }) =>
    nd.prime ? (
      <g>
        <circle cx={nd.x} cy={nd.y} r={r} fill={color} />
        <text x={nd.x} y={nd.y} textAnchor="middle" dominantBaseline="central" fontSize="15" fontFamily="serif" fill="#fff">{nd.v}</text>
      </g>
    ) : (
      <g>
        <rect x={nd.x - r - 3} y={nd.y - r} width={2 * r + 6} height={2 * r} rx={7} fill="var(--bg-2)" stroke="var(--line)" strokeWidth={1.4} />
        <text x={nd.x} y={nd.y} textAnchor="middle" dominantBaseline="central" fontSize="15" fontFamily="serif" fill="var(--fg)">{nd.v}</text>
      </g>
    );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center overflow-x-auto">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: Math.min(W, 360), minWidth: Math.min(W, 240) }} role="img" aria-label="Factor tree">
          {/* branches */}
          {edges.filter((e) => e.revealAt <= shown).map((e, i) => (
            <line key={`e${i}`} x1={e.x1} y1={e.y1 + r - 2} x2={e.x2} y2={e.y2 - r + 2} stroke="var(--fg-3)" strokeWidth={1.6} />
          ))}
          {/* nodes */}
          {nodes.filter((nd) => nd.revealAt <= shown).map((nd, i) => (
            <Node key={`n${i}`} nd={nd} />
          ))}
          {/* "start" label on the root before any split */}
          {shown === 0 && !isPrime(n) && (
            <text x={rootX + r + 8} y={topY} dominantBaseline="central" fontSize="12" fill="var(--fg-3)">start</text>
          )}
        </svg>
      </div>

      {/* Controls */}
      {!isPrime(n) && (
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
      )}

      {/* Final answer */}
      {(done || isPrime(n)) && (
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
        {isPrime(n)
          ? `${n} is already prime — it can't be split.`
          : done
            ? "Every leaf at the bottom is a circled prime — that's the prime factorization."
            : "Each number splits into two branches: its smallest prime (circled) and what's left."}
      </div>
    </div>
  );
}
