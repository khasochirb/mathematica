"use client";

import Link from "next/link";
import { ArrowRight, BookOpen, Trophy, Target } from "lucide-react";
import { T } from "@/components/T";
import { useLang } from "@/lib/lang-context";

const exams = [
  {
    id: "sat",
    icon: "📐",
    en: {
      title: "SAT Math",
      description: "Targeted prep covering algebra, advanced math, and problem-solving strategies for College Board's SAT. We focus on the specific question types and time management skills needed to maximize your score.",
      cta: "Start SAT Prep",
    },
    mn: {
      title: "SAT Математик",
      description: "College Board-ийн SAT шалгалтад зориулсан алгебр, дэвшилтэт математик, бодлого шийдэх стратегийг хамарсан зорилтот бэлтгэл. Онооллоо нэмэгдүүлэхэд шаардлагатай асуултын төрөл, цагийн менежментэд анхаарна.",
      cta: "SAT Бэлтгэл эхлэх",
    },
    topics: ["Heart of Algebra", "Passport to Advanced Math", "Additional Topics", "Data Analysis"],
  },
  {
    id: "act",
    icon: "📊",
    en: {
      title: "ACT Math",
      description: "Comprehensive ACT Math prep covering all 60 questions in 60 minutes. We build speed and accuracy across pre-algebra, algebra, coordinate geometry, plane geometry, and trigonometry.",
      cta: "Start ACT Prep",
    },
    mn: {
      title: "ACT Математик",
      description: "60 минутад 60 асуултыг бүрэн хамарсан ACT математикийн бэлтгэл. Урьдалгебр, алгебр, координатын геометр, хавтгай геометр, тригонометрт хурд, нарийвчлалыг хөгжүүлнэ.",
      cta: "ACT Бэлтгэл эхлэх",
    },
    topics: ["Pre-Algebra", "Elementary Algebra", "Intermediate Algebra", "Geometry", "Trigonometry"],
  },
  {
    id: "ap",
    icon: "🎓",
    en: {
      title: "AP Math",
      description: "Rigorous preparation for AP Calculus AB/BC, AP Statistics, and AP Precalculus. We align with College Board's curriculum framework and provide practice with released FRQs and MCQs.",
      cta: "Start AP Prep",
    },
    mn: {
      title: "AP Математик",
      description: "AP Calculus AB/BC, AP Статистик, AP Урьдcalculus-д зориулсан нягт бэлтгэл. College Board-ийн хөтөлбөрийн тогтолцоотой нийцүүлж, гаргасан FRQ, MCQ асуудлуудаар дадлага хийлгэнэ.",
      cta: "AP Бэлтгэл эхлэх",
    },
    topics: ["Calculus AB", "Calculus BC", "Statistics", "Precalculus"],
  },
  {
    id: "ib",
    icon: "🌍",
    en: {
      title: "IB Mathematics",
      description: "Expert support for IB Math AA and IB Math AI at both Standard and Higher Level. Our tutors are experienced with IB's unique internal assessment requirements and exploration projects.",
      cta: "Start IB Prep",
    },
    mn: {
      title: "IB Математик",
      description: "IB Math AA болон IB Math AI-г Standard болон Higher Level-д мэргэжлийн дэмжлэг. Манай багш нар IB-ийн дотоод үнэлгээний шаардлага, судалгааны төслүүдтэй туршлагатай.",
      cta: "IB Бэлтгэл эхлэх",
    },
    topics: ["Analysis & Approaches SL/HL", "Applications & Interpretation SL/HL", "Internal Assessment"],
  },
  {
    id: "olympiad",
    icon: "🏆",
    en: {
      title: "Math Olympiad",
      description: "Specialized training for AMC 8/10/12, AIME, MATHCOUNTS, and international olympiad competitions. We develop problem-solving intuition through classic competition problems and proof techniques.",
      cta: "Start Olympiad Prep",
    },
    mn: {
      title: "Математикийн Олимпиад",
      description: "AMC 8/10/12, AIME, MATHCOUNTS болон олон улсын олимпиадын тэмцээнд зориулсан тусгай сургалт. Сонгодог тэмцээний бодлогууд, баталгаажуулах аргаар бодлого шийдэх зөн совингийг хөгжүүлнэ.",
      cta: "Олимпиадын Бэлтгэл эхлэх",
    },
    topics: ["AMC 8 / 10 / 12", "AIME", "MATHCOUNTS", "USA(J)MO"],
  },
  {
    id: "psat",
    icon: "🎯",
    en: {
      title: "PSAT / NMSQT",
      description: "Strategic PSAT prep for the National Merit Scholarship Qualifying Test. We focus on the exact content areas and difficulty levels of the PSAT to help students qualify for National Merit recognition.",
      cta: "Start PSAT Prep",
    },
    mn: {
      title: "PSAT / NMSQT",
      description: "National Merit тэтгэлэгийн шалгалтад зориулсан стратегийн PSAT бэлтгэл. Оюутнуудыг National Merit-д тэнцэхэд туслахын тулд PSAT-ийн агуулгын хэсэг, хүндрэлийн түвшинд анхаарна.",
      cta: "PSAT Бэлтгэл эхлэх",
    },
    topics: ["Algebra", "Advanced Math", "Problem-Solving", "Data Analysis"],
  },
  {
    id: "gre",
    icon: "📈",
    en: {
      title: "GRE Quant",
      description: "Focused GRE Quantitative Reasoning preparation for graduate school applicants. We cover arithmetic, algebra, geometry, and data analysis, with extensive practice on quantitative comparison and data interpretation.",
      cta: "Start GRE Prep",
    },
    mn: {
      title: "GRE Тоон хэсэг",
      description: "Магистрын сургуульд орохыг хүссэн хүмүүст зориулсан GRE тоон үндэслэлийн бэлтгэл. Арифметик, алгебр, геометр, өгөгдлийн шинжилгээг хамарч, тоон харьцуулалт, өгөгдлийн тайлбар дээр дадлага хийлгэнэ.",
      cta: "GRE Бэлтгэл эхлэх",
    },
    topics: ["Arithmetic", "Algebra", "Geometry", "Data Analysis"],
  },
  {
    id: "gmat",
    icon: "💼",
    en: {
      title: "GMAT Quant",
      description: "Expert GMAT Quantitative preparation for business school candidates. We cover Problem Solving and Data Sufficiency question types with strategies for the GMAT Focus Edition format.",
      cta: "Start GMAT Prep",
    },
    mn: {
      title: "GMAT Тоон хэсэг",
      description: "Бизнесийн сургуульд орохыг хүссэн хүмүүст зориулсан GMAT тоон хэсгийн мэргэжлийн бэлтгэл. GMAT Focus Edition форматын стратегитай Problem Solving, Data Sufficiency асуултын төрлүүдийг хамарна.",
      cta: "GMAT Бэлтгэл эхлэх",
    },
    topics: ["Problem Solving", "Data Sufficiency", "Number Properties", "Statistics"],
  },
  {
    id: "igcse",
    icon: "📚",
    en: {
      title: "IGCSE / GCSE Math",
      description: "Comprehensive preparation for Cambridge IGCSE and GCSE Mathematics at all tiers. We cover the full syllabus and provide past paper practice for both Cambridge and Edexcel specifications.",
      cta: "Start IGCSE Prep",
    },
    mn: {
      title: "IGCSE / GCSE Математик",
      description: "Бүх түвшний Cambridge IGCSE болон GCSE Математикт иж бүрэн бэлтгэл. Кэмбриж болон Edexcel-ийн хөтөлбөрийн дагуу бүрэн хичээлийн төлөвлөгөөг хамарч, өмнөх жилийн даалгаварыг дадлагад ашиглана.",
      cta: "IGCSE Бэлтгэл эхлэх",
    },
    topics: ["Number", "Algebra", "Geometry", "Statistics & Probability"],
  },
];

