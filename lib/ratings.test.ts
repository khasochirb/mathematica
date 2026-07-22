import { describe, it, expect } from "vitest";
import {
  ATTRIBUTES,
  RATING_CONSTANTS,
  allRatedUnits,
  band,
  computeRatings,
  eshSeverity,
  recommendedCourse,
  recommendedUnits,
  unitAttribute,
  type BankEvidence,
  type RatingAttempt,
  type RatingsProfile,
} from "./ratings";

const NOW = 1_750_000_000_000;
const DAY = 24 * 60 * 60 * 1000;
const FLOOR = RATING_CONSTANTS.RATING_FLOOR;

// Evidence generators — perfect (or fixed-accuracy) records for a unit.
function lessonAttempts(
  context: string,
  unit: string,
  n: number,
  opts: { correctEvery?: number; ageDays?: number } = {},
): RatingAttempt[] {
  const { correctEvery = 1, ageDays = 1 } = opts;
  return Array.from({ length: n }, (_, i) => ({
    context,
    topic: unit,
    subtopic: `lesson-${i}`,
    isCorrect: (i + 1) % correctEvery === 0,
    timestamp: NOW - ageDays * DAY,
    source: "lesson",
  }));
}

function testAttempts(
  context: string,
  unit: string,
  n: number,
  nCorrect: number,
  ageDays = 1,
): RatingAttempt[] {
  return Array.from({ length: n }, (_, i) => ({
    context,
    topic: unit,
    subtopic: "test",
    isCorrect: i < nCorrect,
    timestamp: NOW - ageDays * DAY,
    source: "test",
  }));
}

function eshAttempts(topic: string, n: number, nCorrect: number, ageDays = 1): RatingAttempt[] {
  return Array.from({ length: n }, (_, i) => ({
    topic,
    subtopic: "misc",
    isCorrect: i < nCorrect,
    timestamp: NOW - ageDays * DAY,
    source: "test",
  }));
}

// Full perfect evidence (lessons + tests + bank) for every unit of one
// attribute — the "did everything the courses offer" student.
function perfectAttributeEvidence(
  attrKey: string,
  ageDays = 1,
): { attempts: RatingAttempt[]; bank: BankEvidence } {
  const units = allRatedUnits().filter((u) => u.attribute === attrKey);
  const attempts: RatingAttempt[] = [];
  const bank: BankEvidence = {};
  // Slight headroom over the confidence targets: recency decay makes exactly-N
  // recent attempts count as fractionally under N.
  const nL = RATING_CONSTANTS.N_LESSON + 2;
  const nT = RATING_CONSTANTS.N_TEST + 1;
  for (const u of units) {
    attempts.push(...lessonAttempts(u.context, u.slug, nL, { ageDays }));
    attempts.push(...testAttempts(u.context, u.slug, nT, nT, ageDays));
    bank[`${u.context}/${u.slug}`] = { mastered: 6, attempted: 6 };
  }
  return { attempts, bank };
}

function unitScore(profile: RatingsProfile, context: string, slug: string): number {
  const u = profile.units.find((x) => x.context === context && x.slug === slug);
  expect(u, `${context}/${slug} in rated units`).toBeDefined();
  return u!.score;
}

function attr(profile: RatingsProfile, key: string) {
  return profile.attributes.find((a) => a.key === key)!;
}

describe("ratings map", () => {
  it("rates every live unit and maps each to an attribute", () => {
    const units = allRatedUnits();
    // 7 grades + 11 named courses; anything under 100 means a spine fell out
    // of the walker.
    expect(units.length).toBeGreaterThan(100);
    for (const u of units) {
      expect(unitAttribute(u.context, u.slug), `${u.context}/${u.slug}`).toBeTruthy();
      expect(u.index).toBeGreaterThan(0);
      expect(u.title.length).toBeGreaterThan(0);
    }
    // No duplicate units.
    const keys = units.map((u) => `${u.context}/${u.slug}`);
    expect(new Set(keys).size).toBe(keys.length);
    // Every attribute owns at least one live unit — an empty attribute would
    // make its score meaningless.
    for (const a of ATTRIBUTES) {
      expect(units.some((u) => u.attribute === a.key), a.key).toBe(true);
    }
  });
});

