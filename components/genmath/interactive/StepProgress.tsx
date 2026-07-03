"use client";

// Slim progress bar + dot row for the interactive lesson player.
// Done steps fill with accent; the current step pulses; future steps are muted.
export default function StepProgress({
  total,
  current,
  onJump,
}: {
  total: number;
  current: number;
  onJump?: (i: number) => void;
}) {
  const pct = total > 1 ? (current / (total - 1)) * 100 : 100;
  return (
    <div className="w-full">
      <div
        className="relative h-1.5 w-full overflow-hidden rounded-full"
        style={{ background: "var(--bg-2)" }}
        aria-hidden="true"
      >
        <div
          className="absolute left-0 top-0 h-full rounded-full"
          style={{
            width: `${pct}%`,
            background: "var(--accent)",
            transition: "width 0.4s cubic-bezier(0.22,1,0.36,1)",
          }}
        />
      </div>
      <div className="mt-2 flex items-center justify-center gap-1.5">
        {Array.from({ length: total }).map((_, i) => {
          const done = i < current;
          const active = i === current;
          const dot = (
            <span
              className="block rounded-full"
              style={{
                width: active ? 9 : 7,
                height: active ? 9 : 7,
                background: done || active ? "var(--accent)" : "var(--line-strong, var(--line))",
                opacity: done ? 0.55 : 1,
                transition: "all 0.25s ease",
                boxShadow: active ? "0 0 0 4px var(--accent-wash)" : "none",
              }}
            />
          );
          return onJump ? (
            <button
              key={i}
              type="button"
              onClick={() => onJump(i)}
              aria-label={`Go to step ${i + 1}`}
              aria-current={active ? "step" : undefined}
              className="gm-press grid place-items-center"
              style={{ width: 20, height: 20 }}
            >
              {dot}
            </button>
          ) : (
            <span key={i} className="grid place-items-center" style={{ width: 20, height: 20 }} aria-hidden="true">
              {dot}
            </span>
          );
        })}
      </div>
    </div>
  );
}
