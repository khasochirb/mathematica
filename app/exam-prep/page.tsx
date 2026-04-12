"use client";

import Link from "next/link";
import {
  ArrowRight,
  BookOpen,
  Clock,
  Target,
  CheckCircle,
  GraduationCap,
  BarChart3,
  ExternalLink,
  Calculator,
  FileText,
  Flame,
} from "lucide-react";
import { T } from "@/components/T";
import { useLang } from "@/lib/lang-context";

const mathTopics = [
  {
    en: { name: "Algebra", detail: "Equations, inequalities, polynomials, systems of equations" },
    mn: { name: "Алгебр", detail: "Тэгшитгэл, тэнцэтгэл биш, олон гишүүнт, тэгшитгэлийн систем" },
    weight: "~25%",
  },
  {
    en: { name: "Functions & Graphs", detail: "Linear, quadratic, exponential, logarithmic, trigonometric functions" },
    mn: { name: "Функц ба график", detail: "Шугаман, квадрат, экспоненциал, логарифм, тригонометрийн функцууд" },
    weight: "~20%",
  },
  {
    en: { name: "Geometry", detail: "Triangles, circles, areas, volumes, coordinate geometry" },
    mn: { name: "Геометр", detail: "Гурвалжин, тойрог, талбай, эзэлхүүн, координатын геометр" },
    weight: "~20%",
  },
  {
    en: { name: "Trigonometry", detail: "Identities, equations, inverse functions, applications" },
    mn: { name: "Тригонометр", detail: "Адилтгалууд, тэгшитгэл, урвуу функц, хэрэглээ" },
    weight: "~10%",
  },
  {
    en: { name: "Calculus", detail: "Limits, derivatives, integrals, applications" },
    mn: { name: "Анализ", detail: "Хязгаар, уламжлал, интеграл, хэрэглээ" },
    weight: "~10%",
  },
  {
    en: { name: "Probability & Statistics", detail: "Combinatorics, probability, descriptive statistics" },
    mn: { name: "Магадлал ба статистик", detail: "Комбинаторик, магадлал, тодорхойлох статистик" },
    weight: "~10%",
  },
  {
    en: { name: "Sequences & Series", detail: "Arithmetic, geometric progressions, limits of sequences" },
    mn: { name: "Дараалал ба цуваа", detail: "Арифметик, геометрийн прогресс, дарааллын хязгаар" },
    weight: "~5%",
  },
];

const timeline = [
  { en: { month: "September–November", task: "Build strong foundations — review all topics, identify weak areas" }, mn: { month: "9–11 сар", task: "Суурь бэхжүүлэх — бүх сэдвийг давтах, сул талуудыг тодорхойлох" } },
  { en: { month: "December–February", task: "Focused practice — drill weak topics, timed practice tests" }, mn: { month: "12–2 сар", task: "Зорилтот дадлага — сул сэдвүүдэд анхаарах, цагтай дадлага шалгалт" } },
  { en: { month: "March–April", task: "Full mock exams — simulate real test conditions, review mistakes" }, mn: { month: "3–4 сар", task: "Бүтэн загвар шалгалт — жинхэнэ нөхцлийг загварчлах, алдааг давтах" } },
  { en: { month: "May (Exam)", task: "Final review — light revision, confidence building, rest" }, mn: { month: "5 сар (Шалгалт)", task: "Эцсийн давталт — хөнгөн давталт, итгэл бий болгох, амрах" } },
];

