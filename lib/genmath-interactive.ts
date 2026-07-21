// Interactive lesson model + pure interaction logic for the General Math hub.
// The manipulables are config-driven so later topics assemble interactives from
// these parts. All live math goes through the pure functions below so it can be
// unit-tested (scripts/verify-genmath-interactive.test.ts).

import type { GenMathLesson } from "@/lib/genmath-lessons";
import type { LessonProblem } from "@/lib/lesson-types";

// A small illustrated token (a colored chip standing in for cocoa, milk, an
// apple, …). Kept abstract/clean rather than emoji to stay on-brand.
export interface Token {
  label: string; // singular noun, e.g. "cocoa"
  plural: string; // e.g. "cocoa scoops"
  color: string; // CSS color for the chip fill
  glyph?: string; // optional 1-char/emoji hint, used small + decoratively
}

export interface ScalerConfig {
  a: number;
  b: number;
  tokenA: Token;
  tokenB: Token;
  maxBatches: number; // slider runs 1..maxBatches
  goodLabel: string; // e.g. "tastes just right"
}

export interface OrderFlipConfig {
  a: number;
  b: number;
  tokenA: Token;
  tokenB: Token;
  forwardLabel: string; // e.g. "Smooth hot chocolate"
  flippedLabel: string; // e.g. "A cup of mud"
}

export interface CompareGroup {
  count: number;
  token: Token;
}
export interface CompareToggleConfig {
  groupA: CompareGroup;
  groupB: CompareGroup;
}

// Equivalent ratios — a ratio table / double number line the student extends.
export interface RatioTableConfig {
  a: number;
  b: number;
  tokenA: Token;
  tokenB: Token;
  maxCols: number; // how many equivalent columns can be revealed
}

// Comparing ratios — two mixes side by side; reveal which is stronger.
export interface CompareRatio {
  a: number;
  b: number;
  label: string;
  token: Token;
}
export interface RatioCompareConfig {
  left: CompareRatio;
  right: CompareRatio;
  unitNote: string; // e.g. "more orangey" — what "bigger" means here
}

// Rates — a live two-quantity rate calculator (distance/time, items/min, …).
export interface RateMeterConfig {
  topLabel: string;
  topUnit: string;
  top: number;
  topMax: number;
  topStep: number;
  bottomLabel: string;
  bottomUnit: string;
  bottom: number;
  bottomMax: number;
  bottomStep: number;
  rateUnit: string; // e.g. "km per hour"
}

// Unit rate — two deals side by side; reveal the better buy per unit.
export interface Deal {
  label: string;
  price: number;
  qty: number;
}
export interface DealCompareConfig {
  unit: string; // e.g. "bottle"
  currency: string; // e.g. "$"
  dealA: Deal;
  dealB: Deal;
}

// Word problems — scale a known ratio to find the missing value.
export interface ProportionBuilderConfig {
  aLabel: string;
  bLabel: string;
  a: number;
  b: number;
  knownSide: "a" | "b";
  knownValue: number;
  tokenA: Token;
  tokenB: Token;
}

// A visual figure attached to teach steps and problems.
export interface FigureGroupSpec {
  count: number;
  color: string;
  label: string;
  glyph?: string;
}
export interface FigureSpec {
  mode: "groups" | "partToPart" | "partToWhole" | "cross" | "compareMix" | "fractionBar" | "decimalGrid" | "numberLine" | "decimalColumn" | "decimalArea" | "divideChain" | "percentBar" | "percentChange" | "percentChangeFinder" | "integerLine" | "integerAdd" | "geo";
  groups?: FigureGroupSpec[];
  highlightIndex?: number; // the highlighted "part" in partToWhole (default 0)
  // "cross" — a cross-multiply diagram for a:b vs c:d (draws the two diagonals + products).
  cross?: { a: number; b: number; c: number; d: number };
  // "compareMix" — two read-only mixes side by side (juice + water), so a compare
  // question shows BOTH options, never just one.
  mixes?: { a: number; b: number; label?: string }[];
  // "fractionBar" — a bar split into `den` equal pieces with `num` shaded.
  fraction?: { num: number; den: number; label?: string };
  // "decimalGrid" — a 10×10 grid (one whole) with `value` shaded (e.g. 0.37).
  decimal?: { value: number; label?: string };
  // "numberLine" — a number line (default 0..1, ticks at tenths) with points plotted.
  numberLine?: { min?: number; max?: number; points: { value: number; label?: string; color?: string }[] };
  // "decimalColumn" — a stacked add/subtract with the decimal points aligned.
  column?: { a: number; b: number; op: "add" | "sub" };
  // "decimalArea" — an area model (a across × b up) with the product rectangle.
  area?: { a: number; b: number };
  // "divideChain" — the shift transformation a ÷ b = (a·10ⁿ) ÷ (b·10ⁿ) = quotient.
  divide?: { dividend: number; divisor: number };
  // "percentBar" — a 0–100% bar aligned to a 0–whole value bar (percent of a number).
  percentBar?: { whole: number; percent: number };
  // "percentChange" — a price bar splitting into pay+discount, or extended by tax/tip.
  percentChange?: { original: number; percent: number; mode: "discount" | "increase"; currency?: string };
  // "percentChangeFinder" — before/after bars with the percent increase/decrease.
  percentChangeFinder?: { original: number; final: number; currency?: string };
  // "integerLine" — a number line across zero with integers marked. `highlight`
  // draws a distance band from zero (for absolute value).
  integerLine?: { min: number; max: number; points: { value: number; label?: string; color?: string }[]; highlight?: number };
  // "integerAdd" — a number-line jump from a by b, landing at a + b.
  integerAdd?: { a: number; b: number; min: number; max: number };
  // "geo" — a static geometry diagram (points/segments/rays/lines/angle arcs).
  geo?: GeoDiagramSpec;
}

// Fractions — a bar you split into more (equal) pieces to see equivalent fractions.
export interface FractionScalerConfig {
  num: number;
  den: number;
  maxSplit: number; // split each piece into 1..maxSplit
  color?: string;
}

// Fractions — a bar whose pieces you merge to reach simplest form.
export interface FractionSimplifyConfig {
  num: number;
  den: number;
  color?: string;
}

// Comparing — two bars; give them the same-size pieces (common denominator), then compare.
export interface FractionCompareConfig {
  left: { num: number; den: number; label?: string };
  right: { num: number; den: number; label?: string };
  color?: string;
}

// Add/subtract — match the pieces, then combine the shaded amounts.
export interface FractionCombineConfig {
  left: { num: number; den: number };
  right: { num: number; den: number };
  op: "add" | "sub";
  color?: string;
}

// Multiply — an area model: shade columns (first fraction) × rows (second fraction).
export interface AreaModelConfig {
  aNum: number;
  aDen: number;
  bNum: number;
  bDen: number;
}

// Divide — a measurement model: how many of the divisor fit into the dividend.
export interface FractionDivideConfig {
  dividend: { num: number; den: number };
  divisor: { num: number; den: number };
}

export interface NotationToggleConfig {
  a: number;
  b: number;
  tokenA: Token;
  tokenB: Token;
}

// Decimals — a 10×10 grid that is ONE whole. Filled tenths read as full
// columns, loose hundredths as single cells, so place value is literal. The
// student taps ±0.1 / ±0.01 to build a decimal and watch the grid + fraction
// update in lockstep.
export interface DecimalGridConfig {
  start: number; // initial value in [0, 1], a multiple of 0.01 (e.g. 0.37)
  color?: string;
}

// Comparing decimals — two grids side by side; the student taps <, =, or >
// and gets instant feedback. Targets the "more digits = bigger" misconception
// (0.5 shades more than 0.45).
export interface DecimalCompareConfig {
  left: number; // a value in [0, 1], multiple of 0.01
  right: number;
  color?: string;
}

