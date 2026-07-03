"use client";

import { useRef, useState } from "react";
import { Minus, Plus } from "lucide-react";
import { ArrowHead, arcPath, GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { classifyAngle, clampProtractor, bisect } from "@/lib/geo";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type ProtractorConfig } from "@/lib/genmath-interactive";

// The interactive protractor. A fixed ray points right (0°); drag the other
// ray (or use the steppers) and the measure reads live off the face. Modes:
//   classify: true — names the angle acute / right / obtuse / straight.
//   bisector: true — draws the tracking half-angle ray with equal-angle arcs.
export default function Protractor({ config }: { config: ProtractorConfig }) {
  const { initial, classify = false, bisector = false, labels, color = GEO_ACCENT } = config;
  const [deg, setDeg] = useState(clampProtractor(initial));
  const svgRef = useRef<SVGSVGElement | null>(null);
  const dragging = useRef(false);

  const W = 320;
  const H = 200;
  const cx = W / 2;
  const cy = H - 30;
  const R = 128; // protractor radius
  const rayLen = 118;

  const rad = (v: number) => (v * Math.PI) / 180;
  // angle deg (0..180, counter-clockwise from +x) -> svg point
  const pt = (d: number, r: number) => ({ x: cx + r * Math.cos(rad(d)), y: cy - r * Math.sin(rad(d)) });

  const onPointer = (e: React.PointerEvent) => {
    const el = svgRef.current;
    if (!el || !dragging.current) return;
    const rect = el.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * W;
    const y = ((e.clientY - rect.top) / rect.height) * H;
    const a = (Math.atan2(cy - y, x - cx) * 180) / Math.PI;
    setDeg(clampProtractor(a));
  };

  // Draw from a stiff spring: drags track 1:1, the ±5° steppers glide.
  // All text reads the exact target `deg`, never the in-flight value.
  const degDraw = useAnimatedValue(deg, { stiffness: 320, damping: 30, from: 0 }); // the ray sweeps up from 0° on entry
  const halfDraw = bisect(degDraw);
  const moving = pt(degDraw, rayLen);
  const movingDir = -degDraw; // svg rotation for the arrowhead
  const half = bisect(deg);
  const bisPt = pt(halfDraw, rayLen - 12);
  const kind = classifyAngle(Math.max(1, deg));
  const kindLabel = deg === 0 ? "zero" : kind;

  const lab = labels ?? { vertex: "B", fixed: "C", moving: "A" };

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg
        ref={svgRef}
        viewBox={`0 0 ${W} ${H}`}
        width="100%"
        style={{ maxWidth: 340, touchAction: "none", display: "block", margin: "0 auto" }}
        onPointerDown={(e) => {
          dragging.current = true;
          (e.target as Element).setPointerCapture?.(e.pointerId);
          onPointer(e);
        }}
        onPointerMove={onPointer}
        onPointerUp={() => (dragging.current = false)}
      >
        {/* protractor face */}
        <path d={`M ${cx - R} ${cy} A ${R} ${R} 0 0 1 ${cx + R} ${cy} Z`} fill="var(--bg-2)" stroke="var(--line)" />
        {/* ticks every 10°, labels every 30° */}
        {Array.from({ length: 19 }).map((_, i) => {
          const d = i * 10;
          const p1 = pt(d, R);
          const p2 = pt(d, d % 30 === 0 ? R - 12 : R - 7);
          return <line key={d} x1={p1.x} y1={p1.y} x2={p2.x} y2={p2.y} stroke="var(--fg-3)" strokeWidth={d % 30 === 0 ? 1.4 : 1} />;
        })}
        {Array.from({ length: 7 }).map((_, i) => {
          const d = i * 30;
          const p = pt(d, R - 24);
          return (
            <text key={d} x={p.x} y={p.y + 4} fontSize="10" textAnchor="middle" fill="var(--fg-2)">
              {d}
            </text>
          );
        })}

        {/* swept angle fill */}
        <path d={`M ${cx} ${cy} L ${pt(0, 42).x} ${pt(0, 42).y} ${arcPath(cx, cy, 42, 0, -degDraw)} Z`} fill={`${color}22`} stroke="none" />
        <path d={arcPath(cx, cy, 42, 0, -degDraw)} fill="none" stroke={color} strokeWidth={2} />

        {/* bisector equal-angle arcs */}
        {bisector && deg >= 8 && (
          <>
            <path d={arcPath(cx, cy, 30, 0, -halfDraw)} fill="none" stroke={GEO_BLUE} strokeWidth={1.8} />
            <path d={arcPath(cx, cy, 34, -halfDraw, -degDraw)} fill="none" stroke={GEO_BLUE} strokeWidth={1.8} />
          </>
        )}

        {/* fixed ray at 0° */}
        <line x1={cx} y1={cy} x2={cx + rayLen} y2={cy} stroke="var(--fg-1)" strokeWidth={2.4} />
        <ArrowHead x={cx + rayLen} y={cy} deg={0} color="var(--fg-1)" />
        {/* moving ray */}
        <line x1={cx} y1={cy} x2={moving.x} y2={moving.y} stroke={color} strokeWidth={2.6} />
        <ArrowHead x={moving.x} y={moving.y} deg={movingDir} color={color} />
        {/* drag handle on the moving ray tip */}
        <circle cx={moving.x} cy={moving.y} r={16} fill="transparent" style={{ cursor: "grab" }} />
        <circle cx={moving.x} cy={moving.y} r={5} fill={color} />
        {/* bisector ray */}
        {bisector && deg >= 8 && (
          <>
            <line x1={cx} y1={cy} x2={bisPt.x} y2={bisPt.y} stroke={GEO_BLUE} strokeWidth={2} strokeDasharray="6 4" />
            <ArrowHead x={bisPt.x} y={bisPt.y} deg={-halfDraw} color={GEO_BLUE} />
          </>
        )}

        {/* vertex + labels */}
        <circle cx={cx} cy={cy} r={4} fill="var(--fg)" />
        <text x={cx - 4} y={cy + 16} fontSize="13" fontStyle="italic" fontFamily="serif" fill="var(--fg)">
          {lab.vertex}
        </text>
        <text x={cx + rayLen - 6} y={cy + 16} fontSize="13" fontStyle="italic" fontFamily="serif" fill="var(--fg-1)">
          {lab.fixed}
        </text>
        <text x={moving.x + 8} y={moving.y - 6} fontSize="13" fontStyle="italic" fontFamily="serif" fill={color}>
          {lab.moving}
        </text>
      </svg>

      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <span className="serif tabular text-[18px]" style={{ color: "var(--fg)" }}>
          m∠{lab.moving}{lab.vertex}{lab.fixed} = <b style={{ color: "var(--accent)" }}>{deg}°</b>
        </span>
        {classify && (
          <div className="mt-1 text-[14px]" style={{ color: "var(--fg-1)" }}>
            {deg === 0 ? (
              <span style={{ color: "var(--fg-3)" }}>open the angle…</span>
            ) : (
              <>
                This is <b style={{ color: "var(--accent)" }}>{kindLabel}</b>
                {kind === "acute" && " — less than 90°"}
                {kind === "right" && " — exactly 90°"}
                {kind === "obtuse" && " — between 90° and 180°"}
                {kind === "straight" && " — exactly 180°"}
              </>
            )}
          </div>
        )}
        {bisector && deg >= 8 && (
          <div className="mt-1 text-[14px]" style={{ color: "var(--fg-1)" }}>
            Bisector splits it: <span className="serif tabular" style={{ color: GEO_BLUE }}>{half}° + {half}° = {deg}°</span>
          </div>
        )}
      </div>

      <div className="mt-3 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={() => setDeg((v) => clampProtractor(v - 5))}
          disabled={deg <= 0}
          aria-label="Close the angle"
          className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <Minus className="h-4 w-4" />
        </button>
        <div className="text-center text-[12px]" style={{ color: "var(--fg-3)", minWidth: 90 }}>
          drag the ray
          <br />
          or step ±5°
        </div>
        <button
          type="button"
          onClick={() => setDeg((v) => clampProtractor(v + 5))}
          disabled={deg >= 180}
          aria-label="Open the angle"
          className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          <Plus className="h-4 w-4" />
        </button>
      </div>
    </div>
  );
}
