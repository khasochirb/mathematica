"use client";

import { useMemo, useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { latticePaths, nCr, type PathGridConfig } from "@/lib/genmath-interactive";

// The street grid where combinations live: the number at each corner counts
// the right/down paths from Start, and every corner is (left + above) —
// Pascal's triangle tilted 45°. A stepper fills the grid diagonal by
// diagonal; tap any filled corner to see its two feeders. The finish corner
// reads C(m+n, m).

export default function PathGrid({ config }: { config: PathGridConfig }) {
  const { cols, rows } = config;
  const maxDiag = cols + rows;
  const [diag, setDiag] = useState(1);
  const [pick, setPick] = useState<[number, number] | null>(null);

  const value = useMemo(() => {
    const v: number[][] = [];
    for (let i = 0; i <= cols; i++) {
      v.push([]);
      for (let j = 0; j <= rows; j++) v[i].push(nCr(i + j, i));
    }
    return v;
  }, [cols, rows]);

  const cell = 66;
  const pad = 34;
  const W = pad * 2 + cols * cell;
  const H = pad * 2 + rows * cell;
  const px = (i: number) => pad + i * cell;
  const py = (j: number) => pad + j * cell;

  const shownAll = diag >= maxDiag;
  const total = latticePaths(cols, rows);
  const feeders: [number, number][] = pick
    ? ([
        [pick[0] - 1, pick[1]],
        [pick[0], pick[1] - 1],
      ].filter(([i, j]) => i >= 0 && j >= 0) as [number, number][])
    : [];
  const isFeeder = (i: number, j: number) => feeders.some(([a, b]) => a === i && b === j);

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 380 }} role="img" aria-label="Path-counting grid">
          {/* streets */}
          {Array.from({ length: cols + 1 }, (_, i) => (
            <line key={`v${i}`} x1={px(i)} y1={py(0)} x2={px(i)} y2={py(rows)} stroke="var(--line)" strokeWidth={2} />
          ))}
          {Array.from({ length: rows + 1 }, (_, j) => (
            <line key={`h${j}`} x1={px(0)} y1={py(j)} x2={px(cols)} y2={py(j)} stroke="var(--line)" strokeWidth={2} />
          ))}
          {/* feeder arrows for the tapped corner */}
          {pick &&
            feeders.map(([i, j], ix) => (
              <line
                key={`f${ix}`}
                x1={px(i)}
                y1={py(j)}
                x2={px(pick[0])}
                y2={py(pick[1])}
                stroke="var(--accent)"
                strokeWidth={3}
                strokeDasharray="4 3"
                opacity={0.85}
              />
            ))}
          {/* corner counts, revealed diagonal by diagonal */}
          {value.map((col, i) =>
            col.map((v, j) => {
              if (i + j > diag) return null;
              const hot = pick !== null && pick[0] === i && pick[1] === j;
              const fed = isFeeder(i, j);
              const finish = i === cols && j === rows;
              return (
                <g
                  key={`${i}-${j}`}
                  className={i + j === diag ? "gm-pop" : undefined}
                  style={{ cursor: "pointer", animationDelay: `${(j * 0.06).toFixed(2)}s` }}
                  onClick={() => setPick(hot ? null : [i, j])}
                >
                  <circle
                    cx={px(i)}
                    cy={py(j)}
                    r={15}
                    fill={hot ? "var(--accent)" : fed || finish ? "var(--accent-wash)" : "var(--bg-2)"}
                    stroke={hot || fed || finish ? "var(--accent)" : "var(--line)"}
                    strokeWidth={finish ? 2 : 1.4}
                    style={{ transition: "fill 0.2s ease, stroke 0.2s ease" }}
                  />
                  <text
                    x={px(i)}
                    y={py(j) + 4}
                    fontSize="11.5"
                    textAnchor="middle"
                    fontWeight={hot || finish ? 700 : 500}
                    fill={hot ? "var(--accent-ink, #fff)" : "var(--fg)"}
                    className="tabular"
                  >
                    {v}
                  </text>
                </g>
              );
            }),
          )}
          <text x={px(0) - 6} y={py(0) - 20} fontSize="10.5" fill={GEO_BLUE} fontWeight={700}>
            Start
          </text>
          <text x={px(cols) + 6} y={py(rows) + 24} fontSize="10.5" fill="var(--accent)" fontWeight={700} textAnchor="end">
            Finish
          </text>
        </svg>
      </div>

      {/* readout */}
      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {pick && pick[0] + pick[1] > 0 ? (
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            <b style={{ color: "var(--accent)" }}>{value[pick[0]][pick[1]]}</b> ={" "}
            {feeders.map(([i, j]) => value[i][j]).join(" + ")}
            <span className="ml-2 text-[12px]" style={{ color: "var(--fg-2)" }}>
              — arrive from the left or from above
            </span>
          </div>
        ) : shownAll ? (
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            paths to Finish: C({cols + rows}, {cols}) = <b style={{ color: "var(--accent)" }}>{total}</b>
            <span className="ml-2 text-[12px]" style={{ color: "var(--fg-2)" }}>
              — choose which {cols} of the {cols + rows} moves go right
            </span>
          </div>
        ) : (
          <div className="text-[13px]" style={{ color: "var(--fg-2)" }}>
            each corner counts the paths from Start — reveal the next diagonal, or tap a corner
          </div>
        )}
      </div>

      <div className="mt-3 flex items-center justify-center gap-2">
        <button
          type="button"
          onClick={() => { setDiag((d) => Math.max(1, d - 1)); setPick(null); }}
          disabled={diag <= 1}
          aria-label="Hide a diagonal"
          className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <Minus className="h-4 w-4" />
        </button>
        <div className="text-[12px]" style={{ color: "var(--fg-2)", minWidth: 110, textAlign: "center" }}>
          diagonals filled: <b className="tabular" style={{ color: GEO_BLUE }}>{diag}</b> / {maxDiag}
        </div>
        <button
          type="button"
          onClick={() => { setDiag((d) => Math.min(maxDiag, d + 1)); setPick(null); }}
          disabled={diag >= maxDiag}
          aria-label="Reveal the next diagonal"
          className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          <Plus className="h-4 w-4" />
        </button>
      </div>
    </div>
  );
}
