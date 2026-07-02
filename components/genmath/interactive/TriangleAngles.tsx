"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { arcPath, GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { triangleThirdAngle, exteriorAngle } from "@/lib/geo";
import { type TriangleAnglesConfig } from "@/lib/genmath-interactive";

// A triangle you reshape by its two base angles. The third angle updates so the
// three always total 180° — the Triangle Angle-Sum Theorem, live. In exterior
// mode the base extends past a vertex and the exterior angle appears, equal to
// the sum of the two remote interior angles.
const W = 320;
const H = 230;

export default function TriangleAngles({ config }: { config: TriangleAnglesConfig }) {
  const { beta: b0 = 55, gamma: g0 = 65, exterior = false, color = GEO_ACCENT } = config;
  const [beta, setBeta] = useState(b0);
  const [gamma, setGamma] = useState(g0);
  const alpha = triangleThirdAngle(beta, gamma);

  // triangle in math coords (y up): B=(0,0), C=(base,0), apex A
  const base = 6;
  const rad = (d: number) => (d * Math.PI) / 180;
  const t = (base * Math.sin(rad(gamma))) / Math.sin(rad(beta + gamma));
  const A = { x: t * Math.cos(rad(beta)), y: t * Math.sin(rad(beta)) };
  const B = { x: 0, y: 0 };
  const C = { x: base, y: 0 };
  const extPt = { x: base + 2.4, y: 0 }; // base extended past C

  // fit to viewBox
  const pts = [A, B, C, ...(exterior ? [extPt] : [])];
  const minX = Math.min(...pts.map((p) => p.x)) - 0.8;
  const maxX = Math.max(...pts.map((p) => p.x)) + 0.8;
  const minY = Math.min(...pts.map((p) => p.y)) - 0.8;
  const maxY = Math.max(...pts.map((p) => p.y)) + 0.8;
  const scale = Math.min((W - 40) / (maxX - minX), (H - 40) / (maxY - minY));
  const ox = (W - (maxX - minX) * scale) / 2;
  const oy = (H - (maxY - minY) * scale) / 2;
  const px = (x: number) => ox + (x - minX) * scale;
  const py = (y: number) => H - (oy + (y - minY) * scale);

  const dirDeg = (from: { x: number; y: number }, to: { x: number; y: number }) =>
    (Math.atan2(py(to.y) - py(from.y), px(to.x) - px(from.x)) * 180) / Math.PI;

  const Vertex = ({ at, from, to, label, deg, col }: { at: { x: number; y: number }; from: { x: number; y: number }; to: { x: number; y: number }; label: string; deg: number; col: string }) => {
    const a1 = dirDeg(at, from);
    const a2 = dirDeg(at, to);
    let mid = (a1 + a2) / 2;
    // ensure the label sits inside the angle (shorter arc side)
    let d = a2 - a1;
    while (d < -180) d += 360;
    while (d > 180) d -= 360;
    mid = a1 + d / 2;
    const lp = { x: px(at.x) + Math.cos(rad(mid)) * 30, y: py(at.y) + Math.sin(rad(mid)) * 30 };
    return (
      <g>
        <path d={arcPath(px(at.x), py(at.y), 20, a1, a2)} fill="none" stroke={col} strokeWidth={2} />
        <text x={lp.x} y={lp.y + 4} fontSize="12" textAnchor="middle" fill={col} fontWeight={700}>{deg}°</text>
      </g>
    );
  };

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        {/* extended base for exterior mode */}
        {exterior && (
          <>
            <line x1={px(C.x)} y1={py(C.y)} x2={px(extPt.x)} y2={py(extPt.y)} stroke="var(--fg-3)" strokeWidth={1.6} strokeDasharray="5 4" />
            <Vertex at={C} from={extPt} to={A} label="ext" deg={exteriorAngle(alpha, beta)} col={GEO_BLUE} />
          </>
        )}
        {/* triangle */}
        <polygon points={`${px(A.x)},${py(A.y)} ${px(B.x)},${py(B.y)} ${px(C.x)},${py(C.y)}`} fill={`${color}12`} stroke="var(--fg-1)" strokeWidth={2} strokeLinejoin="round" />
        {/* interior angle arcs */}
        <Vertex at={A} from={B} to={C} label="A" deg={alpha} col={color} />
        <Vertex at={B} from={C} to={A} label="B" deg={beta} col={color} />
        <Vertex at={C} from={A} to={B} label="C" deg={gamma} col={color} />
        {/* vertex dots + names */}
        {[["A", A], ["B", B], ["C", C]].map(([n, p]) => (
          <g key={n as string}>
            <circle cx={px((p as { x: number }).x)} cy={py((p as { y: number }).y)} r={3} fill="var(--fg)" />
          </g>
        ))}
      </svg>

      {/* the sum */}
      <div className="mt-2 rounded-xl p-3 text-center text-[15px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        {exterior ? (
          <>
            Exterior angle <span className="serif tabular" style={{ color: GEO_BLUE }}>{exteriorAngle(alpha, beta)}°</span> ={" "}
            <span className="serif tabular" style={{ color }}>{alpha}° + {beta}°</span> — the two remote interior angles
          </>
        ) : (
          <span className="serif tabular">
            {alpha}° + {beta}° + {gamma}° = <b style={{ color }}>180°</b>
          </span>
        )}
      </div>

      {/* steppers for the two base angles */}
      <div className="mt-4 flex items-center justify-around gap-3">
        {[["∠B", beta, setBeta], ["∠C", gamma, setGamma]].map(([label, val, set]) => (
          <div key={label as string} className="text-center">
            <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>{label as string}</div>
            <div className="mt-1 flex items-center gap-2">
              <button type="button" onClick={() => (set as (f: (v: number) => number) => void)((v) => Math.max(25, v - 5))} disabled={(val as number) <= 25} aria-label={`Decrease ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
              <div className="serif tabular text-center" style={{ minWidth: 40, fontSize: 17, color: "var(--fg)" }}>{val as number}°</div>
              <button type="button" onClick={() => (set as (f: (v: number) => number) => void)((v) => { const other = label === "∠B" ? gamma : beta; return Math.min(180 - other - 25, v + 5); })} aria-label={`Increase ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
            </div>
          </div>
        ))}
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        {exterior
          ? <>An <b style={{ color: "var(--fg-1)" }}>exterior angle</b> equals the sum of the two <b style={{ color: "var(--fg-1)" }}>remote interior</b> angles.</>
          : <>Reshape the triangle — the three angles <b style={{ color: "var(--fg-1)" }}>always total 180°</b>.</>}
      </div>
    </div>
  );
}
