// The home page's two score charts must agree with their own axes.
//
// Before this, both were hand-typed SVG path data. The "Projected score ·
// 8 weeks" chart drew a curve with one `d` string, a confidence band with
// a second, and five dots as five <circle> elements — and the dots did not
// sit on the curve. Neither corresponded to the 800/720/640/560 gridline
// labels printed beside them, and the week labels (W1, W3, W5, W7, NOW,
// EXAM) were spaced 100px apart under a curve whose points were not.
//
// Nothing surfaced it: an SVG path is valid whatever it draws, and a chart
// that is merely decorative still renders. It shipped on the front page of
// a site that sells score prediction.
//
// So the marks are computed from one series (lib/score-projection.ts) and
// this holds the properties that make the drawing honest.
import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";
import {
  PROJECTION,
  PROJECTION_ERR,
  PROJECTION_TARGET,
  pointsFor,
  smoothPath,
  bandPath,
  areaPath,
  xFor,
  yFor,
  type Scale,
} from "../lib/score-projection";

// Must mirror app/page.tsx. Duplicated deliberately: if someone edits the
// scale there without editing it here, these tests fail — which is the
// point. A shared import would make the two agree vacuously.
const SPARK: Scale = { x0: 6, x1: 150, yTop: 4, yBot: 56, sTop: 800, sBot: 580 };
const PROJ: Scale = { x0: 60, x1: 528, yTop: 40, yBot: 236, sTop: 800, sBot: 800 - 196 / 0.75 };

const SRC = fs.readFileSync(path.join(process.cwd(), "app", "page.tsx"), "utf-8");

describe("the score series", () => {
  it("is monotonically improving and inside the ЭШ 0–800 band", () => {
    // A projection that dips would be fine data, but the copy beside it
    // says "watch yourself improve" — the sample must show that.
    for (const s of PROJECTION) {
      expect(s).toBeGreaterThanOrEqual(0);
      expect(s).toBeLessThanOrEqual(800);
    }
    for (let i = 1; i < PROJECTION.length; i++) {
      expect(PROJECTION[i]).toBeGreaterThan(PROJECTION[i - 1]);
    }
  });

  it("ends below the target, so the target line is still ahead of the student", () => {
    expect(PROJECTION[PROJECTION.length - 1]).toBeLessThan(PROJECTION_TARGET);
  });

  it("the card's headline number is the series' last value", () => {
    // The card prints 742 in the serif. If the series moves and the
    // literal does not, the number and the chart tell different stories.
    const last = PROJECTION[PROJECTION.length - 1];
    expect(SRC).toContain(`${last}`);
    expect(last).toBe(742);
  });
});

describe("PROJ: the plotted curve agrees with the printed axis", () => {
  // The gridlines are drawn by mapping these scores through yFor, and the
  // labels are the same array — so the only way they can disagree is if
  // the scale itself stops being linear in the way the labels assume.
  const LABELS = [800, 720, 640, 560];

  it("an 80-point step is exactly 60px, matching the gridline spacing", () => {
    for (let i = 1; i < LABELS.length; i++) {
      const gap = yFor(LABELS[i], PROJ) - yFor(LABELS[i - 1], PROJ);
      expect(gap).toBeCloseTo(60, 6);
    }
  });

  it("800 sits on the top gridline and the axis is right-way-up", () => {
    expect(yFor(800, PROJ)).toBeCloseTo(PROJ.yTop, 6);
    expect(yFor(560, PROJ)).toBeGreaterThan(yFor(800, PROJ));
  });

  it("every plotted point is inside the 560x280 viewBox", () => {
    for (const [x, y] of pointsFor(PROJECTION, PROJ)) {
      expect(x).toBeGreaterThanOrEqual(0);
      expect(x).toBeLessThanOrEqual(560);
      expect(y).toBeGreaterThanOrEqual(0);
      expect(y).toBeLessThanOrEqual(280);
    }
  });

  it("the confidence band stays inside the viewBox at both edges", () => {
    // ±18 on the last point is the closest the band comes to the top.
    const hi = yFor(PROJECTION[PROJECTION.length - 1] + PROJECTION_ERR, PROJ);
    const lo = yFor(PROJECTION[0] - PROJECTION_ERR, PROJ);
    expect(hi).toBeGreaterThanOrEqual(0);
    expect(lo).toBeLessThanOrEqual(280);
  });

  it("the target rule sits above the newest point — it has not been passed", () => {
    expect(yFor(PROJECTION_TARGET, PROJ)).toBeLessThan(
      yFor(PROJECTION[PROJECTION.length - 1], PROJ),
    );
  });

  it("there is one week label per point, and the last is the newest", () => {
    // [\s\S] rather than the /s flag: this repo's tsconfig targets below
    // es2018, where dotAll is not available.
    const labels = SRC.match(/PROJ_WEEK_LABELS = \[([\s\S]*?)\]/);
    expect(labels, "PROJ_WEEK_LABELS not found in app/page.tsx").not.toBeNull();
    const n = labels![1].split(",").filter((s) => s.trim()).length;
    expect(n, "one label per plotted week").toBe(PROJECTION.length);
    // The old chart labelled a sixth column "EXAM" that no point stood
    // under — a category on the axis with no datum behind it.
    expect(labels![1]).not.toContain("EXAM");
  });

  it("week labels are evenly spaced across the same x-scale as the points", () => {
    const pts = pointsFor(PROJECTION, PROJ);
    for (let i = 0; i < PROJECTION.length; i++) {
      expect(xFor(i, PROJ)).toBeCloseTo(pts[i][0], 6);
    }
  });
});

