"use client";

import { useState } from "react";
import RatioFigure from "@/components/genmath/interactive/RatioFigure";
import { type CompareToggleConfig, type FigureSpec, partToWhole, formatRatio } from "@/lib/genmath-interactive";

type Mode = "partToPart" | "partToWhole";

export default function CompareToggle({ config }: { config: CompareToggleConfig }) {
  const [mode, setMode] = useState<Mode>("partToPart");
  const { groupA, groupB } = config;

  const groups = [
    { count: groupA.count, color: groupA.token.color, label: groupA.token.plural },
    { count: groupB.count, color: groupB.token.color, label: groupB.token.plural },
  ];
  const figure: FigureSpec =
    mode === "partToPart"
      ? { mode: "partToPart", groups }
      : { mode: "partToWhole", groups, highlightIndex: 0 };

  const [pwL, pwR] = partToWhole(groupA.count, groupB.count);
  const ratio = mode === "partToPart" ? formatRatio(groupA.count, groupB.count) : formatRatio(pwL, pwR);
  const caption =
    mode === "partToPart"
      ? `${groupA.count} ${groupA.token.plural} to ${groupB.count} ${groupB.token.plural}`
      : `${groupA.count} ${groupA.token.plural} out of ${pwR} total`;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      {/* The figure changes shape with the mode */}
      <div key={mode} className="flex justify-center">
        <RatioFigure figure={figure} />
      </div>

      {/* Readout */}
      <div className="mt-4 text-center">
        <span className="serif tabular" style={{ fontSize: 28, color: "var(--fg)" }}>{ratio}</span>
        <div className="mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>{caption}</div>
      </div>

      {/* Segmented toggle */}
      <div className="mx-auto mt-4 grid max-w-sm grid-cols-2 gap-1 rounded-full p-1" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {([
          ["partToPart", "Group to group"],
          ["partToWhole", "Group to total"],
        ] as [Mode, string][]).map(([m, label]) => {
          const on = mode === m;
          return (
            <button
              key={m}
              type="button"
              onClick={() => setMode(m)}
              className="gm-press rounded-full px-3 py-2 text-[13px]"
              style={{ background: on ? "var(--accent)" : "transparent", color: on ? "var(--accent-ink, #fff)" : "var(--fg-2)", fontWeight: on ? 500 : 400 }}
            >
              {label}
            </button>
          );
        })}
      </div>
    </div>
  );
}
