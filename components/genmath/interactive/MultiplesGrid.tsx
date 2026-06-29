"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { type MultiplesGridConfig } from "@/lib/genmath-interactive";

// A 1..max number grid. The multiples of the chosen number k light up, so
// skip-counting (k, 2k, 3k, …) is visible as a pattern across the chart.
export default function MultiplesGrid({ config }: { config: MultiplesGridConfig }) {
  const { max, start, color = "#e8913c" } = config;
  const [k, setK] = useState(Math.max(2, start));
  const cols = max % 10 === 0 ? 10 : 6;
  const list = [];
  for (let m = k; m <= max && list.length < 6; m += k) list.push(m);

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <div style={{ display: "grid", gridTemplateColumns: `repeat(${cols}, 30px)`, gap: 4 }}>
          {Array.from({ length: max }).map((_, i) => {
            const n = i + 1;
            const on = n % k === 0;
            return (
              <div
                key={n}
                className="grid place-items-center serif tabular"
                style={{
                  width: 30,
                  height: 30,
                  borderRadius: 6,
                  fontSize: 13,
                  background: on ? color : "var(--bg-2)",
                  color: on ? "#fff" : "var(--fg-3)",
                  border: "1px solid var(--line)",
                  transition: "background 120ms ease",
                }}
              >
                {n}
              </div>
            );
          })}
        </div>
      </div>

      <div className="mt-3 text-center text-[14px]" style={{ color: "var(--fg-1)" }}>
        Multiples of <b className="serif tabular" style={{ color: "var(--accent)" }}>{k}</b>:{" "}
        <span className="serif tabular">{list.join(", ")}, …</span>
      </div>

      <div className="mt-4 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={() => setK((v) => Math.max(2, v - 1))}
          disabled={k <= 2}
          aria-label="Smaller number"
          className="gm-press grid h-11 w-11 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <Minus className="h-4 w-4" />
        </button>
        <div className="text-center" style={{ minWidth: 84 }}>
          <div className="serif tabular" style={{ fontSize: 18, color: "var(--fg)" }}>count by {k}</div>
        </div>
        <button
          type="button"
          onClick={() => setK((v) => Math.min(10, v + 1))}
          disabled={k >= 10}
          aria-label="Bigger number"
          className="gm-press grid h-11 w-11 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          <Plus className="h-4 w-4" />
        </button>
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        Skip-count by {k} and every number you land on is a <b style={{ color: "var(--fg-1)" }}>multiple</b>.
      </div>
    </div>
  );
}