describe("SPARK: the report card's inline trend", () => {
  it("the target rule and its label share one y", () => {
    // Both are emitted from yFor(PROJECTION_TARGET, SPARK) in page.tsx.
    expect(yFor(PROJECTION_TARGET, SPARK)).toBeGreaterThan(0);
    expect(yFor(PROJECTION_TARGET, SPARK)).toBeLessThan(SPARK.yBot);
  });

  it("every point is inside the 160x64 viewBox", () => {
    for (const [x, y] of pointsFor(PROJECTION, SPARK)) {
      expect(x).toBeGreaterThanOrEqual(0);
      expect(x).toBeLessThanOrEqual(160);
      expect(y).toBeGreaterThanOrEqual(0);
      expect(y).toBeLessThanOrEqual(64);
    }
  });

  it('does not stretch its geometry with preserveAspectRatio="none"', () => {
    // The old sparkline did, which sheared the curve away from any real
    // slope whenever the card resized.
    const spark = SRC.slice(SRC.indexOf('viewBox="0 0 160 64"'));
    expect(spark.slice(0, 400)).not.toContain('preserveAspectRatio="none"');
  });
});

describe("path generation", () => {
  it("the curve passes exactly through every measured point", () => {
    // Catmull-Rom interpolates; a smoothing spline would not, and the line
    // would then sit somewhere the student never scored.
    const pts = pointsFor(PROJECTION, PROJ);
    const d = smoothPath(pts);
    for (const [x, y] of pts) {
      expect(d, `curve must touch ${x.toFixed(1)},${y.toFixed(1)}`).toContain(
        `${x.toFixed(1)},${y.toFixed(1)}`,
      );
    }
  });

  it("emits no NaN or Infinity into any path", () => {
    const paths = [
      smoothPath(pointsFor(PROJECTION, PROJ)),
      smoothPath(pointsFor(PROJECTION, SPARK)),
      bandPath(PROJECTION, PROJ, PROJECTION_ERR),
      areaPath(pointsFor(PROJECTION, PROJ), PROJ.yBot),
      areaPath(pointsFor(PROJECTION, SPARK), 62),
    ];
    for (const d of paths) {
      expect(d).not.toMatch(/NaN|Infinity|undefined/);
      expect(d.length).toBeGreaterThan(0);
    }
  });

  it("the area and band close back to their start", () => {
    expect(areaPath(pointsFor(PROJECTION, PROJ), PROJ.yBot).endsWith("Z")).toBe(true);
    expect(bandPath(PROJECTION, PROJ, PROJECTION_ERR).endsWith("Z")).toBe(true);
  });

  it("degenerate inputs do not throw", () => {
    expect(smoothPath([])).toBe("");
    expect(areaPath([], 0)).toBe("");
    expect(bandPath([], PROJ, 18)).toBe("");
    expect(smoothPath([[0, 0]])).toBe("M0.0,0.0");
    expect(xFor(0, PROJ, 1)).toBe(PROJ.x0);
  });
});

describe("no hand-typed chart geometry survives on the home page", () => {
  it("the old dot coordinates are gone", () => {
    // These five circles were the visible symptom: they sat off the line.
    for (const dot of ['cy="222"', 'cy="200"', 'cy="168"', 'cy="132"', 'cy="96"']) {
      expect(SRC, `stale hand-placed dot ${dot}`).not.toContain(dot);
    }
  });

  it("the old literal path strings are gone", () => {
    expect(SRC).not.toContain("M40,220 C120,200");
    expect(SRC).not.toContain("M0,50 L20,44");
  });

  it("the hero headline highlights with colour only, not colour plus italic", () => {
    const hero = SRC.slice(SRC.indexOf("const heroHeadline"), SRC.indexOf("return ("));
    expect(hero).not.toContain("serif-italic");
    expect(hero).toContain("var(--accent)");
  });
});
