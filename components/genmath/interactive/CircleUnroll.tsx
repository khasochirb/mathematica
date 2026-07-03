"use client";

import { useEffect, useState } from "react";
import { RotateCcw } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type CircleUnrollConfig } from "@/lib/genmath-interactive";

// Where π comes from, played out: a circle rolls one full turn along a line,
// unrolling its circumference behind it. Diameter-length ticks mark off the
// trail — it fits 3 of them, plus a bit more. That leftover bit IS the .14159…
// of π. Auto-plays on entry; the counter reads the unrolled length live.
const W = 320;
const H = 190;

export default function CircleUnroll({ config }: { config: CircleUnrollConfig }) {
  const { color = GEO_ACCENT } = config;

  const [go, setGo] = useState(false);
  useEffect(() => {
    const id = setTimeout(() => setGo(true), 700);
    return () => clearTimeout(id);
  }, []);
  // slow, steady roll — critically damped so the wheel never rolls backwards
  const p = useAnimatedValue(go ? 1 : 0, { stiffness: 14, damping: 8 });
  const pc = Math.max(0, Math.min(1, p));
  const replay = () => {
    setGo(false);
    setTimeout(() => setGo(true), 380);
  };

  const R = 36;
  const groundY = 120;
  const startX = 24;
  const circumference = 2 * Math.PI * R;
  const cx = startX + circumference * pc;
  const cy = groundY - R;
  // the rim point that started at the ground contact: rolls with the wheel
  const phi = Math.PI / 2 + 2 * Math.PI * pc; // screen angle (rad) of the marked point
  const mark = { x: cx + R * Math.cos(phi), y: cy + R * Math.sin(phi) };
  const d = 2 * R; // one diameter, in px
  const unrolled = circumference * pc;
  const piSoFar = unrolled / d; // how many diameters have unrolled

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        {/* ground */}
        <line x1={8} y1={groundY} x2={W - 8} y2={groundY} stroke="var(--fg-2)" strokeWidth={1.6} />
        {/* the unrolled circumference so far */}
        <line x1={startX} y1={groundY} x2={cx} y2={groundY} stroke={color} strokeWidth={5} strokeLinecap="round" />
        {/* diameter ticks along the trail: 1d, 2d, 3d — then the little bit extra */}
        {[1, 2, 3].map((k) => (
          <g key={k} opacity={unrolled >= k * d - 0.5 ? 1 : 0.22}>
            <line x1={startX + k * d} y1={groundY - 7} x2={startX + k * d} y2={groundY + 7} stroke={GEO_BLUE} strokeWidth={1.8} />
            <text x={startX + k * d} y={groundY + 22} fontSize="11" textAnchor="middle" fill={GEO_BLUE} fontWeight={700}>{k}d</text>
          </g>
        ))}
        {/* πd marker appears as the wheel finishes */}
        <g opacity={Math.max(0, (pc - 0.94) / 0.06)}>
          {/* label above the line — "3d" sits below, only 0.14d away */}
          <line x1={startX + circumference} y1={groundY - 7} x2={startX + circumference} y2={groundY + 7} stroke={color} strokeWidth={1.8} />
          <text x={startX + circumference + 2} y={groundY - 12} fontSize="11" textAnchor="middle" fill={color} fontWeight={700}>πd</text>
        </g>
        {/* the wheel */}
        <circle cx={cx} cy={cy} r={R} fill="var(--bg-2)" stroke="var(--fg-1)" strokeWidth={2} />
        {/* diameter bar inside the wheel, rolling with it */}
        <line x1={cx - R * Math.cos(phi)} y1={cy - R * Math.sin(phi)} x2={mark.x} y2={mark.y} stroke={GEO_BLUE} strokeWidth={1.6} strokeDasharray="4 3" />
        <text x={cx} y={cy - 6} fontSize="10" textAnchor="middle" fill={GEO_BLUE}>d</text>
        {/* marked rim point + its contact trail */}
        <circle cx={mark.x} cy={mark.y} r={4.5} fill={color} />
        <circle cx={cx} cy={cy} r={2.6} fill="var(--fg)" />
      </svg>

      {/* live counter */}
      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <div className="serif tabular text-[16px]" style={{ color: "var(--fg)" }}>
          unrolled so far: <b style={{ color }}>{piSoFar.toFixed(2)} × d</b>
        </div>
        <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>
          {pc > 0.97
            ? <>One full turn unrolls exactly <b style={{ color: "var(--fg-1)" }}>π ≈ 3.14159…</b> diameters. That's what π <i>is</i>: C = πd.</>
            : <>The wheel lays its circumference on the ground — count the diameters as they fit.</>}
        </div>
      </div>

      <div className="mt-3 flex justify-center">
        <button type="button" onClick={replay} aria-label="Roll again" className="gm-press flex items-center gap-1.5 rounded-full px-4 py-2 text-[13px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}>
          <RotateCcw className="h-3.5 w-3.5" /> Roll it again
        </button>
      </div>
    </div>
  );
}
