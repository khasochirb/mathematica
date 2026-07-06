"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type ConicGraphConfig } from "@/lib/genmath-interactive";

// The conic-sections workbench — four modes, one per curve:
//  circle:    (x − h)² + y² = r², with h and r steppers. The center slides,
//             the radius breathes, the equation follows.
//  ellipse:   x²/a² + y²/b² = 1 with a and b steppers. The two foci ride the
//             long axis at c = √|a² − b²| (beacons), swapping axes when b
//             overtakes a; eccentricity read out live.
//  parabola:  x² = 4py with a p-stepper: the focus climbs (beacon) and the
//             directrix (dashed) sinks — the curve is every point equidistant
//             from both.
//  hyperbola: x²/a² − y²/b² = 1 with a and b steppers: two branches hugging
//             the dashed asymptotes y = ±(b/a)x; foci outside at c² = a² + b².

const RED = "rgb(200,60,60)";

function fmt(n: number, dp = 2): string {
  return (Math.round(n * 10 ** dp) / 10 ** dp).toString();
}

export default function ConicGraph({ config }: { config: ConicGraphConfig }) {
  const { mode } = config;

  const [p1, setP1] = useState(mode === "circle" ? 0 : mode === "ellipse" ? 4 : mode === "parabola" ? 1 : 2); // h | a | p | a
  const [p2, setP2] = useState(mode === "circle" ? 2 : mode === "ellipse" ? 2 : 1); // r | b | – | b

  const a1 = useAnimatedValue(p1, { stiffness: 120, damping: 18 });
  const a2 = useAnimatedValue(p2, { stiffness: 120, damping: 18 });

  // grid — centered origin
  const W = 320;
  const H = 300;
  const padL = 26, padR = 12, padT = 12, padB = 22;
  const R = 5.5;
  const px = (x: number) => padL + ((x + R) / (2 * R)) * (W - padL - padR);
  const py = (y: number) => (H - padB) - ((y + R) / (2 * R)) * (H - padB - padT);

  // curve path per mode (parametric / piecewise sampling)
  const path = (() => {
    let d = "";
    if (mode === "circle") {
      for (let t = 0; t <= 2 * Math.PI + 0.01; t += 0.05) {
        const x = a1 + a2 * Math.cos(t);
        const y = a2 * Math.sin(t);
        d += `${d ? "L" : "M"} ${px(x)} ${py(y)} `;
      }
    } else if (mode === "ellipse") {
      for (let t = 0; t <= 2 * Math.PI + 0.01; t += 0.05) {
        d += `${d ? "L" : "M"} ${px(a1 * Math.cos(t))} ${py(a2 * Math.sin(t))} `;
      }
    } else if (mode === "parabola") {
      for (let x = -5.2; x <= 5.2; x += 0.08) {
        const y = (x * x) / (4 * a1);
        if (y > R + 1) { continue; }
        d += `${d ? "L" : "M"} ${px(x)} ${py(y)} `;
      }
    }
    return d.trim();
  })();

  const hyperPaths = (() => {
    if (mode !== "hyperbola") return [];
    const seg = (sign: 1 | -1) => {
      let d = "";
      for (let t = -2.2; t <= 2.2; t += 0.05) {
        const x = sign * a1 * Math.cosh(t);
        const y = a2 * Math.sinh(t);
        if (Math.abs(x) > R + 1 || Math.abs(y) > R + 1) { if (d) continue; }
        d += `${d ? "L" : "M"} ${px(x)} ${py(y)} `;
      }
      return d.trim();
    };
    return [seg(1), seg(-1)];
  })();

  // foci / focus / directrix
  const cEll = Math.sqrt(Math.abs(p1 * p1 - p2 * p2));
  const ellHorizontal = p1 >= p2;
  const cHyp = Math.sqrt(p1 * p1 + p2 * p2);
  const ecc = mode === "ellipse" ? cEll / Math.max(p1, p2) : mode === "hyperbola" ? cHyp / p1 : 0;

  const eqnText =
    mode === "circle" ? `(x ${p1 >= 0 ? "−" : "+"} ${Math.abs(p1)})² + y² = ${p2 * p2}` :
    mode === "ellipse" ? `x²/${p1 * p1} + y²/${p2 * p2} = 1` :
    mode === "parabola" ? `x² = ${4 * p1}y` :
    `x²/${p1 * p1} − y²/${p2 * p2} = 1`;

  const stepper = (label: string, val: number, set: (f: (v: number) => number) => void, lo: number, hi: number, color: string) => (
    <div className="text-center">
      <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>{label}</div>
      <div className="mt-1 flex items-center gap-2">
        <button type="button" onClick={() => set((v) => Math.max(lo, v - 1))} disabled={val <= lo} aria-label={`Decrease ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 34, fontSize: 16, color }}>{val}</div>
        <button type="button" onClick={() => set((v) => Math.min(hi, v + 1))} disabled={val >= hi} aria-label={`Increase ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
    </div>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340 }} role="img" aria-label="A conic section on a grid">
          {Array.from({ length: 11 }, (_, i) => i - 5).map((g) => (
            <g key={g}>
              <line x1={px(g)} y1={py(-R)} x2={px(g)} y2={py(R)} stroke="var(--line)" strokeWidth={1} />
              <line x1={px(-R)} y1={py(g)} x2={px(R)} y2={py(g)} stroke="var(--line)" strokeWidth={1} />
            </g>
          ))}
          <line x1={px(-R)} y1={py(0)} x2={px(R)} y2={py(0)} stroke="var(--fg-2)" strokeWidth={1.8} />
          <line x1={px(0)} y1={py(-R)} x2={px(0)} y2={py(R)} stroke="var(--fg-2)" strokeWidth={1.8} />
          {[-4, -2, 2, 4].map((g) => (
            <text key={`x${g}`} x={px(g)} y={py(0) + 13} fontSize="9" fill="var(--fg-3)" textAnchor="middle">{g}</text>
          ))}
          {[-4, -2, 2, 4].map((g) => (
            <text key={`y${g}`} x={px(0) - 5} y={py(g) + 3} fontSize="9" fill="var(--fg-3)" textAnchor="end">{g}</text>
          ))}

          {/* hyperbola asymptotes */}
          {mode === "hyperbola" && (
            <>
              <line x1={px(-R)} y1={py(-R * (a2 / a1))} x2={px(R)} y2={py(R * (a2 / a1))} stroke="var(--fg-3)" strokeWidth={1.2} strokeDasharray="5 4" />
              <line x1={px(-R)} y1={py(R * (a2 / a1))} x2={px(R)} y2={py(-R * (a2 / a1))} stroke="var(--fg-3)" strokeWidth={1.2} strokeDasharray="5 4" />
            </>
          )}

          {/* parabola directrix */}
          {mode === "parabola" && (
            <line x1={px(-R)} y1={py(-a1)} x2={px(R)} y2={py(-a1)} stroke={RED} strokeWidth={1.5} strokeDasharray="5 4" opacity={0.8} />
          )}

          {/* the curve(s) */}
          {mode !== "hyperbola" && <path d={path} fill="none" stroke={GEO_ACCENT} strokeWidth={2.8} strokeLinecap="round" pathLength={1} className="gm-arc-sweep" />}
          {mode === "hyperbola" && hyperPaths.map((d, i) => (
            <path key={i} d={d} fill="none" stroke={GEO_ACCENT} strokeWidth={2.8} strokeLinecap="round" pathLength={1} className="gm-arc-sweep" />
          ))}

          {/* centers / foci */}
          {mode === "circle" && <circle cx={px(a1)} cy={py(0)} r={4} fill={GEO_BLUE} />}
          {mode === "ellipse" && (ellHorizontal
            ? [cEll, -cEll].map((c, i) => (
                <g key={i}>
                  <circle cx={px(c)} cy={py(0)} r={8} fill="none" stroke={GEO_BLUE} strokeWidth={1.3} opacity={0.5} className="gm-beacon" />
                  <circle cx={px(c)} cy={py(0)} r={4} fill={GEO_BLUE} />
                </g>
              ))
            : [cEll, -cEll].map((c, i) => (
                <g key={i}>
                  <circle cx={px(0)} cy={py(c)} r={8} fill="none" stroke={GEO_BLUE} strokeWidth={1.3} opacity={0.5} className="gm-beacon" />
                  <circle cx={px(0)} cy={py(c)} r={4} fill={GEO_BLUE} />
                </g>
              )))}
          {mode === "parabola" && (
            <g>
              <circle cx={px(0)} cy={py(a1)} r={8} fill="none" stroke={GEO_BLUE} strokeWidth={1.3} opacity={0.5} className="gm-beacon" />
              <circle cx={px(0)} cy={py(a1)} r={4} fill={GEO_BLUE} />
            </g>
          )}
          {mode === "hyperbola" && [cHyp, -cHyp].map((c, i) => (
            <circle key={i} cx={px(c)} cy={py(0)} r={4} fill={GEO_BLUE} />
          ))}
        </svg>
      </div>

      <div className="mt-2 flex justify-center text-[14px]">
        <span className="serif tabular" style={{ color: GEO_ACCENT }}>{eqnText}</span>
      </div>

      {/* readouts */}
      <div className="mt-2 grid grid-cols-2 gap-2">
        {mode === "circle" && (
          <>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_BLUE }}>center</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>({p1}, 0)</div>
            </div>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_ACCENT }}>radius</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>√{p2 * p2} = {p2}</div>
            </div>
          </>
        )}
        {mode === "ellipse" && (
          <>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_BLUE }}>foci at c = √|a² − b²|</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>c = {fmt(cEll)}</div>
            </div>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_ACCENT }}>eccentricity c/a</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>{fmt(ecc)}</div>
            </div>
          </>
        )}
        {mode === "parabola" && (
          <>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_BLUE }}>focus</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>(0, {p1})</div>
            </div>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: RED }}>directrix</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>y = −{p1}</div>
            </div>
          </>
        )}
        {mode === "hyperbola" && (
          <>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>asymptotes</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>y = ±({p2}/{p1})x</div>
            </div>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_BLUE }}>foci at c² = a² + b²</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>c = {fmt(cHyp)}</div>
            </div>
          </>
        )}
      </div>

      {/* verdict */}
      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {mode === "circle" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              Every point exactly <b style={{ color: GEO_ACCENT }}>{p2}</b> from <b style={{ color: GEO_BLUE }}>({p1}, 0)</b>
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              the equation IS the distance formula, squared — h shifts, r breathes
            </div>
          </>
        )}
        {mode === "ellipse" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              {p1 === p2
                ? <>a = b: the foci merge — <b style={{ color: GEO_BLUE }}>a circle</b>, eccentricity 0</>
                : <>Distances to the two <b style={{ color: GEO_BLUE }}>foci</b> sum to <b style={{ color: GEO_ACCENT }}>{2 * Math.max(p1, p2)}</b> at every point</>}
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              {ellHorizontal ? "long axis horizontal (a ≥ b)" : "b beat a: the long axis flipped vertical"} · higher eccentricity = more stretched
            </div>
          </>
        )}
        {mode === "parabola" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              Every point equidistant from the <b style={{ color: GEO_BLUE }}>focus</b> and the <b style={{ color: RED }}>directrix</b>
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              bigger p: the focus climbs, the dish opens wider — satellite dishes live here
            </div>
          </>
        )}
        {mode === "hyperbola" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              Two branches hugging <b style={{ color: "var(--fg-2)" }}>y = ±({p2}/{p1})x</b> ever tighter, never touching
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              distances to the foci DIFFER by a constant (2a = {2 * p1}) — the minus sign's curve
            </div>
          </>
        )}
      </div>

      {/* controls */}
      <div className="mt-4 flex items-center justify-center gap-6">
        {mode === "circle" && (
          <>
            {stepper("center h", p1, setP1, -2, 2, GEO_BLUE)}
            {stepper("radius r", p2, setP2, 1, 4, GEO_ACCENT)}
          </>
        )}
        {mode === "ellipse" && (
          <>
            {stepper("a (x-radius)", p1, setP1, 1, 5, GEO_ACCENT)}
            {stepper("b (y-radius)", p2, setP2, 1, 5, GEO_BLUE)}
          </>
        )}
        {mode === "parabola" && stepper("focal distance p", p1, setP1, 1, 4, GEO_BLUE)}
        {mode === "hyperbola" && (
          <>
            {stepper("a", p1, setP1, 1, 4, GEO_ACCENT)}
            {stepper("b", p2, setP2, 1, 4, GEO_BLUE)}
          </>
        )}
      </div>
      <div className="mt-2 text-center text-[12px]" style={{ color: "var(--fg-3)" }}>
        {mode === "circle" && "slide the center, breathe the radius — the equation tracks both"}
        {mode === "ellipse" && "stretch a and b — watch the foci ride out and the axes swap"}
        {mode === "parabola" && "step p — focus and directrix retreat in mirrored lockstep"}
        {mode === "hyperbola" && "reshape a and b — the asymptote slopes are b/a exactly"}
      </div>
    </div>
  );
}