// Rounding decimals — a number line zoomed to the two bracketing marks at the
// chosen place, with the midpoint shown. The student taps which mark the value
// is nearer; rounding becomes "the closer tick, halfway rounds up".
export interface DecimalRounderConfig {
  value: number;
  place: "whole" | "tenth" | "hundredth";
  color?: string;
}

// Adding / subtracting decimals — a stacked column with the decimal points in a
// vertical line and missing places padded with faded zeros, so "line up the
// points" is literal. The answer reveals on tap.
export interface DecimalColumnConfig {
  a: number;
  b: number;
  op: "add" | "sub";
  color?: string;
}

// Multiplying decimals — an area model on the unit square. One factor runs
// across (columns of tenths), the other up (rows of tenths); the overlap
// rectangle is the product in hundredths (0.3 × 0.4 = 12 squares = 0.12).
// Both factors are tenths (0.1–0.9), so the product fits in one whole.
export interface DecimalAreaConfig {
  a: number; // 0.1–0.9
  b: number; // 0.1–0.9
  color?: string;
}

// Dividing decimals — shift both numbers by ×10 until the divisor is a whole
// number, watching the quotient stay the same: 4.8 ÷ 0.6 → 48 ÷ 6 = 8.
export interface DecimalDivideConfig {
  dividend: number;
  divisor: number;
  color?: string;
}

// Percent — the 10×10 grid is literally "out of 100", so n squares shaded is
// n%. The readout shows the percent, its fraction over 100, and the decimal.
export interface PercentGridConfig {
  start: number; // a percent, 0–100
  color?: string;
}

// Percent of a number — a double bar: a 0–100% scale aligned to a 0–whole
// value scale, so the marker reads both at once (25% of 80 = 20).
export interface PercentBarConfig {
  whole: number;
  start: number; // a percent, 0–100
  color?: string;
}

// Percent word problems — a price bar that either splits into "you pay" +
// "discount" (mode: discount) or extends by "+ tax/tip" (mode: increase),
// with a stepper on the percent. Models real sales, tax, and tips.
export interface PercentChangeConfig {
  original: number;
  start: number; // the percent, 0–100
  mode: "discount" | "increase";
  currency?: string; // default "$"
  color?: string;
}

// Percent increase / decrease — a before/after bar pair with the change
// highlighted; the percent change (out of the ORIGINAL) reveals on tap.
export interface PercentChangeFinderConfig {
  original: number;
  final: number;
  currency?: string; // default "$"
  color?: string;
}

// Integers — a number line crossing zero (negatives left, positives right)
// with a marker the student moves by ±1, reading the integer value.
export interface IntegerLineConfig {
  min: number;
  max: number;
  start: number;
  color?: string;
}

// Comparing integers — two integers plotted on one line; the student taps <,
// =, or >. Targets the "−5 > −2" misconception (further left is smaller).
export interface IntegerCompareConfig {
  left: number;
  right: number;
  min: number;
  max: number;
  color?: string;
}

// Adding integers — a number-line jump: start at a, hop b units (right if
// positive, left if negative), landing at a + b.
export interface IntegerAddConfig {
  a: number;
  b: number;
  min: number;
  max: number;
  color?: string;
}

// Multiplying / dividing integers — flip each factor's sign and watch the
// result's sign follow the rule: same signs → positive, different → negative.
export interface IntegerSignRuleConfig {
  a: number;
  b: number;
  op: "mul" | "div";
  color?: string;
}

// Factors — arrange n squares into a rectangle of a chosen width. A width that
// divides n evenly forms a complete rectangle and reveals a factor pair.
export interface FactorPairsConfig {
  n: number;
  color?: string;
}

// Factor finder — steps through candidate divisors 1, 2, 3, … testing each,
// pairing every divisor d with n/d, and building the ordered list of ALL
// factors, then draws a "factor rainbow" of the pairs. Teaches the METHOD of
// listing factors in order (and why you can stop at √n).
export interface FactorFinderConfig {
  n: number;
  color?: string;
}

// Multiples — a 1..max number grid where the multiples of a chosen number light
// up, making skip-counting visible.
export interface MultiplesGridConfig {
  max: number;
  start: number; // the number whose multiples are shown
  color?: string;
}

// Prime & composite — a 2..max grid with primes highlighted; tap any number to
// see its factor list and the prime/composite verdict.
export interface PrimeExplorerConfig {
  max: number;
  start: number; // number inspected first
  color?: string;
}

// Greatest common factor — two adjustable numbers, their factor lists shown as
// chips with shared factors highlighted and the greatest one ringed.
export interface GcfFinderConfig {
  a: number;
  b: number;
  min?: number;
  max?: number;
  color?: string;
}

// Least common multiple — two adjustable numbers, their multiples shown as
// strips with shared multiples highlighted and the least one ringed.
export interface LcmFinderConfig {
  a: number;
  b: number;
  min?: number;
  max?: number;
  count?: number; // how many multiples to show per number
  color?: string;
}

// Prime factorization — a factor tree that peels the smallest prime factor one
// step at a time until only primes remain.
export interface FactorTreeConfig {
  n: number;
  color?: string;
}

// Exponents — pick a base and exponent; the repeated-multiplication expansion
// and the value appear.
export interface ExponentBuilderConfig {
  base: number;
  exp: number;
  minBase?: number;
  maxBase?: number;
  minExp?: number;
  maxExp?: number;
  color?: string;
}

// Order of operations — step through an expression one operation at a time.
// Each stage is the running expression plus a note on the step just taken.
export interface OrderOfOpsConfig {
  stages: { expr: string; did?: string }[];
  color?: string;
}

// Algebra tiles — visualize ax + b as x-tiles and unit squares. "build" mode has
// steppers; "collect" mode scatters then groups (combining like terms).
export interface AlgebraTilesConfig {
  x: number;
  units: number;
  mode?: "build" | "collect";
  maxX?: number;
  maxUnits?: number;
  color?: string;
}

// Evaluating — a substitution slider for a·x + b: drag the variable's value and
// watch the expression's value update.
export interface EvaluatorConfig {
  a: number;
  b: number;
  varName?: string;
  min?: number;
  max?: number;
  start?: number;
  color?: string;
}

// One-step equations — a pan balance. "add" mode solves x + b = rhs by removing
// b from both sides; "mul" mode solves coef·x = rhs by splitting into groups.
export interface BalanceScaleConfig {
  mode: "add" | "mul";
  coef?: number;
  b?: number;
  rhs: number;
  color?: string;
}

// Coordinate plane — a reusable SVG grid with several modes:
//  plot / identify (tap) / quadrants / reflect (across an axis) / distance.
export interface GridPoint {
  x: number;
  y: number;
  label?: string;
  color?: string;
}
export interface CoordinateGridConfig {
  min?: number;
  max?: number;
  mode: "plot" | "identify" | "quadrants" | "reflect" | "distance";
  points?: GridPoint[];
  reflectAxis?: "x" | "y";
  polygon?: boolean; // plot mode: connect the points into a closed shape
  // identify mode: also shade + label the four quadrants, and report which
  // quadrant (or axis) the tapped point falls in — a "which quadrant" playground.
  showQuadrants?: boolean;
  color?: string;
}

// ---------------------------------------------------------------------------
// Geometry course — declarative diagram spec + interactive configs
// ---------------------------------------------------------------------------

// A named point in abstract diagram units (y up; the renderer flips).
export interface GeoPointSpec {
  id: string;
  x: number;
  y: number;
  label?: string; // defaults to id; "" hides the label
  labelDx?: number; // fine-tune label placement, in diagram units
  labelDy?: number;
}

// A drawable object referencing points by id.
export type GeoObjectSpec =
  // segment: both ends fixed; ray: from → through to, extended past `to`;
  // line: extended past both ends. `ticks` draws congruence marks at the middle.
  // `label` sits at the midpoint, offset to the side away from the figure.
  | { kind: "segment" | "ray" | "line"; from: string; to: string; label?: string; color?: string; ticks?: number; dashed?: boolean }
  // angle arc at vertex `at` between rays toward `from` and `to` (small arc).
  // `right` draws the square corner instead. `label` sits along the arc.
  | { kind: "angle"; at: string; from: string; to: string; label?: string; color?: string; right?: boolean; radius?: number };

