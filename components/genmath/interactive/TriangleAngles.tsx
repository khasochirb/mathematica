"use client";

import { useEffect, useState } from "react";
import { Minus, Plus, RotateCcw } from "lucide-react";
import { arcPath, GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { triangleThirdAngle, exteriorAngle } from "@/lib/geo";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type TriangleAnglesConfig } from "@/lib/genmath-interactive";

// A triangle you reshape by its two base angles. The third angle updates so the
// three always total 180° — and the theorem PLAYS: the three angle wedges tear
// off the corners, glide down, and tile a straight line. Each wedge keeps its
// exact measure while it moves, so the 180° isn't asserted — it's witnessed.
// In exterior mode the base extends past a vertex and the exterior angle
// appears, equal to the sum of the two remote interior angles.
const W = 320;

const GREEN = "#3fa06a";

// sector with an EXPLICIT start + sweep (deg, screen coords, sweep in (0,180)) —
// no shortest-way normalization, because a mid-flight wedge must keep its sweep.
function wedgePath(cx: number, cy: number, r: number, start: number, sweep: number) {
  const rad = (v: number) => (v * Math.PI) / 180;
  const x1 = cx + r * Math.cos(rad(start));
  const y1 = cy + r * Math.sin(rad(start));
  const x2 = cx + r * Math.cos(rad(start + sweep));
  const y2 = cy + r * Math.sin(rad(start + sweep));
  return `M ${cx} ${cy} L ${x1} ${y1} A ${r} ${r} 0 ${sweep > 180 ? 1 : 0} 1 ${x2} ${y2} Z`;
}

// shortest-path angle interpolation
function lerpAngle(a: number, b: number, t: number) {
  const d = ((b - a + 540) % 360) - 180;
  return a + d * t;
}
const lerp = (a: number, b: number, t: number) => a + (b - a) * t;

