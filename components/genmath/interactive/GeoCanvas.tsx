"use client";

import { useRef, useState } from "react";
import { Minus, Plus, Crosshair } from "lucide-react";
import MathText from "@/components/esh/MathText";
import { ArrowHead, PointDot, Ticks, GEO_ACCENT } from "@/components/genmath/interactive/GeoDiagram";
import { segmentParts } from "@/lib/geo";
import { type GeoCanvasConfig } from "@/lib/genmath-interactive";

// The interactive geometry canvas — Unit 1's foundation primitive.
//   lineThrough:     drag A or B anywhere; the unique line through them follows.
//   entityToggle:    the same two points as a line, ray AB, ray BA, or segment.
//   segmentAddition: slide B along AC and watch AB + BC = AC stay true.

const W = 320;
const H = 210;

function useSvgDrag(onMove: (x: number, y: number) => void) {
  const ref = useRef<SVGSVGElement | null>(null);
  const dragging = useRef(false);
  const toLocal = (e: React.PointerEvent) => {
    const el = ref.current;
    if (!el) return null;
    const r = el.getBoundingClientRect();
    return { x: ((e.clientX - r.left) / r.width) * W, y: ((e.clientY - r.top) / r.height) * H };
  };
  return {
    ref,
    start: (e: React.PointerEvent) => {
      dragging.current = true;
      (e.target as Element).setPointerCapture?.(e.pointerId);
      const p = toLocal(e);
      if (p) onMove(p.x, p.y);
    },
    move: (e: React.PointerEvent) => {
      if (!dragging.current) return;
      const p = toLocal(e);
      if (p) onMove(p.x, p.y);
    },
    end: () => {
      dragging.current = false;
    },
  };
}

// ---------------------------------------------------------------------------
// Mode: lineThrough
// ---------------------------------------------------------------------------
function LineThrough({ color }: { color: string }) {
  const [a, setA] = useState({ x: 100, y: 140 });
  const [b, setB] = useState({ x: 230, y: 80 });
  const [active, setActive] = useState<"a" | "b" | null>(null);

  const clamp = (v: number, lo: number, hi: number) => Math.min(hi, Math.max(lo, v));
  const drag = useSvgDrag((x, y) => {
    const p = { x: clamp(x, 20, W - 20), y: clamp(y, 20, H - 20) };
    if (active === "a") setA(p);
    if (active === "b") setB(p);
  });

  const deg = (Math.atan2(b.y - a.y, b.x - a.x) * 180) / Math.PI;
  const ext = 400;
  const ux = Math.cos((deg * Math.PI) / 180);
  const uy = Math.sin((deg * Math.PI) / 180);

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg
        ref={drag.ref}
        viewBox={`0 0 ${W} ${H}`}
        width="100%"
        style={{ maxWidth: 340, touchAction: "none", display: "block", margin: "0 auto" }}
        onPointerMove={drag.move}
        onPointerUp={drag.end}
      >
        {/* faint dot grid */}
        {Array.from({ length: 15 }).map((_, i) =>
          Array.from({ length: 10 }).map((_, j) => (
            <circle key={`${i}-${j}`} cx={10 + i * 21} cy={10 + j * 21} r={1} fill="var(--line)" />
          ))
        )}
        {/* the unique line through A and B */}
        <line x1={a.x - ux * ext} y1={a.y - uy * ext} x2={a.x + ux * ext} y2={a.y + uy * ext} stroke={color} strokeWidth={2} />
        <ArrowHead x={clampArrow(a, ux, uy, 1).x} y={clampArrow(a, ux, uy, 1).y} deg={deg} color={color} />
        <ArrowHead x={clampArrow(a, ux, uy, -1).x} y={clampArrow(a, ux, uy, -1).y} deg={deg + 180} color={color} />
        {/* draggable points */}
        {([["a", a], ["b", b]] as const).map(([id, p]) => (
          <g key={id}>
            <circle
              cx={p.x}
              cy={p.y}
              r={16}
              fill="transparent"
              style={{ cursor: "grab" }}
              onPointerDown={(e) => {
                setActive(id);
                drag.start(e);
              }}
            />
            <circle cx={p.x} cy={p.y} r={5.5} fill="var(--fg)" />
            <text x={p.x + 9} y={p.y - 9} fontSize="14" fontStyle="italic" fontFamily="serif" fill="var(--fg)">
              {id === "a" ? "A" : "B"}
            </text>
          </g>
        ))}
      </svg>

      <div className="mt-3 text-center text-[15px]" style={{ color: "var(--fg-1)" }}>
        <span className="q-math"><MathText text={"Line $\\overleftrightarrow{AB}$"} /></span> — drag either point; the line follows.
      </div>
      <div className="mt-2 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        Through two points there is <b style={{ color: "var(--fg-1)" }}>exactly one</b> line.
      </div>
    </div>
  );
}

