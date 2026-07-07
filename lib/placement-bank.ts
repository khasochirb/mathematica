// Placement-test question bank — a CURATED set with three genuine difficulty
// tiers per topic (1 = easy, 2 = medium, 3 = hard). Unlike harvesting lesson
// questions (whose difficulty was only guessed from position), these are hand-
// picked so the level a learner reaches is meaningful and the test visibly
// ramps up. Example, Equations: x+5=10 (easy) → 2x+7x=18 (medium) →
// 2x+3=11 (hard, two-step).

import { getGrade6Topics, getGeometrySpine, getGrade7Spine, getGrade8Spine, getGrade9Spine, getGrade10Spine, getGrade11Spine, getGrade12Spine } from "@/lib/genmath-lessons";

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


// Grade 8 — 7 topics × 3 genuine tiers.
const G8_CURATED: Curated[] = [
  // 1. The Real Number System
  Q("the-real-number-system", 1, "Write $0.75$ as a fraction in lowest terms.", ["$\\tfrac{3}{4}$", "$\\tfrac{75}{100}$", "$\\tfrac{7}{5}$", "$\\tfrac{1}{4}$"], 0, "$0.75 = \\tfrac{75}{100} = \\tfrac{3}{4}$."),
  Q("the-real-number-system", 2, "Which number is irrational?", ["$\\sqrt{2}$", "$\\sqrt{9}$", "$0.\\overline{3}$", "$\\tfrac{7}{2}$"], 0, "$2$ isn't a perfect square, so $\\sqrt{2}$ never terminates or repeats."),
  Q("the-real-number-system", 3, "Between which two whole numbers does $\\sqrt{50}$ lie?", ["$7$ and $8$", "$6$ and $7$", "$24$ and $26$", "$8$ and $9$"], 0, "$7^2 = 49 < 50 < 64 = 8^2$."),

  // 2. Exponents & Scientific Notation
  Q("exponents-and-scientific-notation", 1, "Simplify $2^3 \\cdot 2^4$ as a single power.", ["$2^7$", "$2^{12}$", "$4^7$", "$2^1$"], 0, "Same base: add the exponents."),
  Q("exponents-and-scientific-notation", 2, "Evaluate $5^{-2}$.", ["$\\tfrac{1}{25}$", "$-25$", "$-10$", "$\\tfrac{1}{10}$"], 0, "A negative exponent flips: $5^{-2} = \\tfrac{1}{5^2}$."),
  Q("exponents-and-scientific-notation", 3, "Compute $(3\\times10^4)(2\\times10^3)$ in scientific notation.", ["$6\\times10^7$", "$6\\times10^{12}$", "$5\\times10^7$", "$6\\times10^1$"], 0, "Multiply the fronts, add the exponents: $6\\times10^{4+3}$."),

  // 3. Square & Cube Roots
  Q("roots", 1, "Evaluate $\\sqrt{81}$.", ["$9$", "$40.5$", "$8$", "$81$"], 0, "$9^2 = 81$."),
  Q("roots", 2, "Solve $x^2 = 49$.", ["$x = \\pm 7$", "$x = 7$ only", "$x = 24.5$", "$x = \\pm 24.5$"], 0, "Both $7^2$ and $(-7)^2$ equal $49$."),
  Q("roots", 3, "Simplify $\\sqrt{50}$.", ["$5\\sqrt{2}$", "$25\\sqrt{2}$", "$2\\sqrt{5}$", "$10\\sqrt{5}$"], 0, "$\\sqrt{50} = \\sqrt{25\\cdot2} = 5\\sqrt{2}$."),

  // 4. Linear Equations
  Q("linear-equations", 1, "Solve $2x + 3 = 11$.", ["$x = 4$", "$x = 7$", "$x = 14$", "$x = 5$"], 0, "Subtract 3, divide by 2."),
  Q("linear-equations", 2, "Solve $5x + 2 = 3x + 10$.", ["$x = 4$", "$x = 6$", "$x = 1$", "$x = 12$"], 0, "Collect: $2x = 8$, so $x = 4$."),
  Q("linear-equations", 3, "How many solutions does $2(x+3) = 2x + 6$ have?", ["Infinitely many", "None", "Exactly one", "Exactly two"], 0, "Both sides simplify to the same expression — every $x$ works."),

  // 5. Linear Functions
  Q("linear-functions", 1, "The rule is $y = 2x + 1$. The output for $x = 3$ is —", ["$7$", "$6$", "$9$", "$5$"], 0, "$2(3)+1 = 7$."),
  Q("linear-functions", 2, "The slope through $(1,2)$ and $(5,10)$ is —", ["$2$", "$\\tfrac{1}{2}$", "$8$", "$4$"], 0, "$\\tfrac{10-2}{5-1} = 2$."),
  Q("linear-functions", 3, "A table reads $(0,7), (1,9), (2,11)$. Its equation is —", ["$y = 2x + 7$", "$y = 7x + 2$", "$y = 2x + 9$", "$y = 9x$"], 0, "Jump of 2 per step; value 7 at $x=0$."),

  // 6. Systems of Linear Equations
  Q("systems-of-linear-equations", 1, "Is $(5,2)$ a solution of $x+y=7$ AND $x-y=3$?", ["Yes — it satisfies both", "No — it fails the first", "No — it fails the second", "Only if $x = 2$"], 0, "$5+2=7$ ✓ and $5-2=3$ ✓."),
  Q("systems-of-linear-equations", 2, "Solve: $y = x + 3$ and $x + y = 9$.", ["$(3, 6)$", "$(6, 3)$", "$(4, 5)$", "$(9, 3)$"], 0, "Substitute: $x + (x+3) = 9$, so $x = 3$, $y = 6$."),
  Q("systems-of-linear-equations", 3, "How many solutions: $y = 2x + 1$ and $y = 2x - 3$?", ["None — parallel lines", "One", "Infinitely many", "Two"], 0, "Same slope, different intercepts — the lines never meet."),

  // 7. Scatter Plots & Bivariate Data
  Q("scatter-plots-and-bivariate-data", 1, "(hours studied, test score): the cloud of dots climbs ↗. Correlation?", ["Positive", "Negative", "None", "Impossible to tell"], 0, "Larger $x$ with larger $y$ — the cloud tilts up."),
  Q("scatter-plots-and-bivariate-data", 2, "Points $(1,1),(2,2),(3,3),(8,0)$: the outlier is —", ["$(8,0)$", "$(3,3)$", "$(1,1)$", "there is none"], 0, "Three points sit on $y=x$; $(8,0)$ is far off that pattern."),
  Q("scatter-plots-and-bivariate-data", 3, "Trend line $y = 0.75x + 2.5$: the prediction at $x = 6$ is —", ["$7$", "$6.25$", "$4.5$", "$9.25$"], 0, "$0.75(6) + 2.5 = 7$."),
];

