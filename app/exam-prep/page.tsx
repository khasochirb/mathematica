"use client";

import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { useLang } from "@/lib/lang-context";

export default function ExamPrepPage() {
  const { lang } = useLang();
  const t = (en: string, mn: string) => (lang === "mn" ? mn : en);

  const bullets = [
    t(
      "Held at the end of June each year, for high school graduates seeking university admission.",
      "Жил бүрийн 6-р сарын сүүлчээр зохион байгуулагддаг их, дээд сургуульд элсэхийг хүссэн ахлах сургуулийн төгсөгчдөд зориулагдсан шалгалт.",
    ),
    t(
      "Section 1: 36 multiple-choice problems. Section 2: 4 open-ended problems.",
      "1-р хэсэг: 36 сонгох бодлого. 2-р хэсэг: 4 нээлттэй бодлого.",
    ),
    t(
      "Total 100 minutes to solve and submit your answers.",
      "Нийт 100 минутад багтаж бодлогоо бодон, хариултаа бөглөнө.",
    ),
  ];

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      {/* Hero — title + 3 facts */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 pb-14">
        <div className="eyebrow mb-3">{t("ЭЕШ Exam Prep · Overview", "ЭЕШ Шалгалтын бэлтгэл · Тойм")}</div>
        <h1
          className="serif"
          style={{
            fontWeight: 400,
            fontSize: "clamp(40px, 6vw, 72px)",
            letterSpacing: "-0.04em",
            lineHeight: 1.02,
            color: "var(--fg)",
            maxWidth: "20ch",
          }}
        >
          {t(
            "Mongolian university entrance exam math prep",
            "Математикийн Элсэлтийн Ерөнхий Шалгалтын бэлтгэл",
          )}
        </h1>
        <ul
          style={{
            margin: "36px 0 0",
            padding: 0,
            listStyle: "none",
            borderTop: "1px solid var(--line)",
            maxWidth: 720,
          }}
        >
          {bullets.map((b, i) => (
            <li
              key={i}
              className="grid gap-4 py-4"
              style={{
                borderBottom: "1px solid var(--line)",
                gridTemplateColumns: "32px 1fr",
                fontSize: 15,
                lineHeight: 1.55,
                color: "var(--fg-1)",
                alignItems: "start",
              }}
            >
              <span
                className="mono uppercase"
                style={{
                  color: "var(--accent)",
                  fontSize: 11,
                  letterSpacing: "0.1em",
                  paddingTop: 3,
                }}
              >
                {String(i + 1).padStart(2, "0")}
              </span>
              <span>{b}</span>
            </li>
          ))}
        </ul>
      </section>

      {/* CTA */}
      <section
        className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-14"
        style={{ borderTop: "1px solid var(--line)" }}
      >
        <div
          className="card-edit p-12 text-center"
          style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
        >
          <div className="eyebrow mb-3">{t("Begin", "Эхлэх")}</div>
          <h2
            className="serif"
            style={{
              fontWeight: 400,
              fontSize: "clamp(32px, 4.5vw, 52px)",
              letterSpacing: "-0.03em",
              color: "var(--fg)",
            }}
          >
            {t("Start your ЭЕШ prep ", "ЭЕШ бэлтгэлээ ")}
            <em className="serif-italic" style={{ color: "var(--accent)" }}>
              {t("today", "өнөөдөр")}
            </em>
            {t(".", " эхэл.")}
          </h2>
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