// keep the arrowheads inside the canvas: walk from `a` along ±(ux,uy) until near an edge
function clampArrow(a: { x: number; y: number }, ux: number, uy: number, sign: 1 | -1) {
  let t = 0;
  const step = 4;
  let x = a.x, y = a.y;
  while (true) {
    const nx = a.x + ux * (t + step) * sign;
    const ny = a.y + uy * (t + step) * sign;
    if (nx < 10 || nx > W - 10 || ny < 10 || ny > H - 10) break;
    t += step;
    x = nx;
    y = ny;
  }
  return { x, y };
}

// ---------------------------------------------------------------------------
// Mode: entityToggle
// ---------------------------------------------------------------------------
type Entity = "line" | "rayAB" | "rayBA" | "segment";
const ENTITY_META: Record<Entity, { label: string; notation: string; blurb: string }> = {
  line: { label: "Line", notation: "$\\overleftrightarrow{AB}$", blurb: "extends forever in **both** directions" },
  rayAB: { label: "Ray AB", notation: "$\\overrightarrow{AB}$", blurb: "starts at $A$, passes through $B$, and keeps going" },
  rayBA: { label: "Ray BA", notation: "$\\overrightarrow{BA}$", blurb: "starts at $B$ — the **opposite** ray to $\\overrightarrow{AB}$" },
  segment: { label: "Segment", notation: "$\\overline{AB}$", blurb: "just the part **between** $A$ and $B$ — two endpoints" },
};

