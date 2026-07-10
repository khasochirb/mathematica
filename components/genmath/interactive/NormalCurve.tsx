"use client";

import { useMemo, useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { normalPdf, type NormalCurveConfig } from "@/lib/genmath-interactive";

// The bell curve, two ways:
//   empirical — chips shade the 1σ / 2σ / 3σ bands with their 68–95–99.7
//               shares, with real axis values at every tick.
//   zscore    — a stepper walks x along the axis; the readout converts the
//               walk into z = (x − μ)/σ, distance measured in sigmas.

const BAND_PCT: Record<number, string> = { 1: "68%", 2: "95%", 3: "99.7%" };

function fmt(n: number): string {
  const r = Math.round(n * 100) / 100;
  return Number.isInteger(r) ? r.toString() : r.toString();
}

export default function NormalCurve({ config }: { config: NormalCurveConfig }) {
  const { mode, mu, sigma, x0, step = sigma / 2, xLabel = "value" } = config;
  const [band, setBand] = useState<number>(mode === "empirical" ? 1 : 0);
  const [x, setX] = useState(x0 ?? mu + sigma);

  const W = 380;
  const H = 200;
  const padL = 14;
  const padR = 14;
  const axisY = H - 40;
  const span = 3.6; // sigmas each side
  const px = (v: number) => padL + ((v - (mu - span * sigma)) / (2 * span * sigma)) * (W - padL - padR);
  const peak = normalPdf(mu, mu, sigma);
  const py = (v: number) => axisY - (normalPdf(v, mu, sigma) / peak) * (axisY - 30);

  const curve = useMemo(() => {
    const pts: string[] = [];
    for (let i = 0; i <= 96; i++) {
      const v = mu - span * sigma + (i / 96) * 2 * span * sigma;
      pts.push(`${i === 0 ? "M" : "L"}${px(v).toFixed(1)},${py(v).toFixed(1)}`);
    }
    return pts.join(" ");
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [mu, sigma]);

  const areaPath = (a: number, b: number) => {
    const pts: string[] = [`M${px(a).toFixed(1)},${axisY}`];
    for (let i = 0; i <= 48; i++) {
      const v = a + (i / 48) * (b - a);
      pts.push(`L${px(v).toFixed(1)},${py(v).toFixed(1)}`);
    }
    pts.push(`L${px(b).toFixed(1)},${axisY} Z`);
    return pts.join(" ");
  };

  const xA = useAnimatedValue(x, { stiffness: 120, damping: 18 });
  const z = (x - mu) / sigma;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 420 }} role="img" aria-label="Normal curve">
          {/* shaded band / walk */}
          {mode === "empirical" && band > 0 && (
            <path d={areaPath(mu - band * sigma, mu + band * sigma)} fill="var(--accent)" fillOpacity={0.22} className="gm-pop" key={band} />
          )}
          {mode === "zscore" && (
            <path d={areaPath(Math.min(mu, x), Math.max(mu, x))} fill="var(--accent)" fillOpacity={0.18} />
          )}

          {/* the curve */}
          <path d={curve} fill="none" stroke={GEO_BLUE} strokeWidth={2.2} />

          {/* axis + sigma ticks */}
          <line x1={padL} y1={axisY} x2={W - padR} y2={axisY} stroke="var(--fg-2)" strokeWidth={1.6} />
          {[-3, -2, -1, 0, 1, 2, 3].map((k) => (
            <g key={k}>
              <line x1={px(mu + k * sigma)} y1={axisY} x2={px(mu + k * sigma)} y2={axisY + 4} stroke="var(--fg-2)" strokeWidth={1.2} />
              <text x={px(mu + k * sigma)} y={axisY + 15} fontSize="8.5" fill="var(--fg-3)" textAnchor="middle" className="tabular">
                {fmt(mu + k * sigma)}
              </text>
              <text x={px(mu + k * sigma)} y={axisY + 27} fontSize="8" fill="var(--fg-3)" textAnchor="middle" className="tabular">
                {k === 0 ? "μ" : `${k > 0 ? "+" : ""}${k}σ`}
              </text>
            </g>
          ))}

          {/* centre line */}
          <line x1={px(mu)} y1={py(mu)} x2={px(mu)} y2={axisY} stroke="var(--fg-2)" strokeWidth={1.2} strokeDasharray="3 3" />

          {/* band edges / x marker */}
          {mode === "empirical" && band > 0 && (
            <g>
              {[mu - band * sigma, mu + band * sigma].map((v, i) => (
                <line key={i} x1={px(v)} y1={py(v)} x2={px(v)} y2={axisY} stroke="var(--accent)" strokeWidth={1.6} />
              ))}
              <text x={px(mu)} y={Math.max(42, py(mu + band * sigma * 0.5) - 8)} fontSize="13" fill="var(--accent)" textAnchor="middle" fontWeight={700}>
                {BAND_PCT[band]}
              </text>
            </g>
          )}
          {mode === "zscore" && (
            <g>
              <line x1={px(xA)} y1={py(xA)} x2={px(xA)} y2={axisY} stroke="var(--accent)" strokeWidth={2} />
              <circle cx={px(xA)} cy={axisY} r={5} fill="var(--accent)" stroke="var(--bg-1)" strokeWidth={1.2} />
            </g>
          )}

          <text x={W - padR} y={H - 4} fontSize="10" fill="var(--fg-2)" textAnchor="end">
            {xLabel}
          </text>
        </svg>
      </div>

      {/* readout */}
      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {mode === "empirical" ? (
          band > 0 ? (
            <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
              within {band}σ of the mean: {fmt(mu - band * sigma)} to {fmt(mu + band * sigma)} — about{" "}
              <b style={{ color: "var(--accent)" }}>{BAND_PCT[band]}</b> of all values
            </div>
          ) : (
            <div className="text-[13px]" style={{ color: "var(--fg-2)" }}>
              μ = {fmt(mu)}, σ = {fmt(sigma)} — pick a band
            </div>
          )
        ) : (
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            z = ({fmt(x)} − {fmt(mu)}) / {fmt(sigma)} = <b style={{ color: "var(--accent)" }}>{fmt(Math.round(z * 100) / 100)}</b>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              {z === 0 ? "dead on the mean" : `${fmt(Math.abs(Math.round(z * 100) / 100))} σ ${z > 0 ? "above" : "below"} the mean`}
            </div>
          </div>
        )}
      </div>

      {/* controls */}
      {mode === "empirical" ? (
        <div className="mt-3 flex justify-center gap-1.5">
          {[1, 2, 3].map((k) => (
            <button
              key={k}
              type="button"
              onClick={() => setBand(band === k ? 0 : k)}
              className="gm-press rounded-full px-4 py-1.5 text-[12px] tabular"
              style={
                band === k
                  ? { background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }
                  : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }
              }
            >
              ±{k}σ
            </button>
          ))}
        </div>
      ) : (
        <div className="mt-3 flex items-center justify-center gap-2">
          <button
            type="button"
            onClick={() => setX((v) => Math.max(mu - 3 * sigma, Math.round((v - step) * 100) / 100))}
            disabled={x <= mu - 3 * sigma}
            aria-label="Move x left"
            className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
          >
            <Minus className="h-4 w-4" />
          </button>
          <div className="text-[12px]" style={{ color: "var(--fg-2)", minWidth: 90, textAlign: "center" }}>
            x = <b className="tabular" style={{ color: "var(--accent)" }}>{fmt(x)}</b>
          </div>
          <button
            type="button"
            onClick={() => setX((v) => Math.min(mu + 3 * sigma, Math.round((v + step) * 100) / 100))}
            disabled={x >= mu + 3 * sigma}
            aria-label="Move x right"
            className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35"
            style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
          >
            <Plus className="h-4 w-4" />
          </button>
        </div>
      )}
    </div>
  );
}
