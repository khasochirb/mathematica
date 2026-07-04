"use client";

import { useEffect, useMemo, useState } from "react";
import { Minus, Plus, RotateCcw } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type ExpGraphConfig } from "@/lib/genmath-interactive";

// The exponential workbench — three modes, all animated:
//  growth:   y = a·bˣ with steppers on a and b (b hops over 1). The curve
//            springs between shapes; dots at x = 0,1,2,3 wear ×b ratio chips —
//            the "same multiplier every step" signature made visible.
//  race:     y = bˣ vs a line y = mx, swept left to right by an auto-playing
//            marker pair. The line leads early; the exponential passes it and
//            never looks back. Crossing point marked. Replay button.
//  compound: a bank balance P growing at rate r per year, drawn as bars that
//            fill in year by year (auto-play). Live A = P(1+r)^t readout.

const RED = "rgb(200,60,60)";

function fmt(n: number): string {
  const r = Math.round(n * 100) / 100;
  return r.toString();
}

export default function ExpGraph({ config }: { config: ExpGraphConfig }) {
  const {
    mode,
    a: a0 = 1,
    b: b0 = 2,
    m = 8,
    p: principal = 100,
    r: rate = 0.1,
    years = 8,
    interactive = true,
  } = config;

  // ---- growth-mode state ----
  const B_STEPS = [0.25, 0.5, 0.75, 1.25, 1.5, 2, 2.5, 3];
  const [a, setA] = useState(a0);
  const [bi, setBi] = useState(Math.max(0, B_STEPS.indexOf(b0) !== -1 ? B_STEPS.indexOf(b0) : 5));
  const b = B_STEPS[bi];
  const ad = useAnimatedValue(a, { stiffness: 120, damping: 18 });
  const bd = useAnimatedValue(b, { stiffness: 120, damping: 18, from: 1 });

  // ---- auto-play (race + compound) ----
  const [go, setGo] = useState(false);
  useEffect(() => {
    if (mode === "growth") return;
    const id = setTimeout(() => setGo(true), 700);
    return () => clearTimeout(id);
  }, [mode]);
  const sweep = useAnimatedValue(go ? 1 : 0, { stiffness: 8, damping: 6.5 });
  const sp = Math.max(0, Math.min(1, sweep));
  const replay = () => {
    setGo(false);
    setTimeout(() => setGo(true), 380);
  };

  // ======================================================== growth mode
  if (mode === "growth") {
    const W = 320;
    const H = 300;
    const padL = 30, padR = 14, padT = 14, padB = 26;
    const X0 = -4, X1 = 4, Y0 = 0, Y1 = 9;
    const px = (x: number) => padL + ((x - X0) / (X1 - X0)) * (W - padL - padR);
    const py = (y: number) => (H - padB) - ((y - Y0) / (Y1 - Y0)) * (H - padB - padT);
    const path = (() => {
      const pts: string[] = [];
      for (let x = X0; x <= X1 + 1e-9; x += 0.1) {
        const y = ad * Math.pow(bd, x);
        if (y > Y1 + 2) continue;
        pts.push(`${px(x)},${py(Math.min(Y1 + 2, y))}`);
      }
      return pts.length > 1 ? `M ${pts.join(" L ")}` : "";
    })();
    const dots = [0, 1, 2, 3].map((x) => ({ x, y: a * Math.pow(b, x), yd: ad * Math.pow(bd, x) }));
    const growth = b > 1;

    return (
      <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }} role="img" aria-label="An exponential curve on a grid">
          {/* grid */}
          {Array.from({ length: Y1 + 1 }, (_, i) => i).map((g) => (
            <line key={`h${g}`} x1={px(X0)} y1={py(g)} x2={px(X1)} y2={py(g)} stroke="var(--line)" strokeWidth={1} />
          ))}
          {Array.from({ length: X1 - X0 + 1 }, (_, i) => X0 + i).map((g) => (
            <line key={`v${g}`} x1={px(g)} y1={py(Y0)} x2={px(g)} y2={py(Y1)} stroke="var(--line)" strokeWidth={1} />
          ))}
          <line x1={px(X0)} y1={py(0)} x2={px(X1)} y2={py(0)} stroke="var(--fg-2)" strokeWidth={1.8} />
          <line x1={px(0)} y1={py(Y0)} x2={px(0)} y2={py(Y1)} stroke="var(--fg-2)" strokeWidth={1.8} />
          {[-4, -2, 2, 4].map((g) => (
            <text key={g} x={px(g)} y={py(0) + 13} fontSize="9" fill="var(--fg-3)" textAnchor="middle">{g}</text>
          ))}
          {[2, 4, 6, 8].map((g) => (
            <text key={g} x={px(0) - 5} y={py(g) + 3} fontSize="9" fill="var(--fg-3)" textAnchor="end">{g}</text>
          ))}

          {/* the curve */}
          {path && <path d={path} fill="none" stroke={GEO_ACCENT} strokeWidth={2.8} strokeLinecap="round" pathLength={1} className="gm-arc-sweep" />}

          {/* asymptote hint: the curve hugs y = 0 on one side */}
          <text x={px(growth ? X0 : X1) + (growth ? 4 : -4)} y={py(0) - 6} fontSize="9" fill="var(--fg-3)" textAnchor={growth ? "start" : "end"}>hugs y = 0</text>

          {/* integer-step dots + ×b chips */}
          {dots.map((d, i) =>
            d.yd <= Y1 + 0.5 ? (
              <g key={d.x}>
                <circle cx={px(d.x)} cy={py(Math.min(Y1, d.yd))} r={4.2} fill={i === 0 ? "var(--fg)" : GEO_BLUE} className="gm-pop" style={{ animationDelay: `${0.3 + i * 0.12}s` }} />
                {i > 0 && dots[i - 1].yd <= Y1 && (
                  <text x={(px(d.x) + px(d.x - 1)) / 2} y={py((Math.min(Y1, d.yd) + Math.min(Y1, dots[i - 1].yd)) / 2) - 7} fontSize="10" fontWeight={700} fill={GEO_BLUE} textAnchor="middle" className="gm-fade" style={{ animationDelay: `${0.4 + i * 0.12}s` }}>
                    ×{fmt(b)}
                  </text>
                )}
              </g>
            ) : null
          )}
          {/* y-intercept label */}
          <text x={px(0) + 7} y={py(Math.min(Y1, ad)) - 8} fontSize="11" fontWeight={700} fill="var(--fg)">(0, {fmt(a)})</text>
        </svg>

        <div className="mt-2 flex justify-center text-[14px]">
          <span className="serif tabular" style={{ color: GEO_ACCENT }}>y = {a === 1 ? "" : `${fmt(a)} · `}{fmt(b)}ˣ</span>
        </div>

        <div className="mt-2 rounded-xl p-3 text-center" style={{ transition: "background 0.35s ease, border-color 0.35s ease", background: growth ? "var(--bg-2)" : "rgba(200,60,60,0.06)", border: `1px solid ${growth ? "var(--line)" : RED}` }}>
          <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
            {growth
              ? <><b style={{ color: GEO_ACCENT }}>Growth</b> — every step right multiplies by <b style={{ color: GEO_BLUE }}>{fmt(b)}</b></>
              : <><b style={{ color: RED }}>Decay</b> — every step right multiplies by <b style={{ color: GEO_BLUE }}>{fmt(b)}</b> (shrinks)</>}
          </div>
          <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
            starts at (0, {fmt(a)}) — that&apos;s a · same multiplier every step: the exponential signature
          </div>
        </div>

        {interactive && (
          <div className="mt-4 flex items-center justify-center gap-6">
            <div className="text-center">
              <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>start a</div>
              <div className="mt-1 flex items-center gap-2">
                <button type="button" onClick={() => setA((v) => Math.max(1, v - 1))} disabled={a <= 1} aria-label="Decrease start a" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
                <div className="serif tabular text-center" style={{ minWidth: 36, fontSize: 16, color: GEO_BLUE }}>{fmt(a)}</div>
                <button type="button" onClick={() => setA((v) => Math.min(4, v + 1))} disabled={a >= 4} aria-label="Increase start a" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
              </div>
            </div>
            <div className="text-center">
              <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>base b</div>
              <div className="mt-1 flex items-center gap-2">
                <button type="button" onClick={() => setBi((v) => Math.max(0, v - 1))} disabled={bi <= 0} aria-label="Decrease base b" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
                <div className="serif tabular text-center" style={{ minWidth: 40, fontSize: 16, color: GEO_ACCENT }}>{fmt(b)}</div>
                <button type="button" onClick={() => setBi((v) => Math.min(B_STEPS.length - 1, v + 1))} disabled={bi >= B_STEPS.length - 1} aria-label="Increase base b" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
              </div>
            </div>
          </div>
        )}
        {interactive && (
          <div className="mt-2 text-center text-[12px]" style={{ color: "var(--fg-3)" }}>
            step the base through 1 — watch growth flip into decay (b never equals 1: that&apos;s a flat line)
          </div>
        )}
      </div>
    );
  }

  // ======================================================== race mode
  if (mode === "race") {
    const W = 320;
    const H = 250;
    const padL = 34, padR = 12, padT = 16, padB = 26;
    const X1 = 7;
    const Y1 = 80;
    const px = (x: number) => padL + (x / X1) * (W - padL - padR);
    const py = (y: number) => (H - padB) - (Math.min(y, Y1) / Y1) * (H - padB - padT);
    const expAt = (x: number) => Math.pow(b0, x);
    const lineAt = (x: number) => m * x;
    // crossing (beyond the early tangle): bisect on [2, X1]
    const cross = (() => {
      let lo = 2, hi = X1;
      if (expAt(hi) < lineAt(hi)) return null;
      for (let i = 0; i < 40; i++) {
        const mid = (lo + hi) / 2;
        if (expAt(mid) < lineAt(mid)) lo = mid; else hi = mid;
      }
      return (lo + hi) / 2;
    })();
    const xNow = X1 * sp;
    const trail = (f: (x: number) => number) => {
      const pts: string[] = [];
      for (let x = 0; x <= xNow + 1e-9; x += X1 / 120) {
        if (f(x) > Y1 + 6) break;
        pts.push(`${px(x)},${py(f(x))}`);
      }
      return pts.length > 1 ? `M ${pts.join(" L ")}` : "";
    };
    const expLeads = expAt(xNow) > lineAt(xNow);
    const passed = cross !== null && xNow >= cross;

    return (
      <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 360, display: "block", margin: "0 auto" }} role="img" aria-label="An exponential racing a straight line">
          <line x1={padL} y1={H - padB} x2={W - 8} y2={H - padB} stroke="var(--fg-2)" strokeWidth={1.6} />
          <line x1={padL} y1={H - padB} x2={padL} y2={10} stroke="var(--fg-2)" strokeWidth={1.6} />
          {Array.from({ length: X1 + 1 }, (_, i) => i).map((t) => (
            <text key={t} x={px(t)} y={H - padB + 13} fontSize="9" fill="var(--fg-3)" textAnchor="middle">{t}</text>
          ))}
          {[20, 40, 60, 80].map((g) => (
            <g key={g}>
              <line x1={padL} y1={py(g)} x2={W - 8} y2={py(g)} stroke="var(--line)" strokeWidth={1} />
              <text x={padL - 5} y={py(g) + 3} fontSize="9" fill="var(--fg-3)" textAnchor="end">{g}</text>
            </g>
          ))}

          {/* full course, faint */}
          <path d={(() => { const pts: string[] = []; for (let x = 0; x <= X1; x += X1 / 120) { if (lineAt(x) > Y1) break; pts.push(`${px(x)},${py(lineAt(x))}`); } return `M ${pts.join(" L ")}`; })()} fill="none" stroke="var(--line)" strokeWidth={1.4} strokeDasharray="3 5" />
          <path d={(() => { const pts: string[] = []; for (let x = 0; x <= X1; x += X1 / 120) { if (expAt(x) > Y1 + 6) break; pts.push(`${px(x)},${py(expAt(x))}`); } return `M ${pts.join(" L ")}`; })()} fill="none" stroke="var(--line)" strokeWidth={1.4} strokeDasharray="3 5" />

          {/* trails */}
          {trail(lineAt) && <path d={trail(lineAt)} fill="none" stroke={GEO_BLUE} strokeWidth={2.6} strokeLinecap="round" />}
          {trail(expAt) && <path d={trail(expAt)} fill="none" stroke={GEO_ACCENT} strokeWidth={2.6} strokeLinecap="round" />}

          {/* crossing marker */}
          {cross !== null && passed && (
            <g className="gm-fade">
              <circle cx={px(cross)} cy={py(expAt(cross))} r={9} fill="none" stroke="var(--fg)" strokeWidth={1.2} opacity={0.4} className="gm-beacon" />
              <text x={px(cross)} y={py(expAt(cross)) - 13} fontSize="10" fontWeight={700} fill="var(--fg)" textAnchor="middle">overtaken</text>
            </g>
          )}

          {/* runners */}
          {lineAt(xNow) <= Y1 && <circle cx={px(xNow)} cy={py(lineAt(xNow))} r={5.5} fill={GEO_BLUE} stroke="var(--bg-1)" strokeWidth={1.4} />}
          {expAt(xNow) <= Y1 + 2 && <circle cx={px(xNow)} cy={py(expAt(xNow))} r={5.5} fill={GEO_ACCENT} stroke="var(--bg-1)" strokeWidth={1.4} />}
        </svg>

        <div className="mt-2 flex justify-center gap-4 text-[13px]">
          <span className="serif tabular" style={{ color: GEO_ACCENT }}>y = {fmt(b0)}ˣ</span>
          <span className="serif tabular" style={{ color: GEO_BLUE }}>y = {fmt(m)}x</span>
        </div>

        <div className="mt-2 rounded-xl p-3 text-center" style={{ transition: "background 0.35s ease", background: passed ? "var(--accent-wash)" : "var(--bg-2)", border: `1px solid ${passed ? "var(--accent-line)" : "var(--line)"}` }}>
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            x = {xNow.toFixed(1)}: line at <b style={{ color: GEO_BLUE }}>{lineAt(xNow).toFixed(0)}</b>, exponential at <b style={{ color: GEO_ACCENT }}>{expAt(xNow).toFixed(1)}</b>
          </div>
          <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
            {sp > 0.97
              ? <>Final: the exponential wins — and the gap only grows from here. Doubling beats adding, always.</>
              : passed
                ? <>Overtaken! Repeated doubling just blew past steady adding — permanently.</>
                : expLeads
                  ? <>Early lead for the exponential… the line will catch it briefly.</>
                  : <>The line leads for now — steady +{fmt(m)} per step. But the doubler is compounding…</>}
          </div>
        </div>

        <div className="mt-3 flex justify-center">
          <button type="button" onClick={replay} aria-label="Race again" className="gm-press flex items-center gap-1.5 rounded-full px-4 py-2 text-[13px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}>
            <RotateCcw className="h-3.5 w-3.5" /> Race again
          </button>
        </div>
      </div>
    );
  }

  // ======================================================== compound mode
  const W = 320;
  const H = 240;
  const padL = 12, padB = 30, padT = 34;
  const n = years;
  const vals = Array.from({ length: n + 1 }, (_, t) => principal * Math.pow(1 + rate, t));
  const maxV = vals[n];
  const bw = (W - padL * 2) / (n + 1);
  const yearNow = Math.min(n, Math.floor(sp * (n + 0.999)));
  const balance = vals[yearNow];

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 360, display: "block", margin: "0 auto" }} role="img" aria-label="A bank balance compounding year by year">
        <line x1={padL} y1={H - padB} x2={W - padL} y2={H - padB} stroke="var(--fg-2)" strokeWidth={1.6} />
        {/* the principal reference line */}
        <line x1={padL} y1={H - padB - ((principal / maxV) * (H - padB - padT))} x2={W - padL} y2={H - padB - ((principal / maxV) * (H - padB - padT))} stroke="var(--line)" strokeWidth={1} strokeDasharray="4 4" />
        {vals.map((v, t) => {
          const h = (v / maxV) * (H - padB - padT);
          const shown = t <= yearNow;
          const isNow = t === yearNow;
          return (
            <g key={t} opacity={shown ? 1 : 0.18} style={{ transition: "opacity 0.3s ease" }}>
              <rect x={padL + t * bw + 3} y={H - padB - h} width={bw - 6} height={h} rx={3}
                fill={isNow ? GEO_ACCENT : "var(--accent-wash)"} stroke={isNow ? GEO_ACCENT : "var(--accent-line)"} strokeWidth={1.2} />
              <text x={padL + t * bw + bw / 2} y={H - padB + 12} fontSize="8.5" fill="var(--fg-3)" textAnchor="middle">{t}</text>
              {shown && (isNow || t === 0) && (
                <text x={padL + t * bw + bw / 2} y={H - padB - h - 5} fontSize="9" fontWeight={700} fill={isNow ? GEO_ACCENT : "var(--fg-2)"} textAnchor="middle">
                  {Math.round(v)}
                </text>
              )}
            </g>
          );
        })}
        <text x={W / 2} y={H - 4} fontSize="9" fill="var(--fg-3)" textAnchor="middle">years</text>
      </svg>

      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
          year {yearNow}: A = {fmt(principal)} · {fmt(1 + rate)}<sup>{yearNow}</sup> = <b style={{ color: GEO_ACCENT }}>{balance.toFixed(2)}</b>
        </div>
        <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
          {sp > 0.97
            ? <>After {n} years: <b style={{ color: GEO_ACCENT }}>{vals[n].toFixed(2)}</b> — vs {fmt(principal * (1 + rate * n))} with simple (non-compounding) interest. The gap is interest earning interest.</>
            : <>Each year multiplies the WHOLE balance by {fmt(1 + rate)} — including all past interest. That&apos;s compounding.</>}
        </div>
      </div>

      <div className="mt-3 flex justify-center">
        <button type="button" onClick={replay} aria-label="Compound again" className="gm-press flex items-center gap-1.5 rounded-full px-4 py-2 text-[13px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}>
          <RotateCcw className="h-3.5 w-3.5" /> Run it again
        </button>
      </div>
    </div>
  );
}
