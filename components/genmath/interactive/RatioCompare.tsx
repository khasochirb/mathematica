"use client";

import { useState } from "react";
import { Trophy, Equal } from "lucide-react";
import { type RatioCompareConfig } from "@/lib/genmath-interactive";

const WATER = "#9cc6e8"; // shared "water" blue so the juice colour is what stands out

type Side = "left" | "right";

function Segment({
  height,
  count,
  color,
  rounded,
  textColor,
}: {
  height: number;
  count: number;
  color: string;
  rounded: boolean;
  textColor: string;
}) {
  return (
    <div
      className="grid w-full place-items-center"
      style={{
        height,
        background: color,
        borderTopLeftRadius: rounded ? 8 : 0,
        borderTopRightRadius: rounded ? 8 : 0,
        transition: "height .55s cubic-bezier(.4,0,.2,1)",
        color: textColor,
        fontSize: 13,
        fontWeight: 600,
      }}
    >
      {count > 0 && height >= 16 ? count : ""}
    </div>
  );
}

function MixColumn({
  label,
  baseA,
  baseB,
  juice,
  water,
  scale,
  juiceColor,
  juiceH,
  waterH,
  barH,
  fair,
  isWinner,
  isTie,
}: {
  label: string;
  baseA: number;
  baseB: number;
  juice: number;
  water: number;
  scale: number;
  juiceColor: string;
  juiceH: number;
  waterH: number;
  barH: number;
  fair: boolean;
  isWinner: boolean;
  isTie: boolean;
}) {
  const highlight = fair && (isWinner || isTie);
  return (
    <div className="flex flex-col items-center">
      {/* marker row — fixed height so nothing jumps */}
      <div style={{ height: 24 }} className="flex items-end">
        {highlight && (
          <span className="gm-pop grid h-6 w-6 place-items-center rounded-full" style={{ background: "var(--accent)", color: "var(--accent-ink, #fff)" }}>
            {isTie ? <Equal className="h-3.5 w-3.5" aria-hidden /> : <Trophy className="h-3.5 w-3.5" aria-hidden />}
          </span>
        )}
      </div>

      <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>
        {label}
      </div>

      {/* stacked bar — juice on top of water, baselines aligned across jugs */}
      <div
        className="mt-1.5 flex w-16 flex-col justify-end overflow-hidden rounded-lg"
        style={{
          height: barH,
          background: "var(--bg-1)",
          border: isWinner && fair ? "2px solid var(--accent)" : "1px solid var(--line)",
          boxShadow: isWinner && fair ? "0 0 0 3px var(--accent-wash)" : "none",
          transition: "border-color .3s, box-shadow .3s",
        }}
      >
        <Segment height={juiceH} count={juice} color={juiceColor} rounded textColor="#3a2a12" />
        <Segment height={waterH} count={water} color={WATER} rounded={false} textColor="#173049" />
      </div>

      {/* ratio readout */}
      <div className="mt-2 text-center">
        <span className="serif tabular" style={{ fontSize: 20, color: "var(--fg)" }}>
          {fair ? `${juice} : ${water}` : `${baseA} : ${baseB}`}
        </span>
        {fair && scale > 1 && (
          <div className="gm-fade text-[11px]" style={{ color: "var(--fg-3)" }}>
            copied ×{scale}
          </div>
        )}
      </div>
    </div>
  );
}

