"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { rectPrismVolume, rectPrismSurface, cylinderVolume, cylinderSurface, pyramidVolume, coneVolume, coneSurface, sphereVolume, sphereSurface, prismVolume } from "@/lib/geo";
import { type Solid3DConfig } from "@/lib/genmath-interactive";

// A 3-D solid drawn in oblique projection, with adjustable dimensions and live
// volume + surface-area readouts. Round solids show answers as exact multiples
// of π; the drawing is schematic but the numbers come from lib/geo.
const W = 320;
const H = 250;
const D = 0.42; // oblique depth factor

export default function Solid3D({ config }: { config: Solid3DConfig }) {
  const { solid, color = GEO_ACCENT } = config;
  const [l, setL] = useState(config.l ?? 4);
  const [w, setW] = useState(config.w ?? 3);
  const [h, setH] = useState(config.h ?? 5);
  const [r, setR] = useState(config.r ?? 3);
  const [baseS, setBaseS] = useState(config.base ?? 6);
  const slant = config.slant ?? 5;

  const s = 22; // px per unit
  const cx = W / 2, cy = H / 2 + 20;
  // project (x up-model? ) — x right, y up, z depth (up-right)
  const P = (x: number, y: number, z: number) => ({ x: cx + (x + z * D) * s, y: cy - (y + z * D) * s });

  const fmtPi = (coef: number) => (coef === 1 ? "π" : `${coef}π`);
  const round2 = (n: number) => (Number.isInteger(n) ? n.toString() : n.toFixed(1));

  // per-solid drawing + formulas
  let draw: React.ReactNode = null;
  let volLine = "", saLine = "";

  if (solid === "rectPrism" || solid === "triangularPrism") {
    // rectangular box l(x) × w(z) × h(y), centred
    const x0 = -l / 2, y0 = -h / 2, z0 = -w / 2;
    const v = (dx: number, dy: number, dz: number) => P(x0 + dx, y0 + dy, z0 + dz);
    if (solid === "rectPrism") {
      const A = v(0, 0, 0), B = v(l, 0, 0), C = v(l, h, 0), Dp = v(0, h, 0);
      const A2 = v(0, 0, w), B2 = v(l, 0, w), C2 = v(l, h, w), D2 = v(0, h, w);
      draw = (
        <g>
          <polygon points={`${A2.x},${A2.y} ${B2.x},${B2.y} ${C2.x},${C2.y} ${D2.x},${D2.y}`} fill={`${color}10`} stroke="var(--fg-3)" strokeWidth={1.2} strokeDasharray="4 3" />
          <line x1={A.x} y1={A.y} x2={A2.x} y2={A2.y} stroke="var(--fg-3)" strokeWidth={1.2} strokeDasharray="4 3" />
          <polygon points={`${Dp.x},${Dp.y} ${C.x},${C.y} ${C2.x},${C2.y} ${D2.x},${D2.y}`} fill={`${color}18`} stroke="var(--fg-1)" strokeWidth={1.6} />
          <polygon points={`${B.x},${B.y} ${C.x},${C.y} ${C2.x},${C2.y} ${B2.x},${B2.y}`} fill={`${color}14`} stroke="var(--fg-1)" strokeWidth={1.6} />
          <polygon points={`${A.x},${A.y} ${B.x},${B.y} ${C.x},${C.y} ${Dp.x},${Dp.y}`} fill={`${color}20`} stroke="var(--fg-1)" strokeWidth={2} />
          <text x={(A.x + B.x) / 2} y={A.y + 16} fontSize="12" textAnchor="middle" fill="var(--fg-2)">{l}</text>
          <text x={A.x - 12} y={(A.y + Dp.y) / 2} fontSize="12" textAnchor="end" fill={GEO_BLUE}>{h}</text>
          <text x={(B.x + B2.x) / 2 + 8} y={(B.y + B2.y) / 2 + 4} fontSize="12" fill="var(--fg-2)">{w}</text>
        </g>
      );
      volLine = `V = l·w·h = ${l}·${w}·${h} = ${rectPrismVolume(l, w, h)}`;
      saLine = `SA = 2(lw+lh+wh) = ${rectPrismSurface(l, w, h)}`;
    } else {
      // triangular prism: triangle (base l, height h) front, depth w
      const A = v(0, 0, 0), B = v(l, 0, 0), Ap = v(l / 2, h, 0);
      const A2 = v(0, 0, w), B2 = v(l, 0, w), Ap2 = v(l / 2, h, w);
      draw = (
        <g>
          <polygon points={`${A2.x},${A2.y} ${B2.x},${B2.y} ${Ap2.x},${Ap2.y}`} fill={`${color}10`} stroke="var(--fg-3)" strokeWidth={1.2} strokeDasharray="4 3" />
          {[[A, A2], [B, B2], [Ap, Ap2]].map(([p, q]: any, i) => <line key={i} x1={p.x} y1={p.y} x2={q.x} y2={q.y} stroke="var(--fg-1)" strokeWidth={1.4} />)}
          <polygon points={`${A.x},${A.y} ${B.x},${B.y} ${Ap.x},${Ap.y}`} fill={`${color}20`} stroke="var(--fg-1)" strokeWidth={2} />
          <text x={(A.x + B.x) / 2} y={A.y + 16} fontSize="12" textAnchor="middle" fill="var(--fg-2)">b={l}</text>
          <text x={Ap.x - 14} y={(Ap.y + A.y) / 2} fontSize="12" fill={GEO_BLUE}>h={h}</text>
          <text x={(B.x + B2.x) / 2 + 8} y={(B.y + B2.y) / 2 + 4} fontSize="12" fill="var(--fg-2)">{w}</text>
        </g>
      );
      const baseArea = (l * h) / 2;
      volLine = `V = (base area)·length = ${baseArea}·${w} = ${prismVolume(baseArea, w)}`;
      saLine = `SA = 2·base + lateral`;
    }
  } else if (solid === "cylinder") {
    const ry = r * s * D * 0.9, rx = r * s;
    const topY = cy - h * s / 2, botY = cy + h * s / 2;
    draw = (
      <g>
        <line x1={cx - rx} y1={topY} x2={cx - rx} y2={botY} stroke="var(--fg-1)" strokeWidth={1.6} />
        <line x1={cx + rx} y1={topY} x2={cx + rx} y2={botY} stroke="var(--fg-1)" strokeWidth={1.6} />
        <path d={`M ${cx - rx} ${botY} A ${rx} ${ry} 0 0 0 ${cx + rx} ${botY}`} fill="none" stroke="var(--fg-3)" strokeWidth={1.2} strokeDasharray="4 3" />
        <path d={`M ${cx - rx} ${botY} A ${rx} ${ry} 0 0 1 ${cx + rx} ${botY}`} fill={`${color}14`} stroke="var(--fg-1)" strokeWidth={1.6} />
        <ellipse cx={cx} cy={topY} rx={rx} ry={ry} fill={`${color}20`} stroke="var(--fg-1)" strokeWidth={1.8} />
        <line x1={cx} y1={topY} x2={cx + rx} y2={topY} stroke={color} strokeWidth={1.4} /><text x={cx + rx / 2} y={topY - 4} fontSize="11" textAnchor="middle" fill={color}>r={r}</text>
        <line x1={cx + rx + 6} y1={topY} x2={cx + rx + 6} y2={botY} stroke={GEO_BLUE} strokeWidth={1.2} /><text x={cx + rx + 10} y={cy} fontSize="12" fill={GEO_BLUE}>h={h}</text>
      </g>
    );
    volLine = `V = πr²h = ${fmtPi(r * r * h)} ≈ ${round2(cylinderVolume(r, h))}`;
    saLine = `SA = 2πr² + 2πrh = ${fmtPi(2 * r * r + 2 * r * h)} ≈ ${round2(cylinderSurface(r, h))}`;
  } else if (solid === "cone") {
    const ry = r * s * D * 0.9, rx = r * s;
    const botY = cy + h * s / 2, apex = { x: cx, y: cy - h * s / 2 };
    draw = (
      <g>
        <path d={`M ${cx - rx} ${botY} A ${rx} ${ry} 0 0 0 ${cx + rx} ${botY}`} fill="none" stroke="var(--fg-3)" strokeWidth={1.2} strokeDasharray="4 3" />
        <path d={`M ${cx - rx} ${botY} A ${rx} ${ry} 0 0 1 ${cx + rx} ${botY}`} fill={`${color}14`} stroke="var(--fg-1)" strokeWidth={1.6} />
        <line x1={cx - rx} y1={botY} x2={apex.x} y2={apex.y} stroke="var(--fg-1)" strokeWidth={1.8} />
        <line x1={cx + rx} y1={botY} x2={apex.x} y2={apex.y} stroke="var(--fg-1)" strokeWidth={1.8} />
        <line x1={cx} y1={botY} x2={cx + rx} y2={botY} stroke={color} strokeWidth={1.4} /><text x={cx + rx / 2} y={botY + 14} fontSize="11" textAnchor="middle" fill={color}>r={r}</text>
        <line x1={cx} y1={botY} x2={apex.x} y2={apex.y} stroke={GEO_BLUE} strokeWidth={1.2} strokeDasharray="3 2" /><text x={cx + 6} y={cy} fontSize="12" fill={GEO_BLUE}>h={h}</text>
      </g>
    );
    volLine = `V = ⅓πr²h = ${fmtPi(Math.round((r * r * h / 3) * 100) / 100)} ≈ ${round2(coneVolume(r, h))}`;
    saLine = `SA = πr² + πr·ℓ = ${fmtPi(r * r + r * slant)} (ℓ=${slant})`;
  } else if (solid === "pyramid") {
    const b = baseS, ry = b * s * D * 0.5, rx = b * s / 2;
    const botY = cy + h * s / 2, apex = { x: cx, y: cy - h * s / 2 };
    // square base drawn as a rhombus in oblique
    const f = { x: cx, y: botY + ry }, rgt = { x: cx + rx, y: botY }, bk = { x: cx, y: botY - ry }, lft = { x: cx - rx, y: botY };
    draw = (
      <g>
        <polygon points={`${f.x},${f.y} ${rgt.x},${rgt.y} ${bk.x},${bk.y} ${lft.x},${lft.y}`} fill={`${color}14`} stroke="var(--fg-1)" strokeWidth={1.6} />
        {[f, rgt, lft].map((p, i) => <line key={i} x1={p.x} y1={p.y} x2={apex.x} y2={apex.y} stroke="var(--fg-1)" strokeWidth={1.8} />)}
        <line x1={bk.x} y1={bk.y} x2={apex.x} y2={apex.y} stroke="var(--fg-3)" strokeWidth={1.2} strokeDasharray="4 3" />
        <text x={(f.x + rgt.x) / 2 + 6} y={(f.y + rgt.y) / 2 + 10} fontSize="12" fill="var(--fg-2)">{b}</text>
        <line x1={cx} y1={botY} x2={apex.x} y2={apex.y} stroke={GEO_BLUE} strokeWidth={1.2} strokeDasharray="3 2" /><text x={cx + 6} y={cy} fontSize="12" fill={GEO_BLUE}>h={h}</text>
      </g>
    );
    const baseArea = b * b;
    volLine = `V = ⅓·(base area)·h = ⅓·${baseArea}·${h} = ${round2(pyramidVolume(baseArea, h))}`;
    saLine = `SA = base + 4 triangular faces`;
  } else {
    // sphere
    const rx = r * s;
    draw = (
      <g>
        <circle cx={cx} cy={cy} r={rx} fill={`${color}16`} stroke="var(--fg-1)" strokeWidth={2} />
        <ellipse cx={cx} cy={cy} rx={rx} ry={rx * 0.35} fill="none" stroke="var(--fg-3)" strokeWidth={1.2} strokeDasharray="4 3" />
        <line x1={cx} y1={cy} x2={cx + rx} y2={cy} stroke={color} strokeWidth={1.6} /><text x={cx + rx / 2} y={cy - 5} fontSize="12" textAnchor="middle" fill={color}>r={r}</text>
        <circle cx={cx} cy={cy} r={2.5} fill="var(--fg)" />
      </g>
    );
    volLine = `V = ⁴⁄₃πr³ = ${fmtPi(Math.round((4 / 3 * r * r * r) * 100) / 100)} ≈ ${round2(sphereVolume(r))}`;
    saLine = `SA = 4πr² = ${fmtPi(4 * r * r)} ≈ ${round2(sphereSurface(r))}`;
  }

  const stepper = (val: number, set: (n: number) => void, min: number, max: number, label: string, col: string) => (
    <div className="text-center">
      <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>{label}</div>
      <div className="mt-1 flex items-center gap-1.5">
        <button type="button" onClick={() => set(Math.max(min, val - 1))} disabled={val <= min} aria-label={`Decrease ${label}`} className="gm-press grid h-8 w-8 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-3.5 w-3.5" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 20, fontSize: 15, color: col }}>{val}</div>
        <button type="button" onClick={() => set(Math.min(max, val + 1))} disabled={val >= max} aria-label={`Increase ${label}`} className="gm-press grid h-8 w-8 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-3.5 w-3.5" /></button>
      </div>
    </div>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>{draw}</svg>

      <div className="mt-2 rounded-xl p-3 text-center text-[13px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        <div className="serif tabular" style={{ color }}>{volLine}</div>
        <div className="serif tabular mt-1" style={{ color: GEO_BLUE }}>{saLine}</div>
      </div>

      <div className="mt-4 flex items-center justify-center gap-4">
        {(solid === "rectPrism" || solid === "triangularPrism") && <>{stepper(l, setL, 2, 8, solid === "rectPrism" ? "l" : "base", color)}{stepper(w, setW, 2, 8, solid === "rectPrism" ? "w" : "length", "var(--fg-1)")}{stepper(h, setH, 2, 8, "h", GEO_BLUE)}</>}
        {(solid === "cylinder" || solid === "cone") && <>{stepper(r, setR, 1, 6, "r", color)}{stepper(h, setH, 2, 8, "h", GEO_BLUE)}</>}
        {solid === "pyramid" && <>{stepper(baseS, setBaseS, 2, 8, "base", color)}{stepper(h, setH, 2, 9, "h", GEO_BLUE)}</>}
        {solid === "sphere" && stepper(r, setR, 1, 6, "r", color)}
      </div>
    </div>
  );
}
