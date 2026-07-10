"use client";

import { useState } from "react";
import { GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { type VennCountsConfig } from "@/lib/genmath-interactive";

// Two overlapping circles with live counts in all four regions.
//   regions  — chips light up each region (only A, both, only B, neither)
//              and read its count.
//   addition — a four-beat play of the double-count story: |A|, then |B|,
//              then the overlap flashing "counted twice", then the fix:
//              |A ∪ B| = |A| + |B| − |A ∩ B|.

const RED = "rgb(200,60,60)";

type Region = "onlyA" | "both" | "onlyB" | "neither" | null;

export default function VennCounts({ config }: { config: VennCountsConfig }) {
  const { mode, labelA, labelB, onlyA, onlyB, both, neither = 0, countNoun = "outcomes" } = config;
  const [region, setRegion] = useState<Region>(null);
  const [beat, setBeat] = useState(0); // addition mode: 0 rest, 1 |A|, 2 |B|, 3 overlap, 4 formula

  const W = 340;
  const H = 210;
  const r = 62;
  const ax = W / 2 - 38;
  const bx = W / 2 + 38;
  const cy = 96;

  const total = onlyA + onlyB + both + neither;
  const sizeA = onlyA + both;
  const sizeB = onlyB + both;
  const union = onlyA + onlyB + both;

  const hlA = region === "onlyA" || (mode === "addition" && beat === 1);
  const hlB = region === "onlyB" || (mode === "addition" && beat === 2);
  const hlBoth = region === "both" || (mode === "addition" && (beat === 1 || beat === 2 || beat === 3));
  const hlNeither = region === "neither";
  const overlapHot = mode === "addition" && beat === 3;
  const fullA = mode === "addition" && beat === 1;
  const fullB = mode === "addition" && beat === 2;

  const regionChips: { key: Region & string; label: string; value: number }[] = [
    { key: "onlyA", label: `only ${labelA}`, value: onlyA },
    { key: "both", label: "both", value: both },
    { key: "onlyB", label: `only ${labelB}`, value: onlyB },
    ...(neither > 0 ? [{ key: "neither" as const, label: "neither", value: neither }] : []),
  ];

  const beatText = [
    <>the two circles overlap — press <b>next</b> to count the union honestly</>,
    <>
      <b style={{ color: GEO_BLUE }}>|{labelA}| = {sizeA}</b> — the whole left circle, overlap included
    </>,
    <>
      <b style={{ color: GEO_BLUE }}>|{labelB}| = {sizeB}</b> — the whole right circle, overlap included
    </>,
    <>
      adding them counts the <b style={{ color: RED }}>{both} in the overlap twice</b>
    </>,
    <>
      <span className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
        |{labelA} ∪ {labelB}| = {sizeA} + {sizeB} − {both} = <b style={{ color: "var(--accent)" }}>{union}</b>
      </span>
    </>,
  ];

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 380 }} role="img" aria-label="Venn diagram with counts">
          <defs>
            {/* the only-A crescent: circle A with circle B cut away (and mirrored) */}
            <mask id="vc-onlyA">
              <rect width={W} height={H} fill="black" />
              <circle cx={ax} cy={cy} r={r} fill="white" />
              <circle cx={bx} cy={cy} r={r} fill="black" />
            </mask>
            <mask id="vc-onlyB">
              <rect width={W} height={H} fill="black" />
              <circle cx={bx} cy={cy} r={r} fill="white" />
              <circle cx={ax} cy={cy} r={r} fill="black" />
            </mask>
            <mask id="vc-neither">
              <rect width={W} height={H} fill="white" />
              <circle cx={ax} cy={cy} r={r} fill="black" />
              <circle cx={bx} cy={cy} r={r} fill="black" />
            </mask>
            <clipPath id="vc-lens">
              <circle cx={ax} cy={cy} r={r} />
            </clipPath>
          </defs>

          {/* universe frame */}
          <rect x={6} y={6} width={W - 12} height={H - 34} rx={14} fill="none" stroke="var(--line)" strokeWidth={1.4} />
          {hlNeither && <rect x={6} y={6} width={W - 12} height={H - 34} rx={14} fill="var(--accent-wash)" mask="url(#vc-neither)" />}

          {/* highlights under the outlines */}
          {(hlA || fullA) && <circle cx={ax} cy={cy} r={r} fill="var(--accent-wash)" mask={fullA ? undefined : "url(#vc-onlyA)"} />}
          {(hlB || fullB) && <circle cx={bx} cy={cy} r={r} fill="var(--accent-wash)" mask={fullB ? undefined : "url(#vc-onlyB)"} />}
          {hlBoth && (
            <g clipPath="url(#vc-lens)">
              <circle cx={bx} cy={cy} r={r} fill={overlapHot ? "rgba(200,60,60,0.22)" : "var(--accent-wash)"} className={overlapHot ? "gm-pop" : undefined} />
            </g>
          )}

          {/* circle outlines */}
          <circle cx={ax} cy={cy} r={r} fill="none" stroke={GEO_BLUE} strokeWidth={2} />
          <circle cx={bx} cy={cy} r={r} fill="none" stroke="var(--accent)" strokeWidth={2} />
          <text x={ax - r + 4} y={cy - r - 6} fontSize="11" fill={GEO_BLUE} fontWeight={700}>
            {labelA}
          </text>
          <text x={bx + r - 4} y={cy - r - 6} fontSize="11" fill="var(--accent)" fontWeight={700} textAnchor="end">
            {labelB}
          </text>

          {/* region counts */}
          <text x={ax - r / 2 - 6} y={cy + 4} fontSize="15" textAnchor="middle" className="tabular" fontWeight={600} fill="var(--fg)">
            {onlyA}
          </text>
          <text x={(ax + bx) / 2} y={cy + 4} fontSize="15" textAnchor="middle" className="tabular" fontWeight={700} fill={overlapHot ? RED : "var(--fg)"}>
            {both}
          </text>
          <text x={bx + r / 2 + 6} y={cy + 4} fontSize="15" textAnchor="middle" className="tabular" fontWeight={600} fill="var(--fg)">
            {onlyB}
          </text>
          {neither > 0 && (
            <text x={W - 24} y={H - 44} fontSize="13" textAnchor="end" className="tabular" fontWeight={600} fill="var(--fg-2)">
              {neither}
            </text>
          )}
          <text x={14} y={H - 8} fontSize="10" fill="var(--fg-3)">
            {total} {countNoun} in all
          </text>
        </svg>
      </div>

      {/* readout + controls */}
      {mode === "regions" ? (
        <>
          <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
            {region ? (
              <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
                {regionChips.find((c) => c.key === region)?.label}:{" "}
                <b style={{ color: "var(--accent)" }}>{regionChips.find((c) => c.key === region)?.value}</b>{" "}
                <span className="text-[12px]" style={{ color: "var(--fg-2)" }}>
                  {countNoun}
                </span>
              </div>
            ) : (
              <div className="text-[13px]" style={{ color: "var(--fg-2)" }}>
                the four regions never overlap and cover everyone — pick one
              </div>
            )}
          </div>
          <div className="mt-3 flex flex-wrap justify-center gap-1.5">
            {regionChips.map((c) => (
              <button
                key={c.key}
                type="button"
                onClick={() => setRegion(region === c.key ? null : c.key)}
                className="gm-press rounded-full px-3.5 py-1.5 text-[12px]"
                style={
                  region === c.key
                    ? { background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }
                    : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }
                }
              >
                {c.label}
              </button>
            ))}
          </div>
        </>
      ) : (
        <>
          <div className="mt-2 rounded-xl p-3 text-center text-[13px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            {beatText[beat]}
          </div>
          <div className="mt-3 flex justify-center gap-2">
            <button
              type="button"
              onClick={() => setBeat((b) => (b + 1) % 5)}
              className="gm-press rounded-full px-4 py-2 text-[13px]"
              style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
            >
              {beat === 0 ? "next" : beat < 4 ? "next" : "replay"}
            </button>
          </div>
        </>
      )}
    </div>
  );
}
