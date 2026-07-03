"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { arcPath, GEO_ACCENT, GEO_BLUE, ArrowHead } from "@/components/genmath/interactive/GeoDiagram";
import { polygonInteriorSum, regularInteriorAngle, regularExteriorAngle, diagonalsFromVertex } from "@/lib/geo";
import { type PolygonAnglesConfig } from "@/lib/genmath-interactive";

// A regular n-gon whose side count the student changes. In "interior" mode we
// fan-triangulate from one vertex — the n − 2 triangles make the sum
// (n − 2)·180° literal. In "exterior" mode the turn arrows at each vertex add
// to a full 360°. Every number comes from lib/geo (unit-tested).
const W = 320;
const H = 300;

export default function PolygonAngles({ config }: { config: PolygonAnglesConfig }) {
  const { start = 5, minSides = 3, maxSides = 10, color = GEO_ACCENT } = config;
  const [n, setN] = useState(start);
  const [mode, setMode] = useState<"interior" | "exterior">(config.mode ?? "interior");

  // regular n-gon on a circle, first vertex at the top, going clockwise
  const cx = W / 2;
  const cy = H / 2 - 6;
  const r = 96;
  const pts = Array.from({ length: n }, (_, i) => {
    const a = -90 + (360 / n) * i;
    const rad = (a * Math.PI) / 180;
    return { x: cx + r * Math.cos(rad), y: cy + r * Math.sin(rad) };
  });
  const poly = pts.map((p) => `${p.x},${p.y}`).join(" ");

  const interiorSum = polygonInteriorSum(n);
  const eachInterior = regularInteriorAngle(n);
  const eachExterior = regularExteriorAngle(n);

  // triangulation diagonals from vertex 0 to every non-adjacent vertex
  const diags = [];
  for (let i = 2; i <= n - 2; i++) diags.push(i);

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        {/* triangulation fan (interior mode) */}
        {mode === "interior" &&
          diags.map((i) => (
            <line key={i} x1={pts[0].x} y1={pts[0].y} x2={pts[i].x} y2={pts[i].y} stroke={color} strokeWidth={1.4} strokeDasharray="4 4" />
          ))}
        {/* the polygon */}
        <polygon points={poly} fill={mode === "interior" ? `${color}12` : "rgba(120,120,120,0.06)"} stroke="var(--fg-1)" strokeWidth={2} strokeLinejoin="round" />
        {/* exterior-angle turn arrows: extend each side and arc to the next */}
        {mode === "exterior" &&
          pts.map((p, i) => {
            const prev = pts[(i - 1 + n) % n];
            const next = pts[(i + 1) % n];
            // direction of incoming side, extended past the vertex
            const inDir = Math.atan2(p.y - prev.y, p.x - prev.x);
            const ext = { x: p.x + Math.cos(inDir) * 26, y: p.y + Math.sin(inDir) * 26 };
            const a1 = (Math.atan2(ext.y - p.y, ext.x - p.x) * 180) / Math.PI;
            const a2 = (Math.atan2(next.y - p.y, next.x - p.x) * 180) / Math.PI;
            return (
              <g key={i}>
                <line x1={p.x} y1={p.y} x2={ext.x} y2={ext.y} stroke="var(--fg-3)" strokeWidth={1.3} strokeDasharray="3 3" />
                <path d={arcPath(p.x, p.y, 15, a1, a2)} fill="none" stroke={GEO_BLUE} strokeWidth={1.8} />
              </g>
            );
          })}
        {/* vertex dots */}
        {pts.map((p, i) => (
          <circle key={i} cx={p.x} cy={p.y} r={3} fill="var(--fg)" />
        ))}
      </svg>

      {/* readout */}
      <div className="mt-2 rounded-xl p-3 text-center text-[15px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        {mode === "interior" ? (
          <>
            <div className="serif tabular">
              ({n} − 2) × 180° = <b style={{ color }}>{interiorSum}°</b>
            </div>
            <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>
              {diagonalsFromVertex(n)} diagonal{diagonalsFromVertex(n) === 1 ? "" : "s"} from one corner → {n - 2} triangle{n - 2 === 1 ? "" : "s"}. Each angle of a regular {n}-gon = {eachInterior}°.
            </div>
          </>
        ) : (
          <>
            <div className="serif tabular">
              {n} × {eachExterior}° = <b style={{ color: GEO_BLUE }}>360°</b>
            </div>
            <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>
              The exterior angles of any convex polygon always total 360°.
            </div>
          </>
        )}
      </div>

      {/* controls */}
      <div className="mt-4 flex items-center justify-between gap-3">
        <div className="flex items-center gap-2">
          <button type="button" onClick={() => setN((v) => Math.max(minSides, v - 1))} disabled={n <= minSides} aria-label="Fewer sides" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
          <div className="serif tabular text-center" style={{ minWidth: 64, fontSize: 15, color: "var(--fg)" }}>{n} sides</div>
          <button type="button" onClick={() => setN((v) => Math.min(maxSides, v + 1))} disabled={n >= maxSides} aria-label="More sides" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
        </div>
        <div className="flex rounded-full p-0.5" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
          {(["interior", "exterior"] as const).map((m) => (
            <button key={m} type="button" onClick={() => setMode(m)} className="gm-press rounded-full px-3 py-1.5 text-[12px] font-semibold capitalize" style={{ background: mode === m ? "var(--accent)" : "transparent", color: mode === m ? "var(--accent-ink, #fff)" : "var(--fg-2)" }}>{m}</button>
          ))}
        </div>
      </div>
    </div>
  );
}
