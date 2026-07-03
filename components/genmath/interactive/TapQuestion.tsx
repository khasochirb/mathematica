"use client";

import { useState } from "react";
import { Check, X } from "lucide-react";
import MathText from "@/components/esh/MathText";
import RatioFigure from "@/components/genmath/interactive/RatioFigure";
import CoordinateGrid from "@/components/genmath/interactive/CoordinateGrid";
import { type FigureSpec, type CoordinateGridConfig } from "@/lib/genmath-interactive";

export default function TapQuestion({
  prompt,
  options,
  correctIndex,
  explanation,
  figure,
  grid,
}: {
  prompt: string;
  options: string[];
  correctIndex: number;
  explanation: string;
  figure?: FigureSpec;
  grid?: CoordinateGridConfig;
}) {
  const [solved, setSolved] = useState(false);
  const [wrong, setWrong] = useState<number[]>([]);
  const [lastWrong, setLastWrong] = useState<number | null>(null);

  const pick = (i: number) => {
    if (solved) return;
    if (i === correctIndex) {
      setSolved(true);
    } else if (!wrong.includes(i)) {
      setWrong((w) => [...w, i]);
      setLastWrong(i);
    } else {
      setLastWrong(i);
    }
  };

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <p className="font-sans" style={{ fontSize: 16, lineHeight: 1.5, color: "var(--fg)" }}>
        <MathText text={prompt} />
      </p>

      {figure && (
        <div className="mt-3 flex justify-center">
          <RatioFigure figure={figure} />
        </div>
      )}

      {grid && (
        <div className="mt-3">
          <CoordinateGrid config={grid} />
        </div>
      )}

      <div className="mt-4 grid gap-2.5 sm:grid-cols-2">
        {options.map((opt, i) => {
          const isCorrect = solved && i === correctIndex;
          const isWrong = wrong.includes(i);
          let bg = "var(--bg-2)";
          let border = "var(--line)";
          let color = "var(--fg)";
          if (isCorrect) {
            bg = "rgba(63,178,127,0.14)";
            border = "#3fb27f";
            color = "var(--fg)";
          } else if (isWrong) {
            bg = "rgba(215,80,63,0.10)";
            border = "rgba(215,80,63,0.5)";
            color = "var(--fg-2)";
          }
          return (
            <button
              key={i}
              type="button"
              onClick={() => pick(i)}
              disabled={solved}
              className={`gm-press flex items-center justify-between gap-2 rounded-xl px-4 py-3 text-left ${
                isWrong && lastWrong === i ? "gm-shake" : ""
              }`}
              style={{ background: bg, border: `1.5px solid ${border}`, color, opacity: solved && !isCorrect ? 0.5 : 1 }}
            >
              <span className="q-math" style={{ fontSize: 15 }}>
                <MathText text={opt} />
              </span>
              {isCorrect && (
                <span className="gm-pop grid h-6 w-6 flex-shrink-0 place-items-center rounded-full" style={{ background: "#3fb27f", color: "#fff" }}>
                  <Check className="h-4 w-4" />
                </span>
              )}
              {isWrong && (
                <span className="grid h-6 w-6 flex-shrink-0 place-items-center rounded-full" style={{ background: "rgba(215,80,63,0.85)", color: "#fff" }}>
                  <X className="h-4 w-4" />
                </span>
              )}
            </button>
          );
        })}
      </div>

      {/* Feedback */}
      {solved ? (
        <div
          className="gm-step mt-3 flex items-start gap-2 rounded-xl p-3"
          style={{ background: "rgba(63,178,127,0.12)", border: "1px solid rgba(63,178,127,0.4)" }}
        >
          <Check className="mt-0.5 h-4 w-4 flex-shrink-0" style={{ color: "#2f9e6e" }} />
          <p className="font-sans" style={{ fontSize: 14, lineHeight: 1.5, color: "var(--fg-1)" }}>
            <span style={{ color: "#2f9e6e", fontWeight: 500 }}>Nice! </span>
            <MathText text={explanation} />
          </p>
        </div>
      ) : wrong.length > 0 ? (
        <p className="mt-3 text-[13px]" style={{ color: "var(--fg-2)" }}>
          Not quite — give it another try.
        </p>
      ) : null}
    </div>
  );
}