export default function TriangleAngles({ config }: { config: TriangleAnglesConfig }) {
  const { beta: b0 = 55, gamma: g0 = 65, exterior = false, color = GEO_ACCENT } = config;
  const [beta, setBeta] = useState(b0);
  const [gamma, setGamma] = useState(g0);
  const alpha = triangleThirdAngle(beta, gamma);

  // the tear animation: auto-plays shortly after the figure appears
  const [go, setGo] = useState(false);
  useEffect(() => {
    const id = setTimeout(() => setGo(true), 600);
    return () => clearTimeout(id);
  }, []);
  const t = useAnimatedValue(go && !exterior ? 1 : 0, { stiffness: 38, damping: 13 });
  const tc = Math.max(0, Math.min(1, t)); // clamped for opacities
  const replay = () => {
    setGo(false);
    setTimeout(() => setGo(true), 380);
  };

  // interior mode reserves a strip at the bottom for the tiled line
  const H = exterior ? 230 : 296;
  const fitH = exterior ? H - 40 : H - 106;

  // triangle in math coords (y up): B=(0,0), C=(base,0), apex A
  const base = 6;
  const rad = (d: number) => (d * Math.PI) / 180;
  const tt = (base * Math.sin(rad(gamma))) / Math.sin(rad(beta + gamma));
  const A = { x: tt * Math.cos(rad(beta)), y: tt * Math.sin(rad(beta)) };
  const B = { x: 0, y: 0 };
  const C = { x: base, y: 0 };
  const extPt = { x: base + 2.4, y: 0 }; // base extended past C

  // fit to viewBox
  const pts = [A, B, C, ...(exterior ? [extPt] : [])];
  const minX = Math.min(...pts.map((p) => p.x)) - 0.8;
  const maxX = Math.max(...pts.map((p) => p.x)) + 0.8;
  const minY = Math.min(...pts.map((p) => p.y)) - 0.8;
  const maxY = Math.max(...pts.map((p) => p.y)) + 0.8;
  const scale = Math.min((W - 40) / (maxX - minX), fitH / (maxY - minY));
  const ox = (W - (maxX - minX) * scale) / 2;
  const oy = exterior ? (H - (maxY - minY) * scale) / 2 : H - 106 - (maxY - minY) * scale - 10;
  const px = (x: number) => ox + (x - minX) * scale;
  const py = (y: number) => oy + (maxY - y) * scale;

  const dirDeg = (from: { x: number; y: number }, to: { x: number; y: number }) =>
    (Math.atan2(py(to.y) - py(from.y), px(to.x) - px(from.x)) * 180) / Math.PI;

  // interior wedge at a vertex: start angle + positive sweep covering the inside
  const wedgeAt = (at: { x: number; y: number }, from: { x: number; y: number }, to: { x: number; y: number }, measure: number) => {
    const a1 = dirDeg(at, from);
    const a2 = dirDeg(at, to);
    let d = a2 - a1;
    while (d < -180) d += 360;
    while (d > 180) d -= 360;
    const start = d >= 0 ? a1 : a1 + d;
    return { cx: px(at.x), cy: py(at.y), start, sweep: measure };
  };

  // baseline where the three wedges land, tiling the upper half-disk
  const bx = W / 2;
  const by = H - 34;
  const R = 26;
  const wedges = [
    { ...wedgeAt(A, B, C, alpha), slotStart: 180, m: alpha, col: color },
    { ...wedgeAt(B, C, A, beta), slotStart: 180 + alpha, m: beta, col: GEO_BLUE },
    { ...wedgeAt(C, A, B, gamma), slotStart: 180 + alpha + beta, m: gamma, col: GREEN },
  ];

  const Vertex = ({ at, from, to, deg, col }: { at: { x: number; y: number }; from: { x: number; y: number }; to: { x: number; y: number }; deg: number; col: string }) => {
    const a1 = dirDeg(at, from);
    const a2 = dirDeg(at, to);
    let d = a2 - a1;
    while (d < -180) d += 360;
    while (d > 180) d -= 360;
    const mid = a1 + d / 2;
    const lp = { x: px(at.x) + Math.cos(rad(mid)) * 30, y: py(at.y) + Math.sin(rad(mid)) * 30 };
    return (
      <g>
        <path d={arcPath(px(at.x), py(at.y), 20, a1, a2)} fill="none" stroke={col} strokeWidth={2} />
        <text x={lp.x} y={lp.y + 4} fontSize="12" textAnchor="middle" fill={col} fontWeight={700}>{deg}°</text>
      </g>
    );
  };

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        {/* extended base for exterior mode */}
        {exterior && (
          <>
            <line x1={px(C.x)} y1={py(C.y)} x2={px(extPt.x)} y2={py(extPt.y)} stroke="var(--fg-3)" strokeWidth={1.6} strokeDasharray="5 4" />
            <Vertex at={C} from={extPt} to={A} deg={exteriorAngle(alpha, beta)} col={GEO_BLUE} />
          </>
        )}
        {/* triangle */}
        <polygon points={`${px(A.x)},${py(A.y)} ${px(B.x)},${py(B.y)} ${px(C.x)},${py(C.y)}`} fill={`${color}12`} stroke="var(--fg-1)" strokeWidth={2} strokeLinejoin="round" />

        {exterior ? (
          <>
            <Vertex at={A} from={B} to={C} deg={alpha} col={color} />
            <Vertex at={B} from={C} to={A} deg={beta} col={color} />
            <Vertex at={C} from={A} to={B} deg={gamma} col={color} />
          </>
        ) : (
          <>
            {/* ghost arcs stay at the corners so you see where each wedge came from */}
            {wedges.map((w, i) => (
              <path key={`g${i}`} d={arcPath(w.cx, w.cy, 20, w.start, w.start + w.sweep)} fill="none" stroke={w.col} strokeWidth={1.6} opacity={0.25 + 0.75 * (1 - tc)} />
            ))}
            {/* the landing line */}
            <line x1={bx - 120} y1={by} x2={bx + 120} y2={by} stroke="var(--fg-3)" strokeWidth={1.4} strokeDasharray="5 4" opacity={0.35 + 0.65 * tc} />
            {/* the travelling wedges — each keeps its exact measure mid-flight */}
            {wedges.map((w, i) => {
              const cx = lerp(w.cx, bx, t);
              const cy = lerp(w.cy, by, t);
              const start = lerpAngle(w.start, w.slotStart, t);
              const mid = rad(start + w.sweep / 2);
              const lp = { x: cx + Math.cos(mid) * (R + 13), y: cy + Math.sin(mid) * (R + 13) };
              return (
                <g key={i}>
                  <path d={wedgePath(cx, cy, R, start, w.sweep)} fill={w.col} fillOpacity={0.3} stroke={w.col} strokeWidth={1.8} strokeLinejoin="round" />
                  <text x={lp.x} y={lp.y + 4} fontSize="11" textAnchor="middle" fill={w.col} fontWeight={700}>{w.m}°</text>
                </g>
              );
            })}
            {/* the payoff, once the wedges have landed */}
            <text x={bx} y={by + 22} fontSize="13" textAnchor="middle" fill="var(--fg)" fontWeight={700} opacity={Math.max(0, (tc - 0.75) / 0.25)}>
              a straight line — {alpha}° + {beta}° + {gamma}° = 180°
            </text>
          </>
        )}
        {/* vertex dots */}
        {[A, B, C].map((p, i) => (
          <circle key={i} cx={px(p.x)} cy={py(p.y)} r={3} fill="var(--fg)" />
        ))}
      </svg>

      {/* the sum */}
      <div className="mt-2 rounded-xl p-3 text-center text-[15px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        {exterior ? (
          <>
            Exterior angle <span className="serif tabular" style={{ color: GEO_BLUE }}>{exteriorAngle(alpha, beta)}°</span> ={" "}
            <span className="serif tabular" style={{ color }}>{alpha}° + {beta}°</span> — the two remote interior angles
          </>
        ) : (
          <span className="serif tabular">
            <span style={{ color }}>{alpha}°</span> + <span style={{ color: GEO_BLUE }}>{beta}°</span> + <span style={{ color: GREEN }}>{gamma}°</span> = <b>180°</b>
          </span>
        )}
      </div>

      {/* steppers for the two base angles (+ replay for the tear) */}
      <div className="mt-4 flex items-center justify-around gap-3">
        {[["∠B", beta, setBeta], ["∠C", gamma, setGamma]].map(([label, val, set]) => (
          <div key={label as string} className="text-center">
            <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>{label as string}</div>
            <div className="mt-1 flex items-center gap-2">
              <button type="button" onClick={() => (set as (f: (v: number) => number) => void)((v) => Math.max(25, v - 5))} disabled={(val as number) <= 25} aria-label={`Decrease ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
              <div className="serif tabular text-center" style={{ minWidth: 40, fontSize: 17, color: "var(--fg)" }}>{val as number}°</div>
              <button type="button" onClick={() => (set as (f: (v: number) => number) => void)((v) => { const other = label === "∠B" ? gamma : beta; return Math.min(180 - other - 25, v + 5); })} aria-label={`Increase ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
            </div>
          </div>
        ))}
        {!exterior && (
          <button type="button" onClick={replay} aria-label="Replay the tear" className="gm-press flex items-center gap-1.5 rounded-full px-3 py-2 text-[12px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}>
            <RotateCcw className="h-3.5 w-3.5" /> Replay
          </button>
        )}
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        {exterior
          ? <>An <b style={{ color: "var(--fg-1)" }}>exterior angle</b> equals the sum of the two <b style={{ color: "var(--fg-1)" }}>remote interior</b> angles.</>
          : <>The corners tear off and tile a straight line — reshape the triangle, they <b style={{ color: "var(--fg-1)" }}>always total 180°</b>.</>}
      </div>
    </div>
  );
}
