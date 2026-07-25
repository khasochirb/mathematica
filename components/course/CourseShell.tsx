"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import type { CourseUnit, GenMathLesson, GeometrySpineEntry } from "@/lib/genmath-lessons";
import LessonPlayer from "@/components/genmath/interactive/LessonPlayer";
import GradedProblemList from "@/components/lesson/GradedProblemList";
import ContentGate from "@/components/genmath/ContentGate";
import CoursePersonalization from "@/components/course/CoursePersonalization";
import CoursePlacementCta from "@/components/course/CoursePlacementCta";

// The five pages every named course under /math needs — hub, unit, lesson,
// practice, test — as one parameterized shell.
//
// The eleven courses that predate this file each carry their own copy of these
// five pages; the copies differ only in the course slug, the display name, and
// which getter they call. New courses take the shell instead, so a change to
// the course chrome lands once rather than once per course.
export interface CourseDef {
  /** Path segment under /math — e.g. "integrated-1". */
  slug: string;
  /** Display name in headings and crumbs — e.g. "Integrated Math 1". */
  title: string;
  /** Perf-context key — e.g. "course:integrated-1". */
  context: string;
  /** Hub intro paragraph. */
  intro: string;
  spine: () => GeometrySpineEntry[];
  unit: (unitSlug: string) => CourseUnit | null;
  lesson: (unitSlug: string, lessonSlug: string) => GenMathLesson | null;
  /** Placement namespace + route, when the course has a placement test. */
  placement?: string;
}

const REVEAL_LABELS = {
  reveal: "Show solution",
  hide: "Hide",
  revealAria: "Show solution",
  hideAria: "Hide solution",
};

const BACK_BUTTON_STYLE = {
  background: "var(--bg-2)",
  border: "1px solid var(--line)",
  color: "var(--fg-2)",
};

function hoverAccent(on: boolean) {
  return (e: React.MouseEvent<HTMLAnchorElement>) => {
    const el = e.currentTarget;
    el.style.borderColor = on ? "var(--accent-line)" : "";
    el.style.background = on ? "var(--accent-wash)" : "";
  };
}

function NotFound({ what, href, label }: { what: string; href: string; label: string }) {
  return (
    <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
      <div className="text-center">
        <p className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
          {what}{" "}
          <em className="serif-italic" style={{ color: "var(--accent)" }}>
            not found
          </em>
          .
        </p>
        <Link href={href} className="btn btn-line mt-5 inline-flex items-center gap-1.5">
          <ArrowLeft className="h-3.5 w-3.5" /> {label}
        </Link>
      </div>
    </div>
  );
}

function Crumb({ href, label }: { href: string; label: string }) {
  return (
    <div className="flex items-center gap-3 mb-6">
      <Link href={href} className="p-2 rounded-md transition-colors" style={BACK_BUTTON_STYLE}>
        <ArrowLeft className="w-4 h-4" />
      </Link>
      <div className="eyebrow">{label}</div>
    </div>
  );
}

function Shell({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">{children}</div>
    </div>
  );
}

