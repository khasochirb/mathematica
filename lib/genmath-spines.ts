// The course and grade SPINES — the platform's light structural metadata:
// slugs, titles, blurbs, live flags, in taught order. Pure literals, ZERO
// data imports, so client code (the ratings taxonomy, placement title maps,
// the /math catalog) can know what exists without shipping the ~14 MB
// course corpus that lib/genmath-lessons.ts imports. That module re-exports
// everything here, so content code keeps importing from the registry;
// weight-sensitive modules import from HERE and are fenced by
// lib/genmath-split.test.ts.

export interface GradeInfo {
  grade: number;
  active: boolean;
}

export interface GradeSpineEntry {
  slug: string;
  title: string;
  blurb: string;
  live: boolean;
}

export interface GeometrySpineEntry {
  unit: number;
  slug: string;
  title: string;
  blurb: string;
  buildsOn?: string;
  live: boolean;
}

const ALL_GRADES: GradeInfo[] = [
  { grade: 4, active: true },
  { grade: 5, active: true },
  { grade: 6, active: true },
  { grade: 7, active: true },
  { grade: 8, active: true },
  { grade: 9, active: true },
  { grade: 10, active: true },
  { grade: 11, active: true },
  { grade: 12, active: true },
];

export function listGrades(): GradeInfo[] {
  return ALL_GRADES;
}

// Grade 4 — the second primary-band year, authored as one complete batch
// (scripts/grade4/build_*.py) and the first grade with figures from day one.
// Content sits strictly BELOW Grade 5: numbers to 10 000, tables to 10,
// fraction meaning (no equivalence), shapes without area, data without mean.
export const GRADE4_SPINE: GradeSpineEntry[] = [
  {
    slug: "numbers-to-10000",
    title: "Numbers to 10 000",
    blurb: "Reading and writing four-digit numbers, place value to thousands, comparing and ordering, rounding to 10 and 100, and skip-counting patterns.",
    live: true,
  },
  {
    slug: "addition-and-subtraction",
    title: "Addition & Subtraction",
    blurb: "Column addition and subtraction with regrouping inside 10 000, mental strategies, missing-number fact families, and one- and two-step word problems.",
    live: true,
  },
  {
    slug: "times-tables-and-multiplication",
    title: "Times Tables & Multiplication",
    blurb: "Equal groups and repeated addition, the times tables to 10 with their patterns, arrays and the turnaround trick, and multiplying two-digit numbers by one digit.",
    live: true,
  },
  {
    slug: "division-and-sharing",
    title: "Division & Sharing",
    blurb: "Sharing and grouping as the two faces of division, division facts from the times tables, first remainders with their receipts, and choosing the right operation.",
    live: true,
  },
  {
    slug: "fractions-parts-of-a-whole",
    title: "Fractions — Parts of a Whole",
    blurb: "What a fraction really is — equal parts of a whole — unit and non-unit fractions, comparing them, and taking a fraction of a set, drawn with fraction bars throughout.",
    live: true,
  },
  {
    slug: "shapes-and-symmetry",
    title: "Shapes & Symmetry",
    blurb: "Naming 2-D shapes by their sides, right angles as quarter turns, sorting quadrilaterals, the fold test for line symmetry, and the faces, edges and vertices of 3-D solids.",
    live: true,
  },
  {
    slug: "measurement-time-and-money",
    title: "Measurement, Time & Money",
    blurb: "Centimetres and metres, grams and kilograms, litres and millilitres, reading the clock to the quarter hour, the calendar, and counting tögrög and making change.",
    live: true,
  },
  {
    slug: "data-and-pictographs",
    title: "Data & Pictographs",
    blurb: "Tally marks in bundles of five, frequency tables with totals as receipts, pictographs with keys, bar charts on small scales, and answering questions from data.",
    live: true,
  },
];

// Grade 5 — the school-entrance transition year that OPENS the primary band
// (grades 1–5). Topics go live one at a time as they are authored
// (scripts/grade5/build_*.py), the way IM3's units did.
export const GRADE5_SPINE: GradeSpineEntry[] = [
  {
    slug: "whole-numbers-and-place-value",
    title: "Whole Numbers & Place Value",
    blurb: "Reading and writing numbers to the millions, what each digit is worth, comparing and ordering, rounding, and estimation.",
    live: true,
  },
  {
    slug: "addition-and-subtraction",
    title: "Addition & Subtraction",
    blurb: "Multi-digit addition and subtraction with regrouping, mental strategies, fact families with missing numbers, and multi-step word problems.",
    live: true,
  },
  {
    slug: "multiplication-and-division",
    title: "Multiplication & Division",
    blurb: "Multi-digit multiplication, long division with remainders, and choosing the operation a problem needs.",
    live: true,
  },
  {
    slug: "fractions-first-steps",
    title: "Fractions — First Steps",
    blurb: "Fractions as parts of a whole, equivalent fractions, comparing, improper fractions and mixed numbers, and adding and subtracting with like denominators.",
    live: true,
  },
  {
    slug: "decimals-first-steps",
    title: "Decimals — First Steps",
    blurb: "Tenths and hundredths on the extended place-value ladder, decimals as fractions, comparing, adding and subtracting, and rounding and measuring with decimals.",
    live: true,
  },
  {
    slug: "measurement-and-units",
    title: "Measurement & Units",
    blurb: "The metric ladders for length, mass and capacity, the base-sixty ladder of time, elapsed time, and convert-first measurement problems.",
    live: true,
  },
  {
    slug: "geometry-shapes-and-area",
    title: "Geometry — Shapes & Area",
    blurb: "Angles and their sums, triangles and the quadrilateral family, perimeter, area, and composite figures solved down two agreeing roads.",
    live: true,
  },
  {
    slug: "data-and-graphs",
    title: "Data & Graphs",
    blurb: "Tally charts and frequency tables, pictographs with a key, bar graphs and their scales, line graphs of change over time, and the mean and range.",
    live: true,
  },
];