describe("computeRatings — the 40–100 scale", () => {
  it("empty profile: everything unrated at the floor, no recommendation", () => {
    const p = computeRatings({ attempts: [], now: NOW });
    expect(p.overall).toBe(FLOOR);
    expect(p.hasAnyEvidence).toBe(false);
    for (const a of p.attributes) {
      expect(a.rated).toBe(false);
      expect(a.score).toBe(FLOOR);
    }
    expect(recommendedCourse(p)).toBeNull();
  });

  it("lesson grinder: perfect lessons alone cap a unit at 61", () => {
    const p = computeRatings({
      attempts: lessonAttempts("course:geometry", "foundations", 50),
      now: NOW,
    });
    // W_LESSON = 0.35 of the 60-point range above the floor: 40 + 21 = 61.
    // Grinding lessons cannot make a unit look Strong.
    expect(unitScore(p, "course:geometry", "foundations")).toBe(61);
  });

  it("no unit test caps a unit at 69 even with lessons + full bank", () => {
    const p = computeRatings({
      attempts: lessonAttempts("course:geometry", "foundations", 50),
      bank: { "course:geometry/foundations": { mastered: 6, attempted: 6 } },
      now: NOW,
    });
    // raw 40 + 60·0.55 = 73 → capped at 69: without the unit test you top
    // out in Developing, never Strong.
    const s = unitScore(p, "course:geometry", "foundations");
    expect(s).toBe(RATING_CONSTANTS.CAP_NO_UNIT_TEST);
  });

  it("sub-elite test record caps a unit at 84; elite unlocks 100", () => {
    const base = {
      attempts: [
        ...lessonAttempts("course:geometry", "circles", 12),
        // 7/8 = 87.5% — below the 90% elite gate.
        ...testAttempts("course:geometry", "circles", 8, 7),
      ],
      bank: { "course:geometry/circles": { mastered: 6, attempted: 6 } },
      now: NOW,
    };
    const p = computeRatings(base);
    // raw ≈ 40 + 60·0.93 ≈ 96 → capped below the Near-mastery band.
    expect(unitScore(p, "course:geometry", "circles")).toBe(RATING_CONSTANTS.CAP_NOT_ELITE);

    const elite = computeRatings({
      ...base,
      attempts: [
        ...lessonAttempts("course:geometry", "circles", 12),
        ...testAttempts("course:geometry", "circles", 9, 9),
      ],
    });
    expect(unitScore(elite, "course:geometry", "circles")).toBe(100);
  });

  it("diligent-no-exam: perfect across every unit still caps the attribute at 84", () => {
    const { attempts, bank } = perfectAttributeEvidence("linear");
    const p = computeRatings({ attempts, bank, now: NOW });
    const a = attr(p, "linear");
    expect(a.rated).toBe(true);
    expect(a.coverage).toBeCloseTo(1, 5);
    expect(a.score).toBe(RATING_CONSTANTS.CAP_NO_EXAM);
    expect(a.band).toBe("strong");
  });

  it("master: full coverage + sustained exam evidence earns 100", () => {
    const { attempts, bank } = perfectAttributeEvidence("linear");
    attempts.push(...eshAttempts("linear_algebra", 30, 30));
    const p = computeRatings({ attempts, bank, now: NOW });
    const a = attr(p, "linear");
    expect(a.score).toBe(100);
    expect(a.band).toBe("mastery");
    // Breadth-weighting with unrated at the floor: one mastered attribute
    // lifts the overall a little above 40, never into fake territory.
    expect(p.overall).toBeGreaterThan(FLOOR);
    expect(p.overall).toBeLessThan(55);
  });

  it("decay: the same mastery evidence a year old collapses toward the floor", () => {
    const { attempts } = perfectAttributeEvidence("linear", 365);
    attempts.push(...eshAttempts("linear_algebra", 30, 30, 365));
    const p = computeRatings({ attempts, now: NOW });
    const a = attr(p, "linear");
    expect(a.rated).toBe(true);
    expect(a.score).toBeLessThan(55);
    expect(a.band).toBe("beginner");
  });

  it("exam-only evidence rates an attribute, capped at 69 until units are proven", () => {
    const p = computeRatings({
      attempts: eshAttempts("trigonometry", 40, 40),
      now: NOW,
    });
    const a = attr(p, "trigonometry");
    expect(a.rated).toBe(true);
    // Perfect sustained exam record with zero unit tests: exactly the cap —
    // the exams carry you to the top of Developing, courses unlock Strong.
    expect(a.score).toBe(RATING_CONSTANTS.CAP_NO_TEST_ATTR);
    expect(a.hasUnitTest).toBe(false);
  });

  it("a handful of exam questions is NOT enough to rate an attribute", () => {
    const p = computeRatings({
      attempts: eshAttempts("set_theory", 3, 0),
      now: NOW,
    });
    // 0/3 on a rarely-tested topic: below MIN_EXAM_RATE_N → unrated, not 40.
    expect(attr(p, "numbers").rated).toBe(false);
    expect(attr(p, "numbers").score).toBe(FLOOR);
  });

  it("the owner's scenario: two ЭЕШ tests (94% and 16%) — no Grade-6 insult", () => {
    // Roughly two 36-question mocks spread over the common topics: one aced,
    // one bombed. Arithmetic/set-theory barely appear (like real papers).
    const seed = (accHigh: number, accLow: number, perTopic: Record<string, number>) => {
      const rows: RatingAttempt[] = [];
      for (const [topic, n] of Object.entries(perTopic)) {
        rows.push(...eshAttempts(topic, n, Math.round(n * accHigh), 1));
        rows.push(...eshAttempts(topic, n, Math.round(n * accLow), 2));
      }
      return rows;
    };
    const p = computeRatings({
      attempts: seed(0.94, 0.16, {
        algebra: 8,
        geometry: 6,
        trigonometry: 5,
        functions: 5,
        probability: 4,
        calculus: 4,
        sequences: 3,
      }),
      now: NOW,
    });

    // Attributes with real exam volume are rated in the Developing range.
    for (const key of ["algebra", "geometry", "trigonometry", "probstats", "calculus"]) {
      const a = attr(p, key);
      expect(a.rated, key).toBe(true);
      expect(a.score, key).toBeGreaterThanOrEqual(FLOOR);
      expect(a.score, key).toBeLessThanOrEqual(RATING_CONSTANTS.CAP_NO_TEST_ATTR);
    }
    // Numbers & linear algebra never appeared → UNRATED, not 0.
    expect(attr(p, "numbers").rated).toBe(false);
    expect(attr(p, "linear").rated).toBe(false);

    // Overall looks like a real rookie rating, not a 5.
    expect(p.overall).toBeGreaterThanOrEqual(42);
    expect(p.overall).toBeLessThan(70);

    // The recommendation targets a RATED weakness — never Grade 6 off a blank.
    const rec = recommendedCourse(p);
    expect(rec).not.toBeNull();
    expect(rec!.attribute).not.toBe("numbers");
    expect(rec!.courseContext).not.toBe("course:grade-6");
    expect(rec!.explanationEn).toContain("lowest rated");
  });

  it("placement alone seeds a provisional rating between 40 and 60", () => {
    const p = computeRatings({
      attempts: [],
      placements: [
        {
          namespace: "geometry",
          takenAt: NOW - DAY,
          topicScores: [
            { slug: "foundations", seen: 4, correct: 3 },
            { slug: "circles", seen: 4, correct: 4 },
          ],
        },
      ],
      now: NOW,
    });
    const a = attr(p, "geometry");
    expect(a.rated).toBe(true);
    expect(a.provisional).toBe(true);
    // 7/8 accuracy → 40 + 20·0.875 ≈ 58.
    expect(a.score).toBe(58);
    expect(a.score).toBeLessThanOrEqual(RATING_CONSTANTS.PLACEMENT_SEED_MAX);
    expect(p.hasAnyEvidence).toBe(true);
    // Real evidence replaces the seed: one wrong lesson answer in a geometry
    // unit and the attribute is earned (at the floor), not seeded.
    const p2 = computeRatings({
      attempts: [
        { context: "course:geometry", topic: "foundations", isCorrect: false, timestamp: NOW - DAY, source: "lesson" },
      ],
      placements: [
        { namespace: "geometry", takenAt: NOW - DAY, topicScores: [{ slug: "foundations", seen: 4, correct: 4 }] },
      ],
      now: NOW,
    });
    expect(attr(p2, "geometry").provisional).toBe(false);
    expect(attr(p2, "geometry").score).toBe(FLOOR);
  });
});