// --- Hub: the course spine, in order --------------------------------------
export function CourseHubPage({ course }: { course: CourseDef }) {
  const spine = course.spine();
  const liveCount = spine.filter((u) => u.live).length;

  return (
    <Shell>
      <Crumb href="/math" label="Courses" />

      <h1
        className="serif"
        style={{
          fontWeight: 400,
          fontSize: "clamp(32px, 5vw, 54px)",
          letterSpacing: "-0.04em",
          lineHeight: 1.05,
          color: "var(--fg)",
        }}
      >
        {course.title}
      </h1>
      <p className="mt-4 mb-8" style={{ color: "var(--fg-1)", fontSize: 17, maxWidth: "56ch" }}>
        {course.intro}
      </p>

      {course.placement && (
        <CoursePlacementCta
          namespace={course.placement}
          href={`/math/${course.slug}/placement`}
          unitTitle={(s) => spine.find((u) => u.slug === s)?.title}
        />
      )}

      <CoursePersonalization context={course.context} />

      <div className="eyebrow mb-4">
        The course — {liveCount} unit{liveCount === 1 ? "" : "s"}, in order
      </div>
      <ol className="space-y-3">
        {spine.map((u) => {
          const number = (
            <span
              className="mono text-[11px] flex-shrink-0 tabular mt-1"
              style={{ color: u.live ? "var(--accent)" : "var(--fg-3)", letterSpacing: "0.04em", minWidth: 24 }}
            >
              {String(u.unit).padStart(2, "0")}
            </span>
          );
          const body = (
            <span className="flex-1 min-w-0">
              <span
                className="serif block"
                style={{ fontWeight: 400, fontSize: 18, letterSpacing: "-0.01em", color: "var(--fg)" }}
              >
                {u.title}
              </span>
              <span className="block mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>
                {u.blurb}
              </span>
            </span>
          );

          return (
            <li key={u.slug}>
              {u.live ? (
                <Link
                  href={`/math/${course.slug}/${u.slug}`}
                  className="card-edit p-5 flex items-start gap-4 transition-colors"
                  style={{ textDecoration: "none" }}
                  onMouseEnter={hoverAccent(true)}
                  onMouseLeave={hoverAccent(false)}
                >
                  {number}
                  {body}
                  <span
                    className="mono text-[10px] uppercase mt-1 flex-shrink-0"
                    style={{ color: "var(--accent)", letterSpacing: "0.08em" }}
                  >
                    Start
                  </span>
                </Link>
              ) : (
                <div className="card-edit p-5 flex items-start gap-4" style={{ opacity: 0.45, cursor: "default" }}>
                  {number}
                  {body}
                  <span
                    className="mono text-[10px] uppercase mt-1 flex-shrink-0"
                    style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}
                  >
                    Soon
                  </span>
                </div>
              )}
            </li>
          );
        })}
      </ol>
    </Shell>
  );
}

// --- Unit: what it builds on, then the lessons in order --------------------
export function CourseUnitPage({ course }: { course: CourseDef }) {
  const params = useParams();
  const unitSlug = params.unit as string;
  const unit = course.unit(unitSlug);
  const spineEntry = course.spine().find((u) => u.slug === unitSlug);

  if (!unit) {
    return <NotFound what="Unit" href={`/math/${course.slug}`} label="Back to the course" />;
  }

  const buildsOn = unit.buildsOn ?? spineEntry?.buildsOn;

  return (
    <Shell>
      <Crumb href={`/math/${course.slug}`} label={`${course.title} · Unit ${unit.unit}`} />

      <h1
        className="serif"
        style={{
          fontWeight: 400,
          fontSize: "clamp(30px, 5vw, 52px)",
          letterSpacing: "-0.04em",
          lineHeight: 1.02,
          color: "var(--fg)",
        }}
      >
        {unit.title}
      </h1>
      <p className="mt-3 mb-6" style={{ color: "var(--fg-1)", fontSize: 16 }}>
        {unit.blurb}
      </p>

      {buildsOn && (
        <div
          className="card-edit p-4 mb-10"
          style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
        >
          <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>
            Builds on
          </div>
          <p className="text-[14px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
            {buildsOn}
          </p>
        </div>
      )}

      <div className="eyebrow mb-4">Lessons</div>
      <ol className="space-y-3">
        {unit.lessons.map((lesson, i) => (
          <li key={lesson.slug}>
            <Link
              href={`/math/${course.slug}/${unitSlug}/${lesson.slug}`}
              className="card-edit p-5 flex items-center gap-4 transition-colors"
              style={{ textDecoration: "none" }}
              onMouseEnter={hoverAccent(true)}
              onMouseLeave={hoverAccent(false)}
            >
              <span
                className="mono text-[11px] flex-shrink-0 tabular"
                style={{ color: "var(--fg-3)", letterSpacing: "0.04em", minWidth: 24 }}
              >
                {String(i + 1).padStart(2, "0")}
              </span>
              <span
                className="serif flex-1"
                style={{ fontWeight: 400, fontSize: 17, letterSpacing: "-0.01em", color: "var(--fg)" }}
              >
                {lesson.title}
              </span>
            </Link>
          </li>
        ))}
      </ol>

      {(unit.practice.length > 0 || unit.testYourself.length > 0) && (
        <>
          <div className="eyebrow mt-10 mb-3">Ready to check yourself?</div>
          <div className="flex flex-wrap gap-3">
            {unit.practice.length > 0 && (
              <Link href={`/math/${course.slug}/${unitSlug}/practice`} className="btn btn-primary">
                Practice
              </Link>
            )}
            {unit.testYourself.length > 0 && (
              <Link href={`/math/${course.slug}/${unitSlug}/test`} className="btn btn-line">
                Test yourself
              </Link>
            )}
          </div>
        </>
      )}
    </Shell>
  );
}

