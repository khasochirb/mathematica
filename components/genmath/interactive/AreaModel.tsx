"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { type AreaModelConfig, gcd } from "@/lib/genmath-interactive";

const A_COLOR = "#e8913c"; // columns (first fraction)
const B_COLOR = "#3f78d7"; // rows (second fraction)

function Stepper({
  label,
  value,
  max,
  onDec,
  onInc,
  color,
}: {
  label: string;
  value: number;
  max: number;
  onDec: () => void;
  onInc: () => void;
  color: string;
}) {
  return (
    <div className="flex items-center gap-2">
      <button type="button" onClick={onDec} disabled={value <= 1} aria-label={`fewer ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}>
        <Minus className="h-4 w-4" />
      </button>
      <span className="serif tabular text-center" style={{ minWidth: 54, fontSize: 16, color }}>{value}/{max}</span>
      <button type="button" onClick={onInc} disabled={value >= max} aria-label={`more ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}>
        <Plus className="h-4 w-4" />
      </button>
    </div>
  );
}

export default function AreaModel({ config }: { config: AreaModelConfig }) {
  const { aDen, bDen } = config;
  const [aNum, setANum] = useState(config.aNum);
  const [bNum, setBNum] = useState(config.bNum);

  const prodNum = aNum * bNum;
  const prodDen = aDen * bDen;
  const g = gcd(prodNum || 1, prodDen);
  const simpNum = prodNum / g;
  const simpDen = prodDen / g;
  const simplified = simpDen !== prodDen;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      {/* the grid: aDen columns × bDen rows */}
      <div className="mx-auto" style={{ maxWidth: 280 }}>
        <div className="grid gap-[2px]" style={{ gridTemplateColumns: `repeat(${aDen}, 1fr)`, aspectRatio: `${aDen} / ${bDen}` }}>
          {Array.from({ length: bDen }).map((_, r) =>
            Array.from({ length: aDen }).map((_, c) => {
              const inCol = c < aNum;
              const inRow = r < bNum;
              let bg = "var(--bg-2)";
              if (inCol && inRow) bg = "#7c5a2d"; // overlap = product (strong)
              else if (inCol) bg = "rgba(232,145,60,0.30)";
              else if (inRow) bg = "rgba(63,120,215,0.30)";
              return <div key={`${r}-${c}`} style={{ background: bg, borderRadius: 3, transition: "background .25s" }} />;
            })
          )}
        </div>
      </div>

      {/* steppers */}
      <div className="mt-4 flex flex-wrap items-center justify-center gap-x-6 gap-y-3">
        <div className="text-center">
          <div className="mb-1 text-[11px] uppercase tracking-wide" style={{ color: A_COLOR }}>columns</div>
          <Stepper label="columns" value={aNum} max={aDen} onDec={() => setANum((v) => Math.max(1, v - 1))} onInc={() => setANum((v) => Math.min(aDen, v + 1))} color={A_COLOR} />
        </div>
        <span className="serif" style={{ fontSize: 20, color: "var(--fg-3)" }}>×</span>
        <div className="text-center">
          <div className="mb-1 text-[11px] uppercase tracking-wide" style={{ color: B_COLOR }}>rows</div>
          <Stepper label="rows" value={bNum} max={bDen} onDec={() => setBNum((v) => Math.max(1, v - 1))} onInc={() => setBNum((v) => Math.min(bDen, v + 1))} color={B_COLOR} />
        </div>
      </div>

      {/* result */}
      <div className="mt-4 rounded-xl px-4 py-3 text-center text-[14px]" style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--fg-1)" }}>
        <span className="serif tabular">{aNum}/{aDen} × {bNum}/{bDen} = {prodNum}/{prodDen}</span>
        {simplified && <span className="serif tabular"> = <b style={{ color: "var(--accent)" }}>{simpNum}/{simpDen}</b></span>}
        <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>
          the dark overlap is <b>{prodNum}</b> of <b>{prodDen}</b> little boxes
        </div>
      </div>
    </div>
  );
}