const whyUs = [
  {
    icon: Target,
    en: { title: "Score-focused approach", desc: "We analyze each exam's exact format and teach the fastest, most reliable strategies for every question type." },
    mn: { title: "Оноонд чиглэсэн арга", desc: "Шалгалт бүрийн яг форматыг задлан шинжилж, асуулт бүрт хамгийн хурдан, найдвартай стратегийг заана." },
  },
  {
    icon: BookOpen,
    en: { title: "Official materials", desc: "Practice with real past papers and official released exams—not generic problem banks." },
    mn: { title: "Албан ёсны материалууд", desc: "Ерөнхий бодлогын санг биш, жинхэнэ өмнөх жилийн шалгалт, албан ёсны материалуудаар дадлага хийнэ." },
  },
  {
    icon: Trophy,
    en: { title: "Proven results", desc: "Students consistently improve their scores by 100+ SAT points or 3+ ACT points within 3 months." },
    mn: { title: "Баталгаат үр дүн", desc: "Оюутнууд 3 сарын дотор SAT-д 100+ оноо, ACT-д 3+ оноогоор тогтмол дэвшдэг." },
  },
];

export default function ExamPrepPage() {
  const { lang } = useLang();

  return (
    <>
      {/* Hero */}
      <section className="bg-gradient-to-br from-primary-900 to-primary-700 text-white pt-32 pb-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="badge bg-white/15 text-white mx-auto mb-4">
            <T en="Exam Preparation" mn="Шалгалтын Бэлтгэл" />
          </div>
          <h1 className="text-4xl sm:text-5xl font-bold mb-5">
            <T en="Ace the exams that matter" mn="Чухал шалгалтуудаа амжилттай өг" />
          </h1>
          <p className="text-blue-100 text-lg max-w-2xl mx-auto leading-relaxed">
            <T
              en="Expert-led preparation for every major math exam—from standardized tests to international olympiads. Our bilingual tutors know exactly what it takes to succeed."
              mn="Стандарт шалгалтаас олон улсын олимпиад хүртэл бүх томоохон математикийн шалгалтад мэргэжилтнийн удирдлагатай бэлтгэл. Манай хоёр хэлтэй багш нар амжилтад хүрэхэд юу шаардлагатайг яг мэддэг."
            />
          </p>
        </div>
      </section>

      {/* Exam cards */}
      <section className="section bg-white">
        <div className="container-lg">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {exams.map((exam) => {
              const content = lang === "mn" ? exam.mn : exam.en;
              return (
                <div
                  key={exam.id}
                  id={exam.id}
                  className="card hover:shadow-lg hover:border-primary-200 transition-all group flex flex-col"
                >
                  <div className="text-4xl mb-4">{exam.icon}</div>
                  <h3 className="text-xl font-bold text-gray-900 mb-3 group-hover:text-primary-600 transition-colors">
                    {content.title}
                  </h3>
                  <p className="text-gray-500 text-sm leading-relaxed mb-4 flex-1">
                    {content.description}
                  </p>
                  <div className="flex flex-wrap gap-2 mb-5">
                    {exam.topics.map((t) => (
                      <span key={t} className="badge bg-primary-50 text-primary-700 text-xs">
                        {t}
                      </span>
                    ))}
                  </div>
                  <Link href="/contact" className="btn-secondary text-sm py-2 text-center">
                    {content.cta}
                    <ArrowRight className="ml-1.5 h-3.5 w-3.5" />
                  </Link>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Why us */}
      <section className="section bg-gray-50">
        <div className="container-lg">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-3">
              <T en="Why Mongol Potential for exam prep?" mn="Яагаад Mongol Potential шалгалтын бэлтгэлд?" />
            </h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {whyUs.map((item) => {
              const Icon = item.icon;
              const content = lang === "mn" ? item.mn : item.en;
              return (
                <div key={item.en.title} className="card text-center">
                  <div className="inline-flex p-3 bg-primary-50 rounded-xl mb-4">
                    <Icon className="h-6 w-6 text-primary-600" />
                  </div>
                  <h3 className="font-bold text-gray-900 mb-2">{content.title}</h3>
                  <p className="text-gray-500 text-sm">{content.desc}</p>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="section bg-primary-600">
        <div className="container-lg text-center">
          <h2 className="text-3xl font-bold text-white mb-4">
            <T en="Ready to start prep?" mn="Бэлтгэл эхлэхэд бэлэн үү?" />
          </h2>
          <p className="text-blue-100 mb-8">
            <T
              en="Book a free consultation and we'll build a personalized study plan for your exam."
              mn="Үнэгүй зөвлөгөө захиалаарай, шалгалтад зориулсан хувийн судалгааны төлөвлөгөө боловсруулна."
            />
          </p>
          <Link href="/contact" className="btn-white text-base px-8 py-3.5">
            <T en="Book Free Consultation" mn="Үнэгүй зөвлөгөө захиалах" />
            <ArrowRight className="ml-2 h-4 w-4" />
          </Link>
        </div>
      </section>
    </>
  );
}
