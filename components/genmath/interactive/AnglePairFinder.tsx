"use client";

import { useRef, useState } from "react";
import { Minus, Plus } from "lucide-react";
import { ArrowHead, arcPath, GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { crossingAngles, complement } from "@/lib/geo";
import { type AnglePairFinderConfig } from "@/lib/genmath-interactive";

// Angle pairs, live.
//  crossing: two lines cross; rotate one and watch the four angles — vertical
//            pairs stay EQUAL while linear pairs keep summing to 180°.
//  corner:   a right angle split by a ray — the two parts stay complementary.
export default function AnglePairFinder({ config }: { config: AnglePairFinderConfig }) {
  const { mode, initial, color = GEO_ACCENT } = config;
  return mode === "crossing" ? (
    <Crossing initial={initial ?? 50} color={color} />
  ) : (
    <Corner initial={initial ?? 30} color={color} />
  );
}

const W = 320;

function useAngleDrag(cx: number, cy: number, onDeg: (d: number) => void) {
  const ref = useRef<SVGSVGElement | null>(null);
  const dragging = useRef(false);
  const handle = (e: React.PointerEvent, H: number) => {
    const el = ref.current;
    if (!el || !dragging.current) return;
    const rect = el.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * W;
    const y = ((e.clientY - rect.top) / rect.height) * H;
    const a = (Math.atan2(cy - y, x - cx) * 180) / Math.PI;
    onDeg(((Math.round(a) % 180) + 180) % 180);
  };
  return { ref, dragging, handle };
}

// ---------------------------------------------------------------------------
function Crossing({ initial, color }: { initial: number; color: string }) {
  const H = 230;
  const cx = W / 2;
  const cy = 105;
  const [deg, setDeg] = useState(Math.min(160, Math.max(20, initial)));
  const [view, setView] = useState<"vertical" | "linear">("vertical");
  // drawing follows a stiff spring; the measure readouts stay exact
  const degDraw = useAnimatedValue(deg, { stiffness: 320, damping: 30 });
  const [a1, a2, a3, a4] = crossingAngles(deg);

  const drag = useAngleDrag(cx, cy, (d) => setDeg(Math.min(160, Math.max(20, d))));

  const rad = (v: number) => (v * Math.PI) / 180;
  const pt = (d: number, r: number) => ({ x: cx + r * Math.cos(rad(d)), y: cy - r * Math.sin(rad(d)) });
  const L = 135;

  // angle arcs sit between the two lines: regions [0,deg],[deg,180],[180,180+deg],[180+deg,360]
  const arcs = [
    { from: 0, to: degDraw, num: 1 },
    { from: degDraw, to: 180, num: 2 },
    { from: 180, to: 180 + degDraw, num: 3 },
    { from: 180 + degDraw, to: 360, num: 4 },
  ];
  const measures: Record<number, number> = { 1: a1, 2: a2, 3: a3, 4: a4 };
  const groupA = view === "vertical" ? [1, 3] : [1, 2];
  const colorFor = (num: number) => (groupA.includes(num) ? color : GEO_BLUE);
  const emphasized = (num: number) => (view === "vertical" ? true : num === 1 || num === 2);

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg
        ref={drag.ref}
        viewBox={`0 0 ${W} ${H}`}
        width="100%"
        style={{ maxWidth: 340, touchAction: "none", display: "block", margin: "0 auto" }}
        onPointerDown={(e) => {
          drag.dragging.current = true;
          (e.target as Element).setPointerCapture?.(e.pointerId);
          drag.handle(e, H);
        }}
        onPointerMove={(e) => drag.handle(e, H)}
        onPointerUp={() => (drag.dragging.current = false)}
      >
        {/* line 1 — fixed horizontal */}
        <line x1={cx - L} y1={cy} x2={cx + L} y2={cy} stroke="var(--fg-1)" strokeWidth={2.2} />
        <ArrowHead x={cx + L} y={cy} deg={0} color="var(--fg-1)" />
        <ArrowHead x={cx - L} y={cy} deg={180} color="var(--fg-1)" />
        {/* line 2 — rotatable */}
        {(() => {
          const p = pt(degDraw, L);
          const q = pt(degDraw + 180, L);
          return (
            <>
              <line x1={q.x} y1={q.y} x2={p.x} y2={p.y} stroke="var(--fg-1)" strokeWidth={2.2} />
              <ArrowHead x={p.x} y={p.y} deg={-degDraw} color="var(--fg-1)" />
              <ArrowHead x={q.x} y={q.y} deg={-degDraw + 180} color="var(--fg-1)" />
              <circle cx={p.x} cy={p.y} r={15} fill="transparent" style={{ cursor: "grab" }} />
              <circle cx={p.x} cy={p.y} r={4.5} fill="var(--fg-1)" />
            </>
          );
        })()}
        {/* angle arcs + numbers */}
        {arcs.map(({ from, to, num }) => {
          const mid = (from + to) / 2;
          const lp = pt(mid, 52);
          const on = emphasized(num);
          return (
            <g key={num} opacity={on ? 1 : 0.28}>
              <path d={arcPath(cx, cy, 26 + num * 2.5, -from, -to)} fill="none" stroke={colorFor(num)} strokeWidth={2} />
              <text x={lp.x} y={lp.y + 4} fontSize="12" textAnchor="middle" fill={colorFor(num)} fontWeight={700}>
                ∠{num}
              </text>
            </g>
          );
        })}
        <circle cx={cx} cy={cy} r={3.5} fill="var(--fg)" />
      </svg>

      <div className="mt-2 flex justify-center gap-2">
        {(["vertical", "linear"] as const).map((v) => (
          <button
            key={v}
            type="button"
            onClick={() => setView(v)}
            className="gm-press rounded-full px-4 py-2 text-[13px]"
            style={
              view === v
                ? { background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }
                : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }
            }
          >
            {v === "vertical" ? "Vertical pairs" : "Linear pairs"}
          </button>
        ))}
      </div>

      <div className="mt-3 rounded-xl p-3 text-center text-[15px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        {view === "vertical" ? (
          <>
            <span className="serif tabular" style={{ color }}>∠1 = ∠3 = {measures[1]}°</span>
            <span className="mx-2" style={{ color: "var(--fg-3)" }}>·</span>
            <span className="serif tabular" style={{ color: GEO_BLUE }}>∠2 = ∠4 = {measures[2]}°</span>
            <div className="mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>
              Vertical angles are <b style={{ color: "var(--fg-1)" }}>congruent</b> — always.
            </div>
          </>
        ) : (
          <>
            <span className="serif tabular">
              ∠1 + ∠2 = {measures[1]}° + {measures[2]}° = <b style={{ color: "var(--accent)" }}>180°</b>
            </span>
            <div className="mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>
              A linear pair is <b style={{ color: "var(--fg-1)" }}>supplementary</b> — always.
            </div>
          </>
        )}
      </div>

      <div className="mt-3 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={() => setDeg((v) => Math.max(20, v - 5))}
          disabled={deg <= 20}
          aria-label="Rotate line"
          className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <Minus className="h-4 w-4" />
        </button>
        <div className="text-center text-[12px]" style={{ color: "var(--fg-3)", minWidth: 90 }}>
          rotate the line
        </div>
        <button
          type="button"
          onClick={() => setDeg((v) => Math.min(160, v + 5))}
          disabled={deg >= 160}
          aria-label="Rotate line"
          className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          <Plus className="h-4 w-4" />
        </button>
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
function Corner({ initial, color }: { initial: number; color: string }) {
  const H = 200;
  const cx = 70;
  const cy = H - 40;
  const [deg, setDeg] = useState(Math.min(80, Math.max(10, initial)));
  const other = complement(deg);
  // drawing follows a stiff spring; the measure readouts stay exact
  const degDraw = useAnimatedValue(deg, { stiffness: 320, damping: 30 });
  const otherDraw = 90 - degDraw;

  const drag = useAngleDrag(cx, cy, (d) => setDeg(Math.min(80, Math.max(10, d))));

  const rad = (v: number) => (v * Math.PI) / 180;
  const pt = (d: number, r: number) => ({ x: cx + r * Math.cos(rad(d)), y: cy - r * Math.sin(rad(d)) });
  const L = 150;
  const mid = pt(degDraw, L - 12);

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg
        ref={drag.ref}
        viewBox={`0 0 ${W} ${H}`}
        width="100%"
        style={{ maxWidth: 340, touchAction: "none", display: "block", margin: "0 auto" }}
        onPointerDown={(e) => {
          drag.dragging.current = true;
          (e.target as Element).setPointerCapture?.(e.pointerId);
          drag.handle(e, H);
        }}
        onPointerMove={(e) => drag.handle(e, H)}
        onPointerUp={() => (drag.dragging.current = false)}
      >
        {/* right-angle rig: horizontal + vertical rays */}
        <line x1={cx} y1={cy} x2={cx + L} y2={cy} stroke="var(--fg-1)" strokeWidth={2.2} />
        <ArrowHead x={cx + L} y={cy} deg={0} color="var(--fg-1)" />
        <line x1={cx} y1={cy} x2={cx} y2={cy - L + 20} stroke="var(--fg-1)" strokeWidth={2.2} />
        <ArrowHead x={cx} y={cy - L + 20} deg={-90} color="var(--fg-1)" />
        {/* right-angle mark */}
        <path d={`M ${cx + 14} ${cy} L ${cx + 14} ${cy - 14} L ${cx} ${cy - 14}`} fill="none" stroke="var(--fg-3)" strokeWidth={1.4} />

        {/* middle ray */}
        <line x1={cx} y1={cy} x2={mid.x} y2={mid.y} stroke={color} strokeWidth={2.4} />
        <ArrowHead x={mid.x} y={mid.y} deg={-degDraw} color={color} />
        <circle cx={mid.x} cy={mid.y} r={15} fill="transparent" style={{ cursor: "grab" }} />
        <circle cx={mid.x} cy={mid.y} r={4.5} fill={color} />

        {/* the two complementary angles */}
        <path d={arcPath(cx, cy, 34, 0, -degDraw)} fill="none" stroke={color} strokeWidth={2.2} />
        <path d={arcPath(cx, cy, 42, -degDraw, -90)} fill="none" stroke={GEO_BLUE} strokeWidth={2.2} />
        {(() => {
          const p1 = pt(degDraw / 2, 58);
          const p2 = pt(degDraw + otherDraw / 2, 64);
          return (
            <>
              <text x={p1.x} y={p1.y + 4} fontSize="12" textAnchor="middle" fill={color} fontWeight={700}>
                {deg}°
              </text>
              <text x={p2.x} y={p2.y + 4} fontSize="12" textAnchor="middle" fill={GEO_BLUE} fontWeight={700}>
                {other}°
              </text>
            </>
          );
        })()}
        <circle cx={cx} cy={cy} r={3.5} fill="var(--fg)" />
      </svg>

      <div className="mt-2 rounded-xl p-3 text-center text-[15px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        <span className="serif tabular">
          <span style={{ color }}>{deg}°</span> + <span style={{ color: GEO_BLUE }}>{other}°</span> ={" "}
          <b style={{ color: "var(--accent)" }}>90°</b>
        </span>
        <div className="mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>
          The two parts of a right angle are <b style={{ color: "var(--fg-1)" }}>complementary</b>.
        </div>
      </div>

      <div className="mt-3 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={() => setDeg((v) => Math.max(10, v - 5))}
          disabled={deg <= 10}
          aria-label="Lower the ray"
          className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <Minus className="h-4 w-4" />
        </button>
        <div className="text-center text-[12px]" style={{ color: "var(--fg-3)", minWidth: 90 }}>
          move the ray
        </div>
        <button
          type="button"
          onClick={() => setDeg((v) => Math.min(80, v + 5))}
          disabled={deg >= 80}
          aria-label="Raise the ray"
          className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          <Plus className="h-4 w-4" />
        </button>
      </div>
    </div>
  );
}
