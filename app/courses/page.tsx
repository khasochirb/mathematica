"use client";

import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { useLang } from "@/lib/lang-context";

const topics = [
  {
    slug: "algebra",
    weight: 25,
    en: {
      name: "Algebra",
      desc: "The foundation of ЭЕШ math — equations, inequalities, and polynomials make up the largest share of the exam.",
      subtopics: ["Linear equations & inequalities", "Quadratic equations", "Systems of equations", "Polynomials & factoring", "Absolute value equations", "Rational expressions"],
    },
    mn: {
      name: "Алгебр",
      desc: "ЭЕШ математикийн суурь — тэгшитгэл, тэнцэтгэл биш, олон гишүүнт нь шалгалтын хамгийн их хувийг эзэлдэг.",
      subtopics: ["Шугаман тэгшитгэл", "Квадрат тэгшитгэл", "Тэгшитгэлийн систем", "Олон гишүүнт", "Абсолют утга", "Рациональ илэрхийлэл"],
    },
  },
  {
    slug: "functions",
    weight: 20,
    en: {
      name: "Functions & Graphs",
      desc: "Understanding how functions behave and how to read their graphs is tested in nearly every ЭЕШ section.",
      subtopics: ["Linear & quadratic functions", "Exponential & logarithmic", "Domain, range, inverses", "Function composition", "Graph transformations", "Piecewise functions"],
    },
    mn: {
      name: "Функц ба график",
      desc: "Функцийн шинж чанар, графикийг уншиж ойлгохыг ЭЕШ-ийн бараг бүх хэсэгт шалгадаг.",
      subtopics: ["Шугаман ба квадрат", "Экспоненциал ба логарифм", "Тодорхойлогдох муж", "Функцийн давхар", "Графикийн хувиргалт", "Хэсэгчилсэн функц"],
    },
  },
  {
    slug: "geometry",
    weight: 20,
    en: {
      name: "Geometry",
      desc: "Plane and solid geometry — triangles, circles, areas, volumes, and coordinate geometry problems.",
      subtopics: ["Triangles", "Circles", "Area and perimeter", "Volume and surface area", "Coordinate geometry", "Vectors in the plane"],
    },
    mn: {
      name: "Геометр",
      desc: "Хавтгай ба огторгуйн геометр — гурвалжин, тойрог, талбай, эзэлхүүн, координатын геометр.",
      subtopics: ["Гурвалжин", "Тойрог", "Талбай ба периметр", "Эзэлхүүн", "Координатын геометр", "Вектор"],
    },
  },
  {
    slug: "trigonometry",
    weight: 10,
    en: {
      name: "Trigonometry",
      desc: "Trigonometric identities, equations, and their applications are a consistent part of the exam.",
      subtopics: ["Trig ratios & unit circle", "Identities (sum, double angle)", "Trig equations", "Inverse trig functions", "Law of sines & cosines", "Applications"],
    },
    mn: {
      name: "Тригонометр",
      desc: "Тригонометрийн адилтгал, тэгшитгэл, тэдгээрийн хэрэглээ шалгалтанд тогтмол ордог.",
      subtopics: ["Харьцаа ба нэгж тойрог", "Адилтгалууд", "Тэгшитгэл", "Урвуу функц", "Синус, косинус теорем", "Хэрэглээ"],
    },
  },
  {
    slug: "calculus",
    weight: 10,
    en: {
      name: "Calculus",
      desc: "Limits, derivatives, and integrals — the most challenging section, heavily tested in Part 2.",
      subtopics: ["Limits & continuity", "Derivatives", "Applications of derivatives", "Definite & indefinite integrals", "Applications of integrals"],
    },
    mn: {
      name: "Анализ",
      desc: "Хязгаар, уламжлал, интеграл — хамгийн хэцүү хэсэг, 2-р хэсэгт ихээр шалгадаг.",
      subtopics: ["Хязгаар", "Уламжлал", "Уламжлалын хэрэглээ", "Интеграл", "Интегралын хэрэглээ"],
    },
  },
  {
    slug: "probability",
    weight: 10,
    en: {
      name: "Probability & Statistics",
      desc: "Combinatorics, probability theory, and descriptive statistics appear in both Part 1 and Part 2.",
      subtopics: ["Counting & permutations", "Combinations", "Basic probability", "Conditional probability", "Mean, median, mode, variance", "Data interpretation"],
    },
    mn: {
      name: "Магадлал ба статистик",
      desc: "Комбинаторик, магадлалын онол, статистик 1-р, 2-р хэсэгт ордог.",
      subtopics: ["Тоолох зарчим", "Хослол", "Үндсэн магадлал", "Нөхцөлт магадлал", "Дундаж, медиан", "Өгөгдлийн тайлбар"],
    },
  },
  {
    slug: "sequences",
    weight: 5,
    en: {
      name: "Sequences & Series",
      desc: "Arithmetic and geometric progressions, their sums, and limits of sequences.",
      subtopics: ["Arithmetic sequences", "Geometric sequences", "Sum formulas", "Limits of sequences", "Recursive sequences"],
    },
    mn: {
      name: "Дараалал ба цуваа",
      desc: "Арифметик, геометрийн прогресс, нийлбэр, дарааллын хязгаар.",
      subtopics: ["Арифметик дараалал", "Геометрийн дараалал", "Нийлбэрийн томъёо", "Хязгаар", "Рекурсив дараалал"],
    },
  },
  {
    slug: "logarithms",
    weight: 5,
    en: {
      name: "Logarithms",
      desc: "Logarithmic properties, equations, and their connection to exponential functions.",
      subtopics: ["Properties", "Equations", "Change of base", "Natural logarithm", "Exponential-log relationships"],
    },
    mn: {
      name: "Логарифм",
      desc: "Логарифмын шинж чанар, тэгшитгэл, экспоненциал функцтэй холбоос.",
      subtopics: ["Шинж чанар", "Тэгшитгэл", "Суурь солих", "Натурал логарифм", "Экспоненциал-логарифмын хамаарал"],
    },
  },
];

