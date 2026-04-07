"use client";

import { BarChart3, TrendingUp, TrendingDown, Trash2 } from "lucide-react";

interface TopicStats {
  topic: string;
  label: string;
  total: number;
  correct: number;
  incorrect: number;
  accuracy: number;
}

interface StatsPanelProps {
  overall: { total: number; correct: number; incorrect: number; accuracy: number };
  topicStats: TopicStats[];
  onClear: () => void;
}

export default function StatsPanel({ overall, topicStats, onClear }: StatsPanelProps) {
  if (overall.total === 0) {
    return (
      <div className="card-glass p-8 text-center">
        <BarChart3 className="w-10 h-10 text-gray-600 mx-auto mb-3" />
        <p className="text-gray-400">
          Бодлого бодож эхлэхэд таны статистик энд харагдана.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Overall */}
      <div className="card-glass p-6">
        <div className="flex items-center justify-between mb-5">
          <h2 className="font-display text-lg font-bold text-white">Таны үзүүлэлт</h2>
          <button
            onClick={onClear}
            className="flex items-center gap-1 text-xs text-gray-500 hover:text-red-400 transition-colors"
          >
            <Trash2 className="w-3.5 h-3.5" /> Арилгах
          </button>
        </div>

        <div className="grid grid-cols-3 gap-4 mb-6">
          <div className="text-center p-4 bg-primary-500/10 border border-primary-400/15 rounded-xl">
            <p className="text-2xl font-bold text-primary-300">{overall.total}</p>
            <p className="text-xs text-gray-500 mt-1">Нийт</p>
          </div>
          <div className="text-center p-4 bg-emerald-500/10 border border-emerald-400/15 rounded-xl">
            <p className="text-2xl font-bold text-emerald-300">{overall.correct}</p>
            <p className="text-xs text-gray-500 mt-1">Зөв</p>
          </div>
          <div className="text-center p-4 bg-red-500/10 border border-red-400/15 rounded-xl">
            <p className="text-2xl font-bold text-red-300">{overall.incorrect}</p>
            <p className="text-xs text-gray-500 mt-1">Буруу</p>
          </div>
        </div>

        {/* Overall accuracy bar */}
        <div>
          <div className="flex items-center justify-between mb-2">
            <span className="text-sm font-medium text-gray-400">Нийт амжилт</span>
            <span className="text-sm font-bold text-white">{overall.accuracy}%</span>
          </div>
          <div className="h-3 bg-white/[0.06] rounded-full overflow-hidden">
            <div
              className={`h-full rounded-full transition-all duration-500 ${
                overall.accuracy >= 80
                  ? "bg-gradient-to-r from-emerald-500 to-emerald-400"
                  : overall.accuracy >= 50
                  ? "bg-gradient-to-r from-yellow-500 to-yellow-400"
                  : "bg-gradient-to-r from-red-500 to-red-400"
              }`}
              style={{ width: `${overall.accuracy}%` }}
            />
          </div>
        </div>
      </div>

      {/* Per-topic */}
      <div className="card-glass p-6">
        <h3 className="font-display text-base font-bold text-white mb-4">Сэдвээр</h3>
        <div className="space-y-4">
          {topicStats.map((stat) => (
            <div key={stat.topic}>
              <div className="flex items-center justify-between mb-1.5">
                <div className="flex items-center gap-2">
                  <span className="text-sm text-gray-300">{stat.label}</span>
                  <span className="text-xs text-gray-600">
                    ({stat.correct}/{stat.total})
                  </span>
                </div>
                <div className="flex items-center gap-2">
                  {stat.accuracy < 50 && (
                    <span className="flex items-center gap-1 text-xs text-red-400">
                      <TrendingDown className="w-3 h-3" /> Сайжруулах
                    </span>
                  )}
                  {stat.accuracy >= 80 && (
                    <span className="flex items-center gap-1 text-xs text-emerald-400">
                      <TrendingUp className="w-3 h-3" /> Сайн
                    </span>
                  )}
                  <span className="text-sm font-medium text-gray-400 w-10 text-right">
                    {stat.accuracy}%
                  </span>
                </div>
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
                  style={{ width: `${stat.accuracy}%` }}
                />
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