function EntityToggle({ color }: { color: string }) {
  const [entity, setEntity] = useState<Entity>("segment");
  const a = { x: 85, y: 105 };
  const b = { x: 235, y: 105 };
  const meta = ENTITY_META[entity];

  const left = entity === "line" || entity === "rayBA";
  const right = entity === "line" || entity === "rayAB";

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} 150`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        <line
          x1={left ? 22 : a.x}
          y1={105}
          x2={right ? W - 22 : b.x}
          y2={105}
          stroke={color}
          strokeWidth={2.4}
        />
        {left && <ArrowHead x={22} y={105} deg={180} color={color} />}
        {right && <ArrowHead x={W - 22} y={105} deg={0} color={color} />}
        <PointDot x={a.x} y={a.y} label="A" />
        <PointDot x={b.x} y={b.y} label="B" />
      </svg>

      <div className="mt-2 flex flex-wrap justify-center gap-2">
        {(Object.keys(ENTITY_META) as Entity[]).map((k) => (
          <button
            key={k}
            type="button"
            onClick={() => setEntity(k)}
            className="gm-press rounded-full px-4 py-2 text-[13px]"
            style={
              entity === k
                ? { background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }
                : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }
            }
          >
            {ENTITY_META[k].label}
          </button>
        ))}
      </div>

      <div className="mt-3 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <span className="q-math text-[17px]" style={{ color: "var(--fg)" }}>
          <MathText text={meta.notation} />
        </span>
        <div className="mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>
          <MathText text={meta.blurb} />
        </div>
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Mode: segmentAddition
// ---------------------------------------------------------------------------
function SegmentAddition({ total, start, color }: { total: number; start: number; color: string }) {
  const [t, setT] = useState(start);
  const { ab, bc, ac } = segmentParts(total, t);
  const atMid = ab === bc;

  const x0 = 30;
  const x1 = W - 30;
  const xb = x0 + ((x1 - x0) * t) / total;

  const [dragOn, setDragOn] = useState(false);
  const drag = useSvgDrag((x) => {
    if (!dragOn) return;
    const raw = ((x - x0) / (x1 - x0)) * total;
    setT(Math.min(total - 1, Math.max(1, Math.round(raw))));
  });

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg
        ref={drag.ref}
        viewBox={`0 0 ${W} 120`}
        width="100%"
        style={{ maxWidth: 340, touchAction: "none", display: "block", margin: "0 auto" }}
        onPointerMove={drag.move}
        onPointerUp={() => setDragOn(false)}
      >
        {/* whole segment */}
        <line x1={x0} y1={70} x2={x1} y2={70} stroke="var(--fg-2)" strokeWidth={2} />
        {/* AB part */}
        <line x1={x0} y1={70} x2={xb} y2={70} stroke={color} strokeWidth={3.2} />
        {atMid && (
          <>
            <Ticks x1={x0} y1={70} x2={xb} y2={70} count={1} color={color} />
            <Ticks x1={xb} y1={70} x2={x1} y2={70} count={1} color={color} />
          </>
        )}
        {/* endpoints + B */}
        <PointDot x={x0} y={70} label="A" />
        <PointDot x={x1} y={70} label="C" />
        <g>
          <circle
            cx={xb}
            cy={70}
            r={18}
            fill="transparent"
            style={{ cursor: "grab" }}
            onPointerDown={(e) => {
              setDragOn(true);
              drag.start(e);
            }}
          />
          <circle cx={xb} cy={70} r={6.5} fill={color} />
          <text x={xb - 4} y={52} fontSize="14" fontStyle="italic" fontFamily="serif" fill={color}>
            B
          </text>
        </g>
        {/* part labels */}
        <text x={(x0 + xb) / 2} y={100} fontSize="12" textAnchor="middle" fill="var(--fg-1)">
          AB = {ab}
        </text>
        <text x={(xb + x1) / 2} y={100} fontSize="12" textAnchor="middle" fill="var(--fg-1)">
          BC = {bc}
        </text>
      </svg>

      <div className="mt-2 rounded-xl p-3 text-center text-[16px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}>
        <span className="serif tabular">
          {ab} + {bc} = <b style={{ color: "var(--accent)" }}>{ac}</b>
        </span>
        {atMid && (
          <div className="mt-1 text-[13px]" style={{ color: "var(--accent)" }}>
            B is the midpoint — the two parts are congruent.
          </div>
        )}
      </div>

      <div className="mt-3 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={() => setT((v) => Math.max(1, v - 1))}
          disabled={t <= 1}
          aria-label="Move B left"
          className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <Minus className="h-4 w-4" />
        </button>
        <button
          type="button"
          onClick={() => setT(total / 2)}
          className="gm-press inline-flex items-center gap-1.5 rounded-full px-4 py-2.5 text-[13px]"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <Crosshair className="h-4 w-4" /> Snap to midpoint
        </button>
        <button
          type="button"
          onClick={() => setT((v) => Math.min(total - 1, v + 1))}
          disabled={t >= total - 1}
          aria-label="Move B right"
          className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          <Plus className="h-4 w-4" />
        </button>
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        Wherever <i>B</i> sits between <i>A</i> and <i>C</i>: <b style={{ color: "var(--fg-1)" }}>AB + BC = AC</b>.
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------

export default function GeoCanvas({ config }: { config: GeoCanvasConfig }) {
  const { mode, total = 10, start = 3, color = GEO_ACCENT } = config;
  if (mode === "lineThrough") return <LineThrough color={color} />;
  if (mode === "entityToggle") return <EntityToggle color={color} />;
  return <SegmentAddition total={total} start={start} color={color} />;
}