const resources = [
  {
    en: { name: "Khan Academy — Math", desc: "Free world-class math lessons covering algebra through calculus" },
    mn: { name: "Khan Academy — Математик", desc: "Алгебраас анализ хүртэлх үнэгүй дэлхийн түвшний математик хичээлүүд" },
    url: "https://www.khanacademy.org/math",
    icon: BookOpen,
  },
  {
    en: { name: "3Blue1Brown (YouTube)", desc: "Visual, intuition-building math explanations — great for calculus and linear algebra" },
    mn: { name: "3Blue1Brown (YouTube)", desc: "Визуал, зөн совинд суурилсан математикийн тайлбар — анализ, шугаман алгебрт маш сайн" },
    url: "https://www.youtube.com/@3blue1brown",
    icon: Flame,
  },
  {
    en: { name: "Professor Leonard (YouTube)", desc: "Full university-level math lectures — detailed and beginner-friendly" },
    mn: { name: "Professor Leonard (YouTube)", desc: "Их сургуулийн түвшний бүтэн математик лекцүүд — дэлгэрэнгүй, эхлэгчдэд тохиромжтой" },
    url: "https://www.youtube.com/@ProfessorLeonard",
    icon: GraduationCap,
  },
  {
    en: { name: "Organic Chemistry Tutor (YouTube)", desc: "Step-by-step math problem walkthroughs for every topic" },
    mn: { name: "Organic Chemistry Tutor (YouTube)", desc: "Бүх сэдвээр алхам алхмаар математик бодлого бодох" },
    url: "https://www.youtube.com/@TheOrganicChemistryTutor",
    icon: Calculator,
  },
  {
    en: { name: "Mathway", desc: "Free math problem solver — check your answers step by step" },
    mn: { name: "Mathway", desc: "Үнэгүй математик бодлого шийдэгч — хариултаа алхам алхмаар шалгах" },
    url: "https://www.mathway.com",
    icon: CheckCircle,
  },
];

