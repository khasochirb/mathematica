"use client";

import Link from "next/link";
import { listGrades, getGrade6Topics, getGrade7Spine, getGrade8Spine, getGrade9Spine, getGrade10Spine, getGrade11Spine, getGrade12Spine } from "@/lib/genmath-lessons";

const TOPIC_COUNTS: Record<number, number> = {
  6: getGrade6Topics().length,
  7: getGrade7Spine().length,
  8: getGrade8Spine().length,
  9: getGrade9Spine().length,
  10: getGrade10Spine().length,
  11: getGrade11Spine().length,
  12: getGrade12Spine().length,
};

// The topic ladder, easiest first. One course serves every exam — instead of
// per-exam duplicates ("Algebra ЭЕШ level"), each card carries a level (1–3)
// and chips for the exams it prepares. This section is the shared "Study by
// topic" destination the ЭЕШ/SAT/IB hubs link to (/math#topics).
const COURSES: {
  href: string;
  title: string;
  blurb: string;
  units: number;
  level: 1 | 2 | 3;
  exams: string[];
  isNew?: boolean;
}[] = [
  {
    href: "/math/algebra-1",
    title: "Algebra 1",
    blurb:
      "Expressions, equations, inequalities, functions, lines, systems, factoring, and quadratics — the whole first course.",
    units: 8,
    level: 1,
    exams: ["ЭЕШ", "SAT"],
  },
  {
    href: "/math/geometry",
    title: "Geometry",
    blurb:
      "From points and lines to proof, circles, and trigonometry — taught from zero, one continuous track.",
    units: 13,
    level: 2,
    exams: ["ЭЕШ", "SAT"],
  },
  {
    href: "/math/algebra-2",
    title: "Algebra 2",
    blurb:
      "Transformations, complex numbers, polynomials, radicals, exponentials and logs, rationals, and sequences — the bridge to precalculus.",
    units: 8,
    level: 2,
    exams: ["ЭЕШ", "SAT", "IB"],
    isNew: true,
  },
  {
    href: "/math/prob-stats",
    title: "Combinatorics, Probability & Statistics",
    blurb:
      "Count first, then measure chance, then read data honestly — one continuous track in three acts.",
    units: 12,
    level: 2,
    exams: ["ЭЕШ", "SAT", "IB"],
  },
  {
    href: "/math/precalculus",
    title: "Precalculus",
    blurb:
      "The bridge to calculus, graph-first: transformations, polynomials, rationals, exponentials and logs, the unit circle, trig waves, and conics.",
    units: 8,
    level: 3,
    exams: ["ЭЕШ", "IB"],
  },
  {
    href: "/math/vectors-matrices",
    title: "Vectors & Matrices",
    blurb:
      "Arrows made of numbers, then the grids that move them — components, dot products, space, determinants, inverses.",
    units: 6,
    level: 3,
    exams: ["ЭЕШ", "IB"],
  },
];

const cardHover = {
  onMouseEnter: (e: React.MouseEvent<HTMLAnchorElement>) => {
    e.currentTarget.style.borderColor = "var(--accent-line)";
    e.currentTarget.style.background = "var(--accent-wash)";
  },
  onMouseLeave: (e: React.MouseEvent<HTMLAnchorElement>) => {
    e.currentTarget.style.borderColor = "";
    e.currentTarget.style.background = "";
  },
};

export default function MathLandingPage() {
  const grades = listGrades();

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 pb-16">
        {/* Header */}
        <div className="eyebrow mb-4">General Math</div>
        <h1
          className="serif"
          style={{
            fontWeight: 400,
            fontSize: "clamp(36px, 5vw, 64px)",
            letterSpacing: "-0.04em",
            lineHeight: 1,
            color: "var(--fg)",
          }}
        >
          General Math
        </h1>
        <p
          className="mt-4 mb-10"
          style={{ color: "var(--fg-1)", fontSize: 17, maxWidth: "56ch" }}
        >
          Two ways in: study a <strong>math topic</strong> as one continuous course
          (the same courses that prepare you for ЭЕШ, SAT, and IB), or follow your{" "}
          <strong>school grade</strong> from Grade 6 through 12.
        </p>

        {/* Study by topic — shared destination for the exam hubs (/math#topics) */}
        <section id="topics" style={{ scrollMarginTop: 96 }}>
          <div className="eyebrow mb-1.5">Study by topic</div>
          <p className="text-[13px] mb-4" style={{ color: "var(--fg-2)" }}>
            Full courses, easiest first. Level 1 → 3; the tags show which exams each
            course prepares you for.
          </p>
          <div className="mb-12 space-y-3">
            {COURSES.map((c) => (
              <Link
                key={c.href}
                href={c.href}
                className="card-edit p-6 flex flex-col gap-2 transition-colors"
                style={{ textDecoration: "none" }}
                {...cardHover}
              >
                <span className="flex flex-wrap items-center gap-2">
                  <span
                    className="mono text-[10px] uppercase"
                    style={{ color: "var(--accent)", letterSpacing: "0.08em" }}
                  >
                    {c.isNew ? "New · " : ""}Level {c.level} · {c.units} units
                  </span>
                  <span className="ml-auto flex gap-1.5">
                    {c.exams.map((x) => (
                      <span
                        key={x}
                        className="mono rounded-full px-2 py-0.5 text-[10px] uppercase"
                        style={{
                          background: "var(--bg-2)",
                          border: "1px solid var(--line)",
                          color: "var(--fg-2)",
                          letterSpacing: "0.06em",
                        }}
                      >
                        {x}
                      </span>
                    ))}
                  </span>
                </span>
                <span
                  className="serif"
                  style={{ fontSize: 32, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)" }}
                >
                  {c.title}
                </span>
                <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
                  {c.blurb}
                </span>
              </Link>
            ))}
          </div>
        </section>

        {/* Study by grade */}
        <section id="grades" style={{ scrollMarginTop: 96 }}>
          <div className="eyebrow mb-1.5">Study by grade</div>
          <p className="text-[13px] mb-4" style={{ color: "var(--fg-2)" }}>
            The school curriculum, grade by grade.
          </p>
          <div
            className="grid gap-4"
            style={{ gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))" }}
          >
            {grades.map(({ grade, active }) =>
              active ? (
                <Link
                  key={grade}
                  href={`/math/${grade}`}
                  className="card-edit p-6 flex flex-col gap-2 transition-colors"
                  style={{ textDecoration: "none" }}
                  {...cardHover}
                >
                  <span
                    className="mono text-[10px] uppercase"
                    style={{ color: "var(--accent)", letterSpacing: "0.08em" }}
                  >
                    Active
                  </span>
                  <span
                    className="serif"
                    style={{ fontSize: 32, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)" }}
                  >
                    Grade {grade}
                  </span>
                  <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
                    {TOPIC_COUNTS[grade] ?? 0} topics
                  </span>
                </Link>
              ) : (
                <div
                  key={grade}
                  className="card-edit p-6 flex flex-col gap-2"
                  style={{ opacity: 0.45, cursor: "default" }}
                >
                  <span
                    className="mono text-[10px] uppercase"
                    style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}
                  >
                    Coming soon
                  </span>
                  <span
                    className="serif"
                    style={{ fontSize: 32, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)" }}
                  >
                    Grade {grade}
                  </span>
                </div>
              ),
            )}
          </div>
        </section>
      </div>
    </div>
  );
}
