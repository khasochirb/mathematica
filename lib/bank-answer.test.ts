import { describe, it, expect } from "vitest";
import {
  checkNumericAnswer,
  formAnswerMode,
  parseNumericAnswer,
  parseStudentAnswer,
  seededOptionOrder,
  variantAnswerMode,
} from "./bank-answer";

// The grader's contract. These tests exist because BOTH failure modes are
// expensive and silent:
//   - accepting a wrong value teaches the student the wrong thing;
//   - rejecting a RIGHT answer because of how it was written is worse than
//     the peeking problem this whole feature was built to fix, and it is the
//     failure a student will never report — they will just assume they were
//     wrong.
// So: every authored answer shape the corpus actually contains is pinned
// here, and so is every way a student plausibly writes a right answer.

describe("parsing authored answers", () => {
  it("reads the numeric shapes the corpus contains", () => {
    expect(parseNumericAnswer("$-6$")).toBe(-6);
    expect(parseNumericAnswer("$0$")).toBe(0);
    expect(parseNumericAnswer("$0.1$")).toBeCloseTo(0.1, 12);
    expect(parseNumericAnswer("$12.75$")).toBeCloseTo(12.75, 12);
    expect(parseNumericAnswer("$\\frac{2}{3}$")).toBeCloseTo(2 / 3, 12);
    expect(parseNumericAnswer("$-\\frac{2}{3}$")).toBeCloseTo(-2 / 3, 12);
    expect(parseNumericAnswer("$\\dfrac{7}{4}$")).toBeCloseTo(7 / 4, 12);
    expect(parseNumericAnswer("$3/8$")).toBeCloseTo(3 / 8, 12);
    expect(parseNumericAnswer("$25\\%$")).toBeCloseTo(0.25, 12);
    expect(parseNumericAnswer("$1{,}250$")).toBe(1250);
    expect(parseNumericAnswer("$12\\text{ cm}$")).toBe(12);
  });

  it("refuses everything that is not a bare number", () => {
    // These are the shapes that MUST fall back to multiple choice — string
    // matching them would mark right answers wrong.
    expect(parseNumericAnswer("$x^2 - 9x + 20$")).toBeNull();
    expect(parseNumericAnswer("$x = -7$ and $x = -6$")).toBeNull();
    expect(parseNumericAnswer("Each additional hour of work adds 25 dollars to the total charge.")).toBeNull();
    expect(parseNumericAnswer("$(x-4)(x-5)$")).toBeNull();
    expect(parseNumericAnswer("$2\\pi$")).toBeNull();
    expect(parseNumericAnswer("$\\sqrt{2}$")).toBeNull();
    expect(parseNumericAnswer("$\\frac{x}{3}$")).toBeNull();
    expect(parseNumericAnswer("")).toBeNull();
    expect(parseNumericAnswer("$$")).toBeNull();
  });

  it("never divides by zero", () => {
    expect(parseNumericAnswer("$\\frac{5}{0}$")).toBeNull();
    expect(parseNumericAnswer("$5/0$")).toBeNull();
  });
});

describe("parsing what a student types", () => {
  it("accepts the natural ways of writing a right answer", () => {
    expect(parseStudentAnswer("5")).toBe(5);
    expect(parseStudentAnswer("  5  ")).toBe(5);
    expect(parseStudentAnswer("+5")).toBe(5);
    expect(parseStudentAnswer("-5")).toBe(-5);
    expect(parseStudentAnswer("−5")).toBe(-5); // U+2212, from a paste
    expect(parseStudentAnswer("x = 5")).toBe(5);
    expect(parseStudentAnswer("y=-5")).toBe(-5);
    expect(parseStudentAnswer("5 cm")).toBe(5);
    expect(parseStudentAnswer("12cm")).toBe(12);
    expect(parseStudentAnswer("12 cm²")).toBe(12);
    expect(parseStudentAnswer("40 degrees")).toBe(40);
    expect(parseStudentAnswer("$5$")).toBe(5);
    expect(parseStudentAnswer(".5")).toBeCloseTo(0.5, 12);
    expect(parseStudentAnswer("5.0")).toBe(5);
    expect(parseStudentAnswer("2/3")).toBeCloseTo(2 / 3, 12);
    expect(parseStudentAnswer("\\frac{2}{3}")).toBeCloseTo(2 / 3, 12);
    expect(parseStudentAnswer("1,250")).toBe(1250); // thousands separator
    expect(parseStudentAnswer("0,5")).toBeCloseTo(0.5, 12); // decimal comma
  });

  it("does not turn an expression into a number", () => {
    // "2x" is not the number 2 — relaxing it would hand out free credit.
    expect(parseStudentAnswer("2x")).toBeNull();
    expect(parseStudentAnswer("x")).toBeNull();
    expect(parseStudentAnswer("abc")).toBeNull();
    expect(parseStudentAnswer("")).toBeNull();
    expect(parseStudentAnswer("   ")).toBeNull();
    expect(parseStudentAnswer("?")).toBeNull();
  });
});

