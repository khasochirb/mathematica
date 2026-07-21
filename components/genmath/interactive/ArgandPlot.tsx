"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type ArgandPlotConfig } from "@/lib/genmath-interactive";

// The complex-numbers workbench (HL) — three modes:
//  plot:   z = a + bi as an arrow on the Argand diagram, with dashed legs,
//          live |z| and arg z, and (optionally) the conjugate mirrored below
//          the real axis. Steppers drive Re(z) and Im(z).
//  powers: z, z², z³, … as a chained spiral. |z| < 1 spirals in, |z| > 1
//          spirals out, |z| = 1 walks the unit circle — De Moivre live:
//          moduli multiply, arguments add.
//  roots:  the n-th roots of a unit-modulus target w as a regular n-gon on
//          the unit circle. Stepping the target's argument rotates the whole
//          polygon by φ/n — one full circle shared n ways.

const RED = "rgb(200,60,60)";

function fmt2(n: number): string {
  const r = Math.round(n * 100) / 100;
  return (Object.is(r, -0) ? 0 : r).toFixed(2);
}

// Signed a + bi string with proper minus signs.
function zLabel(a: number, b: number): string {
  const re = Math.abs(a) < 1e-9 ? "" : `${a}`;
  const im =
    Math.abs(b) < 1e-9 ? "" : `${b < 0 ? "−" : re ? "+" : ""} ${Math.abs(b) === 1 ? "" : Math.abs(b)}i`;
  if (!re && !im) return "0";
  return [re, im].filter(Boolean).join(" ").replace(/\s+/g, " ").trim();
}

function Stepper({
  label,
  onDec,
  onInc,
  value,
}: {
  label: string;
  value: string;
  onDec: () => void;
  onInc: () => void;
}) {
  return (
    <div className="flex items-center gap-1.5">
      <span className="text-[12px]" style={{ color: "var(--fg-2)" }}>{label}</span>
      <button type="button" onClick={onDec} aria-label={`decrease ${label}`} className="gm-press rounded-full p-1.5" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}>
        <Minus className="h-3.5 w-3.5" />
      </button>
      <span className="mono tabular text-[13px] text-center" style={{ color: "var(--fg)", minWidth: 42 }}>{value}</span>
      <button type="button" onClick={onInc} aria-label={`increase ${label}`} className="gm-press rounded-full p-1.5" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}>
        <Plus className="h-3.5 w-3.5" />
      </button>
    </div>
  );
}

