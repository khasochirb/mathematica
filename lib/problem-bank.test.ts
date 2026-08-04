import { describe, it, expect } from "vitest";
import { getBankTopics, getBankTopic, getSatBankTopic, getIbBankTopic } from "./bank-data";
import {
  getBankUnit,
  unitForms,
  unitMastery,
  initSession,
  currentItem,
  answerCurrent,
  isDone,
  summarize,
  displayVariant,
  sessionForms,
  getVariant,
  topicMastery,
  type BankProgress,
} from "./problem-bank";

// Deterministic rng: always picks the first element / identity shuffle.
const rng0 = () => 0;

describe("problem bank data", () => {
  it("ships the course-ladder subjects, each mirroring its course units, >= 4 variants per form", () => {
    const topics = getBankTopics();
    expect(topics.map((t) => t.slug)).toEqual([
      "algebra-1",
      "algebra-2",
      "geometry",
      "trigonometry",
      "solid-geometry",
      "prob-stats",
      "precalculus",
      "calculus",
      "vectors-matrices",
      "integrated-1",
      "integrated-2",
      "integrated-3",
      "4",
      "5",
      "9",
      "12",
    ]);
    for (const t of topics) {
      expect(t.units.length).toBeGreaterThanOrEqual(6);
      const unitIds = new Set(t.units.map((u) => u.id));
      const levels = new Set(t.forms.map((f) => f.level));
      expect(levels).toEqual(new Set([1, 2, 3]));
      for (const f of t.forms) {
        expect(unitIds.has(f.unit), `${t.slug}/${f.id} unit ${f.unit}`).toBe(true);
        expect(f.variants.length, `${t.slug}/${f.id}`).toBeGreaterThanOrEqual(4);
        for (const v of f.variants) {
          expect(v.options.length).toBe(4);
          expect(new Set(v.options).size).toBe(4);
          expect(v.correctIndex).toBeGreaterThanOrEqual(0);
          expect(v.correctIndex).toBeLessThanOrEqual(3);
        }
      }
    }
  });

  it("keeps the SAT hub's bank out of the course-ladder list, in SAT taxonomy", () => {
    const sat = getSatBankTopic();
    expect(sat.slug).toBe("sat");
    // the hub's OWN taxonomy: the four Digital SAT domains, in test order
    expect(sat.units.map((u) => u.id)).toEqual([
      "algebra",
      "advanced-math",
      "problem-solving-data",
      "geometry-trig",
    ]);
    for (const u of sat.units) {
      expect(unitForms(sat, u.id).length, u.id).toBeGreaterThanOrEqual(6);
    }
    for (const f of sat.forms) {
      expect(f.variants.length, f.id).toBeGreaterThanOrEqual(4);
    }
    expect(new Set(sat.forms.map((f) => f.level))).toEqual(new Set([1, 2, 3]));
    // NOT a /math course subject: it must not appear on the General Math
    // bank hub, in the ratings card, or in placement wiring...
    expect(getBankTopics().some((t) => t.slug === "sat")).toBe(false);
    // ...and /math/problem-bank/sat must 404, not render the SAT bank.
    expect(getBankTopic("sat")).toBeNull();
  });

  it("keeps the IB banks out of the course-ladder list, in the 5-topic taxonomy", () => {
    // the hub's OWN taxonomy: the five syllabus topics in syllabus order,
    // with unit ids equal to the COURSE unit slugs so lesson links resolve
    const syllabus = [
      "number-and-algebra",
      "functions",
      "geometry-and-trigonometry",
      "statistics-and-probability",
      "calculus",
    ];
    for (const tier of ["sl", "hl"] as const) {
      const t = getIbBankTopic(tier);
      expect(t.slug).toBe(`ib-${tier}`);
      expect(t.units.map((u) => u.id)).toEqual(syllabus);
      for (const u of t.units) {
        expect(unitForms(t, u.id).length, `${tier}/${u.id}`).toBeGreaterThanOrEqual(4);
      }
      for (const f of t.forms) {
        expect(f.variants.length, f.id).toBeGreaterThanOrEqual(4);
      }
      expect(new Set(t.forms.map((f) => f.level))).toEqual(new Set([1, 2, 3]));
      // NOT a /math course subject, and /math/problem-bank/ib-* must 404
      expect(getBankTopics().some((x) => x.slug === t.slug)).toBe(false);
      expect(getBankTopic(t.slug)).toBeNull();
    }
    // the two tiers are genuinely different banks
    expect(getIbBankTopic("sl")).not.toBe(getIbBankTopic("hl"));
  });

  it("resolves subjects, units, and variants by id", () => {
    const t = getBankTopic("algebra-1")!;
    expect(t.title).toBe("Algebra 1");
    const f = t.forms[0];
    const v = getVariant(t, f.id, f.variants[0].id);
    expect(v?.id).toBe(f.variants[0].id);
    expect(getBankTopic("nope")).toBeNull();
    const u = getBankUnit(t, t.units[0].id)!;
    expect(u.id).toBe(t.units[0].id);
    expect(getBankUnit(t, "nope")).toBeNull();
    // unit scoping: every unit form really belongs to the unit
    for (const uf of unitForms(t, u.id)) {
      expect(uf.unit).toBe(u.id);
    }
  });
});

