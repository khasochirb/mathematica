"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { regularPolygonArea } from "@/lib/geo";
import { type ApothemPolygonConfig } from "@/lib/genmath-interactive";

// A regular polygon split into n triangles from the centre. Each triangle has
// base = one side and height = the apothem, so the whole area is
// ½ · apothem · perimeter. The side count is adjustable.
const W = 320;
const H = 300;

export default function ApothemPolygon({ config }: { config: ApothemPolygonConfig }) {
  const { side = 6, color = GEO_ACCENT } = config;
  const [n, setN] = useState(config.start ?? 6);

  const cx = W / 2, cy = H / 2 - 6;
  const apothemUnits = side / (2 * Math.tan(Math.PI / n));
  const R = side / (2 * Math.sin(Math.PI / n)); // circumradius in units
  const scale = 92 / R; // fit R to ~92 px
  const Rpx = R * scale;
  const aPx = apothemUnits * scale;

  // vertices, flat side at bottom
  const verts = Array.from({ length: n }, (_, i) => {
    const ang = -90 + (360 / n) * i + 180 / n; // rotate so a flat side sits at the bottom
    const rad = (ang * Math.PI) / 180;
    return { x: cx + Rpx * Math.cos(rad), y: cy + Rpx * Math.sin(rad) };
  });
  const poly = verts.map((p) => `${p.x},${p.y}`).join(" ");
  // bottom side midpoint (apothem foot): the side whose midpoint is lowest
  let mid = { x: cx, y: cy + aPx };
  let best = -Infinity;
  for (let i = 0; i < n; i++) {
    const a = verts[i], b = verts[(i + 1) % n];
    const m = { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 };
    if (m.y > best) { best = m.y; mid = m; }
  }

  const perimeter = n * side;
  const area = regularPolygonArea(apothemUnits, perimeter);
  const fmt = (x: number) => (Number.isInteger(x) ? x.toString() : x.toFixed(1));

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        {/* triangulation fan */}
        {verts.map((p, i) => (
          <line key={i} x1={cx} y1={cy} x2={p.x} y2={p.y} stroke={color} strokeWidth={1} strokeDasharray="3 3" opacity={0.7} />
        ))}
        <polygon points={poly} fill={`${color}12`} stroke="var(--fg-1)" strokeWidth={2} strokeLinejoin="round" />
        {/* apothem */}
        <line x1={cx} y1={cy} x2={mid.x} y2={mid.y} stroke={GEO_BLUE} strokeWidth={2} />
        <text x={cx + 6} y={(cy + mid.y) / 2 + 4} fontSize="11" fill={GEO_BLUE} fontWeight={700}>a</text>
        {/* right-angle mark at foot */}
        <rect x={mid.x - 5} y={mid.y - 9} width={8} height={8} fill="none" stroke={GEO_BLUE} strokeWidth={1} />
        <circle cx={cx} cy={cy} r={2.5} fill="var(--fg)" />
      </svg>

      <div className="mt-2 rounded-xl p-3 text-center text-[14px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        <div className="serif tabular">Area = ½ · a · P = ½ · <span style={{ color: GEO_BLUE }}>{fmt(apothemUnits)}</span> · <span>{perimeter}</span> = <b style={{ color }}>{fmt(area)}</b></div>
        <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>{n} triangles, each base = side {side}, height = apothem {fmt(apothemUnits)}. Perimeter P = {n} × {side} = {perimeter}.</div>
      </div>

      <div className="mt-4 flex items-center justify-center gap-3">
        <span className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>sides</span>
        <button type="button" onClick={() => setN((v) => Math.max(3, v - 1))} disabled={n <= 3} aria-label="Fewer" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 28, fontSize: 17, color: "var(--fg)" }}>{n}</div>
        <button type="button" onClick={() => setN((v) => Math.min(10, v + 1))} disabled={n >= 10} aria-label="More" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
    </div>
  );
}
