"use client";

import Link from "next/link";
// Spines, not the registry: the catalog lists courses, it renders no
// lesson, so it must not ship the course corpus (lib/genmath-spines.ts).
import { listGrades, GRADE2_SPINE, GRADE3_SPINE, GRADE4_SPINE, GRADE6_SPINE, GRADE7_SPINE, GRADE8_SPINE, GRADE9_SPINE, GRADE10_SPINE, GRADE11_SPINE, GRADE12_SPINE } from "@/lib/genmath-spines";
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
  // Primary grades go live topic by topic — count only what a student can open.
  3: GRADE2_SPINE.filter((t) => t.live).length,
  4: GRADE3_SPINE.filter((t) => t.live).length,
  5: GRADE4_SPINE.filter((t) => t.live).length,
  6: GRADE6_SPINE.length,
  7: GRADE7_SPINE.length,
  8: GRADE8_SPINE.length,
  9: GRADE9_SPINE.length,
  10: GRADE10_SPINE.length,
  11: GRADE11_SPINE.length,
  12: GRADE12_SPINE.length,
};

// Transition grades (owner's structure diagram, 2026-07-31): the final grade
// of each school band, when families switch schools and prep for competitive
// entrance tests. 12th is served by the ЭЕШ hub; the badge makes the moment
// visible on the catalog.
const TRANSITION: Record<number, string> = {
  5: "Transition year — school entrance",
  9: "Transition year — high-school entrance",
  12: "Transition year — ЭЕШ",
};

type CourseCardDef = {
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
};

