import { describe, expect, it } from "vitest";
import { existsSync } from "fs";
import { join } from "path";
import {
  getSatTest,
  gradeSatQuestion,
  gradeSpr,
  listSatTests,
  module2KeyForRaw,
  satAnalyticsTopic,
  scaledScoreEstimate,
  SatModuleKey,
} from "@/lib/sat-test";
import { SAT_DOMAIN_LABELS } from "@/lib/hub-analytics";

const MODULES: SatModuleKey[] = ["module1", "module2Easy", "module2Hard"];
const ALL_TESTS = listSatTests().map((m) => getSatTest(m.testId)!);

describe("SAT test registry", () => {
  it("lists both practice tests with Bluebook-format meta", () => {
    const metas = listSatTests();
    expect(metas.map((m) => m.testId)).toEqual(["sat-practice-1", "sat-practice-2"]);
    for (const m of metas) {
      expect(m.minutesPerModule).toBe(35);
      expect(m.module2Threshold).toBe(15);
    }
  });

  it("every test has 3 modules × 22 questions with globally unique sources", () => {
    const sources = new Set<string>();
    for (const test of ALL_TESTS) {
      for (const key of MODULES) {
        expect(test[key], `${test.meta.testId}.${key}`).toHaveLength(22);
        for (const q of test[key]) sources.add(q.source);
      }
    }
    expect(sources.size).toBe(66 * ALL_TESTS.length);
  });

  it("every question is well-formed and figures exist on disk", () => {
    for (const test of ALL_TESTS) {
      for (const key of MODULES) {
        for (const q of test[key]) {
          if (q.format === "mcq") {
            expect(Object.keys(q.options ?? {}).sort()).toEqual(["A", "B", "C", "D"]);
            expect(Object.keys(q.options ?? {})).toContain(q.answer);
          } else {
            expect(q.acceptedAnswers!.length).toBeGreaterThan(0);
            for (const a of q.acceptedAnswers!) {
              expect(a.length).toBeLessThanOrEqual(a.startsWith("-") ? 6 : 5);
            }
          }
          if (q.figure) {
            expect(existsSync(join(process.cwd(), "public", q.figure.src)),
              `${q.source} figure ${q.figure.src}`).toBe(true);
          }
        }
      }
    }
  });

  it("every domain maps onto the hub-analytics tagging contract", () => {
    for (const test of ALL_TESTS) {
      for (const key of MODULES) {
        for (const q of test[key]) {
          const topic = satAnalyticsTopic(q.domain);
          expect(SAT_DOMAIN_LABELS[topic], `${q.source} domain ${q.domain}`).toBeTruthy();
        }
      }
    }
  });
});

describe("SPR grading", () => {
  it("accepts listed forms and exact rational re-encodings", () => {
    expect(gradeSpr("3", ["3"])).toBe(true);
    expect(gradeSpr(" 3 ", ["3"])).toBe(true);
    expect(gradeSpr("3.0", ["3"])).toBe(true);
    expect(gradeSpr("03", ["3"])).toBe(true);
    expect(gradeSpr("6/2", ["3"])).toBe(true);
    expect(gradeSpr("3.5", ["7/2", "3.5"])).toBe(true);
    expect(gradeSpr("7/2", ["7/2", "3.5"])).toBe(true);
    expect(gradeSpr(".5", ["1/2"])).toBe(true);
    expect(gradeSpr("-12", ["-12"])).toBe(true);
  });

  it("rejects wrong values, empties, and garbage", () => {
    expect(gradeSpr("", ["3"])).toBe(false);
    expect(gradeSpr("4", ["3"])).toBe(false);
    expect(gradeSpr("3/0", ["3"])).toBe(false);
    expect(gradeSpr("three", ["3"])).toBe(false);
    expect(gradeSpr("3.51", ["7/2", "3.5"])).toBe(false);
    expect(gradeSpr("-3", ["3"])).toBe(false);
  });

  it("grades a real SPR and a real MCQ from the bank", () => {
    const test = getSatTest("sat-practice-1")!;
    const spr = test.module1.find((q) => q.source === "SAT-P1-M1-Q06")!;
    expect(gradeSatQuestion(spr, "3")).toBe(true);
    expect(gradeSatQuestion(spr, "2")).toBe(false);
    expect(gradeSatQuestion(spr, undefined)).toBe(false);
    const mcq = test.module1.find((q) => q.source === "SAT-P1-M1-Q01")!;
    expect(gradeSatQuestion(mcq, mcq.answer)).toBe(true);
    expect(gradeSatQuestion(mcq, "A" === mcq.answer ? "B" : "A")).toBe(false);
  });
});

describe("adaptive routing + scaled score", () => {
  it("routes module 2 by the threshold", () => {
    expect(module2KeyForRaw(15, 15)).toBe("module2Hard");
    expect(module2KeyForRaw(22, 15)).toBe("module2Hard");
    expect(module2KeyForRaw(14, 15)).toBe("module2Easy");
    expect(module2KeyForRaw(0, 15)).toBe("module2Easy");
  });

  it("hits the anchor curve exactly and stays monotone", () => {
    expect(scaledScoreEstimate(0)).toBe(200);
    expect(scaledScoreEstimate(8)).toBe(360);
    expect(scaledScoreEstimate(15)).toBe(440);
    expect(scaledScoreEstimate(22)).toBe(510);
    expect(scaledScoreEstimate(30)).toBe(590);
    expect(scaledScoreEstimate(35)).toBe(650);
    expect(scaledScoreEstimate(40)).toBe(730);
    expect(scaledScoreEstimate(44)).toBe(800);
    for (let r = 1; r <= 44; r++) {
      expect(scaledScoreEstimate(r)).toBeGreaterThanOrEqual(scaledScoreEstimate(r - 1));
      expect(scaledScoreEstimate(r) % 10).toBe(0);
    }
    expect(scaledScoreEstimate(-3)).toBe(200);
    expect(scaledScoreEstimate(99)).toBe(800);
  });
});
