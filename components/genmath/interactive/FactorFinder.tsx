"use client";

import { useState } from "react";
import { RotateCcw, Check, X } from "lucide-react";
import { type FactorFinderConfig } from "@/lib/genmath-interactive";

// The METHOD for listing every factor of n, in order. Test the candidate
// divisors 1, 2, 3, … one at a time. Each one that divides n evenly is a
// factor, and it drags its partner n/d in with it — so factors come in pairs.
// Once the candidates pass √n every "new" factor is just the partner of one you
// already found, so you can stop. A factor rainbow arcs each pair together.
export default function FactorFinder({ config }: { config: FactorFinderConfig }) {
  const { n, color = "#e8913c" } = config;
  const M = Math.floor(Math.sqrt(n)); // stop testing once d exceeds √n
  const [checked, setChecked] = useState(0);
  const done = checked >= M;

  // pairs found from divisors 1..checked
  const pairs: { d: number; partner: number }[] = [];
  const factorSet = new Set<number>();
  for (let d = 1; d <= checked; d++) {
    if (n % d === 0) {
      pairs.push({ d, partner: n / d });
      factorSet.add(d);
      factorSet.add(n / d);
    }
  }
  const factors = Array.from(factorSet).sort((a, b) => a - b);

  // ---- factor rainbow (shown when done) ----
  const rainbow = () => {
    const gap = Math.min(52, Math.max(30, Math.floor(300 / factors.length)));
    const W = (factors.length - 1) * gap + 44;
    const baseY = 78;
    const H = baseY + 26;
    const xs = factors.map((_, i) => 22 + i * gap);
    const arcs: React.ReactNode[] = [];
    for (let i = 0; i < Math.floor(factors.length / 2); i++) {
      const x1 = xs[i], x2 = xs[factors.length - 1 - i];
      const r = (x2 - x1) / 2;
      arcs.push(
        <path key={i} d={`M ${x1} ${baseY} A ${r} ${r} 0 0 1 ${x2} ${baseY}`} fill="none" stroke={color} strokeWidth={1.8} opacity={0.75} />
      );
    }
    // odd count → the middle factor is √n paired with itself
    const selfPair = factors.length % 2 === 1 ? xs[(factors.length - 1) / 2] : null;
    return (
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: Math.min(W, 340) }} role="img" aria-label="Factor rainbow">
        {arcs}
        {selfPair !== null && (
          <circle cx={selfPair} cy={baseY - 10} r={9} fill="none" stroke={color} strokeWidth={1.8} opacity={0.75} />
        )}
        {factors.map((f, i) => (
          <g key={f}>
            <circle cx={xs[i]} cy={baseY} r={13} fill={`${color}22`} stroke={color} strokeWidth={1.6} />
            <text x={xs[i]} y={baseY} textAnchor="middle" dominantBaseline="central" fontSize="13" fontFamily="serif" fill="var(--fg)">{f}</text>
          </g>
        ))}
      </svg>
    );
  };

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      {/* Test track: candidate divisors 1..M */}
      <div className="text-center text-[13px]" style={{ color: "var(--fg-2)" }}>Test each number: does it divide <b className="serif tabular" style={{ color: "var(--fg-1)" }}>{n}</b> evenly?</div>
      <div className="mt-3 flex flex-wrap justify-center gap-2">
        {Array.from({ length: M }).map((_, idx) => {
          const d = idx + 1;
          const state = d <= checked ? (n % d === 0 ? "yes" : "no") : "todo";
          const bg = state === "yes" ? color : state === "no" ? "var(--bg-2)" : "var(--bg-2)";
          const bd = state === "yes" ? color : "var(--line)";
          const col = state === "yes" ? "#fff" : state === "no" ? "var(--fg-3)" : "var(--fg-3)";
          return (
            <span key={d} className="serif tabular grid place-items-center relative" style={{ width: 34, height: 34, borderRadius: 8, background: bg, border: `1.5px solid ${bd}`, color: col, opacity: state === "todo" ? 0.5 : 1, textDecoration: state === "no" ? "line-through" : "none" }}>
              {d}
            </span>
          );
        })}
      </div>

      {/* Pairs found so far */}
      {pairs.length > 0 && (
        <div className="mt-4 space-y-1.5">
          {pairs.map((p) => (
            <div key={p.d} className="flex items-center justify-center gap-1.5 text-[14px]" style={{ color: "var(--fg-1)" }}>
              <Check className="h-4 w-4" style={{ color }} />
              <b className="serif tabular">{p.d} × {p.partner} = {n}</b>
              <span style={{ color: "var(--fg-3)" }}>→ factors {p.d} and {p.partner}</span>
            </div>
          ))}
        </div>
      )}

      {/* Ordered factor list building up */}
      {factors.length > 0 && (
        <div className="mt-3 rounded-xl p-3 text-center text-[14px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
          Factors in order: <b className="serif tabular" style={{ color }}>{factors.join(", ")}</b>
          {done && <span style={{ color: "var(--fg-3)" }}> &nbsp;({factors.length} in all)</span>}
        </div>
      )}

      {/* Controls */}
      <div className="mt-4 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={() => setChecked(0)}
          disabled={checked === 0}
          aria-label="Reset"
          className="gm-press inline-flex items-center gap-1.5 rounded-full px-4 py-2.5 text-[14px] disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <RotateCcw className="h-4 w-4" /> Reset
        </button>
        <button
          type="button"
          onClick={() => setChecked((v) => Math.min(M, v + 1))}
          disabled={done}
          className="gm-press inline-flex items-center gap-1.5 rounded-full px-5 py-2.5 text-[14px] disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          Test the next number
        </button>
      </div>

      {/* Factor rainbow + why-stop note (when done) */}
      {done && (
        <div className="mt-4">
          <div className="flex justify-center">{rainbow()}</div>
          <div className="mt-2 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
            Each arc joins a <b style={{ color: "var(--fg-1)" }}>factor pair</b> that multiplies to {n}. Once the tested number passes <b className="serif tabular" style={{ color: "var(--fg-1)" }}>√{n} ≈ {Math.sqrt(n).toFixed(1)}</b>, every new factor is just the partner of one you already have — so you can stop.
          </div>
        </div>
      )}
      {!done && (
        <div className="mt-3 flex items-center justify-center gap-1.5 text-[13px]" style={{ color: "var(--fg-2)" }}>
          <X className="h-3.5 w-3.5" style={{ color: "var(--fg-3)" }} />
          Numbers that leave a remainder are crossed out — they are not factors.
        </div>
      )}
    </div>
  );
}
