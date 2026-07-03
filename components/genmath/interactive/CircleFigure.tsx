"use client";

import { arcPath, GEO_ACCENT, GEO_BLUE, Ticks } from "@/components/genmath/interactive/GeoDiagram";
import { pointOnCircle } from "@/lib/geo";
import { type CircleFigureConfig } from "@/lib/genmath-interactive";

// The static circle renderer. Places labelled points on a circle by angle, then
// draws chords / radii / diameters / secants / tangents, angle marks, and a
// highlighted arc with its measure. Coordinates are exact (from pointOnCircle),
// so every mark is geometrically honest.
const W = 320;
const H = 280;

export default function CircleFigure({ config }: { config: CircleFigureConfig }) {
  const { radius = 5, points = [], objects = [], angles = [], arcs = [], external, showCenter = true, caption } = config;
  const O = { x: 0, y: 0 };
  const pos = new Map<string, { x: number; y: number }>();
  pos.set("O", O);
  points.forEach((p) => pos.set(p.id, pointOnCircle(0, 0, radius, p.deg)));
  const ext = external ? pointOnCircle(0, 0, external.dist, external.deg) : null;
  if (ext && external) pos.set(external.id, ext);
  const get = (id: string) => pos.get(id) ?? O;

  // fit
  const extra = ext ? [ext] : [];
  const box = radius + 1.2;
  const minX = Math.min(-box, ...extra.map((p) => p.x - 0.8));
  const maxX = Math.max(box, ...extra.map((p) => p.x + 0.8));
  const minY = Math.min(-box, ...extra.map((p) => p.y - 0.8));
  const maxY = Math.max(box, ...extra.map((p) => p.y + 0.8));
  const scale = Math.min((W - 20) / (maxX - minX), (H - 20) / (maxY - minY));
  const ox = (W - (maxX - minX) * scale) / 2, oy = (H - (maxY - minY) * scale) / 2;
  const sx = (x: number) => ox + (x - minX) * scale;
  const sy = (y: number) => H - (oy + (y - minY) * scale);
  const degScreen = (from: any, to: any) => (Math.atan2(sy(to.y) - sy(from.y), sx(to.x) - sx(from.x)) * 180) / Math.PI;
  const R = radius * scale;

  const extendLine = (a: any, b: any, pastA = 30, pastB = 30) => {
    const A = { x: sx(a.x), y: sy(a.y) }, B = { x: sx(b.x), y: sy(b.y) };
    const ang = Math.atan2(B.y - A.y, B.x - A.x);
    return { x1: A.x - Math.cos(ang) * pastA, y1: A.y - Math.sin(ang) * pastA, x2: B.x + Math.cos(ang) * pastB, y2: B.y + Math.sin(ang) * pastB };
  };

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        {/* the circle */}
        <circle cx={sx(0)} cy={sy(0)} r={R} fill="none" stroke="var(--fg-1)" strokeWidth={2} />
        {/* highlighted arcs */}
        {arcs.map((a, i) => {
          const c = a.color ?? GEO_ACCENT;
          const p1 = get(a.from), p2 = get(a.to);
          const a1 = degScreen(O, p1), a2 = degScreen(O, p2);
          const mid = (Math.atan2(sy(p1.y) - sy(O.y), sx(p1.x) - sx(O.x)) + Math.atan2(sy(p2.y) - sy(O.y), sx(p2.x) - sx(O.x))) / 2;
          return (
            <g key={`arc${i}`}>
              <path d={arcPath(sx(0), sy(0), R, a1, a2)} fill="none" stroke={c} strokeWidth={3.5} />
              {a.label && <text x={sx(0) + Math.cos(mid) * (R + 14)} y={sy(0) + Math.sin(mid) * (R + 14) + 4} fontSize="11" textAnchor="middle" fill={c} fontWeight={700}>{a.label}</text>}
            </g>
          );
        })}
        {/* objects */}
        {objects.map((o, i) => {
          const c = (o as any).color ?? "var(--fg-1)";
          if (o.kind === "tangent") {
            const p = get(o.at);
            // tangent is perpendicular to the radius Op; draw a long line through p
            const rad = Math.atan2(sy(p.y) - sy(O.y), sx(p.x) - sx(O.x)) + Math.PI / 2;
            const L = 60;
            return <line key={i} x1={sx(p.x) - Math.cos(rad) * L} y1={sy(p.y) - Math.sin(rad) * L} x2={sx(p.x) + Math.cos(rad) * L} y2={sy(p.y) + Math.sin(rad) * L} stroke={c === "var(--fg-1)" ? GEO_BLUE : c} strokeWidth={2} />;
          }
          const a = get(o.from), b = get(o.to);
          if (o.kind === "secant") {
            const e = extendLine(a, b, 4, 34);
            return <line key={i} x1={e.x1} y1={e.y1} x2={e.x2} y2={e.y2} stroke={c} strokeWidth={2} strokeDasharray={o.dashed ? "5 4" : undefined} />;
          }
          return (
            <g key={i}>
              <line x1={sx(a.x)} y1={sy(a.y)} x2={sx(b.x)} y2={sy(b.y)} stroke={c} strokeWidth={2} strokeDasharray={o.dashed ? "5 4" : undefined} />
              {o.ticks ? <Ticks x1={sx(a.x)} y1={sy(a.y)} x2={sx(b.x)} y2={sy(b.y)} count={o.ticks} color={c} /> : null}
            </g>
          );
        })}
        {/* angle marks */}
        {angles.map((m, i) => {
          const v = get(m.at), f = get(m.from), t = get(m.to);
          const c = m.color ?? GEO_ACCENT;
          if (m.right) {
            const s = 10;
            const a1 = (degScreen(v, f) * Math.PI) / 180, a2 = (degScreen(v, t) * Math.PI) / 180;
            const d1 = { x: Math.cos(a1), y: Math.sin(a1) }, d2 = { x: Math.cos(a2), y: Math.sin(a2) };
            const cc = { x: sx(v.x), y: sy(v.y) };
            return <path key={`m${i}`} d={`M ${cc.x + d1.x * s} ${cc.y + d1.y * s} L ${cc.x + (d1.x + d2.x) * s} ${cc.y + (d1.y + d2.y) * s} L ${cc.x + d2.x * s} ${cc.y + d2.y * s}`} fill="none" stroke={c} strokeWidth={1.6} />;
          }
          const a1 = degScreen(v, f), a2 = degScreen(v, t);
          let d = a2 - a1; while (d < -180) d += 360; while (d > 180) d -= 360;
          const midA = ((a1 + a1 + d) / 2) * Math.PI / 180;
          return (
            <g key={`m${i}`}>
              <path d={arcPath(sx(v.x), sy(v.y), 18, a1, a2)} fill="none" stroke={c} strokeWidth={1.8} />
              {m.label && <text x={sx(v.x) + Math.cos(midA) * 30} y={sy(v.y) + Math.sin(midA) * 30 + 4} fontSize="11" textAnchor="middle" fill={c} fontWeight={700}>{m.label}</text>}
            </g>
          );
        })}
        {/* external point tangents / secant */}
        {ext && external?.tangents && (() => {
          // tangent points: where lines from ext touch the circle. |Oext| = d, radius r; tangent length = √(d²−r²); tangent point angle offset = acos(r/d) from the Oext direction
          const d = external.dist;
          const base = external.deg;
          const off = (Math.acos(radius / d) * 180) / Math.PI;
          const tp1 = pointOnCircle(0, 0, radius, base + off);
          const tp2 = pointOnCircle(0, 0, radius, base - off);
          return (
            <g>
              <line x1={sx(ext.x)} y1={sy(ext.y)} x2={sx(tp1.x)} y2={sy(tp1.y)} stroke={GEO_ACCENT} strokeWidth={2} />
              <line x1={sx(ext.x)} y1={sy(ext.y)} x2={sx(tp2.x)} y2={sy(tp2.y)} stroke={GEO_ACCENT} strokeWidth={2} />
            </g>
          );
        })()}
        {/* centre */}
        {showCenter && <><circle cx={sx(0)} cy={sy(0)} r={3} fill="var(--fg)" /><text x={sx(0) - 6} y={sy(0) + 15} fontSize="12" fontStyle="italic" fontFamily="serif" fill="var(--fg)">O</text></>}
        {/* points */}
        {points.map((p) => {
          const pt = get(p.id);
          const out = pointOnCircle(0, 0, radius + 0.55, p.deg);
          return (
            <g key={p.id}>
              <circle cx={sx(pt.x)} cy={sy(pt.y)} r={3.2} fill="var(--fg)" />
              {(p.label ?? p.id) !== "" && <text x={sx(out.x)} y={sy(out.y) + 4} fontSize="12" textAnchor="middle" fontStyle="italic" fontFamily="serif" fill="var(--fg)">{p.label ?? p.id}</text>}
            </g>
          );
        })}
        {ext && external && (
          <g>
            <circle cx={sx(ext.x)} cy={sy(ext.y)} r={3.2} fill="var(--fg)" />
            <text x={sx(ext.x) + 8} y={sy(ext.y) + 4} fontSize="12" fontStyle="italic" fontFamily="serif" fill="var(--fg)">{external.label ?? external.id}</text>
          </g>
        )}
      </svg>
      {caption && <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>{caption}</div>}
    </div>
  );
}