// A complete static diagram (renders in GeoDiagram; also the figure "geo" mode).
export interface GeoDiagramSpec {
  points: GeoPointSpec[];
  objects: GeoObjectSpec[];
  hidePoints?: string[]; // point ids to use for geometry but not draw
  height?: number; // px height cap (default 200)
}

// The interactive canvas — Unit 1's foundation. Modes:
//  lineThrough:     two draggable points and the unique line through them.
//  entityToggle:    same two points; switch line / ray AB / ray BA / segment.
//  segmentAddition: B slides along AC; AB + BC = AC live, snap-to-midpoint.
export interface GeoCanvasConfig {
  mode: "lineThrough" | "entityToggle" | "segmentAddition";
  total?: number; // segmentAddition: length of AC (default 10)
  start?: number; // segmentAddition: initial AB (default 3)
  color?: string;
}

// A fixed-length segment above a slidable ruler: the endpoint readings change,
// their difference never does.
export interface SegmentRulerConfig {
  length: number; // segment length in ruler units
  max: number; // ruler runs 0..max
  start?: number; // initial left reading
  color?: string;
}

// The protractor: fixed ray at 0°, draggable ray with live degree readout.
// classify adds the acute/right/obtuse/straight label; bisector draws the
// tracking half-angle ray with equal-angle tick arcs.
export interface ProtractorConfig {
  initial: number; // starting measure in degrees (0..180)
  classify?: boolean;
  bisector?: boolean;
  labels?: { vertex: string; fixed: string; moving: string }; // default B / C / A → reads m∠ABC
  color?: string;
}

// Two lines crossing (mode "crossing": vertical + linear pairs) or a right
// angle split by a ray (mode "corner": complementary pairs).
export interface AnglePairFinderConfig {
  mode: "crossing" | "corner";
  initial?: number; // crossing: tilt of line 2 (20..160); corner: middle ray (10..80)
  color?: string;
}

// A two-column statements/reasons proof revealed one row at a time.
export interface StepProofConfig {
  given: string;
  prove: string;
  rows: { statement: string; reason: string }[];
}

// A growing visual pattern revealed stage by stage (inductive reasoning).
export interface PatternGrowConfig {
  pattern: "odds" | "doubling";
  maxSteps?: number;
}

// A conjecture on trial: tap candidates to test; one failure = counterexample.
export interface ConjectureTestConfig {
  conjecture: string;
  items: { label: string; holds: boolean; note: string }[];
}

// An if-then statement whose hypothesis/conclusion swap into the converse.
export interface ConditionalFlipConfig {
  hypothesis: string;
  conclusion: string;
  statementTrue: boolean;
  converseTrue: boolean;
  statementNote: string;
  converseNote: string;
}

// Two lines cut by a transversal — the eight angles, with a pair highlighter
// and a parallel toggle. The engine of the Parallel & Perpendicular unit.
export interface TransversalConfig {
  acute?: number; // acute angle the transversal makes with the lines (35..90)
  highlight?: "none" | "corresponding" | "altInterior" | "altExterior" | "sameSideInterior" | "vertical" | "linearPair";
  interactive?: boolean; // show pair selector + tilt stepper
  showParallelToggle?: boolean; // let the student break parallelism
  startParallel?: boolean;
  showMeasures?: boolean; // print each angle's degree instead of its number
}

// A triangle reshaped by its two base angles; the third completes 180°. In
// exterior mode the base extends and the exterior angle (= sum of remote
// interiors) is shown.
export interface TriangleAnglesConfig {
  beta?: number; // ∠B (bottom-left)
  gamma?: number; // ∠C (bottom-right)
  exterior?: boolean;
  color?: string;
}

// Three side lengths that try to close into a triangle (Triangle Inequality).
export interface TriangleInequalityConfig {
  a?: number;
  b?: number;
  c?: number;
  max?: number;
}

// One triangle with a chosen set of concurrent special segments and the point
// where they meet: perpendicular bisectors → circumcenter, angle bisectors →
// incenter, medians → centroid, altitudes → orthocenter. Optionally draws the
// circumscribed / inscribed circle. One primitive serves Unit-5 lessons 1–4.
export interface TriangleCentersConfig {
  center: "circumcenter" | "incenter" | "centroid" | "orthocenter";
  triangle?: [[number, number], [number, number], [number, number]]; // A, B, C
  showCircle?: boolean; // circumcircle / incircle where meaningful
  caption?: string;
  color?: string;
}

// The Midsegment Theorem, live: the segment joining two side-midpoints is
// parallel to the third side and half as long. "one" draws a single midsegment
// against its parallel base; "all" draws the medial triangle (four congruent
// pieces). `base` (0,1,2 = AB, BC, CA) is the side the midsegment parallels.
export interface MidsegmentConfig {
  triangle?: [[number, number], [number, number], [number, number]]; // A, B, C
  show?: "one" | "all";
  base?: number; // which side the drawn midsegment is parallel to
  caption?: string;
  color?: string;
}

// A regular n-gon whose vertex count the student changes. "interior" mode
// fan-triangulates from one vertex (n − 2 triangles) to show the interior sum
// (n − 2)·180°; "exterior" mode shows the turn arrows that always total 360°.
export interface PolygonAnglesConfig {
  start?: number; // initial number of sides (3..10)
  minSides?: number;
  maxSides?: number;
  mode?: "interior" | "exterior";
  color?: string;
}

// A canonical quadrilateral of a chosen type, drawn with the property marks
// that define it (parallel arrows, congruence ticks, right-angle squares,
// equal-angle arcs) and, on tap, its diagonals and their properties. One
// primitive serves the whole quadrilateral family.
export interface QuadShapeConfig {
  type: "parallelogram" | "rectangle" | "rhombus" | "square" | "trapezoid" | "isosceles-trapezoid" | "kite";
  showDiagonals?: boolean;
  caption?: string;
  color?: string;
}

// Two similar triangles side by side with an adjustable scale factor k. Same
// shape, different size: corresponding angles stay equal, every side is k times
// its match, the perimeter scales by k and the area by k². Serves Unit-7
// lessons on similar figures, similarity shortcuts, and perimeter/area ratios.
export interface SimilarFiguresConfig {
  start?: number; // initial scale factor (×10 internally is avoided; use halves)
  show?: "sides" | "measures"; // readout emphasis: side ratio, or perimeter+area
  color?: string;
}

// A triangle cut by a line parallel to its base (the Side-Splitter setup). A
// slider slides the parallel line; the two sides are always split in the same
// ratio — the Triangle Proportionality Theorem, live.
export interface SideSplitterConfig {
  ab?: number; // length of the left side AB
  ac?: number; // length of the right side AC
  start?: number; // initial fraction of the way down (0..1)
  color?: string;
}

// A figure and its dilation image from a center, with an adjustable scale
// factor k. The image lies on the rays from the center, k times as far; k > 1
// enlarges, 0 < k < 1 reduces. For the dilations lesson.
export interface DilationConfig {
  start?: number; // initial k
  color?: string;
}

// A right triangle with a square drawn on each side, so the areas make
// a² + b² = c² literal (the classic Pythagorean picture). The two legs are
// adjustable. For the Pythagorean-theorem lessons.
export interface PythagoreanSquaresConfig {
  a?: number; // horizontal leg
  b?: number; // vertical leg
  color?: string;
}

// A 45-45-90 or 30-60-90 triangle with its fixed side ratios labelled and a
// size stepper. For the special-right-triangles lesson.
export interface SpecialTriangleConfig {
  type: "45-45-90" | "30-60-90";
  start?: number; // the base length x
  color?: string;
}

// A right triangle with an adjustable acute angle θ. Labels the opposite,
// adjacent, and hypotenuse relative to θ and shows sin, cos, tan (SOH-CAH-TOA)
// with live values. For the trigonometry lessons.
export interface TrigRatiosConfig {
  start?: number; // initial angle in degrees
  color?: string;
}

