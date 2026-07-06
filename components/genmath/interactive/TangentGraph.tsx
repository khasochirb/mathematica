"use client";

import { useMemo, useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type TangentGraphConfig } from "@/lib/genmath-interactive";

// The derivatives workbench, built around f(x) = x²/2 (whose slope at x is
// exactly x — the cleanest possible playground). Three modes:
//  secant:     the definition, animated. A second point sits h away from
//              x = 1; the secant line through both has slope 1 + h/2. Step h
//              down 2 → 1 → 0.5 → 0.1 and the secant collapses onto the
//              dashed tangent: slope → 1. The 0/0 limit, drawn.
//  tangent:    slide the point of tangency. The tangent line springs along
//              the curve; its slope readout equals a — downhill left of the
//              vertex, flat at it (beacon), uphill right.
//  slopeCurve: f and f′ on one grid. The blue line's HEIGHT at each x is the
//              orange curve's SLOPE there — the derivative is a function.

const RED = "rgb(200,60,60)";

function fmt(n: number, dp = 2): string {
  return (Math.round(n * 10 ** dp) / 10 ** dp).toString();
}

const H_STEPS = [2, 1, 0.5, 0.25, 0.1];

export default function TangentGraph({ config }: { config: TangentGraphConfig }) {
  const { mode } = config;

  const [hi, setHi] = useState(0); // secant: index into H_STEPS
  const [a, setA] = useState(mode === "tangent" ? 2 : 1); // tangent/slopeCurve: touch point

  const h = useAnimatedValue(H_STEPS[hi], { stiffness: 120, damping: 18 });
  const ad = useAnimatedValue(a, { stiffness: 120, damping: 18 });

  // f(x) = x²/2 and f'(x) = x
  const f = (x: number) => (x * x) / 2;

  // grid geometry
  const W = 320;
  const H = 300;
  const padL = 30, padR = 14, padT = 14, padB = 26;
  const X0 = -3, X1 = 3.4, Y0 = -3, Y1 = 5;
  const px = (x: number) => padL + ((x - X0) / (X1 - X0)) * (W - padL - padR);
  const py = (y: number) => (H - padB) - ((y - Y0) / (Y1 - Y0)) * (H - padB - padT);

  const curvePath = useMemo(() => {
    let d = "";
    let pen = false;
    for (let x = X0; x <= X1 + 1e-9; x += 0.05) {
      const y = f(x);
      if (y < Y0 - 1 || y > Y1 + 1) { pen = false; continue; }
      d += `${pen ? "L" : "M"} ${px(x)} ${py(y)} `;
      pen = true;
    }
    return d.trim();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // secant mode anchors
  const sa = 1; // fixed base point x = 1
  const secSlope = sa + h / 2; // ((sa+h)²/2 − sa²/2)/h = sa + h/2
  // a line through (x0, y0) with slope m, clipped to the frame edges
  const linePts = (x0: number, y0: number, m: number) => {
    const yAt = (x: number) => y0 + m * (x - x0);
    return { x1: px(X0), y1: py(yAt(X0)), x2: px(X1), y2: py(yAt(X1)) };
  };
  const sec = linePts(sa, f(sa), secSlope);
  const tanAtSa = linePts(sa, f(sa), sa);
  const tanAtA = linePts(ad, f(ad), ad);

  const stepper = (label: string, valText: string, dec: () => void, inc: () => void, canDec: boolean, canInc: boolean, color = GEO_BLUE) => (
    <div className="text-center">
      <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>{label}</div>
      <div className="mt-1 flex items-center gap-2">
        <button type="button" onClick={dec} disabled={!canDec} aria-label={`Decrease ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 44, fontSize: 16, color }}>{valText}</div>
        <button type="button" onClick={inc} disabled={!canInc} aria-label={`Increase ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
    </div>
  );

  const eqnText =
    mode === "secant" ? "f(x) = x²/2 — secant from x = 1 to x = 1 + h" :
    mode === "tangent" ? "f(x) = x²/2 — tangent at x = a" :
    "f(x) = x²/2 (orange) and f′(x) = x (blue)";

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340 }} role="img" aria-label="A curve with a tangent or secant line">
          {Array.from({ length: 7 }, (_, i) => -3 + i).map((g) => (
            <line key={`v${g}`} x1={px(g)} y1={py(Y0)} x2={px(g)} y2={py(Y1)} stroke="var(--line)" strokeWidth={1} />
          ))}
          {Array.from({ length: Y1 - Y0 + 1 }, (_, i) => Y0 + i).map((g) => (
            <line key={`h${g}`} x1={px(X0)} y1={py(g)} x2={px(X1)} y2={py(g)} stroke="var(--line)" strokeWidth={1} />
          ))}
          <line x1={px(X0)} y1={py(0)} x2={px(X1)} y2={py(0)} stroke="var(--fg-2)" strokeWidth={1.8} />
          <line x1={px(0)} y1={py(Y0)} x2={px(0)} y2={py(Y1)} stroke="var(--fg-2)" strokeWidth={1.8} />
          {[-2, -1, 1, 2, 3].map((g) => (
            <text key={g} x={px(g)} y={py(0) + 13} fontSize="9" fill="var(--fg-3)" textAnchor="middle">{g}</text>
          ))}
          {[-2, 2, 4].map((g) => (
            <text key={g} x={px(0) - 5} y={py(g) + 3} fontSize="9" fill="var(--fg-3)" textAnchor="end">{g}</text>
          ))}

          {/* the parabola */}
          <path d={curvePath} fill="none" stroke={GEO_ACCENT} strokeWidth={2.8} strokeLinecap="round" pathLength={1} className="gm-arc-sweep" />

          {/* slopeCurve: the derivative line y = x */}
          {mode === "slopeCurve" && (
            <>
              <line x1={px(X0)} y1={py(X0)} x2={px(3.4)} y2={py(3.4)} stroke={GEO_BLUE} strokeWidth={2.2} className="gm-fade" />
              <line x1={px(ad)} y1={py(f(ad))} x2={px(ad)} y2={py(ad)} stroke="var(--fg-3)" strokeWidth={1} strokeDasharray="3 3" />
              <circle cx={px(ad)} cy={py(f(ad))} r={5.5} fill={GEO_ACCENT} stroke="var(--bg-1)" strokeWidth={1.5} />
              <circle cx={px(ad)} cy={py(ad)} r={5.5} fill={GEO_BLUE} stroke="var(--bg-1)" strokeWidth={1.5} />
            </>
          )}

          {/* secant mode */}
          {mode === "secant" && (
            <>
              <line {...tanAtSa} stroke={GEO_BLUE} strokeWidth={1.6} strokeDasharray="5 4" opacity={0.65} />
              <line {...sec} stroke={RED} strokeWidth={2} />
              <circle cx={px(sa)} cy={py(f(sa))} r={5.5} fill={GEO_BLUE} stroke="var(--bg-1)" strokeWidth={1.5} />
              <circle cx={px(sa + h)} cy={py(f(sa + h))} r={5.5} fill={RED} stroke="var(--bg-1)" strokeWidth={1.5} />
            </>
          )}

          {/* tangent mode */}
          {mode === "tangent" && (
            <>
              <line {...tanAtA} stroke={GEO_BLUE} strokeWidth={2.2} />
              {a === 0 && (
                <circle cx={px(0)} cy={py(0)} r={10} fill="none" stroke={RED} strokeWidth={1.4} opacity={0.6} className="gm-beacon" />
              )}
              <circle cx={px(ad)} cy={py(f(ad))} r={5.5} fill={GEO_ACCENT} stroke="var(--bg-1)" strokeWidth={1.5} />
            </>
          )}
        </svg>
      </div>

      <div className="mt-2 flex justify-center text-[14px]">
        <span className="serif tabular" style={{ color: GEO_ACCENT }}>{eqnText}</span>
      </div>

      {/* readout row */}
      {mode === "secant" && (
        <div className="mt-2 grid grid-cols-2 gap-2">
          <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
            <div className="text-[10px] uppercase tracking-wide" style={{ color: RED }}>secant slope</div>
            <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>
              (f(1+h) − f(1))/h = {fmt(secSlope, 3)}
            </div>
          </div>
          <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
            <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_BLUE }}>tangent slope (target)</div>
            <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>f′(1) = 1</div>
          </div>
        </div>
      )}
      {mode !== "secant" && (
        <div className="mt-2 grid grid-cols-2 gap-2">
          <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
            <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_ACCENT }}>point on f</div>
            <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>({fmt(a)}, {fmt(f(a), 2)})</div>
          </div>
          <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
            <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_BLUE }}>{mode === "tangent" ? "tangent slope" : "f′ reports"}</div>
            <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>f′({fmt(a)}) = {fmt(a)}</div>
          </div>
        </div>
      )}

      {/* verdict */}
      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {mode === "secant" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              Slope {fmt(secSlope, 3)} — shrink h and the <b style={{ color: RED }}>secant</b> collapses onto the <b style={{ color: GEO_BLUE }}>tangent</b>
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              1 + h/2 → 1 as h → 0: the derivative is this limit, drawn
            </div>
          </>
        )}
        {mode === "tangent" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              {a < 0 ? <>Slope {fmt(a)}: <b style={{ color: RED }}>downhill</b> — the curve is falling here</> :
               a === 0 ? <>Slope 0: <b style={{ color: RED }}>flat</b> — the vertex, where fall turns to rise</> :
               <>Slope {fmt(a)}: <b style={{ color: GEO_BLUE }}>uphill</b> — the curve is climbing here</>}
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              the tangent's slope IS the derivative: f′(a) = a for this curve
            </div>
          </>
        )}
        {mode === "slopeCurve" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              At x = {fmt(a)}: the <b style={{ color: GEO_BLUE }}>blue height</b> ({fmt(a)}) reports the <b style={{ color: GEO_ACCENT }}>orange slope</b>
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              the derivative is a FUNCTION: every x gets its own slope
            </div>
          </>
        )}
      </div>

      {/* controls */}
      <div className="mt-4 flex items-center justify-center gap-6">
        {mode === "secant"
          ? stepper("gap h", fmt(H_STEPS[hi]), () => setHi((i) => Math.min(H_STEPS.length - 1, i + 1)), () => setHi((i) => Math.max(0, i - 1)), hi < H_STEPS.length - 1, hi > 0, RED)
          : stepper("touch point a", fmt(a), () => setA((v) => Math.max(-2, v - 1)), () => setA((v) => Math.min(3, v + 1)), a > -2, a < 3)}
      </div>
      <div className="mt-2 text-center text-[12px]" style={{ color: "var(--fg-3)" }}>
        {mode === "secant" && "step h down — the red secant tips onto the dashed tangent"}
        {mode === "tangent" && "slide a along the curve — downhill, flat at the vertex, uphill"}
        {mode === "slopeCurve" && "move x — the blue line always knows the orange curve's slope"}
      </div>
    </div>
  );
}