export const GRADE7_SPINE: GradeSpineEntry[] = [
  {
    slug: "proportional-relationships",
    title: "Proportional Relationships",
    blurb: "Unit rates with fractions, the constant of proportionality, y = kx, and reading proportionality from tables and graphs.",
    live: true,
  },
  {
    slug: "rational-number-operations",
    title: "Rational Number Operations",
    blurb: "Adding, subtracting, multiplying, and dividing with negatives — integers, fractions, and decimals, all four operations, one number line.",
    live: true,
  },
  {
    slug: "equations-and-inequalities",
    title: "Equations & Inequalities",
    blurb: "Simplifying expressions with negatives, two-step equations, and inequalities — including the flip when you multiply by a negative.",
    live: true,
  },
  {
    slug: "percent-applications",
    title: "Percent Applications",
    blurb: "Percent change, discounts, markups, tax, tips, simple interest, and percent error — the percents that show up on receipts.",
    live: true,
  },
  {
    slug: "geometry-scale-and-circles",
    title: "Geometry: Scale, Angles & Circles",
    blurb: "Scale drawings, angle relationships, the triangle inequality, and circles — where \u03c0 finally earns its name.",
    live: true,
  },
  {
    slug: "probability",
    title: "Probability",
    blurb: "Chance from 0 to 1: sample spaces, theoretical vs experimental probability, and simple compound events.",
    live: true,
  },
  {
    slug: "sampling-and-statistics",
    title: "Sampling & Statistics",
    blurb: "Random samples, inference about a population, and comparing two data sets with center and spread.",
    live: true,
  },
];

export const GRADE8_SPINE: GradeSpineEntry[] = [
  {
    slug: "the-real-number-system",
    title: "The Real Number System",
    blurb: "Rational vs. irrational numbers, terminating and repeating decimals, classifying the reals, and placing any number on the line.",
    live: true,
  },
  {
    slug: "exponents-and-scientific-notation",
    title: "Exponents & Scientific Notation",
    blurb: "The laws of exponents, zero and negative powers, and writing huge and tiny numbers in scientific notation.",
    live: true,
  },
  {
    slug: "roots",
    title: "Square & Cube Roots",
    blurb: "Square roots and cube roots, perfect squares and cubes, and solving equations like x² = 49 and x³ = 8.",
    live: true,
  },
  {
    slug: "linear-equations",
    title: "Linear Equations",
    blurb: "Multi-step equations, variables on both sides, and equations with no solution or infinitely many.",
    live: true,
  },
  {
    slug: "linear-functions",
    title: "Linear Functions",
    blurb: "Slope and rate of change, y = mx + b, and reading a line four ways: table, graph, equation, and words.",
    live: true,
  },
  {
    slug: "systems-of-linear-equations",
    title: "Systems of Linear Equations",
    blurb: "Two lines at once — solving by graphing, substitution, and elimination, and what the intersection means.",
    live: true,
  },
  {
    slug: "scatter-plots-and-bivariate-data",
    title: "Scatter Plots & Bivariate Data",
    blurb: "Plotting paired data, spotting correlation, fitting a trend line, and reading two-way tables.",
    live: true,
  },
];

export const GRADE9_SPINE: GradeSpineEntry[] = [
  {
    slug: "equations-and-formulas",
    title: "Equations & Formulas",
    blurb: "Multi-step equations with variables on both sides, special cases, and literal equations — solving formulas for any letter.",
    live: true,
  },
  {
    slug: "inequalities-and-absolute-value",
    title: "Inequalities & Absolute Value",
    blurb: "Compound inequalities (and/or), absolute-value equations, and absolute-value inequalities — distances on the number line.",
    live: true,
  },
  {
    slug: "introduction-to-functions",
    title: "Introduction to Functions",
    blurb: "Function notation, domain and range, the vertical line test, and reading graphs qualitatively.",
    live: true,
  },
  {
    slug: "linear-models-and-variation",
    title: "Linear Models & Variation",
    blurb: "Writing linear models from context, direct variation revisited, and inverse variation \u2014 y = k/x, the other proportionality.",
    live: true,
  },
  {
    slug: "inequalities-in-two-variables",
    title: "Systems of Inequalities",
    blurb: "Graphing two-variable inequalities, shading half-planes, and systems of inequalities as feasible regions.",
    live: true,
  },
  {
    slug: "piecewise-and-absolute-value-graphs",
    title: "Piecewise & Absolute-Value Graphs",
    blurb: "The V of y = |x|, shifts of it, and functions defined in pieces \u2014 including step functions.",
    live: true,
  },
  {
    slug: "data-distributions",
    title: "Data Distributions",
    blurb: "Histograms, box plots, quartiles and IQR \u2014 the shape of data and how to compare distributions.",
    live: true,
  },
];

export const GRADE10_SPINE: GradeSpineEntry[] = [
  {
    slug: "polynomials-and-factoring",
    title: "Polynomials & Factoring",
    blurb: "Terms, degree, and standard form; adding, subtracting, and multiplying polynomials; factoring from GCF to trinomials — and solving by the zero product.",
    live: true,
  },
  {
    slug: "quadratic-equations",
    title: "Quadratic Equations",
    blurb: "Solving by factoring, square roots, completing the square, and the quadratic formula — plus the discriminant.",
    live: true,
  },
  {
    slug: "quadratic-functions",
    title: "Quadratic Functions & Parabolas",
    blurb: "Graphs of y = ax² + bx + c: vertex, axis of symmetry, transformations, and max/min word problems.",
    live: true,
  },
  {
    slug: "rational-expressions",
    title: "Rational Expressions & Equations",
    blurb: "Simplifying, multiplying, and adding algebraic fractions; solving rational equations and spotting excluded values.",
    live: true,
  },
  {
    slug: "radicals-and-rational-exponents",
    title: "Radicals & Rational Exponents",
    blurb: "Operations with radicals, rationalizing, fractional exponents, and solving radical equations.",
    live: true,
  },
  {
    slug: "exponential-functions",
    title: "Exponential Functions & Growth",
    blurb: "y = a·bˣ: growth and decay, compound interest, and how exponentials outrun every line.",
    live: true,
  },
  {
    slug: "probability-and-counting",
    title: "Probability & Counting",
    blurb: "Counting principles, permutations and combinations, and probability of compound events.",
    live: true,
  },
];

export const GRADE11_SPINE: GradeSpineEntry[] = [
  {
    slug: "functions-and-transformations",
    title: "Functions & Transformations",
    blurb: "Function notation, domain and range, shifts, stretches, reflections — and inverse functions that undo it all.",
    live: true,
  },
  {
    slug: "polynomial-functions",
    title: "Polynomial Functions",
    blurb: "Cubics and beyond: end behavior, zeros and multiplicity, the remainder and factor theorems, and sketching from factors.",
    live: true,
  },
  {
    slug: "logarithms",
    title: "Logarithms",
    blurb: "The inverse of the exponential: log laws, solving exponential and log equations, and the scales that measure earthquakes and sound.",
    live: true,
  },
  {
    slug: "sequences-and-series",
    title: "Sequences & Series",
    blurb: "Arithmetic and geometric sequences, recursive and explicit rules, and the sums that add a whole list at once.",
    live: true,
  },
  {
    slug: "trigonometry-and-the-unit-circle",
    title: "Trigonometry & the Unit Circle",
    blurb: "Radians, the unit circle, sine and cosine as coordinates, and the waves they draw.",
    live: true,
  },
  {
    slug: "complex-numbers",
    title: "Complex Numbers",
    blurb: "The number i, arithmetic with a + bi, conjugates and division, and quadratics whose roots finally all exist.",
    live: true,
  },
  {
    slug: "statistics-and-data",
    title: "Statistics & Data",
    blurb: "Mean vs median, standard deviation, z-scores, and the normal curve that grades on it.",
    live: true,
  },
];

