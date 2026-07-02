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
  | { kind: "segment" | "ray" | "line"; from: string; to: string; color?: string; ticks?: number; dashed?: boolean }
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
  | { kind: "tryItSet"; eyebrow?: string; title: string; intro?: string; problems: TryItItem[] }
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
  | { kind: "worked"; eyebrow?: string; title: string; problemId: string }
  | { kind: "tryIt"; eyebrow?: string; title: string; problemId: string }
  | {
      kind: "tapQuestion";
      eyebrow?: string;
      title: string;
      prompt: string;
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
