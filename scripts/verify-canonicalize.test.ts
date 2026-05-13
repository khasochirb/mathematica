// Migrated from the legacy scripts/verify-canonicalize.ts standalone runner.
// Exercises canonicalizeTopic + canonicalizeSubtopic with the same cases.
//
// Topic key set is asserted against lib/esh-questions.ts — adding a new
// canonical topic requires a new test here.

import { describe, it, expect } from "vitest";
import {
  canonicalizeTopic,
  canonicalizeSubtopic,
} from "@/lib/esh-questions";

describe("canonicalizeTopic", () => {
  it("returns canonical key when already canonical", () => {
    expect(canonicalizeTopic("algebra")).toBe("algebra");
  });
  it("lowercases mixed-case input", () => {
    expect(canonicalizeTopic("Algebra")).toBe("algebra");
    expect(canonicalizeTopic("ALGEBRA")).toBe("algebra");
  });
  it("trims surrounding whitespace", () => {
    expect(canonicalizeTopic("  algebra  ")).toBe("algebra");
  });

  // MN-cased aliases (added 2026-05-12 alias map)
  it("maps Алгебр → algebra", () => {
    expect(canonicalizeTopic("Алгебр")).toBe("algebra");
  });
  it("maps Геометр → geometry", () => {
    expect(canonicalizeTopic("Геометр")).toBe("geometry");
  });
  it("maps Анализ → calculus", () => {
    expect(canonicalizeTopic("Анализ")).toBe("calculus");
  });
  it("maps Статистик → statistics", () => {
    expect(canonicalizeTopic("Статистик")).toBe("statistics");
  });
  it("maps Магадлал → probability", () => {
    expect(canonicalizeTopic("Магадлал")).toBe("probability");
  });
  it("maps Тригонометр → trigonometry", () => {
    expect(canonicalizeTopic("Тригонометр")).toBe("trigonometry");
  });
  it("maps Функц → functions", () => {
    expect(canonicalizeTopic("Функц")).toBe("functions");
  });
  it("maps Дараалал → sequences", () => {
    expect(canonicalizeTopic("Дараалал")).toBe("sequences");
  });
  it("maps Комбинаторик → combinatorics", () => {
    expect(canonicalizeTopic("Комбинаторик")).toBe("combinatorics");
  });

  // New canonical topics (added 2026-05-12)
  it("recognises set_theory as canonical", () => {
    expect(canonicalizeTopic("set_theory")).toBe("set_theory");
  });
  it("recognises linear_algebra as canonical", () => {
    expect(canonicalizeTopic("linear_algebra")).toBe("linear_algebra");
  });
  it("recognises arithmetic as canonical", () => {
    expect(canonicalizeTopic("arithmetic")).toBe("arithmetic");
  });
  it("recognises complex_numbers as canonical", () => {
    expect(canonicalizeTopic("complex_numbers")).toBe("complex_numbers");
  });

  // English aliases
  it("maps 'matrices' → linear_algebra", () => {
    expect(canonicalizeTopic("matrices")).toBe("linear_algebra");
  });
  it("maps 'vectors' → linear_algebra", () => {
    expect(canonicalizeTopic("vectors")).toBe("linear_algebra");
  });
  it("maps 'sets' → set_theory", () => {
    expect(canonicalizeTopic("sets")).toBe("set_theory");
  });
  it("maps 'complex numbers' → complex_numbers", () => {
    expect(canonicalizeTopic("complex numbers")).toBe("complex_numbers");
  });
  it("maps 'polynomials' → algebra", () => {
    expect(canonicalizeTopic("polynomials")).toBe("algebra");
  });
  it("maps 'sequences and series' → sequences", () => {
    expect(canonicalizeTopic("sequences and series")).toBe("sequences");
  });
  it("maps 'coordinate geometry' → geometry", () => {
    expect(canonicalizeTopic("Coordinate Geometry")).toBe("geometry");
  });

  // MN cased + alias
  it("maps Вектор → linear_algebra", () => {
    expect(canonicalizeTopic("Вектор")).toBe("linear_algebra");
  });
  it("maps Матриц → linear_algebra", () => {
    expect(canonicalizeTopic("Матриц")).toBe("linear_algebra");
  });
  it("maps Олонлог → set_theory", () => {
    expect(canonicalizeTopic("Олонлог")).toBe("set_theory");
  });

  // Fallback behaviour
  it("falls back to 'other' for unknown strings", () => {
    expect(canonicalizeTopic("nonsense_topic")).toBe("other");
  });
  it("falls back to 'other' for empty / null / undefined", () => {
    expect(canonicalizeTopic("")).toBe("other");
    expect(canonicalizeTopic(null)).toBe("other");
    expect(canonicalizeTopic(undefined)).toBe("other");
  });
});

describe("canonicalizeSubtopic", () => {
  it("lowercases Cyrillic", () => {
    expect(canonicalizeSubtopic("Вектор")).toBe("вектор");
  });
  it("preserves already-lowercase Cyrillic", () => {
    expect(canonicalizeSubtopic("вектор")).toBe("вектор");
  });
  it("collapses internal whitespace", () => {
    expect(canonicalizeSubtopic("  Standard  Form  ")).toBe("standard form");
  });
  it("preserves snake_case identifiers verbatim", () => {
    expect(canonicalizeSubtopic("polynomial_factoring")).toBe(
      "polynomial_factoring",
    );
  });
  it("lowercases multi-word Cyrillic", () => {
    expect(canonicalizeSubtopic("Логарифм тэгшитгэл")).toBe(
      "логарифм тэгшитгэл",
    );
  });
  it("returns null for empty / whitespace / null / undefined", () => {
    expect(canonicalizeSubtopic("")).toBeNull();
    expect(canonicalizeSubtopic("   ")).toBeNull();
    expect(canonicalizeSubtopic(null)).toBeNull();
    expect(canonicalizeSubtopic(undefined)).toBeNull();
  });
});
