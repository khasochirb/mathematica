"use client";

import { useState } from "react";
import { Trophy, Equal } from "lucide-react";
import { type FractionCompareConfig, gcd } from "@/lib/genmath-interactive";
import FractionBar from "@/components/genmath/interactive/FractionBar";

type Side = "left" | "right";

export default function FractionCompare({ config }: { config: FractionCompareConfig }) {
  const { left, right, color = "#e8913c" } = config;
  const [same, setSame] = useState(false);

  const lcd = (left.den / gcd(left.den, right.den)) * right.den;
  const sL = lcd / left.den;
  const sR = lcd / right.den;

  const numL = same ? left.num * sL : left.num;
  const denL = same ? lcd : left.den;
  const numR = same ? right.num * sR : right.num;
  const denR = same ? lcd : right.den;

  const crossL = left.num * right.den;
  const crossR = right.num * left.den;
  const winner: Side | "tie" = crossL > crossR ? "left" : crossL < crossR ? "right" : "tie";
  const winnerLabel = winner === "left" ? left.label ?? "the first" : right.label ?? "the second";

  const Row = ({ n, d, label, isWin }: { n: number; d: number; label?: string; isWin: boolean }) => (
    <div
      className="rounded-xl p-2.5"
      style={{
        background: same && isWin ? "var(--accent-wash)" : "transparent",
        border: same && isWin ? "1px solid var(--accent-line)" : "1px solid transparent",
        transition: "background .3s, border-color .3s",
      }}
    >
      <div className="mb-1 flex items-center justify-between text-[12px]" style={{ color: "var(--fg-2)" }}>
        <span>{label}</span>
        <span className="serif tabular" style={{ fontSize: 16, color: "var(--fg)" }}>{n}/{d}</span>
      </div>
      <FractionBar num={n} den={d} color={color} height={38} />
    </div>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="space-y-2">
        <Row n={numL} d={denL} label={left.label} isWin={winner === "left" || winner === "tie"} />
        <Row n={numR} d={denR} label={right.label} isWin={winner === "right" || winner === "tie"} />
      </div>

      <div
        role="status"
        aria-live="polite"
        className="gm-fade mt-3 rounded-xl px-4 py-3 text-center text-[13px]"
        style={{
          background: same ? "var(--accent-wash)" : "var(--bg-2)",
          border: same ? "1px solid var(--accent-line)" : "1px solid var(--line)",
          color: "var(--fg-1)",
          transition: "background .3s, border-color .3s",
        }}
      >
        {same ? (
          winner === "tie" ? (
            <span className="inline-flex items-center justify-center gap-1.5">
              <Equal className="h-4 w-4" aria-hidden /> Same-size pieces, same amount shaded — <b style={{ color: "var(--accent)" }}>they're equal</b>.
            </span>
          ) : (
            <span>
              Same-size pieces now (<b>{lcd}</b>ths). Compare the shaded pieces: <b>{numL}</b> vs <b>{numR}</b> →{" "}
              <b style={{ color: "var(--accent)" }}>{winnerLabel}</b> is bigger.
            </span>
          )
        ) : (
          <span>Different-size pieces — hard to compare. Give them the same-size pieces first.</span>
        )}
      </div>

      <div className="mt-3 flex justify-center">
        <button
          type="button"
          onClick={() => setSame((v) => !v)}
          aria-pressed={same}
          className="gm-press inline-flex items-center gap-2 rounded-full px-6 py-3 text-[14px] font-medium"
          style={{
            background: same ? "var(--bg-2)" : "var(--accent)",
            color: same ? "var(--fg-2)" : "var(--accent-ink, #fff)",
            border: same ? "1px solid var(--line)" : "1px solid var(--accent)",
            transition: "background .2s, color .2s",
          }}
        >
          {same ? "Reset" : "Give them the same-size pieces"}
        </button>
      </div>
    </div>
  );
}
