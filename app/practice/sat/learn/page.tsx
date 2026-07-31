import Link from "next/link";
import { ArrowLeft, ArrowRight, BookOpen } from "lucide-react";
import { SAT_COURSES } from "@/lib/sat-course";

export const metadata = { title: "SAT Math Course" };

// The SAT hub's Course branch (resource blueprint / backlog #245): four
// domain courses mirroring the College Board's own blueprint. The list stays
// public; lessons, practice and tests gate on sign-in inside the shell.
export default function SatLearnPage() {
  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        <div className="flex items-center gap-3 mb-6">
          <Link
            href="/practice/sat"
            className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">SAT Math · Course</div>
        </div>

        <h1
          className="serif"
          style={{ fontWeight: 400, fontSize: "clamp(36px, 6vw, 56px)", letterSpacing: "-0.04em", lineHeight: 1.0, color: "var(--fg)" }}
        >
          The SAT Math <em className="serif-italic" style={{ color: "var(--accent)" }}>course</em>.
        </h1>
        <p className="text-[15px] mt-4 mb-10" style={{ color: "var(--fg-2)", maxWidth: "54ch" }}>
          Four courses, one per official College Board domain, weighted the way
          the test is. Every unit has lessons, a practice set, and a
          test-yourself — and the topic-practice bank drills the same four
          domains when you want volume.
        </p>

        <div className="space-y-4">
          {SAT_COURSES.map((c) => (
            <Link
              key={c.domain}
              href={`/practice/sat/learn/${c.domain}`}
              className="card-edit p-6 flex items-start gap-4 transition-colors hover:border-[var(--accent-line)]"
              style={{ textDecoration: "none" }}
            >
              <BookOpen className="h-4 w-4 mt-1.5 flex-shrink-0" style={{ color: "var(--accent)" }} />
              <span className="flex-1 min-w-0">
                <span className="flex items-center gap-2 flex-wrap">
                  <span className="serif" style={{ fontSize: 22, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                    {c.title}
                  </span>
                  <span
                    className="mono rounded-full px-2 py-0.5 text-[10px] uppercase"
                    style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)", letterSpacing: "0.06em" }}
                  >
                    {c.weight}
                  </span>
                  <span
                    className="mono rounded-full px-2 py-0.5 text-[10px] uppercase"
                    style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-3)", letterSpacing: "0.06em" }}
                  >
                    {c.units.length} units
                  </span>
                </span>
                <span className="block mt-1.5 text-[13px]" style={{ color: "var(--fg-2)" }}>
                  {c.intro}
                </span>
              </span>
              <ArrowRight className="h-4 w-4 flex-shrink-0 mt-2" style={{ color: "var(--fg-3)" }} />
            </Link>
          ))}
        </div>

        <p className="text-[13px] mt-8" style={{ color: "var(--fg-3)" }}>
          Lessons are shared with the General Math catalog — the same verified
          content, curated and re-ordered for the SAT. Want the fundamentals
          from an earlier grade first? The{" "}
          <Link href="/math" style={{ color: "var(--accent)" }}>
            course catalog
          </Link>{" "}
          has the full ladder.
        </p>
      </div>
    </div>
  );
}
