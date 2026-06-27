"use client";

import { useState } from "react";
import { Equal } from "lucide-react";
import { type DecimalColumnConfig } from "@/lib/genmath-interactive";
import DecimalColumnView from "@/components/genmath/interactive/DecimalColumnView";

export default function DecimalColumnSum({ config }: { config: DecimalColumnConfig }) {
  const { a, b, op, color = "#e8913c" } = config;
  const [shown, setShown] = useState(false);

  return (
    <div className="rounded-2xl p-5 sm:p-6" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <DecimalColumnView a={a} b={b} op={op} showAnswer={shown} color={color} />
      </div>

      <div className="mt-4 flex justify-center">
        {!shown ? (
          <button
            type="button"
            onClick={() => setShown(true)}
            className="gm-press inline-flex items-center gap-2 rounded-full px-5 py-2.5 text-[14px]"
            style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
          >
            <Equal className="h-4 w-4" /> {op === "add" ? "Add it up" : "Subtract"}
          </button>
        ) : (
          <button
            type="button"
            onClick={() => setShown(false)}
            className="gm-press rounded-full px-4 py-2 text-[13px]"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            Reset
          </button>
        )}
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        Decimal points in a line, missing places filled with{" "}
        <span style={{ color: "var(--fg-3)" }}>faded zeros</span> — then work column by column.
      </div>
    </div>
  );
}
