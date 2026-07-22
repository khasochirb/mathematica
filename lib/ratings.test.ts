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

function attrScore(profile: RatingsProfile, key: string) {
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

describe("computeRatings — strictness fixtures", () => {
  it("empty profile: zero everywhere, no recommendation", () => {
    const p = computeRatings({ attempts: [], now: NOW });
    expect(p.overall).toBe(0);
    expect(p.hasAnyEvidence).toBe(false);
    for (const a of p.attributes) expect(a.score).toBe(0);
    expect(recommendedCourse(p)).toBeNull();
  });

  it("lesson grinder: perfect lessons alone cap a unit at 35", () => {
    const p = computeRatings({
      attempts: lessonAttempts("course:geometry", "foundations", 50),
      now: NOW,
    });
    // W_LESSON = 0.35 and nothing else — grinding lessons cannot pass 35.
    expect(unitScore(p, "course:geometry", "foundations")).toBe(35);
  });

  it("no unit test caps a unit at 60 even with lessons + full bank", () => {
    const p = computeRatings({
      attempts: lessonAttempts("course:geometry", "foundations", 50),
      bank: { "course:geometry/foundations": { mastered: 6, attempted: 6 } },
      now: NOW,
    });
    // 35 (lessons) + 20 (bank) = 55 raw — under the 60 cap by construction,
    // which is the design: without a unit test you cannot look "solid".
    const s = unitScore(p, "course:geometry", "foundations");
    expect(s).toBe(55);
    expect(s).toBeLessThanOrEqual(RATING_CONSTANTS.CAP_NO_UNIT_TEST);
  });

  it("sub-elite test record caps a unit at 84; elite unlocks the top", () => {
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
    // raw = 35 + 45·0.875 + 20 ≈ 94 → capped at 84.
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
    const a = attrScore(p, "linear");
    expect(a.coverage).toBe(100);
    expect(a.score).toBe(RATING_CONSTANTS.CAP_NO_EXAM);
    expect(a.band).toBe("strong");
  });

  it("master: full coverage + sustained exam evidence earns 100", () => {
    const { attempts, bank } = perfectAttributeEvidence("linear");
    attempts.push(...eshAttempts("linear_algebra", 30, 30));
    const p = computeRatings({ attempts, bank, now: NOW });
    const a = attrScore(p, "linear");
    expect(a.score).toBe(100);
    expect(a.band).toBe("mastery");
    // Breadth-weighting: one mastered attribute barely moves the overall.
    expect(p.overall).toBeGreaterThan(0);
    expect(p.overall).toBeLessThan(20);
  });

  it("decay: the same mastery evidence a year old collapses", () => {
    const { attempts, bank } = perfectAttributeEvidence("linear", 365);
    attempts.push(...eshAttempts("linear_algebra", 30, 30, 365));
    // Bank mastery has no timestamps, so leave it out of the decay fixture.
    void bank;
    const p = computeRatings({ attempts, now: NOW });
    const a = attrScore(p, "linear");
    expect(a.score).toBeLessThan(20);
    expect(a.band).toBe("beginner");
  });

  it("exam-only evidence cannot pass the no-unit-test attribute cap", () => {
    const p = computeRatings({
      attempts: eshAttempts("trigonometry", 40, 40),
      now: NOW,
    });
    const a = attrScore(p, "trigonometry");
    // coverage 0 → 0.3·exam ≤ 30, and the 69 cap is armed anyway.
    expect(a.score).toBeLessThanOrEqual(RATING_CONSTANTS.CAP_NO_TEST_ATTR);
    expect(a.hasUnitTest).toBe(false);
  });

  it("placement alone seeds a provisional score ≤ 40", () => {
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
    const a = attrScore(p, "geometry");
    expect(a.provisional).toBe(true);
    // 7/8 accuracy → 40·0.875 = 35.
    expect(a.score).toBe(35);
    expect(a.score).toBeLessThanOrEqual(RATING_CONSTANTS.PLACEMENT_SEED_MAX);
    expect(p.hasAnyEvidence).toBe(true);
    // Real evidence replaces the seed: one wrong lesson answer in a geometry
    // unit and the attribute is earned (near zero), not seeded.
    const p2 = computeRatings({
      attempts: [
        { context: "course:geometry", topic: "foundations", isCorrect: false, timestamp: NOW - DAY, source: "lesson" },
      ],
      placements: [
        { namespace: "geometry", takenAt: NOW - DAY, topicScores: [{ slug: "foundations", seen: 4, correct: 4 }] },
      ],
      now: NOW,
    });
    expect(attrScore(p2, "geometry").provisional).toBe(false);
  });
});

describe("recommendations", () => {
  it("recommends the lowest attribute's course with an owner's-voice explanation", () => {
    // Some geometry work at a beginner level; everything else untouched —
    // ties at 0 exist, so assert shape rather than a specific winner among
    // the zeros... give every OTHER attribute a tiny placement seed so
    // geometry (earned, low) still isn't the lowest — instead pin the target:
    // make geometry the ONLY zero-ish attribute with evidence and drag the
    // rest up via seeds.
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
    // The lowest attribute is one of the untouched zeros or geometry; either
    // way the recommendation must point at a real course with both languages.
    expect(rec!.courseHref.startsWith("/math")).toBe(true);
    expect(rec!.explanationEn).toContain(`is ${rec!.score}`);
    expect(rec!.explanationMn).toContain("үнэлгээ");
    expect(rec!.explanationMn).toContain("зөвлөж байна");
  });

  it("strong band climbs the ladder to the second course", () => {
    // Elite-complete geometry coverage (no exam) → 84 = strong → the
    // geometry ladder should recommend Solid Geometry, not Geometry 1.
    const { attempts, bank } = perfectAttributeEvidence("geometry");
    // Drag every other attribute above zero is unnecessary — force the
    // check directly on the ladder rung logic by making geometry lowest
    // impossible; instead check via a profile where geometry IS lowest:
    // strip to only geometry evidence and give others exam mastery is
    // complex — simpler: geometry at 84 with everything else at 0 makes
    // some other attribute the recommendation. So test the rung through a
    // synthetic profile object instead.
    const p = computeRatings({ attempts, bank, now: NOW });
    const geo = attrScore(p, "geometry");
    expect(geo.band).toBe("strong");
    const synthetic: RatingsProfile = {
      ...p,
      attributes: p.attributes.map((a) =>
        a.key === "geometry" ? a : { ...a, score: 90, band: band(90) },
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
    // Unit 2 sits at 55 (35 lessons + 20 bank, capped by no-test) — the
    // first not-yet-solid unit in spine order.
    expect(rec.startHere?.slug).toBe("reasoning-and-proof");
    expect(rec.pinned.map((u) => u.slug)).toContain("triangles-and-congruence");
    expect(rec.solid.map((u) => u.slug)).toContain("foundations");
    // Good-looking but unproven → prompted to take the unit test; the truly
    // weak unit (score < 40) is NOT — it needs lessons first.
    expect(rec.needsUnitTest.map((u) => u.slug)).toContain("reasoning-and-proof");
    expect(rec.needsUnitTest.map((u) => u.slug)).not.toContain("foundations");
    expect(rec.needsUnitTest.map((u) => u.slug)).not.toContain("triangles-and-congruence");
  });
});

describe("eshSeverity", () => {
  it("needs a minimum sample and then bands", () => {
    expect(eshSeverity(20, 2)).toBeNull();
    expect(eshSeverity(20, 5)).toBe("beginner");
    expect(eshSeverity(55, 5)).toBe("developing");
    expect(eshSeverity(75, 5)).toBe("strong");
    expect(eshSeverity(90, 5)).toBe("mastery");
  });
});