// Grade 10 — 7 topics × 3 genuine tiers.
const G10_CURATED: Curated[] = [
  // 1. Polynomials & Factoring
  Q("polynomials-and-factoring", 1, "Expand $(x+2)(x+5)$.", ["$x^2 + 7x + 10$", "$x^2 + 10x + 7$", "$x^2 + 10$", "$2x + 7$"], 0, "FOIL: $x^2 + 5x + 2x + 10$."),
  Q("polynomials-and-factoring", 2, "Factor $x^2 - 25$.", ["$(x+5)(x-5)$", "$(x-5)^2$", "$(x+5)^2$", "$x(x - 25)$"], 0, "Difference of squares: $a^2 - b^2 = (a+b)(a-b)$."),
  Q("polynomials-and-factoring", 3, "Solve $x^2 + 4x = 21$.", ["$x = 3$ or $x = -7$", "$x = -3$ or $x = 7$", "$x = 21$ or $x = 0$", "$x = 3$ only"], 0, "$x^2+4x-21 = (x+7)(x-3) = 0$."),

  // 2. Quadratic Equations
  Q("quadratic-equations", 1, "Solve $x^2 = 64$.", ["$x = \\pm 8$", "$x = 8$ only", "$x = 32$", "$x = \\pm 32$"], 0, "Both $8^2$ and $(-8)^2$ equal $64$."),
  Q("quadratic-equations", 2, "Solve $(x-3)^2 = 25$.", ["$x = 8$ or $x = -2$", "$x = \\pm 5$", "$x = 8$ only", "$x = 28$"], 0, "$x - 3 = \\pm 5$: $x = 8$ or $-2$."),
  Q("quadratic-equations", 3, "How many real solutions does $x^2 + 2x + 5 = 0$ have?", ["None", "One", "Two", "Infinitely many"], 0, "Discriminant $4 - 20 = -16 < 0$: no real roots."),

  // 3. Quadratic Functions & Parabolas
  Q("quadratic-functions", 1, "The graph of $y = -2x^2$ opens —", ["down, narrower than $y=x^2$", "up, narrower", "down, wider", "up, wider"], 0, "$a = -2$: negative flips it down; $|a| = 2 > 1$ narrows it."),
  Q("quadratic-functions", 2, "The vertex of $y = (x-4)^2 + 3$ is —", ["$(4, 3)$", "$(-4, 3)$", "$(4, -3)$", "$(3, 4)$"], 0, "Vertex form: the bracket dies at $x = 4$, $k = 3$."),
  Q("quadratic-functions", 3, "The vertex of $y = x^2 - 6x + 1$ is —", ["$(3, -8)$", "$(-3, 8)$", "$(6, 1)$", "$(3, 1)$"], 0, "Axis $x = 6/2 = 3$; $y(3) = 9 - 18 + 1 = -8$."),

  // 4. Rational Expressions & Equations
  Q("rational-expressions", 1, "The excluded value of $\\tfrac{x+1}{x-4}$ is —", ["$x = 4$", "$x = -1$", "$x = 0$", "$x = -4$"], 0, "The denominator dies at $x = 4$; a zero TOP is fine."),
  Q("rational-expressions", 2, "Simplify $\\tfrac{x^2-9}{x+3}$.", ["$x - 3$", "$x + 3$", "$x - 9$", "it can't simplify"], 0, "$(x+3)(x-3)$ over $(x+3)$."),
  Q("rational-expressions", 3, "A painter takes 6 h alone, a helper 3 h. Together they take —", ["$2$ h", "$4.5$ h", "$9$ h", "$3$ h"], 0, "Rates add: $\\tfrac16 + \\tfrac13 = \\tfrac12$ job/hour → 2 hours."),

  // 5. Radicals & Rational Exponents
  Q("radicals-and-rational-exponents", 1, "Simplify $\\sqrt{72}$.", ["$6\\sqrt{2}$", "$2\\sqrt{6}$", "$36\\sqrt{2}$", "$8\\sqrt{3}$"], 0, "$72 = 36 \\cdot 2$."),
  Q("radicals-and-rational-exponents", 2, "Evaluate $8^{2/3}$.", ["$4$", "$16$", "$\\tfrac{16}{3}$", "$6$"], 0, "Cube root of 8 is 2; squared is 4."),
  Q("radicals-and-rational-exponents", 3, "Solve $\\sqrt{x} = x - 2$.", ["$x = 4$ only", "$x = 4$ or $x = 1$", "$x = 1$ only", "no solution"], 0, "Squaring gives $x = 4$ or $1$, but $\\sqrt1 \\neq -1$: $1$ is extraneous."),

  // 6. Exponential Functions & Growth
  Q("exponential-functions", 1, "Evaluate $y = 3 \\cdot 2^x$ at $x = 4$.", ["$48$", "$1296$", "$24$", "$36$"], 0, "$2^4 = 16$, then $\\times 3$."),
  Q("exponential-functions", 2, "A phone loses $20\\%$ of its value yearly. The yearly factor is —", ["$0.8$", "$0.2$", "$1.2$", "$-0.2$"], 0, "Keep $80\\%$: multiply by $0.8$ each year."),
  Q("exponential-functions", 3, "$1000$ at $10\\%$ compounded yearly is worth, after 2 years —", ["$1210$", "$1200$", "$1100$", "$1020$"], 0, "$1000(1.1)^2 = 1210$ — the extra 10 is interest on interest."),

  // 7. Probability & Counting
  Q("probability-and-counting", 1, "4 shirts and 3 pants make how many outfits?", ["$12$", "$7$", "$4^3$", "$1$"], 0, "Each shirt pairs with each pant: $4 \\times 3$."),
  Q("probability-and-counting", 2, "How many 2-person teams can 8 people form?", ["$28$", "$56$", "$16$", "$64$"], 0, "Order-blind: $_8C_2 = \\tfrac{8 \\cdot 7}{2} = 28$."),
  Q("probability-and-counting", 3, "Two dice: $P(\\text{at least one six})$ = —", ["$\\tfrac{11}{36}$", "$\\tfrac{1}{36}$", "$\\tfrac{1}{3}$", "$\\tfrac{2}{6}$"], 0, "$1 - (\\tfrac56)^2 = \\tfrac{11}{36}$."),
];

