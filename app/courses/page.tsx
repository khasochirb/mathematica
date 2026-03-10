"use client";

import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { T } from "@/components/T";
import { useLang } from "@/lib/lang-context";

const levels = [
  {
    id: "elementary",
    emoji: "🧒",
    en: {
      label: "Elementary School",
      range: "Grades 2–5 · Ages 7–11",
      description: "We build strong foundations in arithmetic, number sense, and early problem-solving. Our approach makes math fun and culturally relevant, using Mongolian stories and everyday contexts to spark curiosity.",
      topics: ["Number sense & place value", "Addition, subtraction, multiplication, division", "Fractions and decimals", "Basic geometry and measurement", "Word problems and logical reasoning"],
      coverLabel: "Topics we cover",
    },
    mn: {
      label: "Бага сургууль",
      range: "2–5-р анги · 7–11 нас",
      description: "Арифметик, тоон ойлголт, эрт дэс бодлого шийдэхэд хүчтэй суурь тавьдаг. Монгол үлгэр, өдөр тутмын орчин ашиглан математикийг хөгжилтэй, соёлтой холбоотой болгоно.",
      topics: ["Тооны мэдрэмж ба байрны утга", "Нэмэх, хасах, үржих, хуваах", "Бутархай ба аравтын бутархай", "Үндсэн геометр ба хэмжилт", "Текст бодлого, логик үндэслэл"],
      coverLabel: "Хамрагдах сэдвүүд",
    },
  },
  {
    id: "middle",
    emoji: "🏫",
    en: {
      label: "Middle School",
      range: "Grades 6–8 · Ages 11–14",
      description: "The years when students either gain confidence in math or lose it. We ensure students develop algebraic thinking, master ratios and proportions, and are fully prepared for high school mathematics.",
      topics: ["Pre-Algebra and introductory Algebra", "Ratios, rates, and proportional reasoning", "Geometry and the coordinate plane", "Statistics and probability", "MATHCOUNTS / AMC 8 competition prep"],
      coverLabel: "Topics we cover",
    },
    mn: {
      label: "Дунд сургууль",
      range: "6–8-р анги · 11–14 нас",
      description: "Оюутнууд математикт итгэлтэй болох эсвэл итгэлгүй болох жилүүд. Алгебрийн сэтгэлгээг хөгжүүлж, харьцаа, пропорцийг эзэмшиж, ахлах сургуулийн математикт бүрэн бэлэн болгоно.",
      topics: ["Алгебрын өмнөх, алгебрын эхэн", "Харьцаа, хурд, пропорциональ үндэслэл", "Геометр ба координатын хавтгай", "Статистик ба магадлал", "MATHCOUNTS / AMC 8 тэмцээний бэлтгэл"],
      coverLabel: "Хамрагдах сэдвүүд",
    },
  },
  {
    id: "high",
    emoji: "🎓",
    en: {
      label: "High School",
      range: "Grades 9–12 · Ages 14–18",
      description: "We support students through the full high school math sequence and beyond—including advanced courses and test preparation. Our tutors help students excel in class and on standardized exams.",
      topics: ["Algebra I & II", "Geometry", "Pre-Calculus and Trigonometry", "AP Calculus AB / BC", "AP Statistics", "SAT, ACT, and PSAT prep"],
      coverLabel: "Topics we cover",
    },
    mn: {
      label: "Ахлах сургууль",
      range: "9–12-р анги · 14–18 нас",
      description: "Ахлах сургуулийн математикийн бүрэн дарааллыг дэмжиж, дэвшилтэт хичээл, шалгалтын бэлтгэлийг хамарна. Манай багш нар ангид болон стандарт шалгалтад амжилттай байхад тусалдаг.",
      topics: ["Алгебр I ба II", "Геометр", "Урьдcalculus ба тригонометр", "AP Calculus AB / BC", "AP Статистик", "SAT, ACT, PSAT бэлтгэл"],
      coverLabel: "Хамрагдах сэдвүүд",
    },
  },
  {
    id: "college",
    emoji: "🏛️",
    en: {
      label: "College",
      range: "Undergraduate · Ages 18+",
      description: "College-level math can be demanding. We help undergraduates navigate calculus sequences, linear algebra, differential equations, and proof-based courses with confidence.",
      topics: ["Calculus I, II, III", "Linear Algebra", "Differential Equations", "Discrete Mathematics", "Statistics and Probability", "GRE / GMAT Quantitative prep"],
      coverLabel: "Topics we cover",
    },
    mn: {
      label: "Их сургууль",
      range: "Бакалавр · 18+ нас",
      description: "Их сургуулийн математик хүнд байж болно. Calculus, шугаман алгебр, дифференциал тэгшитгэл, баталгаанд суурилсан хичээлүүдийг итгэлтэйгээр давахад тусалдаг.",
      topics: ["Calculus I, II, III", "Шугаман алгебр", "Дифференциал тэгшитгэл", "Дискрет математик", "Статистик ба магадлал", "GRE / GMAT тоон хэсгийн бэлтгэл"],
      coverLabel: "Хамрагдах сэдвүүд",
    },
  },
  {
    id: "adult",
    emoji: "👔",
    en: {
      label: "Adult Learning",
      range: "All ages · Professional & personal goals",
      description: "It's never too late to learn math. Whether you're returning to school, preparing for a professional exam, or simply want to fill gaps from years ago, we meet you exactly where you are.",
      topics: ["Foundational arithmetic and algebra review", "GED Math preparation", "GRE / GMAT prep for career transitions", "Statistics for data and business", "Personalized curriculum for any goal"],
      coverLabel: "Topics we cover",
    },
    mn: {
      label: "Насанд хүрэгчид",
      range: "Бүх нас · Мэргэжлийн ба хувийн зорилго",
      description: "Математик сурахад хэзээ ч хожимдохгүй. Сургуульдаа буцаж байгаа эсэхийг үл хамааран, мэргэжлийн шалгалтанд бэлдэж байгаа эсвэл жилийн өмнөх хоцрогдлоо нөхөхийг хүсч байгаа бол бидэн байнаа.",
      topics: ["Үндсэн арифметик ба алгебрын давталт", "GED математикийн бэлтгэл", "Карьераа өөрчлөхөд GRE / GMAT бэлтгэл", "Өгөгдөл, бизнест зориулсан статистик", "Аливаа зорилгод тохирсон хувийн хөтөлбөр"],
      coverLabel: "Хамрагдах сэдвүүд",
    },
  },
];

