"use client";

import { useState } from "react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { dist, midpoint, legs } from "@/lib/geo";
import { type CoordGeoConfig } from "@/lib/genmath-interactive";

// The coordinate-geometry workbench: one grid that shows distance (via the
// run/rise right triangle), midpoint, slope, a line y = mx + b, or a circle.
// Tap "Show …" to reveal the computed value, so the learner predicts first.
function gcd(a: number, b: number): number {
  a = Math.abs(a); b = Math.abs(b);
  while (b) { [a, b] = [b, a % b]; }
  return a || 1;
}
function fmt(n: number): string {
  return Number.isInteger(n) ? n.toString() : (Math.round(n * 100) / 100).toString();
}
// A signed slope as a reduced fraction (or integer) string.
function frac(num: number, den: number): string {
  if (den === 0) return "undefined";
  const sign = num * den < 0 ? "-" : "";
  let n = Math.abs(num), d = Math.abs(den);
  const g = gcd(n, d); n /= g; d /= g;
  return d === 1 ? `${sign}${n}` : `${sign}${n}/${d}`;
}

export default function CoordGeo({ config }: { config: CoordGeoConfig }) {
  const color = config.color ?? GEO_ACCENT;
  const [shown, setShown] = useState(false);
  const min = config.min ?? -6;
  const max = config.max ?? 6;
  const N = max - min;
  const cell = 26;
  const pad = 20;
  const size = N * cell;
  const W = size + pad * 2;
  const px = (gx: number) => pad + (gx - min) * cell;
  const py = (gy: number) => pad + (max - gy) * cell;
  const ints = Array.from({ length: N + 1 }, (_, i) => min + i);
  const step = N > 12 ? 2 : 1;

  const a = config.a ?? { x: 0, y: 0 };
  const b = config.b ?? { x: 3, y: 4 };

  const Dot = ({ p, label, c, below = false }: { p: { x: number; y: number }; label: string; c: string; below?: boolean }) => (
    <g>
      <circle cx={px(p.x)} cy={py(p.y)} r={3.4} fill={c} />
      <text x={px(p.x) + 6} y={py(p.y) + (below ? 15 : -7)} fontSize="12" fontStyle="italic" fontFamily="serif" fill={c}>{label}</text>
    </g>
  );

  // ---- figure per mode ----
  let figure: React.ReactNode = null;
  let readoutTitle = "";
  let readout: React.ReactNode = null;
  let buttonLabel = "";

  if (config.mode === "distance" || config.mode === "slope") {
    const { run, rise } = legs(a, b);
    const corner = { x: b.x, y: a.y };
    const d = dist(a, b);
    figure = (
      <>
        {/* legs of the right triangle */}
        {shown && (
          <>
            <line x1={px(a.x)} y1={py(a.y)} x2={px(corner.x)} y2={py(corner.y)} stroke={GEO_BLUE} strokeWidth={1.8} strokeDasharray="5 3" />
            <line x1={px(corner.x)} y1={py(corner.y)} x2={px(b.x)} y2={py(b.y)} stroke={GEO_BLUE} strokeWidth={1.8} strokeDasharray="5 3" />
            <text x={(px(a.x) + px(corner.x)) / 2} y={py(a.y) + (rise >= 0 ? 15 : -7)} fontSize="11" textAnchor="middle" fill={GEO_BLUE}>{config.mode === "slope" ? `run ${run}` : `${Math.abs(run)}`}</text>
            <text x={px(corner.x) + (run >= 0 ? 8 : -8)} y={(py(corner.y) + py(b.y)) / 2} fontSize="11" textAnchor={run >= 0 ? "start" : "end"} fill={GEO_BLUE}>{config.mode === "slope" ? `rise ${rise}` : `${Math.abs(rise)}`}</text>
          </>
        )}
        <line x1={px(a.x)} y1={py(a.y)} x2={px(b.x)} y2={py(b.y)} stroke={color} strokeWidth={2.4} />
        <Dot p={a} label={`A(${a.x}, ${a.y})`} c="var(--fg-1)" below={a.y < b.y} />
        <Dot p={b} label={`B(${b.x}, ${b.y})`} c="var(--fg-1)" below={b.y < a.y} />
      </>
    );
    if (config.mode === "distance") {
      readoutTitle = "Distance AB";
      readout = (
        <>
          <div className="serif tabular" style={{ color: "var(--fg-2)" }}>d = √(run² + rise²)</div>
          <div className="serif tabular mt-0.5">{`d = √(${Math.abs(run)}² + ${Math.abs(rise)}²) = √${run * run + rise * rise} = `}<b style={{ color }}>{fmt(d)}</b></div>
        </>
      );
      buttonLabel = "Show the distance";
    } else {
      readoutTitle = "Slope of AB";
      readout = (
        <>
          <div className="serif tabular">{`m = rise / run = ${rise} / ${run} = `}<b style={{ color }}>{frac(rise, run)}</b></div>
          <div className="mt-1 text-[12px]" style={{ color: "var(--fg-3)" }}>{run === 0 ? "run = 0 → the line is vertical, slope undefined" : rise === 0 ? "rise = 0 → horizontal line, slope 0" : rise * run > 0 ? "rise and run agree in sign → positive slope (uphill)" : "opposite signs → negative slope (downhill)"}</div>
        </>
      );
      buttonLabel = "Show the slope";
    }
  } else if (config.mode === "midpoint") {
    const M = midpoint(a, b);
    figure = (
      <>
        <line x1={px(a.x)} y1={py(a.y)} x2={px(b.x)} y2={py(b.y)} stroke={color} strokeWidth={2.4} />
        <Dot p={a} label={`A(${a.x}, ${a.y})`} c="var(--fg-1)" below={a.y < b.y} />
        <Dot p={b} label={`B(${b.x}, ${b.y})`} c="var(--fg-1)" below={b.y < a.y} />
        {shown && <>
          <circle cx={px(M.x)} cy={py(M.y)} r={5} fill="none" stroke={color} strokeWidth={2} />
          <circle cx={px(M.x)} cy={py(M.y)} r={3.2} fill={color} />
          <text x={px(M.x) + 8} y={py(M.y) - 6} fontSize="12" fontStyle="italic" fontFamily="serif" fill={color}>M</text>
        </>}
      </>
    );
    readoutTitle = "Midpoint of AB";
    readout = (
      <>
        <div className="serif tabular" style={{ color: "var(--fg-2)" }}>M = ( (x₁+x₂)/2, (y₁+y₂)/2 )</div>
        <div className="serif tabular mt-0.5">{`M = ((${a.x}+${b.x})/2, (${a.y}+${b.y})/2) = `}<b style={{ color }}>{`(${fmt(M.x)}, ${fmt(M.y)})`}</b></div>
      </>
    );
    buttonLabel = "Show the midpoint";
  } else if (config.mode === "line") {
    const m = config.m ?? 1;
    const bInt = config.yint ?? 0;
    const yAt = (x: number) => m * x + bInt;
    // clip the line to the visible box
    const x1 = min, x2 = max;
    figure = (
      <>
        <line x1={px(x1)} y1={py(yAt(x1))} x2={px(x2)} y2={py(yAt(x2))} stroke={color} strokeWidth={2.4} />
        {shown && <>
          {/* slope triangle from the intercept */}
          <line x1={px(0)} y1={py(bInt)} x2={px(1)} y2={py(bInt)} stroke={GEO_BLUE} strokeWidth={1.6} strokeDasharray="4 3" />
          <line x1={px(1)} y1={py(bInt)} x2={px(1)} y2={py(yAt(1))} stroke={GEO_BLUE} strokeWidth={1.6} strokeDasharray="4 3" />
          <text x={px(0.5)} y={py(bInt) + 13} fontSize="10" textAnchor="middle" fill={GEO_BLUE}>run 1</text>
          <text x={px(1) + 5} y={(py(bInt) + py(yAt(1))) / 2} fontSize="10" fill={GEO_BLUE}>rise {fmt(m)}</text>
        </>}
        <circle cx={px(0)} cy={py(bInt)} r={3.6} fill={color} />
        <text x={px(0) - 6} y={py(bInt) - 7} fontSize="11" textAnchor="end" fill={color}>(0, {fmt(bInt)})</text>
      </>
    );
    readoutTitle = "Equation of the line";
    readout = (
      <>
        <div className="serif tabular text-[15px]">{`y = ${fmt(m)}x ${bInt >= 0 ? "+ " + fmt(bInt) : "− " + fmt(-bInt)}`}</div>
        <div className="mt-1 text-[12px]" style={{ color: "var(--fg-3)" }}>slope <b style={{ color: GEO_BLUE }}>m = {fmt(m)}</b> (rise over run), y-intercept <b style={{ color }}>b = {fmt(bInt)}</b></div>
      </>
    );
    buttonLabel = "Show the equation";
  } else {
    // circle
    const c = config.center ?? { x: 0, y: 0 };
    const r = config.r ?? 3;
    figure = (
      <>
        <circle cx={px(c.x)} cy={py(c.y)} r={r * cell} fill={`${color}12`} stroke={color} strokeWidth={2.2} />
        <circle cx={px(c.x)} cy={py(c.y)} r={3.4} fill={GEO_BLUE} />
        <text x={px(c.x) + 6} y={py(c.y) - 7} fontSize="11" fill={GEO_BLUE}>({c.x}, {c.y})</text>
        {shown && <>
          <line x1={px(c.x)} y1={py(c.y)} x2={px(c.x + r)} y2={py(c.y)} stroke={color} strokeWidth={2} />
          <text x={px(c.x + r / 2)} y={py(c.y) - 6} fontSize="11" textAnchor="middle" fill={color}>r = {r}</text>
        </>}
      </>
    );
    readoutTitle = "Equation of the circle";
    const h = c.x, k = c.y;
    readout = (
      <>
        <div className="serif tabular text-[15px]">{`(x ${h >= 0 ? "− " + h : "+ " + -h})² + (y ${k >= 0 ? "− " + k : "+ " + -k})² = ${r * r}`}</div>
        <div className="mt-1 text-[12px]" style={{ color: "var(--fg-3)" }}>center <b style={{ color: GEO_BLUE }}>({h}, {k})</b>, radius <b style={{ color }}>{r}</b> (so r² = {r * r})</div>
      </>
    );
    buttonLabel = "Show the equation";
  }

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${W}`} width="100%" style={{ maxWidth: 340 }} role="img" aria-label="Coordinate geometry figure">
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
          {figure}
        </svg>
      </div>

      <div className="mt-2 rounded-xl p-3 text-center text-[14px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>{readoutTitle}</div>
        {shown ? <div className="mt-1">{readout}</div> : <div className="mt-1 text-[13px]" style={{ color: "var(--fg-3)" }}>Predict it, then reveal.</div>}
      </div>

      <div className="mt-4 flex justify-center">
        <button
          type="button"
          onClick={() => setShown((v) => !v)}
          className="gm-press rounded-full px-5 py-2 text-[14px] font-medium"
          style={{ background: shown ? "var(--bg-2)" : "var(--accent)", border: "1px solid var(--accent)", color: shown ? "var(--fg)" : "var(--accent-ink, #fff)" }}
        >
          {shown ? "Reset" : buttonLabel}
        </button>
      </div>
    </div>
  );
}
