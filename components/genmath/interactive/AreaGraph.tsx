"use client";

import { useEffect, useMemo, useState } from "react";
import { Minus, Plus, RotateCcw } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type AreaGraphConfig } from "@/lib/genmath-interactive";

// The integrals workbench — three modes:
//  riemann:    left-endpoint rectangles under f(x) = x² on [0, 2]. Step n
//              through 2, 4, 8, 16, 32 and watch the staircase melt into the
//              curve while the sum readout climbs toward the true area 8/3.
//  accumulate: the area-so-far function, auto-played. A sweep line rides from
//              0 to 2 filling the region under x² behind it; the readout
//              A(x) = x³/3 grows live — area is a FUNCTION of the right edge.
//  ftc:        f(x) = x on [0, b]. The region is a triangle (geometry:
//              b²/2) and the antiderivative x²/2 evaluated at b agrees —
//              the Fundamental Theorem on the simplest possible stage.

const RED = "rgb(200,60,60)";

function fmt(n: number, dp = 3): string {
  return (Math.round(n * 10 ** dp) / 10 ** dp).toString();
}

const NS = [2, 4, 8, 16, 32];

export default function AreaGraph({ config }: { config: AreaGraphConfig }) {
  const { mode } = config;

  const [ni, setNi] = useState(0); // riemann: index into NS
  const [b, setB] = useState(2); // ftc: right edge

  // accumulate auto-play
  const [go, setGo] = useState(false);
  useEffect(() => {
    if (mode !== "accumulate") return;
    const t = setTimeout(() => setGo(true), 700);
    return () => clearTimeout(t);
  }, [mode]);
  const t = useAnimatedValue(go ? 1 : 0, { stiffness: 5, damping: 6 });
  const replay = () => {
    setGo(false);
    setTimeout(() => setGo(true), 380);
  };

  const bd = useAnimatedValue(b, { stiffness: 120, damping: 18 });

  // geometry
  const W = 320;
  const H = 300;
  const padL = 34, padR = 14, padT = 14, padB = 26;
  const X1 = mode === "ftc" ? 3.4 : 2.4;
  const Y1 = mode === "ftc" ? 3.4 : 4.4;
  const px = (x: number) => padL + (x / X1) * (W - padL - padR);
  const py = (y: number) => (H - padB) - (y / Y1) * (H - padB - padT);

  const f = (x: number): number => (mode === "ftc" ? x : x * x);

  const curvePath = useMemo(() => {
    let d = "";
    for (let x = 0; x <= X1 + 1e-9; x += 0.04) {
      const y = f(x);
      if (y > Y1 + 0.6) break;
      d += `${d ? "L" : "M"} ${px(x)} ${py(y)} `;
    }
    return d.trim();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [mode]);

  // riemann rectangles (left endpoints) on [0, 2]
  const n = NS[ni];
  const rects = useMemo(() => {
    if (mode !== "riemann") return [];
    const w = 2 / n;
    return Array.from({ length: n }, (_, i) => {
      const x0 = i * w;
      return { x: px(x0), y: py(x0 * x0), w: px(w) - px(0), h: py(0) - py(x0 * x0) };
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [mode, n]);
  const riemannSum = useMemo(() => {
    const w = 2 / n;
    let s = 0;
    for (let i = 0; i < n; i++) s += (i * w) * (i * w) * w;
    return s;
  }, [n]);

  // accumulate sweep edge
  const xEdge = 2 * Math.max(0, Math.min(1, t));
  const fillPath = useMemo(() => {
    const to = mode === "accumulate" ? xEdge : mode === "ftc" ? bd : 0;
    if (to <= 0.001) return "";
    let d = `M ${px(0)} ${py(0)} `;
    for (let x = 0; x <= to + 1e-9; x += 0.04) d += `L ${px(x)} ${py(f(x))} `;
    d += `L ${px(to)} ${py(f(to))} L ${px(to)} ${py(0)} Z`;
    return d;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [mode, xEdge, bd]);

  const eqnText =
    mode === "riemann" ? "f(x) = x² on [0, 2] — left-endpoint rectangles" :
    mode === "accumulate" ? "f(x) = x² — area filling behind the sweep line" :
    "f(x) = x on [0, b] — a triangle, two ways";

  const stepBtn = (onClick: () => void, disabled: boolean, kind: "minus" | "plus") => (
    <button type="button" onClick={onClick} disabled={disabled} aria-label={kind === "minus" ? "Fewer" : "More"}
      className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35"
      style={kind === "plus"
        ? { background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }
        : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}>
      {kind === "minus" ? <Minus className="h-4 w-4" /> : <Plus className="h-4 w-4" />}
    </button>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340 }} role="img" aria-label="Area under a curve">
          {Array.from({ length: Math.floor(X1) + 1 }, (_, i) => i).map((g) => (
            <line key={`v${g}`} x1={px(g)} y1={py(0)} x2={px(g)} y2={py(Y1)} stroke="var(--line)" strokeWidth={1} />
          ))}
          {Array.from({ length: Math.floor(Y1) + 1 }, (_, i) => i).map((g) => (
            <line key={`h${g}`} x1={px(0)} y1={py(g)} x2={px(X1)} y2={py(g)} stroke="var(--line)" strokeWidth={1} />
          ))}
          <line x1={px(0)} y1={py(0)} x2={px(X1)} y2={py(0)} stroke="var(--fg-2)" strokeWidth={1.8} />
          <line x1={px(0)} y1={py(0)} x2={px(0)} y2={py(Y1)} stroke="var(--fg-2)" strokeWidth={1.8} />
          {Array.from({ length: Math.floor(X1) }, (_, i) => i + 1).map((g) => (
            <text key={g} x={px(g)} y={py(0) + 13} fontSize="9" fill="var(--fg-3)" textAnchor="middle">{g}</text>
          ))}
          {Array.from({ length: Math.floor(Y1) }, (_, i) => i + 1).map((g) => (
            <text key={g} x={px(0) - 5} y={py(g) + 3} fontSize="9" fill="var(--fg-3)" textAnchor="end">{g}</text>
          ))}

          {/* filled area (accumulate / ftc) */}
          {fillPath && <path d={fillPath} fill={GEO_BLUE} opacity={0.22} />}

          {/* riemann rectangles */}
          {rects.map((r, i) => (
            <rect key={`${n}-${i}`} x={r.x} y={r.y} width={r.w} height={r.h} fill={GEO_BLUE} opacity={0.3} stroke={GEO_BLUE} strokeWidth={1} className="gm-fade" />
          ))}

          {/* the curve on top */}
          <path d={curvePath} fill="none" stroke={GEO_ACCENT} strokeWidth={2.8} strokeLinecap="round" pathLength={1} className="gm-arc-sweep" />

          {/* sweep line (accumulate) */}
          {mode === "accumulate" && xEdge > 0.01 && (
            <line x1={px(xEdge)} y1={py(0)} x2={px(xEdge)} y2={py(Math.min(f(xEdge), Y1))} stroke={RED} strokeWidth={2} />
          )}

          {/* ftc: right-edge marker */}
          {mode === "ftc" && (
            <line x1={px(bd)} y1={py(0)} x2={px(bd)} y2={py(f(bd))} stroke={RED} strokeWidth={2} strokeDasharray="5 4" />
          )}
        </svg>
      </div>

      <div className="mt-2 flex justify-center text-[14px]">
        <span className="serif tabular" style={{ color: GEO_ACCENT }}>{eqnText}</span>
      </div>

      {/* readouts */}
      <div className="mt-2 grid grid-cols-2 gap-2">
        {mode === "riemann" && (
          <>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_BLUE }}>rectangle sum ({n} slices)</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>{fmt(riemannSum)}</div>
            </div>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_ACCENT }}>true area (target)</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>8/3 ≈ 2.667</div>
            </div>
          </>
        )}
        {mode === "accumulate" && (
          <>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: RED }}>sweep edge x</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>{fmt(xEdge, 2)}</div>
            </div>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_BLUE }}>area so far = x³/3</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>{fmt(xEdge ** 3 / 3)}</div>
            </div>
          </>
        )}
        {mode === "ftc" && (
          <>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_BLUE }}>geometry: ½ · b · b</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>{fmt(b * b / 2, 2)}</div>
            </div>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_ACCENT }}>antiderivative: b²/2</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>{fmt(b * b / 2, 2)}</div>
            </div>
          </>
        )}
      </div>

      {/* verdict */}
      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {mode === "riemann" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              {n} slices: sum <b style={{ color: GEO_BLUE }}>{fmt(riemannSum)}</b> — off by {fmt(8 / 3 - riemannSum)}
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              more slices, thinner error: the staircase melts into the curve
            </div>
          </>
        )}
        {mode === "accumulate" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              Area-so-far is a <b style={{ color: GEO_BLUE }}>function</b>: A(x) = x³/3 — and A′(x) = x² = f(x)
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              the rate the area grows equals the curve&apos;s height — the Fundamental Theorem, live
            </div>
          </>
        )}
        {mode === "ftc" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              Triangle says <b style={{ color: GEO_BLUE }}>{fmt(b * b / 2, 2)}</b>; the antiderivative x²/2 at {b} says <b style={{ color: GEO_ACCENT }}>{fmt(b * b / 2, 2)}</b>
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              geometry and calculus agree — ∫₀ᵇ x dx = b²/2, certified by a triangle
            </div>
          </>
        )}
      </div>

      {/* controls */}
      <div className="mt-4 flex items-center justify-center gap-4">
        {mode === "riemann" && (
          <div className="text-center">
            <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>slices n</div>
            <div className="mt-1 flex items-center gap-2">
              {stepBtn(() => setNi((i) => Math.max(0, i - 1)), ni <= 0, "minus")}
              <div className="serif tabular text-center" style={{ minWidth: 44, fontSize: 16, color: GEO_BLUE }}>{n}</div>
              {stepBtn(() => setNi((i) => Math.min(NS.length - 1, i + 1)), ni >= NS.length - 1, "plus")}
            </div>
          </div>
        )}
        {mode === "ftc" && (
          <div className="text-center">
            <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>right edge b</div>
            <div className="mt-1 flex items-center gap-2">
              {stepBtn(() => setB((v) => Math.max(1, v - 1)), b <= 1, "minus")}
              <div className="serif tabular text-center" style={{ minWidth: 44, fontSize: 16, color: RED }}>{b}</div>
              {stepBtn(() => setB((v) => Math.min(3, v + 1)), b >= 3, "plus")}
            </div>
          </div>
        )}
        {mode === "accumulate" && (
          <button type="button" onClick={replay} aria-label="Replay the sweep" className="gm-press flex items-center gap-2 rounded-full px-5 py-2 text-[13px]" style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}>
            <RotateCcw className="h-3.5 w-3.5" /> replay the sweep
          </button>
        )}
      </div>
      <div className="mt-2 text-center text-[12px]" style={{ color: "var(--fg-3)" }}>
        {mode === "riemann" && "step n up — watch the staircase chase 8/3"}
        {mode === "accumulate" && "the sweep fills area; the readout grows like x³/3"}
        {mode === "ftc" && "step b — geometry and the antiderivative move in lockstep"}
      </div>
    </div>
  );
}
