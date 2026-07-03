"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { arcPath, GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { rightTriangleRatios } from "@/lib/geo";
import { type TrigRatiosConfig } from "@/lib/genmath-interactive";

// A right triangle with an adjustable acute angle θ. The three sides are named
// relative to θ — opposite, adjacent, hypotenuse — and the three ratios sin,
// cos, tan (SOH-CAH-TOA) update live. Sides come from a fixed hypotenuse so the
// picture stays a sensible size at every angle.
const W = 330;
const H = 250;
const HYP = 6;

export default function TrigRatios({ config }: { config: TrigRatiosConfig }) {
  const { color = GEO_ACCENT } = config;
  const [theta, setTheta] = useState(config.start ?? 40);
  const rad = (theta * Math.PI) / 180;
  const opp = HYP * Math.sin(rad);
  const adj = HYP * Math.cos(rad);

  // right angle at C=(0,0); B=(adj,0) holds θ; A=(0,opp)
  const C = { x: 0, y: 0 }, B = { x: adj, y: 0 }, A = { x: 0, y: opp };
  const pts = [C, B, A];
  const minX = Math.min(...pts.map((p) => p.x)) - 0.6;
  const maxX = Math.max(...pts.map((p) => p.x)) + 1.4;
  const minY = Math.min(...pts.map((p) => p.y)) - 0.6;
  const maxY = Math.max(...pts.map((p) => p.y)) + 0.8;
  const scale = Math.min((W - 20) / (maxX - minX), (H - 20) / (maxY - minY));
  const ox = (W - (maxX - minX) * scale) / 2, oy = (H - (maxY - minY) * scale) / 2;
  const sx = (v: number) => ox + (v - minX) * scale;
  const sy = (v: number) => H - (oy + (v - minY) * scale);
  const degOf = (from: any, to: any) => (Math.atan2(sy(to.y) - sy(from.y), sx(to.x) - sx(from.x)) * 180) / Math.PI;
  const r = rightTriangleRatios(opp, adj, HYP);
  const fmt = (n: number) => n.toFixed(2);

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 350, display: "block", margin: "0 auto" }}>
        <path d={`M ${sx(C.x)} ${sy(C.y)} L ${sx(B.x)} ${sy(B.y)} L ${sx(A.x)} ${sy(A.y)} Z`} fill={`${color}12`} stroke="var(--fg-1)" strokeWidth={2} strokeLinejoin="round" />
        {/* right angle at C */}
        <path d={`M ${sx(0.4)} ${sy(0)} L ${sx(0.4)} ${sy(0.4)} L ${sx(0)} ${sy(0.4)}`} fill="none" stroke="var(--fg-2)" strokeWidth={1.2} />
        {/* θ arc at B */}
        <path d={arcPath(sx(B.x), sy(B.y), 20, degOf(B, A), degOf(B, C))} fill="none" stroke={GEO_BLUE} strokeWidth={2} />
        <text x={sx(B.x) - 30} y={sy(B.y) - 8} fontSize="12" fill={GEO_BLUE} fontWeight={700}>θ = {theta}°</text>
        {/* side labels */}
        <text x={sx(adj / 2)} y={sy(0) + 15} fontSize="11" textAnchor="middle" fill="var(--fg-2)">adjacent ({fmt(adj)})</text>
        <text x={sx(0) + 6} y={sy(opp / 2)} fontSize="11" textAnchor="start" fill="var(--fg-2)">opp ({fmt(opp)})</text>
        <text x={sx((adj) / 2) + 20} y={sy(opp / 2) - 6} fontSize="11" textAnchor="middle" fill={color} fontWeight={700} transform={`rotate(${degOf(B, A)}, ${sx(adj / 2) + 20}, ${sy(opp / 2) - 6})`}>hyp ({HYP})</text>
      </svg>

      <div className="mt-2 grid grid-cols-3 gap-2 text-center text-[13px]">
        {[["sin θ", "opp/hyp", r.sin], ["cos θ", "adj/hyp", r.cos], ["tan θ", "opp/adj", r.tan]].map(([name, form, val]: any) => (
          <div key={name} className="rounded-xl p-2" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
            <div className="serif" style={{ color, fontWeight: 700 }}>{name}</div>
            <div className="text-[10px]" style={{ color: "var(--fg-3)" }}>{form}</div>
            <div className="serif tabular" style={{ color: "var(--fg)", fontSize: 15 }}>{fmt(val)}</div>
          </div>
        ))}
      </div>

      <div className="mt-4 flex items-center justify-center gap-3">
        <span className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>angle θ</span>
        <button type="button" onClick={() => setTheta((v) => Math.max(15, v - 5))} disabled={theta <= 15} aria-label="Smaller angle" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 40, fontSize: 17, color: "var(--fg)" }}>{theta}°</div>
        <button type="button" onClick={() => setTheta((v) => Math.min(75, v + 5))} disabled={theta >= 75} aria-label="Larger angle" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
    </div>
  );
}
