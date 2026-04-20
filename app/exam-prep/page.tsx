"use client";

import Link from "next/link";
import { ArrowRight, Clock, Target, BarChart3, FileText } from "lucide-react";
import { useLang } from "@/lib/lang-context";

export default function ExamPrepPage() {
  const { lang } = useLang();
  const t = (en: string, mn: string) => (lang === "mn" ? mn : en);

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      {/* Hero */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 pb-10">
        <div className="eyebrow mb-3">{t("ЭЕШ Exam Prep · Overview", "ЭЕШ Шалгалтын бэлтгэл · Тойм")}</div>
        <h1
          className="serif"
          style={{
            fontWeight: 400,
            fontSize: "clamp(48px, 7vw, 88px)",
            letterSpacing: "-0.04em",
            lineHeight: 0.96,
            color: "var(--fg)",
          }}
        >
          {t("Master the ЭЕШ ", "ЭЕШ Математикийг ")}
          <em className="serif-italic" style={{ color: "var(--accent)" }}>
            {t("math exam", "эзэмш")}
          </em>
          .
        </h1>
        <p className="serif mt-5 max-w-2xl" style={{ fontSize: 18, lineHeight: 1.5, color: "var(--fg-1)" }}>
          {t(
            "The ЭЕШ (Элсэлтийн Ерөнхий Шалгалт) is Mongolia's national university entrance exam. Real-format problems, topic breakdowns, and performance tracking — built to score your best.",
            "ЭЕШ (Элсэлтийн Ерөнхий Шалгалт) бол Монголын их, дээд сургуулийн элсэлтийн шалгалт. Жинхэнэ форматын бодлого, сэдвийн задаргаа, гүйцэтгэлийн хяналт — хамгийн өндөр оноо авахад зориулсан.",
          )}
        </p>
        <div className="flex flex-wrap gap-2 mt-7">
          <Link href="/practice/esh" className="btn btn-primary">
            {t("Start practicing now", "Одоо дадлага эхлэх")}
            <ArrowRight className="ml-1 h-3.5 w-3.5" />
          </Link>
          <Link href="/courses" className="btn btn-line">
            {t("Study by topic", "Сэдвээр суралцах")}
          </Link>
        </div>
      </section>

      {/* Exam structure */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12" style={{ borderTop: "1px solid var(--line)" }}>
        <div className="mb-8">
          <div className="eyebrow mb-3">{t("01 · Exam structure", "01 · Шалгалтын бүтэц")}</div>
          <h2 className="serif" style={{ fontWeight: 400, fontSize: "clamp(32px, 4.5vw, 52px)", letterSpacing: "-0.03em", color: "var(--fg)" }}>
            {t("What is the ", "ЭЕШ ")}
            <em className="serif-italic" style={{ color: "var(--accent)" }}>{t("ЭЕШ", "гэж")}</em>
            {t("?", " юу вэ?")}
          </h2>
          <p className="serif mt-4 max-w-2xl" style={{ fontSize: 16, lineHeight: 1.55, color: "var(--fg-1)" }}>
            {t(
              "Taken by all Mongolian high school graduates seeking university admission. Administered annually each May.",
              "Их, дээд сургуульд элсэхийг хүссэн бүх Монгол ахлах сургуулийн төгсөгчдөд зориулагдсан. Жил бүрийн 5-р сард зохион байгуулдаг.",
            )}
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {[
            {
              icon: FileText,
              en: { title: "Format", desc: "Part 1: 30 multiple-choice (A–E). Part 2: 10 open-ended problems with written solutions." },
              mn: { title: "Формат", desc: "1-р хэсэг: 30 сонгох (А–Е). 2-р хэсэг: 10 нээлттэй бодлого, бичгээр бодолтоо харуулна." },
            },
            {
              icon: Clock,
              en: { title: "Duration", desc: "3 hours total. Part 1 and Part 2 in one continuous sitting." },
              mn: { title: "Хугацаа", desc: "Нийт 3 цаг. 1-р ба 2-р хэсгийг нэг удаа тасралтгүй бичнэ." },
            },
            {
              icon: BarChart3,
              en: { title: "Scoring", desc: "Total: 800. Part 1: ~400 (each ~13). Part 2: ~400 (partial credit)." },
              mn: { title: "Оноо", desc: "Нийт: 800. 1-р хэсэг: ~400 (зөв бүр ~13). 2-р хэсэг: ~400 (хэсэгчилсэн)." },
            },
            {
              icon: Target,
              en: { title: "Subjects", desc: "One subject per student. Math is required by most STEM and economics programs." },
              mn: { title: "Хичээл", desc: "Сурагчид нэг хичээл сонгоно. Математик STEM, эдийн засгийн ихэнх хөтөлбөрт шаардлагатай." },
            },
          ].map((card, i) => {
            const Icon = card.icon;
            const content = lang === "mn" ? card.mn : card.en;
            return (
              <div key={card.en.title} className="card-edit p-5">
                <div className="flex items-start justify-between mb-3">
                  <div
                    className="w-9 h-9 rounded-md flex items-center justify-center"
                    style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}
                  >
                    <Icon className="h-4 w-4" />
                  </div>
                  <span className="mono text-[10px]" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                    {String(i + 1).padStart(2, "0")}
                  </span>
                </div>
                <h3 className="serif" style={{ fontWeight: 400, fontSize: 20, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                  {content.title}
                </h3>
                <p className="text-[13px] mt-2 leading-relaxed" style={{ color: "var(--fg-2)" }}>
                  {content.desc}
                </p>
              </div>
            );
          })}
        </div>
      </section>

      {/* CTA */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-14" style={{ borderTop: "1px solid var(--line)" }}>
        <div
          className="card-edit p-12 text-center"
          style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
        >
          <div className="eyebrow mb-3">{t("Begin", "Эхлэх")}</div>
          <h2 className="serif" style={{ fontWeight: 400, fontSize: "clamp(32px, 4.5vw, 52px)", letterSpacing: "-0.03em", color: "var(--fg)" }}>
            {t("Start your ЭЕШ prep ", "ЭЕШ бэлтгэлээ ")}
            <em className="serif-italic" style={{ color: "var(--accent)" }}>{t("today", "өнөөдөр")}</em>
            .
          </h2>
          <p className="text-[15px] mt-4 max-w-xl mx-auto" style={{ color: "var(--fg-1)" }}>
            {t(
              "Real ЭЕШ-format problems, topic-level progress, and a focus on your weak spots.",
              "Жинхэнэ ЭЕШ форматын бодлого, сэдвээр дэвшил, сул талд анхаарал.",
            )}
          </p>
          <div className="flex flex-wrap justify-center gap-2 mt-7">
            <Link href="/practice/esh" className="btn btn-primary">
              {t("Start practicing free", "Үнэгүй дадлага эхлэх")}
              <ArrowRight className="ml-1 h-3.5 w-3.5" />
            </Link>
            <Link href="/courses" className="btn btn-line">
              {t("Browse topics", "Сэдвүүдийг үзэх")}
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}
