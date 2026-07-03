// Placement-test question bank — a CURATED set with three genuine difficulty
// tiers per topic (1 = easy, 2 = medium, 3 = hard). Unlike harvesting lesson
// questions (whose difficulty was only guessed from position), these are hand-
// picked so the level a learner reaches is meaningful and the test visibly
// ramps up. Example, Equations: x+5=10 (easy) → 2x+7x=18 (medium) →
// 2x+3=11 (hard, two-step).

import { getGrade6Topics, getGeometrySpine } from "@/lib/genmath-lessons";

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

// ---------------------------------------------------------------------------
// Geometry course — one tiered question per difficulty for each of the 13 units.
// ---------------------------------------------------------------------------
const GEO_CURATED: Curated[] = [
  // 1. Foundations: Points, Lines & Angles
  Q("foundations", 1, "An angle measures $40^\\circ$. What type of angle is it?", ["Acute", "Right", "Obtuse", "Straight"], 0, "An angle below $90^\\circ$ is acute."),
  Q("foundations", 2, "Two angles are complementary and one is $35^\\circ$. What is the other?", ["$55^\\circ$", "$65^\\circ$", "$145^\\circ$", "$325^\\circ$"], 0, "Complementary angles add to $90^\\circ$: $90 - 35 = 55$."),
  Q("foundations", 3, "Ray $OC$ bisects $\\angle AOB = 80^\\circ$. What is $m\\angle AOC$?", ["$40^\\circ$", "$160^\\circ$", "$20^\\circ$", "$80^\\circ$"], 0, "A bisector halves the angle: $80 \\div 2 = 40$."),

  // 2. Reasoning & Proof
  Q("reasoning-and-proof", 1, "In \"If it rains, then the ground is wet,\" what is the hypothesis?", ["It rains", "The ground is wet", "It is dry", "There is no hypothesis"], 0, "The hypothesis is the \"if\" part."),
  Q("reasoning-and-proof", 2, "A single example that makes a statement false is called a —", ["Counterexample", "Conjecture", "Theorem", "Postulate"], 0, "One counterexample disproves a general claim."),
  Q("reasoning-and-proof", 3, "What is the converse of \"If $p$, then $q$\"?", ["If $q$, then $p$", "If not $p$, then not $q$", "If not $q$, then not $p$", "If $p$, then not $q$"], 0, "The converse swaps hypothesis and conclusion."),

  // 3. Parallel & Perpendicular Lines
  Q("parallel-and-perpendicular", 1, "Two parallel lines are cut by a transversal. Corresponding angles are —", ["Equal", "Supplementary", "Complementary", "Unrelated"], 0, "Corresponding angles are congruent."),
  Q("parallel-and-perpendicular", 2, "Parallel lines cut by a transversal make one interior angle $70^\\circ$. Its same-side interior angle is —", ["$110^\\circ$", "$70^\\circ$", "$20^\\circ$", "$90^\\circ$"], 0, "Same-side interior angles are supplementary: $180 - 70 = 110$."),
  Q("parallel-and-perpendicular", 3, "Alternate interior angles measure $3x$ and $x + 40$. Find $x$.", ["$20$", "$10$", "$40$", "$30$"], 0, "They're equal: $3x = x + 40 \\Rightarrow x = 20$."),

  // 4. Triangles & Congruence
  Q("triangles-and-congruence", 1, "The three angles of a triangle add up to —", ["$180^\\circ$", "$360^\\circ$", "$90^\\circ$", "$270^\\circ$"], 0, "Every triangle's angles sum to $180^\\circ$."),
  Q("triangles-and-congruence", 2, "A triangle has angles $50^\\circ$ and $60^\\circ$. The third angle is —", ["$70^\\circ$", "$80^\\circ$", "$90^\\circ$", "$110^\\circ$"], 0, "$180 - 50 - 60 = 70$."),
  Q("triangles-and-congruence", 3, "Which shortcut proves congruence from two sides and the angle BETWEEN them?", ["SAS", "SSA", "AAA", "ASA"], 0, "Side-Angle-Side: the angle is included between the two sides."),

  // 5. Relationships in Triangles
  Q("relationships-in-triangles", 1, "A segment from a vertex to the midpoint of the opposite side is a —", ["Median", "Altitude", "Angle bisector", "Tangent"], 0, "A median goes to the midpoint of the opposite side."),
  Q("relationships-in-triangles", 2, "A triangle's midsegment is how long compared to the third side?", ["Half", "Equal", "Twice", "One third"], 0, "The midsegment is half the length of the parallel side."),
  Q("relationships-in-triangles", 3, "In any triangle, the longest side is opposite the —", ["Largest angle", "Smallest angle", "Right angle", "Midpoint"], 0, "Bigger angle → longer opposite side."),

  // 6. Quadrilaterals & Polygons
  Q("quadrilaterals-and-polygons", 1, "The four angles of a quadrilateral add up to —", ["$360^\\circ$", "$180^\\circ$", "$540^\\circ$", "$90^\\circ$"], 0, "A quadrilateral splits into two triangles: $2 \\times 180 = 360$."),
  Q("quadrilaterals-and-polygons", 2, "What is the interior angle sum of a pentagon ($5$ sides)?", ["$540^\\circ$", "$360^\\circ$", "$720^\\circ$", "$450^\\circ$"], 0, "$(5-2)\\times 180 = 540$."),
  Q("quadrilaterals-and-polygons", 3, "Opposite angles of a parallelogram are $3x$ and $x + 50$. Find $x$.", ["$25$", "$20$", "$50$", "$30$"], 0, "Opposite angles are equal: $3x = x + 50 \\Rightarrow x = 25$."),

  // 7. Similarity
  Q("similarity", 1, "Similar figures always have the same shape but may differ in —", ["Size", "Angle measures", "Number of sides", "Type"], 0, "Similar = same shape (equal angles), possibly different size."),
  Q("similarity", 2, "Two similar triangles have scale factor $3$. A side of $4$ in the small one becomes —", ["$12$", "$7$", "$\\tfrac{4}{3}$", "$1$"], 0, "$4 \\times 3 = 12$."),
  Q("similarity", 3, "Similar triangles give $\\tfrac{6}{9} = \\tfrac{8}{x}$. Find $x$.", ["$12$", "$5$", "$6$", "$11$"], 0, "Cross-multiply: $6x = 72 \\Rightarrow x = 12$."),

  // 8. Right Triangles & Trigonometry
  Q("right-triangles-and-trig", 1, "A right triangle has legs $3$ and $4$. The hypotenuse is —", ["$5$", "$7$", "$1$", "$12$"], 0, "$\\sqrt{3^2+4^2} = \\sqrt{25} = 5$."),
  Q("right-triangles-and-trig", 2, "A right triangle has legs $5$ and $12$. The hypotenuse is —", ["$13$", "$17$", "$7$", "$60$"], 0, "$\\sqrt{25+144} = \\sqrt{169} = 13$."),
  Q("right-triangles-and-trig", 3, "A $45\\text{-}45\\text{-}90$ triangle has legs of $5$. The hypotenuse is —", ["$5\\sqrt{2}$", "$10$", "$5$", "$25$"], 0, "In a $45\\text{-}45\\text{-}90$, hypotenuse $=$ leg $\\times \\sqrt{2}$."),

  // 9. Circles
  Q("circles", 1, "The distance straight across a circle through its center is the —", ["Diameter", "Radius", "Chord", "Arc"], 0, "The diameter passes through the center."),
  Q("circles", 2, "A central angle of $80^\\circ$ cuts off an arc measuring —", ["$80^\\circ$", "$40^\\circ$", "$160^\\circ$", "$100^\\circ$"], 0, "A central angle equals its intercepted arc."),
  Q("circles", 3, "An inscribed angle intercepts an arc of $100^\\circ$. The angle measures —", ["$50^\\circ$", "$100^\\circ$", "$200^\\circ$", "$25^\\circ$"], 0, "An inscribed angle is half its arc: $100 \\div 2 = 50$."),

  // 10. Area & Perimeter
  Q("area-and-perimeter", 1, "The area of a $5$-by-$6$ rectangle is —", ["$30$", "$11$", "$22$", "$36$"], 0, "Area $= 5 \\times 6 = 30$."),
  Q("area-and-perimeter", 2, "A triangle has base $10$ and height $8$. Its area is —", ["$40$", "$80$", "$18$", "$20$"], 0, "Area $= \\tfrac12 \\times 10 \\times 8 = 40$."),
  Q("area-and-perimeter", 3, "The area of a circle with radius $3$ (in terms of $\\pi$) is —", ["$9\\pi$", "$6\\pi$", "$3\\pi$", "$9$"], 0, "Area $= \\pi r^2 = 9\\pi$."),

  // 11. Surface Area & Volume
  Q("surface-area-and-volume", 1, "The volume of a $2 \\times 3 \\times 5$ box is —", ["$30$", "$10$", "$31$", "$25$"], 0, "Volume $= 2 \\times 3 \\times 5 = 30$."),
  Q("surface-area-and-volume", 2, "A cylinder has radius $2$ and height $5$. Its volume (in terms of $\\pi$) is —", ["$20\\pi$", "$10\\pi$", "$40\\pi$", "$20$"], 0, "$V = \\pi r^2 h = \\pi(4)(5) = 20\\pi$."),
  Q("surface-area-and-volume", 3, "A cone has radius $3$ and height $4$. Its volume (in terms of $\\pi$) is —", ["$12\\pi$", "$36\\pi$", "$4\\pi$", "$24\\pi$"], 0, "$V = \\tfrac13 \\pi r^2 h = \\tfrac13\\pi(9)(4) = 12\\pi$."),

  // 12. Transformations
  Q("transformations", 1, "Sliding a figure without turning or flipping it is a —", ["Translation", "Rotation", "Reflection", "Dilation"], 0, "A translation is a slide."),
  Q("transformations", 2, "Reflect the point $(4, 2)$ over the x-axis.", ["$(4, -2)$", "$(-4, 2)$", "$(2, 4)$", "$(-4, -2)$"], 0, "Over the x-axis the y-coordinate flips sign."),
  Q("transformations", 3, "Rotate the point $(3, 1)$ by $90^\\circ$ about the origin.", ["$(-1, 3)$", "$(1, -3)$", "$(-3, -1)$", "$(3, -1)$"], 0, "$(x, y) \\to (-y, x)$, so $(3,1) \\to (-1,3)$."),

  // 13. Coordinate Geometry
  Q("coordinate-geometry", 1, "The distance from $(0,0)$ to $(3,4)$ is —", ["$5$", "$7$", "$25$", "$1$"], 0, "$\\sqrt{3^2+4^2} = 5$."),
  Q("coordinate-geometry", 2, "The midpoint of $(2,4)$ and $(8,10)$ is —", ["$(5, 7)$", "$(10, 14)$", "$(3, 2)$", "$(6, 6)$"], 0, "Average each coordinate: $(5, 7)$."),
  Q("coordinate-geometry", 3, "The slope of the line through $(1,2)$ and $(4,11)$ is —", ["$3$", "$\\tfrac{1}{3}$", "$-3$", "$9$"], 0, "$\\tfrac{11-2}{4-1} = \\tfrac{9}{3} = 3$."),
];

let cache: PlacementQuestion[] | null = null;
let geoCache: PlacementQuestion[] | null = null;

export function getPlacementBank(): PlacementQuestion[] {
  if (cache) return cache;
  const titleBySlug = new Map(getGrade6Topics().map((t) => [t.slug, t.title]));
  cache = CURATED.map((q) => ({ ...q, topicTitle: titleBySlug.get(q.topicSlug) ?? q.topicSlug }));
  return cache;
}

export function getGeometryPlacementBank(): PlacementQuestion[] {
  if (geoCache) return geoCache;
  const titleBySlug = new Map(getGeometrySpine().map((u) => [u.slug, u.title]));
  geoCache = GEO_CURATED.map((q) => ({ ...q, topicTitle: titleBySlug.get(q.topicSlug) ?? q.topicSlug }));
  return geoCache;
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
