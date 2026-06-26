"use client";

import { useState } from "react";
import { Check, Tag } from "lucide-react";
import {
  type DealCompareConfig,
  unitPrice,
  cheaperDeal,
} from "@/lib/genmath-interactive";

export default function DealCompare({ config }: { config: DealCompareConfig }) {
  const { unit, currency, dealA, dealB } = config;
  const [revealed, setReveal] = useState(false);

  const upA = unitPrice(dealA.price, dealA.qty);
  const upB = unitPrice(dealB.price, dealB.qty);
  const winner = cheaperDeal(dealA, dealB); // 0, 1, or -1
  const tie = winner === -1;

  const deals = [dealA, dealB];
  const unitPrices = [upA, upB];

  function handlePress() {
    setReveal((v) => !v);
  }

  return (
    <div
      className="rounded-2xl p-4 sm:p-5"
      style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}
    >
      {/* Deal cards */}
      <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
        {deals.map((deal, i) => {
          const isBest = revealed && !tie && winner === i;
          const isDimmed = revealed && !tie && winner !== i;

          return (
            <div
              key={i}
              className="rounded-xl p-4"
              style={{
                background: "var(--bg-2)",
                border: `2px solid ${
                  isBest ? "#3fb27f" : "var(--line)"
                }`,
                opacity: isDimmed ? 0.5 : 1,
                transition: "border-color .25s ease, opacity .25s ease",
              }}
            >
              {/* Label row */}
              <div className="flex items-start justify-between gap-2">
                <span
                  className="text-[13px] font-medium uppercase tracking-wide"
                  style={{ color: "var(--fg-2)" }}
                >
                  {deal.label}
                </span>

                {/* Best-deal badge */}
                {isBest && (
                  <span
                    className="gm-pop inline-flex items-center gap-1 rounded-full px-2.5 py-0.5 text-[11px] font-semibold"
                    style={{
                      background: "#3fb27f",
                      color: "#fff",
                      border: "1px solid #2f9e6e",
                      whiteSpace: "nowrap",
                    }}
                  >
                    <Check className="h-3 w-3" />
                    Best deal
                  </span>
                )}
              </div>

              {/* Headline price */}
              <div className="mt-2 flex items-baseline gap-1.5">
                <span
                  className="serif tabular"
                  style={{ fontSize: 32, lineHeight: 1, color: "var(--fg)" }}
                >
                  {currency}{deal.price}
                </span>
                <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
                  for {deal.qty} {unit}s
                </span>
              </div>

              {/* Revealed unit price */}
              {revealed && (
                <div
                  className="gm-step mt-3 flex items-center gap-1.5 rounded-lg px-3 py-2"
                  style={{
                    background: isBest
                      ? "rgba(63,178,127,0.12)"
                      : "var(--bg-1)",
                    border: `1px solid ${isBest ? "#3fb27f" : "var(--line)"}`,
                  }}
                >
                  <Tag
                    className="h-3.5 w-3.5 shrink-0"
                    style={{ color: isBest ? "#2f9e6e" : "var(--fg-3)" }}
                  />
                  <span
                    className="serif tabular text-[14px] font-medium"
                    style={{ color: isBest ? "#2f9e6e" : "var(--fg)" }}
                  >
                    {currency}{unitPrices[i].toFixed(2)} per {unit}
                  </span>
                </div>
              )}
            </div>
          );
        })}
      </div>

      {/* Tie callout — only shown when revealed and equal */}
      {revealed && tie && (
        <div
          className="gm-fade mt-3 rounded-xl px-4 py-3 text-center text-[13px]"
          style={{
            background: "var(--bg-2)",
            border: "1px solid var(--line)",
            color: "var(--fg-2)",
          }}
        >
          Same price per {unit} — pick either!
        </div>
      )}

      {/* Action button */}
      <button
        type="button"
        onClick={handlePress}
        className="gm-press mt-4 w-full rounded-xl py-3.5 text-[15px] font-semibold"
        style={{
          background: revealed ? "var(--bg-2)" : "var(--accent)",
          color: revealed ? "var(--fg-2)" : "var(--accent-ink, #fff)",
          border: revealed ? "1px solid var(--line)" : "1px solid var(--accent)",
          transition: "background .2s ease, color .2s ease",
        }}
      >
        {revealed ? "Reset" : "Find the better deal"}
      </button>
    </div>
  );
}