// Grade 11 — 7 topics × 3 genuine tiers.
const G11_CURATED: Curated[] = [
  // 1. Functions & Transformations
  Q("functions-and-transformations", 1, "If $f(x) = x^2 + 1$, then $f(3)$ = —", ["$10$", "$7$", "$9$", "$16$"], 0, "$3^2 + 1 = 10$."),
  Q("functions-and-transformations", 2, "The graph of $y = f(x - 2) + 5$ is $f$ shifted —", ["right 2, up 5", "left 2, up 5", "right 5, up 2", "left 2, down 5"], 0, "Inside the brackets moves opposite ($-2$ → right); outside moves as written."),
  Q("functions-and-transformations", 3, "If $f(x) = 2x - 6$, its inverse is $f^{-1}(x)$ = —", ["$\\tfrac{x+6}{2}$", "$\\tfrac{x-6}{2}$", "$6 - 2x$", "$\\tfrac{1}{2x-6}$"], 0, "Swap and solve: $x = 2y - 6$ gives $y = \\tfrac{x+6}{2}$."),

  // 2. Polynomial Functions
  Q("polynomial-functions", 1, "The degree of $5x^3 - 2x^7 + 1$ is —", ["$7$", "$3$", "$5$", "$1$"], 0, "The largest exponent anywhere wins: $-2x^7$."),
  Q("polynomial-functions", 2, "As $x \\to \\pm\\infty$, the graph of $y = -x^4 + 3x$ heads —", ["down on both ends", "up on both ends", "up right, down left", "down right, up left"], 0, "Even degree with a negative lead: both arms point down."),
  Q("polynomial-functions", 3, "At $x = 2$, the graph of $y = (x+1)(x-2)^2$ —", ["touches and bounces off the axis", "crosses the axis", "has a vertical asymptote", "is undefined"], 0, "Even multiplicity (2): the graph kisses the axis and turns back."),

  // 3. Logarithms
  Q("logarithms", 1, "$\\log_2 32$ = —", ["$5$", "$16$", "$4$", "$6$"], 0, "$2^5 = 32$."),
  Q("logarithms", 2, "$\\log 4 + \\log 25$ = —", ["$2$", "$29$", "$100$", "$10$"], 0, "Logs add when insides multiply: $\\log 100 = 2$."),
  Q("logarithms", 3, "The solution of $3^x = 20$ is —", ["$x = \\tfrac{\\log 20}{\\log 3}$, between 2 and 3", "$x = \\tfrac{20}{3}$", "$x = \\log \\tfrac{20}{3}$", "$x = \\log 60$"], 0, "Take logs of both sides; $3^2 = 9 < 20 < 27 = 3^3$ brackets it."),

  // 4. Sequences & Series
  Q("sequences-and-series", 1, "The next term of $4, 7, 10, 13, \\ldots$ is —", ["$16$", "$15$", "$17$", "$14$"], 0, "Common difference $+3$."),
  Q("sequences-and-series", 2, "Geometric with $a_1 = 3$ and $r = 2$: $a_5$ = —", ["$48$", "$96$", "$24$", "$30$"], 0, "$a_5 = 3 \\cdot 2^4 = 48$."),
  Q("sequences-and-series", 3, "$1 + 2 + 3 + \\cdots + 100$ = —", ["$5050$", "$5000$", "$10100$", "$4950$"], 0, "Gauss pairing: $\\tfrac{100 \\cdot 101}{2}$."),

  // 5. Trigonometry & the Unit Circle
  Q("trigonometry-and-the-unit-circle", 1, "$180°$ in radians is —", ["$\\pi$", "$2\\pi$", "$\\tfrac{\\pi}{2}$", "$90\\pi$"], 0, "Half a turn is $\\pi$ radians."),
  Q("trigonometry-and-the-unit-circle", 2, "$\\sin \\tfrac{\\pi}{6}$ = —", ["$\\tfrac{1}{2}$", "$\\tfrac{\\sqrt{3}}{2}$", "$\\tfrac{\\sqrt{2}}{2}$", "$1$"], 0, "$30°$: the short leg of the 30-60-90 triangle."),
  Q("trigonometry-and-the-unit-circle", 3, "If $\\cos\\theta < 0$ and $\\sin\\theta < 0$, then $\\theta$ is in quadrant —", ["III", "II", "IV", "I"], 0, "Both coordinates negative: bottom-left."),

  // 6. Complex Numbers
  Q("complex-numbers", 1, "$i^2$ = —", ["$-1$", "$1$", "$i$", "$-i$"], 0, "That's the definition of $i$."),
  Q("complex-numbers", 2, "$(3 + 2i) + (1 - 5i)$ = —", ["$4 - 3i$", "$4 + 3i$", "$2 + 7i$", "$3 - 10i$"], 0, "Reals with reals, imaginaries with imaginaries."),
  Q("complex-numbers", 3, "$(2 + i)(2 - i)$ = —", ["$5$", "$3$", "$4$", "$5 - 4i$"], 0, "Conjugates: $4 - i^2 = 4 + 1 = 5$ — purely real."),

  // 7. Statistics & Data
  Q("statistics-and-data", 1, "The median of $2, 3, 7, 8, 100$ is —", ["$7$", "$8$", "$24$", "$100$"], 0, "The middle of the sorted list — the 100 can't drag it."),
  Q("statistics-and-data", 2, "Scores: mean $70$, SD $10$. A score of $85$ has $z$ = —", ["$1.5$", "$15$", "$-1.5$", "$0.5$"], 0, "$z = \\tfrac{85 - 70}{10} = 1.5$."),
  Q("statistics-and-data", 3, "Normal with $\\mu = 100$, $\\sigma = 15$: about what share lies between $85$ and $115$?", ["$68\\%$", "$95\\%$", "$50\\%$", "$99.7\\%$"], 0, "That's $\\mu \\pm 1\\sigma$ — the 68 of 68-95-99.7."),
];