export default function TopicsPage() {
  const { lang } = useLang();
  const t = (en: string, mn: string) => (lang === "mn" ? mn : en);

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      {/* Hero */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 pb-10">
        <div className="eyebrow mb-3">{t("ЭЕШ Topics · Math", "ЭЕШ Сэдвүүд · Математик")}</div>
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
          {t("Study by ", "Сэдвээр ")}
          <em className="serif-italic" style={{ color: "var(--accent)" }}>
            {t("topic", "суралцах")}
          </em>
          .
        </h1>
        <p className="serif mt-5 max-w-2xl" style={{ fontSize: 18, lineHeight: 1.5, color: "var(--fg-1)" }}>
          {t(
            "Every topic covered in the ЭЕШ math exam, organized by subject area. Pick a topic to start practicing.",
            "ЭЕШ математикийн шалгалтад хамрагдах бүх сэдвүүд, чиглэлээр ангилсан. Сэдвээ сонгоод дадлагаа эхлээрэй.",
          )}
        </p>
      </section>

      {/* Topic cards */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-10" style={{ borderTop: "1px solid var(--line)" }}>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {topics.map((topic, idx) => {
            const content = lang === "mn" ? topic.mn : topic.en;
            return (
              <div key={topic.slug} id={topic.slug} className="card-edit p-6 flex flex-col group">
                <div className="flex items-start justify-between mb-4">
                  <div>
                    <div className="eyebrow mb-1.5" style={{ color: "var(--accent)" }}>
                      {String(idx + 1).padStart(2, "0")} · {t("Weight", "Жин")} ~{topic.weight}%
                    </div>
                    <h3
                      className="serif"
                      style={{ fontWeight: 400, fontSize: 26, letterSpacing: "-0.02em", color: "var(--fg)" }}
                    >
                      {content.name}
                    </h3>
                  </div>
                  <div
                    className="serif tabular flex items-baseline gap-1"
                    style={{ color: "var(--fg-3)" }}
                  >
                    <span style={{ fontSize: 32, color: "var(--accent)", letterSpacing: "-0.03em" }}>
                      {topic.weight}
                    </span>
                    <span className="mono text-[10px]" style={{ letterSpacing: "0.06em" }}>%</span>
                  </div>
                </div>

                <p className="text-[14px] leading-relaxed mb-4" style={{ color: "var(--fg-2)" }}>
                  {content.desc}
                </p>

                <div className="flex-1">
                  <div className="eyebrow mb-2.5">{t("Subtopics", "Дэд сэдвүүд")}</div>
                  <div className="flex flex-wrap gap-1.5 mb-5">
                    {content.subtopics.map((sub) => (
                      <span
                        key={sub}
                        className="badge-edit"
                        style={{ background: "var(--bg-2)" }}
                      >
                        {sub}
                      </span>
                    ))}
                  </div>
                </div>

                <Link href="/practice/esh" className="btn btn-line w-full">
                  {t("Practice ", "Дадлага · ")}
                  {content.name}
                  <ArrowRight className="ml-1 h-3.5 w-3.5" />
                </Link>
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
          <div className="eyebrow mb-3">{t("Not sure?", "Эргэлзэж байна уу?")}</div>
          <h2
            className="serif"
            style={{ fontWeight: 400, fontSize: "clamp(32px, 4.5vw, 52px)", letterSpacing: "-0.03em", color: "var(--fg)" }}
          >
            {t("Where to ", "Хаанаас ")}
            <em className="serif-italic" style={{ color: "var(--accent)" }}>
              {t("start", "эхлэх")}
            </em>
            ?
          </h2>
          <p className="text-[15px] mt-4 max-w-xl mx-auto" style={{ color: "var(--fg-1)" }}>
            {t(
              "Try all topics and our system will identify your weak areas. Focus your time where it matters most.",
              "Бүх сэдвийг туршаад манай систем сул талуудыг танижуулна. Хамгийн чухал газартаа цагаа зарцуул.",
            )}
          </p>
          <div className="flex flex-wrap justify-center gap-2 mt-7">
            <Link href="/practice/esh" className="btn btn-primary">
              {t("Start all topics", "Бүх сэдвийг эхлэх")}
              <ArrowRight className="ml-1 h-3.5 w-3.5" />
            </Link>
            <Link href="/exam-prep" className="btn btn-line">
              {t("Exam overview", "Шалгалтын тойм")}
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}
