"use client";

import { useMemo, useState } from "react";
import { Sparkles, X } from "lucide-react";
import QuestionCard from "./QuestionCard";
import { getSimilarQuestions, getTestInfo } from "@/lib/esh-questions";
import type { Question } from "@/lib/esh-questions";
import usePerformance from "@/lib/use-performance";
import { useAuth } from "@/lib/auth-context";
import { useUpgradeModal } from "@/lib/upgrade-modal-context";

interface SimilarQuestionsPanelProps {
  question: Question;
  count?: number;
}

export default function SimilarQuestionsPanel({
  question,
  count = 3,
}: SimilarQuestionsPanelProps) {
  const [expanded, setExpanded] = useState(false);
  const { isSubscribed } = useAuth();
  const upgrade = useUpgradeModal();
  const perf = usePerformance();

  const similars = useMemo(
    () => getSimilarQuestions(question, isSubscribed, count),
    [question.source, isSubscribed, count],
  );

  if (similars.length === 0) return null;

  if (!expanded) {
    return (
      <button
        type="button"
        onClick={() => setExpanded(true)}
        className="mt-3 w-full text-left rounded-md p-3 flex items-center gap-3 transition-colors"
        style={{
          background: "var(--accent-wash)",
          border: "1px solid var(--accent-line)",
          color: "var(--accent-ink)",
        }}
      >
        <span
          className="w-7 h-7 rounded-full flex items-center justify-center shrink-0"
          style={{
            background: "var(--bg)",
            border: "1px solid var(--accent-line)",
            color: "var(--accent)",
          }}
        >
          <Sparkles className="w-3.5 h-3.5" />
        </span>
        <span className="flex-1 min-w-0">
          <span
            className="mono text-[10px] uppercase block"
            style={{ color: "var(--accent)", letterSpacing: "0.08em" }}
          >
            Сайжруулах
          </span>
          <span className="text-[13px]" style={{ color: "var(--fg-1)" }}>
            Ижил төрлийн {similars.length} бодлого үзэх
          </span>
        </span>
        <span
          className="mono text-[10px] uppercase shrink-0"
          style={{ color: "var(--accent)", letterSpacing: "0.08em" }}
        >
          Үзэх →
        </span>
      </button>
    );
  }

  return (
    <div
      className="mt-3 p-3 rounded-md"
      style={{
        background: "var(--bg-2)",
        border: "1px solid var(--accent-line)",
      }}
    >
      <div className="flex items-center justify-between mb-3">
        <span
          className="mono text-[10px] uppercase"
          style={{ color: "var(--accent)", letterSpacing: "0.08em" }}
        >
          Ижил төрлийн бодлого · {similars.length}
        </span>
        <button
          type="button"
          onClick={() => setExpanded(false)}
          className="p-1.5 rounded-md transition-colors"
          style={{ color: "var(--fg-3)" }}
          title="Хаах"
        >
          <X className="w-4 h-4" />
        </button>
      </div>

      {similars.map((s) => {
        const testKey = `${s.testNumber}${s.testVariant}`;
        const solutionsLocked =
          !isSubscribed && !!getTestInfo(testKey)?.solutionsRequirePremium;

        return (
          <QuestionCard
            key={s.source}
            mode="instant"
            question={s}
            onAnswer={(source, topic, subtopic, selected, correct, isCorrect) =>
              perf.recordAttempt({
                questionSource: source,
                topic,
                subtopic,
                selectedAnswer: selected,
                correctAnswer: correct,
                isCorrect,
              })
            }
            solutionsLocked={solutionsLocked}
            onSolutionUpgrade={upgrade.openSolutionUpgrade}
          />
        );
      })}
    </div>
  );
}
