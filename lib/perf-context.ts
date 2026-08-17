// Performance contexts — the "which section of the platform" dimension on
// every recorded attempt. One event pipeline serves all sections; this
// module is the vocabulary that keeps their stats apart.
//
// Rules the whole analytics layer leans on:
//   - undefined/absent context on an attempt means "esh" (every row written
//     before contexts existed was ЭШ).
//   - accuracy is NEVER blended across contexts — an ЭШ exam MCQ and a
//     grade-6 lesson check are incomparable populations. Only additive
//     activity counts (attempts this week, streaks, XP) may cross contexts.

export const ESH_CONTEXT = "esh";

// The taught ЭШ courses at /practice/esh/learn. Kept apart from ESH_CONTEXT
// (past papers and topic drills) so neither pollutes the other's accuracy.
export const ESH_COURSE_CONTEXT = "course:esh";

// The taught SAT Math course at /practice/sat/learn — same split for the
// same reason: course lessons and mock-test MCQs are different populations.
export const SAT_COURSE_CONTEXT = "course:sat";

// Course contexts are derived from the lesson URL, so the player needs no
// per-page wiring: /math/prob-stats/... → "course:prob-stats",
// /math/6/... → "course:grade-6". Non-course paths return null (record
// nothing rather than guess).
export function contextFromPathname(pathname: string): string | null {
  // The ЭШ prep courses live inside the exam hub, not under /math. They are
  // course work, not exam practice, so they get their own course context
  // rather than folding into "esh" — accuracy on a taught lesson and accuracy
  // on a past-paper MCQ are not comparable populations.
  if (/^\/practice\/esh\/learn\/[^/]+\/[^/]+/.test(pathname)) return ESH_COURSE_CONTEXT;
  if (/^\/practice\/sat\/learn\/[^/]+\/[^/]+/.test(pathname)) return SAT_COURSE_CONTEXT;

  const m = /^\/math\/(solid-geometry|geometry|prob-stats|vectors-matrices|algebra-1|algebra-2|integrated-1|integrated-2|integrated-3|precalculus|calculus|trigonometry|ib-sl|ib-hl|ib-ai-sl|\d+)\//.exec(pathname);
  if (!m) return null;
  const seg = m[1];
  return /^\d+$/.test(seg) ? `course:grade-${seg}` : `course:${seg}`;
}

// Unit/topic and lesson slugs from a lesson pathname —
// /math/<section>/<unit-or-topic>/<lesson>. Null when the path isn't a
// lesson page (hub, practice, test, placement).
export function lessonSlugsFromPathname(
  pathname: string,
): { unit: string; lesson: string } | null {
  const parts = pathname.split("/").filter(Boolean);
  // /practice/<hub>/learn/<topic>/<unit>/<lesson> — one segment deeper than
  // the /math courses, because the hub topic/domain is part of the path.
  if (
    parts.length === 6 &&
    parts[0] === "practice" &&
    (parts[1] === "esh" || parts[1] === "sat") &&
    parts[2] === "learn"
  ) {
    const [, , , , unit, lesson] = parts;
    if (["practice", "test"].includes(lesson)) return null;
    return { unit, lesson };
  }
  if (parts.length !== 4 || parts[0] !== "math") return null;
  const [, , unit, lesson] = parts;
  if (["practice", "test", "placement"].includes(lesson)) return null;
  return { unit, lesson };
}

// Student-facing Mongolian name for a context (dashboard section titles).
export function contextLabel(context: string): string {
  if (context === ESH_CONTEXT) return "ЭШ бэлтгэл";
  if (context === ESH_COURSE_CONTEXT) return "ЭШ курс";
  if (context === SAT_COURSE_CONTEXT) return "SAT курс";
  if (context === "course:geometry") return "Геометр";
  if (context === "course:prob-stats") return "Магадлал ба Статистик";
  if (context === "course:vectors-matrices") return "Вектор ба Матриц";
  if (context === "course:algebra-1") return "Алгебр 1";
  if (context === "course:algebra-2") return "Алгебр 2";
  if (context === "course:integrated-1") return "Нэгдсэн математик 1";
  if (context === "course:integrated-2") return "Нэгдсэн математик 2";
  if (context === "course:integrated-3") return "Нэгдсэн математик 3";
  if (context === "course:precalculus") return "Прекалькулюс";
  if (context === "course:calculus") return "Математик анализ";
  if (context === "course:trigonometry") return "Тригонометр";
  if (context === "course:solid-geometry") return "Огторгуйн геометр";
  if (context === "course:ib-sl") return "IB Math SL (AA)";
  if (context === "course:ib-ai-sl") return "IB Math SL (AI)";
  if (context === "course:ib-hl") return "IB Math HL (AA)";
  const grade = /^course:grade-(\d+)$/.exec(context);
  if (grade) return `${grade[1]}-р анги`;
  if (context === "sat") return "SAT";
  if (context === "ib") return "IB";
  return context;
}

// Where a context's course lives, for dashboard links.
export function contextHref(context: string): string | null {
  if (context === ESH_COURSE_CONTEXT) return "/practice/esh/learn";
  if (context === SAT_COURSE_CONTEXT) return "/practice/sat/learn";
  if (context === "course:geometry") return "/math/geometry";
  if (context === "course:prob-stats") return "/math/prob-stats";
  if (context === "course:vectors-matrices") return "/math/vectors-matrices";
  if (context === "course:algebra-1") return "/math/algebra-1";
  if (context === "course:algebra-2") return "/math/algebra-2";
  if (context === "course:integrated-1") return "/math/integrated-1";
  if (context === "course:integrated-2") return "/math/integrated-2";
  if (context === "course:integrated-3") return "/math/integrated-3";
  if (context === "course:precalculus") return "/math/precalculus";
  if (context === "course:calculus") return "/math/calculus";
  if (context === "course:trigonometry") return "/math/trigonometry";
  if (context === "course:solid-geometry") return "/math/solid-geometry";
  if (context === "course:ib-sl") return "/math/ib-sl";
  if (context === "course:ib-ai-sl") return "/math/ib-ai-sl";
  if (context === "course:ib-hl") return "/math/ib-hl";
  const grade = /^course:grade-(\d+)$/.exec(context);
  if (grade) return `/math/${grade[1]}`;
  if (context === ESH_CONTEXT) return "/practice/esh";
  if (context === "sat") return "/practice/sat";
  if (context === "ib") return "/practice/ib";
  return null;
}

// Where a context's detailed progress view lives. Exam hubs own their own
// deep-dive pages; courses share one report page keyed by query param.
// The dashboard only ever links, never inlines.
export function contextProgressHref(context: string): string | null {
  // ЭШ has ONE report, at /analytics; the hub route redirects there.
  if (context === ESH_CONTEXT) return "/analytics";
  // Course-shaped, but it lives in the exam hub — must not fall through to
  // /math/progress?course=esh, which is not a course /math knows about.
  if (context === ESH_COURSE_CONTEXT) return "/analytics";
  if (context === SAT_COURSE_CONTEXT) return "/sat-analytics";
  // Each exam hub has ONE analytics report; the hub's /progress route
  // redirects to it. Same rule as ЭШ above.
  if (context === "sat") return "/sat-analytics";
  if (context === "ib") return "/ib-analytics";
  if (context.startsWith("course:") && contextHref(context)) {
    return `/math/progress?course=${context.slice("course:".length)}`;
  }
  return contextHref(context);
}
