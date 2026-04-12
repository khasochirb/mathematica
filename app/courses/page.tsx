"use client";

import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { T } from "@/components/T";
import { useLang } from "@/lib/lang-context";

/*
 * ЭЕШ math topics with subtopics.
 * Each topic card links to /practice/esh with a topic query param.
 * TODO: wire up topic query param filtering once practice/esh supports ?topic=<slug>
 */
const topics = [
  {
    slug: "algebra",
    icon: "📐",
    en: {
      name: "Algebra",
      desc: "The foundation of ЭЕШ math — equations, inequalities, and polynomials make up the largest share of the exam.",
      subtopics: [
        "Linear equations & inequalities",
        "Quadratic equations",
        "Systems of equations",
        "Polynomials & factoring",
        "Absolute value equations",
        "Rational expressions",
      ],
    },
    mn: {
      name: "Алгебр",
      desc: "ЭЕШ математикийн суурь — тэгшитгэл, тэнцэтгэл биш, олон гишүүнт нь шалгалтын хамгийн их хувийг эзэлдэг.",
      subtopics: [
        "Шугаман тэгшитгэл ба тэнцэтгэл биш",
        "Квадрат тэгшитгэл",
        "Тэгшитгэлийн систем",
        "Олон гишүүнт ба задлан шинжлэх",
        "Абсолют утгын тэгшитгэл",
        "Рациональ илэрхийлэл",
      ],
    },
    weight: "~25%",
    color: "from-blue-500 to-blue-400",
  },
  {
    slug: "functions",
    icon: "📈",
    en: {
      name: "Functions & Graphs",
      desc: "Understanding how functions behave and how to read their graphs is tested in nearly every ЭЕШ section.",
      subtopics: [
        "Linear & quadratic functions",
        "Exponential & logarithmic functions",
        "Domain, range, and inverses",
        "Function composition",
        "Graph transformations",
        "Piecewise functions",
      ],
    },
    mn: {
      name: "Функц ба график",
      desc: "Функцийн шинж чанар, графикийг уншиж ойлгохыг ЭЕШ-ийн бараг бүх хэсэгт шалгадаг.",
      subtopics: [
        "Шугаман ба квадрат функц",
        "Экспоненциал ба логарифм функц",
        "Тодорхойлогдох муж, утгын муж, урвуу",
        "Функцийн давхар",
        "Графикийн хувиргалт",
        "Хэсэгчилсэн функц",
      ],
    },
    weight: "~20%",
    color: "from-emerald-500 to-emerald-400",
  },
  {
    slug: "geometry",
    icon: "📏",
    en: {
      name: "Geometry",
      desc: "Plane and solid geometry — triangles, circles, areas, volumes, and coordinate geometry problems.",
      subtopics: [
        "Triangles (properties, similarity, congruence)",
        "Circles (chords, tangents, arcs)",
        "Area and perimeter",
        "Volume and surface area",
        "Coordinate geometry",
        "Vectors in the plane",
      ],
    },
    mn: {
      name: "Геометр",
      desc: "Хавтгай ба огторгуйн геометр — гурвалжин, тойрог, талбай, эзэлхүүн, координатын геометрийн бодлогууд.",
      subtopics: [
        "Гурвалжин (шинж чанар, ижил төстэй, тэнцүү)",
        "Тойрог (хөвч, шүргэгч, нум)",
        "Талбай ба периметр",
        "Эзэлхүүн ба гадаргуугийн талбай",
        "Координатын геометр",
        "Хавтгай дахь вектор",
      ],
    },
    weight: "~20%",
    color: "from-violet-500 to-violet-400",
  },
  {
    slug: "trigonometry",
    icon: "🔺",
    en: {
      name: "Trigonometry",
      desc: "Trigonometric identities, equations, and their applications are a consistent part of the exam.",
      subtopics: [
        "Trigonometric ratios & unit circle",
        "Trig identities (sum, double angle, etc.)",
        "Trigonometric equations",
        "Inverse trigonometric functions",
        "Law of sines & cosines",
        "Applications (triangles, angles)",
      ],
    },
    mn: {
      name: "Тригонометр",
      desc: "Тригонометрийн адилтгал, тэгшитгэл, тэдгээрийн хэрэглээ шалгалтанд тогтмол ордог.",
      subtopics: [
        "Тригонометрийн харьцаа ба нэгж тойрог",
        "Триг адилтгалууд (нийлбэр, давхар өнцөг г.м.)",
        "Тригонометрийн тэгшитгэл",
        "Урвуу тригонометрийн функц",
        "Синусын ба косинусын теорем",
        "Хэрэглээ (гурвалжин, өнцөг)",
      ],
    },
    weight: "~10%",
    color: "from-orange-500 to-orange-400",
  },
  {
    slug: "calculus",
    icon: "∫",
    en: {
      name: "Calculus",
      desc: "Limits, derivatives, and integrals — the most challenging section, heavily tested in Part 2.",
      subtopics: [
        "Limits & continuity",
        "Derivatives (rules, chain rule)",
        "Applications of derivatives",
        "Definite & indefinite integrals",
        "Applications of integrals (area, volume)",
      ],
    },
    mn: {
      name: "Анализ",
      desc: "Хязгаар, уламжлал, интеграл — хамгийн хэцүү хэсэг, 2-р хэсэгт ихээр шалгадаг.",
      subtopics: [
        "Хязгаар ба тасралтгүй байдал",
        "Уламжлал (дүрмүүд, гинжин дүрэм)",
        "Уламжлалын хэрэглээ",
        "Тодорхой ба тодорхойгүй интеграл",
        "Интегралын хэрэглээ (талбай, эзэлхүүн)",
      ],
    },
    weight: "~10%",
    color: "from-red-500 to-red-400",
  },
  {
    slug: "probability",
    icon: "🎲",
    en: {
      name: "Probability & Statistics",
      desc: "Combinatorics, probability theory, and descriptive statistics appear in both Part 1 and Part 2.",
      subtopics: [
        "Counting principles & permutations",
        "Combinations",
        "Basic probability",
        "Conditional probability",
        "Mean, median, mode, variance",
        "Data interpretation",
      ],
    },
    mn: {
      name: "Магадлал ба статистик",
      desc: "Комбинаторик, магадлалын онол, тодорхойлох статистик 1-р ба 2-р хэсэгт аль алинд нь ордог.",
      subtopics: [
        "Тоолох зарчим ба сэлгэмэл",
        "Хослол",
        "Үндсэн магадлал",
        "Нөхцөлт магадлал",
        "Дундаж, медиан, моод, дисперс",
        "Өгөгдлийн тайлбар",
      ],
    },
    weight: "~10%",
    color: "from-pink-500 to-pink-400",
  },
  {
    slug: "sequences",
    icon: "🔢",
    en: {
      name: "Sequences & Series",
      desc: "Arithmetic and geometric progressions, their sums, and limits of sequences.",
      subtopics: [
        "Arithmetic sequences & series",
        "Geometric sequences & series",
        "Sum formulas",
        "Limits of sequences",
        "Recursive sequences",
      ],
    },
    mn: {
      name: "Дараалал ба цуваа",
      desc: "Арифметик ба геометрийн прогресс, тэдгээрийн нийлбэр, дарааллын хязгаар.",
      subtopics: [
        "Арифметик дараалал ба цуваа",
        "Геометрийн дараалал ба цуваа",
        "Нийлбэрийн томъёо",
        "Дарааллын хязгаар",
        "Рекурсив дараалал",
      ],
    },
    weight: "~5%",
    color: "from-cyan-500 to-cyan-400",
  },
  {
    slug: "logarithms",
    icon: "📊",
    en: {
      name: "Logarithms",
      desc: "Logarithmic properties, equations, and their connection to exponential functions.",
      subtopics: [
        "Logarithmic properties",
        "Logarithmic equations",
        "Change of base",
        "Natural logarithm",
        "Exponential-logarithmic relationships",
      ],
    },
    mn: {
      name: "Логарифм",
      desc: "Логарифмын шинж чанар, тэгшитгэл, экспоненциал функцтэй холбоос.",
      subtopics: [
        "Логарифмын шинж чанар",
        "Логарифмын тэгшитгэл",
        "Суурь солих",
        "Натурал логарифм",
        "Экспоненциал-логарифмын хамаарал",
      ],
    },
    weight: "~5%",
    color: "from-amber-500 to-amber-400",
  },
];

