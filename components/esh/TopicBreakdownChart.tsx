"use client";

import { TOPIC_LABELS } from "@/lib/esh-questions";

interface TopicStat {
  topic: string;
  correct: number;
  total: number;
  accuracy: number;
}

interface TopicBreakdownChartProps {
  stats: TopicStat[];
  highlightWeak?: boolean;
}

export default function TopicBreakdownChart({
  stats,
  highlightWeak = true,
}: TopicBreakdownChartProps) {
  if (stats.length === 0) return null;

  const sorted = [...stats].sort((a, b) => a.accuracy - b.accuracy);

  return (
    <div className="space-y-3">
      {sorted.map((stat) => {
        const isWeak = highlightWeak && stat.accuracy < 50;
        return (
          <div key={stat.topic}>
            <div className="flex items-center justify-between mb-1">
              <div className="flex items-center gap-2">
                <span
                  className={`text-sm ${isWeak ? "text-red-300 font-medium" : "text-gray-300"}`}
                >
                  {TOPIC_LABELS[stat.topic] || stat.topic}
                </span>
                <span className="text-xs text-gray-600">
                  ({stat.correct}/{stat.total})
                </span>
              </div>
              <span
                className={`text-sm font-medium ${
                  stat.accuracy >= 80
                    ? "text-emerald-400"
                    : stat.accuracy >= 50
                      ? "text-yellow-400"
                      : "text-red-400"
                }`}
              >
                {stat.accuracy}%
              </span>
            </div>
            <div className="h-2 bg-white/[0.06] rounded-full overflow-hidden">
              <div
                className={`h-full rounded-full transition-all duration-500 ${
                  stat.accuracy >= 80
                    ? "bg-emerald-500"
                    : stat.accuracy >= 50
                      ? "bg-yellow-500"
                      : "bg-red-500"
                }`}
                style={{ width: `${Math.max(stat.accuracy, 2)}%` }}
              />
            </div>
          </div>
        );
      })}
    </div>
  );
}
