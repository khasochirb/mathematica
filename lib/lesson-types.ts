// Hub-agnostic lesson rendering types. Shared by the ЭЕШ hub (question-bank-backed)
// and the General Math hub (authored-inline). Components in components/lesson/ render
// these shapes; each hub maps its own data into them. This is the seam that lets both
// hubs reuse one lesson system without one depending on the other.

export interface FigureData {
  src: string;
  alt_mn: string;
  alt_en: string;
  width: number;
  height: number;
}

export interface LessonProblemBadge {
  text: string;
  mono?: boolean;
}

// A worked example or practice/test problem, normalized across hubs.
export interface LessonProblem {
  id: string; // unique key: ЭЕШ question source, or an authored id
  statement: string; // problem body (MathText: $...$, $$...$$, **bold**)
  solution: string; // worked solution (MathText)
  note?: string; // optional teaching note shown before the solution
  badges?: LessonProblemBadge[]; // e.g. difficulty / skill-tag chips
  figure?: FigureData;
  // Sympy-verifiable boolean expressions. Each must evaluate True. Required for
  // every authored (General Math) problem — enforced by scripts/verify-genmath.py.
  // Not used by ЭЕШ (bank-backed) problems.
  check?: string[];
}

export interface LessonFact {
  title: string;
  latex: string;
  explanation: string;
}

export interface LessonMistake {
  text: string;
  correction?: string;
  authored: boolean; // false => scaffold, hidden in production
}
