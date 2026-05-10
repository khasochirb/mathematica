"use client";

import Section2Card from "./Section2Card";
import { composeSlotAnswer, type Section2Item } from "@/lib/esh-section2";

// Renders one Section 2 problem (e.g. "2.1") as a single screen with
// every subproblem stacked vertically. Mirrors the printed EYSH paper
// where problem 2.1's shared context appears once on top, then parts
// (1), (2), (3) follow in order on the same page.
//
// Internally each sub-part is still a Section2Card — keeps the slot-
// rendering / per-letter-input logic in one place. The only difference
// is `showContext` is true ONLY on the first sub-part so the context
// block renders once per problem, not once per sub-part.

interface Section2ProblemProps {
  items: Section2Item[]; // all subproblems for one problem id, sorted by subproblem
  section2Answers: Record<string, Record<string, string>>;
  onAnswerChange: (
    itemSource: string,
    slotLabel: string,
    fullAnswer: string,
  ) => void;
  disabled?: boolean;
}

export default function Section2Problem({
  items,
  section2Answers,
  onAnswerChange,
  disabled,
}: Section2ProblemProps) {
  if (items.length === 0) return null;
  return (
    <div className="space-y-4">
      {items.map((item, i) => (
        <Section2Card
          key={item.source}
          item={item}
          showContext={i === 0}
          questionLabel={`${item.problem} (${item.subproblem})`}
          disabled={disabled}
          answers={Object.fromEntries(
            item.slots.map((slot) => [
              slot.label,
              composeSlotAnswer(slot, section2Answers[item.source] ?? {}),
            ]),
          )}
          onAnswerChange={(slotLabel, value) =>
            onAnswerChange(item.source, slotLabel, value)
          }
        />
      ))}
    </div>
  );
}
