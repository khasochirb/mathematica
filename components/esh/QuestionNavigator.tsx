"use client";

interface QuestionNavigatorProps {
  totalQuestions: number;
  currentIndex: number;
  answers: Record<number, string>;
  flagged: number[];
  onJumpTo: (index: number) => void;
}

export default function QuestionNavigator({
  totalQuestions,
  currentIndex,
  answers,
  flagged,
  onJumpTo,
}: QuestionNavigatorProps) {
  return (
    <div className="card-edit p-4">
      <div
        className="mono text-[10px] uppercase mb-3"
        style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}
      >
        Бодлогууд · {Object.keys(answers).length}/{totalQuestions}
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
      <div
        className="mt-3 flex items-center gap-3 mono text-[10px]"
        style={{ color: "var(--fg-3)", letterSpacing: "0.04em" }}
      >
        <span className="flex items-center gap-1">
          <span
            className="w-2.5 h-2.5 rounded-sm"
            style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)" }}
          />
          Хариулсан
        </span>
        <span className="flex items-center gap-1">
          <span
            className="w-2.5 h-2.5 rounded-sm"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}
          />
          Хариулаагүй
        </span>
        <span className="flex items-center gap-1">
          <span className="w-2.5 h-2.5 rounded-full" style={{ background: "var(--warn)" }} />
          Тэмдэглэсэн
        </span>
      </div>
    </div>
  );
}