// A declarative circle diagram: centre O, labelled points placed on the circle
// by angle, and objects between them (chords, radii, diameters, secants,
// tangents), plus angle marks and a highlighted arc with its measure. The
// static circle renderer for the Circles unit.
export interface CirclePointSpec { id: string; deg: number; label?: string }
export type CircleObjectSpec =
  | { kind: "chord" | "radius" | "diameter" | "secant"; from: string; to: string; color?: string; ticks?: number; dashed?: boolean }
  | { kind: "tangent"; at: string; color?: string }; // tangent line at a point on the circle
export interface CircleAngleMark { at: string; from: string; to: string; label?: string; right?: boolean; color?: string }
export interface CircleArcMark { from: string; to: string; label?: string; color?: string }
export interface CircleFigureConfig {
  radius?: number;
  points?: CirclePointSpec[];
  objects?: CircleObjectSpec[];
  angles?: CircleAngleMark[];
  arcs?: CircleArcMark[];
  external?: { id: string; deg: number; dist: number; label?: string; tangents?: boolean; secantTo?: [string, string] };
  showCenter?: boolean;
  caption?: string;
}

// A circle with an adjustable central angle. "central" mode shows the central
// angle equal to its intercepted arc; "inscribed" mode adds an inscribed angle
// on the same arc, always half the central angle (Inscribed Angle Theorem).
export interface CircleAngleConfig {
  mode: "central" | "inscribed";
  start?: number; // central angle in degrees
  color?: string;
}

// A circle with an external point and the two tangent lines from it: each
// tangent meets the radius at a right angle, and the two tangent segments are
// equal. Reveals on tap.
export interface TangentCircleConfig {
  color?: string;
}

// A circle with an adjustable central angle showing the sector's arc length
// (θ/360 of the circumference) and area (θ/360 of the circle's area).
export interface ArcSectorConfig {
  start?: number; // central angle
  radius?: number; // the labelled radius value
  color?: string;
}

// The bivariate-data workbench: an animated scatter plot with four modes —
// points rain in (plot), datasets morph between correlation shapes
// (correlation), a stray point pulses (outlier), and a line-fitting game
// scores the average miss against the least-squares fit (fit).
export interface ScatterPlotConfig {
  mode: "plot" | "correlation" | "outlier" | "fit";
  dataset?: "positive" | "negative" | "none";
  xLabel?: string;
  yLabel?: string;
  m0?: number; // fit mode: starting slope
  b0?: number; // fit mode: starting intercept
}

// The quadratic-functions workbench — one animated parabola, five modes:
// shape (y = ax², stepper on a), vertex (y = a(x−h)²+k, steppers on h/k),
// standard (y = ax²+bx+c, steppers on b/c, axis/vertex/y-intercept computed
// live), roots (stepper on k: two crossings → kiss → none), and projectile
// (auto-playing ball along h = v₀t − 5t² with the vertex marked at the apex).
export interface ParabolaGraphConfig {
  mode: "shape" | "vertex" | "standard" | "roots" | "projectile";
  a?: number; // shape: starting a; vertex/roots: fixed a (default 1)
  h?: number; // vertex: starting h; roots: fixed h
  k?: number; // vertex/roots: starting k
  b?: number; // standard: starting b
  c?: number; // standard: starting c
  v0?: number; // projectile: launch speed (default 20 → h = 20t − 5t²)
  interactive?: boolean;
  min?: number;
  max?: number;
}

// The polynomial workbench: endBehavior (y = ±xⁿ, degree stepper + sign flip,
// arm arrows), zeros (a factored cubic with one movable zero), and
// multiplicity (cross / bounce / flatten-through at a repeated zero).
export interface PolyGraphConfig {
  mode: "endBehavior" | "zeros" | "multiplicity";
  n?: number; // endBehavior: starting degree
  negative?: boolean; // endBehavior: leading sign
  zeros?: [number, number, number]; // zeros: the cubic's roots (third is steppable)
  m?: number; // multiplicity: starting multiplicity at x = 1
}

// The exponential workbench: growth (y = a·bˣ with steppers, ×b ratio chips),
// race (exponential vs line, auto-swept with the overtake marked), and
// compound (a balance compounding year by year as growing bars).
export interface ExpGraphConfig {
  mode: "growth" | "race" | "compound";
  a?: number; // growth: starting value (y-intercept)
  b?: number; // growth/race: the base
  m?: number; // race: the line's slope
  p?: number; // compound: principal
  r?: number; // compound: rate per year (e.g. 0.1)
  years?: number; // compound: years shown
  interactive?: boolean;
}

// The trigonometry workbench: radians (radius-arcs wrap the rim), explore (an
// angle stepper drives the unit-circle point; the inner right triangle shows
// cos/sin as coordinates), and wave (an orbiting point traces the sine curve
// onto a scroll — auto-play with replay).
export interface UnitCircleConfig {
  mode: "radians" | "explore" | "wave";
  start?: number; // explore: initial angle in degrees
}

// The complex-numbers workbench (HL). plot: z = a + bi as an Argand arrow
// with |z|, arg z, and the conjugate mirrored in the real axis; powers: the
// De Moivre spiral (moduli multiply, arguments add), |z| stepper crossing 1;
// roots: the n-th roots of a unit-modulus target as a regular n-gon whose
// first vertex sits at (arg w)/n.
export interface ArgandPlotConfig {
  mode: "plot" | "powers" | "roots";
  a?: number; // plot: initial Re(z)
  b?: number; // plot: initial Im(z)
  r?: number; // powers: base modulus (0.85 | 1 | 1.1 look best)
  thetaDeg?: number; // powers: base argument in degrees
  n?: number; // powers: initial power; roots: initial n
  targetDeg?: number; // roots: argument of the target w
  showConjugate?: boolean; // plot: mirror z̄ below the real axis
}

// The limits workbench: two dots close in on a target x from both sides.
// approach: the squeeze finds the limit; hole: the limit exists where the
// value doesn't; jump: one-sided limits disagree (DNE); infinite: outputs
// blow up along a vertical asymptote (auto-played with replay).
export interface LimitGraphConfig {
  mode: "approach" | "hole" | "jump" | "infinite";
}

// The derivatives workbench on f(x) = x²/2 (slope at x is exactly x).
// secant: an h-stepper collapses the secant onto the tangent — the definition
// drawn; tangent: slide the touch point, slope readout goes downhill/flat/
// uphill; slopeCurve: f and f′ share the grid — the derivative is a function.
export interface TangentGraphConfig {
  mode: "secant" | "tangent" | "slopeCurve";
}

// The vectors workbench: components (one arrow, dashed legs, live magnitude),
// add (tip-to-tail with a springing resultant), dot (term-by-term dot product
// whose sign calls the angle: acute / right / obtuse).
export interface VectorGraphConfig {
  mode: "components" | "add" | "dot";
}

// The conic-sections workbench: circle (center + radius steppers), ellipse
// (a/b steppers, foci beacons, live eccentricity, axis swap), parabola
// (p-stepper, focus beacon + dashed directrix), hyperbola (a/b steppers,
// dashed asymptotes, foci outside).
export interface ConicGraphConfig {
  mode: "circle" | "ellipse" | "parabola" | "hyperbola";
}

// The integrals workbench. riemann: left-endpoint rectangles under x² on
// [0,2] with an n-stepper — the staircase melts into the curve chasing 8/3;
// accumulate: auto-played sweep filling area behind a moving edge, readout
// A(x) = x³/3 — area as a function; ftc: f(x) = x on [0,b], triangle geometry
// vs the antiderivative, agreeing at every b.
export interface AreaGraphConfig {
  mode: "riemann" | "accumulate" | "ftc";
}

// Two lines y = m1x + b1 and y = m2x + b2 on one grid; line 2 adjustable.
// Marks the intersection (the system's solution) and calls parallel /
// same-line verdicts live. The systems-of-equations workbench.
export interface SystemGraphConfig {
  m1: number; b1: number;
  m2: number; b2: number;
  interactive?: boolean;
  min?: number; max?: number;
}

