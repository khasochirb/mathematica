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

import { getBankMirrorMn, getBankTopic } from "@/lib/bank-data";
import type { PlacementQuestion } from "@/lib/placement-bank";

// One harvested question plus where it came from, so the Mongolian twin can
// pick the very same variant out of the mirror.
type Pick = { q: PlacementQuestion; formId: string; variantId: string };

const pickCache = new Map<string, Pick[]>();

function harvest(courseSlug: string): Pick[] {
  const cached = pickCache.get(courseSlug);
  if (cached) return cached;
  const topic = getBankTopic(courseSlug);
  if (!topic) return [];

  const titleByUnit = new Map(topic.units.map((u) => [u.id, u.title]));
  const picks: Pick[] = [];
  for (const unit of topic.units) {
    for (const level of [1, 2, 3] as const) {
      const form = topic.forms.find(
        (f) => f.unit === unit.id && f.level === level && f.variants.some((v) => !v.geoFigure),
      );
      if (!form) continue;
      const v = form.variants.find((x) => !x.geoFigure)!;
      picks.push({
        formId: form.id,
        variantId: v.id,
        q: {
          id: `${unit.id}:d${level}`,
          topicSlug: unit.id,
          topicTitle: titleByUnit.get(unit.id) ?? unit.id,
          difficulty: level,
          prompt: v.statement,
          options: v.options,
          correctIndex: v.correctIndex,
          explanation: v.explanation,
        },
      });
    }
  }
  pickCache.set(courseSlug, picks);
  return picks;
}

const courseCache = new Map<string, PlacementQuestion[]>();

export function getCoursePlacementBank(courseSlug: string): PlacementQuestion[] {
  const cached = courseCache.get(courseSlug);
  if (cached) return cached;
  const bank = harvest(courseSlug).map((p) => p.q);
  courseCache.set(courseSlug, bank);
  return bank;
}

const mnCache = new Map<string, PlacementQuestion[] | null>();

/**
 * The Mongolian twin of getCoursePlacementBank: the SAME variants (same ids,
 * same correctIndex, same topicSlug), carrying the mirror's statement,
 * options, explanation and unit title. Null when the course has no Mongolian
 * mirror, or when any picked variant is missing from it or disagrees on its
 * option count: a half-Mongolian sitting is worse than an English one, and
 * the page simply stays English.
 */
export function getCoursePlacementBankMn(courseSlug: string): PlacementQuestion[] | null {
  if (mnCache.has(courseSlug)) return mnCache.get(courseSlug)!;
  const mn = getBankMirrorMn(courseSlug);
  const picks = harvest(courseSlug);
  let out: PlacementQuestion[] | null = null;
  if (mn && picks.length > 0) {
    const unitTitle = new Map(mn.units.map((u) => [u.id, u.title]));
    // Keyed by unit AND id: form ids are not unique across units (integrated-1
    // ships "im1-slope-two-points" in two units).
    const forms = new Map(mn.forms.map((f) => [`${f.unit}|${f.id}`, f]));
    out = [];
    for (const p of picks) {
      const v = forms.get(`${p.q.topicSlug}|${p.formId}`)?.variants.find((x) => x.id === p.variantId);
      if (!v || v.options.length !== p.q.options.length || v.correctIndex !== p.q.correctIndex) {
        out = null;
        break;
      }
      out.push({
        ...p.q,
        topicTitle: unitTitle.get(p.q.topicSlug) ?? p.q.topicTitle,
        prompt: v.statement,
        options: v.options,
        explanation: v.explanation,
      });
    }
  }
  mnCache.set(courseSlug, out);
  return out;
}

/** The Mongolian course title from the mirror, or null without one. */
export function getCourseTitleMn(courseSlug: string): string | null {
  return getBankMirrorMn(courseSlug)?.title ?? null;
}
