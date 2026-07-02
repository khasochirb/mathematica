"use client";

import { useState } from "react";
import { arcPath, GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import {
  centroid,
  circumcenter,
  incenter,
  orthocenter,
  perpFoot,
  midpoint,
  dist,
  type XY,
} from "@/lib/geo";
import { type TriangleCentersConfig } from "@/lib/genmath-interactive";

// One triangle, one family of concurrent special segments, and the single point
// where they meet. Perpendicular bisectors → circumcenter, angle bisectors →
// incenter, medians → centroid, altitudes → orthocenter. The construction and
// the meeting point are computed exactly from lib/geo (unit-tested), so the
// picture can never lie about where the lines cross.
const W = 340;
const H = 260;

type Center = "circumcenter" | "incenter" | "centroid" | "orthocenter";

const INFO: Record<Center, { name: string; property: string; color: string }> = {
  circumcenter: { name: "circumcenter", property: "the same distance from all three vertices", color: GEO_BLUE },
  incenter: { name: "incenter", property: "the same distance from all three sides", color: "#3fa06a" },
  centroid: { name: "centroid", property: "the balance point — ⅔ of the way down each median", color: GEO_ACCENT },
  orthocenter: { name: "orthocenter", property: "where the three altitudes meet", color: "#c05a9e" },
};

const DEFAULT_TRIANGLE: [XY, XY, XY] = [
  { x: 1, y: 1 },
  { x: 9, y: 1 },
  { x: 4.2, y: 7.2 },
];

export default function TriangleCenters({ config }: { config: TriangleCentersConfig }) {
  const { center, showCircle = false, caption } = config;
  const tri: [XY, XY, XY] = config.triangle
    ? [
        { x: config.triangle[0][0], y: config.triangle[0][1] },
        { x: config.triangle[1][0], y: config.triangle[1][1] },
        { x: config.triangle[2][0], y: config.triangle[2][1] },
      ]
    : DEFAULT_TRIANGLE;
  const [A, B, C] = tri;
  const [shown, setShown] = useState(false); // reveal the segments + point on tap

  const info = INFO[center];
  const P =
    center === "circumcenter"
      ? circumcenter(A, B, C)
      : center === "incenter"
      ? incenter(A, B, C)
      : center === "centroid"
      ? centroid(A, B, C)
      : orthocenter(A, B, C);

  // radius for the optional circle
  const circleR =
    center === "circumcenter"
      ? dist(P, A)
      : center === "incenter"
      ? dist(P, perpFoot(P, A, B))
      : 0;

  // fit everything into the viewBox
  const extra: XY[] = [];
  if (showCircle && circleR > 0) {
    extra.push({ x: P.x + circleR, y: P.y }, { x: P.x - circleR, y: P.y }, { x: P.x, y: P.y + circleR }, { x: P.x, y: P.y - circleR });
  } else {
    extra.push(P);
  }
  const pts = [A, B, C, ...extra];
  const minX = Math.min(...pts.map((p) => p.x)) - 0.8;
  const maxX = Math.max(...pts.map((p) => p.x)) + 0.8;
  const minY = Math.min(...pts.map((p) => p.y)) - 0.8;
  const maxY = Math.max(...pts.map((p) => p.y)) + 0.8;
  const scale = Math.min((W - 30) / (maxX - minX), (H - 30) / (maxY - minY));
  const ox = (W - (maxX - minX) * scale) / 2;
  const oy = (H - (maxY - minY) * scale) / 2;
  const sx = (x: number) => ox + (x - minX) * scale;
  const sy = (y: number) => H - (oy + (y - minY) * scale);

  const degOf = (from: XY, to: XY) => (Math.atan2(sy(to.y) - sy(from.y), sx(to.x) - sx(from.x)) * 180) / Math.PI;
  const rad = (d: number) => (d * Math.PI) / 180;

  // a small right-angle square at diagram point `at`, between the screen
  // directions toward u and v.
  const RightSquare = ({ at, u, v }: { at: XY; u: XY; v: XY }) => {
    const a1 = rad(degOf(at, u));
    const a2 = rad(degOf(at, v));
    const s = 9;
    const d1 = { x: Math.cos(a1), y: Math.sin(a1) };
    const d2 = { x: Math.cos(a2), y: Math.sin(a2) };
    const c = { x: sx(at.x), y: sy(at.y) };
    return (
      <path
        d={`M ${c.x + d1.x * s} ${c.y + d1.y * s} L ${c.x + (d1.x + d2.x) * s} ${c.y + (d1.y + d2.y) * s} L ${c.x + d2.x * s} ${c.y + d2.y * s}`}
        fill="none"
        stroke={info.color}
        strokeWidth={1.5}
      />
    );
  };

  // two adjacent equal arcs at a vertex, split by the bisector toward P.
  const BisectorArcs = ({ v, p1, p2 }: { v: XY; p1: XY; p2: XY }) => {
    const a1 = degOf(v, p1);
    const ab = degOf(v, P);
    const a2 = degOf(v, p2);
    const r = 17;
    return (
      <g>
        <path d={arcPath(sx(v.x), sy(v.y), r, a1, ab)} fill="none" stroke={info.color} strokeWidth={1.6} />
        <path d={arcPath(sx(v.x), sy(v.y), r, ab, a2)} fill="none" stroke={info.color} strokeWidth={1.6} />
      </g>
    );
  };

  // congruence ticks at the midpoint of the screen segment from p→q.
  const Tick = ({ p, q, n }: { p: XY; q: XY; n: number }) => {
    const x1 = sx(p.x), y1 = sy(p.y), x2 = sx(q.x), y2 = sy(q.y);
    const mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
    const ang = Math.atan2(y2 - y1, x2 - x1);
    const nx = Math.cos(ang + Math.PI / 2), ny = Math.sin(ang + Math.PI / 2);
    const ux = Math.cos(ang), uy = Math.sin(ang);
    const marks = [];
    for (let i = 0; i < n; i++) {
      const off = (i - (n - 1) / 2) * 4.5;
      marks.push(
        <line key={i} x1={mx + ux * off - nx * 4.5} y1={my + uy * off - ny * 4.5} x2={mx + ux * off + nx * 4.5} y2={my + uy * off + ny * 4.5} stroke="var(--fg-2)" strokeWidth={1.4} />
      );
    }
    return <>{marks}</>;
  };

  // opposite-side midpoints, feet, etc.
  const mAB = midpoint(A, B);
  const mBC = midpoint(B, C);
  const mCA = midpoint(C, A);

  // Build the construction segments (from → to) + their decorations.
  const line = (p: XY, q: XY, key: string, dashed = true) => (
    <line key={key} x1={sx(p.x)} y1={sy(p.y)} x2={sx(q.x)} y2={sy(q.y)} stroke={info.color} strokeWidth={1.8} strokeDasharray={dashed ? "5 4" : undefined} strokeLinecap="round" />
  );

  const construction = () => {
    if (center === "centroid") {
      return (
        <g>
          {line(A, mBC, "mA", false)}
          {line(B, mCA, "mB", false)}
          {line(C, mAB, "mC", false)}
          {/* midpoint ticks: each side's two halves are equal (distinct marks per side) */}
          <Tick p={B} q={mBC} n={1} /><Tick p={mBC} q={C} n={1} />
          <Tick p={C} q={mCA} n={2} /><Tick p={mCA} q={A} n={2} />
          <Tick p={A} q={mAB} n={3} /><Tick p={mAB} q={B} n={3} />
        </g>
      );
    }
    if (center === "circumcenter") {
      return (
        <g>
          {line(mBC, P, "pbA")}{line(mCA, P, "pbB")}{line(mAB, P, "pbC")}
          <RightSquare at={mBC} u={C} v={P} />
          <RightSquare at={mCA} u={A} v={P} />
          <RightSquare at={mAB} u={B} v={P} />
          <Tick p={B} q={mBC} n={1} /><Tick p={mBC} q={C} n={1} />
          <Tick p={C} q={mCA} n={2} /><Tick p={mCA} q={A} n={2} />
          <Tick p={A} q={mAB} n={3} /><Tick p={mAB} q={B} n={3} />
        </g>
      );
    }
    if (center === "incenter") {
      // bisector reaches the opposite side, then continue the arc marks
      const toBC = perpFoot; // unused placeholder to keep imports tidy
      void toBC;
      return (
        <g>
          {line(A, P, "biA")}{line(B, P, "biB")}{line(C, P, "biC")}
          <BisectorArcs v={A} p1={B} p2={C} />
          <BisectorArcs v={B} p1={C} p2={A} />
          <BisectorArcs v={C} p1={A} p2={B} />
        </g>
      );
    }
    // orthocenter — altitudes to the feet
    const fA = perpFoot(A, B, C);
    const fB = perpFoot(B, C, A);
    const fC = perpFoot(C, A, B);
    return (
      <g>
        {line(A, fA, "alA")}{line(B, fB, "alB")}{line(C, fC, "alC")}
        <RightSquare at={fA} u={C} v={A} />
        <RightSquare at={fB} u={A} v={B} />
        <RightSquare at={fC} u={B} v={C} />
      </g>
    );
  };

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 360, display: "block", margin: "0 auto" }}>
        {/* optional circle */}
        {shown && showCircle && circleR > 0 && (
          <circle cx={sx(P.x)} cy={sy(P.y)} r={circleR * scale} fill="none" stroke={info.color} strokeWidth={1.4} strokeDasharray="2 4" opacity={0.9} />
        )}
        {/* triangle */}
        <polygon points={`${sx(A.x)},${sy(A.y)} ${sx(B.x)},${sy(B.y)} ${sx(C.x)},${sy(C.y)}`} fill="rgba(120,120,120,0.06)" stroke="var(--fg-1)" strokeWidth={2} strokeLinejoin="round" />
        {/* construction, revealed on tap */}
        {shown && construction()}
        {/* the center point */}
        {shown && (
          <g>
            <circle cx={sx(P.x)} cy={sy(P.y)} r={5} fill={info.color} stroke="#fff" strokeWidth={1.5} />
          </g>
        )}
        {/* vertex dots + names */}
        {([["A", A], ["B", B], ["C", C]] as [string, XY][]).map(([n, p]) => (
          <g key={n}>
            <circle cx={sx(p.x)} cy={sy(p.y)} r={3.2} fill="var(--fg)" />
            <text x={sx(p.x) + (p.x < (A.x + B.x + C.x) / 3 ? -14 : 8)} y={sy(p.y) + (p.y < (A.y + B.y + C.y) / 3 ? 16 : -6)} fontSize="13" fontStyle="italic" fontFamily="serif" fill="var(--fg)">{n}</text>
          </g>
        ))}
      </svg>

      <button
        type="button"
        onClick={() => setShown((s) => !s)}
        className="gm-press mt-3 w-full rounded-xl px-4 py-2.5 text-[14px] font-semibold"
        style={{ background: shown ? "var(--bg-2)" : "var(--accent)", border: "1px solid var(--line)", color: shown ? "var(--fg)" : "var(--accent-ink, #fff)" }}
      >
        {shown ? "Hide the construction" : `Construct the ${info.name}`}
      </button>

      {shown && (
        <div className="mt-3 rounded-xl p-3 text-center text-[14px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
          The three lines meet at one point — the <b style={{ color: info.color }}>{info.name}</b> — {info.property}.
        </div>
      )}

      {caption && (
        <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
          {caption}
        </div>
      )}
    </div>
  );
}
