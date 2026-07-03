"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { pythagoreanHypotenuse } from "@/lib/geo";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type PythagoreanSquaresConfig } from "@/lib/genmath-interactive";

// The classic Pythagorean picture: a right triangle with a square built on each
// side. The area of the two leg squares (a² and b²) always adds up to the area
// of the hypotenuse square (c²). Both legs are adjustable.
const W = 320;
const H = 300;

export default function PythagoreanSquares({ config }: { config: PythagoreanSquaresConfig }) {
  const { color = GEO_ACCENT } = config;
  const [a, setA] = useState(config.a ?? 3);
  const [b, setB] = useState(config.b ?? 4);
  const c = pythagoreanHypotenuse(a, b);
  // geometry follows springs (squares morph smoothly); every number shown is exact
  const ad = useAnimatedValue(a, { stiffness: 140, damping: 20 });
  const bd = useAnimatedValue(b, { stiffness: 140, damping: 20 });

  // right angle at C=(0,0); B=(a,0); A=(0,b) in math coords (y up)
  const C = { x: 0, y: 0 }, B = { x: ad, y: 0 }, A = { x: 0, y: bd };
  // squares (corners in math coords)
  const sqA = [C, B, { x: ad, y: -ad }, { x: 0, y: -ad }]; // on leg a (below)
  const sqB = [C, A, { x: -bd, y: bd }, { x: -bd, y: 0 }]; // on leg b (left)
  const sqC = [B, A, { x: bd, y: ad + bd }, { x: ad + bd, y: ad }]; // on hypotenuse (outward)

  const allPts = [...sqA, ...sqB, ...sqC];
  const minX = Math.min(...allPts.map((p) => p.x)) - 0.6;
  const maxX = Math.max(...allPts.map((p) => p.x)) + 0.6;
  const minY = Math.min(...allPts.map((p) => p.y)) - 0.6;
  const maxY = Math.max(...allPts.map((p) => p.y)) + 0.6;
  const scale = Math.min((W - 20) / (maxX - minX), (H - 20) / (maxY - minY));
  const ox = (W - (maxX - minX) * scale) / 2, oy = (H - (maxY - minY) * scale) / 2;
  const sx = (x: number) => ox + (x - minX) * scale;
  const sy = (y: number) => H - (oy + (y - minY) * scale);
  const path = (pts: any[]) => pts.map((p, i) => `${i ? "L" : "M"} ${sx(p.x)} ${sy(p.y)}`).join(" ") + " Z";
  const cen = (pts: any[]) => ({ x: pts.reduce((s, p) => s + p.x, 0) / pts.length, y: pts.reduce((s, p) => s + p.y, 0) / pts.length });
  const ca = cen(sqA), cb = cen(sqB), cc = cen(sqC);
  const fmt = (n: number) => (Number.isInteger(n) ? n.toString() : n.toFixed(2));

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        <g className="gm-fade"><path d={path(sqA)} fill={`${color}22`} stroke={color} strokeWidth={1.5} /></g>
        <g className="gm-fade" style={{ animationDelay: "0.3s" }}><path d={path(sqB)} fill={`${GEO_BLUE}22`} stroke={GEO_BLUE} strokeWidth={1.5} /></g>
        <g className="gm-fade" style={{ animationDelay: "0.6s" }}><path d={path(sqC)} fill="rgba(63,160,106,0.14)" stroke="#3fa06a" strokeWidth={1.5} /></g>
        {/* the triangle */}
        <path d={path([C, B, A])} fill="rgba(120,120,120,0.10)" stroke="var(--fg-1)" strokeWidth={2} />
        {/* right-angle square at C */}
        <path d={`M ${sx(0.5)} ${sy(0)} L ${sx(0.5)} ${sy(0.5)} L ${sx(0)} ${sy(0.5)}`} fill="none" stroke="var(--fg-2)" strokeWidth={1.2} />
        <text className="gm-fade" style={{ animationDelay: "0.15s" }} x={sx(ca.x)} y={sy(ca.y) + 4} fontSize="12" textAnchor="middle" fill={color} fontWeight={700}>{a}² = {a * a}</text>
        <text className="gm-fade" style={{ animationDelay: "0.45s" }} x={sx(cb.x)} y={sy(cb.y) + 4} fontSize="12" textAnchor="middle" fill={GEO_BLUE} fontWeight={700}>{b}² = {b * b}</text>
        <text className="gm-fade" style={{ animationDelay: "0.75s" }} x={sx(cc.x)} y={sy(cc.y) + 4} fontSize="12" textAnchor="middle" fill="#3fa06a" fontWeight={700}>c² = {a * a + b * b}</text>
      </svg>

      <div className="mt-2 rounded-xl p-3 text-center text-[15px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        <span className="serif tabular">
          <span style={{ color }}>{a * a}</span> + <span style={{ color: GEO_BLUE }}>{b * b}</span> = <b style={{ color: "#3fa06a" }}>{a * a + b * b}</b>
        </span>
        <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>c = √{a * a + b * b} = {fmt(c)}{Number.isInteger(c) ? " (a whole number — a Pythagorean triple!)" : ""}</div>
      </div>

      <div className="mt-4 flex items-center justify-around gap-3">
        {[["a", a, setA, color], ["b", b, setB, GEO_BLUE]].map(([label, val, set, col]: any) => (
          <div key={label} className="text-center">
            <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>leg {label}</div>
            <div className="mt-1 flex items-center gap-2">
              <button type="button" onClick={() => set((v: number) => Math.max(2, v - 1))} disabled={val <= 2} aria-label={`Decrease ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
              <div className="serif tabular text-center" style={{ minWidth: 28, fontSize: 17, color: col }}>{val}</div>
              <button type="button" onClick={() => set((v: number) => Math.min(8, v + 1))} disabled={val >= 8} aria-label={`Increase ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