describe("recommendations", () => {
  it("recommends the lowest RATED attribute with an owner's-voice explanation", () => {
    const placements = [
      {
        namespace: "grade12",
        takenAt: NOW - DAY,
        topicScores: [
          { slug: "derivatives", seen: 4, correct: 4 },
          { slug: "vectors", seen: 4, correct: 4 },
          { slug: "trigonometric-identities", seen: 4, correct: 4 },
          { slug: "conic-sections", seen: 4, correct: 4 },
        ],
      },
    ];
    const p = computeRatings({
      attempts: [
        ...lessonAttempts("course:geometry", "foundations", 10, { correctEvery: 2 }),
        ...eshAttempts("geometry", 10, 3),
      ],
      placements,
      now: NOW,
    });
    const rec = recommendedCourse(p);
    expect(rec).not.toBeNull();
    // Only rated attributes may be recommended.
    expect(attr(p, rec!.attribute).rated).toBe(true);
    expect(rec!.courseHref.startsWith("/math")).toBe(true);
    expect(rec!.explanationEn).toContain(`is ${rec!.score}`);
    expect(rec!.explanationMn).toContain("үнэлгээ");
    expect(rec!.explanationMn).toContain("зөвлөж байна");
  });

  it("strong band climbs the ladder to the second course", () => {
    const { attempts, bank } = perfectAttributeEvidence("geometry");
    const p = computeRatings({ attempts, bank, now: NOW });
    const geo = attr(p, "geometry");
    expect(geo.band).toBe("strong");
    const synthetic: RatingsProfile = {
      ...p,
      attributes: p.attributes.map((a) =>
        a.key === "geometry" ? a : { ...a, rated: true, score: 90, band: band(90) },
      ),
    };
    const rec = recommendedCourse(synthetic);
    expect(rec!.attribute).toBe("geometry");
    expect(rec!.courseContext).toBe("course:solid-geometry");
  });

  it("recommendedUnits pins weak units and finds the start point", () => {
    const attempts = [
      // Unit 1 (foundations): elite — solid.
      ...lessonAttempts("course:geometry", "foundations", 12),
      ...testAttempts("course:geometry", "foundations", 9, 9),
      // Unit 2 (reasoning-and-proof): good lessons + bank, but no unit test.
      ...lessonAttempts("course:geometry", "reasoning-and-proof", 12),
      // Unit 4 (triangles-and-congruence): struggling.
      ...lessonAttempts("course:geometry", "triangles-and-congruence", 10, { correctEvery: 2 }),
    ];
    const bank: BankEvidence = {
      "course:geometry/foundations": { mastered: 6, attempted: 6 },
      "course:geometry/reasoning-and-proof": { mastered: 6, attempted: 6 },
    };
    const p = computeRatings({ attempts, bank, now: NOW });
    const rec = recommendedUnits(p, "course:geometry");
    // Unit 1 proven → the course starts at unit 2 for this student.
    expect(rec.canStartAtUnit).toBe(2);
    // Unit 2 sits at 69 (capped by no-test) — the first not-yet-solid unit.
    expect(rec.startHere?.slug).toBe("reasoning-and-proof");
    expect(rec.pinned.map((u) => u.slug)).toContain("triangles-and-congruence");
    expect(rec.solid.map((u) => u.slug)).toContain("foundations");
    // Good-looking but unproven → prompted to take the unit test; the truly
    // weak unit (Beginner) is NOT — it needs lessons first.
    expect(rec.needsUnitTest.map((u) => u.slug)).toContain("reasoning-and-proof");
    expect(rec.needsUnitTest.map((u) => u.slug)).not.toContain("foundations");
    expect(rec.needsUnitTest.map((u) => u.slug)).not.toContain("triangles-and-congruence");
  });
});

describe("eshSeverity", () => {
  it("needs a minimum sample and then bands on raw accuracy", () => {
    expect(eshSeverity(20, 2)).toBeNull();
    expect(eshSeverity(20, 5)).toBe("beginner");
    expect(eshSeverity(55, 5)).toBe("developing");
    expect(eshSeverity(75, 5)).toBe("strong");
    expect(eshSeverity(90, 5)).toBe("mastery");
  });
});