// --- Lesson: the paced interactive player ---------------------------------
function LessonInner({ course }: { course: CourseDef }) {
  const params = useParams();
  const unitSlug = params.unit as string;
  const lessonSlug = params.lesson as string;

  const unit = course.unit(unitSlug);
  const lesson = course.lesson(unitSlug, lessonSlug);

  if (!lesson || !unit || !lesson.interactive) {
    return <NotFound what="Lesson" href={`/math/${course.slug}/${unitSlug}`} label="Back to unit" />;
  }

  return (
    <LessonPlayer
      lesson={lesson}
      topicSlug={unitSlug}
      topicTitle={unit.title}
      baseHref={`/math/${course.slug}/${unitSlug}`}
      crumb={`${course.title} · Unit ${unit.unit} · ${unit.title}`}
    />
  );
}

// Content requires an account; the hub and unit pages stay public.
export function CourseLessonPage({ course }: { course: CourseDef }) {
  const params = useParams();
  const unitSlug = params.unit as string;
  return (
    <ContentGate backHref={`/math/${course.slug}/${unitSlug}`} backLabel="Back to unit">
      <LessonInner course={course} />
    </ContentGate>
  );
}

// --- Practice + Test yourself ---------------------------------------------
function ProblemsInner({ course, kind }: { course: CourseDef; kind: "practice" | "test" }) {
  const params = useParams();
  const unitSlug = params.unit as string;
  const unit = course.unit(unitSlug);

  if (!unit) {
    return <NotFound what="Unit" href={`/math/${course.slug}`} label="Back to the course" />;
  }

  const problems = kind === "practice" ? unit.practice : unit.testYourself;

  return (
    <Shell>
      <Crumb
        href={`/math/${course.slug}/${unitSlug}`}
        label={`${course.title} · Unit ${unit.unit} · ${unit.title}`}
      />

      <h1
        className="serif"
        style={{
          fontWeight: 400,
          fontSize: "clamp(28px, 4vw, 48px)",
          letterSpacing: "-0.04em",
          lineHeight: 1,
          color: "var(--fg)",
        }}
      >
        {kind === "practice" ? "Practice" : "Test Yourself"} — {unit.title}
      </h1>

      {kind === "practice" ? (
        <p className="mt-3 mb-8" style={{ color: "var(--fg-2)", fontSize: 14 }}>
          Work through each problem, then reveal the solution to check your answer.
        </p>
      ) : (
        <div className="card-edit p-4 mt-4 mb-8" style={{ background: "var(--bg-1)" }}>
          <p className="mono text-[11px] uppercase mb-1" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
            Self-graded
          </p>
          <p className="text-[13px]" style={{ color: "var(--fg-2)" }}>
            Attempt each problem on paper, reveal the solution, and grade yourself honestly — your self-checks feed
            your progress stats.
          </p>
        </div>
      )}

      <div className="space-y-4">
        <GradedProblemList problems={problems} labels={REVEAL_LABELS} kind={kind} />
      </div>
    </Shell>
  );
}

export function CoursePracticePage({ course }: { course: CourseDef }) {
  const params = useParams();
  const unitSlug = params.unit as string;
  return (
    <ContentGate backHref={`/math/${course.slug}/${unitSlug}`} backLabel="Back to unit">
      <ProblemsInner course={course} kind="practice" />
    </ContentGate>
  );
}

export function CourseTestPage({ course }: { course: CourseDef }) {
  const params = useParams();
  const unitSlug = params.unit as string;
  return (
    <ContentGate backHref={`/math/${course.slug}/${unitSlug}`} backLabel="Back to unit">
      <ProblemsInner course={course} kind="test" />
    </ContentGate>
  );
}
