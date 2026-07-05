"use client";

import { useEffect, useMemo, useState } from "react";
import { Minus, Plus, RotateCcw } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type LimitGraphConfig } from "@/lib/genmath-interactive";

// The limits workbench — four modes:
//  approach: f(x) = x²/2 with a δ-stepper. Two dots pin x = 2 ± δ; shrink δ
//            and watch both outputs squeeze toward L = 2. The limit as a
//            two-sided ambush.
//  hole:     f(x) = (x² − 4)/(x − 2) — the line y = x + 2 wearing an open
//            circle at x = 2. Same squeeze, but the target value ISN'T there:
//            the limit exists, f(2) doesn't. Limits don't care about the hole.
//  jump:     a piecewise step: x + 1 left of 1, 4 − x from 1 on. The left dot
//            reports 2, the right dot reports 3 — the sides disagree, so the
//            two-sided limit does not exist.
//  infinite: f(x) = 1/(x − 2)², auto-played: dots ride the curve toward the
//            dashed asymptote while the outputs blow past every bound.

const RED = "rgb(200,60,60)";

function fmt(n: number, dp = 2): string {
  return (Math.round(n * 10 ** dp) / 10 ** dp).toString();
}

const DELTAS = [1, 0.5, 0.25, 0.1];

export default function LimitGraph({ config }: { config: LimitGraphConfig }) {
  const { mode } = config;

  // δ stepper (approach / hole / jump)
  const [di, setDi] = useState(0);
  const delta = useAnimatedValue(DELTAS[di], { stiffness: 120, damping: 18 });

  // infinite mode auto-play
  const [go, setGo] = useState(false);
  useEffect(() => {
    if (mode !== "infinite") return;
    const t = setTimeout(() => setGo(true), 700);
    return () => clearTimeout(t);
  }, [mode]);
  const t = useAnimatedValue(go ? 1 : 0, { stiffness: 7, damping: 7 });
  const replay = () => {
    setGo(false);
    setTimeout(() => setGo(true), 380);
  };

  // grid geometry
  const W = 320;
  const H = 300;
  const padL = 30, padR = 14, padT = 14, padB = 26;
  const X0 = -1, X1 = mode === "infinite" ? 5 : 4;
  const Y0 = -1, Y1 = mode === "infinite" ? 8 : 7;
  const px = (x: number) => padL + ((x - X0) / (X1 - X0)) * (W - padL - padR);
  const py = (y: number) => (H - padB) - ((y - Y0) / (Y1 - Y0)) * (H - padB - padT);

  // the anchor point a and the mode's function(s)
  const a = mode === "jump" ? 1 : 2;
  const fAt = (x: number): number => {
    if (mode === "approach") return (x * x) / 2;
    if (mode === "hole") return x + 2;
    if (mode === "jump") return x < a ? x + 1 : 4 - x;
    return 1 / ((x - 2) * (x - 2)); // infinite
  };

  // dot positions
  const dNow = mode === "infinite" ? 1.5 * Math.pow(0.06 / 1.5, Math.max(0, Math.min(1, t))) : delta;
  const xL = a - dNow;
  const xR = a + dNow;
  const yL = mode === "jump" ? xL + 1 : fAt(xL);
  const yR = fAt(xR);

  const curvePaths = useMemo(() => {
    const seg = (from: number, to: number, f: (x: number) => number) => {
      let d = "";
      let pen = false;
      for (let x = from; x <= to + 1e-9; x += 0.04) {
        const y = f(x);
        if (y < Y0 - 2 || y > Y1 + 2) { pen = false; continue; }
        d += `${pen ? "L" : "M"} ${px(x)} ${py(Math.max(Y0 - 2, Math.min(Y1 + 2, y)))} `;
        pen = true;
      }
      return d.trim();
    };
    if (mode === "jump") return [seg(X0, a - 0.001, (x) => x + 1), seg(a, X1, (x) => 4 - x)];
    if (mode === "infinite") return [seg(X0, 1.99, fAt), seg(2.01, X1, fAt)];
    return [seg(X0, X1, fAt)];
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [mode]);

  const L = mode === "approach" ? 2 : mode === "hole" ? 4 : null;

  const eqnText =
    mode === "approach" ? "f(x) = x²/2, x → 2" :
    mode === "hole" ? "f(x) = (x² − 4)/(x − 2), x → 2" :
    mode === "jump" ? "f(x) = x + 1 (x < 1);  4 − x (x ≥ 1)" :
    "f(x) = 1/(x − 2)², x → 2";

  const stepBtn = (dir: -1 | 1) => {
    const next = di + dir;
    return (
      <button
        type="button"
        onClick={() => setDi(Math.max(0, Math.min(DELTAS.length - 1, next)))}
        disabled={next < 0 || next > DELTAS.length - 1}
        aria-label={dir === 1 ? "Shrink delta" : "Grow delta"}
        className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35"
        style={dir === 1
          ? { background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }
          : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
      >
        {dir === 1 ? <Minus className="h-4 w-4" /> : <Plus className="h-4 w-4" />}
      </button>
    );
  };

  const bigY = yR > Y1;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340 }} role="img" aria-label="A function graph with points approaching a target x-value">
          {Array.from({ length: X1 - X0 + 1 }, (_, i) => X0 + i).map((g) => (
            <line key={`v${g}`} x1={px(g)} y1={py(Y0)} x2={px(g)} y2={py(Y1)} stroke="var(--line)" strokeWidth={1} />
          ))}
          {Array.from({ length: Y1 - Y0 + 1 }, (_, i) => Y0 + i).map((g) => (
            <line key={`h${g}`} x1={px(X0)} y1={py(g)} x2={px(X1)} y2={py(g)} stroke="var(--line)" strokeWidth={1} />
          ))}
          <line x1={px(X0)} y1={py(0)} x2={px(X1)} y2={py(0)} stroke="var(--fg-2)" strokeWidth={1.8} />
          <line x1={px(0)} y1={py(Y0)} x2={px(0)} y2={py(Y1)} stroke="var(--fg-2)" strokeWidth={1.8} />
          {[1, 2, 3, ...(mode === "infinite" ? [4] : [])].map((g) => (
            <text key={g} x={px(g)} y={py(0) + 13} fontSize="9" fill="var(--fg-3)" textAnchor="middle">{g}</text>
          ))}
          {[2, 4, 6].map((g) => (
            <text key={g} x={px(0) - 5} y={py(g) + 3} fontSize="9" fill="var(--fg-3)" textAnchor="end">{g}</text>
          ))}

          {/* vertical asymptote (infinite) */}
          {mode === "infinite" && (
            <line x1={px(2)} y1={py(Y0)} x2={px(2)} y2={py(Y1)} stroke={RED} strokeWidth={1.5} strokeDasharray="5 4" opacity={0.7} />
          )}

          {/* the curve */}
          {curvePaths.map((d, i) => (
            <path key={`${mode}-${i}`} d={d} fill="none" stroke={GEO_ACCENT} strokeWidth={2.8} strokeLinecap="round" pathLength={1} className="gm-arc-sweep" />
          ))}

          {/* target guides */}
          {L !== null && (
            <g>
              <line x1={px(a)} y1={py(0)} x2={px(a)} y2={py(L)} stroke="var(--fg-3)" strokeWidth={1} strokeDasharray="3 3" />
              <line x1={px(0)} y1={py(L)} x2={px(a)} y2={py(L)} stroke="var(--fg-3)" strokeWidth={1} strokeDasharray="3 3" />
              <circle cx={px(a)} cy={py(L)} r={9} fill="none" stroke={GEO_BLUE} strokeWidth={1.3} opacity={0.5} className="gm-beacon" />
            </g>
          )}

          {/* hole: open circle */}
          {mode === "hole" && (
            <circle cx={px(2)} cy={py(4)} r={4.5} fill="var(--bg-1)" stroke={GEO_ACCENT} strokeWidth={2.2} />
          )}

          {/* jump: open + filled endpoints */}
          {mode === "jump" && (
            <g>
              <circle cx={px(1)} cy={py(2)} r={4.5} fill="var(--bg-1)" stroke={GEO_ACCENT} strokeWidth={2.2} />
              <circle cx={px(1)} cy={py(3)} r={4.5} fill={GEO_ACCENT} />
            </g>
          )}

          {/* the two approaching dots (clamped to the frame; fade once they exit) */}
          <circle cx={px(xR)} cy={py(Math.min(yR, Y1))} r={5} fill={GEO_ACCENT} stroke="var(--bg-1)" strokeWidth={1.5} opacity={bigY ? 0.3 : 1} />
          <circle cx={px(xL)} cy={py(Math.min(mode === "infinite" ? fAt(xL) : yL, Y1))} r={5} fill={GEO_BLUE} stroke="var(--bg-1)" strokeWidth={1.5} opacity={(mode === "infinite" ? fAt(xL) : yL) > Y1 ? 0.3 : 1} />
        </svg>
      </div>

      <div className="mt-2 flex justify-center text-[14px]">
        <span className="serif tabular" style={{ color: GEO_ACCENT }}>{eqnText}</span>
      </div>

      {/* readouts */}
      <div className="mt-2 grid grid-cols-2 gap-2">
        <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
          <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_BLUE }}>from the left</div>
          <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>
            f({fmt(xL)}) = {mode === "infinite" ? fmt(fAt(xL), 1) : fmt(yL, 3)}
          </div>
        </div>
        <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
          <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_ACCENT }}>from the right</div>
          <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>
            f({fmt(xR)}) = {mode === "infinite" ? fmt(yR, 1) : fmt(yR, 3)}
          </div>
        </div>
      </div>

      {/* verdict */}
      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {mode === "approach" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              Both sides squeeze toward <b style={{ color: GEO_BLUE }}>2</b> — so lim f(x) = 2
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              the limit is where the squeeze POINTS, whether or not the point is ever reached
            </div>
          </>
        )}
        {mode === "hole" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              The squeeze points at <b style={{ color: GEO_BLUE }}>4</b> — but f(2) is <b style={{ color: RED }}>undefined</b>
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              limit = 4 anyway: limits read the approach, not the arrival
            </div>
          </>
        )}
        {mode === "jump" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              Left says <b style={{ color: GEO_BLUE }}>2</b>, right says <b style={{ color: GEO_ACCENT }}>3</b> — <b style={{ color: RED }}>no two-sided limit</b>
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              a limit exists only when both one-sided limits agree
            </div>
          </>
        )}
        {mode === "infinite" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              Outputs pass every bound — <b style={{ color: RED }}>no finite limit</b> (we write → ∞)
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              the dashed line is a vertical asymptote: the curve climbs it forever
            </div>
          </>
        )}
      </div>

      {/* controls */}
      <div className="mt-4 flex items-center justify-center gap-4">
        {mode !== "infinite" ? (
          <div className="text-center">
            <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>distance δ from {a}</div>
            <div className="mt-1 flex items-center gap-2">
              {stepBtn(-1)}
              <div className="serif tabular text-center" style={{ minWidth: 44, fontSize: 16, color: GEO_BLUE }}>{DELTAS[di]}</div>
              {stepBtn(1)}
            </div>
          </div>
        ) : (
          <button type="button" onClick={replay} aria-label="Replay the approach" className="gm-press flex items-center gap-2 rounded-full px-5 py-2 text-[13px]" style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}>
            <RotateCcw className="h-3.5 w-3.5" /> replay the approach
          </button>
        )}
      </div>
      <div className="mt-2 text-center text-[12px]" style={{ color: "var(--fg-3)" }}>
        {mode === "approach" && "shrink δ — the two outputs close in on the limit"}
        {mode === "hole" && "shrink δ — the squeeze works even though the target is missing"}
        {mode === "jump" && "shrink δ — the two sides refuse to meet"}
        {mode === "infinite" && "the dots ride the curve into the asymptote — outputs explode"}
      </div>
    </div>
  );
}
