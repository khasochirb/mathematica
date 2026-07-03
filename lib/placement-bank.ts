// Placement-test question bank — harvested from the auto-gradeable multiple-
// choice questions already embedded in the Grade-6 lessons (the tapQuestion
// "quick check" steps and the tryItSet practice problems). Each carries
// options + a correctIndex, so it can be machine-graded. We tag every question
// with its topic and a 1–3 difficulty derived from where it sits in the course.

import { getGrade6Topics } from "@/lib/genmath-lessons";
import type { InteractiveStep } from "@/lib/genmath-interactive";

export type PlacementQuestion = {
  id: string;
  topicSlug: string;
  topicTitle: string;
  lessonSlug: string;
  difficulty: 1 | 2 | 3;
  prompt: string;
  options: string[];
  correctIndex: number;
  explanation: string;
};

// Difficulty rises through a topic: early lessons are easier, later ones harder,
// and the cumulative "Chapter/Mixed practice" sets bump up a level.
function difficultyFor(lessonIdx: number, lessonCount: number, eyebrow?: string): 1 | 2 | 3 {
  const frac = lessonCount > 1 ? lessonIdx / (lessonCount - 1) : 0.5;
  let d = frac < 0.34 ? 1 : frac < 0.67 ? 2 : 3;
  const ey = (eyebrow ?? "").toLowerCase();
  if (ey.includes("chapter") || ey.includes("mixed")) d = Math.min(3, d + 1);
  return d as 1 | 2 | 3;
}

let cache: PlacementQuestion[] | null = null;

export function getPlacementBank(): PlacementQuestion[] {
  if (cache) return cache;
  const out: PlacementQuestion[] = [];
  for (const topic of getGrade6Topics()) {
    const lessons = topic.lessons ?? [];
    lessons.forEach((lesson, li) => {
      const steps: InteractiveStep[] = lesson.interactive?.steps ?? [];
      steps.forEach((step, si) => {
        if (step.kind === "tapQuestion" && Array.isArray(step.options) && step.options.length >= 2) {
          out.push({
            id: `${topic.slug}:${lesson.slug}:tq${si}`,
            topicSlug: topic.slug,
            topicTitle: topic.title,
            lessonSlug: lesson.slug,
            difficulty: difficultyFor(li, lessons.length, step.eyebrow),
            prompt: step.prompt,
            options: step.options,
            correctIndex: step.correctIndex,
            explanation: step.explanation,
          });
        } else if (step.kind === "tryItSet") {
          step.problems.forEach((p, pi) => {
            if (Array.isArray(p.options) && p.options.length >= 2) {
              out.push({
                id: `${topic.slug}:${lesson.slug}:ts${si}_${pi}`,
                topicSlug: topic.slug,
                topicTitle: topic.title,
                lessonSlug: lesson.slug,
                difficulty: difficultyFor(li, lessons.length, step.eyebrow),
                prompt: p.prompt,
                options: p.options,
                correctIndex: p.correctIndex,
                explanation: p.explanation,
              });
            }
          });
        }
      });
    });
  }
  cache = out;
  return out;
}

// The topics that actually have gradeable questions (some intro topics don't),
// with a count — used to build and validate the adaptive test.
export function placementTopics(bank = getPlacementBank()): { slug: string; title: string; count: number }[] {
  const map = new Map<string, { slug: string; title: string; count: number }>();
  for (const q of bank) {
    const cur = map.get(q.topicSlug);
    if (cur) cur.count++;
    else map.set(q.topicSlug, { slug: q.topicSlug, title: q.topicTitle, count: 1 });
  }
  return Array.from(map.values());
}