export default function TopicsPage() {
  const { lang } = useLang();

  return (
    <>
      {/* Hero */}
      <section className="relative bg-surface-900 text-white pt-28 pb-20 overflow-hidden">
        <div className="absolute inset-0 bg-grid animate-grid-fade" />
        <div className="absolute inset-0 glow-top-right" />
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative">
          <div className="badge-glow mb-4 mx-auto w-fit">
            <T en="ЭЕШ Math Topics" mn="ЭЕШ математикийн сэдвүүд" />
          </div>
          <h1 className="font-display text-4xl sm:text-5xl lg:text-6xl font-bold mb-5">
            <T en="Study by " mn="Сэдвээр " />
            <span className="gradient-text">
              <T en="topic" mn="суралцах" />
            </span>
          </h1>
          <p className="text-gray-400 text-lg max-w-2xl mx-auto leading-relaxed">
            <T
              en="Every topic covered in the ЭЕШ math exam, organized by subject area. Pick a topic to start practicing."
              mn="ЭЕШ математикийн шалгалтанд хамрагдах бүх сэдвүүд, чиглэлээр ангилсан. Сэдвээ сонгоод дадлагаа эхлээрэй."
            />
          </p>
        </div>
      </section>

      {/* Topic cards */}
      <section className="section-dark">
        <div className="absolute inset-0 bg-grid opacity-30" />
        <div className="container-lg relative">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {topics.map((topic) => {
              const content = lang === "mn" ? topic.mn : topic.en;
              return (
                <div
                  key={topic.slug}
                  id={topic.slug}
                  className="card-glass-glow border-glow group flex flex-col"
                >
                  <div className="flex items-start justify-between mb-4">
                    <div className="flex items-center gap-3">
                      <div className={`text-3xl`}>{topic.icon}</div>
                      <div>
                        <h3 className="text-lg font-display font-bold text-white group-hover:text-primary-300 transition-colors">
                          {content.name}
                        </h3>
                        <span className="text-xs font-semibold text-primary-400">{topic.weight} <T en="of the exam" mn="шалгалтаас" /></span>
                      </div>
                    </div>
                  </div>

                  <p className="text-gray-400 text-sm leading-relaxed mb-4">{content.desc}</p>

                  <div className="flex-1">
                    <p className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">
                      <T en="Subtopics" mn="Дэд сэдвүүд" />
                    </p>
                    <div className="flex flex-wrap gap-1.5 mb-5">
                      {content.subtopics.map((sub) => (
                        <span
                          key={sub}
                          className="px-2.5 py-1 bg-white/[0.04] border border-white/[0.08] rounded-lg text-xs text-gray-400"
                        >
                          {sub}
                        </span>
                      ))}
                    </div>
                  </div>

                  {/* TODO: add ?topic=slug query param once practice/esh supports topic filtering from URL */}
                  <Link
                    href="/practice/esh"
                    className="btn-secondary text-sm py-2.5 text-center w-full"
                  >
                    <T en={`Practice ${content.name}`} mn={`${content.name} дадлага`} />
                    <ArrowRight className="ml-1.5 h-3.5 w-3.5" />
                  </Link>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="section relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-primary-950 via-primary-900 to-surface-900" />
        <div className="absolute inset-0 bg-grid opacity-30" />
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-primary-500/[0.12] blur-[120px] rounded-full" />
        <div className="container-lg text-center relative">
          <h2 className="font-display text-3xl sm:text-4xl font-bold text-white mb-5">
            <T en="Not sure where to start?" mn="Хаанаас эхлэхээ мэдэхгүй байна уу?" />
          </h2>
          <p className="text-gray-400 text-lg mb-10 max-w-xl mx-auto">
            <T
              en="Try all topics and our system will identify your weak areas. Focus your time where it matters most."
              mn="Бүх сэдвийг туршаад манай систем сул талуудыг тань тодорхойлно. Хамгийн чухал газартаа цагаа зарцуул."
            />
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <Link href="/practice/esh" className="btn-white text-base px-8 py-3.5">
              <T en="Start All Topics" mn="Бүх сэдвийг эхлэх" />
              <ArrowRight className="ml-2 h-4 w-4" />
            </Link>
            <Link href="/exam-prep" className="btn-secondary text-base px-8 py-3.5">
              <T en="Exam Overview" mn="Шалгалтын тойм" />
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