export const GRADE12_SPINE: GradeSpineEntry[] = [
  {
    slug: "trigonometric-identities",
    title: "Trigonometric Identities",
    blurb: "The Pythagorean identity, sum and double-angle formulas, proving identities, and solving trig equations.",
    live: true,
  },
  {
    slug: "limits-and-continuity",
    title: "Limits & Continuity",
    blurb: "What a function approaches: reading limits from graphs, computing them with algebra, and where functions break.",
    live: true,
  },
  {
    slug: "derivatives",
    title: "Derivatives",
    blurb: "The slope of a curve: the derivative as a limit, and the power, product, quotient, and chain rules.",
    live: true,
  },
  {
    slug: "applications-of-derivatives",
    title: "Applications of Derivatives",
    blurb: "Tangent lines, increasing and decreasing, maxima and minima, and optimization problems that pay.",
    live: true,
  },
  {
    slug: "integrals",
    title: "Integrals",
    blurb: "Undoing the derivative: antiderivatives, the area under a curve, and the Fundamental Theorem of Calculus.",
    live: true,
  },
  {
    slug: "vectors",
    title: "Vectors",
    blurb: "Magnitude and direction: components, addition, scalar multiples, the dot product, and the angle between.",
    live: true,
  },
  {
    slug: "conic-sections",
    title: "Conic Sections",
    blurb: "Circles, ellipses, parabolas, and hyperbolas — the four curves hiding in a sliced cone.",
    live: true,
  },
];

export const GEOMETRY_SPINE: GeometrySpineEntry[] = [
  {
    unit: 1,
    slug: "foundations",
    title: "Foundations: Points, Lines & Angles",
    blurb: "Points, lines, rays, segments and planes; measuring segments and angles; angle types, angle pairs, and bisectors.",
    buildsOn: "Nothing — geometry starts here, from zero.",
    live: true,
  },
  {
    unit: 2,
    slug: "reasoning-and-proof",
    title: "Reasoning & Proof",
    blurb: "From noticing patterns to proving facts: conjectures, if-then statements, and your first two-column proofs.",
    buildsOn: "Unit 1's definitions and the segment/angle facts you measured there.",
    live: true,
  },
  {
    unit: 3,
    slug: "parallel-and-perpendicular",
    title: "Parallel & Perpendicular Lines",
    blurb: "Transversals and the angle pairs they create — which are congruent, which are supplementary — and proving lines parallel.",
    buildsOn: "Angle pairs from Unit 1; the proof habits from Unit 2.",
    live: true,
  },
  {
    unit: 4,
    slug: "triangles-and-congruence",
    title: "Triangles & Congruence",
    blurb: "Triangle types, the angle sum, the triangle inequality, and the congruence shortcuts SSS · SAS · ASA · AAS · HL.",
    buildsOn: "Units 1–3: angles, proof, and parallel-line facts.",
    live: true,
  },
  {
    unit: 5,
    slug: "relationships-in-triangles",
    title: "Relationships in Triangles",
    blurb: "Bisectors, medians, altitudes, the midsegment theorem, and inequalities inside a triangle.",
    buildsOn: "Triangle congruence from Unit 4.",
    live: true,
  },
  {
    unit: 6,
    slug: "quadrilaterals-and-polygons",
    title: "Quadrilaterals & Polygons",
    blurb: "Angle sums for any polygon; parallelograms, rectangles, rhombi, squares, trapezoids, and kites — with proofs.",
    buildsOn: "Triangles (Unit 4) and parallel lines (Unit 3).",
    live: true,
  },
  {
    unit: 7,
    slug: "similarity",
    title: "Similarity",
    blurb: "Ratio and proportion, similar polygons, the AA · SSS · SAS similarity shortcuts, and the side-splitter theorem.",
    buildsOn: "Triangle facts from Units 4–5; ratios from Grade 6.",
    live: true,
  },
  {
    unit: 8,
    slug: "right-triangles-and-trig",
    title: "Right Triangles & Trigonometry",
    blurb: "The Pythagorean theorem, special right triangles, and sine · cosine · tangent with elevation and depression.",
    buildsOn: "Similarity (Unit 7) — trig ratios ARE similarity.",
    live: true,
  },
  {
    unit: 9,
    slug: "circles",
    title: "Circles",
    blurb: "Radius, chord, tangent, secant; central and inscribed angles; arcs; and the circle relationships.",
    buildsOn: "Angles (Unit 1), triangles (Unit 4), and right triangles (Unit 8).",
    live: true,
  },
  {
    unit: 10,
    slug: "area-and-perimeter",
    title: "Area & Perimeter",
    blurb: "Areas of triangles, quadrilaterals and regular polygons; circumference, circle area, sectors, and composite figures.",
    buildsOn: "The shape properties from Units 4, 6, and 9.",
    live: true,
  },
  {
    unit: 11,
    slug: "surface-area-and-volume",
    title: "Surface Area & Volume",
    blurb: "Prisms, cylinders, pyramids, cones, and spheres — wrapping and filling 3-D solids.",
    buildsOn: "Area formulas from Unit 10.",
    live: true,
  },
  {
    unit: 12,
    slug: "transformations",
    title: "Transformations",
    blurb: "Translations, reflections, rotations, and dilations; symmetry; congruence and similarity re-seen through motion.",
    buildsOn: "Congruence (Unit 4) and similarity (Unit 7).",
    live: true,
  },
  {
    unit: 13,
    slug: "coordinate-geometry",
    title: "Coordinate Geometry",
    blurb: "Distance, midpoint, and slope; equations of lines and circles; proofs with coordinates — the course capstone.",
    buildsOn: "Everything — algebra meets every earlier unit.",
    live: true,
  },
];

