"use client";

// Client assembly for the ratings engine: gathers every evidence source the
// device knows about (synced attempts, local problem-bank mastery, local
// placement results) and feeds lib/ratings.ts. Pure computation stays there;
// this hook only collects.

import { useEffect, useMemo, useState } from "react";
import usePerformance from "./use-performance";
import { useAuth } from "./auth-context";
import { getBankTopics, loadBankProgress } from "./problem-bank";
import { loadPlacement } from "./placement-result";
import {
  computeRatings,
  type BankEvidence,
  type PlacementEvidence,
  type RatingsProfile,
} from "./ratings";

// Every namespace a placement result may live under. Phase 3 adds the named
// course placements; keeping the list here means the ratings pick them up the
// moment their pages exist.
export const RATING_PLACEMENT_NAMESPACES = [
  "grade6",
  "grade7",
  "grade8",
  "grade9",
  "grade10",
  "grade11",
  "grade12",
  "geometry",
] as const;

export default function useRatings(): {
  profile: RatingsProfile;
  status: ReturnType<typeof usePerformance>["status"];
} {
  const perf = usePerformance();
  const { user } = useAuth();
  const userId = user?.id ?? null;

  // localStorage sources load after mount so server and client renders match.
  const [bank, setBank] = useState<BankEvidence>({});
  const [placements, setPlacements] = useState<PlacementEvidence[]>([]);

  useEffect(() => {
    const evidence: BankEvidence = {};
    for (const topic of getBankTopics()) {
      const progress = loadBankProgress(topic.slug, userId);
      for (const form of topic.forms) {
        const p = progress.forms[form.id];
        if (!p || p.attempts <= 0) continue;
        const key = `course:${topic.slug}/${form.unit}`;
        const e = evidence[key] ?? { mastered: 0, attempted: 0 };
        e.attempted++;
        if (p.mastered) e.mastered++;
        evidence[key] = e;
      }
    }
    setBank(evidence);

    setPlacements(
      RATING_PLACEMENT_NAMESPACES.flatMap((ns) => {
        const stored = loadPlacement(userId, ns);
        if (!stored) return [];
        return [
          {
            namespace: ns,
            takenAt: stored.takenAt,
            topicScores: stored.topicScores.map((t) => ({
              slug: t.slug,
              seen: t.seen,
              correct: t.correct,
            })),
          },
        ];
      }),
    );
  }, [userId]);

  const profile = useMemo(
    () =>
      computeRatings({
        attempts: perf.attempts,
        bank,
        placements,
        now: Date.now(),
      }),
    [perf.attempts, bank, placements],
  );

  return { profile, status: perf.status };
}