// Grade 12 — 7 topics × 3 genuine tiers.
const G12_CURATED: Curated[] = [
  // 1. Trigonometric Identities
  Q("trigonometric-identities", 1, "$\\sin^2\\theta + \\cos^2\\theta$ = —", ["$1$", "$0$", "$2$", "$\\cos 2\\theta$"], 0, "The Pythagorean identity — the unit circle's radius as algebra."),
  Q("trigonometric-identities", 2, "$\\sin\\theta = \\tfrac{3}{5}$ with $\\theta$ in QI. Then $\\cos\\theta$ = —", ["$\\tfrac{4}{5}$", "$\\tfrac{3}{4}$", "$-\\tfrac{4}{5}$", "$\\tfrac{5}{4}$"], 0, "$\\cos^2 = 1 - \\tfrac{9}{25} = \\tfrac{16}{25}$; QI keeps it positive."),
  Q("trigonometric-identities", 3, "Solve $\\sin x = \\tfrac{1}{2}$ on $[0, 2\\pi)$.", ["$\\tfrac{\\pi}{6}$ and $\\tfrac{5\\pi}{6}$", "$\\tfrac{\\pi}{6}$ only", "$\\tfrac{\\pi}{3}$ and $\\tfrac{2\\pi}{3}$", "$\\tfrac{\\pi}{6}$ and $\\tfrac{7\\pi}{6}$"], 0, "Height $\\tfrac12$ hits twice per lap: QI and its vertical mirror in QII."),

  // 2. Limits & Continuity
  Q("limits-and-continuity", 1, "$\\lim_{x \\to 3}(2x + 1)$ = —", ["$7$", "$6$", "does not exist", "$3$"], 0, "Polynomial: substitute. $2(3) + 1$."),
  Q("limits-and-continuity", 2, "$\\lim_{x \\to 2} \\tfrac{x^2 - 4}{x - 2}$ = —", ["$4$", "does not exist — $\\tfrac{0}{0}$", "$2$", "$\\infty$"], 0, "Factor and cancel: $x + 2 \\to 4$. The $\\tfrac00$ was a work order, not a verdict."),
  Q("limits-and-continuity", 3, "$f(x) = x + 1$ for $x < 1$; $f(x) = 4 - x$ for $x \\geq 1$. Then $\\lim_{x \\to 1} f(x)$ —", ["does not exist — left gives 2, right gives 3", "equals $2$", "equals $3$", "equals $2.5$"], 0, "One-sided limits disagree: a jump. Existence requires agreement."),

  // 3. Derivatives
  Q("derivatives", 1, "$\\tfrac{d}{dx} x^3$ = —", ["$3x^2$", "$x^2$", "$3x^3$", "$\\tfrac{x^4}{4}$"], 0, "Power rule: down front, drop by one."),
  Q("derivatives", 2, "The slope of $y = x^2$ at $x = 3$ is —", ["$6$", "$9$", "$2x$", "$3$"], 0, "$y' = 2x$; at 3: slope 6. (9 is the HEIGHT.)"),
  Q("derivatives", 3, "$\\tfrac{d}{dx}(x^2 + 1)^3$ = —", ["$6x(x^2+1)^2$", "$3(x^2+1)^2$", "$6x$", "$3x^2(x^2+1)^2$"], 0, "Chain rule: outer $3(\\cdot)^2$, keep the inside, pay the $2x$ toll."),

  // 4. Applications of Derivatives
  Q("applications-of-derivatives", 1, "Where $f'(x) > 0$, the graph of $f$ is —", ["rising", "falling", "above the x-axis", "flat"], 0, "The derivative's sign is the function's direction."),
  Q("applications-of-derivatives", 2, "The critical points of $f(x) = x^3 - 3x$ are —", ["$x = 1$ and $x = -1$", "$x = 0$ only", "$x = 3$ and $x = -3$", "$x = 1$ only"], 0, "$f' = 3x^2 - 3 = 0$ at $x = \\pm 1$."),
  Q("applications-of-derivatives", 3, "With 100 m of fence, the biggest rectangular paddock has area —", ["$625$ m² — the $25 \\times 25$ square", "$2500$ m²", "$100$ m²", "$250$ m²"], 0, "$A = x(50 - x)$ peaks at $x = 25$: $A'' < 0$ certifies the max."),

  // 5. Integrals
  Q("integrals", 1, "$\\int x^2\\,dx$ = —", ["$\\tfrac{x^3}{3} + C$", "$2x + C$", "$x^3 + C$", "$3x^3 + C$"], 0, "Up by one, divide by the new one — plus the family constant."),
  Q("integrals", 2, "$\\int_1^3 2x\\,dx$ = —", ["$8$", "$6$", "$9$", "$4$"], 0, "$[x^2]_1^3 = 9 - 1 = 8$ — top minus bottom."),
  Q("integrals", 3, "$v(t) = 20 - 10t$ on $[0, 4]$: the displacement is —", ["$0$ — up 20 m, back 20 m", "$40$ m", "$80$ m", "$20$ m"], 0, "$\\int_0^4 v = 80 - 80 = 0$: the ball lands where it started. (Distance is 40.)"),

  // 6. Vectors
  Q("vectors", 1, "$|\\langle 3, 4 \\rangle|$ = —", ["$5$", "$7$", "$12$", "$25$"], 0, "Pythagoras: $\\sqrt{9 + 16}$."),
  Q("vectors", 2, "$\\langle 2, 3 \\rangle \\cdot \\langle 3, -2 \\rangle$ = —", ["$0$ — perpendicular", "$12$", "$6$", "$-6$"], 0, "$6 - 6 = 0$: a right angle, certified by arithmetic."),
  Q("vectors", 3, "The angle between $\\langle 1, 0 \\rangle$ and $\\langle 1, 1 \\rangle$ is —", ["$45°$", "$30°$", "$60°$", "$90°$"], 0, "$\\cos\\theta = \\tfrac{1}{\\sqrt2} = \\tfrac{\\sqrt2}{2}$: the unit-circle lookup gives 45°."),

  // 7. Conic Sections
  Q("conic-sections", 1, "$(x-2)^2 + (y+1)^2 = 9$: center and radius?", ["$(2, -1)$, $r = 3$", "$(-2, 1)$, $r = 3$", "$(2, -1)$, $r = 9$", "$(-2, 1)$, $r = 9$"], 0, "Signs flip for the center; square-root the right side."),
  Q("conic-sections", 2, "The foci of $\\tfrac{x^2}{25} + \\tfrac{y^2}{9} = 1$ are —", ["$(\\pm 4, 0)$", "$(\\pm\\sqrt{34}, 0)$", "$(\\pm 3, 0)$", "$(\\pm 5, 0)$"], 0, "Ellipse: $c^2 = a^2 - b^2 = 16$ — minus-law, foci inside."),
  Q("conic-sections", 3, "$9x^2 - 4y^2 = 36$ is a —", ["hyperbola", "ellipse", "parabola", "circle"], 0, "Opposite signs on the squared terms: the minus sign's curve."),
];