export default function RatioCompare({ config }: { config: RatioCompareConfig }) {
  const { left, right, unitNote } = config;
  const [fair, setFair] = useState(false);

  // "Make the water equal": copy each mix (multiply both numbers by the same
  // amount — equivalent ratios) until both waters reach left.b × right.b. The
  // juice totals then come out as the cross-products.
  const scaleL = right.b;
  const scaleR = left.b;
  const water = left.b * right.b;
  const juiceL = fair ? left.a * scaleL : left.a;
  const waterL = fair ? water : left.b;
  const juiceR = fair ? right.a * scaleR : right.a;
  const waterR = fair ? water : right.b;

  const crossL = left.a * right.b;
  const crossR = right.a * left.b;
  const winner: Side | "tie" = crossL > crossR ? "left" : crossL < crossR ? "right" : "tie";
  const winnerLabel = winner === "left" ? left.label : right.label;

  // Bar sizing: tallest column fills a fixed pixel height; min 18px per present
  // segment so its number always fits.
  const maxTotal = Math.max(juiceL + waterL, juiceR + waterR);
  const unit = 142 / maxTotal;
  const segH = (c: number) => (c > 0 ? Math.max(Math.round(c * unit), 18) : 0);
  const jL = segH(juiceL);
  const wL = segH(waterL);
  const jR = segH(juiceR);
  const wR = segH(waterR);
  const barH = Math.max(jL + wL, jR + wR) + 4;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      {/* legend */}
      <div className="mb-3 flex items-center justify-center gap-4 text-[12px]" style={{ color: "var(--fg-2)" }}>
        <span className="inline-flex items-center gap-1.5">
          <span className="inline-block h-3 w-3 rounded" style={{ background: left.token.color }} /> juice
        </span>
        <span className="inline-flex items-center gap-1.5">
          <span className="inline-block h-3 w-3 rounded" style={{ background: WATER }} /> water
        </span>
      </div>

      {/* the two mixes */}
      <div className="flex items-end justify-center gap-8 sm:gap-12">
        <MixColumn
          label={left.label}
          baseA={left.a}
          baseB={left.b}
          juice={juiceL}
          water={waterL}
          scale={scaleL}
          juiceColor={left.token.color}
          juiceH={jL}
          waterH={wL}
          barH={barH}
          fair={fair}
          isWinner={winner === "left"}
          isTie={winner === "tie"}
        />
        <MixColumn
          label={right.label}
          baseA={right.a}
          baseB={right.b}
          juice={juiceR}
          water={waterR}
          scale={scaleR}
          juiceColor={right.token.color}
          juiceH={jR}
          waterH={wR}
          barH={barH}
          fair={fair}
          isWinner={winner === "right"}
          isTie={winner === "tie"}
        />
      </div>

      {/* conclusion — announced to screen readers when it changes */}
      <div
        role="status"
        aria-live="polite"
        className="gm-fade mt-4 rounded-xl px-4 py-3 text-center text-[13px]"
        style={{
          background: fair ? "var(--accent-wash)" : "var(--bg-2)",
          border: fair ? "1px solid var(--accent-line)" : "1px solid var(--line)",
          color: "var(--fg-1)",
          transition: "background .3s, border-color .3s",
        }}
      >
        {fair ? (
          winner === "tie" ? (
            <span>
              Same water (<b>{water}</b>), same juice (<b>{juiceL}</b> = <b>{juiceR}</b>) → they{" "}
              <b style={{ color: "var(--accent)" }}>taste exactly the same</b>.
            </span>
          ) : (
            <span>
              Same water now (<b>{water}</b>). Compare the juice: <b>{juiceL}</b> vs <b>{juiceR}</b> →{" "}
              <b style={{ color: "var(--accent)" }}>{winnerLabel}</b> {unitNote}.
            </span>
          )
        ) : (
          <span>Different amounts of water — hard to compare. Make the water equal first.</span>
        )}
      </div>

      {/* control */}
      <div className="mt-3 flex justify-center">
        <button
          type="button"
          onClick={() => setFair((v) => !v)}
          aria-pressed={fair}
          className="gm-press inline-flex items-center gap-2 rounded-full px-6 py-3 text-[14px] font-medium"
          style={{
            background: fair ? "var(--bg-2)" : "var(--accent)",
            color: fair ? "var(--fg-2)" : "var(--accent-ink, #fff)",
            border: fair ? "1px solid var(--line)" : "1px solid var(--accent)",
            transition: "background .2s, color .2s",
          }}
        >
          {fair ? "Reset" : "Make the water equal"}
        </button>
      </div>
    </div>
  );
}