// A circle rolling one full turn along a line, unrolling its circumference —
// π played out as "a little more than 3 diameters". Auto-plays with a replay.
export interface CircleUnrollConfig {
  color?: string;
}

// A shape with its base/height (or diagonals) labelled and its area computed
// live from an adjustable set of dimensions. Serves the area lessons for
// parallelograms, triangles, trapezoids, and rhombi.
export interface AreaShapeConfig {
  shape: "rectangle" | "parallelogram" | "triangle" | "trapezoid" | "rhombus";
  base?: number;
  height?: number;
  base2?: number; // trapezoid top base
  d1?: number; // rhombus horizontal diagonal
  d2?: number; // rhombus vertical diagonal
  color?: string;
}

// A regular polygon whose side count the student changes, split into n triangles
// from the centre. The apothem is each triangle's height, so the area is
// ½ · apothem · perimeter. For the regular-polygon area lesson.
export interface ApothemPolygonConfig {
  start?: number; // initial number of sides
  side?: number; // side length (label)
  color?: string;
}

// A composite figure built from positioned rectangles, triangles, and
// circles/semicircles, each added or subtracted. Areas are authored (exact) so
// the breakdown readout is honest; the renderer just draws and tallies.
export interface CompositePart {
  kind: "rect" | "triangle" | "circle" | "semicircle";
  op?: "add" | "subtract";
  x?: number; y?: number; w?: number; h?: number; // rect
  pts?: [number, number][]; // triangle
  cx?: number; cy?: number; r?: number; half?: "top" | "bottom" | "left" | "right"; // circle / semicircle
  area?: string; // authored area label (e.g. "24" or "8π")
  label?: string;
  color?: string;
}
export interface CompositeAreaConfig {
  width: number;
  height: number;
  parts: CompositePart[];
  total?: string; // authored total-area label
  caption?: string;
}

// A 3-D solid drawn in oblique projection with adjustable dimensions and live
// volume + surface-area readouts. One primitive covers prisms, cylinders,
// pyramids, cones, and spheres.
export interface Solid3DConfig {
  solid: "rectPrism" | "triangularPrism" | "cylinder" | "pyramid" | "cone" | "sphere";
  l?: number; w?: number; h?: number; // box / prism
  r?: number; // cylinder / cone / sphere radius
  slant?: number; // cone slant height (for surface area)
  base?: number; // pyramid base side
  color?: string;
}

// A solid unfolded into its flat net, so surface area reads as the sum of the
// face areas. Supports the rectangular prism (6 rectangles) and the cylinder
// (two circles + a wrapped rectangle).
export interface SolidNetConfig {
  solid: "rectPrism" | "cylinder";
  l?: number; w?: number; h?: number;
  r?: number;
  color?: string;
}

// A coordinate-geometry figure on the plane with a tap-to-reveal computation:
// distance (via the run/rise right triangle), midpoint, slope (rise/run), a
// line y = mx + b, or a circle (x−h)²+(y−k)²=r².
export interface CoordGeoConfig {
  mode: "distance" | "midpoint" | "slope" | "line" | "circle";
  a?: { x: number; y: number }; // first point (distance / midpoint / slope)
  b?: { x: number; y: number }; // second point
  m?: number; // line slope
  yint?: number; // line y-intercept
  center?: { x: number; y: number }; // circle center
  r?: number; // circle radius
  min?: number; max?: number; // grid extent (default -6..6)
  color?: string;
}

// One figure and its image under a single transformation on the coordinate
// plane: a slide, flip, turn, or resize. Tapping reveals the image and the
// per-vertex coordinate mapping.
export interface TransformPlaneConfig {
  transform: "translate" | "reflectX" | "reflectY" | "reflectYeqX" | "rotate" | "dilate";
  shape?: { x: number; y: number }[]; // preimage vertices; default a right triangle
  dx?: number; dy?: number; // translation vector
  deg?: 90 | 180 | 270; // rotation about the origin
  k?: number; // dilation scale factor
  min?: number; max?: number; // grid extent (default -6..6)
  color?: string;
}

// Two congruent triangles with marked parts; the student names the shortcut.
export interface CongruentTrianglesConfig {
  sides?: [number, number, number]; // tick counts on AB, BC, CA
  angles?: [number, number, number]; // arc counts at A, B, C
  rightAngleAt?: number; // vertex index (0=A,1=B,2=C) with a right-angle square, or -1
  answer: "SSS" | "SAS" | "ASA" | "AAS" | "HL";
  caption?: string;
}

// ---------------------------------------------------------------------------
// Probability & statistics widgets
// ---------------------------------------------------------------------------

// A branching tree drawn left-to-right. "count" mode counts leaves (the
// multiplication principle made visible); "prob" mode labels each branch with
// its probability and multiplies along a tapped path. Stage options can vary
// by the path so far (byPath, keyed by the labels walked, joined with ""),
// which draws conditional trees: shrinking choices, without-replacement draws.
export interface TreeOption {
  label: string;
  p?: number; // branch probability as a decimal (prob mode)
  pLabel?: string; // branch probability as displayed, e.g. "1/2"
}
export interface TreeStage {
  name?: string; // stage caption, e.g. "shirt"
  options?: TreeOption[]; // same options whatever came before
  byPath?: Record<string, TreeOption[]>; // options keyed by joined path labels
}
export interface TreeDiagramConfig {
  mode: "count" | "prob";
  stages: TreeStage[];
  caption?: string;
}

// Pascal's triangle explorer. build: a stepper reveals rows, each entry the
// sum of the two above; sums: row totals appear at the right (powers of 2);
// combinations: tap any cell for its C(n, k) reading; expansion: a row
// stepper writes out (a+b)^n with the row as its coefficients.
export interface PascalTriangleConfig {
  mode: "build" | "sums" | "combinations" | "expansion";
  rows?: number; // deepest row shown (default 6)
}

// A street grid where the number at each corner counts the paths from Start
// (top-left) walking only right/down — Pascal's triangle tilted 45°. A
// stepper fills the corners diagonal by diagonal; the finish shows C(m+n, m).
export interface PathGridConfig {
  cols: number; // blocks across (right-moves needed)
  rows: number; // blocks down (down-moves needed)
}

// Two overlapping circles with live region counts. regions: tap a region to
// read it (only A, both, only B, neither); addition: plays the double-count
// story — |A| + |B| counts the overlap twice, so subtract it once.
export interface VennCountsConfig {
  mode: "regions" | "addition";
  labelA: string;
  labelB: string;
  onlyA: number;
  onlyB: number;
  both: number;
  neither?: number;
  countNoun?: string; // e.g. "students" (default "outcomes")
}

// The long-run frequency machine: run an event with true probability p in
// batches and watch the running relative frequency wobble, then settle onto
// the dashed true-p line. The Law of Large Numbers as a toy.
export interface LongRunFrequencyConfig {
  p: number; // true probability as a decimal
  pLabel: string; // as displayed, e.g. "1/6"
  eventLabel: string; // e.g. "roll a 6"
  actionLabel?: string; // verb on the buttons, e.g. "roll" (default "run")
}

// A discrete random variable's distribution as bars on a number line (values
// may be negative — winnings work). Tap a bar for its x · P(x) contribution;
// the mean marker sits at the balance point; whiskers show mu ± sigma.
export interface DistributionBarsConfig {
  values: number[];
  probs: number[]; // decimals, summing to 1
  pLabels?: string[]; // displayed probabilities, e.g. ["1/4", ...]
  xLabel?: string;
  showMean?: boolean;
  showSd?: boolean;
}

// The binomial distribution workbench: steppers on n and p redraw the pmf
// bars live. Tap a bar for its C(n,k) p^k q^(n-k) reading; optional mu = np
// marker with sigma whiskers shows the mean-and-shape story.
export interface BinomialBarsConfig {
  n0?: number; // starting n (default 6)
  p0?: number; // starting p (default 0.5)
  nMax?: number; // stepper ceiling (default 14)
  showMuSigma?: boolean;
  highlightK?: number; // pre-highlighted bar
}