// ---------------------------------------------------------------------------
// Grade 7 — one tiered question per difficulty for each of the 7 topics.
// ---------------------------------------------------------------------------
const G7_CURATED: Curated[] = [
  // 1. Proportional Relationships
  Q("proportional-relationships", 1, "$3$ notebooks cost $\\$12$. What is the unit price?", ["$\\$4$", "$\\$3$", "$\\$12$", "$\\$36$"], 0, "$12 \\div 3 = 4$ dollars per notebook."),
  Q("proportional-relationships", 2, "You walk $\\tfrac{1}{2}$ mile in $\\tfrac{1}{4}$ hour. Your speed in miles per hour is —", ["$2$", "$\\tfrac{1}{2}$", "$\\tfrac{1}{8}$", "$4$"], 0, "$\\tfrac{1}{2} \\div \\tfrac{1}{4} = 2$ mph."),
  Q("proportional-relationships", 3, "A proportional relationship contains $(4, 10)$. Its equation is —", ["$y = \\tfrac{5}{2}x$", "$y = \\tfrac{2}{5}x$", "$y = x + 6$", "$y = 40x$"], 0, "$k = \\tfrac{10}{4} = \\tfrac{5}{2}$, so $y = \\tfrac{5}{2}x$."),

  // 2. Rational Number Operations
  Q("rational-number-operations", 1, "Compute $-\\tfrac{1}{4} + \\tfrac{3}{4}$.", ["$\\tfrac{1}{2}$", "$-\\tfrac{1}{2}$", "$1$", "$-1$"], 0, "Different signs: $\\tfrac{3}{4} - \\tfrac{1}{4} = \\tfrac{2}{4} = \\tfrac{1}{2}$."),
  Q("rational-number-operations", 2, "Compute $-2.5 - (-4)$.", ["$1.5$", "$-6.5$", "$-1.5$", "$6.5$"], 0, "Add the opposite: $-2.5 + 4 = 1.5$."),
  Q("rational-number-operations", 3, "Compute $\\left(-\\tfrac{2}{3}\\right) \\div \\tfrac{4}{9}$.", ["$-\\tfrac{3}{2}$", "$\\tfrac{3}{2}$", "$-\\tfrac{8}{27}$", "$\\tfrac{2}{3}$"], 0, "Keep–change–flip: $-\\tfrac{2}{3} \\times \\tfrac{9}{4} = -\\tfrac{3}{2}$."),

  // 3. Equations & Inequalities
  Q("equations-and-inequalities", 1, "Simplify $3x - 7x$.", ["$-4x$", "$4x$", "$-4$", "$10x$"], 0, "$3 - 7 = -4$, so $-4x$."),
  Q("equations-and-inequalities", 2, "Solve $2x + 5 = -9$.", ["$x = -7$", "$x = -2$", "$x = 7$", "$x = 2$"], 0, "$2x = -14$, so $x = -7$."),
  Q("equations-and-inequalities", 3, "Solve $-3x + 4 > 10$.", ["$x < -2$", "$x > -2$", "$x < 2$", "$x > 2$"], 0, "$-3x > 6$; dividing by $-3$ flips: $x < -2$."),

  // 4. Percent Applications
  Q("percent-applications", 1, "Find $20\\%$ of $45$.", ["$9$", "$20$", "$5$", "$25$"], 0, "$0.20 \\times 45 = 9$."),
  Q("percent-applications", 2, "A price falls from $\\$80$ to $\\$60$. The percent decrease is —", ["$25\\%$", "$33\\%$", "$20\\%$", "$75\\%$"], 0, "$\\tfrac{20}{80} = 25\\%$ — divide by the ORIGINAL."),
  Q("percent-applications", 3, "After a $20\\%$ discount, a jacket costs $\\$48$. The original price was —", ["$\\$60$", "$\\$57.60$", "$\\$58$", "$\\$68$"], 0, "$48 \\div 0.80 = 60$: divide by the multiplier."),

  // 5. Geometry: Scale, Angles & Circles
  Q("geometry-scale-and-circles", 1, "At a scale of $1:50$, a $6$ cm drawing represents —", ["$300$ cm", "$56$ cm", "$3$ cm", "$50$ cm"], 0, "$6 \\times 50 = 300$ cm."),
  Q("geometry-scale-and-circles", 2, "Two lines cross, making one angle of $110^\\circ$. The angle NEXT to it measures —", ["$70^\\circ$", "$110^\\circ$", "$250^\\circ$", "$90^\\circ$"], 0, "Adjacent angles on a line sum to $180$: $180 - 110 = 70$."),
  Q("geometry-scale-and-circles", 3, "A circle has radius $6$. Its area, in terms of $\\pi$, is —", ["$36\\pi$", "$12\\pi$", "$6\\pi$", "$36$"], 0, "$A = \\pi r^2 = 36\\pi$. ($12\\pi$ is the circumference.)"),

  // 6. Probability
  Q("probability", 1, "One die is rolled. $P(\\text{even})$ = —", ["$\\tfrac{1}{2}$", "$\\tfrac{1}{6}$", "$\\tfrac{1}{3}$", "$\\tfrac{2}{3}$"], 0, "Evens $\\{2,4,6\\}$: $\\tfrac{3}{6} = \\tfrac{1}{2}$."),
  Q("probability", 2, "A spinner landed on red $18$ of $60$ spins. The experimental probability of red is —", ["$0.3$", "$0.18$", "$0.6$", "$0.5$"], 0, "$\\tfrac{18}{60} = 0.3$."),
  Q("probability", 3, "A coin is flipped and a die is rolled. $P(\\text{heads AND a } 6)$ = —", ["$\\tfrac{1}{12}$", "$\\tfrac{1}{8}$", "$\\tfrac{2}{3}$", "$\\tfrac{1}{6}$"], 0, "Independent: $\\tfrac{1}{2} \\times \\tfrac{1}{6} = \\tfrac{1}{12}$."),

  // 7. Sampling & Statistics
  Q("sampling-and-statistics", 1, "Find the median of $8, 3, 5, 9, 1$.", ["$5$", "$3$", "$8$", "$9$"], 0, "Sorted: $1, 3, 5, 8, 9$ — middle is $5$."),
  Q("sampling-and-statistics", 2, "A random sample finds $12$ of $40$ students bike to school. Estimate bikers among $1{,}000$ students.", ["$300$", "$120$", "$480$", "$12$"], 0, "$\\tfrac{12}{40} = 0.3$; $0.3 \\times 1000 = 300$."),
  Q("sampling-and-statistics", 3, "Data: $6, 8, 10, 12, 14$ (mean $10$). The MAD is —", ["$2.4$", "$4$", "$10$", "$2$"], 0, "Distances $4,2,0,2,4$ average to $\\tfrac{12}{5} = 2.4$."),
];