export default function ArgandPlot({ config }: { config: ArgandPlotConfig }) {
  const {
    mode,
    a: a0 = 3,
    b: b0 = 2,
    r: r0 = 1.1,
    thetaDeg = 30,
    n: nInit = mode === "roots" ? 5 : 6,
    targetDeg = 0,
    showConjugate = true,
  } = config;

  const W = 340, H = 340, cx = W / 2, cy = H / 2;

  // ---- plot state ----
  const [a, setA] = useState(a0);
  const [b, setB] = useState(b0);
  const aD = useAnimatedValue(a, { stiffness: 120, damping: 16, from: 0 });
  const bD = useAnimatedValue(b, { stiffness: 120, damping: 16, from: 0 });

  // ---- powers state ----
  const [rIdx, setRIdx] = useState(-1); // index into R_CHOICES; -1 → from config
  const R_CHOICES = [0.85, 1, 1.1];
  const rBase = rIdx < 0 ? r0 : R_CHOICES[rIdx];
  const [nPow, setNPow] = useState(nInit);

  // ---- roots state ----
  const [nRoots, setNRoots] = useState(nInit);
  const [phi, setPhi] = useState(targetDeg); // argument of the target, degrees
  const phiD = useAnimatedValue(phi, { stiffness: 100, damping: 15, from: 0 });

  // ======================================================== plot mode
  if (mode === "plot") {
    const unit = 34; // px per 1
    const px = (re: number) => cx + re * unit;
    const py = (im: number) => cy - im * unit;
    const zx = px(aD), zy = py(bD);
    const mod = Math.sqrt(a * a + b * b);
    const arg = Math.atan2(b, a);
    const argDeg = (arg * 180) / Math.PI;

    return (
      <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }} role="img" aria-label="A complex number plotted on the Argand diagram">
          {/* grid */}
          {[-4, -3, -2, -1, 1, 2, 3, 4].map((k) => (
            <g key={k}>
              <line x1={px(k)} y1={16} x2={px(k)} y2={H - 16} stroke="var(--line)" strokeWidth={0.6} />
              <line x1={16} y1={py(k)} x2={W - 16} y2={py(k)} stroke="var(--line)" strokeWidth={0.6} />
            </g>
          ))}
          {/* axes */}
          <line x1={10} y1={cy} x2={W - 10} y2={cy} stroke="var(--fg-2)" strokeWidth={1.4} />
          <line x1={cx} y1={10} x2={cx} y2={H - 10} stroke="var(--fg-2)" strokeWidth={1.4} />
          <text x={W - 16} y={cy - 6} fontSize="10" fill="var(--fg-3)">Re</text>
          <text x={cx + 6} y={18} fontSize="10" fill="var(--fg-3)">Im</text>
          {[-3, 3].map((k) => (
            <g key={k}>
              <text x={px(k)} y={cy + 14} fontSize="9" fill="var(--fg-3)" textAnchor="middle">{k}</text>
              <text x={cx - 10} y={py(k) + 3} fontSize="9" fill="var(--fg-3)" textAnchor="middle">{k}i</text>
            </g>
          ))}

          {/* angle arc */}
          {mod > 0.2 && (
            <path
              d={`M ${px(0.7 * Math.max(0.001, Math.cos(0)))} ${py(0)} A 24 24 0 ${Math.abs(argDeg) > 180 ? 1 : 0} ${arg >= 0 ? 0 : 1} ${cx + 24 * Math.cos(arg)} ${cy - 24 * Math.sin(arg)}`}
              fill="none" stroke={GEO_ACCENT} strokeWidth={1.4} opacity={0.75}
            />
          )}

          {/* conjugate, mirrored */}
          {showConjugate && (
            <g opacity={0.75}>
              <line x1={cx} y1={cy} x2={zx} y2={py(-bD)} stroke={GEO_BLUE} strokeWidth={1.8} strokeDasharray="5 4" />
              <circle cx={zx} cy={py(-bD)} r={4.4} fill={GEO_BLUE} stroke="var(--bg-1)" strokeWidth={1.2} />
              <text x={zx + 8} y={py(-bD) + 4} fontSize="11" fontWeight={700} fill={GEO_BLUE}>z̄</text>
            </g>
          )}

          {/* dashed legs of z */}
          <line x1={zx} y1={cy} x2={zx} y2={zy} stroke="var(--fg-3)" strokeWidth={1.1} strokeDasharray="3 3" />
          <line x1={cx} y1={zy} x2={zx} y2={zy} stroke="var(--fg-3)" strokeWidth={1.1} strokeDasharray="3 3" />

          {/* z arrow */}
          <line x1={cx} y1={cy} x2={zx} y2={zy} stroke={GEO_ACCENT} strokeWidth={2.6} strokeLinecap="round" />
          <circle cx={zx} cy={zy} r={5.4} fill={GEO_ACCENT} stroke="var(--bg-1)" strokeWidth={1.4} />
          <text x={zx + (a >= 0 ? 9 : -9)} y={zy - 8} fontSize="12" fontWeight={700} fill="var(--fg)" textAnchor={a >= 0 ? "start" : "end"}>z</text>
        </svg>

        <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            z = <b style={{ color: GEO_ACCENT }}>{zLabel(a, b)}</b> · |z| = <b>{fmt2(mod)}</b> · arg z = <b>{fmt2(arg)}</b> rad ({Math.round(argDeg)}°)
          </div>
          <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
            {showConjugate
              ? <>the conjugate z̄ is z reflected in the REAL axis — same modulus, opposite argument</>
              : <>|z| is the arrow&apos;s length (Pythagoras); arg z is its angle from the positive real axis</>}
          </div>
        </div>

        <div className="mt-3 flex flex-wrap justify-center gap-x-5 gap-y-2">
          <Stepper label="Re(z)" value={`${a}`} onDec={() => setA(Math.max(-4, a - 1))} onInc={() => setA(Math.min(4, a + 1))} />
          <Stepper label="Im(z)" value={`${b}`} onDec={() => setB(Math.max(-4, b - 1))} onInc={() => setB(Math.min(4, b + 1))} />
        </div>
      </div>
    );
  }

  // ======================================================== powers mode
  if (mode === "powers") {
    const th = (thetaDeg * Math.PI) / 180;
    const unit = 44;
    const pts = Array.from({ length: nPow }, (_, i) => {
      const k = i + 1;
      const m = Math.pow(rBase, k);
      return { k, m, x: cx + m * unit * Math.cos(k * th), y: cy - m * unit * Math.sin(k * th) };
    });
    const modN = Math.pow(rBase, nPow);
    const argNdeg = nPow * thetaDeg;

    return (
      <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }} role="img" aria-label="Powers of a complex number spiralling on the Argand diagram">
          <line x1={10} y1={cy} x2={W - 10} y2={cy} stroke="var(--fg-2)" strokeWidth={1.2} />
          <line x1={cx} y1={10} x2={cx} y2={H - 10} stroke="var(--fg-2)" strokeWidth={1.2} />
          {/* unit circle for reference */}
          <circle cx={cx} cy={cy} r={unit} fill="none" stroke="var(--fg-3)" strokeWidth={1} strokeDasharray="4 4" opacity={0.7} />
          <text x={cx + unit + 4} y={cy + 12} fontSize="9" fill="var(--fg-3)">|z| = 1</text>

          {/* chained spokes */}
          {pts.map((p, i) => {
            const prev = i === 0 ? { x: cx, y: cy } : pts[i - 1];
            return <line key={p.k} x1={prev.x} y1={prev.y} x2={p.x} y2={p.y} stroke={GEO_BLUE} strokeWidth={1.4} opacity={0.55} />;
          })}
          {pts.map((p) => (
            <g key={p.k}>
              <line x1={cx} y1={cy} x2={p.x} y2={p.y} stroke={p.k === nPow ? GEO_ACCENT : "var(--fg-3)"} strokeWidth={p.k === nPow ? 2.4 : 1} opacity={p.k === nPow ? 1 : 0.5} />
              <circle cx={p.x} cy={p.y} r={p.k === nPow ? 5.4 : 3.6} fill={p.k === nPow ? GEO_ACCENT : GEO_BLUE} stroke="var(--bg-1)" strokeWidth={1.2} />
              {(p.k === 1 || p.k === nPow) && (
                <text x={p.x + 8} y={p.y - 6} fontSize="11" fontWeight={700} fill="var(--fg)">
                  z{p.k > 1 ? <tspan dy={-4} fontSize="8.5">{p.k}</tspan> : null}
                </text>
              )}
            </g>
          ))}
        </svg>

        <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            |z| = <b>{fmt2(rBase)}</b>, arg z = <b>{thetaDeg}°</b> → |z<sup style={{ fontSize: 11 }}>{nPow}</sup>| = <b style={{ color: GEO_ACCENT }}>{fmt2(modN)}</b>, arg = <b style={{ color: GEO_ACCENT }}>{argNdeg}°</b>
          </div>
          <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
            {rBase > 1 ? "spiralling OUT — each power stretches by |z| and turns by arg z" : rBase < 1 ? "spiralling IN — moduli shrink, arguments still add" : "walking the unit circle — modulus stays 1, only the argument grows"}
          </div>
        </div>

        <div className="mt-3 flex flex-wrap justify-center gap-x-5 gap-y-2">
          <Stepper label="n" value={`${nPow}`} onDec={() => setNPow(Math.max(1, nPow - 1))} onInc={() => setNPow(Math.min(8, nPow + 1))} />
          <Stepper
            label="|z|"
            value={fmt2(rBase)}
            onDec={() => setRIdx(Math.max(0, (rIdx < 0 ? R_CHOICES.findIndex((v) => Math.abs(v - r0) < 1e-9) : rIdx) - 1))}
            onInc={() => setRIdx(Math.min(R_CHOICES.length - 1, (rIdx < 0 ? R_CHOICES.findIndex((v) => Math.abs(v - r0) < 1e-9) : rIdx) + 1))}
          />
        </div>
      </div>
    );
  }

  // ======================================================== roots mode
  const R = 108;
  const roots = Array.from({ length: nRoots }, (_, k) => {
    const ang = ((phiD / nRoots + (360 * k) / nRoots) * Math.PI) / 180;
    return { k, x: cx + R * Math.cos(ang), y: cy - R * Math.sin(ang) };
  });
  const poly = roots.map((p) => `${p.x},${p.y}`).join(" ");
  const tx = cx + R * Math.cos((phiD * Math.PI) / 180);
  const ty = cy - R * Math.sin((phiD * Math.PI) / 180);

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }} role="img" aria-label="The nth roots of a complex number forming a regular polygon on a circle">
        <line x1={10} y1={cy} x2={W - 10} y2={cy} stroke="var(--fg-2)" strokeWidth={1.2} />
        <line x1={cx} y1={10} x2={cx} y2={H - 10} stroke="var(--fg-2)" strokeWidth={1.2} />
        <circle cx={cx} cy={cy} r={R} fill="none" stroke="var(--fg-2)" strokeWidth={1.5} />

        {/* target w, marked hollow on the circle */}
        <circle cx={tx} cy={ty} r={7.5} fill="none" stroke={RED} strokeWidth={2} />
        <text x={tx + (Math.cos((phiD * Math.PI) / 180) >= 0 ? 12 : -12)} y={ty + 4} fontSize="11.5" fontWeight={700} fill={RED} textAnchor={Math.cos((phiD * Math.PI) / 180) >= 0 ? "start" : "end"}>w</text>

        {/* the regular n-gon of roots */}
        <polygon points={poly} fill={GEO_BLUE} fillOpacity={0.08} stroke={GEO_BLUE} strokeWidth={1.4} />
        {roots.map((p) => (
          <g key={p.k}>
            <line x1={cx} y1={cy} x2={p.x} y2={p.y} stroke="var(--fg-3)" strokeWidth={1} opacity={0.5} />
            <circle cx={p.x} cy={p.y} r={4.8} fill={p.k === 0 ? GEO_ACCENT : GEO_BLUE} stroke="var(--bg-1)" strokeWidth={1.3} />
          </g>
        ))}
      </svg>

      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
          z<sup style={{ fontSize: 11 }}>n</sup> = w, arg w = <b style={{ color: RED }}>{phi}°</b> → <b style={{ color: GEO_BLUE }}>{nRoots} roots</b>, spaced <b>{Math.round(3600 / nRoots) / 10}°</b> apart
        </div>
        <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
          first root at {fmt2(phi / nRoots)}° (arg w ÷ n), the rest every 360°/n — a regular {nRoots}-gon, always
        </div>
      </div>

      <div className="mt-3 flex flex-wrap justify-center gap-x-5 gap-y-2">
        <Stepper label="n" value={`${nRoots}`} onDec={() => setNRoots(Math.max(3, nRoots - 1))} onInc={() => setNRoots(Math.min(8, nRoots + 1))} />
        <Stepper label="arg w" value={`${phi}°`} onDec={() => setPhi(Math.max(-180, phi - 45))} onInc={() => setPhi(Math.min(315, phi + 45))} />
      </div>
    </div>
  );
}
