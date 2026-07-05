"use client";

import { useMemo, useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type PolyGraphConfig } from "@/lib/genmath-interactive";

// The polynomial-functions workbench — three modes:
//  endBehavior:  y = ±xⁿ with a degree stepper and a sign flip. The four
//                arm-cases (even/odd × up/down) play out live; the verdict
//                panel names the case. Degree changes redraw with a sweep;
//                the sign flip springs.
//  zeros:        a factored cubic (x−a)(x−b)(x−c) with a stepper on the third
//                zero — the curve morphs on a spring and the beacon-ringed
//                crossing chases it. Factored form ↔ crossings, live.
//  multiplicity: y = (x+2)(x−1)^m with m stepped 1→2→3: cross, bounce,
//                flatten-through. The bounce zero wears a beacon.

const RED = "rgb(200,60,60)";

function fmt(n: number): string {
  return (Math.round(n * 100) / 100).toString();
}

export default function PolyGraph({ config }: { config: PolyGraphConfig }) {
  const { mode, n: n0 = 3, negative: neg0 = false, zeros: z0 = [-2, 1, 3], m: m0 = 1 } = config;

  const [n, setN] = useState(n0);
  const [neg, setNeg] = useState(neg0);
  const [z3, setZ3] = useState(z0[2] ?? 3);
  const [m, setM] = useState(m0);

  const signd = useAnimatedValue(neg ? -1 : 1, { stiffness: 120, damping: 18 });
  const z3d = useAnimatedValue(z3, { stiffness: 120, damping: 18 });

  // grid geometry (shared)
  const W = 320;
  const H = 300;
  const padL = 30, padR = 14, padT = 14, padB = 26;
  const X0 = -4, X1 = 4, Y0 = -8, Y1 = 8;
  const px = (x: number) => padL + ((x - X0) / (X1 - X0)) * (W - padL - padR);
  const py = (y: number) => (H - padB) - ((y - Y0) / (Y1 - Y0)) * (H - padB - padT);

  const fAt = (x: number): number => {
    if (mode === "endBehavior") {
      // scale so the arms exit the frame around |x| ≈ 2.6, whatever the degree
      return signd * Math.pow(x / 2.2, n) * 6 / Math.pow(1.4, n - 2);
    }
    if (mode === "zeros") {
      return (x - z0[0]) * (x - z0[1]) * (x - z3d) / 3;
    }
    // multiplicity: (x+2)(x-1)^m, rescaled per m so the frame stays busy
    const scale = m === 1 ? 3 : m === 2 ? 4 : 6;
    return (x + 2) * Math.pow(x - 1, m) / scale;
  };

  const curvePath = useMemo(() => {
    const pts: string[] = [];
    let pen = false;
    let d = "";
    for (let x = X0; x <= X1 + 1e-9; x += 0.05) {
      const y = fAt(x);
      if (y < Y0 - 3 || y > Y1 + 3) { pen = false; continue; }
      const cmd = pen ? "L" : "M";
      d += `${cmd} ${px(x)} ${py(Math.max(Y0 - 3, Math.min(Y1 + 3, y)))} `;
      pen = true;
    }
    return d.trim();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [n, signd, z3d, m, mode]);

  const stepper = (label: string, val: number, set: (f: (v: number) => number) => void, lo: number, hi: number, color = GEO_BLUE) => (
    <div className="text-center">
      <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>{label}</div>
      <div className="mt-1 flex items-center gap-2">
        <button type="button" onClick={() => set((v) => Math.max(lo, v - 1))} disabled={val <= lo} aria-label={`Decrease ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 36, fontSize: 16, color }}>{fmt(val)}</div>
        <button type="button" onClick={() => set((v) => Math.min(hi, v + 1))} disabled={val >= hi} aria-label={`Increase ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
    </div>
  );

  const even = n % 2 === 0;
  const leftUp = mode === "endBehavior" ? (even ? !neg : neg) : false;
  const rightUp = mode === "endBehavior" ? !neg : false;

  // multiplicity verdicts
  const multWord = m === 1 ? "crosses" : m === 2 ? "bounces" : "flattens through";

  const eqnText =
    mode === "endBehavior" ? `y = ${neg ? "−" : ""}x${n === 1 ? "" : `^${n}`}` :
    mode === "zeros" ? `y = (x ${z0[0] < 0 ? "+" : "−"} ${Math.abs(z0[0])})(x ${z0[1] < 0 ? "+" : "−"} ${Math.abs(z0[1])})(x ${z3 < 0 ? "+" : "−"} ${Math.abs(z3)})` :
    `y = (x + 2)(x − 1)${m === 1 ? "" : `^${m}`}`;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340 }} role="img" aria-label="A polynomial curve on a grid">
          {Array.from({ length: X1 - X0 + 1 }, (_, i) => X0 + i).map((g) => (
            <line key={`v${g}`} x1={px(g)} y1={py(Y0)} x2={px(g)} y2={py(Y1)} stroke="var(--line)" strokeWidth={1} />
          ))}
          {Array.from({ length: (Y1 - Y0) / 2 + 1 }, (_, i) => Y0 + i * 2).map((g) => (
            <line key={`h${g}`} x1={px(X0)} y1={py(g)} x2={px(X1)} y2={py(g)} stroke="var(--line)" strokeWidth={1} />
          ))}
          <line x1={px(X0)} y1={py(0)} x2={px(X1)} y2={py(0)} stroke="var(--fg-2)" strokeWidth={1.8} />
          <line x1={px(0)} y1={py(Y0)} x2={px(0)} y2={py(Y1)} stroke="var(--fg-2)" strokeWidth={1.8} />
          {[-4, -2, 2, 4].map((g) => (
            <text key={g} x={px(g)} y={py(0) + 13} fontSize="9" fill="var(--fg-3)" textAnchor="middle">{g}</text>
          ))}
          {[-8, -4, 4, 8].map((g) => (
            <text key={g} x={px(0) - 5} y={py(g) + 3} fontSize="9" fill="var(--fg-3)" textAnchor="end">{g}</text>
          ))}

          {/* the curve — keyed so degree/multiplicity changes re-run the sweep */}
          <path key={`${mode}-${n}-${m}`} d={curvePath} fill="none" stroke={GEO_ACCENT} strokeWidth={2.8} strokeLinecap="round" pathLength={1} className="gm-arc-sweep" />

          {/* end-behavior arm arrows */}
          {mode === "endBehavior" && (
            <g className="gm-fade" style={{ animationDelay: "0.4s" }}>
              <text x={px(X0) + 8} y={leftUp ? py(Y1) + 16 : py(Y0) - 8} fontSize="16" fill={GEO_BLUE} fontWeight={700}>{leftUp ? "↖" : "↙"}</text>
              <text x={px(X1) - 20} y={rightUp ? py(Y1) + 16 : py(Y0) - 8} fontSize="16" fill={GEO_BLUE} fontWeight={700}>{rightUp ? "↗" : "↘"}</text>
            </g>
          )}

          {/* zeros mode: beacon dots at each crossing */}
          {mode === "zeros" && [z0[0], z0[1], z3d].map((z, i) => (
            <g key={i}>
              <circle cx={px(z)} cy={py(0)} r={8.5} fill="none" stroke={GEO_BLUE} strokeWidth={1.3} opacity={0.5} className="gm-beacon" />
              <circle cx={px(z)} cy={py(0)} r={4.2} fill={GEO_BLUE} />
            </g>
          ))}

          {/* multiplicity mode: beacon the special zero at x = 1 */}
          {mode === "multiplicity" && (
            <g>
              <circle cx={px(1)} cy={py(0)} r={9} fill="none" stroke={m === 1 ? GEO_BLUE : RED} strokeWidth={1.4} opacity={0.55} className="gm-beacon" />
              <circle cx={px(1)} cy={py(0)} r={4.2} fill={m === 1 ? GEO_BLUE : RED} />
              <circle cx={px(-2)} cy={py(0)} r={4.2} fill={GEO_BLUE} />
            </g>
          )}
        </svg>
      </div>

      <div className="mt-2 flex justify-center text-[14px]">
        <span className="serif tabular" style={{ color: GEO_ACCENT }}>{eqnText}</span>
      </div>

      {/* verdict */}
      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {mode === "endBehavior" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              Degree {n} ({even ? "even" : "odd"}), leading coefficient {neg ? "negative" : "positive"}: arms {leftUp ? "↖" : "↙"} {rightUp ? "↗" : "↘"}
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              {even ? "even degree: both arms point the SAME way" : "odd degree: the arms point OPPOSITE ways"} · negative flips both
            </div>
          </>
        )}
        {mode === "zeros" && (
          <>
            <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
              Crossings at <b style={{ color: GEO_BLUE }}>x = {z0[0]}, {z0[1]}, {fmt(z3)}</b> — each factor&apos;s zero
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              factored form hands you the x-intercepts; degree 3 → at most 3 of them
            </div>
          </>
        )}
        {mode === "multiplicity" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              At x = 1 (multiplicity {m}) the curve <b style={{ color: m === 1 ? GEO_BLUE : RED }}>{multWord}</b>
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              {m === 1 ? "multiplicity 1: a clean pass through the axis" : m === 2 ? "even multiplicity: touch and turn back — a bounce" : "odd multiplicity ≥ 3: squeezes flat, then continues through"}
            </div>
          </>
        )}
      </div>

      {/* controls */}
      <div className="mt-4 flex items-center justify-center gap-6 flex-wrap">
        {mode === "endBehavior" && (
          <>
            {stepper("degree n", n, setN, 2, 5, GEO_ACCENT)}
            <div className="text-center">
              <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>leading sign</div>
              <button type="button" onClick={() => setNeg((v) => !v)} aria-label="Flip leading sign" className="gm-press mt-1 rounded-full px-5 py-2 text-[14px] serif" style={{ background: neg ? "rgba(200,60,60,0.1)" : "var(--accent-wash)", border: `1px solid ${neg ? RED : "var(--accent-line)"}`, color: neg ? RED : "var(--accent)" }}>
                {neg ? "negative" : "positive"}
              </button>
            </div>
          </>
        )}
        {mode === "zeros" && stepper("third zero", z3, setZ3, 2, 4)}
        {mode === "multiplicity" && stepper("multiplicity m", m, setM, 1, 3, RED)}
      </div>
      <div className="mt-2 text-center text-[12px]" style={{ color: "var(--fg-3)" }}>
        {mode === "endBehavior" && "step the degree and flip the sign — watch the four arm-cases"}
        {mode === "zeros" && "slide the third zero — the crossing (and the curve) follows"}
        {mode === "multiplicity" && "step m through 1, 2, 3 — cross, bounce, flatten-through"}
      </div>
    </div>
  );
}