// ---------------------------------------------------------------------------
// Grade 9 — one tiered question per difficulty for each of the 7 topics.
// ---------------------------------------------------------------------------
const G9_CURATED: Curated[] = [
  // 1. Equations & Formulas
  Q("equations-and-formulas", 1, "Solve $3x - 4 = 2x + 6$.", ["$x = 10$", "$x = 2$", "$x = -10$", "$x = 5$"], 0, "Subtract $2x$: $x - 4 = 6$, so $x = 10$."),
  Q("equations-and-formulas", 2, "Solve $2(x - 3) = 4x + 8$ .", ["$x = -7$", "$x = 7$", "$x = -1$", "$x = 1$"], 0, "$2x - 6 = 4x + 8 \\Rightarrow -14 = 2x \\Rightarrow x = -7$."),
  Q("equations-and-formulas", 3, "Solve $A = \\tfrac{1}{2}bh$ for $h$.", ["$h = \\tfrac{2A}{b}$", "$h = \\tfrac{A}{2b}$", "$h = 2Ab$", "$h = \\tfrac{b}{2A}$"], 0, "Multiply by 2, divide by $b$: $h = \\tfrac{2A}{b}$."),

  // 2. Inequalities & Absolute Value
  Q("inequalities-and-absolute-value", 1, "Which values satisfy $-2 < x \\le 3$?", ["$0$ and $3$", "$-2$ and $3$", "$-3$ and $0$", "$4$ and $0$"], 0, "$0$ is inside; $3$ is included by $\\le$. $-2$ itself is excluded."),
  Q("inequalities-and-absolute-value", 2, "Solve $|x| = 5$.", ["$x = 5$ or $x = -5$", "$x = 5$ only", "$x = -5$ only", "no solution"], 0, "Two numbers sit 5 from zero: $\\pm 5$."),
  Q("inequalities-and-absolute-value", 3, "Solve $|x - 2| < 3$.", ["$-1 < x < 5$", "$x < 5$", "$x < -1$ or $x > 5$", "$-3 < x < 3$"], 0, "Within 3 of 2: $2 - 3 < x < 2 + 3$."),

  // 3. Introduction to Functions
  Q("introduction-to-functions", 1, "If $f(x) = 2x + 1$, find $f(3)$.", ["$7$", "$6$", "$5$", "$9$"], 0, "$f(3) = 2(3) + 1 = 7$."),
  Q("introduction-to-functions", 2, "Which relation is NOT a function?", ["$\\{(1,2), (1,3), (2,4)\\}$", "$\\{(1,2), (2,2), (3,2)\\}$", "$y = x^2$", "$y = 3x - 1$"], 0, "Input $1$ has two outputs — it fails the one-output rule."),
  Q("introduction-to-functions", 3, "The domain of $f(x) = \\tfrac{1}{x - 4}$ is —", ["all reals except $4$", "all reals", "$x > 4$", "all reals except $0$"], 0, "Only $x = 4$ makes the denominator zero."),

  // 4. Linear Models & Variation
  Q("linear-models-and-variation", 1, "$y$ varies directly with $x$, and $y = 12$ when $x = 4$. Find $k$.", ["$3$", "$48$", "$8$", "$\\tfrac{1}{3}$"], 0, "$k = \\tfrac{y}{x} = 3$."),
  Q("linear-models-and-variation", 2, "$y$ varies inversely with $x$: $y = 6$ when $x = 4$. Find $y$ when $x = 8$.", ["$3$", "$12$", "$2$", "$48$"], 0, "$xy = 24$ stays constant: $y = 24 \\div 8 = 3$."),
  Q("linear-models-and-variation", 3, "A gym costs $\\$25$ to join plus $\\$15$ per month. Which model gives the total cost after $m$ months?", ["$C = 15m + 25$", "$C = 25m + 15$", "$C = 40m$", "$C = 15m - 25$"], 0, "Per-month rate multiplies $m$; the joining fee adds once."),

  // 5. Systems of Inequalities
  Q("inequalities-in-two-variables", 1, "Is $(1, 5)$ a solution of $y > 2x + 1$?", ["Yes — $5 > 3$", "No — $5 < 3$", "Only on the line", "Can't tell"], 0, "Substitute: $5 > 2(1) + 1 = 3$. ✓"),
  Q("inequalities-in-two-variables", 2, "The graph of $y \\le x - 2$ uses —", ["a solid line, shaded below", "a dashed line, shaded below", "a solid line, shaded above", "a dashed line, shaded above"], 0, "$\\le$ includes the line (solid) and takes the lesser side (below)."),
  Q("inequalities-in-two-variables", 3, "Which point satisfies BOTH $y \\ge x$ and $y < 4$?", ["$(1, 2)$", "$(3, 1)$", "$(0, 5)$", "$(4, 4)$"], 0, "$2 \\ge 1$ ✓ and $2 < 4$ ✓; the others fail one test."),

  // 6. Piecewise & Absolute-Value Graphs
  Q("piecewise-and-absolute-value-graphs", 1, "The graph of $y = |x|$ looks like —", ["a V with its point at the origin", "a straight line", "a U-shaped curve", "a circle"], 0, "Absolute value folds the line $y = x$ upward into a V."),
  Q("piecewise-and-absolute-value-graphs", 2, "The vertex of $y = |x - 3| + 1$ is —", ["$(3, 1)$", "$(-3, 1)$", "$(3, -1)$", "$(1, 3)$"], 0, "Inside shifts right 3; outside shifts up 1."),
  Q("piecewise-and-absolute-value-graphs", 3, "For $f(x) = \\begin{cases} x + 1 & x < 0 \\\\ 2x & x \\ge 0 \\end{cases}$, find $f(-2) + f(3)$.", ["$5$", "$7$", "$4$", "$1$"], 0, "$f(-2) = -1$ (first piece), $f(3) = 6$ (second): $-1 + 6 = 5$."),

  // 7. Data Distributions
  Q("data-distributions", 1, "The median of $2, 4, 6, 8, 10$ is —", ["$6$", "$5$", "$8$", "$30$"], 0, "The middle of the sorted list."),
  Q("data-distributions", 2, "For the data $1, 3, 5, 7, 9, 11, 13, 15$, the first quartile $Q_1$ is —", ["$4$", "$3$", "$5$", "$8$"], 0, "Lower half $1,3,5,7$: median $= \\tfrac{3+5}{2} = 4$."),
  Q("data-distributions", 3, "A data set has $Q_1 = 20$ and $Q_3 = 32$. The IQR is —", ["$12$", "$52$", "$26$", "$6$"], 0, "IQR $= Q_3 - Q_1 = 12$."),
];

