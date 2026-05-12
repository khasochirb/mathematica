"use client";

import Section2Card from "./Section2Card";
import { composeSlotAnswer, type Section2Item } from "@/lib/esh-section2";
import { TOPIC_LABELS, canonicalizeTopic } from "@/lib/esh-questions";

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
  // Topic chip is shown once per problem (all subproblems share the same
  // topic). Drawn from the first subproblem's metadata. Mirrors the
  // chip style used on Section 1 questions in QuestionCard.tsx.
  const head = items[0];
  const topicKey = canonicalizeTopic(head.topic);
  const topicLabel = TOPIC_LABELS[topicKey] || head.topic;
  return (
    <div className="space-y-4">
      {(head.topic || head.subtopic) && (
        <div className="flex items-center gap-2 flex-wrap">
          {head.topic && (
            <span
              className="mono text-[10px] uppercase px-2 py-1 rounded-full"
              style={{
                background: "var(--bg-2)",
                border: "1px solid var(--line)",
                color: "var(--fg-2)",
                letterSpacing: "0.06em",
              }}
            >
              {topicLabel}
            </span>
          )}
          {head.subtopic && (
            <span
              className="mono text-[10px]"
              style={{ color: "var(--fg-3)", letterSpacing: "0.04em" }}
            >
              {head.subtopic}
            </span>
          )}
        </div>
      )}
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
