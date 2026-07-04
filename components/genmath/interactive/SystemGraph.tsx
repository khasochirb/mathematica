"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type SystemGraphConfig } from "@/lib/genmath-interactive";

// Two lines, one plane — the systems-of-equations workbench. Line 1 is fixed;
// line 2 is adjustable (slope and intercept steppers), and the readout tracks
// the verdict live: one solution (the intersection point, marked), no solution
// (parallel), or infinitely many (the same line twice). Lines glide on their
// springs, and the intersection dot follows the algebra in real time.

function fmt(n: number): string {
  return Number.isInteger(n) ? n.toString() : (Math.round(n * 100) / 100).toString();
}
function eqn(m: number, b: number): string {
  const mPart = m === 1 ? "x" : m === -1 ? "−x" : `${fmt(m)}x`;
  if (b === 0) return `y = ${mPart}`;
  return `y = ${mPart} ${b > 0 ? "+" : "−"} ${fmt(Math.abs(b))}`;
}

export default function SystemGraph({ config }: { config: SystemGraphConfig }) {
  const {
    m1, b1,
    m2: m20, b2: b20,
    interactive = true,
    min = -6, max = 6,
  } = config;

  const [m2, setM2] = useState(m20);
  const [b2, setB2] = useState(b20);

  // both lines glide; line 2 additionally springs when stepped
  const m1d = useAnimatedValue(m1, { stiffness: 140, damping: 20, from: 0 });
  const b1d = useAnimatedValue(b1, { stiffness: 140, damping: 20 });
  const m2d = useAnimatedValue(m2, { stiffness: 140, damping: 20, from: 0 });
  const b2d = useAnimatedValue(b2, { stiffness: 140, damping: 20 });

  const N = max - min;
  const cell = 26;
  const pad = 20;
  const W = N * cell + pad * 2;
  const px = (gx: number) => pad + (gx - min) * cell;
  const py = (gy: number) => pad + (max - gy) * cell;
  const ints = Array.from({ length: N + 1 }, (_, i) => min + i);
  const step = N > 12 ? 2 : 1;

  // verdict from the TARGET values (exact math, not the in-flight spring)
  const parallel = m1 === m2;
  const sameLine = parallel && b1 === b2;
  const ix = parallel ? null : (b2 - b1) / (m1 - m2);
  const iy = ix === null ? null : m1 * ix + b1;
  // the drawn dot follows the springs so it glides with the lines
  const ixd = m1d === m2d ? null : (b2d - b1d) / (m1d - m2d);
  const iyd = ixd === null ? null : m1d * ixd + b1d;

  const clip = (m: number, b: number) => ({ x1: px(min), y1: py(m * min + b), x2: px(max), y2: py(m * max + b) });
  const L1 = clip(m1d, b1d);
  const L2 = clip(m2d, b2d);

  const stepper = (label: string, val: number, set: (f: (v: number) => number) => void, lo: number, hi: number, delta: number) => (
    <div className="text-center">
      <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>{label}</div>
      <div className="mt-1 flex items-center gap-2">
        <button type="button" onClick={() => set((v) => Math.max(lo, v - delta))} disabled={val <= lo} aria-label={`Decrease ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 36, fontSize: 16, color: GEO_BLUE }}>{fmt(val)}</div>
        <button type="button" onClick={() => set((v) => Math.min(hi, v + delta))} disabled={val >= hi} aria-label={`Increase ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
    </div>
  );

  const onGrid = ix !== null && iy !== null && ix >= min && ix <= max && iy >= min && iy <= max;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${W}`} width="100%" style={{ maxWidth: 340 }} role="img" aria-label="Two lines on a coordinate grid">
          {ints.map((g) => (
            <g key={`g${g}`}>
              <line x1={px(g)} y1={py(max)} x2={px(g)} y2={py(min)} stroke="var(--line)" strokeWidth={1} />
              <line x1={px(min)} y1={py(g)} x2={px(max)} y2={py(g)} stroke="var(--line)" strokeWidth={1} />
            </g>
          ))}
          <line x1={px(min)} y1={py(0)} x2={px(max)} y2={py(0)} stroke="var(--fg-2)" strokeWidth={1.8} />
          <line x1={px(0)} y1={py(max)} x2={px(0)} y2={py(min)} stroke="var(--fg-2)" strokeWidth={1.8} />
          <text x={px(max) + 5} y={py(0) + 4} fontSize="11" fill="var(--fg-3)">x</text>
          <text x={px(0) - 4} y={py(max) - 5} fontSize="11" fill="var(--fg-3)" textAnchor="end">y</text>
          {ints.filter((g) => g !== 0 && g % step === 0).map((g) => (
            <g key={`lbl${g}`}>
              <text x={px(g)} y={py(0) + 12} fontSize="8.5" fill="var(--fg-3)" textAnchor="middle">{g}</text>
              <text x={px(0) - 5} y={py(g) + 3} fontSize="8.5" fill="var(--fg-3)" textAnchor="end">{g}</text>
            </g>
          ))}

          {/* the two lines */}
          <line x1={L1.x1} y1={L1.y1} x2={L1.x2} y2={L1.y2} stroke={GEO_ACCENT} strokeWidth={2.6} />
          <line x1={L2.x1} y1={L2.y1} x2={L2.x2} y2={L2.y2} stroke={GEO_BLUE} strokeWidth={2.6} strokeDasharray={sameLine ? "7 5" : undefined} />

          {/* the intersection — the system's one solution */}
          {!parallel && ixd !== null && iyd !== null && onGrid && (
            <g>
              <circle cx={px(ixd)} cy={py(iyd)} r={10} fill="none" stroke="var(--fg)" strokeWidth={1.2} opacity={0.35} className="gm-beacon" />
              <circle cx={px(ixd)} cy={py(iyd)} r={4.6} fill="var(--fg)" />
              <text x={px(ixd) + 9} y={py(iyd) - 8} fontSize="12" fontWeight={700} fill="var(--fg)">
                ({fmt(ix!)}, {fmt(iy!)})
              </text>
            </g>
          )}
        </svg>
      </div>

      {/* equations legend */}
      <div className="mt-2 flex justify-center gap-4 text-[13px]">
        <span className="serif tabular" style={{ color: GEO_ACCENT }}>{eqn(m1, b1)}</span>
        <span className="serif tabular" style={{ color: GEO_BLUE }}>{eqn(m2, b2)}</span>
      </div>

      {/* verdict */}
      <div
        className="mt-2 rounded-xl p-3 text-center"
        style={{
          transition: "background 0.35s ease, border-color 0.35s ease",
          ...(sameLine
            ? { background: "var(--accent-wash)", border: "1px solid var(--accent-line)" }
            : parallel
              ? { background: "rgba(200,60,60,0.08)", border: "1px solid rgb(200,60,60)" }
              : { background: "var(--bg-2)", border: "1px solid var(--line)" }),
        }}
      >
        {sameLine ? (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>Same line twice — <b style={{ color: "var(--accent)" }}>infinitely many solutions</b></div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>Every point on the line satisfies both equations.</div>
          </>
        ) : parallel ? (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>Parallel lines — <b style={{ color: "rgb(200,60,60)" }}>no solution</b></div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>Equal slopes, different intercepts: they never meet.</div>
          </>
        ) : (
          <>
            <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
              One solution: <b style={{ color: "var(--accent)" }}>({fmt(ix!)}, {fmt(iy!)})</b>{!onGrid && <span className="text-[12px]" style={{ color: "var(--fg-3)" }}> (off this grid)</span>}
            </div>
            <div className="mt-0.5 text-[12px] serif tabular" style={{ color: "var(--fg-2)" }}>
              check: {fmt(m1)}·{fmt(ix!)} {b1 >= 0 ? "+" : "−"} {fmt(Math.abs(b1))} = {fmt(iy!)} ✓ and {fmt(m2)}·{fmt(ix!)} {b2 >= 0 ? "+" : "−"} {fmt(Math.abs(b2))} = {fmt(iy!)} ✓
            </div>
          </>
        )}
      </div>

      {/* line-2 steppers */}
      {interactive && (
        <div className="mt-4 flex items-center justify-center gap-6">
          {stepper("slope m₂", m2, setM2, -3, 3, 1)}
          {stepper("intercept b₂", b2, setB2, min + 1, max - 1, 1)}
        </div>
      )}
      {interactive && (
        <div className="mt-2 text-center text-[12px]" style={{ color: "var(--fg-3)" }}>
          adjust the blue line — make the lines cross, parallel, or identical
        </div>
      )}
    </div>
  );
}