// The topic ladder, easiest first. One course serves every exam — instead of
// per-exam duplicates ("Algebra ЭЕШ level"), each card carries a level (1–3)
// and chips for the exams it prepares. This is the shared "Study by topic"
// destination the ЭЕШ/SAT/IB hubs link to (/math#topics); per the resource
// blueprint these named topic courses LIVE inside the High school band.
const TOPIC_COURSES: CourseCardDef[] = [
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

// The IM pathway sits BESIDE the school bands (blueprint): a different route
// through the same mathematics, each year mixing algebra, geometry and
// statistics. Each IM course conforms to the full schema — bank + course +
// exams (IM3 is still in development).
const IM_COURSES: CourseCardDef[] = [
  {
    href: "/math/integrated-1",
    title: "Integrated Math 1",
    blurb:
      "Linear equations and functions, systems, exponential growth, transformations and congruence, coordinate geometry, and one-variable statistics — algebra and geometry together, not in sequence.",
    units: 9,
    level: 1,
    exams: ["SAT"],
  },
  {
    href: "/math/integrated-2",
    title: "Integrated Math 2",
    blurb:
      "Quadratics end to end — including the complex numbers a negative discriminant forces — plus rational exponents, similarity and right-triangle trigonometry, circles, and probability.",
    units: 8,
    level: 2,
    exams: ["SAT"],
  },
  {
    href: "/math/integrated-3",
    title: "Integrated Math 3",
    blurb:
      "Polynomials, rational and radical functions, logarithms, trigonometric functions, and statistical inference — the year that opens Precalculus. First three units live; the rest land in order.",
    units: 8,
    level: 3,
    exams: ["SAT"],
    isNew: true,
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

function TransitionChip({ grade }: { grade: number }) {
  const label = TRANSITION[grade];
  if (!label) return null;
  return (
    <span
      className="mono rounded-full px-2 py-0.5 text-[10px] uppercase"
      title={label}
      style={{
        background: "rgba(216,150,32,0.10)",
        border: "1px solid rgba(216,150,32,0.4)",
        color: "var(--warn, #d89620)",
        letterSpacing: "0.06em",
      }}
    >
      {grade === 12 ? "ЭЕШ year" : "Entrance year"}
    </span>
  );
}

// The band's ENTRY test (resource blueprint: placement at the top of each
// band, exit exams at the bottom).
function BandPlacementCard({ href, body }: { href: string; body: string }) {
  return (
    <Link
      href={href}
      className="card-edit p-4 mb-4 flex items-center gap-3 transition-colors"
      style={{ textDecoration: "none" }}
      {...cardHover}
    >
      <span className="mono text-[10px] uppercase flex-shrink-0" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
        Placement
      </span>
      <span className="flex-1 text-[13px]" style={{ color: "var(--fg-1)" }}>{body}</span>
      <span className="mono text-[10px] uppercase flex-shrink-0" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
        Start
      </span>
    </Link>
  );
}

// The band's EXIT exams, at the band's final grade.
function BandExamCard({ href, body }: { href: string; body: string }) {
  return (
    <Link
      href={href}
      className="card-edit p-4 mt-4 flex items-center gap-3 transition-colors"
      style={{ textDecoration: "none" }}
      {...cardHover}
    >
      <span className="mono text-[10px] uppercase flex-shrink-0" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
        Band exam
      </span>
      <span className="flex-1 text-[13px]" style={{ color: "var(--fg-1)" }}>{body}</span>
      <span className="mono text-[10px] uppercase flex-shrink-0" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
        Open
      </span>
    </Link>
  );
}

function GradeCard({ grade, active }: { grade: number; active: boolean }) {
  if (!active) {
    return (
      <div className="card-edit p-6 flex flex-col gap-2" style={{ opacity: 0.45, cursor: "default" }}>
        <span className="mono text-[10px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
          Coming soon
        </span>
        <span className="serif" style={{ fontSize: 32, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)" }}>
          Grade {grade}
        </span>
      </div>
    );
  }
  return (
    <Link
      href={`/math/${grade}`}
      className="card-edit p-6 flex flex-col gap-2 transition-colors"
      style={{ textDecoration: "none" }}
      {...cardHover}
    >
      <span className="flex items-center gap-1.5 flex-wrap">
        <span className="mono text-[10px] uppercase" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
          Active
        </span>
        <TransitionChip grade={grade} />
      </span>
      <span className="serif" style={{ fontSize: 32, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)" }}>
        Grade {grade}
      </span>
      <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
        {TOPIC_COUNTS[grade] ?? 0} topics
      </span>
    </Link>
  );
}

export default function MathLandingPage() {
  const grades = listGrades();
  const { profile } = useRatings();
  const { lang } = useLang();
  const rec = recommendedCourse(profile);
  const isActive = (grade: number) => grades.find((g) => g.grade === grade)?.active ?? false;
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

  const renderCourseCard = (c: CourseCardDef) =>
    c.upcoming ? (
      <div key={c.href} className="card-edit p-6 flex flex-col gap-2" style={{ opacity: 0.45, cursor: "default" }}>
        <span className="flex flex-col gap-1.5">
          <span className="mono text-[10px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
            In development · {c.units} units
          </span>
          <span className="flex flex-wrap gap-1.5 items-center">
            {c.exams.map((x) => (
              <span
                key={x}
                className="mono rounded-full px-2 py-0.5 text-[10px] uppercase"
                style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-3)", letterSpacing: "0.06em" }}
              >
                {x}
              </span>
            ))}
          </span>
        </span>
        <span className="serif" style={{ fontSize: 24, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)", lineHeight: 1.15 }}>
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
          <span className="mono text-[10px] uppercase" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
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
                style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)", letterSpacing: "0.06em" }}
              >
                {x}
              </span>
            ))}
          </span>
        </span>
        <span className="serif" style={{ fontSize: 24, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)", lineHeight: 1.15 }}>
          {c.title}
        </span>
        <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
          {c.blurb}
        </span>
      </Link>
    );

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
        <p className="mt-4 mb-10" style={{ color: "var(--fg-1)", fontSize: 17, maxWidth: "56ch" }}>
          Find your <strong>school band</strong> below — Primary, Mid school or
          High school on the Mongol curriculum — or take the Integrated Math
          pathway beside them. Preparing for ЭЕШ, SAT or IB? Those have their
          own hubs.
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

        {/* ── The school bands (Mongol curriculum) ─────────────────────────
            Blueprint: General Math is organized by school band, not a flat
            course list. Primary is a visible coming-soon band; Mid school is
            grades 6–9; High school is grades 10–12 PLUS the named topic
            courses. Transition grades (5th/9th/12th) carry a badge. */}

        <section id="primary" className="mb-12" style={{ scrollMarginTop: 96 }}>
          <div className="eyebrow mb-1.5">Primary school · Mongol curriculum</div>
          <p className="text-[13px] mb-4" style={{ color: "var(--fg-2)", maxWidth: "62ch" }}>
            Grades 1–5, year by year, on the ministry's own grade labels
            (renumbered 2026-08 to match the national core curriculum).
            Grades 2, 3 and 4 are complete and open; grades 1 and 5 are
            being authored against the same standard and follow next.
          </p>
          <div className="grid gap-4" style={gridStyle}>
            <GradeCard grade={5} active={isActive(5)} />
            <GradeCard grade={4} active={isActive(4)} />
            <GradeCard grade={3} active={isActive(3)} />
            <GradeCard grade={2} active={isActive(2)} />
            <GradeCard grade={1} active={isActive(1)} />
          </div>
        </section>

        <section id="mid-school" className="mb-12" style={{ scrollMarginTop: 96 }}>
          <div className="eyebrow mb-1.5">Mid school · Mongol curriculum</div>
          <p className="text-[13px] mb-4" style={{ color: "var(--fg-2)", maxWidth: "62ch" }}>
            Grades 6–9, following the school curriculum year by year. Grade 9
            is the transition year — the springboard to high-school entrance
            exams.
          </p>
          <BandPlacementCard
            href="/math/placement/mid"
            body="Not sure which grade to start in? A short adaptive test samples every grade 6–9 and names your starting grade."
          />
          <div className="grid gap-4" style={gridStyle}>
            {[6, 7, 8, 9].map((g) => (
              <GradeCard key={g} grade={g} active={isActive(g)} />
            ))}
          </div>
          <BandExamCard
            href="/math/9/exam"
            body="Finish the band with a full Grade 9 exam — three papers, every topic represented, a per-topic breakdown of where you stand."
          />
        </section>

        <section id="high-school" className="mb-12" style={{ scrollMarginTop: 96 }}>
          <div className="eyebrow mb-1.5">High school · Mongol curriculum</div>
          <p className="text-[13px] mb-4" style={{ color: "var(--fg-2)", maxWidth: "62ch" }}>
            Grades 10–12 year by year — and the full topic courses that live in
            this band. Grade 12 is the ЭЕШ year; the ЭЕШ hub has the exam prep.
          </p>
          <BandPlacementCard
            href="/math/placement/high"
            body="Not sure which grade to start in? A short adaptive test samples every grade 10–12 and names your starting grade."
          />
          <div className="grid gap-4" style={gridStyle}>
            {[10, 11, 12].map((g) => (
              <GradeCard key={g} grade={g} active={isActive(g)} />
            ))}
          </div>
          <BandExamCard
            href="/math/12/exam"
            body="Finish the band with a full Grade 12 exam — three papers, every topic represented, the same map ЭЕШ prep starts from."
          />

          {/* `#topics` stays on the topic-course catalog so the exam hubs'
              existing deep links still land here rather than the page top. */}
          <div id="topics" className="mt-8" style={{ scrollMarginTop: 96 }}>
            <div className="eyebrow mb-1.5">Topic courses</div>
            <p className="text-[13px] mb-4" style={{ color: "var(--fg-2)", maxWidth: "62ch" }}>
              The high-school material taught subject by subject, from zero —
              take them in the classic order (Algebra 1 → Geometry → Algebra 2)
              or jump straight to the topic you need. Each card shows the exams
              it prepares.
            </p>
            <div className="grid gap-4" style={gridStyle}>
              {TOPIC_COURSES.map(renderCourseCard)}
            </div>
          </div>
        </section>

        <section id="integrated" className="mb-12" style={{ scrollMarginTop: 96 }}>
          <div className="eyebrow mb-1.5">Integrated Math pathway</div>
          <p className="text-[13px] mb-4" style={{ color: "var(--fg-2)", maxWidth: "62ch" }}>
            The pathway beside the bands — each year mixes algebra, geometry
            and statistics rather than teaching them one at a time. IM1 → IM2
            → IM3, then Precalculus.
          </p>
          <div className="grid gap-4" style={gridStyle}>
            {IM_COURSES.map(renderCourseCard)}
          </div>
        </section>
      </div>
    </div>
  );
}
