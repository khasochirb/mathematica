"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { rectangleArea, parallelogramArea, triangleArea, trapezoidArea, rhombusArea } from "@/lib/geo";
import { type AreaShapeConfig } from "@/lib/genmath-interactive";

// A shape drawn to scale with its base/height (or diagonals) labelled, and its
// area computed live from adjustable dimensions. One primitive covers
// rectangles, parallelograms, triangles, trapezoids, and rhombi.
const W = 320;
const H = 250;

export default function AreaShape({ config }: { config: AreaShapeConfig }) {
  const { shape, color = GEO_ACCENT } = config;
  const [base, setBase] = useState(config.base ?? 8);
  const [height, setHeight] = useState(config.height ?? 5);
  const [base2, setBase2] = useState(config.base2 ?? 4);
  const [d1, setD1] = useState(config.d1 ?? 8);
  const [d2, setD2] = useState(config.d2 ?? 6);

  const isRhombus = shape === "rhombus";
  const isTrap = shape === "trapezoid";
  // fit: use the max horizontal extent and vertical
  const wUnits = isRhombus ? d1 : Math.max(base, isTrap ? base2 : 0) + 2;
  const hUnits = (isRhombus ? d2 : height) + 2;
  const scale = Math.min((W - 60) / wUnits, (H - 60) / hUnits);
  const cxpx = W / 2, bottomY = H - 34;
  const ux = (u: number) => u * scale;

  // area + formula
  const area = isRhombus ? rhombusArea(d1, d2) : shape === "rectangle" ? rectangleArea(base, height) : shape === "parallelogram" ? parallelogramArea(base, height) : shape === "triangle" ? triangleArea(base, height) : trapezoidArea(base, base2, height);
  const formula: Record<string, string> = {
    rectangle: `${base} × ${height}`,
    parallelogram: `${base} × ${height}`,
    triangle: `½ × ${base} × ${height}`,
    trapezoid: `½ × (${base} + ${base2}) × ${height}`,
    rhombus: `½ × ${d1} × ${d2}`,
  };

  // shape polygon points (screen)
  const poly = (() => {
    const bx = cxpx - ux(base) / 2, by = bottomY, top = bottomY - ux(height);
    const slant = ux(Math.min(2.5, height * 0.5));
    if (shape === "rectangle") return [[bx, by], [bx + ux(base), by], [bx + ux(base), top], [bx, top]];
    if (shape === "parallelogram") return [[bx, by], [bx + ux(base), by], [bx + ux(base) + slant, top], [bx + slant, top]];
    if (shape === "triangle") return [[bx, by], [bx + ux(base), by], [cxpx - ux(base) / 2 + ux(base) * 0.35, top]];
    if (shape === "trapezoid") { const t2 = ux(base2); return [[bx, by], [bx + ux(base), by], [cxpx + t2 / 2, top], [cxpx - t2 / 2, top]]; }
    // rhombus: diamond centred
    const cy = (bottomY + (bottomY - ux(d2))) / 2;
    return [[cxpx, cy - ux(d2) / 2], [cxpx + ux(d1) / 2, cy], [cxpx, cy + ux(d2) / 2], [cxpx - ux(d1) / 2, cy]];
  })();
  const pts = poly.map((p) => `${p[0]},${p[1]}`).join(" ");
  const top = bottomY - ux(height);

  const step = (val: number, set: (n: number) => void, min: number, max: number, label: string, col: string) => (
    <div className="text-center">
      <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>{label}</div>
      <div className="mt-1 flex items-center gap-1.5">
        <button type="button" onClick={() => set(Math.max(min, val - 1))} disabled={val <= min} aria-label={`Decrease ${label}`} className="gm-press grid h-8 w-8 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-3.5 w-3.5" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 22, fontSize: 15, color: col }}>{val}</div>
        <button type="button" onClick={() => set(Math.min(max, val + 1))} disabled={val >= max} aria-label={`Increase ${label}`} className="gm-press grid h-8 w-8 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-3.5 w-3.5" /></button>
      </div>
    </div>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        <polygon points={pts} fill={`${color}18`} stroke="var(--fg-1)" strokeWidth={2} strokeLinejoin="round" />
        {!isRhombus && (
          <>
            {/* base label */}
            <text x={cxpx} y={bottomY + 18} fontSize="12" textAnchor="middle" fill="var(--fg-2)">b = {base}</text>
            {/* height dashed */}
            <line x1={cxpx - ux(base) / 2 - 6} y1={bottomY} x2={cxpx - ux(base) / 2 - 6} y2={top} stroke={GEO_BLUE} strokeWidth={1.4} strokeDasharray="4 3" />
            <text x={cxpx - ux(base) / 2 - 12} y={(bottomY + top) / 2} fontSize="12" textAnchor="end" fill={GEO_BLUE}>h = {height}</text>
            {isTrap && <text x={cxpx} y={top - 6} fontSize="12" textAnchor="middle" fill="var(--fg-2)">{base2}</text>}
          </>
        )}
        {isRhombus && (() => {
          const cy = (bottomY + (bottomY - ux(d2))) / 2;
          return (
            <>
              <line x1={cxpx - ux(d1) / 2} y1={cy} x2={cxpx + ux(d1) / 2} y2={cy} stroke={color} strokeWidth={1.4} strokeDasharray="4 3" />
              <line x1={cxpx} y1={cy - ux(d2) / 2} x2={cxpx} y2={cy + ux(d2) / 2} stroke={GEO_BLUE} strokeWidth={1.4} strokeDasharray="4 3" />
              <text x={cxpx + ux(d1) / 2 + 4} y={cy + 4} fontSize="12" fill={color}>d₁ = {d1}</text>
              <text x={cxpx + 6} y={cy - ux(d2) / 2 + 4} fontSize="12" fill={GEO_BLUE}>d₂ = {d2}</text>
            </>
          );
        })()}
      </svg>

      <div className="mt-2 rounded-xl p-3 text-center text-[15px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        <span className="serif tabular">Area = {formula[shape]} = <b style={{ color }}>{area}</b></span>
      </div>

      <div className="mt-4 flex items-center justify-center gap-4">
        {isRhombus ? (
          <>{step(d1, setD1, 2, 12, "d₁", color)}{step(d2, setD2, 2, 12, "d₂", GEO_BLUE)}</>
        ) : (
          <>
            {step(base, setBase, 2, 14, "base", color)}
            {isTrap && step(base2, setBase2, 1, 12, "top", "var(--fg-1)")}
            {step(height, setHeight, 2, 9, "height", GEO_BLUE)}
          </>
        )}
      </div>
    </div>
  );
}
