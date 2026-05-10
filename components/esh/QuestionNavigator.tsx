"use client";

import type { Section2Item } from "@/lib/esh-section2";
import { composeSlotAnswer, parseSlotLabel } from "@/lib/esh-section2";

interface QuestionNavigatorProps {
  totalQuestions: number;
  currentIndex: number;
  answers: Record<number, string>;
  flagged: number[];
  onJumpTo: (index: number) => void;

  // Optional Section 2 surface. When provided, the navigator renders a
  // second row-group ("Хэсэг 2") with ONE cell per problem (2.1, 2.2,
  // 2.3, 2.4) — not per subproblem. Each problem screen contains all
  // its sub-parts stacked, matching the printed EYSH paper layout.
  // The runner's `currentIndex` is over the combined screen list:
  //   0..totalQuestions-1                  → MCQ cells
  //   totalQuestions..totalQuestions+P-1   → Section 2 problem cells
  //                                          (P = # of unique problem ids)
  section2Items?: readonly Section2Item[];
  section2Answers?: Record<string, Record<string, string>>;
}

type ProblemFill = "empty" | "partial" | "filled";

function problemFillStatus(
  items: Section2Item[],
  answers: Record<string, Record<string, string>>,
): ProblemFill {
  let anyFilled = false;
  let allFilled = true;
  for (const item of items) {
    const letterMap = answers[item.source] ?? {};
    for (const slot of item.slots) {
      const composed = composeSlotAnswer(slot, letterMap);
      const fullyFilled = composed.length === slot.answer.length;
      if (fullyFilled) {
        anyFilled = true;
      } else {
        allFilled = false;
        // Even a partially-filled slot counts as "anyFilled" — useful
        // for the partial-state display.
        const { varPart } = parseSlotLabel(slot.label);
        for (const letter of varPart) {
          if (letterMap[letter]) anyFilled = true;
        }
      }
    }
  }
  if (allFilled) return "filled";
  if (anyFilled) return "partial";
  return "empty";
}

function uniqueProblemIds(items: readonly Section2Item[]): string[] {
  const seen: string[] = [];
  for (const item of items) {
    if (!seen.includes(item.problem)) seen.push(item.problem);
  }
  return seen;
}

export default function QuestionNavigator({
  totalQuestions,
  currentIndex,
  answers,
  flagged,
  onJumpTo,
  section2Items,
  section2Answers,
}: QuestionNavigatorProps) {
  const hasSection2 = !!section2Items && section2Items.length > 0;
  const part2BaseIndex = totalQuestions;
  const problemIds = hasSection2 ? uniqueProblemIds(section2Items!) : [];
  const itemsByProblem: Record<string, Section2Item[]> = {};
  if (hasSection2) {
    for (const item of section2Items!) {
      (itemsByProblem[item.problem] ??= []).push(item);
    }
  }

  const filledProblemCount = problemIds.filter(
    (id) =>
      problemFillStatus(itemsByProblem[id], section2Answers ?? {}) ===
      "filled",
  ).length;

  return (
    <div className="card-edit p-4">
      <div
        className="mono text-[10px] uppercase mb-3"
        style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}
      >
        {hasSection2 ? "Хэсэг 1" : "Бодлогууд"} ·{" "}
        {Object.keys(answers).length}/{totalQuestions}
      </div>
      <div className="grid grid-cols-6 gap-1.5">
        {Array.from({ length: totalQuestions }, (_, i) => {
          const qNum = i + 1;
          const isAnswered = qNum in answers;
          const isFlagged = flagged.includes(qNum);
          const isCurrent = i === currentIndex;

          const cellStyle: React.CSSProperties = isAnswered
            ? {
                background: "var(--accent-wash)",
                border: "1px solid var(--accent-line)",
                color: "var(--accent)",
              }
            : {
                background: "var(--bg-2)",
                border: "1px solid var(--line)",
                color: "var(--fg-3)",
              };

          if (isCurrent) {
            cellStyle.outline = "2px solid var(--accent)";
            cellStyle.outlineOffset = "1px";
          }

          return (
            <button
              key={i}
              onClick={() => onJumpTo(i)}
              className="relative w-full aspect-square rounded-md mono tabular text-[11px] flex items-center justify-center transition-colors hover:opacity-80"
              style={cellStyle}
            >
              {qNum}
              {isFlagged && (
                <span
                  className="absolute -top-0.5 -right-0.5 w-2.5 h-2.5 rounded-full"
                  style={{
                    background: "var(--warn)",
                    border: "2px solid var(--bg-1)",
                  }}
                />
              )}
            </button>
          );
        })}
      </div>

      {hasSection2 && (
        <>
          <div
            className="mono text-[10px] uppercase mt-4 mb-3"
            style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}
          >
            Хэсэг 2 · {filledProblemCount}/{problemIds.length}
          </div>
          <div className="grid grid-cols-4 gap-1.5">
            {problemIds.map((id, i) => {
              const screenIndex = part2BaseIndex + i;
              const isCurrent = screenIndex === currentIndex;
              const status = problemFillStatus(
                itemsByProblem[id],
                section2Answers ?? {},
              );

              const cellStyle: React.CSSProperties =
                status === "filled"
                  ? {
                      background: "var(--accent-wash)",
                      border: "1px solid var(--accent-line)",
                      color: "var(--accent)",
                    }
                  : status === "partial"
                    ? {
                        background:
                          "color-mix(in oklch, var(--warn) 14%, transparent)",
                        border:
                          "1px solid color-mix(in oklch, var(--warn) 30%, transparent)",
                        color: "var(--warn)",
                      }
                    : {
                        background: "var(--bg-2)",
                        border: "1px solid var(--line)",
                        color: "var(--fg-3)",
                      };

              if (isCurrent) {
                cellStyle.outline = "2px solid var(--accent)";
                cellStyle.outlineOffset = "1px";
              }

              return (
                <button
                  key={id}
                  onClick={() => onJumpTo(screenIndex)}
                  className="w-full rounded-md mono tabular text-[12px] py-2 transition-colors hover:opacity-80"
                  style={cellStyle}
                  title={`Хэсэг 2 · ${id}`}
                >
                  {id}
                </button>
              );
            })}
          </div>
        </>
      )}

      <div
        className="mt-3 flex items-center gap-3 mono text-[10px] flex-wrap"
        style={{ color: "var(--fg-3)", letterSpacing: "0.04em" }}
      >
        <span className="flex items-center gap-1">
          <span
            className="w-2.5 h-2.5 rounded-sm"
            style={{
              background: "var(--accent-wash)",
              border: "1px solid var(--accent-line)",
            }}
          />
          Хариулсан
        </span>
        {hasSection2 && (
          <span className="flex items-center gap-1">
            <span
              className="w-2.5 h-2.5 rounded-sm"
              style={{
                background:
                  "color-mix(in oklch, var(--warn) 14%, transparent)",
                border:
                  "1px solid color-mix(in oklch, var(--warn) 30%, transparent)",
              }}
            />
            Дутуу
          </span>
        )}
        <span className="flex items-center gap-1">
          <span
            className="w-2.5 h-2.5 rounded-sm"
            style={{
              background: "var(--bg-2)",
              border: "1px solid var(--line)",
            }}
          />
          Хариулаагүй
        </span>
        <span className="flex items-center gap-1">
          <span
            className="w-2.5 h-2.5 rounded-full"
            style={{ background: "var(--warn)" }}
          />
          Тэмдэглэсэн
        </span>
      </div>
    </div>
  );
}
