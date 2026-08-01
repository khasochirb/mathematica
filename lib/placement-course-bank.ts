// Named-course placement banks, HARVESTED from the problem bank: for every
// unit, one form per level (1/2/3), first variant. Bank variants are real
// MCQs with computed answers (sympy-gated at authoring), which makes them the
// right placement currency — unlike testYourself problems, which have no
// options. Variants that need a figure are skipped (the placement runner
// renders text + math only).
//
// SERVER-SIDE ONLY, because it reads the corpus (lib/bank-data.ts). Course
// placement PAGES call this in a server component and hand the ~40 harvested
// questions to the CoursePlacement client wrapper — the corpus itself never
// reaches the browser (lib/bank-split.test.ts enforces this).

import { getBankTopic } from "@/lib/bank-data";
import type { PlacementQuestion } from "@/lib/placement-bank";

const courseCache = new Map<string, PlacementQuestion[]>();

export function getCoursePlacementBank(courseSlug: string): PlacementQuestion[] {
  const cached = courseCache.get(courseSlug);
  if (cached) return cached;
  const topic = getBankTopic(courseSlug);
  if (!topic) return [];

  const titleByUnit = new Map(topic.units.map((u) => [u.id, u.title]));
  const bank: PlacementQuestion[] = [];
  for (const unit of topic.units) {
    for (const level of [1, 2, 3] as const) {
      const form = topic.forms.find(
        (f) => f.unit === unit.id && f.level === level && f.variants.some((v) => !v.geoFigure),
      );
      if (!form) continue;
      const v = form.variants.find((x) => !x.geoFigure)!;
      bank.push({
        id: `${unit.id}:d${level}`,
        topicSlug: unit.id,
        topicTitle: titleByUnit.get(unit.id) ?? unit.id,
        difficulty: level,
        prompt: v.statement,
        options: v.options,
        correctIndex: v.correctIndex,
        explanation: v.explanation,
      });
    }
  }
  courseCache.set(courseSlug, bank);
  return bank;
}