let cache: PlacementQuestion[] | null = null;
let geoCache: PlacementQuestion[] | null = null;
let g7Cache: PlacementQuestion[] | null = null;
let g8Cache: PlacementQuestion[] | null = null;
let g9Cache: PlacementQuestion[] | null = null;
let g10Cache: PlacementQuestion[] | null = null;
let g11Cache: PlacementQuestion[] | null = null;
let g12Cache: PlacementQuestion[] | null = null;

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

export function getGrade7PlacementBank(): PlacementQuestion[] {
  if (g7Cache) return g7Cache;
  const titleBySlug = new Map(getGrade7Spine().map((t) => [t.slug, t.title]));
  g7Cache = G7_CURATED.map((q) => ({ ...q, topicTitle: titleBySlug.get(q.topicSlug) ?? q.topicSlug }));
  return g7Cache;
}

export function getGrade8PlacementBank(): PlacementQuestion[] {
  if (g8Cache) return g8Cache;
  const titleBySlug = new Map(getGrade8Spine().map((t) => [t.slug, t.title]));
  g8Cache = G8_CURATED.map((q) => ({ ...q, topicTitle: titleBySlug.get(q.topicSlug) ?? q.topicSlug }));
  return g8Cache;
}

export function getGrade9PlacementBank(): PlacementQuestion[] {
  if (g9Cache) return g9Cache;
  const titleBySlug = new Map(getGrade9Spine().map((t) => [t.slug, t.title]));
  g9Cache = G9_CURATED.map((q) => ({ ...q, topicTitle: titleBySlug.get(q.topicSlug) ?? q.topicSlug }));
  return g9Cache;
}

export function getGrade10PlacementBank(): PlacementQuestion[] {
  if (g10Cache) return g10Cache;
  const titleBySlug = new Map(getGrade10Spine().map((t) => [t.slug, t.title]));
  g10Cache = G10_CURATED.map((q) => ({ ...q, topicTitle: titleBySlug.get(q.topicSlug) ?? q.topicSlug }));
  return g10Cache;
}

export function getGrade11PlacementBank(): PlacementQuestion[] {
  if (g11Cache) return g11Cache;
  const titleBySlug = new Map(getGrade11Spine().map((t) => [t.slug, t.title]));
  g11Cache = G11_CURATED.map((q) => ({ ...q, topicTitle: titleBySlug.get(q.topicSlug) ?? q.topicSlug }));
  return g11Cache;
}

export function getGrade12PlacementBank(): PlacementQuestion[] {
  if (g12Cache) return g12Cache;
  const titleBySlug = new Map(getGrade12Spine().map((t) => [t.slug, t.title]));
  g12Cache = G12_CURATED.map((q) => ({ ...q, topicTitle: titleBySlug.get(q.topicSlug) ?? q.topicSlug }));
  return g12Cache;
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
