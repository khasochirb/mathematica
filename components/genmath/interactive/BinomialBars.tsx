"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { binomMean, binomPmf, binomSd, nCr, type BinomialBarsConfig } from "@/lib/genmath-interactive";

// The binomial workbench: steppers on n and p redraw the pmf live. Tap a bar
// to read its C(n,k) p^k q^(n−k) value; the μ = np marker and σ whiskers
// carry the mean-and-shape story — the pile is tallest near np, and skew
// follows p away from ½.

function fmt(x: number, dp = 3): string {
  const r = Math.round(x * 10 ** dp) / 10 ** dp;
  return Number.isInteger(r) ? r.toString() : r.toString();
}

export default function BinomialBars({ config }: { config: BinomialBarsConfig }) {
  const { n0 = 6, p0 = 0.5, nMax = 14, showMuSigma = false, highlightK } = config;
  const [n, setN] = useState(n0);
  const [p, setP] = useState(p0);
  const [pick, setPick] = useState<number | null>(highlightK ?? null);

  const pmf = Array.from({ length: n + 1 }, (_, k) => binomPmf(n, p, k));
  const maxP = Math.max(...pmf);
  const mu = binomMean(n, p);
  const sd = binomSd(n, p);

  const W = 360;
  const H = 200;
  const padL = 18;
  const padR = 18;
  const axisY = H - 38;
  const plotH = axisY - 22;
  const slot = (W - padL - padR) / (n + 1);
  const barW = Math.min(30, slot * 0.72);
  const px = (k: number) => padL + slot * (k + 0.5);
  // μ sits between bar centres: map a real-valued k the same way
  const pxr = (k: number) => padL + slot * (k + 0.5);

  const stepBtn = (dir: -1 | 1, disabled: boolean, onClick: () => void, label: string) => (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      aria-label={label}
      className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35"
      style={
        dir > 0
          ? { background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }
          : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }
      }
    >
      {dir > 0 ? <Plus className="h-4 w-4" /> : <Minus className="h-4 w-4" />}
    </button>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 400 }} role="img" aria-label="Binomial distribution bars">
          <line x1={padL} y1={axisY} x2={W - padR} y2={axisY} stroke="var(--fg-2)" strokeWidth={1.6} />
          {pmf.map((q, k) => {
            const hot = pick === k;
            const h = (q / maxP) * plotH;
            return (
              <g key={`${n}-${p}-${k}`} className="gm-pop" style={{ cursor: "pointer", animationDelay: `${(k * 0.03).toFixed(2)}s` }} onClick={() => setPick(hot ? null : k)}>
                <rect
                  x={px(k) - barW / 2}
                  y={axisY - h}
                  width={barW}
                  height={Math.max(1, h)}
                  rx={3}
                  fill={hot ? "var(--accent)" : GEO_BLUE}
                  fillOpacity={hot ? 0.95 : 0.72}
                  style={{ transition: "fill 0.2s ease" }}
                />
                {n <= 14 && (
                  <text x={px(k)} y={axisY + 13} fontSize="8.5" fill="var(--fg-3)" textAnchor="middle" className="tabular">
                    {k}
                  </text>
                )}
              </g>
            );
          })}
          <text x={W - padR} y={axisY + 26} fontSize="10" fill="var(--fg-2)" textAnchor="end">
            successes k
          </text>

          {showMuSigma && (
            <g>
              <line x1={pxr(mu - sd)} y1={axisY + 22} x2={pxr(mu + sd)} y2={axisY + 22} stroke="var(--accent)" strokeWidth={1.6} />
              {[mu - sd, mu + sd].map((x, i) => (
                <line key={i} x1={pxr(x)} y1={axisY + 18} x2={pxr(x)} y2={axisY + 26} stroke="var(--accent)" strokeWidth={1.6} />
              ))}
              <path d={`M${pxr(mu)},${axisY - plotH - 8} l -6,-9 l 12,0 Z`} fill="var(--accent)" />
              <line x1={pxr(mu)} y1={axisY - plotH - 6} x2={pxr(mu)} y2={axisY} stroke="var(--accent)" strokeWidth={1.4} strokeDasharray="4 3" />
            </g>
          )}
        </svg>
      </div>

      {/* readout */}
      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {pick !== null && pick <= n ? (
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            P(X = {pick}) = C({n},{pick}) · {fmt(p, 2)}
            <sup>{pick}</sup> · {fmt(1 - p, 2)}
            <sup>{n - pick}</sup> = <b style={{ color: "var(--accent)" }}>{pmf[pick].toFixed(4)}</b>
            <span className="ml-2 text-[12px]" style={{ color: "var(--fg-2)" }}>
              (C = {nCr(n, pick)})
            </span>
          </div>
        ) : showMuSigma ? (
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            μ = np = <b style={{ color: "var(--accent)" }}>{fmt(mu, 2)}</b>, σ = √(np(1−p)) ={" "}
            <b style={{ color: "var(--accent)" }}>{fmt(sd, 2)}</b>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              {p === 0.5 ? "p = ½ — a symmetric pile" : p < 0.5 ? "p < ½ — the pile leans left, tail to the right" : "p > ½ — the pile leans right, tail to the left"}
            </div>
          </div>
        ) : (
          <div className="text-[13px]" style={{ color: "var(--fg-2)" }}>
            X ~ B({n}, {fmt(p, 2)}) — tap a bar for its exact probability
          </div>
        )}
      </div>

      {/* steppers */}
      <div className="mt-3 flex items-center justify-center gap-6">
        <div className="flex items-center gap-2">
          {stepBtn(-1, n <= 1, () => { setN((v) => Math.max(1, v - 1)); setPick(null); }, "Decrease n")}
          <div className="text-[12px]" style={{ color: "var(--fg-2)", minWidth: 52, textAlign: "center" }}>
            n = <b className="tabular" style={{ color: GEO_BLUE }}>{n}</b>
          </div>
          {stepBtn(1, n >= nMax, () => { setN((v) => Math.min(nMax, v + 1)); setPick(null); }, "Increase n")}
        </div>
        <div className="flex items-center gap-2">
          {stepBtn(-1, p <= 0.1, () => { setP((v) => Math.round((v - 0.1) * 100) / 100); setPick(null); }, "Decrease p")}
          <div className="text-[12px]" style={{ color: "var(--fg-2)", minWidth: 56, textAlign: "center" }}>
            p = <b className="tabular" style={{ color: GEO_BLUE }}>{fmt(p, 2)}</b>
          </div>
          {stepBtn(1, p >= 0.9, () => { setP((v) => Math.round((v + 0.1) * 100) / 100); setPick(null); }, "Increase p")}
        </div>
      </div>
    </div>
  );
}
