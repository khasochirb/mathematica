// The score series behind the home page's two projection charts, and the
// geometry that turns it into SVG.
//
// Both charts previously carried hand-typed path data. That is how they
// came to disagree with themselves: the "Projected score · 8 weeks" chart
// drew its points as five <circle> elements at coordinates that did not
// sit on its own <path>, and neither chart's curve corresponded to the
// axis labels printed beside it. A reader who checked was misled; a
// reader who did not was shown a decorative squiggle sold as data.
//
// So the numbers live here once, and every mark — curve, confidence
// band, area fill, dots, endpoint — is computed from them against a
// single scale. The axis labels are checked against that same scale by
// scripts/verify-score-projection.test.ts, so a future edit that moves
// one without the other fails the gate instead of shipping.
//
// This is the same discipline the practice-test figures use
// (.claude/skills/practice-test-authoring §8): figure and statement
// interpolate the same variables, so they cannot desync.

/** Eight weekly projected scores, oldest first. The last is "now". */
export const PROJECTION: readonly number[] = [604, 621, 638, 659, 681, 702, 724, 742];

/** The model's stated confidence interval, in score points (± this). */
export const PROJECTION_ERR = 18;

/** The target line drawn across both charts. */
export const PROJECTION_TARGET = 780;

export interface Scale {
  /** Left and right edge of the plot area, in viewBox units. */
  x0: number;
  x1: number;
  /** Top and bottom edge of the plot area, in viewBox units. */
  yTop: number;
  yBot: number;
  /** The score at yTop and at yBot. */
  sTop: number;
  sBot: number;
}

export type Point = readonly [number, number];

/** Score -> y, in viewBox units. */
export function yFor(s: number, k: Scale): number {
  return k.yTop + ((k.yBot - k.yTop) * (k.sTop - s)) / (k.sTop - k.sBot);
}

/** Series index -> x, in viewBox units. */
export function xFor(i: number, k: Scale, n = PROJECTION.length): number {
  return n === 1 ? k.x0 : k.x0 + ((k.x1 - k.x0) * i) / (n - 1);
}

/** The plotted points for a series under a scale. */
export function pointsFor(scores: readonly number[], k: Scale): Point[] {
  return scores.map((s, i) => [xFor(i, k, scores.length), yFor(s, k)] as Point);
}

/**
 * A Catmull-Rom spline through every point, emitted as cubic Béziers.
 *
 * Catmull-Rom rather than a smoothing curve, because the curve must pass
 * exactly through each measured score — a spline that merely approaches
 * the points would put the drawn line somewhere the student never scored.
 */
export function smoothPath(pts: readonly Point[]): string {
  if (pts.length === 0) return "";
  const f = (n: number) => n.toFixed(1);
  if (pts.length < 3) {
    return pts.map((p, i) => `${i ? "L" : "M"}${f(p[0])},${f(p[1])}`).join(" ");
  }
  let d = `M${f(pts[0][0])},${f(pts[0][1])}`;
  for (let i = 0; i < pts.length - 1; i++) {
    const p0 = pts[Math.max(0, i - 1)];
    const p1 = pts[i];
    const p2 = pts[i + 1];
    const p3 = pts[Math.min(pts.length - 1, i + 2)];
    const c1x = p1[0] + (p2[0] - p0[0]) / 6;
    const c1y = p1[1] + (p2[1] - p0[1]) / 6;
    const c2x = p2[0] - (p3[0] - p1[0]) / 6;
    const c2y = p2[1] - (p3[1] - p1[1]) / 6;
    d += ` C${f(c1x)},${f(c1y)} ${f(c2x)},${f(c2y)} ${f(p2[0])},${f(p2[1])}`;
  }
  return d;
}

/** The curve closed down to `floor`, for the area fill under it. */
export function areaPath(pts: readonly Point[], floor: number): string {
  if (pts.length === 0) return "";
  const f = (n: number) => n.toFixed(1);
  const last = pts[pts.length - 1];
  return `${smoothPath(pts)} L${f(last[0])},${f(floor)} L${f(pts[0][0])},${f(floor)} Z`;
}

/**
 * The ±err ribbon: the upper edge smoothed forward, the lower edge
 * traced back, closed. Both edges come from the same series, so the
 * band can never drift away from the line it belongs to.
 */
export function bandPath(scores: readonly number[], k: Scale, err: number): string {
  if (scores.length === 0) return "";
  const f = (n: number) => n.toFixed(1);
  const hi = scores.map((s, i) => [xFor(i, k, scores.length), yFor(s + err, k)] as Point);
  const lo = scores
    .map((s, i) => [xFor(i, k, scores.length), yFor(s - err, k)] as Point)
    .reverse();
  return `${smoothPath(hi)} L${lo.map((p) => `${f(p[0])},${f(p[1])}`).join(" L")} Z`;
}
