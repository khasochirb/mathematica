"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { arcPath, GEO_ACCENT } from "@/components/genmath/interactive/GeoDiagram";
import { fortyFiveTriangle, thirtySixtyTriangle } from "@/lib/geo";
import { type SpecialTriangleConfig } from "@/lib/genmath-interactive";

// A 45-45-90 or 30-60-90 triangle with its fixed side ratios labelled (in terms
// of x) and a size stepper. The ratios never change — only the scale — which is
// exactly why these triangles are worth memorising.
const W = 320;
const H = 240;

export default function SpecialTriangle({ config }: { config: SpecialTriangleConfig }) {
  const { type, color = GEO_ACCENT } = config;
  const [x, setX] = useState(config.start ?? 3);
  const is45 = type === "45-45-90";

  // unit-shape vertices (right angle at C); B along +x, A along +y
  const C = { x: 0, y: 0 };
  const B = { x: is45 ? 1 : Math.sqrt(3), y: 0 };
  const A = { x: 0, y: 1 };

  const pts = [C, B, A];
  const minX = Math.min(...pts.map((p) => p.x)) - 0.5;
  const maxX = Math.max(...pts.map((p) => p.x)) + 0.5;
  const minY = Math.min(...pts.map((p) => p.y)) - 0.5;
  const maxY = Math.max(...pts.map((p) => p.y)) + 0.5;
  const scale = Math.min((W - 70) / (maxX - minX), (H - 50) / (maxY - minY));
  const ox = (W - (maxX - minX) * scale) / 2, oy = (H - (maxY - minY) * scale) / 2;
  const sx = (v: number) => ox + (v - minX) * scale;
  const sy = (v: number) => H - (oy + (v - minY) * scale);
  const degOf = (from: any, to: any) => (Math.atan2(sy(to.y) - sy(from.y), sx(to.x) - sx(from.x)) * 180) / Math.PI;

  const fmt = (n: number) => (Number.isInteger(n) ? n.toString() : n.toFixed(2));
  const t45 = fortyFiveTriangle(x);
  const t30 = thirtySixtyTriangle(x);

  const Angle = ({ v, from, to, label }: any) => (
    <g>
      <path d={arcPath(sx(v.x), sy(v.y), 16, degOf(v, from), degOf(v, to))} fill="none" stroke={color} strokeWidth={1.5} />
      <text x={sx(v.x) + (v.x < 0.4 ? 22 : v === B ? -24 : 0)} y={sy(v.y) + (v.y > 0.4 ? 22 : -8)} fontSize="11" textAnchor="middle" fill={color} fontWeight={700}>{label}</text>
    </g>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        <path d={`M ${sx(C.x)} ${sy(C.y)} L ${sx(B.x)} ${sy(B.y)} L ${sx(A.x)} ${sy(A.y)} Z`} fill={`${color}12`} stroke="var(--fg-1)" strokeWidth={2} strokeLinejoin="round" />
        {/* right-angle square at C */}
        <path d={`M ${sx(0.28)} ${sy(0)} L ${sx(0.28)} ${sy(0.28)} L ${sx(0)} ${sy(0.28)}`} fill="none" stroke="var(--fg-2)" strokeWidth={1.2} />
        {/* angles */}
        {is45 ? (
          <>
            <Angle v={B} from={C} to={A} deg={45} label="45°" />
            <Angle v={A} from={C} to={B} deg={45} label="45°" />
          </>
        ) : (
          <>
            <Angle v={B} from={C} to={A} deg={30} label="30°" />
            <Angle v={A} from={C} to={B} deg={60} label="60°" />
          </>
        )}
        {/* side labels: symbolic */}
        <text x={sx((C.x + B.x) / 2)} y={sy(0) + 16} fontSize="12" textAnchor="middle" fill="var(--fg-1)">{is45 ? "x" : "x√3"}</text>
        <text x={sx(0) - 12} y={sy((C.y + A.y) / 2) + 4} fontSize="12" textAnchor="middle" fill="var(--fg-1)">{is45 ? "x" : "x"}</text>
        <text x={sx((B.x + A.x) / 2) + 14} y={sy((B.y + A.y) / 2) - 4} fontSize="12" textAnchor="middle" fill={color} fontWeight={700}>{is45 ? "x√2" : "2x"}</text>
      </svg>

      <div className="mt-2 rounded-xl p-3 text-center text-[14px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        {is45 ? (
          <>
            <div className="serif tabular">legs <b>{x}</b>, {x} · hypotenuse <b style={{ color }}>{x}√2 ≈ {fmt(t45.hyp)}</b></div>
            <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>Both legs equal; the hypotenuse is a leg times √2.</div>
          </>
        ) : (
          <>
            <div className="serif tabular">short <b>{x}</b> · long <b>{x}√3 ≈ {fmt(t30.long)}</b> · hyp <b style={{ color }}>{2 * x}</b></div>
            <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>Sides are in the ratio x : x√3 : 2x; the hypotenuse is twice the short leg.</div>
          </>
        )}
      </div>

      <div className="mt-4 flex items-center justify-center gap-3">
        <span className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>size x</span>
        <button type="button" onClick={() => setX((v) => Math.max(1, v - 1))} disabled={x <= 1} aria-label="Smaller" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 28, fontSize: 17, color: "var(--fg)" }}>{x}</div>
        <button type="button" onClick={() => setX((v) => Math.min(6, v + 1))} disabled={x >= 6} aria-label="Larger" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
    </div>
  );
}
