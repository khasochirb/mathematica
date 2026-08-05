"use client";

import Link from "next/link";
import TopicLink from "@/components/genmath/TopicLink";
import { ArrowLeft, ArrowRight } from "lucide-react";
import { getGrade3Spine, getGrade3TopicLocalized } from "@/lib/genmath-data/grade-3";
import { useLang } from "@/lib/lang-context";

// Grade 3 — the lowest year currently open, and the rung below Grade 4. It
// shipped as one complete batch, but the page still renders from the spine's
// `live` flags rather than assuming completeness: that is what will let
// grades 1 and 2 open topic by topic without touching this file.
export default function Grade3TopicsPage() {
  const spine = getGrade3Spine();
  const { lang } = useLang();
  const mn = lang === "mn";
  const liveCount = spine.filter((t) => t.live).length;
  const complete = liveCount === spine.length;

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        <div className="flex items-center gap-3 mb-6">
          <Link href="/math" className="p-2 rounded-md transition-colors" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">{mn ? "Хичээлүүд · 3-р анги" : "Courses · Grade 3"}</div>
        </div>

        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(32px, 5vw, 56px)", letterSpacing: "-0.04em", lineHeight: 1, color: "var(--fg)" }}>
          {mn ? "3-р ангийн сэдвүүд" : "Grade 3 Topics"}
        </h1>
        <p className="mt-3 mb-8" style={{ color: "var(--fg-1)", fontSize: 16 }}>
          {complete
            ? mn
              ? "Мянга хүртэлх тоо, дөрвөн үйлдэл, бутархай, дүрс, хэмжилт — бүтэн хичээлийн жил, зурагтайгаа бэлэн."
              : "Numbers to a thousand, the four operations, first fractions, shapes and measuring — the full year, drawn with figures throughout."
            : mn
              ? "Сэдвүүд нэг нэгээрээ нэмэгдэж байна."
              : "Topics go live one at a time as they are written."}
        </p>

        <div className="grid gap-4 sm:grid-cols-2">
          {spine.map((entry) => {
            if (!entry.live) {
              return (
                <div key={entry.slug} className="card-edit p-5 flex flex-col gap-1.5" style={{ opacity: 0.5, cursor: "default" }}>
                  <span className="mono text-[10px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                    {mn ? "Тун удахгүй" : "Coming soon"}
                  </span>
                  <span className="serif" style={{ fontSize: 22, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                    {entry.title}
                  </span>
                  <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>{entry.blurb}</span>
                </div>
              );
            }
            const topic = getGrade3TopicLocalized(entry.slug, lang);
            const lessonCount = topic?.lessons.length ?? 0;
            return (
              <TopicLink courseKey="3" topicSlug={entry.slug} key={entry.slug} href={`/math/3/${entry.slug}`} className="card-edit p-5 flex flex-col gap-1.5 transition-colors group" style={{ textDecoration: "none" }}>
                <span className="mono text-[10px] uppercase" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
                  {mn ? `${lessonCount} хичээл` : `${lessonCount} lessons`}
                </span>
                <span className="serif" style={{ fontSize: 22, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                  {topic?.title ?? entry.title}
                </span>
                <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>{topic?.blurb ?? entry.blurb}</span>
                <span className="mono text-[11px] uppercase inline-flex items-center gap-1 mt-1" style={{ color: "var(--accent)", letterSpacing: "0.06em" }}>
                  {mn ? "Эхлэх" : "Start"}
                  <ArrowRight className="w-3.5 h-3.5 transition-transform group-hover:translate-x-0.5" />
                </span>
              </TopicLink>
            );
          })}
        </div>

        <p className="text-[13px] mt-8" style={{ color: "var(--fg-3)" }}>
          {complete
            ? mn
              ? `Бүх ${spine.length} сэдэв нээлттэй — 3-р ангийн бүтэн хөтөлбөр.`
              : `All ${spine.length} topics are open — the complete Grade 3 year.`
            : mn
              ? `Одоогоор ${liveCount} сэдэв нээлттэй. Үлдсэн сэдвүүд бичигдэнгүүт нэмэгдэнэ.`
              : `${liveCount} of ${spine.length} topics are open so far; the rest join as they are written.`}
        </p>
      </div>
    </div>
  );
}
