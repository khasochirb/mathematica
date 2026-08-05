// Hub-agnostic lesson rendering types. Shared by the ЭЕШ hub (question-bank-backed)
// and the Courses hub (authored-inline). Components in components/lesson/ render
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
  // A declarative geometry diagram (points/segments/angle arcs) rendered by
  // GeoDiagram — the genmath course system, distinct from the image-based
  // `figure` above. Used by figure-heavy course banks (Trigonometry).
  geoFigure?: import("@/lib/genmath-interactive").GeoDiagramSpec;
  // A declarative genmath figure (groups / fraction bar / number line / geo)
  // rendered by RatioFigure — the same spec the interactive player draws.
  //
  // Deliberately NOT `figure` above: that field is the ЭЕШ hub's IMAGE
  // (src/width/height), and a genmath spec put there renders as a broken
  // <img>. The primary-band builders wrote practice-bank figures into it for
  // months and every one was invisible, which left statements like "the
  // picture shows the bundles" unanswerable. Own field, own renderer.
  courseFigure?: import("@/lib/genmath-interactive").FigureSpec;
  // Sympy-verifiable boolean expressions. Each must evaluate True. Required for
  // every authored (Courses) problem — enforced by scripts/verify-genmath.py.
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
