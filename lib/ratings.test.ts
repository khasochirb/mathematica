import { describe, it, expect } from "vitest";
import { getSatBankTopic } from "./bank-data";
import {
  ATTRIBUTES,
  RATING_CONSTANTS,
  SAT_BANK_ATTRIBUTE,
  SAT_DOMAIN_ATTRIBUTE,
  practiceCredit,
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

// A unit's bank worked to the point of full credit: both the breadth and
// the volume targets met. Anything less earns proportionally less.
const FULL_BANK = {
  solvedForms: RATING_CONSTANTS.N_BANK_FORMS,
  solvedProblems: RATING_CONSTANTS.N_BANK_PROBLEMS,
};

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
    bank[`${u.context}/${u.slug}`] = FULL_BANK;
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
      bank: { "course:geometry/foundations": FULL_BANK },
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
      bank: { "course:geometry/circles": FULL_BANK },
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

  it("exam performance drives the rating: a strong ЭШ record earns a high number", () => {
    // Perfect, well-sampled ЭШ record on one attribute — the placement is in.
    const p = computeRatings({
      attempts: eshAttempts("trigonometry", 40, 40),
      now: NOW,
    });
    const a = attr(p, "trigonometry");
    expect(a.rated).toBe(true);
    expect(a.hasUnitTest).toBe(false);
    // ЭШ difficulty 1.0, full confidence → rating ≈ the score itself (100),
    // NOT stuck at a Developing cap. This is the whole point of the change.
    expect(a.score).toBe(100);
    expect(a.band).toBe("mastery");
  });

  it("exam difficulty: 100% SAT tops out at 80; ЭШ and IB reach 100 and match", () => {
    // Compare the SAME attribute (algebra) across the three hubs, since every
    // hub tags algebra the same (SAT 'algebra', ЭШ 'algebra', IB
    // 'number_algebra' → algebra).
    const sat = computeRatings({
      attempts: Array.from({ length: 40 }, () => ({
        topic: "algebra", subtopic: "misc", isCorrect: true,
        timestamp: NOW - DAY, source: "test", context: "sat",
      })),
      now: NOW,
    });
    expect(attr(sat, "algebra").score).toBe(80); // 100% · 0.8 difficulty

    const esh = computeRatings({ attempts: eshAttempts("algebra", 40, 40), now: NOW });
    const ib = computeRatings({
      attempts: Array.from({ length: 40 }, () => ({
        topic: "aa-paper-1", subtopic: "number_algebra", isCorrect: true,
        timestamp: NOW - DAY, source: "test", context: "ib",
      })),
      now: NOW,
    });
    // ЭШ and IB are the hard pair — same difficulty, same rating.
    expect(attr(esh, "algebra").score).toBe(100);
    expect(attr(ib, "algebra").score).toBe(100);
    // And a 100% SAT rates strictly below a 100% ЭШ.
    expect(attr(sat, "algebra").score).toBeLessThan(attr(esh, "algebra").score);
  });

  it("a handful of exam questions is NOT enough to rate an attribute", () => {
    const p = computeRatings({
      attempts: eshAttempts("set_theory", 3, 0),
      now: NOW,
    });
    // 3 questions is far below the accuracy bar → unrated ("—"), not 40.
    expect(attr(p, "numbers").rated).toBe(false);
    expect(attr(p, "numbers").score).toBe(FLOOR);
  });

  it("attributes need ~five full tests before they're rated", () => {
    // ~2 tests' worth on a topic (12 questions) — not enough to grade.
    const two = computeRatings({ attempts: eshAttempts("algebra", 12, 9), now: NOW });
    expect(attr(two, "algebra").rated).toBe(false);
    // ~5 tests' worth (30 questions) — now it's rated.
    const five = computeRatings({ attempts: eshAttempts("algebra", 30, 24), now: NOW });
    expect(attr(five, "algebra").rated).toBe(true);
  });

  it("weak exam performance floors at 40, not below", () => {
    const p = computeRatings({ attempts: eshAttempts("trigonometry", 40, 6), now: NOW });
    const a = attr(p, "trigonometry"); // 15% on ЭШ
    expect(a.rated).toBe(true);
    expect(a.score).toBe(FLOOR);
    expect(a.band).toBe("beginner");
  });

  it("the owner's scenario: two ЭШ tests — not enough to rate, so route to placement", () => {
    // Two 36-question mocks spread over the common topics. That's below the
    // ~5-test bar, so attributes stay UNRATED ("—") — but we still see the
    // weakness signal and route the focus topic to its adaptive placement.
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
        algebra: 8, geometry: 6, trigonometry: 5, functions: 5,
        probability: 4, calculus: 4, sequences: 3,
      }),
      now: NOW,
    });

    // Not enough evidence yet → nothing rated, everything "—".
    for (const key of ["algebra", "geometry", "trigonometry", "probstats", "calculus", "numbers", "linear"]) {
      expect(attr(p, key).rated, key).toBe(false);
    }
    // But there IS evidence, so the recommendation fires and routes to the
    // weakest topic's placement — never Grade 6 off a blank.
    const rec = recommendedCourse(p);
    expect(rec).not.toBeNull();
    expect(rec!.needsPlacement).toBe(true);
    expect(rec!.attribute).not.toBe("numbers"); // numbers never appeared
    expect(rec!.placementHref).toContain("/placement");
    expect(rec!.explanationEn.toLowerCase()).toContain("placement test");
    expect(rec!.improvements[0].kind).toBe("placement");
  });

  it("a completed placement test rates the attribute accurately (not a low seed)", () => {
    const p = computeRatings({
      attempts: [],
      placements: [
        {
          namespace: "geometry",
          takenAt: NOW - DAY,
          // A deep adaptive run: 12 questions, 90% correct.
          topicScores: [
            { slug: "foundations", seen: 6, correct: 5 },
            { slug: "circles", seen: 6, correct: 6 },
          ],
        },
      ],
      now: NOW,
    });
    const a = attr(p, "geometry");
    expect(a.rated).toBe(true);
    // ~92% · 0.9 difficulty ≈ 83 — a real, accurate rating, well above the
    // old 70 seed cap. And a full adaptive run is confident, not provisional.
    expect(a.score).toBeGreaterThan(75);
    expect(a.provisional).toBe(false);
    expect(p.hasAnyEvidence).toBe(true);
  });
});

