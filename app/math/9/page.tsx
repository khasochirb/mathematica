"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Sparkles } from "lucide-react";
import { getGrade9Spine, getGenMathTopic, getGenMathTopicLocalized } from "@/lib/genmath-lessons";
import { useLang } from "@/lib/lang-context";
import { useAuth } from "@/lib/auth-context";
import { loadPlacement, type StoredPlacement } from "@/lib/placement-result";

// Grade 9 hub — built one topic at a time. The full roadmap is visible from
// day one: live topics link in, the rest show the road ahead.
export default function Grade9TopicsPage() {
  const spine = getGrade9Spine();
  const { user } = useAuth();
  const { lang } = useLang();
  const mn = lang === "mn";
  const [placement, setPlacement] = useState<StoredPlacement | null>(null);

  // Placement result lives in the browser (keyed to the account when signed
  // in); load after mount and re-read when the signed-in user changes.
  useEffect(() => {
    setPlacement(loadPlacement(user?.id, "grade9"));
  }, [user?.id]);

  const prioritySet = new Set(placement?.priorityTopics ?? []);
  const priorityTitles = (placement?.priorityTopics ?? [])
    .map((slug) => getGenMathTopicLocalized(slug, lang)?.title ?? spine.find((t) => t.slug === slug)?.title)
    .filter(Boolean) as string[];

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        {/* Back + eyebrow */}
        <div className="flex items-center gap-3 mb-6">
          <Link href="/math" className="p-2 rounded-md transition-colors" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">{mn ? "Ерөнхий математик · 9-р анги" : "General Math · Grade 9"}</div>
        </div>

        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(32px, 5vw, 56px)", letterSpacing: "-0.04em", lineHeight: 1, color: "var(--fg)" }}>
          {mn ? "9-р ангийн сэдвүүд" : "Grade 9 Topics"}
        </h1>
        <p className="mt-3 mb-8" style={{ color: "var(--fg-1)", fontSize: 16, maxWidth: "56ch" }}>
          {mn
            ? "Алгебр 1-ийн жил — томьёо ба үсэгт тэгшитгэл, давхар ба абсолют утгат тэнцэтгэл биш, функцийн тэмдэглэгээ, шугаман загвар ба хувьсал, хоёр хувьсагчтай тэнцэтгэл бишийн системүүд, хэсэгчилсэн графикууд, өгөгдлийн тархалт. Сэдэв бүрийг интерактив, өөрийгөө шалгадаг хичээлүүдээр сууриас нь зааж өгнө."
            : "The Algebra 1 year — formulas and literal equations, compound and absolute-value inequalities, function notation, linear models and variation, systems of inequalities, piecewise graphs, and data distributions. Each topic is taught from the ground up with interactive, self-checking lessons."}
        </p>

        {/* Placement CTA / summary */}
        {placement ? (
          <Link href="/math/9/placement" className="card-edit p-4 mb-8 flex items-center gap-4" style={{ textDecoration: "none", borderColor: "var(--accent-line)", background: "var(--accent-wash)" }}>
            <span className="grid h-9 w-9 flex-shrink-0 place-items-center rounded-full" style={{ background: "var(--accent)", color: "var(--accent-ink, #fff)" }}>
              <Sparkles className="h-4.5 w-4.5" />
            </span>
            <div className="flex-1 min-w-0">
              <p className="serif" style={{ fontSize: 16, color: "var(--fg)" }}>
                {mn ? <>Таны түвшин: <b style={{ color: "var(--accent)" }}>{placement.level}</b></> : <>You&apos;re at the <b style={{ color: "var(--accent)" }}>{placement.level}</b> level</>}
              </p>
              <p className="text-[13px] mt-0.5" style={{ color: "var(--fg-2)" }}>
                {priorityTitles.length > 0
                  ? (mn ? <>Эхлээд <b>{priorityTitles.slice(0, 3).join(", ")}</b> сэдвүүдэд анхаараарай — доор тэмдэглэсэн.</> : <>Focus first on <b>{priorityTitles.slice(0, 3).join(", ")}</b> — marked below.</>)
                  : (mn ? <>Та бүх сэдэвт хүчтэй байна. Хүссэн үедээ дахин өгөөрэй.</> : <>You&apos;re strong across the board. Retake anytime.</>)}
              </p>
            </div>
            <span className="mono text-[11px] flex-shrink-0" style={{ color: "var(--accent)" }}>{mn ? "Дахин өгөх →" : "Retake →"}</span>
          </Link>
        ) : (
          <Link href="/math/9/placement" className="card-edit p-4 mb-8 flex items-center gap-4" style={{ textDecoration: "none", borderColor: "var(--accent-line)", background: "var(--accent-wash)" }}>
            <span className="grid h-9 w-9 flex-shrink-0 place-items-center rounded-full" style={{ background: "var(--accent)", color: "var(--accent-ink, #fff)" }}>
              <Sparkles className="h-4.5 w-4.5" />
            </span>
            <div className="flex-1 min-w-0">
              <p className="serif" style={{ fontSize: 16, color: "var(--fg)" }}>{mn ? "Түвшин тогтоох тест өгөх" : "Take the placement test"}</p>
              <p className="text-[13px] mt-0.5" style={{ color: "var(--fg-2)" }}>
                {mn ? "Богино дасан зохицдог тест таны түвшинг тогтоож, танд хамгийн чухал сэдвүүдийг тэмдэглэнэ." : "A quick adaptive test finds your level and marks the topics most important for you."}
              </p>
            </div>
            <ArrowRight className="h-4 w-4 flex-shrink-0" style={{ color: "var(--accent)" }} />
          </Link>
        )}

        {/* The spine */}
        <div className="eyebrow mb-4">{mn ? "Хөтөлбөр — 7 сэдэв, дарааллаар" : "The course — 7 topics, in order"}</div>
        <ol className="space-y-3">
          {spine.map((t, i) => {
            const topic = t.live ? getGenMathTopicLocalized(t.slug, lang) : null;
            const lessonCount = topic?.lessons.length ?? 0;
            const cardTitle = topic?.title ?? t.title;
            const cardBlurb = topic?.blurb ?? t.blurb;
            const important = prioritySet.has(t.slug);
            return t.live ? (
              <li key={t.slug}>
                <Link
                  href={`/math/9/${t.slug}`}
                  className="card-edit p-5 flex items-start gap-4 transition-colors"
                  style={{ textDecoration: "none", ...(important ? { borderColor: "var(--accent-line)" } : {}) }}
                  onMouseEnter={(e) => {
                    (e.currentTarget as HTMLAnchorElement).style.borderColor = "var(--accent-line)";
                    (e.currentTarget as HTMLAnchorElement).style.background = "var(--accent-wash)";
                  }}
                  onMouseLeave={(e) => {
                    (e.currentTarget as HTMLAnchorElement).style.borderColor = "";
                    (e.currentTarget as HTMLAnchorElement).style.background = "";
                  }}
                >
                  <span className="mono text-[11px] flex-shrink-0 tabular mt-1" style={{ color: "var(--accent)", letterSpacing: "0.04em", minWidth: 24 }}>
                    {String(i + 1).padStart(2, "0")}
                  </span>
                  <span className="flex-1 min-w-0">
                    <span className="flex items-center gap-2 flex-wrap">
                      <span className="serif" style={{ fontWeight: 400, fontSize: 18, letterSpacing: "-0.01em", color: "var(--fg)" }}>
                        {cardTitle}
                      </span>
                      {important && (
                        <span className="rounded-full px-2 py-0.5 text-[10px] font-medium" style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}>
                          {mn ? "Танд чухал" : "Important for you"}
                        </span>
                      )}
                    </span>
                    <span className="block mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>
                      {cardBlurb}
                    </span>
                  </span>
                  <span className="mono text-[11px] flex-shrink-0 mt-1" style={{ color: "var(--fg-3)" }}>
                    {mn ? `${lessonCount} хичээл` : `${lessonCount} lesson${lessonCount !== 1 ? "s" : ""}`}
                  </span>
                </Link>
              </li>
            ) : (
              <li key={t.slug}>
                <div className="card-edit p-5 flex items-start gap-4" style={{ opacity: 0.45, cursor: "default" }}>
                  <span className="mono text-[11px] flex-shrink-0 tabular mt-1" style={{ color: "var(--fg-3)", letterSpacing: "0.04em", minWidth: 24 }}>
                    {String(i + 1).padStart(2, "0")}
                  </span>
                  <span className="flex-1 min-w-0">
                    <span className="serif block" style={{ fontWeight: 400, fontSize: 18, letterSpacing: "-0.01em", color: "var(--fg)" }}>
                      {t.title}
                    </span>
                    <span className="block mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>
                      {t.blurb}
                    </span>
                  </span>
                  <span className="mono text-[10px] uppercase mt-1 flex-shrink-0" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                    Soon
                  </span>
                </div>
              </li>
            );
          })}
        </ol>
      </div>
    </div>
  );
}
