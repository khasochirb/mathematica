"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { arcPath, GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { pointOnCircle, inscribedAngle } from "@/lib/geo";
import { type CircleAngleConfig } from "@/lib/genmath-interactive";

// A circle with an adjustable central angle AOB. The intercepted arc AB always
// measures the same as the central angle. In "inscribed" mode a point C on the
// far arc adds an inscribed angle ACB that is always HALF the central angle —
// the Inscribed Angle Theorem, live.
const W = 320;
const H = 300;
const STEPS = [40, 60, 80, 100, 120, 140, 160];

export default function CircleAngle({ config }: { config: CircleAngleConfig }) {
  const { mode, color = GEO_ACCENT } = config;
  const [ti, setTi] = useState(() => {
    const i = STEPS.indexOf(config.start ?? 100);
    return i < 0 ? 3 : i;
  });
  const theta = STEPS[ti];

  const cx = W / 2, cy = H / 2 - 4, R = 100;
  const O = { x: cx, y: cy };
  // A and B on the circle, arc centred at the top (screen: up = -y)
  const A = { x: cx + R * Math.cos(((-90 - theta / 2) * Math.PI) / 180), y: cy + R * Math.sin(((-90 - theta / 2) * Math.PI) / 180) };
  const B = { x: cx + R * Math.cos(((-90 + theta / 2) * Math.PI) / 180), y: cy + R * Math.sin(((-90 + theta / 2) * Math.PI) / 180) };
  const C = { x: cx + R * Math.cos((90 * Math.PI) / 180), y: cy + R * Math.sin((90 * Math.PI) / 180) }; // bottom
  const degS = (from: any, to: any) => (Math.atan2(to.y - from.y, to.x - from.x) * 180) / Math.PI;
  void pointOnCircle;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        <circle cx={cx} cy={cy} r={R} fill="none" stroke="var(--fg-1)" strokeWidth={2} />
        {/* highlighted arc AB (the top minor arc) */}
        <path d={arcPath(cx, cy, R, degS(O, A), degS(O, B))} fill="none" stroke={color} strokeWidth={4} />
        <text x={cx} y={cy - R - 8} fontSize="12" textAnchor="middle" fill={color} fontWeight={700}>arc = {theta}°</text>
        {/* radii + central angle */}
        <line x1={cx} y1={cy} x2={A.x} y2={A.y} stroke="var(--fg-1)" strokeWidth={1.8} />
        <line x1={cx} y1={cy} x2={B.x} y2={B.y} stroke="var(--fg-1)" strokeWidth={1.8} />
        <path d={arcPath(cx, cy, 26, degS(O, A), degS(O, B))} fill="none" stroke={GEO_BLUE} strokeWidth={2} />
        <text x={cx} y={cy - 34} fontSize="12" textAnchor="middle" fill={GEO_BLUE} fontWeight={700}>{theta}°</text>
        {/* inscribed angle */}
        {mode === "inscribed" && (
          <g>
            <line x1={C.x} y1={C.y} x2={A.x} y2={A.y} stroke={GEO_ACCENT} strokeWidth={1.8} />
            <line x1={C.x} y1={C.y} x2={B.x} y2={B.y} stroke={GEO_ACCENT} strokeWidth={1.8} />
            <path d={arcPath(C.x, C.y, 24, degS(C, A), degS(C, B))} fill="none" stroke={GEO_ACCENT} strokeWidth={2} />
            <text x={C.x} y={C.y + 34} fontSize="12" textAnchor="middle" fill={GEO_ACCENT} fontWeight={700}>{inscribedAngle(theta)}°</text>
          </g>
        )}
        {/* labels */}
        {[["A", A, -1], ["B", B, 1]].map(([n, p, s]: any) => (
          <g key={n}><circle cx={p.x} cy={p.y} r={3.2} fill="var(--fg)" /><text x={p.x + s * 10} y={p.y - 6} fontSize="12" fontStyle="italic" fontFamily="serif" fill="var(--fg)">{n}</text></g>
        ))}
        {mode === "inscribed" && <g><circle cx={C.x} cy={C.y} r={3.2} fill="var(--fg)" /><text x={C.x} y={C.y + 18} fontSize="12" fontStyle="italic" fontFamily="serif" fill="var(--fg)">C</text></g>}
        <circle cx={cx} cy={cy} r={3} fill="var(--fg)" /><text x={cx + 7} y={cy + 14} fontSize="12" fontStyle="italic" fontFamily="serif" fill="var(--fg)">O</text>
      </svg>

      <div className="mt-2 rounded-xl p-3 text-center text-[14px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        {mode === "central" ? (
          <>
            <div className="serif tabular">central angle <b style={{ color: GEO_BLUE }}>{theta}°</b> = arc <b style={{ color }}>{theta}°</b></div>
            <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>A central angle equals the measure of the arc it cuts off.</div>
          </>
        ) : (
          <>
            <div className="serif tabular">inscribed <b style={{ color: GEO_ACCENT }}>{inscribedAngle(theta)}°</b> = ½ of central <b style={{ color: GEO_BLUE }}>{theta}°</b></div>
            <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>An inscribed angle is half the central angle on the same arc.</div>
          </>
        )}
      </div>

      <div className="mt-4 flex items-center justify-center gap-3">
        <span className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>central angle</span>
        <button type="button" onClick={() => setTi((v) => Math.max(0, v - 1))} disabled={ti <= 0} aria-label="Smaller" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 44, fontSize: 17, color: "var(--fg)" }}>{theta}°</div>
        <button type="button" onClick={() => setTi((v) => Math.min(STEPS.length - 1, v + 1))} disabled={ti >= STEPS.length - 1} aria-label="Larger" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
    </div>
  );
}