describe("recommendations", () => {
  it("recommends the lowest RATED attribute with an owner's-voice explanation", () => {
    // Rate two attributes via deep placements; geometry lower than algebra.
    const p = computeRatings({
      attempts: [],
      placements: [
        {
          namespace: "geometry",
          takenAt: NOW - DAY,
          topicScores: [
            { slug: "foundations", seen: 6, correct: 3 },
            { slug: "circles", seen: 6, correct: 3 }, // ~50% → low geometry
          ],
        },
        {
          namespace: "algebra-1",
          takenAt: NOW - DAY,
          topicScores: [
            { slug: "expressions-and-operations", seen: 6, correct: 6 },
            { slug: "linear-equations", seen: 6, correct: 6 }, // 100% → high algebra
          ],
        },
      ],
      now: NOW,
    });
    const rec = recommendedCourse(p);
    expect(rec).not.toBeNull();
    // Only rated attributes may be recommended; geometry is the lower one.
    expect(attr(p, rec!.attribute).rated).toBe(true);
    expect(rec!.attribute).toBe("geometry");
    expect(rec!.needsPlacement).toBe(false); // a full placement is confident
    expect(rec!.courseHref.startsWith("/math")).toBe(true);
    expect(rec!.explanationEn).toContain(`is ${rec!.score}`);
    expect(rec!.explanationMn).toContain("үнэлгээ");
    expect(rec!.explanationMn).toContain("зөвлөж байна");
  });

  it("improvements: unrated → placement; rated-weak → a concrete +N step", () => {
    // Unrated attribute: the only step is 'take the placement to get rated'.
    const blank = computeRatings({ attempts: eshAttempts("algebra", 3, 2), now: NOW });
    // (algebra unrated here) — the recommendation's steps lead with placement.
    const rec = recommendedCourse(blank);
    if (rec) expect(rec.improvements[0].kind).toBe("placement");

    // Rated attribute with a weak, untested unit → a step that raises it.
    const p = computeRatings({
      attempts: [
        // Rate geometry via a deep placement at a middling level...
        ...lessonAttempts("course:geometry", "triangles-and-congruence", 10, { correctEvery: 2 }),
      ],
      placements: [
        {
          namespace: "geometry",
          takenAt: NOW - DAY,
          topicScores: [
            { slug: "foundations", seen: 6, correct: 4 },
            { slug: "circles", seen: 6, correct: 4 },
          ],
        },
      ],
      now: NOW,
    });
    const geo = attr(p, "geometry");
    if (geo.rated) {
      const gains = geo.improvements.filter((s) => (s.delta ?? 0) > 0);
      expect(gains.length).toBeGreaterThan(0);
      // Each projected gain is honest: projectedScore = current + delta.
      for (const s of gains) {
        expect(s.projectedScore).toBe(geo.score + s.delta!);
        expect(s.href.length).toBeGreaterThan(0);
      }
      // Unit steps point into the course; the mock-exam step into practice.
      expect(gains.every((s) => s.href.startsWith("/math") || s.href.startsWith("/practice"))).toBe(true);
    }
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
      "course:geometry/foundations": FULL_BANK,
      "course:geometry/reasoning-and-proof": FULL_BANK,
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

// ---------------------------------------------------------------------------
// The reported scenario: strong-but-imperfect SAT mocks plus a PERFECT
// Algebra 2 placement left Functions in the 60s with no explanation and no
// next steps. The score being strict is by design; the dashboard must now
// expose WHY (evidence streams) and WHAT NEXT (non-empty improvements).
// ---------------------------------------------------------------------------

function satAttempts(topic: string, n: number, nCorrect: number, ageDays = 1): RatingAttempt[] {
  return Array.from({ length: n }, (_, i) => ({
    context: "sat",
    topic,
    subtopic: "misc",
    isCorrect: i < nCorrect,
    timestamp: NOW - ageDays * DAY,
    source: "test",
  }));
}

describe("evidence transparency + guidance", () => {
  const alg2FunctionUnits = allRatedUnits().filter(
    (u) => u.context === "course:algebra-2" && u.attribute === "functions",
  );

  const profile = () =>
    computeRatings({
      // 20 SAT advanced-math questions at 65% — the drag on the blend.
      attempts: satAttempts("advanced-math", 20, 13),
      placements: [
        {
          namespace: "algebra-2",
          takenAt: NOW - DAY,
          // Perfect placement across the functions-mapped Algebra 2 units.
          topicScores: alg2FunctionUnits.map((u) => ({ slug: u.slug, seen: 2, correct: 2 })),
        },
      ],
      now: NOW,
    });

  it("every attribute carries an evidence breakdown", () => {
    const p = profile();
    for (const a of p.attributes) {
      expect(Array.isArray(a.evidence.streams)).toBe(true);
      expect(a.evidence.combinedConf).toBeGreaterThanOrEqual(0);
      expect(a.evidence.combinedConf).toBeLessThanOrEqual(1);
    }
  });

  it("exam+placement evidence shows both streams, SAT difficulty, and stays strict", () => {
    const p = profile();
    const f = attr(p, "functions");
    expect(f.rated).toBe(true);
    const kinds = f.evidence.streams.map((s) => s.kind).sort();
    expect(kinds).toEqual(["exam", "placement"]);
    // SAT-only exam evidence → attempt-weighted difficulty is the SAT dial.
    expect(f.evidence.examDifficulty).toBeCloseTo(0.8, 5);
    // Strictness preserved: a perfect placement does NOT push past 90, and the
    // 65% SAT evidence holds the blend below the placement's own 90.
    expect(f.score).toBeLessThan(90);
    expect(f.score).toBeGreaterThanOrEqual(55);
  });

  it("a rated attribute with no course work still gets concrete next steps", () => {
    const p = profile();
    const f = attr(p, "functions");
    expect(f.improvements.length).toBeGreaterThan(0);
    // The honest big lever: prove it on a harder mock (+N computed for real).
    const mock = f.improvements.find((s) => s.kind === "mock-exam");
    expect(mock).toBeDefined();
    expect(mock!.delta ?? 0).toBeGreaterThanOrEqual(1);
    // And a course step exists (work the ladder course, pass its unit tests).
    const course = f.improvements.find((s) => s.kind === "master-unit" || s.kind === "unit-test");
    expect(course).toBeDefined();
    // Every projected gain is simulated against the real formula.
    for (const s of f.improvements) {
      if (s.projectedScore !== undefined) {
        expect(s.projectedScore).toBeGreaterThan(f.score);
        expect(s.projectedScore).toBeLessThanOrEqual(100);
      }
    }
  });
});

// ---------------------------------------------------------------------------
// Problem-bank credit — the two promises made to students, as tests.
//
//   1. Bank practice can ONLY help. Nothing a student does in the bank, and
//      no shape of bank evidence, may lower any number on the ratings card.
//      Punishing a wrong answer on voluntary practice teaches students that
//      the safe move is to stop practising.
//   2. It has to be EARNED. A handful of problems must barely move the
//      overall, or the number stops meaning anything.
//
// These pull in opposite directions, which is exactly why they are pinned.
// ---------------------------------------------------------------------------

// Every geometry-attribute unit that lives in the Geometry course.
function geometryUnits() {
  return allRatedUnits().filter((u) => u.attribute === "geometry" && u.context === "course:geometry");
}

describe("problem bank: practice can only ever help", () => {
  it("a bank-only unit never drags an attribute down", () => {
    // The dangerous shape: an attribute whose course mastery is a MEAN over
    // touched units, plus one unit lit up by bank work alone. Averaging that
    // unit in naively would LOWER the attribute — the student practises and
    // the card drops.
    const [proven, fresh] = geometryUnits();
    const attempts = [
      ...lessonAttempts("course:geometry", proven.slug, 12),
      ...testAttempts("course:geometry", proven.slug, 9, 9),
    ];
    const before = computeRatings({ attempts, now: NOW });
    const after = computeRatings({
      attempts,
      bank: { [`course:geometry/${fresh.slug}`]: { solvedForms: 6, solvedProblems: 8 } },
      now: NOW,
    });

    expect(attr(after, "geometry").score).toBeGreaterThanOrEqual(attr(before, "geometry").score);
    expect(after.overall).toBeGreaterThanOrEqual(before.overall);
  });

  it("no amount or shape of bank work lowers any attribute or the overall", () => {
    const [proven, fresh, third] = geometryUnits();
    const attempts = [
      ...lessonAttempts("course:geometry", proven.slug, 12),
      ...testAttempts("course:geometry", proven.slug, 8, 6),
      ...lessonAttempts("course:geometry", third.slug, 6, { correctEvery: 3 }),
    ];
    const baseline = computeRatings({ attempts, now: NOW });

    // Sweep from "one lucky problem" to "ground out the whole unit", on a
    // fresh unit and on an already-worked one.
    const shapes: BankEvidence[] = [];
    for (const forms of [1, 2, 6, 12]) {
      for (const problems of [1, 3, 8, 24, 90]) {
        if (problems < forms) continue;
        shapes.push({ [`course:geometry/${fresh.slug}`]: { solvedForms: forms, solvedProblems: problems } });
        shapes.push({ [`course:geometry/${proven.slug}`]: { solvedForms: forms, solvedProblems: problems } });
        shapes.push({
          [`course:geometry/${fresh.slug}`]: { solvedForms: forms, solvedProblems: problems },
          [`course:geometry/${third.slug}`]: { solvedForms: forms, solvedProblems: problems },
        });
      }
    }

    for (const bank of shapes) {
      const p = computeRatings({ attempts, bank, now: NOW });
      expect(p.overall, `overall dropped for ${JSON.stringify(bank)}`).toBeGreaterThanOrEqual(
        baseline.overall,
      );
      for (const a of ATTRIBUTES) {
        const now = attr(p, a.key).score;
        const was = attr(baseline, a.key).score;
        expect(now, `${a.key} dropped for ${JSON.stringify(bank)}`).toBeGreaterThanOrEqual(was);
      }
    }
  });

  it("more bank work never scores lower than less", () => {
    const [, fresh] = geometryUnits();
    const attempts = lessonAttempts("course:geometry", geometryUnits()[0].slug, 12);
    let previous = -1;
    for (const problems of [0, 1, 4, 8, 12, 24, 48]) {
      const p = computeRatings({
        attempts,
        bank:
          problems > 0
            ? { [`course:geometry/${fresh.slug}`]: { solvedForms: 6, solvedProblems: problems } }
            : undefined,
        now: NOW,
      });
      expect(p.overall).toBeGreaterThanOrEqual(previous);
      previous = p.overall;
    }
  });

  it("problems a student got WRONG are simply absent — never a penalty", () => {
    // BankEvidence carries solved counts only, so "attempted 40, solved 3"
    // and "attempted 3, solved 3" are the same input. There is no shape of
    // this type that can express a miss, which is the point.
    const [, fresh] = geometryUnits();
    const attempts = lessonAttempts("course:geometry", geometryUnits()[0].slug, 12);
    const noBank = computeRatings({ attempts, now: NOW });
    const allMissed = computeRatings({
      attempts,
      bank: { [`course:geometry/${fresh.slug}`]: { solvedForms: 0, solvedProblems: 0 } },
      now: NOW,
    });
    expect(allMissed.overall).toBe(noBank.overall);
    expect(allMissed.units.find((u) => u.slug === fresh.slug)!.touched).toBe(false);
  });
});

describe("problem bank: credit has to be earned", () => {
  it("a handful of problems barely moves the overall", () => {
    const attempts = lessonAttempts("course:geometry", geometryUnits()[0].slug, 12);
    const before = computeRatings({ attempts, now: NOW });
    // Six problems, one from each of six types — real work, but a fraction
    // of a unit. Must not read as progress the student did not make.
    const after = computeRatings({
      attempts,
      bank: { [`course:geometry/${geometryUnits()[1].slug}`]: { solvedForms: 6, solvedProblems: 6 } },
      now: NOW,
    });
    expect(after.overall - before.overall).toBeLessThanOrEqual(1);
  });

  it("breadth and volume both matter — neither alone is full credit", () => {
    const key = `course:geometry/${geometryUnits()[0].slug}`;
    const C = RATING_CONSTANTS;
    const score = (bank: BankEvidence) =>
      computeRatings({ attempts: [], bank, now: NOW }).units.find(
        (u) => `${u.context}/${u.slug}` === key,
      )!;

    // 90 problems, all of ONE type: breadth caps it at 1/6.
    const grinder = score({ [key]: { solvedForms: 1, solvedProblems: 90 } });
    expect(grinder.bankCredit).toBeCloseTo(1 / C.N_BANK_FORMS, 6);

    // One problem from each of six types: volume caps it at 6/24.
    const sampler = score({ [key]: { solvedForms: C.N_BANK_FORMS, solvedProblems: 6 } });
    expect(sampler.bankCredit).toBeCloseTo(6 / C.N_BANK_PROBLEMS, 6);

    // Both targets met — and no more than full credit for overshooting.
    const worker = score({
      [key]: { solvedForms: C.N_BANK_FORMS, solvedProblems: C.N_BANK_PROBLEMS },
    });
    expect(worker.bankCredit).toBe(1);
    expect(score({ [key]: { solvedForms: 40, solvedProblems: 500 } }).bankCredit).toBe(1);
  });

  it("bank work alone can never rate an attribute", () => {
    // Full bank credit on every geometry unit, and nothing else. The bank is
    // practice, not evidence of exam ability: it must not be enough to put a
    // number on the card by itself.
    const bank: BankEvidence = {};
    for (const u of allRatedUnits().filter((x) => x.attribute === "geometry")) {
      bank[`${u.context}/${u.slug}`] = {
        solvedForms: RATING_CONSTANTS.N_BANK_FORMS,
        solvedProblems: RATING_CONSTANTS.N_BANK_PROBLEMS,
      };
    }
    const p = computeRatings({ attempts: [], bank, now: NOW });
    const geometry = attr(p, "geometry");
    expect(geometry.rated).toBe(false);
    // ...and even if it were shown, grinding the bank tops out well short of
    // the ceiling: no unit test means the CAP_NO_UNIT_TEST cap still applies.
    expect(geometry.score).toBeLessThanOrEqual(RATING_CONSTANTS.CAP_NO_UNIT_TEST);
  });
});

// ---------------------------------------------------------------------------
// SAT and IB bank practice (owner request, 2026-08-13). Two different routes
// in, because the two banks are shaped differently:
//   • the IB banks' units ARE the IB courses' units, so their work lands on
//     those units exactly like /math bank work;
//   • the SAT bank is organized by the 20 exam domains, which are not course
//     units, so its work lands on the ATTRIBUTE as a practice stream.
// Both obey the same two promises: only ever helps, and has to be earned.
// ---------------------------------------------------------------------------

describe("SAT and IB bank practice", () => {
  it("maps every shipped SAT bank unit to an attribute", () => {
    // The gate that stops a new SAT domain silently dropping out of the
    // ratings: the bank ships the units, this table must know them all.
    const shipped = getSatBankTopic().units.map((u) => u.id);
    expect(shipped.length).toBeGreaterThan(0);
    const missing = shipped.filter((id) => !SAT_BANK_ATTRIBUTE[id]);
    expect(missing, `SAT bank units with no attribute: ${missing.join(", ")}`).toEqual([]);
    // And no stale entries pointing at domains the bank no longer ships.
    const stale = Object.keys(SAT_BANK_ATTRIBUTE).filter((id) => !shipped.includes(id));
    expect(stale, `stale SAT attribute entries: ${stale.join(", ")}`).toEqual([]);
  });

  it("agrees with the exam-domain map where they overlap", () => {
    // SAT_DOMAIN_ATTRIBUTE routes SAT TEST attempts; SAT_BANK_ATTRIBUTE routes
    // SAT BANK practice. Both must send the same maths to the same attribute.
    expect(SAT_BANK_ATTRIBUTE["linear-equations-one-variable"]).toBe(SAT_DOMAIN_ATTRIBUTE.algebra);
    expect(SAT_BANK_ATTRIBUTE["nonlinear-functions"]).toBe(SAT_DOMAIN_ATTRIBUTE["advanced-math"]);
    expect(SAT_BANK_ATTRIBUTE["one-variable-data"]).toBe(
      SAT_DOMAIN_ATTRIBUTE["problem-solving-data"],
    );
    expect(SAT_BANK_ATTRIBUTE["lines-angles-and-triangles"]).toBe(
      SAT_DOMAIN_ATTRIBUTE["geometry-trig"],
    );
  });

  it("IB bank units land on the IB course's rated units", () => {
    const ibUnits = allRatedUnits().filter((u) => u.context === "course:ib-sl");
    expect(ibUnits.length).toBeGreaterThan(0);
    const target = ibUnits[0];
    const p = computeRatings({
      attempts: [],
      bank: {
        [`course:ib-sl/${target.slug}`]: {
          solvedForms: RATING_CONSTANTS.N_BANK_FORMS,
          solvedProblems: RATING_CONSTANTS.N_BANK_PROBLEMS,
        },
      },
      now: NOW,
    });
    const u = p.units.find((x) => x.context === "course:ib-sl" && x.slug === target.slug)!;
    expect(u.bankCredit).toBe(1);
    expect(u.touched).toBe(true);
    expect(u.bankSolved).toBe(RATING_CONSTANTS.N_BANK_PROBLEMS);
  });

  it("SAT bank practice shows as its own evidence stream on the right attribute", () => {
    // A modest exam record, so practice argues UP rather than down and the
    // stream survives into the displayed evidence.
    const p = computeRatings({
      attempts: eshAttempts("algebra", 40, 12),
      hubBank: {
        "sat/linear-equations-one-variable": { solvedForms: 8, solvedProblems: 30 },
        "sat/equivalent-expressions": { solvedForms: 6, solvedProblems: 25 },
      },
      now: NOW,
    });
    const algebra = attr(p, "algebra");
    const practice = algebra.evidence.streams.find((s) => s.kind === "practice");
    expect(practice, "algebra should carry a practice stream").toBeDefined();
    expect(practice!.certifying).toBe(false);
    expect(practice!.n).toBe(55);
    // Practice without a test tops out in Developing, the same ceiling a unit
    // gets with no test behind it — drilling cannot argue you are a 100.
    expect(practice!.perf).toBeLessThanOrEqual(RATING_CONSTANTS.CAP_NO_UNIT_TEST);
    // ...and it lands nowhere else.
    expect(attr(p, "geometry").evidence.streams.some((s) => s.kind === "practice")).toBe(false);
  });

  it("SAT bank practice alone never rates an attribute", () => {
    // Every SAT algebra domain ground out, and nothing else. Self-paced,
    // retryable practice is not evidence of exam ability at any volume.
    const hubBank: Record<string, { solvedForms: number; solvedProblems: number }> = {};
    for (const [unit, a] of Object.entries(SAT_BANK_ATTRIBUTE)) {
      if (a === "algebra") hubBank[`sat/${unit}`] = { solvedForms: 40, solvedProblems: 500 };
    }
    const p = computeRatings({ attempts: [], hubBank, now: NOW });
    const algebra = attr(p, "algebra");
    expect(algebra.rated).toBe(false);
    expect(algebra.score).toBe(RATING_CONSTANTS.RATING_FLOOR);
    expect(p.overall).toBe(RATING_CONSTANTS.RATING_FLOOR);
  });

  it("SAT bank practice can only ever help a rated attribute", () => {
    // Including the case that motivates the max() guard: a strong exam record
    // plus modest practice, where blending practice in would argue LOWER.
    const strong = eshAttempts("algebra", 40, 38);
    const baseline = computeRatings({ attempts: strong, now: NOW });
    for (const [forms, problems] of [
      [1, 1],
      [4, 10],
      [12, 48],
      [40, 500],
    ]) {
      const p = computeRatings({
        attempts: strong,
        hubBank: { "sat/linear-equations-one-variable": { solvedForms: forms, solvedProblems: problems } },
        now: NOW,
      });
      expect(
        attr(p, "algebra").score,
        `algebra dropped at ${forms} forms / ${problems} problems`,
      ).toBeGreaterThanOrEqual(attr(baseline, "algebra").score);
      expect(p.overall).toBeGreaterThanOrEqual(baseline.overall);
    }
  });

  it("SAT practice credit needs breadth AND volume, like every other bank", () => {
    const C = RATING_CONSTANTS;
    const credit = (solvedForms: number, solvedProblems: number) =>
      practiceCredit({ solvedForms, solvedProblems });
    expect(credit(1, 200)).toBeCloseTo(1 / C.N_PRACTICE_FORMS, 6); // no breadth
    expect(credit(C.N_PRACTICE_FORMS, 6)).toBeCloseTo(6 / C.N_PRACTICE_PROBLEMS, 6); // no volume
    expect(credit(C.N_PRACTICE_FORMS, C.N_PRACTICE_PROBLEMS)).toBe(1);
    expect(credit(99, 999)).toBe(1); // never more than full
    expect(practiceCredit(undefined)).toBe(0);
  });

  it("unhelpful practice never cancels out unit credit that WAS helping", () => {
    // The two bank sources are weighed independently. A student with useful
    // /math bank credit plus SAT drilling below their level must keep the
    // benefit of the former.
    const [proven, fresh] = geometryUnits();
    const attempts = [
      ...lessonAttempts("course:geometry", proven.slug, 12),
      ...testAttempts("course:geometry", proven.slug, 9, 9),
      ...eshAttempts("geometry", 40, 38),
    ];
    const unitBankOnly = computeRatings({
      attempts,
      bank: { [`course:geometry/${proven.slug}`]: { solvedForms: 6, solvedProblems: 24 } },
      now: NOW,
    });
    const plusWeakPractice = computeRatings({
      attempts,
      bank: { [`course:geometry/${proven.slug}`]: { solvedForms: 6, solvedProblems: 24 } },
      hubBank: { "sat/lines-angles-and-triangles": { solvedForms: 1, solvedProblems: 1 } },
      now: NOW,
    });
    expect(attr(plusWeakPractice, "geometry").score).toBeGreaterThanOrEqual(
      attr(unitBankOnly, "geometry").score,
    );
  });

  it("practice a strong student has outgrown simply does nothing", () => {
    // A 95% ЭШ record plus a little SAT drilling: the practice stream would
    // argue for a LOWER number than the exams already earned. The guard keeps
    // the higher one, so the card reads "no change" rather than punishing the
    // student for practising.
    const strong = eshAttempts("algebra", 40, 38);
    const baseline = computeRatings({ attempts: strong, now: NOW });
    const withPractice = computeRatings({
      attempts: strong,
      hubBank: { "sat/linear-equations-one-variable": { solvedForms: 1, solvedProblems: 2 } },
      now: NOW,
    });
    expect(attr(withPractice, "algebra").score).toBe(attr(baseline, "algebra").score);
    expect(
      attr(withPractice, "algebra").evidence.streams.some((s) => s.kind === "practice"),
      "the rejected practice stream should not be shown as the reason for the score",
    ).toBe(false);
  });
});