export const PROBSTAT_SPINE: GeometrySpineEntry[] = [
  {
    unit: 1,
    slug: "counting-principles",
    title: "Counting Principles",
    blurb: "The multiplication and addition principles, complementary counting, and organized lists — how to count without counting.",
    buildsOn: "Nothing — the course starts here, from zero.",
    live: true,
  },
  {
    unit: 2,
    slug: "permutations",
    title: "Permutations & Arrangements",
    blurb: "Factorials, arrangements of all or some objects, repeated letters, and seating with restrictions.",
    buildsOn: "The multiplication principle from Unit 1.",
    live: true,
  },
  {
    unit: 3,
    slug: "combinations",
    title: "Combinations",
    blurb: "Choosing without order: nCr, committees, at-least and at-most counts, and when order matters vs when it doesn't.",
    buildsOn: "Permutations (Unit 2) — combinations are permutations with the order divided out.",
    live: true,
  },
  {
    unit: 4,
    slug: "binomial-theorem",
    title: "Pascal's Triangle & the Binomial Theorem",
    blurb: "The triangle that counts everything: binomial coefficients, expanding powers, and finding specific terms.",
    buildsOn: "Combinations (Unit 3) — Pascal's triangle IS nCr in disguise.",
    live: true,
  },
  {
    unit: 5,
    slug: "probability-models",
    title: "Probability Models",
    blurb: "Sample spaces, events, equally-likely outcomes, complements, and the addition rule with Venn diagrams.",
    buildsOn: "Counting (Units 1–3) — probability is counting favorable over counting all.",
    live: true,
  },
  {
    unit: 6,
    slug: "conditional-probability",
    title: "Conditional Probability & Independence",
    blurb: "How information changes chance: P(A|B), the multiplication rule, independence, weighted trees, and Bayes by table.",
    buildsOn: "Probability models from Unit 5.",
    live: true,
  },
  {
    unit: 7,
    slug: "random-variables",
    title: "Random Variables & Expected Value",
    blurb: "Turning outcomes into numbers: probability distributions, expected value, variance, and what makes a game fair.",
    buildsOn: "Units 5–6 — distributions are probability models wearing numbers.",
    live: true,
  },
  {
    unit: 8,
    slug: "binomial-distribution",
    title: "The Binomial Distribution",
    blurb: "Repeated independent trials: binomial probabilities, expected count np, shape, and simulation.",
    buildsOn: "Combinations (Unit 3) and random variables (Unit 7) — the course's two halves meet here.",
    live: true,
  },
  {
    unit: 9,
    slug: "describing-data",
    title: "Describing Data",
    blurb: "Center and spread done right: mean, median, IQR, standard deviation, boxplots, and the 1.5×IQR outlier fence.",
    buildsOn: "Expected value (Unit 7) — the mean of data is expectation seen from below.",
    live: true,
  },
  {
    unit: 10,
    slug: "distributions-and-position",
    title: "Distribution Shape & Position",
    blurb: "Histograms and shape, percentiles, z-scores, and the normal curve with the 68–95–99.7 rule.",
    buildsOn: "Center and spread from Unit 9.",
    live: true,
  },
  {
    unit: 11,
    slug: "two-variable-data",
    title: "Two-Variable Data",
    blurb: "Scatterplots, the correlation coefficient, the least-squares line, and why correlation is not causation.",
    buildsOn: "One-variable tools from Units 9–10.",
    live: true,
  },
  {
    unit: 12,
    slug: "inference-and-studies",
    title: "Sampling, Studies & Inference",
    blurb: "Random sampling, bias, experiments vs observation, simulation-based inference, and margin of error — the capstone.",
    buildsOn: "Everything — probability (Units 5–8) judges what data (Units 9–11) shows.",
    live: true,
  },
];

export const VECMAT_SPINE: GeometrySpineEntry[] = [
  {
    unit: 1,
    slug: "vectors-and-coordinates",
    title: "Vectors & Coordinates",
    blurb: "What a vector is, components and magnitude, equal/opposite/parallel vectors, and unit vectors.",
    live: true,
  },
  {
    unit: 2,
    slug: "vector-arithmetic",
    title: "Vector Arithmetic",
    blurb: "Tip-to-tail addition, scaling, subtraction, vectors inside figures, and the section formula.",
    buildsOn: "Components and magnitude from Unit 1.",
    live: true,
  },
  {
    unit: 3,
    slug: "the-dot-product",
    title: "The Dot Product",
    blurb: "u\u00b7v two ways, angles from the sign, perpendicularity tests, and the |u+v|\u00b2 toolbox.",
    buildsOn: "Vector arithmetic from Units 1\u20132.",
    live: true,
  },
  {
    unit: 4,
    slug: "vectors-in-space",
    title: "Vectors in Space",
    blurb: "The third coordinate: 3D magnitudes and dot products, the box diagonal, and normal vectors of planes.",
    buildsOn: "Every 2D formula grows one more term.",
    live: true,
  },
  {
    unit: 5,
    slug: "matrices-and-operations",
    title: "Matrices & Operations",
    blurb: "Grids with an address system: entrywise arithmetic, row-times-column multiplication, identity and powers.",
    buildsOn: "Componentwise thinking from the vector units.",
    live: true,
  },
  {
    unit: 6,
    slug: "determinants-and-inverses",
    title: "Determinants, Inverses & Systems",
    blurb: "ad \u2212 bc, the 2\u00d72 inverse, Cramer's rule, and matrices as transformations \u2014 the capstone.",
    buildsOn: "Matrix multiplication (Unit 5) and the Geometry course's transformation matrices.",
    live: true,
  },
];

export const ALG1_SPINE: GeometrySpineEntry[] = [
  {
    unit: 1,
    slug: "expressions-and-operations",
    title: "Expressions & Operations",
    blurb: "Variables, evaluating and simplifying, exponents, order of operations, and words-to-algebra.",
    live: true,
  },
  {
    unit: 2,
    slug: "linear-equations",
    title: "Solving Linear Equations",
    blurb: "One-step to both-sides equations, fractions and special cases, and rearranging formulas.",
    buildsOn: "Simplifying and the distributive property from Unit 1.",
    live: true,
  },
  {
    unit: 3,
    slug: "inequalities",
    title: "Linear Inequalities",
    blurb: "Solving and graphing, the negative-flip rule, compound and/or, and absolute-value equations.",
    buildsOn: "Equation solving from Unit 2.",
    live: true,
  },
  {
    unit: 4,
    slug: "functions",
    title: "Introduction to Functions",
    blurb: "The one-output rule, f(x) notation, domain and range, and reading real-world graphs.",
    buildsOn: "Evaluating expressions and the coordinate plane.",
    live: true,
  },
  {
    unit: 5,
    slug: "linear-functions",
    title: "Linear Functions & Slope",
    blurb: "Slope as a rate, y = mx + b, point-slope and standard forms, parallel and perpendicular lines.",
    buildsOn: "Functions and their graphs from Unit 4.",
    live: true,
  },
  {
    unit: 6,
    slug: "systems-of-equations",
    title: "Systems of Equations",
    blurb: "Graphing, substitution, elimination, applications, and the no-solution/infinite cases.",
    buildsOn: "Equations (Unit 2) and lines (Unit 5).",
    live: true,
  },
  {
    unit: 7,
    slug: "polynomials-and-factoring",
    title: "Polynomials & Factoring",
    blurb: "Polynomial arithmetic, the special products, and factoring — GCF, trinomials, difference of squares.",
    buildsOn: "Like terms, distribution, and exponent laws from Unit 1.",
    live: true,
  },
  {
    unit: 8,
    slug: "quadratic-equations",
    title: "Quadratic Equations & Functions",
    blurb: "Parabola anatomy, factoring and square roots, completing the square, the formula, the discriminant.",
    buildsOn: "Factoring (Unit 7) and function graphs (Unit 4) — the capstone.",
    live: true,
  },
];

