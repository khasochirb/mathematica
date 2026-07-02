"use client";

import { useState } from "react";
import { Minus, Plus, Check, X } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { canFormTriangle } from "@/lib/geo";
import { type TriangleInequalityConfig } from "@/lib/genmath-interactive";

// Three adjustable side lengths try to close into a triangle. The base sits on
// the bottom; arcs of the other two lengths swing up from its ends. If they
// reach each other a triangle snaps shut; if the two shorter sides can't span
// the longest, the arcs fall short — the Triangle Inequality, made physical.
const W = 320;
const H = 200;

export default function TriangleInequality({ config }: { config: TriangleInequalityConfig }) {
  const { a: a0 = 4, b: b0 = 5, c: c0 = 6, max = 12 } = config;
  const [a, setA] = useState(a0); // left arm (from left base end)
  const [b, setB] = useState(b0); // right arm (from right base end)
  const [c, setC] = useState(c0); // base

  const forms = canFormTriangle(a, b, c);
  const unit = (W - 80) / max;
  const Lx = 40, Rx = 40 + c * unit, baseY = H - 45;

  // apex by intersecting circles radius a (from L) and b (from R) when forms
  let apex: { x: number; y: number } | null = null;
  if (forms) {
    const d = c;
    const x = (d * d + a * a - b * b) / (2 * d); // distance along base from L
    const h2 = a * a - x * x;
    if (h2 >= 0) apex = { x: Lx + x * unit, y: baseY - Math.sqrt(h2) * unit };
  }

  const arc = (cx: number, r: number, sweepDir: 1 | -1) => {
    // quarter-ish arc from the base sweeping up toward the middle
    const rr = r * unit;
    const start = { x: cx, y: baseY - rr }; // straight up
    const endAngle = sweepDir === 1 ? 20 : 160; // degrees
    const end = { x: cx + rr * Math.cos((endAngle * Math.PI) / 180), y: baseY - rr * Math.sin((endAngle * Math.PI) / 180) };
    return `M ${start.x} ${start.y} A ${rr} ${rr} 0 0 ${sweepDir === 1 ? 1 : 0} ${end.x} ${end.y}`;
  };

  const Stepper = ({ label, val, set, col }: { label: string; val: number; set: (f: (v: number) => number) => void; col: string }) => (
    <div className="text-center">
      <div className="text-[11px] uppercase tracking-wide" style={{ color: col }}>{label} = {val}</div>
      <div className="mt-1 flex items-center gap-1.5">
        <button type="button" onClick={() => set((v) => Math.max(1, v - 1))} disabled={val <= 1} aria-label={`Decrease ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <button type="button" onClick={() => set((v) => Math.min(max, v + 1))} disabled={val >= max} aria-label={`Increase ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
    </div>
  );

  // find the longest side + the sum of the other two, for the verdict line
  const sides = [a, b, c];
  const longest = Math.max(...sides);
  const otherTwo = a + b + c - longest;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        {/* base c */}
        <line x1={Lx} y1={baseY} x2={Rx} y2={baseY} stroke="var(--fg-1)" strokeWidth={3} />
        <circle cx={Lx} cy={baseY} r={3.5} fill="var(--fg)" />
        <circle cx={Rx} cy={baseY} r={3.5} fill="var(--fg)" />
        <text x={(Lx + Rx) / 2} y={baseY + 20} fontSize="12" textAnchor="middle" fill="var(--fg-2)">c = {c}</text>

        {forms && apex ? (
          <>
            <line x1={Lx} y1={baseY} x2={apex.x} y2={apex.y} stroke={GEO_ACCENT} strokeWidth={2.6} />
            <line x1={Rx} y1={baseY} x2={apex.x} y2={apex.y} stroke={GEO_BLUE} strokeWidth={2.6} />
            <circle cx={apex.x} cy={apex.y} r={3.5} fill="var(--fg)" />
            <text x={apex.x - 26} y={(baseY + apex.y) / 2} fontSize="12" fill={GEO_ACCENT}>a = {a}</text>
            <text x={apex.x + 8} y={(baseY + apex.y) / 2} fontSize="12" fill={GEO_BLUE}>b = {b}</text>
          </>
        ) : (
          <>
            {/* arcs falling short */}
            <path d={arc(Lx, a, 1)} fill="none" stroke={GEO_ACCENT} strokeWidth={2.4} strokeDasharray="4 3" />
            <path d={arc(Rx, b, -1)} fill="none" stroke={GEO_BLUE} strokeWidth={2.4} strokeDasharray="4 3" />
            <line x1={Lx} y1={baseY} x2={Lx} y2={baseY - a * unit} stroke={GEO_ACCENT} strokeWidth={2.4} />
            <line x1={Rx} y1={baseY} x2={Rx} y2={baseY - b * unit} stroke={GEO_BLUE} strokeWidth={2.4} />
            <text x={Lx - 6} y={baseY - a * unit - 6} fontSize="12" textAnchor="end" fill={GEO_ACCENT}>a = {a}</text>
            <text x={Rx + 6} y={baseY - b * unit - 6} fontSize="12" fill={GEO_BLUE}>b = {b}</text>
          </>
        )}
      </svg>

      <div className="mt-2 rounded-xl p-3 text-center" style={forms ? { background: "rgba(80,160,90,0.1)", border: "1px solid rgba(80,160,90,0.5)" } : { background: "rgba(200,60,60,0.08)", border: "1px solid rgb(200,60,60)" }}>
        <span className="inline-flex items-center gap-1.5 text-[15px]" style={{ color: "var(--fg)" }}>
          {forms ? <Check className="h-4 w-4" style={{ color: "rgb(70,150,80)" }} /> : <X className="h-4 w-4" style={{ color: "rgb(200,60,60)" }} />}
          <b>{forms ? "These close into a triangle" : "These can't close"}</b>
        </span>
        <div className="mt-0.5 serif tabular text-[13px]" style={{ color: "var(--fg-1)" }}>
          two shorter sides: {otherTwo} {otherTwo > longest ? ">" : otherTwo === longest ? "=" : "<"} {longest} (longest side)
        </div>
      </div>

      <div className="mt-4 flex items-center justify-around gap-2">
        <Stepper label="a" val={a} set={setA} col={GEO_ACCENT} />
        <Stepper label="b" val={b} set={setB} col={GEO_BLUE} />
        <Stepper label="c" val={c} set={setC} col="var(--fg-2)" />
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        A triangle closes only when the <b style={{ color: "var(--fg-1)" }}>two shorter sides sum to more</b> than the longest.
      </div>
    </div>
  );
}
