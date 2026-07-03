"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { dilate } from "@/lib/geo";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type DilationConfig } from "@/lib/genmath-interactive";

// A triangle and its dilation image from a center O. Each image vertex lies on
// the ray from O through the matching original vertex, k times as far. k > 1
// enlarges, 0 < k < 1 reduces, k = 1 leaves it unchanged. Image sides are k
// times the originals and parallel to them.
const W = 330;
const H = 260;
const KS = [0.5, 1, 1.5, 2, 2.5];

export default function Dilation({ config }: { config: DilationConfig }) {
  const { color = GEO_ACCENT } = config;
  const [ki, setKi] = useState(() => {
    const i = KS.indexOf(config.start ?? 2);
    return i < 0 ? 3 : i;
  });
  const k = KS[ki];
  // the image triangle glides along the dilation rays between steps
  const kDraw = useAnimatedValue(k, { stiffness: 150, damping: 22 });

  const O = { x: 1, y: 1 };
  const pre = [{ x: 4, y: 2 }, { x: 6, y: 5 }, { x: 3, y: 5 }];
  const img = pre.map((p) => dilate(p, O, kDraw));

  const all = [O, ...pre, ...img];
  const minX = Math.min(...all.map((p) => p.x)) - 1, maxX = Math.max(...all.map((p) => p.x)) + 1;
  const minY = Math.min(...all.map((p) => p.y)) - 1, maxY = Math.max(...all.map((p) => p.y)) + 1;
  const scale = Math.min((W - 30) / (maxX - minX), (H - 40) / (maxY - minY));
  const ox = (W - (maxX - minX) * scale) / 2, oy = (H - (maxY - minY) * scale) / 2;
  const sx = (x: number) => ox + (x - minX) * scale;
  const sy = (y: number) => H - (oy + (y - minY) * scale);
  const poly = (ps: any[]) => ps.map((p) => `${sx(p.x)},${sy(p.y)}`).join(" ");
  const fmt = (n: number) => (Number.isInteger(n) ? n.toString() : n.toFixed(1));

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 350, display: "block", margin: "0 auto" }}>
        {/* rays from center through each vertex */}
        {pre.map((p, i) => (
          <line key={i} x1={sx(O.x)} y1={sy(O.y)} x2={sx(img[i].x)} y2={sy(img[i].y)} stroke="var(--fg-3)" strokeWidth={1} strokeDasharray="3 3" />
        ))}
        {/* image triangle */}
        {k !== 1 && <polygon points={poly(img)} fill={`${color}12`} stroke={color} strokeWidth={2} strokeLinejoin="round" />}
        {/* pre-image triangle */}
        <polygon points={poly(pre)} fill="rgba(120,120,120,0.10)" stroke="var(--fg-1)" strokeWidth={2} strokeLinejoin="round" />
        {/* center */}
        <circle cx={sx(O.x)} cy={sy(O.y)} r={4} fill={GEO_BLUE} />
        <text x={sx(O.x) - 6} y={sy(O.y) + 16} fontSize="12" fill={GEO_BLUE}>O</text>
      </svg>

      <div className="mt-2 rounded-xl p-3 text-center text-[14px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        <div className="serif tabular">scale factor <b style={{ color }}>k = {fmt(k)}</b> — {k > 1 ? "an enlargement" : k < 1 ? "a reduction" : "no change"}</div>
        <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>Each image vertex is {fmt(k)} × as far from <b style={{ color: GEO_BLUE }}>O</b>; image sides are {fmt(k)} × the originals and parallel to them.</div>
      </div>

      <div className="mt-4 flex items-center justify-center gap-3">
        <span className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>scale factor</span>
        <button type="button" onClick={() => setKi((v) => Math.max(0, v - 1))} disabled={ki <= 0} aria-label="Smaller" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 40, fontSize: 17, color: "var(--fg)" }}>{fmt(k)}</div>
        <button type="button" onClick={() => setKi((v) => Math.min(KS.length - 1, v + 1))} disabled={ki >= KS.length - 1} aria-label="Larger" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
    </div>
  );
}
