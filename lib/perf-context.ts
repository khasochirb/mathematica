// Performance contexts — the "which section of the platform" dimension on
// every recorded attempt. One event pipeline serves all sections; this
// module is the vocabulary that keeps their stats apart.
//
// Rules the whole analytics layer leans on:
//   - undefined/absent context on an attempt means "esh" (every row written
//     before contexts existed was ЭЕШ).
//   - accuracy is NEVER blended across contexts — an ЭЕШ exam MCQ and a
//     grade-6 lesson check are incomparable populations. Only additive
//     activity counts (attempts this week, streaks, XP) may cross contexts.

export const ESH_CONTEXT = "esh";

// Course contexts are derived from the lesson URL, so the player needs no
// per-page wiring: /math/prob-stats/... → "course:prob-stats",
// /math/6/... → "course:grade-6". Non-course paths return null (record
// nothing rather than guess).
export function contextFromPathname(pathname: string): string | null {
  const m = /^\/math\/(geometry|prob-stats|vectors-matrices|algebra-1|\d+)\//.exec(pathname);
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
  if (parts.length !== 4 || parts[0] !== "math") return null;
  const [, , unit, lesson] = parts;
  if (["practice", "test", "placement"].includes(lesson)) return null;
  return { unit, lesson };
}

// Student-facing Mongolian name for a context (dashboard section titles).
export function contextLabel(context: string): string {
  if (context === ESH_CONTEXT) return "ЭЕШ бэлтгэл";
  if (context === "course:geometry") return "Геометр";
  if (context === "course:prob-stats") return "Магадлал ба Статистик";
  if (context === "course:vectors-matrices") return "Вектор ба Матриц";
  if (context === "course:algebra-1") return "Алгебр 1";
  const grade = /^course:grade-(\d+)$/.exec(context);
  if (grade) return `${grade[1]}-р анги`;
  if (context === "sat") return "SAT";
  if (context === "ib") return "IB";
  return context;
}

// Where a context's course lives, for dashboard links.
export function contextHref(context: string): string | null {
  if (context === "course:geometry") return "/math/geometry";
  if (context === "course:prob-stats") return "/math/prob-stats";
  if (context === "course:vectors-matrices") return "/math/vectors-matrices";
  if (context === "course:algebra-1") return "/math/algebra-1";
  const grade = /^course:grade-(\d+)$/.exec(context);
  if (grade) return `/math/${grade[1]}`;
  if (context === ESH_CONTEXT) return "/practice/esh";
  if (context === "sat") return "/practice/sat";
  if (context === "ib") return "/practice/ib";
  return null;
}

// Where a context's detailed progress view lives. Exam hubs own their own
// deep-dive pages; the dashboard only ever links, never inlines.
export function contextProgressHref(context: string): string | null {
  if (context === ESH_CONTEXT) return "/practice/esh/progress";
  if (context === "sat") return "/practice/sat/progress";
  if (context === "ib") return "/practice/ib/progress";
  return contextHref(context);
}
