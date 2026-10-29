"use client";

import { isUnpublished, publishedOnly } from "@/lib/unpublished";
import Link from "next/link";
// Spines, not the registry: the catalog lists courses, it renders no
// lesson, so it must not ship the course corpus (lib/genmath-spines.ts).
import { listGrades, GRADE6_SPINE, GRADE7_SPINE, GRADE8_SPINE, GRADE9_SPINE, GRADE10_SPINE, GRADE11_SPINE, GRADE12_SPINE } from "@/lib/genmath-spines";
import useRatings from "@/lib/use-ratings";
import {
  COURSE_DEFAULT_ATTRIBUTE,
  attributeInfo,
  recommendedCourse,
  type Band,
} from "@/lib/ratings";
import RecommendedNextCard from "@/components/ratings/RecommendedNextCard";
import { HubShell, HubHeader } from "@/components/hub/HubKit";
import { useLang } from "@/lib/lang-context";

const BAND_COLOR: Record<Band, string> = {
  beginner: "var(--danger)",
  developing: "var(--warn)",
  strong: "var(--accent)",
  mastery: "var(--accent)",
};

const TOPIC_COUNTS: Record<number, number> = {
  // Grades 1-5 are absent because the primary band is withdrawn from the site
  // (see lib/genmath-spines.ts). Restoring the band restores their rows here,
  // counting only `live` topics as the primary spines did.
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
// entrance tests. 12th is served by the ЭШ hub; the badge makes the moment
// visible on the catalog.
const TRANSITION: Record<number, string> = {
  5: "Transition year — school entrance",
  9: "Transition year — high-school entrance",
  12: "Transition year — ЭШ",
};
const TRANSITION_MN: Record<number, string> = {
  5: "Шилжилтийн жил: сургуульд элсэх",
  9: "Шилжилтийн жил: ахлах ангид элсэх",
  12: "Шилжилтийн жил: ЭШ",
};

type CourseCardDef = {
  href: string;
  title: string;
  // Mongolian title: exactly the established course name
  // (data/problembank-mn/<slug>.json "title").
  titleMn: string;
  blurb: string;
  blurbMn: string;
  units: number;
  level: 1 | 2 | 3;
  exams: string[];
  isNew?: boolean;
  // Announced but not yet authored. Renders as a dimmed, non-clickable card
  // so the program's shape is visible without promising a dead link.
  upcoming?: boolean;
};

// The topic ladder, easiest first. One course serves every exam — instead of
// per-exam duplicates ("Algebra ЭШ level"), each card carries a level (1–3)
// and chips for the exams it prepares. This is the shared "Study by topic"
// destination the ЭШ/SAT/IB hubs link to (/math#topics); per the resource
// blueprint these named topic courses LIVE inside the High school band.
const TOPIC_COURSES: CourseCardDef[] = [
  {
    href: "/math/algebra-1",
    title: "Algebra 1",
    titleMn: "Алгебр 1",
    blurb:
      "Expressions, equations, inequalities, functions, lines, systems, factoring, and quadratics — the whole first course.",
    blurbMn:
      "Илэрхийлэл, тэгшитгэл, тэнцэтгэл биш, функц, шулуун, систем, үржигдэхүүнд задлах, квадрат тэгшитгэл. Эхний курс бүтнээрээ.",
    units: 8,
    level: 1,
    exams: ["ЭШ", "SAT"],
  },
  {
    href: "/math/geometry",
    title: "Geometry",
    titleMn: "Геометр",
    blurb:
      "From points and lines to proof, circles, and trigonometry — taught from zero, one continuous track.",
    blurbMn:
      "Цэг, шулуунаас баталгаа, тойрог, тригонометр хүртэл. Эхнээс нь, нэг тасралтгүй замаар заана.",
    units: 13,
    level: 2,
    exams: ["ЭШ", "SAT"],
  },
  {
    href: "/math/trigonometry",
    title: "Trigonometry",
    titleMn: "Тригонометр",
    blurb:
      "Right-triangle ratios, the special triangles, the unit circle and its waves, identities — and the laws that solve any triangle. A diagram at nearly every step.",
    blurbMn:
      "Тэгш өнцөгт гурвалжны харьцаа, нэгж тойрог ба түүний долгион, адилтгал, ямар ч гурвалжинг бодох синус, косинусын теорем. Бараг алхам бүрт зурагтай.",
    units: 6,
    level: 2,
    exams: ["ЭШ", "SAT", "IB"],
    isNew: true,
  },
  {
    href: "/math/solid-geometry",
    title: "Solid Geometry",
    titleMn: "Огторгуйн геометр",
    blurb:
      "Geometry 2, off the page: lines and planes in space, prisms to spheres, cross-sections, and the k-k²-k³ scaling law — every 3D problem reduced to a flat triangle you can see.",
    blurbMn:
      "Огторгуй дахь шулуун ба хавтгай, призмээс бөмбөрцөг хүртэл, огтлол, төстэй биетийн k, k², k³ харьцаа. Огторгуйн бодлого бүрийг нүдээр харж болох хавтгай гурвалжин руу шилжүүлнэ.",
    units: 6,
    level: 2,
    exams: ["ЭШ", "SAT", "IB"],
    isNew: true,
  },
  {
    href: "/math/algebra-2",
    title: "Algebra 2",
    titleMn: "Алгебр 2",
    blurb:
      "Transformations, complex numbers, polynomials, radicals, exponentials and logs, rationals, and sequences — the bridge to precalculus.",
    blurbMn:
      "Хувиргалт, комплекс тоо, олон гишүүнт, язгуур, илтгэгч функц ба логарифм, рационал функц, дараалал. Прекалькулюс руу гүүр болно.",
    units: 8,
    level: 2,
    exams: ["ЭШ", "SAT", "IB"],
    isNew: true,
  },
  {
    href: "/math/prob-stats",
    title: "Combinatorics, Probability & Statistics",
    titleMn: "Магадлал ба статистик",
    blurb:
      "Count first, then measure chance, then read data honestly — one continuous track in three acts.",
    blurbMn:
      "Эхлээд тоолно, дараа нь магадлалыг хэмжинэ, эцэст нь өгөгдлийг шударгаар уншина. Гурван хэсэгтэй нэг тасралтгүй зам.",
    units: 12,
    level: 2,
    exams: ["ЭШ", "SAT", "IB"],
  },
  {
    href: "/math/precalculus",
    title: "Precalculus",
    titleMn: "Прекалькулюс",
    blurb:
      "The bridge to calculus, graph-first: transformations, polynomials, rationals, exponentials and logs, the unit circle, trig waves, and conics.",
    blurbMn:
      "Калькулюс руу гүүр, графикаас эхэлнэ: хувиргалт, олон гишүүнт, рационал функц, илтгэгч функц ба логарифм, нэгж тойрог, тригонометрийн долгион, конус огтлол.",
    units: 8,
    level: 3,
    exams: ["ЭШ", "IB"],
  },
  {
    href: "/math/vectors-matrices",
    title: "Vectors & Matrices",
    titleMn: "Вектор ба матриц",
    blurb:
      "Arrows made of numbers, then the grids that move them — components, dot products, space, determinants, inverses.",
    blurbMn:
      "Тоогоор бичсэн сум, дараа нь түүнийг хөдөлгөх матриц: координат, скаляр үржвэр, огторгуй, тодорхойлогч, урвуу матриц.",
    units: 6,
    level: 3,
    exams: ["ЭШ", "IB"],
  },
  {
    href: "/math/calculus",
    title: "Calculus",
    titleMn: "Калькулюс",
    blurb:
      "The mathematics of change: limits, derivatives and optimization, integrals and the Fundamental Theorem — the ladder's capstone.",
    blurbMn:
      "Өөрчлөлтийн математик: хязгаар, уламжлал ба оновчлол, интеграл ба Үндсэн теорем. Сэдвийн курсуудын оргил.",
    units: 6,
    level: 3,
    exams: ["ЭШ", "IB"],
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
    titleMn: "Нэгдсэн математик 1",
    blurb:
      "Linear equations and functions, systems, exponential growth, transformations and congruence, coordinate geometry, and one-variable statistics — algebra and geometry together, not in sequence.",
    blurbMn:
      "Шугаман тэгшитгэл ба функц, систем, илтгэгч өсөлт, хувиргалт, координатын геометр, өгөгдөл. Алгебр, геометрийг ээлжлэн биш, хамт заана.",
    units: 9,
    level: 1,
    exams: ["SAT"],
  },
  {
    href: "/math/integrated-2",
    title: "Integrated Math 2",
    titleMn: "Нэгдсэн математик 2",
    blurb:
      "Quadratics end to end — including the complex numbers a negative discriminant forces — plus rational exponents, similarity and right-triangle trigonometry, circles, and probability.",
    blurbMn:
      "Квадрат функцийг эхнээс нь дуустал, сөрөг дискриминант гарахад хэрэг болох комплекс тоотой нь. Мөн рационал илтгэгч, төсөөтэй дүрс, тэгш өнцөгт гурвалжны тригонометр, тойрог, магадлал.",
    units: 8,
    level: 2,
    exams: ["SAT"],
  },
  {
    href: "/math/integrated-3",
    title: "Integrated Math 3",
    titleMn: "Нэгдсэн математик 3",
    blurb:
      "Polynomials, rational and radical functions, logarithms, trigonometric functions, and statistical inference — the year that opens Precalculus. First three units live; the rest land in order.",
    blurbMn:
      "Олон гишүүнт, рационал ба язгуур функц, логарифм, тригонометрийн функц, статистик дүгнэлт. Прекалькулюсын үүд болох жил. Эхний гурван бүлэг нээлттэй, үлдсэн нь дарааллаар нэмэгдэнэ.",
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

function TransitionChip({ grade, mn }: { grade: number; mn: boolean }) {
  const label = mn ? TRANSITION_MN[grade] : TRANSITION[grade];
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
      {grade === 12 ? (mn ? "ЭШ-ын жил" : "ЭШ year") : mn ? "Элсэлтийн жил" : "Entrance year"}
    </span>
  );
}

// The band's ENTRY test (resource blueprint: placement at the top of each
// band, exit exams at the bottom).
function BandPlacementCard({ href, body, mn }: { href: string; body: string; mn: boolean }) {
  return (
    <Link
      href={href}
      className="card-edit p-4 mb-4 flex items-center gap-3 transition-colors"
      style={{ textDecoration: "none" }}
      {...cardHover}
    >
      <span className="mono text-[10px] uppercase flex-shrink-0" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
        {mn ? "Түвшин тогтоох" : "Placement"}
      </span>
      <span className="flex-1 text-[13px]" style={{ color: "var(--fg-1)" }}>{body}</span>
      <span className="mono text-[10px] uppercase flex-shrink-0" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
        {mn ? "Эхлэх" : "Start"}
      </span>
    </Link>
  );
}

// The band's EXIT exams, at the band's final grade.
function BandExamCard({ href, body, mn }: { href: string; body: string; mn: boolean }) {
  return (
    <Link
      href={href}
      className="card-edit p-4 mt-4 flex items-center gap-3 transition-colors"
      style={{ textDecoration: "none" }}
      {...cardHover}
    >
      <span className="mono text-[10px] uppercase flex-shrink-0" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
        {mn ? "Жишиг шалгалт" : "Band exam"}
      </span>
      <span className="flex-1 text-[13px]" style={{ color: "var(--fg-1)" }}>{body}</span>
      <span className="mono text-[10px] uppercase flex-shrink-0" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
        {mn ? "Нээх" : "Open"}
      </span>
    </Link>
  );
}

function GradeCard({ grade, active, mn }: { grade: number; active: boolean; mn: boolean }) {
  if (!active) {
    return (
      <div className="card-edit p-6 flex flex-col gap-2" style={{ opacity: 0.45, cursor: "default" }}>
        <span className="mono text-[10px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
          {mn ? "Удахгүй" : "Coming soon"}
        </span>
        <span className="serif" style={{ fontSize: 32, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)" }}>
          {mn ? `${grade}-р анги` : `Grade ${grade}`}
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
          {mn ? "Нээлттэй" : "Active"}
        </span>
        <TransitionChip grade={grade} mn={mn} />
      </span>
      <span className="serif" style={{ fontSize: 32, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)" }}>
        {mn ? `${grade}-р анги` : `Grade ${grade}`}
      </span>
      <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
        {mn ? `${TOPIC_COUNTS[grade] ?? 0} сэдэв` : `${TOPIC_COUNTS[grade] ?? 0} topics`}
      </span>
    </Link>
  );
}

export default function MathLandingPage() {
  const grades = listGrades();
  const { profile } = useRatings();
  const { lang } = useLang();
  const mn = lang === "mn";
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
            {mn ? `Удахгүй · ${c.units} бүлэг` : `In development · ${c.units} units`}
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
          {mn ? c.titleMn : c.title}
        </span>
        <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
          {mn ? c.blurbMn : c.blurb}
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
            {mn
              ? `${c.isNew ? "Шинэ · " : ""}Түвшин ${c.level} · ${c.units} бүлэг`
              : <>{c.isNew ? "New · " : ""}Level {c.level} · {c.units} units</>}
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
          {mn ? c.titleMn : c.title}
        </span>
        <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
          {mn ? c.blurbMn : c.blurb}
        </span>
      </Link>
    );

  return (
    // On the shared shell, like every other hub. This page used to
    // hand-copy HubShell's markup — same classes, but pt-12 pb-16 where
    // the kit says py-8, and its own <h1> at a different size — so it
    // drifted a little further from the hubs with every edit. A copy of
    // a design system is not the design system.
    <HubShell>
      <HubHeader
        eyebrow="Courses"
        title="Courses"
        // Counts, like every other hub's stats line — not a restatement
        // of the paragraph directly beneath it.
        statsLine={
          mn ? (
            <>
              <span className="tabular">{publishedOnly(TOPIC_COURSES).length}</span> сэдвийн
              курс · Нэгдсэн математикийн <span className="tabular">{publishedOnly(IM_COURSES).length}</span>{" "}
              жил · <span className="tabular">6–12</span>-р анги
            </>
          ) : (
          <>
            <span className="tabular">{publishedOnly(TOPIC_COURSES).length}</span> topic
            courses · <span className="tabular">{publishedOnly(IM_COURSES).length}</span>{" "}
            Integrated Math years · grades{" "}
            <span className="tabular">6–12</span>
          </>
          )
        }
      />
      <>
        <p className="mb-10 -mt-4" style={{ color: "var(--fg-1)", fontSize: 17, maxWidth: "56ch" }}>
          {mn ? (
            <>
              Доороос <strong>ангийн түвшнээ</strong> сонгоорой. Монголын
              хөтөлбөрийн Дунд анги, Ахлах анги, эсвэл тэдний хажуудах
              Нэгдсэн математикийн замаар явж болно. ЭШ, SAT, IB-д бэлдэж
              байгаа бол тэдгээр нь тусдаа хэсэгтэй.
            </>
          ) : (
            <>
          Find your <strong>school band</strong> below — Primary, Mid school or
          High school on the Mongol curriculum — or take the Integrated Math
          pathway beside them. Preparing for ЭШ, SAT or IB? Those have their
          own hubs.
            </>
          )}
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
              {mn ? "Дасгал" : "Practice"}
            </span>
            <span className="serif block mt-1" style={{ fontWeight: 400, fontSize: 20, letterSpacing: "-0.01em", color: "var(--fg)" }}>
              {mn ? "Бодлогын сан" : "Problem Bank"}
            </span>
            <span className="block mt-1 text-[13px]" style={{ color: "var(--fg-1)" }}>
              {mn
                ? "Курсын бүлэг бүрт Түвшин 1–3 гэж ангилсан бодлогын цуглуулга бий. Алдсан бодлогынхоо оронд ижил төстэй бодлого гарч, эзэмштэлээ давтана."
                : <>A problem collection for every course unit, labeled Level 1–3.
              Miss one and a similar problem comes right back until it sticks.</>}
            </span>
          </div>
          <span className="mono text-[10px] uppercase flex-shrink-0" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
            {mn ? "Нээх" : "Open"}
          </span>
        </Link>

        {/* ── The school bands (Mongol curriculum) ─────────────────────────
            Blueprint: General Math is organized by school band, not a flat
            course list. Primary is a visible coming-soon band; Mid school is
            grades 6–9; High school is grades 10–12 PLUS the named topic
            courses. Transition grades (5th/9th/12th) carry a badge. */}

        {/* PRIMARY BAND WITHDRAWN 2026-08-13 (owner: "elementary is the last
            last thing we worry about — you can even remove them from the
            website now"). The grades 2-4 courses, their builders, banks and
            the ministry alignment all remain in the repo and in the gates;
            only the public entry point is gone, so bringing the band back is
            re-adding this section, not re-authoring a year. lib/genmath-spines
            ALL_GRADES marks 1-5 inactive, which is what keeps their routes
            and the placement/ratings wiring off the site with them. */}

        <section id="mid-school" className="mb-12" style={{ scrollMarginTop: 96 }}>
          <div className="eyebrow mb-1.5">{mn ? "Дунд анги · Монголын хөтөлбөр" : "Mid school · Mongol curriculum"}</div>
          <p className="text-[13px] mb-4" style={{ color: "var(--fg-2)", maxWidth: "62ch" }}>
            {mn
              ? "6–9-р анги, сургуулийн хөтөлбөрийн дагуу жил жилээр. 9-р анги бол шилжилтийн жил: ахлах ангийн элсэлтийн шалгалтад бэлдэх үе."
              : <>Grades 6–9, following the school curriculum year by year. Grade 9
            is the transition year — the springboard to high-school entrance
            exams.</>}
          </p>
          <BandPlacementCard
            href="/math/placement/mid"
            mn={mn}
            body={mn
              ? "Аль ангиас эхлэхээ мэдэхгүй байна уу? Богино дасан зохицох тест 6–9-р анги бүрээс бодлого өгч, таны эхлэх ангийг тодорхойлно."
              : "Not sure which grade to start in? A short adaptive test samples every grade 6–9 and names your starting grade."}
          />
          <div className="grid gap-4" style={gridStyle}>
            {[6, 7, 8, 9].filter((g) => !isUnpublished(`/math/${g}`)).map((g) => (
              <GradeCard key={g} grade={g} active={isActive(g)} mn={mn} />
            ))}
          </div>
          <BandExamCard
            href="/math/9/exam"
            mn={mn}
            body={mn
              ? "Дунд ангийг 9-р ангийн бүрэн шалгалтаар дуусгаарай. Гурван хувилбар, сэдэв бүр багтсан, хаана явааг тань сэдэв бүрээр задалж харуулна."
              : "Finish the band with a full Grade 9 exam — three papers, every topic represented, a per-topic breakdown of where you stand."}
          />
        </section>

        <section id="high-school" className="mb-12" style={{ scrollMarginTop: 96 }}>
          <div className="eyebrow mb-1.5">{mn ? "Ахлах анги · Монголын хөтөлбөр" : "High school · Mongol curriculum"}</div>
          <p className="text-[13px] mb-4" style={{ color: "var(--fg-2)", maxWidth: "62ch" }}>
            {mn
              ? "10–12-р анги жил жилээр, мөн энэ түвшинд багтах сэдвийн бүрэн курсууд. 12-р анги бол ЭШ-ын жил. ЭШ-д бэлдэх материал ЭШ хэсэгт бий."
              : <>Grades 10–12 year by year — and the full topic courses that live in
            this band. Grade 12 is the ЭШ year; the ЭШ hub has the exam prep.</>}
          </p>
          <BandPlacementCard
            href="/math/placement/high"
            mn={mn}
            body={mn
              ? "Аль ангиас эхлэхээ мэдэхгүй байна уу? Богино дасан зохицох тест 10–12-р анги бүрээс бодлого өгч, таны эхлэх ангийг тодорхойлно."
              : "Not sure which grade to start in? A short adaptive test samples every grade 10–12 and names your starting grade."}
          />
          <div className="grid gap-4" style={gridStyle}>
            {[10, 11, 12].filter((g) => !isUnpublished(`/math/${g}`)).map((g) => (
              <GradeCard key={g} grade={g} active={isActive(g)} mn={mn} />
            ))}
          </div>
          <BandExamCard
            href="/math/12/exam"
            mn={mn}
            body={mn
              ? "Ахлах ангийг 12-р ангийн бүрэн шалгалтаар дуусгаарай. Гурван хувилбар, сэдэв бүр багтсан, ЭШ-д бэлдэж эхлэх тэр л зураглал."
              : "Finish the band with a full Grade 12 exam — three papers, every topic represented, the same map ЭШ prep starts from."}
          />

          {/* `#topics` stays on the topic-course catalog so the exam hubs'
              existing deep links still land here rather than the page top. */}
          {/* Phase 0 unpublished every standalone topic course, so this
              catalog can be empty. An eyebrow over an empty grid reads as a
              broken page, not as a deliberate cut — hide the whole block.
              `#topics` keeps its anchor for the hubs' existing deep links. */}
          <div
            id="topics"
            className="mt-8"
            style={{ scrollMarginTop: 96, display: publishedOnly(TOPIC_COURSES).length ? undefined : "none" }}
          >
            <div className="eyebrow mb-1.5">{mn ? "Сэдвийн курсууд" : "Topic courses"}</div>
            <p className="text-[13px] mb-4" style={{ color: "var(--fg-2)", maxWidth: "62ch" }}>
              {mn
                ? "Ахлах ангийн материалыг хичээл хичээлээр нь, эхнээс нь заана. Уламжлалт дарааллаар (Алгебр 1 → Геометр → Алгебр 2) үзэх эсвэл хэрэгтэй сэдэв рүүгээ шууд орж болно. Карт бүр ямар шалгалтад бэлддэгийг харуулна."
                : <>The high-school material taught subject by subject, from zero —
              take them in the classic order (Algebra 1 → Geometry → Algebra 2)
              or jump straight to the topic you need. Each card shows the exams
              it prepares.</>}
            </p>
            <div className="grid gap-4" style={gridStyle}>
              {publishedOnly(TOPIC_COURSES).map(renderCourseCard)}
            </div>
          </div>
        </section>

        <section
          id="integrated"
          className="mb-12"
          style={{ scrollMarginTop: 96, display: publishedOnly(IM_COURSES).length ? undefined : "none" }}
        >
          <div className="eyebrow mb-1.5">{mn ? "Нэгдсэн математикийн зам" : "Integrated Math pathway"}</div>
          <p className="text-[13px] mb-4" style={{ color: "var(--fg-2)", maxWidth: "62ch" }}>
            {mn
              ? "Ангийн түвшнүүдийн хажуудах зам. Жил бүр алгебр, геометр, статистикийг нэг нэгээр нь биш, хольж заана. IM1 → IM2 → IM3, дараа нь Прекалькулюс."
              : <>The pathway beside the bands — each year mixes algebra, geometry
            and statistics rather than teaching them one at a time. IM1 → IM2
            → IM3, then Precalculus.</>}
          </p>
          <div className="grid gap-4" style={gridStyle}>
            {publishedOnly(IM_COURSES).map(renderCourseCard)}
          </div>
        </section>
      </>
    </HubShell>
  );
}
