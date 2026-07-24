import { describe, expect, it } from "vitest";
import {
  IB_GRADE_BOUNDARIES,
  IB_TOPIC_LABELS,
  clampEarned,
  getIbPaper,
  ibAnalyticsTopic,
  ibGradeEstimate,
  ibPaperSourcePrefix,
  ibPartKey,
  listIbPapers,
  listIbPracticeSets,
  tallyByTopic,
  tallyPaper,
} from "./ib-test";

describe("IB paper registry", () => {
  it("lists both AA SL papers of ib-practice-1", () => {
    const metas = listIbPapers();
    expect(metas.length).toBeGreaterThanOrEqual(2);
    const p1 = metas.find((m) => m.testId === "ib-practice-1" && m.paper === 1);
    const p2 = metas.find((m) => m.testId === "ib-practice-1" && m.paper === 2);
    expect(p1).toBeDefined();
    expect(p2).toBeDefined();
    expect(p1!.calculator).toBe(false); // AA Paper 1 is the no-calculator paper
    expect(p2!.calculator).toBe(true);
  });

  it("routes getIbPaper by testId + paper number", () => {
    expect(getIbPaper("ib-practice-1", 1)?.meta.paper).toBe(1);
    expect(getIbPaper("ib-practice-1", 2)?.meta.paper).toBe(2);
    expect(getIbPaper("ib-practice-1", 3)).toBeUndefined();
    expect(getIbPaper("nope", 1)).toBeUndefined();
  });

  it("every paper is internally consistent (marks arithmetic)", () => {
    for (const meta of listIbPapers()) {
      const paper = getIbPaper(meta.testId, meta.paper)!;
      let grand = 0;
      for (const q of paper.questions) {
        const partSum = q.parts.reduce((s, p) => s + p.marks, 0);
        expect(partSum).toBe(q.maximumMark);
        for (const p of q.parts) {
          expect(p.markscheme.length).toBe(p.marks);
        }
        expect(IB_TOPIC_LABELS[q.topic]).toBeDefined();
        grand += q.maximumMark;
      }
      expect(grand).toBe(meta.totalMarks);
      expect(meta.totalMarks).toBe(meta.level === "hl" ? 110 : 80);
    }
  });

  it("lists the AA HL practice set with both 110-mark papers", () => {
    const p1 = getIbPaper("ib-hl-practice-1", 1);
    const p2 = getIbPaper("ib-hl-practice-1", 2);
    expect(p1?.meta.level).toBe("hl");
    expect(p1?.meta.totalMarks).toBe(110);
    expect(p1?.meta.calculator).toBe(false);
    expect(p2?.meta.calculator).toBe(true);
    expect(p2?.meta.timeMinutes).toBe(120);
  });

  it("groups papers into practice sets numbered within each track", () => {
    const sets = listIbPracticeSets();
    const sl = sets.filter((s) => s.level === "sl");
    const hl = sets.filter((s) => s.level === "hl");
    expect(sl.length).toBeGreaterThanOrEqual(3);
    expect(hl.length).toBeGreaterThanOrEqual(1);
    expect(sl[0].label).toBe("AA SL Practice Set 1");
    expect(hl[0].label).toBe("AA HL Practice Set 1"); // numbering restarts per track
    for (const s of sets) {
      expect(s.papers.map((p) => p.paper)).toEqual([1, 2]);
      for (const p of s.papers) {
        expect(ibPaperSourcePrefix(p.testId, p.paper)).toMatch(/^IB-/);
      }
    }
  });

  it("maps meta onto the hub-analytics component vocabulary", () => {
    const meta = getIbPaper("ib-practice-1", 1)!.meta;
    expect(ibAnalyticsTopic(meta)).toBe("aa-paper-1");
    expect(ibAnalyticsTopic(getIbPaper("ib-practice-1", 2)!.meta)).toBe("aa-paper-2");
    // HL papers carry an explicit level segment so SL/HL stats never blend.
    expect(ibAnalyticsTopic(getIbPaper("ib-hl-practice-1", 1)!.meta)).toBe("aa-hl-paper-1");
  });
});

describe("marks tallying", () => {
  it("clamps self-awarded marks to the part bracket", () => {
    expect(clampEarned(2, 3)).toBe(2);
    expect(clampEarned(5, 3)).toBe(3);
    expect(clampEarned(-1, 3)).toBe(0);
    expect(clampEarned(Number.NaN, 3)).toBe(0);
    expect(clampEarned(2.6, 3)).toBe(3); // rounds
  });

  it("tallies a fully-marked paper to its total", () => {
    const paper = getIbPaper("ib-practice-1", 1)!;
    const full: Record<string, number> = {};
    for (const q of paper.questions) {
      for (const p of q.parts) full[ibPartKey(q, p)] = p.marks;
    }
    expect(tallyPaper(paper, full)).toEqual({ earned: 80, total: 80 });
  });

  it("missing entries count zero; overclaims are clamped", () => {
    const paper = getIbPaper("ib-practice-1", 1)!;
    const q0 = paper.questions[0];
    const p0 = q0.parts[0];
    const t = tallyPaper(paper, { [ibPartKey(q0, p0)]: 999 });
    expect(t.total).toBe(80);
    expect(t.earned).toBe(p0.marks);
  });

  it("tallyByTopic partitions the full 80 marks across the 5 topics", () => {
    const paper = getIbPaper("ib-practice-1", 2)!;
    const by = tallyByTopic(paper, {});
    const total = Object.values(by).reduce((s, b) => s + b.total, 0);
    expect(total).toBe(80);
    expect(Object.keys(by).sort()).toEqual(
      ["calculus", "functions", "geometry_trig", "number_algebra", "stats_probability"],
    );
  });
});

describe("indicative grade bands", () => {
  it("uses the documented AA SL boundaries", () => {
    expect(ibGradeEstimate(100)).toBe(7);
    expect(ibGradeEstimate(71)).toBe(7);
    expect(ibGradeEstimate(70.9)).toBe(6);
    expect(ibGradeEstimate(59)).toBe(6);
    expect(ibGradeEstimate(47)).toBe(5);
    expect(ibGradeEstimate(36)).toBe(4);
    expect(ibGradeEstimate(25)).toBe(3);
    expect(ibGradeEstimate(15)).toBe(2);
    expect(ibGradeEstimate(14.9)).toBe(1);
    expect(ibGradeEstimate(0)).toBe(1);
  });

  it("boundaries are strictly descending and end at grade 1 / 0%", () => {
    for (let i = 1; i < IB_GRADE_BOUNDARIES.length; i++) {
      expect(IB_GRADE_BOUNDARIES[i].minPercent).toBeLessThan(
        IB_GRADE_BOUNDARIES[i - 1].minPercent,
      );
      expect(IB_GRADE_BOUNDARIES[i].grade).toBe(
        IB_GRADE_BOUNDARIES[i - 1].grade - 1,
      );
    }
    const last = IB_GRADE_BOUNDARIES[IB_GRADE_BOUNDARIES.length - 1];
    expect(last).toEqual({ grade: 1, minPercent: 0 });
  });

  it("clamps out-of-range percentages", () => {
    expect(ibGradeEstimate(-5)).toBe(1);
    expect(ibGradeEstimate(140)).toBe(7);
  });
});
