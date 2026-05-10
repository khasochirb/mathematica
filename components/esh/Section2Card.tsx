"use client";

import { useCallback, useMemo } from "react";
import MathText from "./MathText";
import EshFigure from "./EshFigure";
import type { Section2Item, Slot } from "@/lib/esh-section2";
import { parseSlotLabel } from "@/lib/esh-section2";

// Renders one Section 2 subproblem in the official EYSH answer-sheet
// format:
//
//   - Top: the formula. Each `[label]` placeholder renders as
//     `\boxed{<varPart>}` so the unknown variables appear inside visible
//     KaTeX-typeset rectangles. Pure visual; no inputs in the formula.
//   - Bottom: an "answer panel" — a grid of small labeled inputs. ONE
//     input per individual variable letter. Multi-letter slots like
//     `ab` (answer "12") split into separate inputs for `a` and `b`;
//     each takes one digit. Literal-prefix slots like `1e` (answer "10")
//     show only the variable portion (`e`) in the panel — the literal
//     `1` stays in the formula's `\boxed{}` group context.
//
// This mirrors the printed EYSH paper: students read a formula with
// boxed variables and fill answers in a separate alphabetic grid.
//
// Parent contract: `answers` is keyed by slot.label and holds the
// reconstructed full answer string (prefix + per-letter digits).
// `onAnswerChange(label, value)` fires with the full reconstructed slot
// answer on every keystroke. Empty letter positions in the middle of a
// multi-letter slot are stored as a space (sentinel) so positional
// integrity survives partial fills; trailing empties are trimmed.

interface Section2CardProps {
  item: Section2Item;
  answers: Record<string, string>;
  onAnswerChange: (label: string, value: string) => void;
  disabled?: boolean;
  showContext?: boolean;
  questionLabel?: string;
}

interface LetterCell {
  slotLabel: string;
  letter: string; // single variable letter shown above the input
  letterIdxInVarPart: number; // 0-based position within the slot's varPart
  prefix: string; // slot's literal prefix, used when reassembling the full answer
}

function transformInstructionForRender(text: string): string {
  return text.replace(/\[([A-Za-z0-9]+)\]/g, (_match, label: string) => {
    const { prefix, varPart } = parseSlotLabel(label);
    if (prefix.length > 0) {
      // Literal-prefix: render the prefix as plain math text BEFORE
      // the box, so it reads as "1▢" (the "1" outside, only "e" boxed).
      return `${prefix}\\boxed{${varPart}}`;
    }
    return `\\boxed{${varPart}}`;
  });
}

function decomposeLetters(slots: Slot[]): LetterCell[] {
  const cells: LetterCell[] = [];
  for (const slot of slots) {
    const { prefix, varPart } = parseSlotLabel(slot.label);
    for (let i = 0; i < varPart.length; i++) {
      cells.push({
        slotLabel: slot.label,
        letter: varPart[i],
        letterIdxInVarPart: i,
        prefix,
      });
    }
  }
  return cells;
}

// Read the current digit at a specific letter position from the parent's
// stored slot answer. Empty positions (or the space sentinel) read as "".
function getLetterDigit(cell: LetterCell, slotAnswer: string): string {
  const varValue = slotAnswer.slice(cell.prefix.length);
  const ch = varValue[cell.letterIdxInVarPart];
  return ch && ch !== " " ? ch : "";
}

// Reassemble a slot's answer from per-letter digits. Empty middle
// positions become " " so positional integrity is preserved when only
// some letters are filled. Trailing empties are trimmed for cleanliness.
function assembleSlotAnswer(slot: Slot, letters: string[]): string {
  const { prefix } = parseSlotLabel(slot.label);
  const padded = letters.map((l) => (l ? l : " ")).join("");
  const trimmed = padded.replace(/ +$/, "");
  return prefix + trimmed;
}

export default function Section2Card({
  item,
  answers,
  onAnswerChange,
  disabled = false,
  showContext = false,
  questionLabel,
}: Section2CardProps) {
  const transformedInstruction = useMemo(
    () => transformInstructionForRender(item.instruction),
    [item.instruction],
  );
  const letterCells = useMemo(
    () => decomposeLetters(item.slots),
    [item.slots],
  );

  const handleLetterChange = useCallback(
    (cell: LetterCell, newDigit: string) => {
      const slot = item.slots.find((s) => s.label === cell.slotLabel);
      if (!slot) return;
      const slotAnswer = answers[cell.slotLabel] ?? "";
      const slotCells = letterCells
        .filter((c) => c.slotLabel === cell.slotLabel)
        .sort((a, b) => a.letterIdxInVarPart - b.letterIdxInVarPart);
      const letters = slotCells.map((c) =>
        c.letterIdxInVarPart === cell.letterIdxInVarPart
          ? newDigit
          : getLetterDigit(c, slotAnswer),
      );
      onAnswerChange(slot.label, assembleSlotAnswer(slot, letters));
    },
    [item.slots, answers, onAnswerChange, letterCells],
  );

  return (
    <div
      className={`card-edit p-4 ${disabled ? "opacity-90" : ""}`}
      data-source={item.source}
    >
      <div className="flex items-center gap-2 mb-2">
        <span
          className="text-xs font-medium px-2 py-0.5 rounded-full"
          style={{
            background: "var(--accent-wash)",
            color: "var(--accent)",
            border: "1px solid var(--accent-line)",
          }}
        >
          {questionLabel ?? `${item.problem} (${item.subproblem})`}
        </span>
        <span
          className="text-xs"
          style={{ color: "var(--fg-3)" }}
        >{item.points} оноо</span>
      </div>

      {/* Figure: shown once per problem group at the top, above the
          context. Only set on subproblem === 1 by wire-figures-to-json.py;
          gated on showContext as well for defensive belt-and-suspenders. */}
      {showContext && item.figure && (
        <div className="mb-3">
          <EshFigure {...item.figure} />
        </div>
      )}

      {showContext && item.context && (
        <div
          className="text-[14px] leading-relaxed mb-3 pl-3"
          style={{
            color: "var(--fg-1)",
            borderLeft: "2px solid var(--accent-line)",
          }}
        >
          <MathText text={item.context} />
        </div>
      )}

      {/* Formula display — variables wrapped in \boxed{} for visual emphasis */}
      <div
        className="text-[15px] leading-loose"
        style={{ color: "var(--fg)" }}
      >
        <MathText text={transformedInstruction} />
      </div>

      {/* Answer panel — one input per individual variable letter */}
      {letterCells.length > 0 && (
        <div className="mt-6">
          <div
            className="text-xs uppercase tracking-wide mb-2"
            style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}
          >
            Хариулт
          </div>
          <div className="grid grid-cols-4 sm:grid-cols-6 gap-2">
            {letterCells.map((cell) => {
              const cellKey = `${cell.slotLabel}:${cell.letterIdxInVarPart}`;
              const slotAnswer = answers[cell.slotLabel] ?? "";
              const value = getLetterDigit(cell, slotAnswer);
              return (
                <label
                  key={cellKey}
                  className="esh-s2-letter-cell"
                  aria-label={`Letter ${cell.letter}`}
                >
                  <span className="esh-s2-letter-label">{cell.letter}</span>
                  <input
                    type="text"
                    inputMode="numeric"
                    pattern="\d"
                    maxLength={1}
                    value={value}
                    onChange={(e) => {
                      const filtered = e.target.value
                        .replace(/\D/g, "")
                        .slice(0, 1);
                      handleLetterChange(cell, filtered);
                    }}
                    disabled={disabled}
                    autoComplete="off"
                    className="esh-s2-letter-input"
                  />
                </label>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
}
