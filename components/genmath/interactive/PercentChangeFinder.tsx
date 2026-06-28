"use client";

import { useState } from "react";
import { Eye, RotateCcw } from "lucide-react";
import { type PercentChangeFinderConfig } from "@/lib/genmath-interactive";
import PercentChangeFinderView from "@/components/genmath/interactive/PercentChangeFinderView";

export default function PercentChangeFinder({ config }: { config: PercentChangeFinderConfig }) {
  const { original, final, currency = "$", color = "#e8913c" } = config;
  const [shown, setShown] = useState(false);

  return (
    <div className="rounded-2xl p-4 sm:p-6" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <PercentChangeFinderView original={original} final={final} currency={currency} color={color} showAnswer={shown} />
      </div>

      <div className="mt-5 flex justify-center">
        {!shown ? (
          <button
            type="button"
            onClick={() => setShown(true)}
            className="gm-press inline-flex items-center gap-2 rounded-full px-5 py-2.5 text-[14px]"
            style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
          >
            <Eye className="h-4 w-4" /> Show percent change
          </button>
        ) : (
          <button
            type="button"
            onClick={() => setShown(false)}
            className="gm-press inline-flex items-center gap-1.5 rounded-full px-4 py-2 text-[13px]"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <RotateCcw className="h-3.5 w-3.5" /> Reset
          </button>
        )}
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        The percent is the change divided by the <b style={{ color: "var(--fg-1)" }}>original</b>.
      </div>
    </div>
  );
}
