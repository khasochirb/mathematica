"use client";

import { useState } from "react";
import { Check, X } from "lucide-react";
import { type DecimalCompareConfig } from "@/lib/genmath-interactive";
import DecimalGridView from "@/components/genmath/interactive/DecimalGridView";

export default function DecimalCompare({ config }: { config: DecimalCompareConfig }) {
  const { left, right, color = "#e8913c" } = config;
  const lh = Math.round(left * 100);
  const rh = Math.round(right * 100);
  const correct = lh > rh ? ">" : lh < rh ? "<" : "=";
  const [picked, setPicked] = useState<string | null>(null);
  const done = picked !== null;
  const right_ = picked === correct;

  const fmt = (v: number) => v.toFixed(2).replace(/0+$/, "").replace(/\.$/, "");

  const Side = ({ v }: { v: number }) => (
    <div className="flex flex-col items-center gap-2">
      <DecimalGridView hundredths={Math.round(v * 100)} color={color} size={130} />
      <span className="serif tabular" style={{ fontSize: 22, color: "var(--fg)" }}>
        {fmt(v)}
      </span>
    </div>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex items-start justify-center gap-4 sm:gap-7">
        <Side v={left} />
        <span className="serif self-center" style={{ fontSize: 26, color: "var(--fg-3)" }}>
          ?
        </span>
        <Side v={right} />
      </div>

      {/* tap a verdict */}
      <div className="mt-4 flex items-center justify-center gap-2.5">
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

      {/* feedback */}
      {done && (
        <div className="gm-fade mt-3 flex items-center justify-center gap-2 text-center text-[13.5px]" style={{ color: "var(--fg-1)" }}>
          {right_ ? (
            <Check className="h-4 w-4" style={{ color: "var(--accent)" }} />
          ) : (
            <X className="h-4 w-4" style={{ color: "rgb(200,60,60)" }} />
          )}
          <span>
            <b className="serif tabular">{fmt(left)} {correct} {fmt(right)}</b>
            {" — "}
            {correct === "="
              ? "same amount shaded."
              : `${correct === ">" ? fmt(left) : fmt(right)} shades more of the whole.`}
          </span>
        </div>
      )}
      {!done && (
        <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
          Tap the sign that makes it true.
        </div>
      )}
    </div>
  );
}