export const IM1_SPINE: GeometrySpineEntry[] = [
  {
    unit: 1,
    slug: "quantities-and-expressions",
    title: "Quantities & the Structure of Expressions",
    blurb:
      "Units, conversion and precision; the terms, factors and coefficients of an expression; writing equations from a situation; rearranging formulas.",
    buildsOn: "Nothing — the course starts here, from zero.",
    live: true,
  },
  {
    unit: 2,
    slug: "linear-equations-and-inequalities",
    title: "Linear Equations & Inequalities",
    blurb:
      "Solving one-variable equations with a reason for every step, special cases, inequalities and the negative-flip rule, and compound statements.",
    buildsOn: "Rearranging formulas from Unit 1 — the same moves, now with a number as the target.",
    live: true,
  },
  {
    unit: 3,
    slug: "functions-and-sequences",
    title: "Functions & Sequences",
    blurb:
      "The one-output rule, function notation, domain and range, and arithmetic and geometric sequences read as functions on the whole numbers.",
    buildsOn: "Creating equations from Unit 1 and solving them from Unit 2.",
    live: true,
  },
  {
    unit: 4,
    slug: "linear-functions",
    title: "Linear Functions & Modelling",
    blurb:
      "Slope as a rate of change, the three forms of a line, graphing from each, and interpreting the parameters of a linear model in context.",
    buildsOn: "Function notation and the sequence-as-function idea from Unit 3.",
    live: true,
  },
  {
    unit: 5,
    slug: "systems-of-equations-and-inequalities",
    title: "Systems of Equations & Inequalities",
    blurb:
      "Graphical, substitution and elimination methods; why adding equations is legal; systems with no or infinitely many solutions; and shaded feasible regions.",
    buildsOn: "Linear equations from Unit 2 and the graph of a line from Unit 4.",
    live: true,
  },
  {
    unit: 6,
    slug: "exponential-functions",
    title: "Exponential Functions & Growth",
    blurb:
      "Repeated multiplication as a function, growth and decay factors, comparing exponential against linear growth, and fitting a model to data.",
    buildsOn: "Geometric sequences from Unit 3 and function notation from Unit 4.",
    live: true,
  },
  {
    unit: 7,
    slug: "transformations-and-congruence",
    title: "Transformations & Congruence",
    blurb:
      "Translations, reflections and rotations as rigid motions; congruence defined by a sequence of them; the triangle congruence criteria; and compass constructions.",
    buildsOn: "The coordinate plane from Unit 4 — transformations are described by coordinate rules.",
    live: true,
  },
  {
    unit: 8,
    slug: "coordinate-geometry",
    title: "Connecting Algebra & Geometry",
    blurb:
      "Distance and midpoint on the plane, the slope criteria for parallel and perpendicular lines, partitioning a segment, and proving geometric facts with coordinates.",
    buildsOn: "Slope from Unit 4 and rigid motions from Unit 7.",
    live: true,
  },
  {
    unit: 9,
    slug: "data-and-statistics",
    title: "Describing Data",
    blurb:
      "Centre and spread for one variable, comparing distributions, outliers, two-way tables, scatter plots and the line of best fit — and why correlation is not causation.",
    buildsOn: "Linear models from Unit 4 — the line of best fit is one.",
    live: true,
  },
];

export const IM2_SPINE: GeometrySpineEntry[] = [
  {
    unit: 1,
    slug: "rational-exponents-and-radicals",
    title: "Rational Exponents & Radicals",
    blurb:
      "Extending the exponent rules to fractional powers, simplifying radicals, and why the sum of a rational and an irrational number is always irrational.",
    buildsOn: "Exponential functions from IM1 Unit 6 — now with the exponent allowed to be a fraction.",
    live: true,
  },
  {
    unit: 2,
    slug: "polynomials-and-factoring",
    title: "Polynomials & Factoring",
    blurb:
      "Adding, subtracting and multiplying polynomials; the closure of the system; and every factoring technique from a common factor to the difference of squares.",
    buildsOn: "The structure of expressions from IM1 Unit 1.",
    live: true,
  },
  {
    unit: 3,
    slug: "quadratic-functions",
    title: "Quadratic Functions",
    blurb:
      "The parabola and its vertex, the three forms of a quadratic and what each reveals, transformations of the graph, and comparing quadratic against linear and exponential growth.",
    buildsOn: "Function notation and linear models from IM1 Units 3 and 4.",
    live: true,
  },
  {
    unit: 4,
    slug: "solving-quadratic-equations",
    title: "Solving Quadratic Equations",
    blurb:
      "Factoring, square roots, completing the square and the quadratic formula; the discriminant; and complex numbers, which arrive because some parabolas never cross the axis.",
    buildsOn: "Factoring from Unit 2 and the shape of a parabola from Unit 3.",
    live: true,
  },
  {
    unit: 5,
    slug: "similarity-and-dilations",
    title: "Similarity & Dilations",
    blurb:
      "Dilation as the one non-rigid transformation, similarity defined by it, the AA criterion, and how similar triangles prove the side-splitter and midsegment theorems.",
    buildsOn: "Congruence and rigid motion from IM1 Unit 7 — similarity is what happens when you add a scale factor.",
    live: true,
  },
  {
    unit: 6,
    slug: "right-triangle-trigonometry",
    title: "Right-Triangle Trigonometry",
    blurb:
      "Sine, cosine and tangent as ratios that similarity makes well defined, the special triangles, solving right triangles, and the complementary-angle relationship.",
    buildsOn: "Similarity from Unit 5 — the trigonometric ratios exist BECAUSE similar triangles share them.",
    live: true,
  },
  {
    unit: 7,
    slug: "circles",
    title: "Circles",
    blurb:
      "Central and inscribed angles, tangents and chords, arc length and sector area, and the equation of a circle derived from the distance formula.",
    buildsOn: "The distance formula from IM1 Unit 8 — a circle is the set of points at a fixed distance from a centre.",
    live: true,
  },
  {
    unit: 8,
    slug: "probability",
    title: "Probability",
    blurb:
      "Sample spaces and events, unions and intersections, conditional probability and independence, two-way tables as probability models, and the addition and multiplication rules.",
    buildsOn: "Two-way tables from IM1 Unit 9 — the same tables, now read as probabilities.",
    live: true,
  },
];

