"use client";

interface QuestionNavigatorProps {
  totalQuestions: number;
  currentIndex: number; // 0-based
  answers: Record<number, string>; // questionNumber -> letter
  flagged: number[]; // questionNumbers
  onJumpTo: (index: number) => void; // 0-based index
}

export default function QuestionNavigator({
  totalQuestions,
  currentIndex,
  answers,
  flagged,
  onJumpTo,
}: QuestionNavigatorProps) {
  return (
    <div className="card-glass p-4">
      <div className="text-xs font-medium text-gray-500 mb-3">
        Бодлогууд ({Object.keys(answers).length}/{totalQuestions})
      </div>
      <div className="grid grid-cols-6 gap-1.5">
        {Array.from({ length: totalQuestions }, (_, i) => {
          const qNum = i + 1;
          const isAnswered = qNum in answers;
          const isFlagged = flagged.includes(qNum);
          const isCurrent = i === currentIndex;

          let bg = "bg-white/[0.06] text-gray-500";
          if (isAnswered) bg = "bg-primary-500/20 text-primary-300";
          if (isCurrent)
            bg += " ring-2 ring-primary-400/60";

          return (
            <button
              key={i}
              onClick={() => onJumpTo(i)}
              className={`relative w-full aspect-square rounded-lg text-xs font-bold flex items-center justify-center transition-all hover:opacity-80 ${bg}`}
            >
              {qNum}
              {isFlagged && (
                <span className="absolute -top-0.5 -right-0.5 w-2.5 h-2.5 bg-orange-500 rounded-full border-2 border-surface-900" />
              )}
            </button>
          );
        })}
      </div>
      <div className="mt-3 flex items-center gap-3 text-[10px] text-gray-600">
        <span className="flex items-center gap-1">
          <span className="w-2.5 h-2.5 rounded bg-primary-500/20" /> Хариулсан
        </span>
        <span className="flex items-center gap-1">
          <span className="w-2.5 h-2.5 rounded bg-white/[0.06]" /> Хариулаагүй
        </span>
        <span className="flex items-center gap-1">
          <span className="w-2.5 h-2.5 rounded bg-orange-500" /> Тэмдэглэсэн
        </span>
      </div>
    </div>
  );
}
