"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { arcPath, GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { arcLength, sectorArea } from "@/lib/geo";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type ArcSectorConfig } from "@/lib/genmath-interactive";

// A circle with an adjustable central angle θ. The shaded sector's arc length is
// the fraction θ/360 of the circumference, and its area is θ/360 of the circle's
// area. Both are shown symbolically (as multiples of π) and numerically.
const W = 320;
const H = 300;
const STEPS = [30, 45, 60, 90, 120, 180, 270];

export default function ArcSector({ config }: { config: ArcSectorConfig }) {
  const { radius = 6, color = GEO_ACCENT } = config;
  const [ti, setTi] = useState(() => {
    const i = STEPS.indexOf(config.start ?? 90);
    return i < 0 ? 3 : i;
  });
  const theta = STEPS[ti];
  // the drawn sector glides between steps; every readout uses the exact theta
  const thetaDraw = useAnimatedValue(theta, { stiffness: 160, damping: 22, from: 0 }); // the sector unfurls on entry
  const cx = W / 2, cy = H / 2 - 4, R = 100;

  // sector from angle -90 (top) sweeping clockwise on screen... use start at right (0) going CCW in math but screen y down. We'll draw from 0° sweeping by theta.
  const start = -90; // start at top (screen)
  const p1 = { x: cx + R * Math.cos((start * Math.PI) / 180), y: cy + R * Math.sin((start * Math.PI) / 180) };
  const end = start + thetaDraw;
  const p2 = { x: cx + R * Math.cos((end * Math.PI) / 180), y: cy + R * Math.sin((end * Math.PI) / 180) };
  const large = thetaDraw > 180 ? 1 : 0;
  const sectorPath = `M ${cx} ${cy} L ${p1.x} ${p1.y} A ${R} ${R} 0 ${large} 1 ${p2.x} ${p2.y} Z`;

  // exact multiples of π, reduced
  const gcd = (a: number, b: number): number => (b ? gcd(b, a % b) : a);
  const frac = (num: number, den: number) => {
    const g = gcd(Math.round(num), den) || 1;
    const n = Math.round(num) / g, d = den / g;
    return d === 1 ? `${n}` : `${n}/${d}`;
  };
  const arcCoef = frac(theta * 2 * radius, 360); // arcLength = (θ·2r/360)·π
  const areaCoef = frac(theta * radius * radius, 360); // sectorArea = (θ·r²/360)·π
  const fmt = (n: number) => (Number.isInteger(n) ? n.toString() : n.toFixed(2));

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        <circle cx={cx} cy={cy} r={R} fill="none" stroke="var(--fg-1)" strokeWidth={2} />
        <path d={sectorPath} fill={`${color}22`} stroke="none" />
        <path d={arcPath(cx, cy, R, start, end)} fill="none" stroke={color} strokeWidth={4} />
        <line x1={cx} y1={cy} x2={p1.x} y2={p1.y} stroke="var(--fg-1)" strokeWidth={1.8} />
        <line x1={cx} y1={cy} x2={p2.x} y2={p2.y} stroke="var(--fg-1)" strokeWidth={1.8} />
        <path d={arcPath(cx, cy, 26, start, end)} fill="none" stroke={GEO_BLUE} strokeWidth={2} />
        <circle cx={cx} cy={cy} r={3} fill="var(--fg)" />
        <text x={cx + 4} y={cy - 8} fontSize="12" fill={GEO_BLUE} fontWeight={700}>{theta}°</text>
        {/* radius label */}
        <text x={(cx + p1.x) / 2 - 6} y={(cy + p1.y) / 2} fontSize="11" fill="var(--fg-2)">r = {radius}</text>
      </svg>

      <div className="mt-2 grid grid-cols-2 gap-2 text-center text-[13px]">
        <div className="rounded-xl p-2" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
          <div className="serif" style={{ color, fontWeight: 700 }}>arc length</div>
          <div className="text-[10px]" style={{ color: "var(--fg-3)" }}>(θ/360)·2πr</div>
          <div className="serif tabular" style={{ color: "var(--fg)", fontSize: 14 }}>{arcCoef}π ≈ {fmt(arcLength(theta, radius))}</div>
        </div>
        <div className="rounded-xl p-2" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
          <div className="serif" style={{ color: GEO_BLUE, fontWeight: 700 }}>sector area</div>
          <div className="text-[10px]" style={{ color: "var(--fg-3)" }}>(θ/360)·πr²</div>
          <div className="serif tabular" style={{ color: "var(--fg)", fontSize: 14 }}>{areaCoef}π ≈ {fmt(sectorArea(theta, radius))}</div>
        </div>
      </div>

      <div className="mt-4 flex items-center justify-center gap-3">
        <span className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>angle θ</span>
        <button type="button" onClick={() => setTi((v) => Math.max(0, v - 1))} disabled={ti <= 0} aria-label="Smaller" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 44, fontSize: 17, color: "var(--fg)" }}>{theta}°</div>
        <button type="button" onClick={() => setTi((v) => Math.min(STEPS.length - 1, v + 1))} disabled={ti >= STEPS.length - 1} aria-label="Larger" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
    </div>
  );
}