export const IM3_SPINE: GeometrySpineEntry[] = [
  {
    unit: 1,
    slug: "polynomial-functions",
    title: "Polynomial Functions",
    blurb:
      "End behaviour from the leading term, zeros and multiplicity, the remainder and factor theorems, and polynomial arithmetic beyond the quadratic.",
    buildsOn: "Factoring from IM2 Unit 2 — the same techniques, now on cubics and beyond.",
    live: true,
  },
  {
    unit: 2,
    slug: "rational-and-radical-functions",
    title: "Rational & Radical Functions",
    blurb:
      "Simplifying and combining rational expressions, asymptotes and holes, solving rational and radical equations, and why extraneous solutions appear.",
    buildsOn: "Rational exponents from IM2 Unit 1 and factoring from IM2 Unit 2.",
    live: true,
  },
  {
    unit: 3,
    slug: "exponential-and-logarithmic-functions",
    title: "Exponential & Logarithmic Functions",
    blurb:
      "The logarithm as the inverse of an exponential, the three laws and where they come from, solving equations in the exponent, and modelling growth and decay.",
    buildsOn: "Exponential functions from IM1 Unit 6 — now with a way to solve for the exponent.",
    live: true,
  },
  {
    unit: 4,
    slug: "trigonometric-functions",
    title: "Trigonometric Functions",
    blurb:
      "Radian measure and the unit circle, extending the ratios beyond acute angles, the graphs of sine and cosine with amplitude and period, and the Pythagorean identity.",
    buildsOn: "Right-triangle trigonometry from IM2 Unit 6 and radians from IM2 Unit 7.",
    live: true,
  },
  {
    unit: 5,
    slug: "function-families-and-inverses",
    title: "Function Families & Inverses",
    blurb:
      "Transformations applied to every family at once, even and odd symmetry, composing functions, and inverses — what they undo and when they exist.",
    buildsOn: "Transformations of parabolas from IM2 Unit 3, generalised to every function.",
    live: true,
  },
  {
    unit: 6,
    slug: "sequences-series-and-the-binomial-theorem",
    title: "Sequences, Series & the Binomial Theorem",
    blurb:
      "Arithmetic and geometric series and their sum formulas, infinite geometric series and when they converge, and the binomial theorem from Pascal's triangle.",
    buildsOn: "Sequences from IM1 Unit 3 — now summed rather than only listed.",
    live: true,
  },
  {
    unit: 7,
    slug: "statistical-inference",
    title: "Statistical Inference",
    blurb:
      "Populations against samples, random sampling and why it matters, the normal model, simulation, margin of error, and what an experiment can conclude that an observational study cannot.",
    buildsOn: "Describing data from IM1 Unit 9 — from summarising a sample to inferring about a population.",
    live: true,
  },
  {
    unit: 8,
    slug: "modelling-with-functions",
    title: "Modelling with Functions",
    blurb:
      "Choosing a function family from a situation, fitting it to data, judging a model against its residuals, and knowing the range over which it can be trusted.",
    buildsOn: "Every function family in the pathway — this unit is about choosing between them.",
    live: true,
  },
];

export const ALG2_SPINE: GeometrySpineEntry[] = [
  {
    unit: 1,
    slug: "functions-and-transformations",
    title: "Functions & Transformations",
    blurb: "Function notation, domain and range, the four graph moves, absolute value, and piecewise functions.",
    live: true,
  },
  {
    unit: 2,
    slug: "quadratics-and-complex-numbers",
    title: "Quadratics & Complex Numbers",
    blurb: "Vertex form and completing the square, the number i, complex roots, and quadratic inequalities.",
    buildsOn: "Unit 1's transformation recipe and Algebra 1's quadratic toolkit.",
    live: true,
  },
  {
    unit: 3,
    slug: "systems-and-nonlinear-models",
    title: "Systems & Nonlinear Models",
    blurb: "2×2 systems at speed, three variables, curves meeting lines, and feasible regions with the corner principle.",
    buildsOn: "Algebra 1 systems; Unit 2's quadratic solving.",
    live: true,
  },
  {
    unit: 4,
    slug: "polynomial-functions",
    title: "Polynomial Functions",
    blurb: "End behavior, division and the remainder/factor theorems, zeros with multiplicity, and cubic+ equations.",
    buildsOn: "Unit 2's complex roots and Algebra 1 factoring.",
    live: true,
  },
  {
    unit: 5,
    slug: "radicals-and-rational-exponents",
    title: "Radicals & Rational Exponents",
    blurb: "Fractional powers, radical arithmetic, equations with phantom solutions, and inverse functions.",
    buildsOn: "Exponent laws; Unit 1's function machine.",
    live: true,
  },
  {
    unit: 6,
    slug: "exponentials-and-logarithms",
    title: "Exponentials & Logarithms",
    blurb: "Growth and decay, logs as the reverse gear, the three log laws, and solving both equation families.",
    buildsOn: "Unit 5's rational exponents and inverse functions.",
    live: true,
  },
  {
    unit: 7,
    slug: "rational-functions",
    title: "Rational Functions",
    blurb: "Variation, asymptotes and holes, rational-expression arithmetic, and equations with work problems.",
    buildsOn: "Unit 4's factoring.",
    live: true,
  },
  {
    unit: 8,
    slug: "sequences-and-series",
    title: "Sequences & Series",
    blurb: "Arithmetic ladders, geometric rockets, infinite sums, sigma notation, and recursion — the capstone.",
    buildsOn: "Linear (Unit 3) and exponential (Unit 6) thinking, reborn as lists.",
    live: true,
  },
];

