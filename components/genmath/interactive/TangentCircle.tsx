"use client";

import { useState } from "react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { type TangentCircleConfig } from "@/lib/genmath-interactive";

// A circle with an external point P and its two tangent lines. Each tangent
// touches the circle where it meets the radius at a RIGHT ANGLE, and the two
// tangent segments PA and PB are always EQUAL. Reveals on tap.
const W = 320;
const H = 260;

export default function TangentCircle({ config }: { config: TangentCircleConfig }) {
  const { color = GEO_ACCENT } = config;
  const [shown, setShown] = useState(false);

  const cx = 130, cy = H / 2, R = 78;
  const O = { x: cx, y: cy };
  const d = 200; // distance O→P (screen units)
  const P = { x: cx + d, y: cy };
  // tangent points: offset angle from the O→P direction is acos(R/d)
  const off = Math.acos(R / d);
  const A = { x: cx + R * Math.cos(-off), y: cy + R * Math.sin(-off) };
  const B = { x: cx + R * Math.cos(off), y: cy + R * Math.sin(off) };

  const RightSq = ({ v, u, w }: { v: any; u: any; w: any }) => {
    const a1 = Math.atan2(u.y - v.y, u.x - v.x), a2 = Math.atan2(w.y - v.y, w.x - v.x);
    const s = 9;
    const d1 = { x: Math.cos(a1), y: Math.sin(a1) }, d2 = { x: Math.cos(a2), y: Math.sin(a2) };
    return <path d={`M ${v.x + d1.x * s} ${v.y + d1.y * s} L ${v.x + (d1.x + d2.x) * s} ${v.y + (d1.y + d2.y) * s} L ${v.x + d2.x * s} ${v.y + d2.y * s}`} fill="none" stroke={GEO_BLUE} strokeWidth={1.5} />;
  };

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        <circle cx={cx} cy={cy} r={R} fill="none" stroke="var(--fg-1)" strokeWidth={2} />
        {shown && (
          <g>
            {/* radii to tangent points */}
            <line x1={cx} y1={cy} x2={A.x} y2={A.y} stroke="var(--fg-2)" strokeWidth={1.5} strokeDasharray="4 3" />
            <line x1={cx} y1={cy} x2={B.x} y2={B.y} stroke="var(--fg-2)" strokeWidth={1.5} strokeDasharray="4 3" />
            {/* tangent segments */}
            <line x1={P.x} y1={P.y} x2={A.x} y2={A.y} stroke={color} strokeWidth={2.2} />
            <line x1={P.x} y1={P.y} x2={B.x} y2={B.y} stroke={color} strokeWidth={2.2} />
            <RightSq v={A} u={O} w={P} />
            <RightSq v={B} u={O} w={P} />
            {/* equal-length ticks on the two tangent segments */}
            {[[P, A], [P, B]].map(([p, q]: any, i) => {
              const mx = (p.x + q.x) / 2, my = (p.y + q.y) / 2;
              const ang = Math.atan2(q.y - p.y, q.x - p.x);
              const nx = Math.cos(ang + Math.PI / 2), ny = Math.sin(ang + Math.PI / 2);
              return <line key={i} x1={mx - nx * 5} y1={my - ny * 5} x2={mx + nx * 5} y2={my + ny * 5} stroke={color} strokeWidth={1.6} />;
            })}
          </g>
        )}
        {/* points */}
        <circle cx={cx} cy={cy} r={3} fill="var(--fg)" /><text x={cx - 6} y={cy + 16} fontSize="12" fontStyle="italic" fontFamily="serif" fill="var(--fg)">O</text>
        <circle cx={P.x} cy={P.y} r={3.2} fill="var(--fg)" /><text x={P.x + 7} y={P.y + 4} fontSize="12" fontStyle="italic" fontFamily="serif" fill="var(--fg)">P</text>
        {shown && (["A", "B"] as const).map((n, i) => {
          const p = i === 0 ? A : B;
          return <g key={n}><circle cx={p.x} cy={p.y} r={3.2} fill="var(--fg)" /><text x={p.x - 12} y={p.y + (i === 0 ? -6 : 14)} fontSize="12" fontStyle="italic" fontFamily="serif" fill="var(--fg)">{n}</text></g>;
        })}
      </svg>

      <button type="button" onClick={() => setShown((s) => !s)} className="gm-press mt-3 w-full rounded-xl px-4 py-2.5 text-[14px] font-semibold" style={{ background: shown ? "var(--bg-2)" : "var(--accent)", border: "1px solid var(--line)", color: shown ? "var(--fg)" : "var(--accent-ink, #fff)" }}>
        {shown ? "Hide the tangents" : "Draw the two tangents from P"}
      </button>

      {shown && (
        <div className="mt-3 rounded-xl p-3 text-center text-[14px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
          Each tangent meets the radius at a <b style={{ color: GEO_BLUE }}>right angle</b>, and the two tangent segments <b style={{ color }}>PA = PB</b> are equal.
        </div>
      )}
    </div>
  );
}
