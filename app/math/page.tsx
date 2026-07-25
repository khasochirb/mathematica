"use client";

import Link from "next/link";
import { listGrades, getGrade6Topics, getGrade7Spine, getGrade8Spine, getGrade9Spine, getGrade10Spine, getGrade11Spine, getGrade12Spine } from "@/lib/genmath-lessons";
import useRatings from "@/lib/use-ratings";
import {
  COURSE_DEFAULT_ATTRIBUTE,
  attributeInfo,
  recommendedCourse,
  type Band,
} from "@/lib/ratings";
import RecommendedNextCard from "@/components/ratings/RecommendedNextCard";
import { useLang } from "@/lib/lang-context";

const BAND_COLOR: Record<Band, string> = {
  beginner: "var(--danger)",
  developing: "var(--warn)",
  strong: "var(--accent)",
  mastery: "var(--accent)",
};

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
  // Announced but not yet authored. Renders as a dimmed, non-clickable card
  // so the program's shape is visible without promising a dead link.
  upcoming?: boolean;
}[] = [
  {
    href: "/math/integrated-1",
    title: "Integrated Math 1",
    blurb:
      "Linear equations and functions, systems, exponential growth, transformations and congruence, coordinate geometry, and one-variable statistics — algebra and geometry together, not in sequence.",
    units: 7,
    level: 1,
    exams: ["SAT"],
    upcoming: true,
  },
  {
    href: "/math/integrated-2",
    title: "Integrated Math 2",
    blurb:
      "Quadratics end to end, similarity and right-triangle trigonometry, circles, probability, and formal proof — the middle year of the integrated pathway.",
    units: 7,
    level: 2,
    exams: ["SAT"],
    upcoming: true,
  },
  {
    href: "/math/integrated-3",
    title: "Integrated Math 3",
    blurb:
      "Polynomials, rational and radical functions, logarithms, trigonometric functions, and statistical inference — the year that opens Precalculus.",
    units: 7,
    level: 3,
    exams: ["SAT"],
    upcoming: true,
  },
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
    href: "/math/trigonometry",
    title: "Trigonometry",
    blurb:
      "Right-triangle ratios, the special triangles, the unit circle and its waves, identities — and the laws that solve any triangle. A diagram at nearly every step.",
    units: 6,
    level: 2,
    exams: ["ЭЕШ", "SAT", "IB"],
    isNew: true,
  },
  {
    href: "/math/solid-geometry",
    title: "Solid Geometry",
    blurb:
      "Geometry 2, off the page: lines and planes in space, prisms to spheres, cross-sections, and the k-k²-k³ scaling law — every 3D problem reduced to a flat triangle you can see.",
    units: 6,
    level: 2,
    exams: ["ЭЕШ", "SAT", "IB"],
    isNew: true,
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
  {
    href: "/math/calculus",
    title: "Calculus",
    blurb:
      "The mathematics of change: limits, derivatives and optimization, integrals and the Fundamental Theorem — the ladder's capstone.",
    units: 6,
    level: 3,
    exams: ["ЭЕШ", "IB"],
    isNew: true,
  },
];