export const PRECALC_SPINE: GeometrySpineEntry[] = [
  {
    unit: 1,
    slug: "functions-and-their-graphs",
    title: "Functions & Their Graphs",
    blurb: "Domain, range, and graph features; composition; inverse functions; even/odd symmetry.",
    live: true,
  },
  {
    unit: 2,
    slug: "transformations-of-graphs",
    title: "Transformations of Graphs",
    blurb: "Shifts, stretches, reflections, the combined form a·f(x−h)+k, and piecewise graphs.",
    buildsOn: "Graph features and function notation from Unit 1.",
    live: true,
  },
  {
    unit: 3,
    slug: "polynomial-functions",
    title: "Polynomial Functions",
    blurb: "End behavior, zeros and the Factor Theorem, multiplicity, division and the Remainder Theorem.",
    buildsOn: "Quadratics and factoring from Algebra 1.",
    live: true,
  },
  {
    unit: 4,
    slug: "rational-functions",
    title: "Rational Functions",
    blurb: "Vertical asymptotes, holes, horizontal and slant asymptotes, and complete graphs.",
    buildsOn: "Polynomial zeros and factoring from Unit 3.",
    live: true,
  },
  {
    unit: 5,
    slug: "exponentials-and-logarithms",
    title: "Exponentials & Logarithms",
    blurb: "Growth and decay, compound interest and e, logs as inverses, and exponential/log equations.",
    buildsOn: "Exponent rules and inverse functions (Unit 1).",
    live: true,
  },
  {
    unit: 6,
    slug: "the-unit-circle",
    title: "The Unit Circle",
    blurb: "Radians, sine and cosine as coordinates, special angles, and reference angles in all quadrants.",
    buildsOn: "Right-triangle trig from Geometry.",
    live: true,
  },
  {
    unit: 7,
    slug: "trigonometric-graphs-and-equations",
    title: "Trig Graphs & Equations",
    blurb: "The sine wave, amplitude/period/shifts, fundamental identities, and solving trig equations.",
    buildsOn: "The unit circle (Unit 6) and transformations (Unit 2).",
    live: true,
  },
  {
    unit: 8,
    slug: "conic-sections",
    title: "Conic Sections",
    blurb: "Circles, ellipses, parabolas with foci, hyperbolas, and classifying second-degree equations.",
    buildsOn: "Completing the square and the distance formula — the capstone.",
    live: true,
  },
];

export const CALC_SPINE: GeometrySpineEntry[] = [
  {
    unit: 1,
    slug: "limits-and-continuity",
    title: "Limits & Continuity",
    blurb: "What a function is heading toward: limits from graphs and algebra, limits at infinity, and the definition of an unbroken graph.",
    live: true,
  },
  {
    unit: 2,
    slug: "the-derivative",
    title: "The Derivative",
    blurb: "Secants collapse onto tangents: the difference quotient, the derivative function, the power rule, and the four library derivatives.",
    buildsOn: "Limits from Unit 1.",
    live: true,
  },
  {
    unit: 3,
    slug: "differentiation-techniques",
    title: "Differentiation Techniques",
    blurb: "Product, quotient, and chain rules; combining them, and second derivatives — the whole differentiable world unlocked.",
    buildsOn: "The power rule and library derivatives from Unit 2.",
    live: true,
  },
  {
    unit: 4,
    slug: "applications-of-derivatives",
    title: "Applications of Derivatives",
    blurb: "Tangent and normal lines, rise and fall, peaks and valleys certified two ways, concavity — and optimization, the art of the best.",
    buildsOn: "The full differentiation toolkit from Units 2–3.",
    live: true,
  },
  {
    unit: 5,
    slug: "integrals",
    title: "Integrals",
    blurb: "Differentiation reversed, areas by slicing, and the Fundamental Theorem that collapses infinite sums into one subtraction.",
    buildsOn: "Every derivative from Units 2–3, run backwards.",
    live: true,
  },
  {
    unit: 6,
    slug: "applications-of-integrals",
    title: "Applications of Integrals",
    blurb: "Areas between curves, motion recovered from velocity, average values — and a capstone running the whole course in one arc.",
    buildsOn: "The Fundamental Theorem and substitution from Unit 5.",
    live: true,
  },
];

export const TRIG_SPINE: GeometrySpineEntry[] = [
  {
    unit: 1,
    slug: "right-triangle-trigonometry",
    title: "Right-Triangle Trigonometry",
    blurb: "SOH-CAH-TOA: name the sides, pick the ratio, solve for any missing side or angle — then aim it at towers, ramps, and shadows.",
    live: true,
  },
  {
    unit: 2,
    slug: "special-triangles-and-exact-values",
    title: "Special Triangles & Exact Values",
    blurb: "Half a square and half an equilateral: the two triangles behind every exact value of 30°, 45°, and 60°.",
    buildsOn: "The three ratios from Unit 1.",
    live: true,
  },
  {
    unit: 3,
    slug: "radians-and-the-unit-circle",
    title: "Radians & the Unit Circle",
    blurb: "Angles measured by arc, a circle where cosine and sine ARE the coordinates — and exact values in every quadrant.",
    buildsOn: "The exact-value table from Unit 2.",
    live: true,
  },
  {
    unit: 4,
    slug: "graphs-of-trig-functions",
    title: "Graphs of Trig Functions",
    blurb: "The circle unrolled into a wave: amplitude, period, phase, midline — and tangent's wilder portrait.",
    buildsOn: "The unit circle and periodicity from Unit 3.",
    live: true,
  },
  {
    unit: 5,
    slug: "identities-and-equations",
    title: "Identities & Equations",
    blurb: "The Pythagorean identity, sum and double-angle formulas — and solving equations whose unknown is an angle.",
    buildsOn: "Exact values across quadrants from Unit 3.",
    live: true,
  },
  {
    unit: 6,
    slug: "laws-of-sines-and-cosines",
    title: "Laws of Sines & Cosines",
    blurb: "Trigonometry for EVERY triangle: the sine area formula, both laws, and the strategy for solving any triangle from any three facts.",
    buildsOn: "Right-triangle trig from Unit 1; obtuse angles from Unit 3.",
    live: true,
  },
];

export const SOLIDGEO_SPINE: GeometrySpineEntry[] = [
  {
    unit: 1,
    slug: "lines-and-planes-in-space",
    title: "Lines & Planes in Space",
    blurb: "The rules of 3D: what determines a plane, skew lines, perpendicularity, and the two angles every exam measures.",
    live: true,
  },
  {
    unit: 2,
    slug: "prisms-and-the-cube",
    title: "Prisms & the Cube",
    blurb: "The box family: prism anatomy, the cube's √2 and √3 diagonals, and surface & volume you can see face by face.",
    buildsOn: "Unit 1's perpendicular-and-oblique triangle.",
    live: true,
  },
  {
    unit: 3,
    slug: "pyramids",
    title: "Pyramids",
    blurb: "Height, apothem, slant, edge — the two Pythagorean triangles inside every pyramid, the ⅓ in the volume, and the frustum.",
    buildsOn: "Prisms from Unit 2 (a pyramid is a prism's third).",
    live: true,
  },
  {
    unit: 4,
    slug: "cylinders-and-cones",
    title: "Cylinders & Cones",
    blurb: "The round solids you can unroll: the cylinder's rectangle label, the cone's pie-slice development, and both volumes.",
    buildsOn: "Prisms and pyramids — same formulas, circular bases.",
    live: true,
  },
  {
    unit: 5,
    slug: "spheres",
    title: "Spheres",
    blurb: "Every slice a circle (r² = R² − d²), the surface of exactly four great circles, and Archimedes' tombstone 2:3.",
    buildsOn: "The cylinder and cone from Unit 4.",
    live: true,
  },
  {
    unit: 6,
    slug: "cross-sections-and-similar-solids",
    title: "Cross-Sections & Similar Solids",
    blurb: "Predict any cut, scale with k / k² / k³, glue and drill combined solids — and the five-triangle exam strategy.",
    buildsOn: "All five solid families.",
    live: true,
  },
];

