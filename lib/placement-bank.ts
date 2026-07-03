// Placement-test question bank — a CURATED set with three genuine difficulty
// tiers per topic (1 = easy, 2 = medium, 3 = hard). Unlike harvesting lesson
// questions (whose difficulty was only guessed from position), these are hand-
// picked so the level a learner reaches is meaningful and the test visibly
// ramps up. Example, Equations: x+5=10 (easy) → 2x+7x=18 (medium) →
// 2x+3=11 (hard, two-step).

import { getGrade6Topics } from "@/lib/genmath-lessons";

export type PlacementQuestion = {
  id: string;
  topicSlug: string;
  topicTitle: string;
  difficulty: 1 | 2 | 3;
  prompt: string;
  options: string[];
  correctIndex: number;
  explanation: string;
};

type Curated = Omit<PlacementQuestion, "topicTitle">;

// Correct answer is always options[correctIndex]. Kept at index 0 in the source
// for authoring clarity; the runner shuffles option order at display time.
const Q = (
  topicSlug: string,
  difficulty: 1 | 2 | 3,
  prompt: string,
  options: string[],
  correctIndex: number,
  explanation: string
): Curated => ({ id: `${topicSlug}:d${difficulty}`, topicSlug, difficulty, prompt, options, correctIndex, explanation });

const CURATED: Curated[] = [
  // Ratios & Rates
  Q("ratios-and-rates", 1, "Write the ratio $4 : 8$ in simplest form.", ["$1 : 2$", "$2 : 4$", "$4 : 8$", "$1 : 4$"], 0, "Divide both parts by $4$: $4:8 = 1:2$."),
  Q("ratios-and-rates", 2, "If $3$ apples cost $\\$6$, what does one apple cost (the unit rate)?", ["$\\$2$", "$\\$3$", "$\\$18$", "$\\$1$"], 0, "$\\$6 \\div 3 = \\$2$ per apple."),
  Q("ratios-and-rates", 3, "A car travels $150$ miles in $3$ hours. At that rate, how far in $5$ hours?", ["$250$ miles", "$300$ miles", "$200$ miles", "$450$ miles"], 0, "Rate $= 150/3 = 50$ mph; $50 \\times 5 = 250$."),

  // Fractions
  Q("fractions", 1, "Simplify $\\tfrac{2}{6}$.", ["$\\tfrac{1}{3}$", "$\\tfrac{2}{6}$", "$\\tfrac{1}{2}$", "$\\tfrac{2}{3}$"], 0, "Divide top and bottom by $2$."),
  Q("fractions", 2, "Add: $\\tfrac{1}{2} + \\tfrac{1}{4}$.", ["$\\tfrac{3}{4}$", "$\\tfrac{2}{6}$", "$\\tfrac{1}{3}$", "$\\tfrac{2}{4}$"], 0, "$\\tfrac{1}{2} = \\tfrac{2}{4}$, so $\\tfrac{2}{4}+\\tfrac{1}{4}=\\tfrac{3}{4}$."),
  Q("fractions", 3, "Divide: $\\tfrac{2}{3} \\div \\tfrac{4}{9}$.", ["$\\tfrac{3}{2}$", "$\\tfrac{8}{27}$", "$\\tfrac{1}{2}$", "$\\tfrac{2}{3}$"], 0, "Multiply by the reciprocal: $\\tfrac{2}{3}\\times\\tfrac{9}{4}=\\tfrac{18}{12}=\\tfrac{3}{2}$."),

  // Decimals
  Q("decimals", 1, "Which is greater, $0.5$ or $0.05$?", ["$0.5$", "$0.05$", "They are equal", "Can't tell"], 0, "$0.5 = 0.50$, which is more than $0.05$."),
  Q("decimals", 2, "Add: $0.6 + 0.45$.", ["$1.05$", "$0.51$", "$1.5$", "$0.15$"], 0, "Line up the points: $0.60 + 0.45 = 1.05$."),
  Q("decimals", 3, "Multiply: $0.3 \\times 0.2$.", ["$0.06$", "$0.6$", "$0.5$", "$0.006$"], 0, "$3 \\times 2 = 6$, and two decimal places → $0.06$."),

  // Percentages
  Q("percentages", 1, "Find $50\\%$ of $20$.", ["$10$", "$5$", "$15$", "$40$"], 0, "$50\\%$ is half: $20 \\div 2 = 10$."),
  Q("percentages", 2, "Find $15\\%$ of $80$.", ["$12$", "$15$", "$8$", "$20$"], 0, "$\\tfrac{15}{100}\\times 80 = 12$."),
  Q("percentages", 3, "$12$ is what percent of $48$?", ["$25\\%$", "$4\\%$", "$36\\%$", "$40\\%$"], 0, "$\\tfrac{12}{48} = \\tfrac14 = 25\\%$."),

  // Integers
  Q("integers", 1, "Compute $-3 + 5$.", ["$2$", "$-2$", "$8$", "$-8$"], 0, "Start at $-3$ and move up $5$ → $2$."),
  Q("integers", 2, "Compute $-6 - 4$.", ["$-10$", "$-2$", "$10$", "$2$"], 0, "Subtracting moves further down: $-6-4 = -10$."),
  Q("integers", 3, "Compute $-4 \\times -3 + 2$.", ["$14$", "$-10$", "$-14$", "$10$"], 0, "Multiply first: $-4\\times-3 = 12$; then $12 + 2 = 14$."),

  // Factors and Multiples
  Q("factors-and-multiples", 1, "Which of these is a factor of $12$?", ["$3$", "$5$", "$7$", "$8$"], 0, "$12 \\div 3 = 4$ exactly, so $3$ is a factor."),
  Q("factors-and-multiples", 2, "Find the GCF of $12$ and $18$.", ["$6$", "$3$", "$2$", "$12$"], 0, "Largest number dividing both is $6$."),
  Q("factors-and-multiples", 3, "Find the LCM of $4$ and $6$.", ["$12$", "$24$", "$6$", "$2$"], 0, "Smallest number both divide into is $12$."),

  // Expressions and Equations
  Q("expressions-and-equations", 1, "Solve $x + 5 = 10$.", ["$x = 5$", "$x = 15$", "$x = 2$", "$x = 50$"], 0, "Subtract $5$ from both sides: $x = 5$."),
  Q("expressions-and-equations", 2, "Solve $2x + 7x = 18$.", ["$x = 2$", "$x = 9$", "$x = 4$", "$x = 16$"], 0, "Combine like terms: $9x = 18$, so $x = 2$."),
  Q("expressions-and-equations", 3, "Solve $2x + 3 = 11$.", ["$x = 4$", "$x = 7$", "$x = 5$", "$x = 28$"], 0, "Subtract $3$: $2x = 8$; divide by $2$: $x = 4$."),

  // Coordinate Plane
  Q("coordinate-plane", 1, "Which quadrant is the point $(2, 3)$ in?", ["Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV"], 0, "Both coordinates positive → Quadrant I."),
  Q("coordinate-plane", 2, "Which quadrant is the point $(-4, 2)$ in?", ["Quadrant II", "Quadrant I", "Quadrant III", "Quadrant IV"], 0, "Left ($x<0$), up ($y>0$) → Quadrant II."),
  Q("coordinate-plane", 3, "Reflect the point $(3, -5)$ over the x-axis.", ["$(3, 5)$", "$(-3, -5)$", "$(-3, 5)$", "$(5, 3)$"], 0, "Over the x-axis the y-coordinate flips sign: $(3, 5)$."),

  // Geometry: Area and Volume
  Q("geometry-area-volume", 1, "Find the area of a rectangle $4$ by $5$.", ["$20$", "$9$", "$18$", "$40$"], 0, "Area $= 4 \\times 5 = 20$."),
  Q("geometry-area-volume", 2, "Find the area of a triangle with base $6$ and height $4$.", ["$12$", "$24$", "$10$", "$20$"], 0, "Area $= \\tfrac12 \\times 6 \\times 4 = 12$."),
  Q("geometry-area-volume", 3, "Find the volume of a box $2 \\times 3 \\times 4$.", ["$24$", "$9$", "$20$", "$14$"], 0, "Volume $= 2 \\times 3 \\times 4 = 24$."),

  // Data and Statistics
  Q("data-and-statistics", 1, "Find the mean (average) of $2, 4, 6$.", ["$4$", "$6$", "$12$", "$3$"], 0, "$(2+4+6)\\div 3 = 12\\div 3 = 4$."),
  Q("data-and-statistics", 2, "Find the median of $3, 7, 5, 9, 1$.", ["$5$", "$7$", "$3$", "$9$"], 0, "Sorted: $1,3,5,7,9$; the middle value is $5$."),
  Q("data-and-statistics", 3, "Find the mean of $4, 8, 10, 2$.", ["$6$", "$8$", "$24$", "$5$"], 0, "$(4+8+10+2)\\div 4 = 24\\div 4 = 6$."),
];

