"use client";

import { useState } from "react";
import { GEO_ACCENT } from "@/components/genmath/interactive/GeoDiagram";
import { midpoint, dist, type XY } from "@/lib/geo";
import { type MidsegmentConfig } from "@/lib/genmath-interactive";

// The Midsegment Theorem made visible: join two side-midpoints and the new
// segment is parallel to the third side and exactly half its length. "one"
// shows a single midsegment against its parallel base (with numeric lengths so
// the half is concrete); "all" draws the medial triangle — four congruent
// pieces. Midpoints and lengths come from lib/geo (unit-tested).
const W = 340;
const H = 250;

const DEFAULT_TRIANGLE: [XY, XY, XY] = [
  { x: 0, y: 0 },
  { x: 8, y: 0 },
  { x: 2, y: 6 },
];

export default function Midsegment({ config }: { config: MidsegmentConfig }) {
  const { show = "one", base = 0, caption, color = GEO_ACCENT } = config;
  const tri: [XY, XY, XY] = config.triangle
    ? [
        { x: config.triangle[0][0], y: config.triangle[0][1] },
        { x: config.triangle[1][0], y: config.triangle[1][1] },
        { x: config.triangle[2][0], y: config.triangle[2][1] },
      ]
    : DEFAULT_TRIANGLE;
  const [A, B, C] = tri;
  const [shown, setShown] = useState(false);

  const mAB = midpoint(A, B);
  const mBC = midpoint(B, C);
  const mCA = midpoint(C, A);

  // For "one": pick the base side and the midsegment parallel to it.
  // base 0 = AB, 1 = BC, 2 = CA. The midsegment joins the midpoints of the
  // OTHER two sides.
  const CONFIGS = [
    { baseEnds: [A, B] as [XY, XY], mseg: [mCA, mBC] as [XY, XY], baseName: "AB" },
    { baseEnds: [B, C] as [XY, XY], mseg: [mAB, mCA] as [XY, XY], baseName: "BC" },
    { baseEnds: [C, A] as [XY, XY], mseg: [mBC, mAB] as [XY, XY], baseName: "CA" },
  ];
  const one = CONFIGS[base % 3];
  const baseLen = dist(one.baseEnds[0], one.baseEnds[1]);
  const msegLen = dist(one.mseg[0], one.mseg[1]);

  // fit
  const pts = [A, B, C];
  const minX = Math.min(...pts.map((p) => p.x)) - 0.8;
  const maxX = Math.max(...pts.map((p) => p.x)) + 0.8;
  const minY = Math.min(...pts.map((p) => p.y)) - 0.8;
  const maxY = Math.max(...pts.map((p) => p.y)) + 0.8;
  const scale = Math.min((W - 30) / (maxX - minX), (H - 40) / (maxY - minY));
  const ox = (W - (maxX - minX) * scale) / 2;
  const oy = (H - (maxY - minY) * scale) / 2;
  const sx = (x: number) => ox + (x - minX) * scale;
  const sy = (y: number) => H - (oy + (y - minY) * scale);

  const fmt = (n: number) => (Math.round(n * 10) / 10).toString();

  // a ">" chevron centered at the screen midpoint of p→q, pointing along it.
  const Chevron = ({ p, q, c }: { p: XY; q: XY; c: string }) => {
    const x1 = sx(p.x), y1 = sy(p.y), x2 = sx(q.x), y2 = sy(q.y);
    const mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
    const ang = Math.atan2(y2 - y1, x2 - x1);
    const ux = Math.cos(ang), uy = Math.sin(ang);
    const nx = Math.cos(ang + Math.PI / 2), ny = Math.sin(ang + Math.PI / 2);
    const tip = { x: mx + ux * 3.5, y: my + uy * 3.5 };
    const a = { x: mx - ux * 3.5 + nx * 4.5, y: my - uy * 3.5 + ny * 4.5 };
    const b = { x: mx - ux * 3.5 - nx * 4.5, y: my - uy * 3.5 - ny * 4.5 };
    return (
      <g>
        <line x1={a.x} y1={a.y} x2={tip.x} y2={tip.y} stroke={c} strokeWidth={1.8} strokeLinecap="round" />
        <line x1={b.x} y1={b.y} x2={tip.x} y2={tip.y} stroke={c} strokeWidth={1.8} strokeLinecap="round" />
      </g>
    );
  };

  const Tick = ({ p, q, n }: { p: XY; q: XY; n: number }) => {
    const x1 = sx(p.x), y1 = sy(p.y), x2 = sx(q.x), y2 = sy(q.y);
    const mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
    const ang = Math.atan2(y2 - y1, x2 - x1);
    const nx = Math.cos(ang + Math.PI / 2), ny = Math.sin(ang + Math.PI / 2);
    const ux = Math.cos(ang), uy = Math.sin(ang);
    const marks = [];
    for (let i = 0; i < n; i++) {
      const off = (i - (n - 1) / 2) * 4.5;
      marks.push(<line key={i} x1={mx + ux * off - nx * 4.5} y1={my + uy * off - ny * 4.5} x2={mx + ux * off + nx * 4.5} y2={my + uy * off + ny * 4.5} stroke="var(--fg-2)" strokeWidth={1.4} />);
    }
    return <>{marks}</>;
  };

  const seg = (p: XY, q: XY, c: string, key: string, w = 2) => (
    <line key={key} x1={sx(p.x)} y1={sy(p.y)} x2={sx(q.x)} y2={sy(q.y)} stroke={c} strokeWidth={w} strokeLinecap="round" />
  );

  const dot = (p: XY, key: string, c = "var(--fg-2)") => (
    <circle key={key} cx={sx(p.x)} cy={sy(p.y)} r={3} fill={c} />
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 360, display: "block", margin: "0 auto" }}>
        {/* medial-triangle fill for "all" */}
        {shown && show === "all" && (
          <polygon points={`${sx(mAB.x)},${sy(mAB.y)} ${sx(mBC.x)},${sy(mBC.y)} ${sx(mCA.x)},${sy(mCA.y)}`} fill={`${color}22`} stroke="none" />
        )}
        {/* triangle */}
        <polygon points={`${sx(A.x)},${sy(A.y)} ${sx(B.x)},${sy(B.y)} ${sx(C.x)},${sy(C.y)}`} fill="rgba(120,120,120,0.05)" stroke="var(--fg-1)" strokeWidth={2} strokeLinejoin="round" />

        {shown && show === "one" && (
          <g>
            {/* emphasize the base + the midsegment, mark them parallel */}
            {seg(one.baseEnds[0], one.baseEnds[1], "var(--fg-1)", "base", 3)}
            {seg(one.mseg[0], one.mseg[1], color, "mseg", 3)}
            <Chevron p={one.baseEnds[0]} q={one.baseEnds[1]} c="var(--fg-1)" />
            <Chevron p={one.mseg[0]} q={one.mseg[1]} c={color} />
            {/* midpoint ticks on the two split sides */}
            {base === 0 && (<><Tick p={C} q={mCA} n={1} /><Tick p={mCA} q={A} n={1} /><Tick p={C} q={mBC} n={2} /><Tick p={mBC} q={B} n={2} /></>)}
            {base === 1 && (<><Tick p={A} q={mAB} n={1} /><Tick p={mAB} q={B} n={1} /><Tick p={A} q={mCA} n={2} /><Tick p={mCA} q={C} n={2} /></>)}
            {base === 2 && (<><Tick p={B} q={mBC} n={1} /><Tick p={mBC} q={C} n={1} /><Tick p={B} q={mAB} n={2} /><Tick p={mAB} q={A} n={2} /></>)}
            {dot(one.mseg[0], "e0", color)}{dot(one.mseg[1], "e1", color)}
          </g>
        )}

        {shown && show === "all" && (
          <g>
            {seg(mAB, mBC, color, "m0", 2.4)}
            {seg(mBC, mCA, color, "m1", 2.4)}
            {seg(mCA, mAB, color, "m2", 2.4)}
            {dot(mAB, "d0", color)}{dot(mBC, "d1", color)}{dot(mCA, "d2", color)}
          </g>
        )}

        {/* vertex dots + names */}
        {([["A", A], ["B", B], ["C", C]] as [string, XY][]).map(([n, p]) => {
          const gx = (A.x + B.x + C.x) / 3, gy = (A.y + B.y + C.y) / 3;
          return (
            <g key={n}>
              <circle cx={sx(p.x)} cy={sy(p.y)} r={3.2} fill="var(--fg)" />
              <text x={sx(p.x) + (p.x < gx ? -14 : 8)} y={sy(p.y) + (p.y < gy ? 16 : -6)} fontSize="13" fontStyle="italic" fontFamily="serif" fill="var(--fg)">{n}</text>
            </g>
          );
        })}
      </svg>

      <button
        type="button"
        onClick={() => setShown((s) => !s)}
        className="gm-press mt-3 w-full rounded-xl px-4 py-2.5 text-[14px] font-semibold"
        style={{ background: shown ? "var(--bg-2)" : "var(--accent)", border: "1px solid var(--line)", color: shown ? "var(--fg)" : "var(--accent-ink, #fff)" }}
      >
        {shown ? "Hide" : show === "all" ? "Join all three midpoints" : "Draw the midsegment"}
      </button>

      {shown && show === "one" && (
        <div className="mt-3 rounded-xl p-3 text-center text-[14px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
          Midsegment <span className="serif tabular" style={{ color }}>{fmt(msegLen)}</span> is half of base {one.baseName} <span className="serif tabular">{fmt(baseLen)}</span> — and the two are <b>parallel</b>.
        </div>
      )}
      {shown && show === "all" && (
        <div className="mt-3 rounded-xl p-3 text-center text-[14px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
          The three midsegments cut the triangle into <b style={{ color }}>four congruent triangles</b>.
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