export const IB_SL_SPINE: GeometrySpineEntry[] = [
  {
    unit: 1,
    slug: "number-and-algebra",
    title: "Number & Algebra",
    blurb: "Standard form, sequences and series, money mathematics, exponents and logarithms, proof, infinite sums, and the binomial theorem — SL 1.1 to 1.9.",
    live: true,
  },
  {
    unit: 2,
    slug: "functions",
    title: "Functions",
    blurb: "Straight lines, the function machine, graphs and key features, composites and inverses, quadratics, the discriminant, rationals, exponential and log graphs, solving strategy, and transformations — SL 2.1 to 2.11.",
    buildsOn: "Topic 1's exponent and log machinery.",
    live: true,
  },
  {
    unit: 3,
    slug: "geometry-and-trigonometry",
    title: "Geometry & Trigonometry",
    blurb: "3D geometry, the unit circle, identities, trig equations and graphs, sine and cosine rules — SL 3.1 to 3.8.",
    buildsOn: "Functions and their transformations from Topic 2.",
    live: true,
  },
  {
    unit: 4,
    slug: "statistics-and-probability",
    title: "Statistics & Probability",
    blurb: "Sampling, presenting data, correlation, probability laws, discrete and normal distributions — SL 4.1 to 4.12.",
    buildsOn: "Counting ideas from the binomial theorem (SL 1.9).",
    live: true,
  },
  {
    unit: 5,
    slug: "calculus",
    title: "Calculus",
    blurb: "Limits, differentiation, tangents and optimization, integration and areas — SL 5.1 to 5.11.",
    buildsOn: "Everything: functions, trig, and algebraic fluency.",
    live: true,
  },
];

export const IB_HL_SPINE: GeometrySpineEntry[] = [
  {
    unit: 1,
    slug: "number-and-algebra",
    title: "Number & Algebra (AHL)",
    blurb: "Permutations and the extended binomial theorem, partial fractions, complex numbers from Cartesian to Euler form, De Moivre with powers and roots, proof by induction and contradiction, and 3×3 systems — AHL 1.10 to 1.16.",
    buildsOn: "The whole of SL Topic 1 — sequences, exponents, logarithms, binomial theorem.",
    live: true,
  },
  {
    unit: 2,
    slug: "functions",
    title: "Functions (AHL)",
    blurb: "Factor and remainder theorems, sums and products of roots, rational functions with oblique asymptotes, self-inverse and even/odd structure, modulus equations and inequalities, and the |f|, 1/f, f(|x|) graph family — AHL 2.12 to 2.16.",
    buildsOn: "SL Topic 2's function machinery and transformations.",
    live: true,
  },
  {
    unit: 3,
    slug: "geometry-and-trigonometry",
    title: "Geometry & Trigonometry (AHL)",
    blurb: "Reciprocal and inverse trig, compound angles, and the whole vector toolkit: scalar and vector products, lines and planes in space, intersections and angles — AHL 3.9 to 3.18.",
    buildsOn: "SL Topic 3's unit circle and identities.",
    live: true,
  },
  {
    unit: 4,
    slug: "statistics-and-probability",
    title: "Statistics & Probability (AHL)",
    blurb: "Bayes' theorem, and continuous random variables with probability density functions — mode, median, mean and variance from integrals — AHL 4.13 to 4.14.",
    buildsOn: "SL Topic 4's probability laws and distributions.",
    live: true,
  },
  {
    unit: 5,
    slug: "calculus",
    title: "Calculus (AHL)",
    blurb: "First principles and l'Hôpital, implicit differentiation and related rates, the full derivative library, integration by substitution and parts, volumes of revolution, differential equations, and Maclaurin series — AHL 5.12 to 5.19.",
    buildsOn: "Everything — SL Topic 5 end to end.",
    live: true,
  },
];

// Grade 6 predates the spine convention — every topic shipped live on day
// one, so no roadmap literal existed. This one is the registry order;
// lib/genmath-split.test.ts keeps it in step with the topic data.
export const GRADE6_SPINE: GradeSpineEntry[] = [
  {
    slug: "ratios-and-rates",
    title: "Ratios & Rates",
    blurb: "Ratios compare amounts; rates compare different kinds of things. Master both and you can scale recipes, read maps, spot the best deal, and figure out speed — the math behind everyday choices.",
    live: true,
  },
  {
    slug: "fractions",
    title: "Fractions",
    blurb: "Equivalent fractions, comparing, the four operations, and word problems — taught with bars you can split, merge, and combine.",
    live: true,
  },
  {
    slug: "decimals",
    title: "Decimals",
    blurb: "Place value past the dot, comparing, rounding, and the four operations — built on a 10×10 grid you can shade.",
    live: true,
  },
  {
    slug: "percentages",
    title: "Percentages",
    blurb: "Percent means out of 100 — read on the same 10×10 grid, then converted to fractions and decimals and used on real prices.",
    live: true,
  },
  {
    slug: "integers",
    title: "Integers",
    blurb: "Positive and negative whole numbers on a number line that crosses zero — temperatures, depths, and debts.",
    live: true,
  },
  {
    slug: "factors-and-multiples",
    title: "Factors and Multiples",
    blurb: "Factors, multiples, primes, GCF, and LCM — built from rectangles and skip-counting.",
    live: true,
  },
  {
    slug: "expressions-and-equations",
    title: "Expressions and Equations",
    blurb: "Write and evaluate expressions with exponents and variables, build equivalent expressions, and solve one-step equations.",
    live: true,
  },
  {
    slug: "coordinate-plane",
    title: "Coordinate Plane",
    blurb: "Plot and read points in all four quadrants, reflect across the axes, measure distance, and build polygons on the grid.",
    live: true,
  },
  {
    slug: "geometry-area-volume",
    title: "Geometry: Area and Volume",
    blurb: "Find areas of triangles, parallelograms, trapezoids, and composite figures; put polygons on the coordinate plane; fill and wrap prisms with volume and surface area.",
    live: true,
  },
  {
    slug: "data-and-statistics",
    title: "Data and Statistics",
    blurb: "Ask statistical questions, organize data with dot plots and histograms, and summarize it with mean, median, mode, and range.",
    live: true,
  },
];