export default function CoursesPage() {
  const { lang } = useLang();

  return (
    <>
      {/* Hero */}
      <section className="bg-gradient-to-br from-primary-800 to-primary-600 text-white pt-32 pb-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="badge bg-white/15 text-white mx-auto mb-4">
            <T en="Grade Levels" mn="Ангийн түвшин" />
          </div>
          <h1 className="text-4xl sm:text-5xl font-bold mb-5">
            <T en="Math tutoring for every age group" mn="Бүх насны бүлэгт зориулсан математикийн хичээл" />
          </h1>
          <p className="text-blue-100 text-lg max-w-xl mx-auto">
            <T
              en="We believe everyone can learn. World-class online tutoring from 2nd grade through adulthood."
              mn="Бид хүн бүр суралцах чадвартай гэдэгт итгэдэг. 2-р ангиас насанд хүрэгч хүртэл дэлхийн түвшний онлайн хичээл."
            />
          </p>
        </div>
      </section>

      {/* Jump links */}
      <div className="sticky top-16 z-40 bg-white border-b border-gray-100 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex gap-1 overflow-x-auto py-3 no-scrollbar">
            {levels.map((l) => {
              const content = lang === "mn" ? l.mn : l.en;
              return (
                <a
                  key={l.id}
                  href={`#${l.id}`}
                  className="flex-shrink-0 px-4 py-1.5 rounded-full text-sm font-medium text-gray-600 hover:text-primary-600 hover:bg-primary-50 transition-colors whitespace-nowrap"
                >
                  {l.emoji} {content.label}
                </a>
              );
            })}
          </div>
        </div>
      </div>

      {/* Level sections */}
      <div className="bg-white">
        {levels.map((level, idx) => {
          const content = lang === "mn" ? level.mn : level.en;
          return (
            <section
              key={level.id}
              id={level.id}
              className={`section ${idx % 2 === 0 ? "bg-white" : "bg-gray-50"}`}
            >
              <div className="container-lg">
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                  <div className={idx % 2 !== 0 ? "lg:order-2" : ""}>
                    <div className="text-5xl mb-4">{level.emoji}</div>
                    <div className="badge bg-primary-100 text-primary-700 mb-3">{content.range}</div>
                    <h2 className="text-3xl font-bold text-gray-900 mb-4">{content.label}</h2>
                    <p className="text-gray-600 leading-relaxed mb-6">{content.description}</p>
                    <Link href="/contact" className="btn-primary">
                      <T en="Get Started" mn="Эхлэх" />
                      <ArrowRight className="ml-2 h-4 w-4" />
                    </Link>
                  </div>

                  <div className={idx % 2 !== 0 ? "lg:order-1" : ""}>
                    <div className="card bg-gray-50 border-gray-100">
                      <h3 className="font-semibold text-gray-900 mb-4">{content.coverLabel}</h3>
                      <ul className="space-y-2.5">
                        {content.topics.map((t) => (
                          <li key={t} className="flex items-center gap-2.5 text-sm text-gray-700">
                            <span className="w-1.5 h-1.5 rounded-full bg-primary-500 flex-shrink-0" />
                            {t}
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            </section>
          );
        })}
      </div>

      {/* CTA */}
      <section className="section bg-primary-600">
        <div className="container-lg text-center">
          <h2 className="text-3xl font-bold text-white mb-4">
            <T en="Not sure which program fits?" mn="Ямар хөтөлбөр тохирохыг мэдэхгүй байна уу?" />
          </h2>
          <p className="text-blue-100 mb-8">
            <T
              en="Contact us and we'll recommend the right level and approach for your student."
              mn="Бидэнтэй холбогдоорой, оюутандаа тохирсон түвшин, арга барилыг зөвлөж өгнө."
            />
          </p>
          <Link href="/contact" className="btn-white text-base px-8 py-3.5">
            <T en="Talk to Us" mn="Бидэнтэй ярилцах" />
            <ArrowRight className="ml-2 h-4 w-4" />
          </Link>
        </div>
      </section>
    </>
  );
}
