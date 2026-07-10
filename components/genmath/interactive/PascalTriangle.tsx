"use client";

import { useMemo, useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { pascalRow, type PascalTriangleConfig } from "@/lib/genmath-interactive";

// Pascal's triangle explorer, four ways in:
//   build        — a stepper grows the triangle row by row; tap any inner
//                  cell and its two parents light up: 10 = 4 + 6.
//   sums         — every row's total appears at the right: the powers of 2.
//   combinations — tap any cell for its C(n, k) reading.
//   expansion    — a row stepper writes out (a+b)^n with that row as its
//                  coefficients, term by term.

export default function PascalTriangle({ config }: { config: PascalTriangleConfig }) {
  const { mode, rows = 6 } = config;
  const [visible, setVisible] = useState(mode === "build" ? 2 : mode === "expansion" ? 2 : rows);
  const [pick, setPick] = useState<[number, number] | null>(null);

  const allRows = useMemo(() => Array.from({ length: rows + 1 }, (_, n) => pascalRow(n)), [rows]);
  const shown = mode === "build" ? visible : rows;
  const expN = mode === "expansion" ? visible : 0;

  const cellW = 40;
  const rowH = 32;
  const padX = 16;
  const padTop = 18;
  const sumCol = mode === "sums" ? 64 : 0;
  const W = padX * 2 + (rows + 1) * cellW + sumCol;
  const H = padTop + (shown + 1) * rowH + 8;
  const cx = (W - sumCol) / 2;
  const px = (n: number, k: number) => cx + (k - n / 2) * cellW;
  const py = (n: number) => padTop + n * rowH;

  const parents: [number, number][] =
    pick && pick[0] > 0
      ? ([
          [pick[0] - 1, pick[1] - 1],
          [pick[0] - 1, pick[1]],
        ].filter(([n, k]) => k >= 0 && k <= n) as [number, number][])
      : [];

  const isParent = (n: number, k: number) => parents.some(([pn, pk]) => pn === n && pk === k);
  const isPick = (n: number, k: number) => pick !== null && pick[0] === n && pick[1] === k;
  const hotRow = mode === "expansion" ? expN : -1;

  const stepper = (val: number, set: (v: number) => void, lo: number, hi: number, label: string) => (
    <div className="mt-3 flex items-center justify-center gap-2">
      <button
        type="button"
        onClick={() => set(Math.max(lo, val - 1))}
        disabled={val <= lo}
        aria-label={`Fewer ${label}`}
        className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35"
        style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
      >
        <Minus className="h-4 w-4" />
      </button>
      <div className="text-[12px]" style={{ color: "var(--fg-2)", minWidth: 88, textAlign: "center" }}>
        {label}: <b className="tabular" style={{ color: GEO_BLUE }}>{val}</b>
      </div>
      <button
        type="button"
        onClick={() => set(Math.min(hi, val + 1))}
        disabled={val >= hi}
        aria-label={`More ${label}`}
        className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35"
        style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
      >
        <Plus className="h-4 w-4" />
      </button>
    </div>
  );

  const term = (n: number, k: number, coef: number) => {
    const a = n - k;
    return (
      <span key={k}>
        {k > 0 && " + "}
        {coef > 1 && coef}
        {a > 0 && <>a{a > 1 && <sup>{a}</sup>}</>}
        {k > 0 && <>b{k > 1 && <sup>{k}</sup>}</>}
        {a === 0 && k === 0 && 1}
      </span>
    );
  };

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 430 }} role="img" aria-label="Pascal's triangle">
          {allRows.slice(0, shown + 1).map((row, n) => (
            <g key={n}>
              {/* parent connectors for the tapped cell */}
              {row.map((v, k) => {
                if (!isPick(n, k)) return null;
                return parents.map(([pn, pk], i) => (
                  <line
                    key={`c${i}`}
                    x1={px(pn, pk)}
                    y1={py(pn) + 9}
                    x2={px(n, k)}
                    y2={py(n) - 9}
                    stroke="var(--accent)"
                    strokeWidth={2}
                    strokeDasharray="3 2"
                  />
                ));
              })}
              {row.map((v, k) => {
                const hot = isPick(n, k);
                const par = isParent(n, k);
                const rowHot = n === hotRow;
                return (
                  <g
                    key={k}
                    className={mode === "build" && n === shown ? "gm-pop" : undefined}
                    style={{
                      cursor: mode === "build" || mode === "combinations" ? "pointer" : undefined,
                      animationDelay: `${(k * 0.05).toFixed(2)}s`,
                    }}
                    onClick={
                      mode === "build" || mode === "combinations"
                        ? () => setPick(hot ? null : [n, k])
                        : undefined
                    }
                  >
                    <rect
                      x={px(n, k) - 16}
                      y={py(n) - 11}
                      width={32}
                      height={22}
                      rx={7}
                      fill={hot ? "var(--accent)" : par ? "var(--accent-wash)" : rowHot ? "var(--accent-wash)" : "var(--bg-2)"}
                      stroke={hot || par || rowHot ? "var(--accent)" : "var(--line)"}
                      style={{ transition: "fill 0.2s ease, stroke 0.2s ease" }}
                    />
                    <text
                      x={px(n, k)}
                      y={py(n) + 4}
                      fontSize="11.5"
                      textAnchor="middle"
                      fontWeight={hot || rowHot ? 700 : 500}
                      fill={hot ? "var(--accent-ink, #fff)" : "var(--fg)"}
                      className="tabular"
                    >
                      {v}
                    </text>
                  </g>
                );
              })}
              {/* row labels + sums */}
              <text x={8} y={py(n) + 4} fontSize="9" fill="var(--fg-3)">
                n={n}
              </text>
              {mode === "sums" && (
                <text x={W - sumCol + 14} y={py(n) + 4} fontSize="11" fill={GEO_BLUE} className="tabular" fontWeight={600}>
                  = {row.reduce((a, b) => a + b, 0)}
                </text>
              )}
            </g>
          ))}
        </svg>
      </div>

      {/* readout */}
      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {mode === "build" &&
          (pick && pick[0] > 0 ? (
            <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
              <b style={{ color: "var(--accent)" }}>{allRows[pick[0]][pick[1]]}</b> ={" "}
              {parents.map(([n, k]) => allRows[n][k]).join(" + ") || "1 (an edge — nothing above)"}
            </div>
          ) : (
            <div className="text-[13px]" style={{ color: "var(--fg-2)" }}>
              every inner number is the <b>sum of the two above it</b> — tap one to see its parents
            </div>
          ))}
        {mode === "sums" && (
          <div className="text-[13px]" style={{ color: "var(--fg-2)" }}>
            row n adds to <b className="tabular" style={{ color: GEO_BLUE }}>2<sup>n</sup></b> — every subset of n
            things, counted by size
          </div>
        )}
        {mode === "combinations" &&
          (pick ? (
            <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
              C({pick[0]}, {pick[1]}) = <b style={{ color: "var(--accent)" }}>{allRows[pick[0]][pick[1]]}</b>
              <span className="ml-2 text-[12px]" style={{ color: "var(--fg-2)" }}>
                — ways to choose {pick[1]} from {pick[0]}
              </span>
            </div>
          ) : (
            <div className="text-[13px]" style={{ color: "var(--fg-2)" }}>
              row n, position k <b>is</b> C(n, k) — tap any cell to read it
            </div>
          ))}
        {mode === "expansion" && (
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            (a + b)<sup>{expN}</sup> = {allRows[expN].map((c, k) => term(expN, k, c))}
          </div>
        )}
      </div>

      {mode === "build" && stepper(visible, (v) => { setVisible(v); setPick(null); }, 1, rows, "rows")}
      {mode === "expansion" && stepper(visible, setVisible, 1, rows, "power n")}
    </div>
  );
}