describe("grading a typed answer", () => {
  it("accepts equivalent forms of the same value", () => {
    expect(checkNumericAnswer("5", "$5$")).toBe("correct");
    expect(checkNumericAnswer("5.00", "$5$")).toBe("correct");
    expect(checkNumericAnswer("x = 5", "$5$")).toBe("correct");
    expect(checkNumericAnswer("2/3", "$\\frac{2}{3}$")).toBe("correct");
    expect(checkNumericAnswer("4/6", "$\\frac{2}{3}$")).toBe("correct"); // unreduced
    expect(checkNumericAnswer("0.25", "$25\\%$")).toBe("correct");
    expect(checkNumericAnswer("-6", "$-6$")).toBe("correct");
  });

  it("rejects a different value", () => {
    expect(checkNumericAnswer("6", "$5$")).toBe("incorrect");
    expect(checkNumericAnswer("-5", "$5$")).toBe("incorrect");
    expect(checkNumericAnswer("0.67", "$\\frac{2}{3}$")).toBe("incorrect"); // rounded ≠ exact
    expect(checkNumericAnswer("0", "$0.1$")).toBe("incorrect");
  });

  it("separates 'not a number' from 'wrong'", () => {
    // A student who types something unreadable gets another try, not a miss.
    expect(checkNumericAnswer("", "$5$")).toBe("unparsed");
    expect(checkNumericAnswer("dunno", "$5$")).toBe("unparsed");
    // And a non-numeric authored answer can never be graded this way.
    expect(checkNumericAnswer("5", "$x + 1$")).toBe("unparsed");
  });

  it("tolerates float error but not rounding", () => {
    expect(checkNumericAnswer("0.6666666666666667", "$\\frac{2}{3}$")).toBe("correct");
    expect(checkNumericAnswer("0.666", "$\\frac{2}{3}$")).toBe("incorrect");
  });
});

describe("choosing how a problem is asked", () => {
  it("types the numeric answers and offers choices for the rest", () => {
    expect(variantAnswerMode({ options: ["$3$", "$4$", "$5$", "$6$"], correctIndex: 2 })).toBe("numeric");
    expect(variantAnswerMode({ options: ["$\\frac{1}{2}$", "$1$", "$2$", "$3$"], correctIndex: 0 })).toBe("numeric");
    expect(
      variantAnswerMode({ options: ["$(x-4)(x-5)$", "$(x+4)(x+5)$", "$(x-2)(x-10)$", "$(x-1)(x-20)$"], correctIndex: 0 }),
    ).toBe("choice");
    expect(variantAnswerMode({ options: ["Adds 25 dollars.", "b", "c", "d"], correctIndex: 0 })).toBe("choice");
  });

  it("keeps the options when a DISTRACTOR is not a number", () => {
    // Real corpus cases. The answer parses as a number, but hiding the
    // options would hide an answer the student has no way to type.
    expect(
      variantAnswerMode({ options: ["$0$", "$1$", "$2$", "infinitely many"], correctIndex: 1 }),
    ).toBe("choice");
    expect(variantAnswerMode({ options: ["$1$", "$-1$", "$i$", "$-i$"], correctIndex: 1 })).toBe("choice");
    expect(
      variantAnswerMode({ options: ["$4$", "$\\sqrt{10}$", "$16$", "$10$"], correctIndex: 0 }),
    ).toBe("choice");
  });

  it("falls back to choices when the answer is missing", () => {
    expect(variantAnswerMode({ options: ["$3$"], correctIndex: 7 })).toBe("choice");
  });

  it("asks a whole FORM one way, never variant-by-variant", () => {
    // $i^{6}$ is $-1$ (typeable) but $i^{7}$ is $-i$ (not). Deciding per
    // variant would type problem 3 and offer choices for problem 8 of the
    // same kind; one non-numeric variant drags the form to choices.
    const numericForm = {
      variants: [
        { options: ["$1$", "$2$", "$3$", "$4$"], correctIndex: 0 },
        { options: ["$5$", "$6$", "$7$", "$8$"], correctIndex: 1 },
      ],
    };
    expect(formAnswerMode(numericForm)).toBe("numeric");

    const mixedForm = {
      variants: [
        { options: ["$1$", "$-1$", "$2$", "$-2$"], correctIndex: 1 },
        { options: ["$1$", "$-1$", "$i$", "$-i$"], correctIndex: 3 },
      ],
    };
    expect(formAnswerMode(mixedForm)).toBe("choice");

    expect(formAnswerMode({ variants: [] })).toBe("choice");
  });
});

describe("option order", () => {
  const v = { id: "v01", options: ["a", "b", "c", "d"], correctIndex: 1 };

  it("is stable for a given variant, so SSR and the client agree", () => {
    // A Math.random shuffle here would hydrate differently than it rendered.
    expect(seededOptionOrder(v)).toEqual(seededOptionOrder(v));
  });

  it("keeps every option and still points at the right one", () => {
    const out = seededOptionOrder(v);
    expect([...out.options].sort()).toEqual(["a", "b", "c", "d"]);
    expect(out.options[out.correctIndex]).toBe("b");
  });

  it("varies between variants and between salts", () => {
    const orders = new Set(
      ["v01", "v02", "v03", "v04", "v05", "v06", "v07", "v08"].map((id) =>
        seededOptionOrder({ ...v, id }).options.join(""),
      ),
    );
    expect(orders.size).toBeGreaterThan(1);
    const a = seededOptionOrder(v, "1").options.join("");
    const b = seededOptionOrder(v, "2").options.join("");
    expect(a === b && a === seededOptionOrder(v, "3").options.join("")).toBe(false);
  });
});
