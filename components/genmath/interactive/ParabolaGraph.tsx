"use client";

import { useEffect, useMemo, useState } from "react";
import { Minus, Plus, RotateCcw } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type ParabolaGraphConfig } from "@/lib/genmath-interactive";

// The quadratic-functions workbench — one animated parabola, five modes:
//  shape:      y = ax² with a stepper on a. Flip it, widen it, squash it; the
//              curve springs between shapes and mirror-pair dots show symmetry.
//  vertex:     y = a(x−h)² + k with steppers on h and k. The whole parabola
//              glides; the vertex dot and the dashed axis of symmetry track it.
//  standard:   y = ax² + bx + c with steppers on b and c. The axis x = −b/2a,
//              the vertex, and the y-intercept (0, c) are computed live.
//  roots:      y = a(x−h)² + k with a stepper on k only. Raising and lowering
//              the parabola makes its x-intercepts appear, kiss, and vanish —
//              the discriminant story, played on the axis.
//  projectile: a ball flies along h = v₀t − 5t², leaving a trail; the apex is
//              marked at the vertex. Auto-plays with a replay (max/min lessons).
// Everything renders from springs so steps glide instead of jump.

const RED = "rgb(200,60,60)";

function fmt(n: number): string {
  const r = Math.round(n * 100) / 100;
  return Number.isInteger(r) ? r.toString() : r.toString();
}

// y = a(x−h)² + k rendered as a readable equation string (plain text, not TeX —
// it sits inside the SVG/legend where MathText doesn't reach).
function vertexEqn(a: number, h: number, k: number): string {
  const aPart = a === 1 ? "" : a === -1 ? "−" : a < 0 ? `−${fmt(Math.abs(a))}` : fmt(a);
  const inner = h === 0 ? "x" : `(x ${h > 0 ? "−" : "+"} ${fmt(Math.abs(h))})`;
  const sq = h === 0 ? "x²" : `${inner}²`;
  const kPart = k === 0 ? "" : ` ${k > 0 ? "+" : "−"} ${fmt(Math.abs(k))}`;
  return `y = ${aPart}${sq}${kPart}`;
}
function stdEqn(a: number, b: number, c: number): string {
  const aPart = a === 1 ? "x²" : a === -1 ? "−x²" : `${fmt(a)}x²`;
  const bPart = b === 0 ? "" : ` ${b > 0 ? "+" : "−"} ${fmt(Math.abs(b))}x`;
  const cPart = c === 0 ? "" : ` ${c > 0 ? "+" : "−"} ${fmt(Math.abs(c))}`;
  return `y = ${aPart}${bPart}${cPart}`;
}