let cache: PlacementQuestion[] | null = null;

export function getPlacementBank(): PlacementQuestion[] {
  if (cache) return cache;
  const titleBySlug = new Map(getGrade6Topics().map((t) => [t.slug, t.title]));
  cache = CURATED.map((q) => ({ ...q, topicTitle: titleBySlug.get(q.topicSlug) ?? q.topicSlug }));
  return cache;
}

// A stable, per-question shuffle of the answer options (the source keeps the
// correct answer at index 0 for authoring). Deterministic from the id so it
// doesn't reshuffle on re-render. Returns the display options, the correct
// index within them, and a map back to the original indices.
export function displayQuestion(q: PlacementQuestion): {
  options: string[];
  correctIndex: number;
  toOriginal: number[];
} {
  const n = q.options.length;
  const order = q.options.map((_, i) => i);
  let seed = 2166136261;
  for (const c of q.id) seed = (Math.imul(seed ^ c.charCodeAt(0), 16777619) >>> 0);
  for (let i = n - 1; i > 0; i--) {
    seed = (Math.imul(seed, 1103515245) + 12345) & 0x7fffffff;
    const j = seed % (i + 1);
    [order[i], order[j]] = [order[j], order[i]];
  }
  return {
    options: order.map((k) => q.options[k]),
    correctIndex: order.indexOf(q.correctIndex),
    toOriginal: order,
  };
}

// The topics that have placement questions, in the order they first appear.
export function placementTopics(bank = getPlacementBank()): { slug: string; title: string; count: number }[] {
  const map = new Map<string, { slug: string; title: string; count: number }>();
  for (const q of bank) {
    const cur = map.get(q.topicSlug);
    if (cur) cur.count++;
    else map.set(q.topicSlug, { slug: q.topicSlug, title: q.topicTitle, count: 1 });
  }
  return Array.from(map.values());
}