// A dot plot on a number line. meanMedian: steppers drag the largest value
// away and the mean chases it while the median stays put; deviations: sticks
// from the mean to each dot make the standard deviation visible.
export interface DotPlotConfig {
  mode: "meanMedian" | "deviations";
  data: number[];
  min: number;
  max: number;
  xLabel?: string;
}

// One dataset, several bin widths: chips regroup the same values into a new
// histogram, so shape emerges (or drowns) with the choice of bins.
export interface HistogramBinsConfig {
  data: number[];
  min: number;
  max: number;
  widths: number[]; // bin-width choices
  start?: number; // index into widths (default 0)
  xLabel?: string;
}

// A boxplot computed live from its data: five-number summary, IQR, and the
// 1.5 × IQR fences on toggle — points beyond the fences flagged as outliers.
export interface BoxPlotConfig {
  data: number[];
  xLabel?: string;
  showFences?: boolean; // fences drawn from the start
}

// The normal curve. empirical: tap 1σ / 2σ / 3σ to shade the 68–95–99.7
// bands with real axis values; zscore: a stepper walks x along the axis with
// the live z = (x − mu) / sigma reading — distance measured in sigmas.
export interface NormalCurveConfig {
  mode: "empirical" | "zscore";
  mu: number;
  sigma: number;
  x0?: number; // zscore: starting x
  step?: number; // zscore: stepper increment (default sigma / 2)
  xLabel?: string;
}

// The sampling-wobble machine: draw samples of size n from a population with
// true proportion p and stack each sample's p-hat as a dot. Bigger n, tighter
// pile — with the 1/sqrt(n) margin-of-error band on request.
export interface SamplingWobbleConfig {
  p: number; // true population proportion
  pLabel?: string; // as displayed
  statLabel?: string; // e.g. "sample % who say yes"
  nChoices?: number[]; // sample sizes (default [25, 100, 400])
  showMoe?: boolean; // shade p ± 1/sqrt(n)
}

// One worked example on a multi-example page (figure + reasoning steps).
export interface WorkedItem {
  prompt: string;
  figure?: FigureSpec;
  steps: string[];
  answer: string;
  check: string[];
}

// One try-it problem on a multi-problem page — the student ANSWERS (taps an
// option) and gets instant feedback, with a figure.
export interface TryItItem {
  prompt: string;
  figure?: FigureSpec;
  grid?: CoordinateGridConfig; // an interactive coordinate plane to reason with
  options: string[];
  correctIndex: number;
  explanation: string;
  check: string[];
}