export default function ExamPrepPage() {
  const { lang } = useLang();

  return (
    <>
      {/* Hero */}
      <section className="relative bg-surface-900 text-white pt-28 pb-20 overflow-hidden">
        <div className="absolute inset-0 bg-grid animate-grid-fade" />
        <div className="absolute inset-0 glow-top-right" />
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative">
          <div className="badge-glow mb-4 mx-auto w-fit">
            <GraduationCap className="h-3.5 w-3.5 mr-1.5 text-primary-400" />
            <T en="ЭЕШ Exam Prep" mn="ЭЕШ шалгалтын бэлтгэл" />
          </div>
          <h1 className="font-display text-4xl sm:text-5xl lg:text-6xl font-bold mb-5">
            <T en="Master the " mn="ЭЕШ Математикийг " />
            <span className="gradient-text">
              <T en="ЭЕШ Math exam" mn="эзэмш" />
            </span>
          </h1>
          <p className="text-gray-400 text-lg max-w-2xl mx-auto leading-relaxed mb-10">
            <T
              en="The ЭЕШ (Элсэлтийн Ерөнхий Шалгалт) is Mongolia's national university entrance exam. Our platform gives you thousands of real-format practice problems, topic breakdowns, and performance tracking to help you score your best."
              mn="ЭЕШ (Элсэлтийн Ерөнхий Шалгалт) бол Монголын их, дээд сургуулийн элсэлтийн шалгалт. Манай платформ танд жинхэнэ форматын мянга мянган дадлагын бодлого, сэдвийн задаргаа, гүйцэтгэлийн хяналтыг өгч, хамгийн өндөр оноо авахад тусална."
            />
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <Link href="/practice/esh" className="btn-primary text-base px-8 py-3.5">
              <T en="Start Practicing Now" mn="Одоо дадлага эхлэх" />
              <ArrowRight className="ml-2 h-4 w-4" />
            </Link>
            <Link href="#math-topics" className="btn-secondary text-base px-8 py-3.5">
              <T en="See Math Topics" mn="Математикийн сэдвүүдийг харах" />
            </Link>
          </div>
        </div>
      </section>

      {/* Exam structure overview */}
      <section className="section-dark">
        <div className="absolute inset-0 bg-grid opacity-50" />
        <div className="container-lg relative">
          <div className="text-center mb-12">
            <div className="badge-glow mb-4 mx-auto w-fit">
              <FileText className="h-3.5 w-3.5 mr-1.5 text-primary-400" />
              <T en="Exam Overview" mn="Шалгалтын тойм" />
            </div>
            <h2 className="font-display text-3xl sm:text-4xl font-bold text-white mb-4">
              <T en="What is the ЭЕШ?" mn="ЭЕШ гэж юу вэ?" />
            </h2>
            <p className="text-gray-400 max-w-2xl mx-auto">
              <T
                en="The Элсэлтийн Ерөнхий Шалгалт (General Entrance Exam) is taken by all Mongolian high school graduates who want to attend university. It is administered annually in May."
                mn="Элсэлтийн Ерөнхий Шалгалт нь их, дээд сургуульд элсэхийг хүссэн бүх Монгол ахлах сургуулийн төгсөгчдөд зориулагдсан. Жил бүрийн 5-р сард зохион байгуулдаг."
              />
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {[
              {
                icon: FileText,
                en: { title: "Format", desc: "Part 1: 30 multiple-choice questions (A–E). Part 2: 10 open-ended problems with written solutions." },
                mn: { title: "Формат", desc: "1-р хэсэг: 30 сонгох бодлого (А–Е). 2-р хэсэг: 10 нээлттэй бодлого, бичгээр бодолтоо харуулна." },
              },
              {
                icon: Clock,
                en: { title: "Duration", desc: "3 hours total. Part 1 and Part 2 are written in one continuous sitting." },
                mn: { title: "Хугацаа", desc: "Нийт 3 цаг. 1-р ба 2-р хэсгийг нэг удаа тасралтгүй бичнэ." },
              },
              {
                icon: BarChart3,
                en: { title: "Scoring", desc: "Total: 800 points. Part 1: ~400 pts (each correct = ~13 pts). Part 2: ~400 pts (partial credit given)." },
                mn: { title: "Оноо", desc: "Нийт: 800 оноо. 1-р хэсэг: ~400 оноо (зөв бүр ~13 оноо). 2-р хэсэг: ~400 оноо (хэсэгчлэн оноо өгнө)." },
              },
              {
                icon: Target,
                en: { title: "Subjects", desc: "Students choose one exam subject. Math is the most popular, required by most STEM and economics programs." },
                mn: { title: "Хичээл", desc: "Сурагчид нэг хичээлийг сонгоно. Математик хамгийн түгээмэл, STEM болон эдийн засгийн ихэнх хөтөлбөрт шаардлагатай." },
              },
            ].map((card) => {
              const Icon = card.icon;
              const content = lang === "mn" ? card.mn : card.en;
              return (
                <div key={card.en.title} className="card-glass-glow border-glow">
                  <div className="inline-flex p-3 rounded-xl bg-primary-500/10 mb-4">
                    <Icon className="h-6 w-6 text-primary-400" />
                  </div>
                  <h3 className="text-lg font-display font-semibold text-white mb-2">{content.title}</h3>
                  <p className="text-gray-400 text-sm leading-relaxed">{content.desc}</p>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Math section breakdown */}
      <section id="math-topics" className="section-darker">
        <div className="absolute inset-0 glow-bottom-left" />
        <div className="container-lg relative">
          <div className="text-center mb-12">
            <div className="badge-glow mb-4 mx-auto w-fit">
              <Calculator className="h-3.5 w-3.5 mr-1.5 text-accent-cyan" />
              <T en="Math Section" mn="Математикийн хэсэг" />
            </div>
            <h2 className="font-display text-3xl sm:text-4xl font-bold text-white mb-4">
              <T en="What the math exam " mn="Математикийн шалгалт юу " />
              <span className="gradient-text">
                <T en="actually covers" mn="хамардаг вэ" />
              </span>
            </h2>
            <p className="text-gray-400 max-w-xl mx-auto">
              <T
                en="The ЭЕШ math exam tests 10–12th grade topics. Here's the approximate weight of each area."
                mn="ЭЕШ математикийн шалгалт нь 10–12-р ангийн сэдвүүдийг шалгадаг. Сэдэв тус бүрийн ойролцоо жин."
              />
            </p>
          </div>

          <div className="max-w-3xl mx-auto space-y-3">
            {mathTopics.map((topic) => {
              const content = lang === "mn" ? topic.mn : topic.en;
              const pct = parseInt(topic.weight.replace(/[^0-9]/g, ""));
              return (
                <div key={topic.en.name} className="card-glass">
                  <div className="flex items-center justify-between mb-2">
                    <h3 className="font-display font-semibold text-gray-200">{content.name}</h3>
                    <span className="text-sm font-bold text-primary-400">{topic.weight}</span>
                  </div>
                  <p className="text-gray-500 text-sm mb-3">{content.detail}</p>
                  <div className="h-2 bg-white/[0.06] rounded-full overflow-hidden">
                    <div
                      className="h-full bg-gradient-to-r from-primary-500 to-accent-cyan rounded-full"
                      style={{ width: `${pct}%` }}
                    />
                  </div>
                </div>
              );
            })}
          </div>

          <div className="text-center mt-8">
            <p className="text-gray-500 text-sm mb-4">
              <T
                en="Difficulty curve: Part 1 questions go from easy (Q1–10) to medium (Q11–20) to hard (Q21–30). Part 2 problems are all challenging and require full written solutions."
                mn="Хүндрэлийн муруй: 1-р хэсгийн бодлогууд хялбар (1–10) → дунд (11–20) → хэцүү (21–30). 2-р хэсгийн бодлогууд бүгд хэцүү, бичгэн бодолт шаарддаг."
              />
            </p>
            <Link href="/courses" className="btn-glow text-base px-8 py-3.5">
              <T en="Study by Topic" mn="Сэдвээр суралцах" />
              <ArrowRight className="ml-2 h-4 w-4" />
            </Link>
          </div>
        </div>
      </section>

      {/* Study timeline */}
      <section className="section-dark">
        <div className="absolute inset-0 glow-top-right" />
        <div className="container-lg relative">
          <div className="text-center mb-12">
            <h2 className="font-display text-3xl sm:text-4xl font-bold text-white mb-4">
              <T en="Recommended study " mn="Санал болгох суралцах " />
              <span className="gradient-text-warm">
                <T en="timeline" mn="хуваарь" />
              </span>
            </h2>
            <p className="text-gray-400 max-w-xl mx-auto">
              <T
                en="A typical 8-month plan for a 12th grader preparing for the May ЭЕШ."
                mn="5-р сарын ЭЕШ-д бэлтгэж буй 12-р ангийн сурагчийн ердийн 8 сарын төлөвлөгөө."
              />
            </p>
          </div>

          <div className="max-w-2xl mx-auto">
            {timeline.map((item, i) => {
              const content = lang === "mn" ? item.mn : item.en;
              const isLast = i === timeline.length - 1;
              return (
                <div key={item.en.month} className="flex gap-4">
                  <div className="flex flex-col items-center">
                    <div className={`w-10 h-10 rounded-xl flex items-center justify-center flex-shrink-0 ${isLast ? "bg-accent-gold/20 border border-accent-gold/30" : "bg-primary-500/15 border border-primary-400/20"}`}>
                      <span className="text-sm font-bold text-primary-300">{i + 1}</span>
                    </div>
                    {!isLast && <div className="w-px h-full bg-white/[0.08] my-1" />}
                  </div>
                  <div className="pb-8">
                    <p className="font-display font-semibold text-white text-sm">{content.month}</p>
                    <p className="text-gray-400 text-sm mt-1">{content.task}</p>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Resources */}
      <section className="section-darker">
        <div className="absolute inset-0 bg-grid opacity-30" />
        <div className="container-lg relative">
          <div className="text-center mb-12">
            <h2 className="font-display text-3xl sm:text-4xl font-bold text-white mb-4">
              <T en="Recommended " mn="Санал болгох " />
              <span className="gradient-text">
                <T en="study resources" mn="нөөцүүд" />
              </span>
            </h2>
            <p className="text-gray-400 max-w-xl mx-auto">
              <T
                en="Free external resources to supplement your ЭЕШ practice. These are the best free math learning tools on the internet."
                mn="ЭЕШ дадлагаа нөхөх үнэгүй гадны нөөцүүд. Интернетийн шилдэг үнэгүй математик суралцах хэрэгслүүд."
              />
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 max-w-4xl mx-auto">
            {resources.map((r) => {
              const Icon = r.icon;
              const content = lang === "mn" ? r.mn : r.en;
              return (
                <a
                  key={r.url}
                  href={r.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="card-glass-glow group flex items-start gap-3"
                >
                  <div className="p-2 bg-primary-500/10 border border-primary-400/10 rounded-lg flex-shrink-0 group-hover:bg-primary-500/20 transition-colors">
                    <Icon className="h-4 w-4 text-primary-400" />
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="font-semibold text-gray-200 text-sm group-hover:text-primary-300 transition-colors flex items-center gap-1.5">
                      {content.name}
                      <ExternalLink className="h-3 w-3 text-gray-600 flex-shrink-0" />
                    </p>
                    <p className="text-gray-500 text-xs mt-0.5 leading-relaxed">{content.desc}</p>
                  </div>
                </a>
              );
            })}
          </div>
        </div>
      </section>

      {/* International exams note */}
      <section className="section-dark">
        <div className="container-lg relative">
          <div className="card-glass max-w-3xl mx-auto text-center">
            <h3 className="font-display text-xl font-bold text-white mb-3">
              <T en="Studying abroad? We also prep for international exams" mn="Гадаадад суралцаж байна уу? Олон улсын шалгалтанд ч бэлтгэдэг" />
            </h3>
            <p className="text-gray-400 text-sm mb-6 max-w-xl mx-auto">
              <T
                en="If you're a Mongolian student preparing for SAT, ACT, AP Calculus, IB Math, or competition math, we offer 1-on-1 tutoring with bilingual instructors."
                mn="Хэрэв та SAT, ACT, AP Calculus, IB Math, эсвэл олимпиадын математикт бэлтгэж байгаа Монгол сурагч бол бид хоёр хэлтэй багш нартай 1-1 хичээл санал болгодог."
              />
            </p>
            <Link href="/tutoring" className="btn-secondary text-sm px-6 py-2.5">
              <T en="Learn About Tutoring" mn="Хичээлийн тухай" />
              <ArrowRight className="ml-1.5 h-3.5 w-3.5" />
            </Link>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="section relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-primary-950 via-primary-900 to-surface-900" />
        <div className="absolute inset-0 bg-grid opacity-30" />
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-primary-500/[0.12] blur-[120px] rounded-full" />
        <div className="container-lg text-center relative">
          <h2 className="font-display text-3xl sm:text-4xl lg:text-5xl font-bold text-white mb-5">
            <T en="Start your ЭЕШ prep " mn="ЭЕШ бэлтгэлээ " />
            <span className="gradient-text">
              <T en="today" mn="өнөөдөр эхлэ" />
            </span>
          </h2>
          <p className="text-gray-400 text-lg mb-10 max-w-xl mx-auto">
            <T
              en="Practice with real ЭЕШ-format problems, track your progress by topic, and focus on your weak areas."
              mn="Жинхэнэ ЭЕШ форматын бодлогуудаар дадлага хийж, сэдвээр дэвшлээ хянаж, сул талуудад анхаар."
            />
          </p>
          <Link href="/practice/esh" className="btn-white text-base px-8 py-3.5">
            <T en="Start Practicing Free" mn="Үнэгүй дадлага эхлэх" />
            <ArrowRight className="ml-2 h-4 w-4" />
          </Link>
        </div>
      </section>
    </>
  );
}
