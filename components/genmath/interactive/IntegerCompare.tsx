"use client";

import { useState } from "react";
import { Check, X } from "lucide-react";
import { type IntegerCompareConfig } from "@/lib/genmath-interactive";
import IntegerLineView from "@/components/genmath/interactive/IntegerLineView";

export default function IntegerCompare({ config }: { config: IntegerCompareConfig }) {
  const { left, right, min, max, color = "#e8913c" } = config;
  const correct = left < right ? "<" : left > right ? ">" : "=";
  const [picked, setPicked] = useState<string | null>(null);
  const done = picked !== null;
  const right_ = picked === correct;
  const smaller = Math.min(left, right);

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <IntegerLineView
          min={min}
          max={max}
          points={[
            { value: left, label: String(left), color },
            { value: right, label: String(right), color: "#3b82f6" },
          ]}
        />
      </div>

      <div className="mt-2 flex flex-wrap items-center justify-center gap-2.5">
        <span className="serif tabular" style={{ fontSize: 22, color }}>{left}</span>
        <span className="serif" style={{ fontSize: 22, color: "var(--fg-3)" }}>?</span>
        <span className="serif tabular" style={{ fontSize: 22, color: "#3b82f6" }}>{right}</span>
      </div>

      <div className="mt-3 flex items-center justify-center gap-2.5">
        {(["<", "=", ">"] as const).map((sym) => {
          const isPick = picked === sym;
          const reveal = done && sym === correct;
          const wrongPick = done && isPick && sym !== correct;
          return (
            <button
              key={sym}
              type="button"
              onClick={() => !done && setPicked(sym)}
              disabled={done}
              aria-label={`Pick ${sym}`}
              className="gm-press grid h-12 w-14 place-items-center rounded-xl serif"
              style={{
                fontSize: 22,
                background: reveal ? "var(--accent-wash)" : wrongPick ? "rgba(220,80,80,0.12)" : "var(--bg-2)",
                border: `1px solid ${reveal ? "var(--accent-line)" : wrongPick ? "rgba(220,80,80,0.5)" : "var(--line)"}`,
                color: reveal ? "var(--accent)" : wrongPick ? "rgb(200,60,60)" : "var(--fg)",
                opacity: done && !reveal && !wrongPick ? 0.45 : 1,
              }}
            >
              {sym}
            </button>
          );
        })}
      </div>

      {done ? (
        <div className="gm-fade mt-3 flex items-center justify-center gap-2 text-center text-[13.5px]" style={{ color: "var(--fg-1)" }}>
          {right_ ? <Check className="h-4 w-4" style={{ color: "var(--accent)" }} /> : <X className="h-4 w-4" style={{ color: "rgb(200,60,60)" }} />}
          <span>
            <b className="serif tabular">{left} {correct} {right}</b>
            {correct === "=" ? " — they are equal." : ` — ${smaller} is further left, so it's smaller.`}
          </span>
        </div>
      ) : (
        <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
          Tap the sign — the number further left is smaller.
        </div>
      )}
    </div>
  );
}