// ── Programs ──────────────────────────────────────────────────────────
// A student arrives knowing which PROGRAM they are in, not which course
// slug they need. Grouping the catalog by program is what turns "hunt
// through eleven cards" into "open my track". IB, SAT and ЭЕШ are
// deliberately absent — each has its own hub, and duplicating them here
// would give two answers to the same question.
//
// `courses` lists hrefs into COURSES; `grades` lists grade numbers. A
// course may appear in more than one program (a Geometry student can be
// on either pathway) — these are routes through the catalog, not owners
// of it.
const PROGRAMS: {
  id: string;
  title: string;
  blurb: string;
  courses?: string[];
  grades?: number[];
}[] = [
  {
    id: "integrated",
    title: "Integrated Math",
    blurb:
      "The integrated pathway — each year mixes algebra, geometry and statistics rather than teaching them one at a time. IM1 → IM2 → IM3, then Precalculus.",
    courses: ["/math/integrated-1", "/math/integrated-2", "/math/integrated-3"],
  },
  {
    id: "traditional",
    title: "Traditional pathway",
    blurb:
      "The classic three-course sequence — one subject at a time, Algebra 1 → Geometry → Algebra 2. The other way through the same material.",
    courses: ["/math/algebra-1", "/math/geometry", "/math/algebra-2"],
  },
  {
    id: "advanced",
    title: "Advanced & specialist",
    blurb:
      "What comes after either pathway, plus the specialist tracks. Start these once you have finished IM3 or Algebra 2.",
    courses: [
      "/math/trigonometry",
      "/math/precalculus",
      "/math/prob-stats",
      "/math/solid-geometry",
      "/math/vectors-matrices",
      "/math/calculus",
    ],
  },
  {
    id: "mn-middle",
    title: "Mongolian curriculum · Middle School",
    blurb: "Grades 6–9, following the Mongolian school curriculum year by year.",
    grades: [6, 7, 8, 9],
  },
  {
    id: "mn-high",
    title: "Mongolian curriculum · High School",
    blurb: "Grades 10–12, following the Mongolian school curriculum year by year.",
    grades: [10, 11, 12],
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

const gridStyle = { gridTemplateColumns: "repeat(auto-fill, minmax(280px, 1fr))" };

export default function MathLandingPage() {
  const grades = listGrades();
  const { profile } = useRatings();
  const { lang } = useLang();
  const rec = recommendedCourse(profile);
  // The student's attribute rating behind each course card ("your rating on
  // this course's domain") — only for RATED attributes; unrated shows nothing.
  const courseChip = (href: string) => {
    if (!profile.hasAnyEvidence) return null;
    const attrKey = COURSE_DEFAULT_ATTRIBUTE[`course:${href.slice("/math/".length)}`];
    if (!attrKey) return null;
    const a = profile.attributes.find((x) => x.key === attrKey)!;
    if (!a.rated) return null;
    return { info: attributeInfo(attrKey), score: a.score, band: a.band, provisional: a.provisional };
  };

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 pb-16">
        {/* Header */}
        <div className="eyebrow mb-4">Courses</div>
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
          Courses
        </h1>
        <p
          className="mt-4 mb-10"
          style={{ color: "var(--fg-1)", fontSize: 17, maxWidth: "56ch" }}
        >
          Find your <strong>program</strong> below — Integrated Math, the
          traditional pathway, or the Mongolian school curriculum — and every
          course in it is together in one place. Preparing for ЭЕШ, SAT or IB?
          Those have their own hubs.
        </p>

        {/* Pinned course recommendation from the ratings profile — the same
            owner's-voice card as the dashboard, so "where do I start?" is
            answered before the catalog. */}
        {rec && (
          <div className="mb-6">
            <RecommendedNextCard rec={rec} />
          </div>
        )}

        {/* Problem Bank — leveled drilling with miss→similar remediation */}
        <Link
          href="/math/problem-bank"
          className="card-edit p-5 mb-10 flex items-center gap-4 transition-colors"
          style={{ textDecoration: "none", borderColor: "var(--accent-line)", background: "var(--accent-wash)" }}
        >
          <div className="flex-1 min-w-0">
            <span className="mono text-[10px] uppercase" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
              Practice
            </span>
            <span className="serif block mt-1" style={{ fontWeight: 400, fontSize: 20, letterSpacing: "-0.01em", color: "var(--fg)" }}>
              Problem Bank
            </span>
            <span className="block mt-1 text-[13px]" style={{ color: "var(--fg-1)" }}>
              A problem collection for every course unit, labeled Level 1–3.
              Miss one and a similar problem comes right back until it sticks.
            </span>
          </div>
          <span className="mono text-[10px] uppercase flex-shrink-0" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
            Open
          </span>
        </Link>

        {/* One section per program. `#topics` stays on the first course
            section so the exam hubs' existing deep links still land on the
            catalog rather than the page top. */}
        {PROGRAMS.map((program, programIndex) => {
          const programCourses = (program.courses ?? [])
            .map((href) => COURSES.find((c) => c.href === href))
            .filter((c): c is (typeof COURSES)[number] => Boolean(c));

          return (
            <section
              key={program.id}
              id={programIndex === 0 ? "topics" : program.id}
              className="mb-12"
              style={{ scrollMarginTop: 96 }}
            >
              <div className="eyebrow mb-1.5">{program.title}</div>
              <p className="text-[13px] mb-4" style={{ color: "var(--fg-2)", maxWidth: "62ch" }}>
                {program.blurb}
              </p>

              <div className="grid gap-4" style={gridStyle}>
                {programCourses.map((c) =>
                  c.upcoming ? (
                    <div
                      key={c.href}
                      className="card-edit p-6 flex flex-col gap-2"
                      style={{ opacity: 0.45, cursor: "default" }}
                    >
                      <span className="flex flex-col gap-1.5">
                        <span
                          className="mono text-[10px] uppercase"
                          style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}
                        >
                          In development · {c.units} units
                        </span>
                        <span className="flex flex-wrap gap-1.5 items-center">
                          {c.exams.map((x) => (
                            <span
                              key={x}
                              className="mono rounded-full px-2 py-0.5 text-[10px] uppercase"
                              style={{
                                background: "var(--bg-2)",
                                border: "1px solid var(--line)",
                                color: "var(--fg-3)",
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
                        style={{ fontSize: 24, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)", lineHeight: 1.15 }}
                      >
                        {c.title}
                      </span>
                      <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
                        {c.blurb}
                      </span>
                    </div>
                  ) : (
                    <Link
                      key={c.href}
                      href={c.href}
                      className="card-edit p-6 flex flex-col gap-2 transition-colors"
                      style={{ textDecoration: "none" }}
                      {...cardHover}
                    >
                      {/* Two fixed lines — level on one, chips on the next — so every
                          card's header is the same height and the titles line up
                          across a row regardless of how many exam tags a course has. */}
                      <span className="flex flex-col gap-1.5">
                        <span
                          className="mono text-[10px] uppercase"
                          style={{ color: "var(--accent)", letterSpacing: "0.08em" }}
                        >
                          {c.isNew ? "New · " : ""}Level {c.level} · {c.units} units
                        </span>
                        <span className="flex flex-wrap gap-1.5 items-center">
                          {(() => {
                            const chip = courseChip(c.href);
                            if (!chip) return null;
                            return (
                              <span
                                className="mono tabular rounded-full px-2 py-0.5 text-[10px]"
                                title={lang === "mn" ? chip.info.mn : chip.info.en}
                                style={{
                                  background: "var(--bg-2)",
                                  border: "1px solid var(--line)",
                                  color: BAND_COLOR[chip.band],
                                  letterSpacing: "0.04em",
                                }}
                              >
                                {lang === "mn" ? "Таны үнэлгээ" : "You"} {chip.score}
                                {chip.provisional ? "*" : ""}
                              </span>
                            );
                          })()}
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
                        style={{ fontSize: 24, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)", lineHeight: 1.15 }}
                      >
                        {c.title}
                      </span>
                      <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
                        {c.blurb}
                      </span>
                    </Link>
                  ),
                )}

                {(program.grades ?? []).map((grade) => {
                  const active = grades.find((g) => g.grade === grade)?.active ?? false;
                  return active ? (
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
                  );
                })}
              </div>
            </section>
          );
        })}
      </div>
    </div>
  );
}