export type InteractiveStep =
  | { kind: "concept"; eyebrow?: string; title: string; body: string }
  | { kind: "teach"; eyebrow?: string; title: string; body?: string; beats?: string[]; figure?: FigureSpec }
  | { kind: "notationToggle"; eyebrow?: string; title: string; teach: string; config: NotationToggleConfig }
  | { kind: "workedSet"; eyebrow?: string; title: string; intro?: string; examples: WorkedItem[] }
  | { kind: "tryItSet"; eyebrow?: string; title: string; intro?: string; grid?: CoordinateGridConfig; problems: TryItItem[] }
  | { kind: "scaler"; eyebrow?: string; title: string; teach: string; config: ScalerConfig }
  | { kind: "orderFlip"; eyebrow?: string; title: string; teach: string; config: OrderFlipConfig }
  | { kind: "compareToggle"; eyebrow?: string; title: string; teach: string; config: CompareToggleConfig }
  | { kind: "ratioTable"; eyebrow?: string; title: string; teach: string; config: RatioTableConfig }
  | { kind: "ratioCompare"; eyebrow?: string; title: string; teach: string; config: RatioCompareConfig }
  | { kind: "rateMeter"; eyebrow?: string; title: string; teach: string; config: RateMeterConfig }
  | { kind: "dealCompare"; eyebrow?: string; title: string; teach: string; config: DealCompareConfig }
  | { kind: "proportionBuilder"; eyebrow?: string; title: string; teach: string; config: ProportionBuilderConfig }
  | { kind: "fractionScaler"; eyebrow?: string; title: string; teach: string; config: FractionScalerConfig }
  | { kind: "fractionSimplify"; eyebrow?: string; title: string; teach: string; config: FractionSimplifyConfig }
  | { kind: "fractionCompare"; eyebrow?: string; title: string; teach: string; config: FractionCompareConfig }
  | { kind: "fractionCombine"; eyebrow?: string; title: string; teach: string; config: FractionCombineConfig }
  | { kind: "areaModel"; eyebrow?: string; title: string; teach: string; config: AreaModelConfig }
  | { kind: "fractionDivide"; eyebrow?: string; title: string; teach: string; config: FractionDivideConfig }
  | { kind: "decimalGrid"; eyebrow?: string; title: string; teach: string; config: DecimalGridConfig }
  | { kind: "decimalCompare"; eyebrow?: string; title: string; teach: string; config: DecimalCompareConfig }
  | { kind: "decimalRounder"; eyebrow?: string; title: string; teach: string; config: DecimalRounderConfig }
  | { kind: "decimalColumnSum"; eyebrow?: string; title: string; teach: string; config: DecimalColumnConfig }
  | { kind: "decimalArea"; eyebrow?: string; title: string; teach: string; config: DecimalAreaConfig }
  | { kind: "decimalShiftDivide"; eyebrow?: string; title: string; teach: string; config: DecimalDivideConfig }
  | { kind: "percentGrid"; eyebrow?: string; title: string; teach: string; config: PercentGridConfig }
  | { kind: "percentBar"; eyebrow?: string; title: string; teach: string; config: PercentBarConfig }
  | { kind: "percentChange"; eyebrow?: string; title: string; teach: string; config: PercentChangeConfig }
  | { kind: "percentChangeFinder"; eyebrow?: string; title: string; teach: string; config: PercentChangeFinderConfig }
  | { kind: "integerLine"; eyebrow?: string; title: string; teach: string; config: IntegerLineConfig }
  | { kind: "integerCompare"; eyebrow?: string; title: string; teach: string; config: IntegerCompareConfig }
  | { kind: "absoluteValue"; eyebrow?: string; title: string; teach: string; config: IntegerLineConfig }
  | { kind: "integerAdd"; eyebrow?: string; title: string; teach: string; config: IntegerAddConfig }
  | { kind: "integerSubtract"; eyebrow?: string; title: string; teach: string; config: IntegerAddConfig }
  | { kind: "integerSignRule"; eyebrow?: string; title: string; teach: string; config: IntegerSignRuleConfig }
  | { kind: "factorPairs"; eyebrow?: string; title: string; teach: string; config: FactorPairsConfig }
  | { kind: "factorFinder"; eyebrow?: string; title: string; teach: string; config: FactorFinderConfig }
  | { kind: "multiplesGrid"; eyebrow?: string; title: string; teach: string; config: MultiplesGridConfig }
  | { kind: "primeExplorer"; eyebrow?: string; title: string; teach: string; config: PrimeExplorerConfig }
  | { kind: "gcfFinder"; eyebrow?: string; title: string; teach: string; config: GcfFinderConfig }
  | { kind: "lcmFinder"; eyebrow?: string; title: string; teach: string; config: LcmFinderConfig }
  | { kind: "factorTree"; eyebrow?: string; title: string; teach: string; config: FactorTreeConfig }
  | { kind: "exponentBuilder"; eyebrow?: string; title: string; teach: string; config: ExponentBuilderConfig }
  | { kind: "orderOfOps"; eyebrow?: string; title: string; teach: string; config: OrderOfOpsConfig }
  | { kind: "algebraTiles"; eyebrow?: string; title: string; teach: string; config: AlgebraTilesConfig }
  | { kind: "evaluator"; eyebrow?: string; title: string; teach: string; config: EvaluatorConfig }
  | { kind: "balanceScale"; eyebrow?: string; title: string; teach: string; config: BalanceScaleConfig }
  | { kind: "coordinateGrid"; eyebrow?: string; title: string; teach: string; config: CoordinateGridConfig }
  | { kind: "geoCanvas"; eyebrow?: string; title: string; teach: string; config: GeoCanvasConfig }
  | { kind: "segmentRuler"; eyebrow?: string; title: string; teach: string; config: SegmentRulerConfig }
  | { kind: "protractor"; eyebrow?: string; title: string; teach: string; config: ProtractorConfig }
  | { kind: "anglePairs"; eyebrow?: string; title: string; teach: string; config: AnglePairFinderConfig }
  | { kind: "stepProof"; eyebrow?: string; title: string; teach?: string; config: StepProofConfig }
  | { kind: "patternGrow"; eyebrow?: string; title: string; teach: string; config: PatternGrowConfig }
  | { kind: "conjectureTest"; eyebrow?: string; title: string; teach: string; config: ConjectureTestConfig }
  | { kind: "conditionalFlip"; eyebrow?: string; title: string; teach: string; config: ConditionalFlipConfig }
  | { kind: "transversal"; eyebrow?: string; title: string; teach: string; config: TransversalConfig }
  | { kind: "triangleAngles"; eyebrow?: string; title: string; teach: string; config: TriangleAnglesConfig }
  | { kind: "triangleInequality"; eyebrow?: string; title: string; teach: string; config: TriangleInequalityConfig }
  | { kind: "congruentTriangles"; eyebrow?: string; title: string; teach: string; config: CongruentTrianglesConfig }
  | { kind: "triangleCenters"; eyebrow?: string; title: string; teach: string; config: TriangleCentersConfig }
  | { kind: "midsegment"; eyebrow?: string; title: string; teach: string; config: MidsegmentConfig }
  | { kind: "polygonAngles"; eyebrow?: string; title: string; teach: string; config: PolygonAnglesConfig }
  | { kind: "quadShape"; eyebrow?: string; title: string; teach: string; config: QuadShapeConfig }
  | { kind: "similarFigures"; eyebrow?: string; title: string; teach: string; config: SimilarFiguresConfig }
  | { kind: "sideSplitter"; eyebrow?: string; title: string; teach: string; config: SideSplitterConfig }
  | { kind: "dilation"; eyebrow?: string; title: string; teach: string; config: DilationConfig }
  | { kind: "pythagoreanSquares"; eyebrow?: string; title: string; teach: string; config: PythagoreanSquaresConfig }
  | { kind: "specialTriangle"; eyebrow?: string; title: string; teach: string; config: SpecialTriangleConfig }
  | { kind: "trigRatios"; eyebrow?: string; title: string; teach: string; config: TrigRatiosConfig }
  | { kind: "circleFigure"; eyebrow?: string; title: string; teach: string; config: CircleFigureConfig }
  | { kind: "circleAngle"; eyebrow?: string; title: string; teach: string; config: CircleAngleConfig }
  | { kind: "tangentCircle"; eyebrow?: string; title: string; teach: string; config: TangentCircleConfig }
  | { kind: "arcSector"; eyebrow?: string; title: string; teach: string; config: ArcSectorConfig }
  | { kind: "circleUnroll"; eyebrow?: string; title: string; teach: string; config: CircleUnrollConfig }
  | { kind: "systemGraph"; eyebrow?: string; title: string; teach: string; config: SystemGraphConfig }
  | { kind: "parabolaGraph"; eyebrow?: string; title: string; teach: string; config: ParabolaGraphConfig }
  | { kind: "expGraph"; eyebrow?: string; title: string; teach: string; config: ExpGraphConfig }
  | { kind: "polyGraph"; eyebrow?: string; title: string; teach: string; config: PolyGraphConfig }
  | { kind: "unitCircle"; eyebrow?: string; title: string; teach: string; config: UnitCircleConfig }
  | { kind: "argandPlot"; eyebrow?: string; title: string; teach: string; config: ArgandPlotConfig }
  | { kind: "limitGraph"; eyebrow?: string; title: string; teach: string; config: LimitGraphConfig }
  | { kind: "tangentGraph"; eyebrow?: string; title: string; teach: string; config: TangentGraphConfig }
  | { kind: "areaGraph"; eyebrow?: string; title: string; teach: string; config: AreaGraphConfig }
  | { kind: "vectorGraph"; eyebrow?: string; title: string; teach: string; config: VectorGraphConfig }
  | { kind: "conicGraph"; eyebrow?: string; title: string; teach: string; config: ConicGraphConfig }
  | { kind: "scatterPlot"; eyebrow?: string; title: string; teach: string; config: ScatterPlotConfig }
  | { kind: "treeDiagram"; eyebrow?: string; title: string; teach: string; config: TreeDiagramConfig }
  | { kind: "pascalTriangle"; eyebrow?: string; title: string; teach: string; config: PascalTriangleConfig }
  | { kind: "pathGrid"; eyebrow?: string; title: string; teach: string; config: PathGridConfig }
  | { kind: "vennCounts"; eyebrow?: string; title: string; teach: string; config: VennCountsConfig }
  | { kind: "longRunFrequency"; eyebrow?: string; title: string; teach: string; config: LongRunFrequencyConfig }
  | { kind: "distributionBars"; eyebrow?: string; title: string; teach: string; config: DistributionBarsConfig }
  | { kind: "binomialBars"; eyebrow?: string; title: string; teach: string; config: BinomialBarsConfig }
  | { kind: "dotPlot"; eyebrow?: string; title: string; teach: string; config: DotPlotConfig }
  | { kind: "histogramBins"; eyebrow?: string; title: string; teach: string; config: HistogramBinsConfig }
  | { kind: "boxPlot"; eyebrow?: string; title: string; teach: string; config: BoxPlotConfig }
  | { kind: "normalCurve"; eyebrow?: string; title: string; teach: string; config: NormalCurveConfig }
  | { kind: "samplingWobble"; eyebrow?: string; title: string; teach: string; config: SamplingWobbleConfig }
  | { kind: "areaShape"; eyebrow?: string; title: string; teach: string; config: AreaShapeConfig }
  | { kind: "apothemPolygon"; eyebrow?: string; title: string; teach: string; config: ApothemPolygonConfig }
  | { kind: "compositeArea"; eyebrow?: string; title: string; teach: string; config: CompositeAreaConfig }
  | { kind: "solid3d"; eyebrow?: string; title: string; teach: string; config: Solid3DConfig }
  | { kind: "solidNet"; eyebrow?: string; title: string; teach: string; config: SolidNetConfig }
  | { kind: "transformPlane"; eyebrow?: string; title: string; teach: string; config: TransformPlaneConfig }
  | { kind: "coordGeo"; eyebrow?: string; title: string; teach: string; config: CoordGeoConfig }
  | { kind: "worked"; eyebrow?: string; title: string; problemId: string }
  | { kind: "tryIt"; eyebrow?: string; title: string; problemId: string }
  | {
      kind: "tapQuestion";
      eyebrow?: string;
      title: string;
      prompt: string;
      grid?: CoordinateGridConfig; // an interactive coordinate plane to reason with
      figure?: FigureSpec; // a static diagram (e.g. mode "geo") the question reads from
      options: string[];
      correctIndex: number;
      explanation: string;
      check: string[]; // sympy assertions proving the correct option is right
    }
  | { kind: "funFact"; eyebrow?: string; title: string; body: string }
  | { kind: "tip"; eyebrow?: string; title: string; body: string }
  | { kind: "recap"; eyebrow?: string; title: string; points: string[] };

export interface InteractiveLesson {
  steps: InteractiveStep[];
}

// ---------------------------------------------------------------------------
// Pure interaction logic — unit-tested
// ---------------------------------------------------------------------------

