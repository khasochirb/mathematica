"use client";

import { TOPIC_LABELS, ESH_DOMAINS, DOMAIN_OF_TOPIC } from "@/lib/esh-questions";

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

  // Group under the five MAIN topics (ministry strands), weakest subtopic
  // first within each — so the report reads "Алгебр: 12/18" with the exact
  // subtopic to fix right underneath, not a flat 14-row list.
  const groups = ESH_DOMAINS.map((domain) => {
    const rows = stats
      .filter((s) => DOMAIN_OF_TOPIC[s.topic] === domain.key)
      .sort((a, b) => a.accuracy - b.accuracy);
    const total = rows.reduce((n, r) => n + r.total, 0);
    const correct = rows.reduce((n, r) => n + r.correct, 0);
    return { domain, rows, total, correct };
  }).filter((g) => g.rows.length > 0);
  const ungrouped = stats
    .filter((s) => !DOMAIN_OF_TOPIC[s.topic])
    .sort((a, b) => a.accuracy - b.accuracy);

  return (
    <div className="space-y-5">
      {groups.map(({ domain, rows, total, correct }) => (
        <div key={domain.key}>
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs font-medium uppercase tracking-wide text-gray-400">
              {domain.titleMn}
            </span>
            <span className="text-xs text-gray-500">
              {correct}/{total}
            </span>
          </div>
          <div className="space-y-3">
            {rows.map((stat) => renderRow(stat, highlightWeak))}
          </div>
        </div>
      ))}
      {ungrouped.length > 0 && (
        <div className="space-y-3">{ungrouped.map((stat) => renderRow(stat, highlightWeak))}</div>
      )}
    </div>
  );
}

function renderRow(stat: TopicStat, highlightWeak: boolean) {
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
}