describe("session engine", () => {
  const topic = getBankTopic("algebra-1")!;

  it("serves one variant per form, easier levels first", () => {
    const s = initSession(topic, 0, rng0);
    expect(s.queue.length).toBe(topic.forms.length);
    const levels = s.queue.map((q) => topic.forms.find((f) => f.id === q.formId)!.level);
    expect([...levels]).toEqual([...levels].sort((a, b) => a - b));
    // every form exactly once
    expect(new Set(s.queue.map((q) => q.formId)).size).toBe(topic.forms.length);
  });

  it("level filter narrows the sweep to that level's forms", () => {
    const s = initSession(topic, 2, rng0);
    expect(s.queue.length).toBe(sessionForms(topic, 2).length);
    for (const q of s.queue) {
      expect(topic.forms.find((f) => f.id === q.formId)!.level).toBe(2);
    }
  });

  it("a MISS queues a similar problem (sibling variant, same form) immediately next", () => {
    let s = initSession(topic, 0, rng0);
    const first = currentItem(s)!;
    s = answerCurrent(topic, s, false, rng0);
    const retry = currentItem(s)!;
    expect(retry.formId).toBe(first.formId); // same form = similar problem
    expect(retry.variantId).not.toBe(first.variantId); // different numbers
    expect(retry.isRetry).toBe(true);
  });

  it("a correct answer does NOT queue a retry", () => {
    let s = initSession(topic, 0, rng0);
    const len = s.queue.length;
    s = answerCurrent(topic, s, true, rng0);
    expect(s.queue.length).toBe(len);
    expect(currentItem(s)!.isRetry).toBe(false);
  });

  it("retries are capped and never repeat a served variant", () => {
    let s = initSession(topic, 0, rng0);
    const formId = currentItem(s)!.formId;
    // miss the original + both granted retries
    s = answerCurrent(topic, s, false, rng0);
    s = answerCurrent(topic, s, false, rng0);
    s = answerCurrent(topic, s, false, rng0);
    // cap reached: next item is a different form
    expect(currentItem(s)!.formId).not.toBe(formId);
    const servedForForm = s.served[formId];
    expect(new Set(servedForForm).size).toBe(servedForForm.length);
  });

  it("finishes and summarizes: recovered vs needsWork", () => {
    let s = initSession(topic, 0, rng0);
    const firstForm = currentItem(s)!.formId;
    s = answerCurrent(topic, s, false, rng0); // miss form 1
    s = answerCurrent(topic, s, true, rng0); // similar one: recovered
    const secondForm = currentItem(s)!.formId;
    s = answerCurrent(topic, s, false, rng0); // miss form 2
    s = answerCurrent(topic, s, false, rng0); // miss the similar too
    s = answerCurrent(topic, s, false, rng0); // and the second similar
    while (!isDone(s)) s = answerCurrent(topic, s, true, rng0);

    const sum = summarize(topic, s);
    const f1 = sum.forms.find((f) => f.formId === firstForm)!;
    expect(f1.recovered).toBe(true);
    expect(f1.needsWork).toBe(false);
    const f2 = sum.forms.find((f) => f.formId === secondForm)!;
    expect(f2.needsWork).toBe(true);
    expect(sum.needsWork.map((f) => f.formId)).toContain(secondForm);
    expect(sum.total).toBe(s.answers.length);
    expect(sum.perLevel.reduce((n, l) => n + l.total, 0)).toBe(sum.total);
  });

  it("form-filtered session powers 'practice these again'", () => {
    const weak = [topic.forms[2].id, topic.forms[5].id];
    const s = initSession(topic, 0, rng0, weak);
    expect(s.queue.map((q) => q.formId).sort()).toEqual([...weak].sort());
  });
});

describe("option shuffle", () => {
  it("keeps the correct answer under the mapped index", () => {
    const topic = getBankTopic("geometry")!;
    const v = topic.forms[0].variants[0];
    for (const seed of [0, 0.33, 0.67, 0.99]) {
      const d = displayVariant(v, () => seed);
      expect(d.options[d.correctIndex]).toBe(v.options[v.correctIndex]);
      expect([...d.options].sort()).toEqual([...v.options].sort());
    }
  });
});

describe("mastery", () => {
  it("counts mastered forms against the topic total", () => {
    const topic = getBankTopic("algebra-2")!;
    const progress: BankProgress = {
      version: 1,
      forms: {
        [topic.forms[0].id]: { mastered: true, attempts: 1, correct: 1, updatedAt: 1 },
        [topic.forms[1].id]: { mastered: false, attempts: 2, correct: 0, updatedAt: 1 },
      },
    };
    expect(topicMastery(topic, progress)).toEqual({ mastered: 1, total: topic.forms.length });
  });

  it("unit mastery counts only that unit's forms", () => {
    const topic = getBankTopic("trigonometry")!;
    const unit = topic.units.find((u) => unitForms(topic, u.id).length > 0)!;
    const forms = unitForms(topic, unit.id);
    const progress: BankProgress = {
      version: 1,
      forms: { [forms[0].id]: { mastered: true, attempts: 1, correct: 1, updatedAt: 1 } },
    };
    expect(unitMastery(topic, unit.id, progress)).toEqual({ mastered: 1, total: forms.length });
  });
});
