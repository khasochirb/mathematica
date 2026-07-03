"use client";

import { useState } from "react";
import { arcPath, GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { type QuadShapeConfig } from "@/lib/genmath-interactive";

// A canonical quadrilateral drawn with the marks that DEFINE its type —
// parallel arrows, congruence ticks, right-angle squares, equal-angle arcs —
// and, on tap, its diagonals with their signature property. Vertices are fixed
// exact coordinates so every mark is geometrically honest.
const W = 320;
const H = 250;

type XY = { x: number; y: number };

interface Spec {
  v: [number, number][]; // A, B, C, D  (y up)
  parallels: [number, number, number][]; // [sideIdxA, sideIdxB, chevronCount]
  sideTicks: number[]; // per side 0:AB 1:BC 2:CD 3:DA
  angleArcs: number[]; // per vertex A,B,C,D
  rightAngles: number[]; // vertex indices with a right angle
  diag: { bisect?: boolean; congruent?: boolean; perpendicular?: boolean };
  label: string;
}

const SHAPES: Record<QuadShapeConfig["type"], Spec> = {
  parallelogram: { v: [[0, 0], [6, 0], [8, 3.6], [2, 3.6]], parallels: [[0, 2, 1], [1, 3, 2]], sideTicks: [1, 2, 1, 2], angleArcs: [1, 2, 1, 2], rightAngles: [], diag: { bisect: true }, label: "parallelogram" },
  rectangle: { v: [[0, 0], [7, 0], [7, 4], [0, 4]], parallels: [[0, 2, 1], [1, 3, 2]], sideTicks: [1, 2, 1, 2], angleArcs: [], rightAngles: [0, 1, 2, 3], diag: { bisect: true, congruent: true }, label: "rectangle" },
  rhombus: { v: [[0, 0], [5, 0], [8, 4], [3, 4]], parallels: [[0, 2, 1], [1, 3, 2]], sideTicks: [1, 1, 1, 1], angleArcs: [1, 2, 1, 2], rightAngles: [], diag: { bisect: true, perpendicular: true }, label: "rhombus" },
  square: { v: [[0, 0], [5, 0], [5, 5], [0, 5]], parallels: [[0, 2, 1], [1, 3, 2]], sideTicks: [1, 1, 1, 1], angleArcs: [], rightAngles: [0, 1, 2, 3], diag: { bisect: true, congruent: true, perpendicular: true }, label: "square" },
  trapezoid: { v: [[0, 0], [8, 0], [5, 4], [2, 4]], parallels: [[0, 2, 1]], sideTicks: [0, 0, 0, 0], angleArcs: [], rightAngles: [], diag: {}, label: "trapezoid" },
  "isosceles-trapezoid": { v: [[0, 0], [8, 0], [6, 4], [2, 4]], parallels: [[0, 2, 1]], sideTicks: [0, 2, 0, 2], angleArcs: [1, 1, 2, 2], rightAngles: [], diag: { congruent: true }, label: "isosceles trapezoid" },
  kite: { v: [[3, 7], [6, 3], [3, 0], [0, 3]], parallels: [], sideTicks: [1, 2, 2, 1], angleArcs: [], rightAngles: [], diag: { perpendicular: true }, label: "kite" },
};

function lineIntersect(p1: XY, p2: XY, p3: XY, p4: XY): XY {
  const d = (p1.x - p2.x) * (p3.y - p4.y) - (p1.y - p2.y) * (p3.x - p4.x);
  const a = p1.x * p2.y - p1.y * p2.x;
  const b = p3.x * p4.y - p3.y * p4.x;
  return { x: (a * (p3.x - p4.x) - (p1.x - p2.x) * b) / d, y: (a * (p3.y - p4.y) - (p1.y - p2.y) * b) / d };
}

export default function QuadShape({ config }: { config: QuadShapeConfig }) {
  const { type, showDiagonals = false, caption } = config;
  const spec = SHAPES[type];
  const [diagOn, setDiagOn] = useState(false);

  const V = spec.v.map(([x, y]) => ({ x, y }));
  const [A, B, C, D] = V;
  const sideEnds: [XY, XY][] = [[A, B], [B, C], [C, D], [D, A]];

  // fit
  const minX = Math.min(...V.map((p) => p.x)) - 1;
  const maxX = Math.max(...V.map((p) => p.x)) + 1;
  const minY = Math.min(...V.map((p) => p.y)) - 1;
  const maxY = Math.max(...V.map((p) => p.y)) + 1;
  const scale = Math.min((W - 30) / (maxX - minX), (H - 30) / (maxY - minY));
  const ox = (W - (maxX - minX) * scale) / 2;
  const oy = (H - (maxY - minY) * scale) / 2;
  const sx = (x: number) => ox + (x - minX) * scale;
  const sy = (y: number) => H - (oy + (y - minY) * scale);
  const S = (p: XY) => ({ x: sx(p.x), y: sy(p.y) });

  const degOf = (from: XY, to: XY) => (Math.atan2(sy(to.y) - sy(from.y), sx(to.x) - sx(from.x)) * 180) / Math.PI;
  const rad = (d: number) => (d * Math.PI) / 180;

  const Ticks = ({ p, q, n, c = "var(--fg-2)" }: { p: XY; q: XY; n: number; c?: string }) => {
    if (n <= 0) return null;
    const a = S(p), b = S(q);
    const mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2;
    const ang = Math.atan2(b.y - a.y, b.x - a.x);
    const nx = Math.cos(ang + Math.PI / 2), ny = Math.sin(ang + Math.PI / 2);
    const ux = Math.cos(ang), uy = Math.sin(ang);
    return (
      <>
        {Array.from({ length: n }, (_, i) => {
          const off = (i - (n - 1) / 2) * 4.5;
          return <line key={i} x1={mx + ux * off - nx * 4.5} y1={my + uy * off - ny * 4.5} x2={mx + ux * off + nx * 4.5} y2={my + uy * off + ny * 4.5} stroke={c} strokeWidth={1.4} />;
        })}
      </>
    );
  };

  const Chevrons = ({ p, q, n }: { p: XY; q: XY; n: number }) => {
    const a = S(p), b = S(q);
    const mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2;
    const ang = Math.atan2(b.y - a.y, b.x - a.x);
    const ux = Math.cos(ang), uy = Math.sin(ang);
    const nx = Math.cos(ang + Math.PI / 2), ny = Math.sin(ang + Math.PI / 2);
    return (
      <>
        {Array.from({ length: n }, (_, i) => {
          const base = mx + ux * (i - (n - 1) / 2) * 5, baseY = my + uy * (i - (n - 1) / 2) * 5;
          const tip = { x: base + ux * 3, y: baseY + uy * 3 };
          return (
            <g key={i}>
              <line x1={base - ux * 3 + nx * 4} y1={baseY - uy * 3 + ny * 4} x2={tip.x} y2={tip.y} stroke={GEO_BLUE} strokeWidth={1.7} strokeLinecap="round" />
              <line x1={base - ux * 3 - nx * 4} y1={baseY - uy * 3 - ny * 4} x2={tip.x} y2={tip.y} stroke={GEO_BLUE} strokeWidth={1.7} strokeLinecap="round" />
            </g>
          );
        })}
      </>
    );
  };

  const RightSquare = ({ at, u, w, c = GEO_ACCENT }: { at: XY; u: XY; w: XY; c?: string }) => {
    const a1 = rad(degOf(at, u)), a2 = rad(degOf(at, w));
    const s = 9;
    const d1 = { x: Math.cos(a1), y: Math.sin(a1) }, d2 = { x: Math.cos(a2), y: Math.sin(a2) };
    const c0 = S(at);
    return <path d={`M ${c0.x + d1.x * s} ${c0.y + d1.y * s} L ${c0.x + (d1.x + d2.x) * s} ${c0.y + (d1.y + d2.y) * s} L ${c0.x + d2.x * s} ${c0.y + d2.y * s}`} fill="none" stroke={c} strokeWidth={1.5} />;
  };

  const Arc = ({ v, prev, next, n }: { v: XY; prev: XY; next: XY; n: number }) => {
    if (n <= 0) return null;
    const a1 = degOf(v, prev), a2 = degOf(v, next);
    const c0 = S(v);
    return (
      <>
        {Array.from({ length: n }, (_, i) => (
          <path key={i} d={arcPath(c0.x, c0.y, 12 + i * 4, a1, a2)} fill="none" stroke={GEO_ACCENT} strokeWidth={1.5} />
        ))}
      </>
    );
  };

  const showDiags = diagOn && showDiagonals;
  const center = showDiags ? lineIntersect(A, C, B, D) : null;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        {/* diagonals */}
        {showDiags && (
          <g>
            <line x1={sx(A.x)} y1={sy(A.y)} x2={sx(C.x)} y2={sy(C.y)} stroke={GEO_BLUE} strokeWidth={1.7} strokeDasharray="5 4" />
            <line x1={sx(B.x)} y1={sy(B.y)} x2={sx(D.x)} y2={sy(D.y)} stroke={GEO_BLUE} strokeWidth={1.7} strokeDasharray="5 4" />
            {center && spec.diag.perpendicular && <RightSquare at={center} u={A} w={B} c={GEO_BLUE} />}
            {center && spec.diag.bisect && !spec.diag.congruent && (
              <>
                <Ticks p={A} q={center} n={1} c={GEO_BLUE} /><Ticks p={center} q={C} n={1} c={GEO_BLUE} />
                <Ticks p={B} q={center} n={2} c={GEO_BLUE} /><Ticks p={center} q={D} n={2} c={GEO_BLUE} />
              </>
            )}
            {spec.diag.congruent && (<><Ticks p={A} q={C} n={1} c={GEO_BLUE} /><Ticks p={B} q={D} n={1} c={GEO_BLUE} /></>)}
            {center && <circle cx={sx(center.x)} cy={sy(center.y)} r={3} fill={GEO_BLUE} />}
          </g>
        )}
        {/* quad outline */}
        <polygon points={V.map((p) => `${sx(p.x)},${sy(p.y)}`).join(" ")} fill="rgba(120,120,120,0.06)" stroke="var(--fg-1)" strokeWidth={2} strokeLinejoin="round" />
        {/* parallel chevrons */}
        {spec.parallels.map(([a, b, cnt], i) => (
          <g key={`p${i}`}>
            <Chevrons p={sideEnds[a][0]} q={sideEnds[a][1]} n={cnt} />
            <Chevrons p={sideEnds[b][0]} q={sideEnds[b][1]} n={cnt} />
          </g>
        ))}
        {/* side ticks */}
        {spec.sideTicks.map((n, i) => <Ticks key={`t${i}`} p={sideEnds[i][0]} q={sideEnds[i][1]} n={n} />)}
        {/* right angles */}
        {spec.rightAngles.map((k) => <RightSquare key={`r${k}`} at={V[k]} u={V[(k + 1) % 4]} w={V[(k + 3) % 4]} />)}
        {/* equal-angle arcs */}
        {spec.angleArcs.map((n, k) => <Arc key={`a${k}`} v={V[k]} prev={V[(k + 3) % 4]} next={V[(k + 1) % 4]} n={n} />)}
        {/* vertex labels */}
        {(["A", "B", "C", "D"] as const).map((name, k) => {
          const gx = (A.x + B.x + C.x + D.x) / 4, gy = (A.y + B.y + C.y + D.y) / 4;
          const p = V[k];
          return (
            <g key={name}>
              <circle cx={sx(p.x)} cy={sy(p.y)} r={3} fill="var(--fg)" />
              <text x={sx(p.x) + (p.x < gx ? -14 : 8)} y={sy(p.y) + (p.y < gy ? 16 : -6)} fontSize="13" fontStyle="italic" fontFamily="serif" fill="var(--fg)">{name}</text>
            </g>
          );
        })}
      </svg>

      {showDiagonals && (
        <button
          type="button"
          onClick={() => setDiagOn((s) => !s)}
          className="gm-press mt-3 w-full rounded-xl px-4 py-2.5 text-[14px] font-semibold"
          style={{ background: diagOn ? "var(--bg-2)" : "var(--accent)", border: "1px solid var(--line)", color: diagOn ? "var(--fg)" : "var(--accent-ink, #fff)" }}
        >
          {diagOn ? "Hide the diagonals" : "Draw the diagonals"}
        </button>
      )}

      {showDiags && (
        <div className="mt-3 rounded-xl p-3 text-center text-[13px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
          {spec.diag.perpendicular && <span>The diagonals meet at a <b style={{ color: GEO_BLUE }}>right angle</b>. </span>}
          {spec.diag.congruent && <span>The two diagonals are <b style={{ color: GEO_BLUE }}>equal in length</b>. </span>}
          {spec.diag.bisect && !spec.diag.congruent && !spec.diag.perpendicular && <span>The diagonals <b style={{ color: GEO_BLUE }}>bisect each other</b>. </span>}
          {spec.diag.bisect && (spec.diag.congruent || spec.diag.perpendicular) && <span>They also <b>bisect each other</b>.</span>}
          {Object.keys(spec.diag).length === 0 && <span>In a general trapezoid the diagonals have no special length or angle.</span>}
        </div>
      )}

      {caption && <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>{caption}</div>}
    </div>
  );
}