export default function ParabolaGraph({ config }: { config: ParabolaGraphConfig }) {
  const {
    mode,
    a: a0 = mode === "shape" ? 1 : 1,
    h: h0 = 0,
    k: k0 = 0,
    b: b0 = 0,
    c: c0 = 0,
    v0 = 20,
    interactive = true,
    min = -6,
    max = 6,
  } = config;

  // ---- state per mode (unused ones just sit still) ----
  const [a, setA] = useState(a0);
  const [h, setH] = useState(h0);
  const [k, setK] = useState(k0);
  const [b, setB] = useState(b0);
  const [c, setC] = useState(c0);

  // ---- springs ----
  const ad = useAnimatedValue(a, { stiffness: 120, damping: 18, from: mode === "shape" ? 0 : a });
  const hd = useAnimatedValue(h, { stiffness: 120, damping: 18 });
  const kd = useAnimatedValue(k, { stiffness: 120, damping: 18, from: mode === "roots" ? Math.abs(k) + 3 : k });
  const bd = useAnimatedValue(b, { stiffness: 120, damping: 18, from: 0 });
  const cd = useAnimatedValue(c, { stiffness: 120, damping: 18 });

  // ---- projectile auto-play ----
  const [go, setGo] = useState(false);
  useEffect(() => {
    if (mode !== "projectile") return;
    const id = setTimeout(() => setGo(true), 700);
    return () => clearTimeout(id);
  }, [mode]);
  const flight = useAnimatedValue(go ? 1 : 0, { stiffness: 11, damping: 7.5 });
  const fp = Math.max(0, Math.min(1, flight));
  const replay = () => {
    setGo(false);
    setTimeout(() => setGo(true), 380);
  };

  // ---- grid geometry ----
  const N = max - min;
  const cell = 26;
  const pad = 20;
  const W = N * cell + pad * 2;
  const px = (gx: number) => pad + (gx - min) * cell;
  const py = (gy: number) => pad + (max - gy) * cell;
  const ints = Array.from({ length: N + 1 }, (_, i) => min + i);
  const step = N > 12 ? 2 : 1;

  // ---- the drawn curve (from springs) ----
  const yAt = (x: number): number => {
    if (mode === "standard") return ad * x * x + bd * x + cd;
    return ad * (x - hd) * (x - hd) + kd; // shape / vertex / roots
  };
  const curvePath = useMemo(() => {
    if (mode === "projectile") return "";
    const pts: string[] = [];
    const S = 0.125;
    for (let x = min; x <= max + 1e-9; x += S) {
      const y = yAt(x);
      // let the curve run just past the frame so clipping looks natural
      pts.push(`${px(x)},${py(Math.max(min - 2, Math.min(max + 2, y)))}`);
    }
    return `M ${pts.join(" L ")}`;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [ad, hd, kd, bd, cd, mode]);

  // ---- exact features (from TARGET values, not springs) ----
  const vx = mode === "standard" ? (a === 0 ? 0 : -b / (2 * a)) : h;
  const vy = mode === "standard" ? a * vx * vx + b * vx + c : k;
  // drawn (spring) vertex so the dot glides with the curve
  const vxd = mode === "standard" ? (ad === 0 ? 0 : -bd / (2 * ad)) : hd;
  const vyd = mode === "standard" ? ad * vxd * vxd + bd * vxd + cd : kd;

  // roots mode: x-intercepts of a(x−h)² + k = 0 → h ± √(−k/a)
  const under = mode === "roots" ? -k / a : NaN;
  const rootCount = mode === "roots" ? (under > 0 ? 2 : under === 0 ? 1 : 0) : 0;
  const rootOff = rootCount > 0 ? Math.sqrt(Math.max(0, -kd / ad)) : 0;

  // projectile geometry: h(t) = v0·t − 5t², flight ends at t = v0/5
  const tEnd = v0 / 5;
  const apexT = v0 / 10;
  const apexH = v0 * apexT - 5 * apexT * apexT;
  const PW = 320;
  const PH = 205;
  const ppadL = 34;
  const ppadB = 26;
  const ppadT = 18;
  const ptx = (t: number) => ppadL + (t / tEnd) * (PW - ppadL - 14);
  const pty = (hh: number) => (PH - ppadB) - (hh / (apexH * 1.12)) * (PH - ppadB - ppadT);
  const tNow = tEnd * fp;
  const hNow = v0 * tNow - 5 * tNow * tNow;
  const trail = useMemo(() => {
    if (mode !== "projectile") return "";
    const pts: string[] = [];
    const S = tEnd / 90;
    for (let t = 0; t <= tNow + 1e-9; t += S) {
      pts.push(`${ptx(t)},${pty(v0 * t - 5 * t * t)}`);
    }
    return pts.length > 1 ? `M ${pts.join(" L ")}` : "";
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [fp, mode]);

  const stepper = (label: string, val: number, set: (f: (v: number) => number) => void, lo: number, hi: number, delta: number, color: string = GEO_BLUE) => (
    <div className="text-center">
      <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>{label}</div>
      <div className="mt-1 flex items-center gap-2">
        <button type="button" onClick={() => set((v) => Math.max(lo, Math.round((v - delta) * 100) / 100))} disabled={val <= lo} aria-label={`Decrease ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 40, fontSize: 16, color }}>{fmt(val)}</div>
        <button type="button" onClick={() => set((v) => Math.min(hi, Math.round((v + delta) * 100) / 100))} disabled={val >= hi} aria-label={`Increase ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
    </div>
  );

  // shape mode: skip a = 0 (not a parabola) by stepping over it
  const stepA = (f: (v: number) => number) => {
    setA((v) => {
      let next = f(v);
      if (Math.abs(next) < 1e-9) next = f(next); // hop over zero
      return next;
    });
  };

  // ======================================================== projectile render
  if (mode === "projectile") {
    const apexPassed = tNow >= apexT - 0.02;
    const landed = fp > 0.985;
    return (
      <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
        <svg viewBox={`0 0 ${PW} ${PH}`} width="100%" style={{ maxWidth: 360, display: "block", margin: "0 auto" }} role="img" aria-label="A ball flying along a parabolic arc">
          {/* axes */}
          <line x1={ppadL} y1={PH - ppadB} x2={PW - 8} y2={PH - ppadB} stroke="var(--fg-2)" strokeWidth={1.6} />
          <line x1={ppadL} y1={PH - ppadB} x2={ppadL} y2={8} stroke="var(--fg-2)" strokeWidth={1.6} />
          <text x={PW - 10} y={PH - ppadB + 14} fontSize="10" fill="var(--fg-3)" textAnchor="end">time t (s)</text>
          <text x={ppadL - 6} y={14} fontSize="10" fill="var(--fg-3)" textAnchor="end">h (m)</text>
          {/* t ticks each second */}
          {Array.from({ length: Math.floor(tEnd) + 1 }, (_, i) => i).map((t) => (
            <g key={t}>
              <line x1={ptx(t)} y1={PH - ppadB - 3} x2={ptx(t)} y2={PH - ppadB + 3} stroke="var(--fg-3)" strokeWidth={1} />
              <text x={ptx(t)} y={PH - ppadB + 14} fontSize="9" fill="var(--fg-3)" textAnchor="middle">{t}</text>
            </g>
          ))}
          {/* height gridline + label at the apex */}
          <line x1={ppadL} y1={pty(apexH)} x2={PW - 8} y2={pty(apexH)} stroke="var(--line)" strokeWidth={1} strokeDasharray="4 4" />
          <text x={ppadL - 5} y={pty(apexH) + 3} fontSize="9" fill="var(--fg-3)" textAnchor="end">{fmt(apexH)}</text>

          {/* full arc, faint — the road ahead */}
          <path d={(() => { const pts: string[] = []; for (let t = 0; t <= tEnd + 1e-9; t += tEnd / 90) pts.push(`${ptx(t)},${pty(v0 * t - 5 * t * t)}`); return `M ${pts.join(" L ")}`; })()} fill="none" stroke="var(--line)" strokeWidth={1.6} strokeDasharray="3 5" />
          {/* flown trail */}
          {trail && <path d={trail} fill="none" stroke={GEO_ACCENT} strokeWidth={2.8} strokeLinecap="round" />}

          {/* apex beacon (appears once passed) */}
          {apexPassed && (
            <g className="gm-fade">
              <circle cx={ptx(apexT)} cy={pty(apexH)} r={10} fill="none" stroke={GEO_BLUE} strokeWidth={1.4} opacity={0.5} className="gm-beacon" />
              <circle cx={ptx(apexT)} cy={pty(apexH)} r={3.4} fill={GEO_BLUE} />
              <text x={ptx(apexT)} y={pty(apexH) - 14} fontSize="10.5" fontWeight={700} fill={GEO_BLUE} textAnchor="middle">
                vertex ({fmt(apexT)}, {fmt(apexH)})
              </text>
            </g>
          )}

          {/* the ball */}
          <circle cx={ptx(tNow)} cy={pty(hNow)} r={6.5} fill={GEO_ACCENT} stroke="var(--bg-1)" strokeWidth={1.5} />
          {/* landing flash */}
          {landed && <circle cx={ptx(tEnd)} cy={pty(0)} r={11} fill="none" stroke={GEO_ACCENT} strokeWidth={1.6} opacity={0.5} className="gm-beacon" />}
        </svg>

        <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            h = {fmt(v0)}t − 5t²  ·  t = <b style={{ color: GEO_ACCENT }}>{tNow.toFixed(1)}</b> s, h = <b style={{ color: GEO_ACCENT }}>{Math.max(0, hNow).toFixed(1)}</b> m
          </div>
          <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>
            {landed
              ? <>Landed at t = {fmt(tEnd)} s. The peak was the <b style={{ color: GEO_BLUE }}>vertex</b>: t = {fmt(apexT)} s, h = {fmt(apexH)} m — highest point, halfway through the flight.</>
              : apexPassed
                ? <>Past the peak — the vertex was the maximum. Coming down now.</>
                : <>Climbing… the parabola's vertex will be the highest point.</>}
          </div>
        </div>

        <div className="mt-3 flex justify-center">
          <button type="button" onClick={replay} aria-label="Throw again" className="gm-press flex items-center gap-1.5 rounded-full px-4 py-2 text-[13px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}>
            <RotateCcw className="h-3.5 w-3.5" /> Throw it again
          </button>
        </div>
      </div>
    );
  }

  // ======================================================== grid modes render
  const showAxisOfSym = mode !== "shape";
  const yint = mode === "standard" ? c : null;
  const eqnText = mode === "standard" ? stdEqn(a, b, c) : vertexEqn(a, h, k);

  // symmetry mirror dots (shape mode): (±1, a), (±2, 4a)
  const mirror = mode === "shape" ? [1, 2].map((m) => ({ x: m, y: a * m * m })) : [];

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${W}`} width="100%" style={{ maxWidth: 340 }} role="img" aria-label="A parabola on a coordinate grid">
          {ints.map((g) => (
            <g key={`g${g}`}>
              <line x1={px(g)} y1={py(max)} x2={px(g)} y2={py(min)} stroke="var(--line)" strokeWidth={1} />
              <line x1={px(min)} y1={py(g)} x2={px(max)} y2={py(g)} stroke="var(--line)" strokeWidth={1} />
            </g>
          ))}
          <line x1={px(min)} y1={py(0)} x2={px(max)} y2={py(0)} stroke="var(--fg-2)" strokeWidth={1.8} />
          <line x1={px(0)} y1={py(max)} x2={px(0)} y2={py(min)} stroke="var(--fg-2)" strokeWidth={1.8} />
          <text x={px(max) + 5} y={py(0) + 4} fontSize="11" fill="var(--fg-3)">x</text>
          <text x={px(0) - 4} y={py(max) - 5} fontSize="11" fill="var(--fg-3)" textAnchor="end">y</text>
          {ints.filter((g) => g !== 0 && g % step === 0).map((g) => (
            <g key={`lbl${g}`}>
              <text x={px(g)} y={py(0) + 12} fontSize="8.5" fill="var(--fg-3)" textAnchor="middle">{g}</text>
              <text x={px(0) - 5} y={py(g) + 3} fontSize="8.5" fill="var(--fg-3)" textAnchor="end">{g}</text>
            </g>
          ))}

          {/* axis of symmetry — tracks the vertex */}
          {showAxisOfSym && vxd >= min && vxd <= max && (
            <line x1={px(vxd)} y1={py(max)} x2={px(vxd)} y2={py(min)} stroke={GEO_BLUE} strokeWidth={1.4} strokeDasharray="6 5" opacity={0.75} />
          )}

          {/* the parabola — draws itself on, then springs between shapes */}
          <path d={curvePath} fill="none" stroke={GEO_ACCENT} strokeWidth={2.8} strokeLinecap="round" pathLength={1} className="gm-arc-sweep" />

          {/* shape mode: mirror-pair dots showing symmetry */}
          {mode === "shape" && mirror.map((m2, i) => (
            m2.y >= min && m2.y <= max ? (
              <g key={i}>
                <circle cx={px(-m2.x)} cy={py(ad * m2.x * m2.x)} r={4} fill={GEO_BLUE} className="gm-pop" style={{ animationDelay: `${0.45 + i * 0.12}s` }} />
                <circle cx={px(m2.x)} cy={py(ad * m2.x * m2.x)} r={4} fill={GEO_BLUE} className="gm-pop" style={{ animationDelay: `${0.45 + i * 0.12}s` }} />
              </g>
            ) : null
          ))}

          {/* roots mode: x-intercepts (or the kiss, or nothing) */}
          {mode === "roots" && rootCount === 2 && (
            <g>
              {[-1, 1].map((s) => (
                <g key={s}>
                  <circle cx={px(hd + s * rootOff)} cy={py(0)} r={9} fill="none" stroke={GEO_BLUE} strokeWidth={1.3} opacity={0.5} className="gm-beacon" />
                  <circle cx={px(hd + s * rootOff)} cy={py(0)} r={4.4} fill={GEO_BLUE} />
                </g>
              ))}
            </g>
          )}
          {mode === "roots" && rootCount === 1 && (
            <g>
              <circle cx={px(hd)} cy={py(0)} r={10} fill="none" stroke={GEO_BLUE} strokeWidth={1.4} opacity={0.6} className="gm-beacon" />
              <circle cx={px(hd)} cy={py(0)} r={4.6} fill={GEO_BLUE} />
            </g>
          )}

          {/* y-intercept (standard mode) */}
          {yint !== null && yint >= min && yint <= max && (
            <g>
              <circle cx={px(0)} cy={py(cd)} r={4.4} fill={GEO_BLUE} />
              <text x={px(0) + 8} y={py(cd) + 4} fontSize="11" fontWeight={700} fill={GEO_BLUE}>(0, {fmt(c)})</text>
            </g>
          )}

          {/* the vertex — ringed and labelled */}
          {vxd >= min && vxd <= max && vyd >= min - 1 && vyd <= max + 1 && (
            <g>
              <circle cx={px(vxd)} cy={py(vyd)} r={9} fill="none" stroke="var(--fg)" strokeWidth={1.1} opacity={0.35} className="gm-beacon" />
              <circle cx={px(vxd)} cy={py(vyd)} r={4.6} fill="var(--fg)" />
              <text x={px(vxd) + 9} y={py(vyd) + (a > 0 ? 16 : -10)} fontSize="12" fontWeight={700} fill="var(--fg)">
                ({fmt(vx)}, {fmt(vy)})
              </text>
            </g>
          )}
        </svg>
      </div>

      {/* equation legend */}
      <div className="mt-2 flex justify-center text-[14px]">
        <span className="serif tabular" style={{ color: GEO_ACCENT }}>{eqnText}</span>
      </div>

      {/* verdict / readout */}
      <div className="mt-2 rounded-xl p-3 text-center" style={{ transition: "background 0.35s ease, border-color 0.35s ease", background: mode === "roots" && rootCount === 0 ? "rgba(200,60,60,0.08)" : "var(--bg-2)", border: `1px solid ${mode === "roots" && rootCount === 0 ? RED : "var(--line)"}` }}>
        {mode === "shape" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              Opens <b style={{ color: GEO_ACCENT }}>{a > 0 ? "up" : "down"}</b>{Math.abs(a) !== 1 && <> · {Math.abs(a) > 1 ? <b style={{ color: GEO_BLUE }}>narrower</b> : <b style={{ color: GEO_BLUE }}>wider</b>} than y = x²</>}
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              a {a > 0 ? "> 0: happy cup" : "< 0: sad frown"} · |a| = {fmt(Math.abs(a))} {Math.abs(a) > 1 ? "(steep squeeze)" : Math.abs(a) < 1 ? "(gentle spread)" : ""} · blue dots: same height at ±x
            </div>
          </>
        )}
        {mode === "vertex" && (
          <>
            <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
              Vertex <b style={{ color: "var(--accent)" }}>({fmt(h)}, {fmt(k)})</b> · axis <b style={{ color: GEO_BLUE }}>x = {fmt(h)}</b>
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              (x − h)² slides it sideways to h; + k lifts it to k. The vertex reads straight off the form.
            </div>
          </>
        )}
        {mode === "standard" && (
          <>
            <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
              axis x = −b/2a = <b style={{ color: GEO_BLUE }}>{fmt(vx)}</b> · vertex <b style={{ color: "var(--accent)" }}>({fmt(vx)}, {fmt(vy)})</b>
            </div>
            <div className="mt-0.5 text-[12px] serif tabular" style={{ color: "var(--fg-2)" }}>
              x = −({fmt(b)})/(2·{fmt(a)}) = {fmt(vx)} · y-intercept (0, {fmt(c)}) = c, where the curve meets the y-axis
            </div>
          </>
        )}
        {mode === "roots" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              {rootCount === 2 && <><b style={{ color: GEO_BLUE }}>Two</b> x-intercepts — the equation has two real solutions</>}
              {rootCount === 1 && <>It <b style={{ color: GEO_BLUE }}>kisses</b> the axis — exactly one solution (double root)</>}
              {rootCount === 0 && <>No crossing — <b style={{ color: RED }}>no real solutions</b></>}
            </div>
            <div className="mt-0.5 text-[12px] serif tabular" style={{ color: "var(--fg-2)" }}>
              {rootCount === 2 && <>x = {fmt(h)} ± {fmt(Math.round(Math.sqrt(under) * 100) / 100)} — where y = 0</>}
              {rootCount === 1 && <>the vertex sits ON the x-axis: y = 0 exactly once</>}
              {rootCount === 0 && <>the whole curve floats {a > 0 ? "above" : "below"} the axis — y never reaches 0</>}
            </div>
          </>
        )}
      </div>

      {/* steppers */}
      {interactive && (
        <div className="mt-4 flex items-center justify-center gap-6 flex-wrap">
          {mode === "shape" && stepper("a", a, stepA, -2, 2, 0.25, GEO_ACCENT)}
          {mode === "vertex" && (
            <>
              {stepper("h (slide)", h, setH, min + 2, max - 2, 1)}
              {stepper("k (lift)", k, setK, min + 2, max - 2, 1)}
            </>
          )}
          {mode === "standard" && (
            <>
              {stepper("b", b, setB, -6, 6, 1)}
              {stepper("c", c, setC, -6, 6, 1)}
            </>
          )}
          {mode === "roots" && stepper("k (raise / lower)", k, setK, -5, 5, 1)}
        </div>
      )}
      {interactive && (
        <div className="mt-2 text-center text-[12px]" style={{ color: "var(--fg-3)" }}>
          {mode === "shape" && "step a — flip it negative, squash it toward 0, stretch it past 1"}
          {mode === "vertex" && "slide (h) and lift (k) the parabola — watch the vertex and axis follow"}
          {mode === "roots" && "raise and lower the curve — make two crossings, one kiss, then none"}
          {mode === "standard" && "step b and c — the axis, vertex, and y-intercept recompute live"}
        </div>
      )}
    </div>
  );
}
