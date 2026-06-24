"use client";

import { useState } from "react";
import { type CompareToggleConfig, partToWhole, formatRatio } from "@/lib/genmath-interactive";

type Mode = "partToPart" | "partToWhole";

function Chips({
  count,
  color,
  glyph,
  ring,
  dim,
}: {
  count: number;
  color: string;
  glyph?: string;
  ring: string | null;
  dim: boolean;
}) {
  return (
    <>
      {Array.from({ length: count }).map((_, i) => (
        <span
          key={i}
          className="grid place-items-center rounded-lg"
          style={{
            width: 30,
            height: 30,
            background: color,
            border: "1px solid rgba(0,0,0,0.10)",
            boxShadow: ring ? `0 0 0 3px ${ring}` : "0 1px 2px rgba(0,0,0,0.08)",
            opacity: dim ? 0.4 : 1,
            transition: "box-shadow .2s ease, opacity .2s ease",
            fontSize: 14,
          }}
        >
          {glyph ?? ""}
        </span>
      ))}
    </>
  );
}

export default function CompareToggle({ config }: { config: CompareToggleConfig }) {
  const [mode, setMode] = useState<Mode>("partToPart");
  const { groupA, groupB } = config;
  const [ptpL, ptpR] = [groupA.count, groupB.count];
  const [pwhL, pwhR] = partToWhole(groupA.count, groupB.count);

  const isPP = mode === "partToPart";

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      {/* Object stage — in part-to-whole, the whole set is wrapped to show "the total" */}
      <div
        className="mx-auto flex max-w-sm flex-wrap items-center justify-center gap-2 rounded-xl p-3"
        style={{
          background: "var(--bg-2)",
          border: `2px solid ${isPP ? "transparent" : "var(--accent)"}`,
          transition: "border-color .25s ease",
        }}
      >
        <Chips
          count={groupA.count}
          color={groupA.token.color}
          glyph={groupA.token.glyph}
          ring={groupA.token.color}
          dim={false}
        />
        <Chips
          count={groupB.count}
          color={groupB.token.color}
          glyph={groupB.token.glyph}
          ring={isPP ? groupB.token.color : null}
          dim={false}
        />
      </div>

      {/* Readout */}
      <div className="mt-4 text-center">
        <span className="serif tabular" style={{ fontSize: 26, color: "var(--fg)" }}>
          {isPP ? formatRatio(ptpL, ptpR) : formatRatio(pwhL, pwhR)}
        </span>
        <div className="mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>
          {isPP ? (
            <>
              {groupA.count} {groupA.token.plural} to {groupB.count} {groupB.token.plural}
            </>
          ) : (
            <>
              {groupA.count} {groupA.token.plural} out of {pwhR} total
            </>
          )}
        </div>
      </div>

      {/* Segmented toggle */}
      <div
        className="mx-auto mt-4 grid max-w-sm grid-cols-2 gap-1 rounded-full p-1"
        style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}
      >
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
              style={{
                background: on ? "var(--accent)" : "transparent",
                color: on ? "var(--accent-ink, #fff)" : "var(--fg-2)",
                fontWeight: on ? 500 : 400,
              }}
            >
              {label}
            </button>
          );
        })}
      </div>
    </div>
  );
}