export function gcd(a: number, b: number): number {
  a = Math.abs(a);
  b = Math.abs(b);
  while (b) {
    [a, b] = [b, a % b];
  }
  return a || 1;
}

// Simplest form of a ratio, e.g. simplifyRatio(2,6) -> [1,3].
export function simplifyRatio(a: number, b: number): [number, number] {
  const g = gcd(a, b);
  return [a / g, b / g];
}

// Scale a ratio by n batches, e.g. scaleRatio(2,6,3) -> [6,18].
export function scaleRatio(a: number, b: number, n: number): [number, number] {
  return [a * n, b * n];
}

// True when a:b and c:d are the same ratio (cross-multiply).
export function ratioEquivalent(a: number, b: number, c: number, d: number): boolean {
  return a * d === b * c;
}

// Format a ratio as "a:b".
export function formatRatio(a: number, b: number): string {
  return `${a}:${b}`;
}

// Part-to-whole pair for a compare toggle, e.g. partToWhole(3,5) -> [3,8].
export function partToWhole(part: number, other: number): [number, number] {
  return [part, part + other];
}

// Unit price of a deal (price per single unit).
export function unitPrice(price: number, qty: number): number {
  return price / qty;
}

// Index (0 = first, 1 = second) of the cheaper deal by unit price; -1 if equal.
export function cheaperDeal(
  a: { price: number; qty: number },
  b: { price: number; qty: number },
): number {
  const ua = a.price / a.qty;
  const ub = b.price / b.qty;
  if (ua < ub) return 0;
  if (ub < ua) return 1;
  return -1;
}

// A rate value, top per bottom (e.g. distance per time).
export function rateValue(top: number, bottom: number): number {
  return bottom === 0 ? 0 : top / bottom;
}

// Scale a:b so the known side equals knownValue; return the matching other side.
// e.g. proportionMissing(3,5,"b",15) -> 9  (red:blue 3:5, 15 blue -> 9 red)
export function proportionMissing(
  a: number,
  b: number,
  knownSide: "a" | "b",
  knownValue: number,
): number {
  return knownSide === "a" ? (b * knownValue) / a : (a * knownValue) / b;
}

// Decimal places in a number as written, e.g. decimalPlaces(0.25) -> 2.
export function decimalPlaces(x: number): number {
  const s = String(x);
  const i = s.indexOf(".");
  return i < 0 ? 0 : s.length - i - 1;
}

// The shift-to-whole-divisor chain for dividing decimals. Multiply both by
// 10^shifts so the divisor is whole; the quotient is computed via integers so
// it stays exact (4.8 / 0.6 -> 48 / 6 = 8, never 7.9999).
export function divideShift(
  dividend: number,
  divisor: number,
): { shifts: number; scaledDividend: number; scaledDivisor: number; quotient: number } {
  const shifts = decimalPlaces(divisor);
  const f = Math.pow(10, shifts);
  const scaledDividend = Math.round(dividend * f * 1e6) / 1e6;
  const scaledDivisor = Math.round(divisor * f);
  const p = Math.max(decimalPlaces(dividend), decimalPlaces(divisor));
  const s = Math.pow(10, p);
  const quotient = Math.round(dividend * s) / Math.round(divisor * s);
  return { shifts, scaledDividend, scaledDivisor, quotient };
}

// ---------------------------------------------------------------------------
// Helpers for the renderer
// ---------------------------------------------------------------------------

// Find a worked-example or try-it problem referenced by an interactive step.
export function getLessonProblem(lesson: GenMathLesson, id: string): LessonProblem | null {
  return (
    lesson.workedExamples.find((p) => p.id === id) ??
    lesson.tryIt.find((p) => p.id === id) ??
    null
  );
}

// ---------------------------------------------------------------------------
// Probability & statistics logic — unit-tested
// ---------------------------------------------------------------------------

export function factorialInt(n: number): number {
  let r = 1;
  for (let i = 2; i <= n; i++) r *= i;
  return r;
}

// C(n, k) via the Pascal recurrence product form — exact for the sizes we draw.
export function nCr(n: number, k: number): number {
  if (k < 0 || k > n) return 0;
  k = Math.min(k, n - k);
  let r = 1;
  for (let i = 1; i <= k; i++) r = (r * (n - k + i)) / i;
  return Math.round(r);
}

// Row n of Pascal's triangle: [C(n,0), ..., C(n,n)].
export function pascalRow(n: number): number[] {
  const row = [1];
  for (let k = 1; k <= n; k++) row.push((row[k - 1] * (n - k + 1)) / k);
  return row.map(Math.round);
}

// Lattice paths moving only right/down across an r-by-u block grid.
export function latticePaths(right: number, up: number): number {
  return nCr(right + up, right);
}

// Binomial pmf P(X = k) for X ~ B(n, p).
export function binomPmf(n: number, p: number, k: number): number {
  return nCr(n, k) * Math.pow(p, k) * Math.pow(1 - p, n - k);
}

export function binomMean(n: number, p: number): number {
  return n * p;
}

export function binomSd(n: number, p: number): number {
  return Math.sqrt(n * p * (1 - p));
}

// E[X] for a discrete random variable given as parallel value/probability lists.
export function expectedValue(values: number[], probs: number[]): number {
  return values.reduce((s, x, i) => s + x * (probs[i] ?? 0), 0);
}

// Var(X) = E[(X - mu)^2] for the same parallel lists.
export function rvVariance(values: number[], probs: number[]): number {
  const mu = expectedValue(values, probs);
  return values.reduce((s, x, i) => s + (x - mu) * (x - mu) * (probs[i] ?? 0), 0);
}

export function meanOf(xs: number[]): number {
  return xs.length === 0 ? 0 : xs.reduce((s, x) => s + x, 0) / xs.length;
}

export function medianOf(xs: number[]): number {
  const s = [...xs].sort((a, b) => a - b);
  const n = s.length;
  if (n === 0) return 0;
  return n % 2 === 1 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2;
}

// Quartiles by the median-of-halves convention the lessons teach: when n is
// odd the overall median is left OUT of both halves.
export function quartilesOf(xs: number[]): { q1: number; q2: number; q3: number } {
  const s = [...xs].sort((a, b) => a - b);
  const n = s.length;
  const half = Math.floor(n / 2);
  const lower = s.slice(0, half);
  const upper = s.slice(n % 2 === 1 ? half + 1 : half);
  return { q1: medianOf(lower), q2: medianOf(s), q3: medianOf(upper) };
}

export function iqrOf(xs: number[]): number {
  const { q1, q3 } = quartilesOf(xs);
  return q3 - q1;
}

// The 1.5 x IQR outlier fences.
export function fencesOf(xs: number[]): { lower: number; upper: number } {
  const { q1, q3 } = quartilesOf(xs);
  const iqr = q3 - q1;
  return { lower: q1 - 1.5 * iqr, upper: q3 + 1.5 * iqr };
}

export function outliersOf(xs: number[]): number[] {
  const { lower, upper } = fencesOf(xs);
  return xs.filter((x) => x < lower || x > upper);
}

// Population standard deviation (divide by n) — the lessons' convention.
export function stdevPop(xs: number[]): number {
  if (xs.length === 0) return 0;
  const mu = meanOf(xs);
  return Math.sqrt(xs.reduce((s, x) => s + (x - mu) * (x - mu), 0) / xs.length);
}

export function normalPdf(x: number, mu = 0, sigma = 1): number {
  const z = (x - mu) / sigma;
  return Math.exp(-0.5 * z * z) / (sigma * Math.sqrt(2 * Math.PI));
}

// Histogram counts for [min, min+w), [min+w, min+2w), ...; a value equal to
// the top edge lands in the last bin so nothing falls off the plot.
export function binCounts(data: number[], min: number, width: number, max: number): number[] {
  const bins = Math.max(1, Math.round((max - min) / width));
  const counts = new Array(bins).fill(0);
  for (const x of data) {
    if (x < min || x > max) continue;
    counts[Math.min(bins - 1, Math.floor((x - min) / width))]++;
  }
  return counts;
}
