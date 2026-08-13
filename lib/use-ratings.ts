"use client";

// Client assembly for the ratings engine: gathers every evidence source the
// device knows about (synced attempts, local problem-bank mastery, local
// placement results) and feeds lib/ratings.ts. Pure computation stays there;
// this hook only collects.

import { useEffect, useMemo, useState } from "react";
import usePerformance from "./use-performance";
import { useAuth } from "./auth-context";
// Manifest, not corpus: the ratings card only needs form ids and their
// units, and this hook runs on every dashboard/catalog render — importing
// lib/bank-data here would put ~9 MB back into the shared client chunk.
import { loadBankProgress } from "./problem-bank";
import { bankManifest, type BankTopicMeta } from "./bank-manifest";
import { loadPlacement } from "./placement-result";
import {
  computeRatings,
  type BankEvidence,
  type HubBankEvidence,
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
  "algebra-1",
  "algebra-2",
  "trigonometry",
  "solid-geometry",
  "prob-stats",
  "precalculus",
  "calculus",
  "vectors-matrices",
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
  const [hubBank, setHubBank] = useState<HubBankEvidence>({});
  const [placements, setPlacements] = useState<PlacementEvidence[]>([]);

  useEffect(() => {
    // SOLVED work only — a form the student attempted but never got right
    // contributes nothing rather than counting against them (lib/ratings
    // BankEvidence). Both tallies only ever grow.
    //
    // Two destinations, decided by whether a bank's units ARE course units:
    //   • the /math ladder and the IB tiers mirror real course units, so
    //     their work lands on those units precisely (`bank`);
    //   • the SAT bank is organized by exam domain with no unit to attach
    //     to, so it lands on the attribute as practice (`hubBank`).
    const evidence: BankEvidence = {};
    const hub: HubBankEvidence = {};

    const collect = (topic: BankTopicMeta, keyFor: (unit: string) => string, into: BankEvidence) => {
      const progress = loadBankProgress(topic.slug, userId);
      for (const form of topic.forms) {
        const p = progress.forms[form.id];
        if (!p || p.correct <= 0) continue;
        const key = keyFor(form.unit);
        const e = into[key] ?? { solvedForms: 0, solvedProblems: 0 };
        e.solvedForms++;
        e.solvedProblems += p.correct;
        into[key] = e;
      }
    };

    for (const topic of bankManifest()) {
      if (topic.courseLadder) {
        // Bank slug === /math course segment.
        collect(topic, (unit) => `course:${topic.slug}/${unit}`, evidence);
      } else if (topic.slug === "ib-sl" || topic.slug === "ib-hl") {
        // The IB banks' unit ids equal their course's unit slugs, so their
        // work counts exactly like course-ladder bank work.
        collect(topic, (unit) => `course:${topic.slug}/${unit}`, evidence);
      } else if (topic.slug === "sat") {
        collect(topic, (unit) => `sat/${unit}`, hub);
      }
    }

    setBank(evidence);
    setHubBank(hub);

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
        hubBank,
        placements,
        now: Date.now(),
      }),
    [perf.attempts, bank, hubBank, placements],
  );

  return { profile, status: perf.status };
}
