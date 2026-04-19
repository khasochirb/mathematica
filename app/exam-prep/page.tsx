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
import { useLang } from "@/lib/lang-context";

const mathTopics = [
  {
    en: { name: "Algebra", detail: "Equations, inequalities, polynomials, systems of equations" },
    mn: { name: "Алгебр", detail: "Тэгшитгэл, тэнцэтгэл биш, олон гишүүнт, тэгшитгэлийн систем" },
    weight: 25,
  },
  {
    en: { name: "Functions & Graphs", detail: "Linear, quadratic, exponential, logarithmic, trigonometric functions" },
    mn: { name: "Функц ба график", detail: "Шугаман, квадрат, экспоненциал, логарифм, тригонометрийн функцууд" },
    weight: 20,
  },
  {
    en: { name: "Geometry", detail: "Triangles, circles, areas, volumes, coordinate geometry" },
    mn: { name: "Геометр", detail: "Гурвалжин, тойрог, талбай, эзэлхүүн, координатын геометр" },
    weight: 20,
  },
  {
    en: { name: "Trigonometry", detail: "Identities, equations, inverse functions, applications" },
    mn: { name: "Тригонометр", detail: "Адилтгалууд, тэгшитгэл, урвуу функц, хэрэглээ" },
    weight: 10,
  },
  {
    en: { name: "Calculus", detail: "Limits, derivatives, integrals, applications" },
    mn: { name: "Анализ", detail: "Хязгаар, уламжлал, интеграл, хэрэглээ" },
    weight: 10,
  },
  {
    en: { name: "Probability & Statistics", detail: "Combinatorics, probability, descriptive statistics" },
    mn: { name: "Магадлал ба статистик", detail: "Комбинаторик, магадлал, тодорхойлох статистик" },
    weight: 10,
  },
  {
    en: { name: "Sequences & Series", detail: "Arithmetic, geometric progressions, limits of sequences" },
    mn: { name: "Дараалал ба цуваа", detail: "Арифметик, геометрийн прогресс, дарааллын хязгаар" },
    weight: 5,
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
          <Link href="#math-topics" className="btn btn-line">
            {t("See math topics", "Математикийн сэдвүүдийг харах")}
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

      {/* Math topics */}
      <section id="math-topics" className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12" style={{ borderTop: "1px solid var(--line)" }}>
        <div className="mb-8">
          <div className="eyebrow mb-3">{t("02 · Topic weights", "02 · Сэдвийн жин")}</div>
          <h2 className="serif" style={{ fontWeight: 400, fontSize: "clamp(32px, 4.5vw, 52px)", letterSpacing: "-0.03em", color: "var(--fg)" }}>
            {t("What the math exam ", "Математикийн шалгалт ")}
            <em className="serif-italic" style={{ color: "var(--accent)" }}>{t("actually covers", "юу хамардаг вэ")}</em>
            {t(".", "")}
          </h2>
          <p className="serif mt-4 max-w-2xl" style={{ fontSize: 16, lineHeight: 1.55, color: "var(--fg-1)" }}>
            {t(
              "Tests grades 10–12 material. Approximate weight per area, by historical exam analysis.",
              "10–12-р ангийн материалаас. Шалгалтын түүхэн анализаас гарсан ойролцоо жин.",
            )}
          </p>
        </div>

        <div className="card-edit p-2 max-w-3xl">
          {mathTopics.map((topic, i) => {
            const content = lang === "mn" ? topic.mn : topic.en;
            return (
              <div
                key={topic.en.name}
                className="p-4"
                style={{ borderBottom: i < mathTopics.length - 1 ? "1px solid var(--line)" : "none" }}
              >
                <div className="flex items-baseline justify-between mb-2 gap-4">
                  <div className="flex items-baseline gap-3 min-w-0">
                    <span className="mono text-[10px]" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                      {String(i + 1).padStart(2, "0")}
                    </span>
                    <h3 className="serif" style={{ fontWeight: 400, fontSize: 18, letterSpacing: "-0.01em", color: "var(--fg)" }}>
                      {content.name}
                    </h3>
                  </div>
                  <div className="serif tabular flex items-baseline gap-1 flex-shrink-0">
                    <span style={{ fontSize: 22, color: "var(--accent)", letterSpacing: "-0.02em" }}>{topic.weight}</span>
                    <span className="mono text-[10px]" style={{ color: "var(--fg-3)" }}>%</span>
                  </div>
                </div>
                <p className="text-[13px] mb-3" style={{ color: "var(--fg-2)" }}>{content.detail}</p>
                <div className="h-[3px] rounded-full overflow-hidden" style={{ background: "var(--bg-2)" }}>
                  <div className="h-full rounded-full" style={{ width: `${topic.weight * 4}%`, background: "var(--accent)" }} />
                </div>
              </div>
            );
          })}
        </div>

        <div className="mt-6 max-w-3xl">
          <p className="text-[13px]" style={{ color: "var(--fg-3)" }}>
            {t(
              "Difficulty curve: Part 1 ramps easy → medium → hard (Q1–10, 11–20, 21–30). Part 2 is uniformly challenging and requires written solutions.",
              "Хүндрэлийн муруй: 1-р хэсэг хялбар → дунд → хэцүү (1–10, 11–20, 21–30). 2-р хэсэг бүгд хэцүү, бичгэн бодолт шаарддаг.",
            )}
          </p>
          <Link href="/courses" className="btn btn-line mt-5">
            {t("Study by topic", "Сэдвээр суралцах")}
            <ArrowRight className="ml-1 h-3.5 w-3.5" />
          </Link>
        </div>
      </section>

      {/* Timeline */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12" style={{ borderTop: "1px solid var(--line)" }}>
        <div className="mb-8">
          <div className="eyebrow mb-3">{t("03 · Study timeline", "03 · Суралцах хуваарь")}</div>
          <h2 className="serif" style={{ fontWeight: 400, fontSize: "clamp(32px, 4.5vw, 52px)", letterSpacing: "-0.03em", color: "var(--fg)" }}>
            {t("An eight-month ", "Найман сарын ")}
            <em className="serif-italic" style={{ color: "var(--accent)" }}>{t("plan", "төлөвлөгөө")}</em>
            .
          </h2>
          <p className="serif mt-4 max-w-2xl" style={{ fontSize: 16, lineHeight: 1.55, color: "var(--fg-1)" }}>
            {t(
              "A typical pacing for a 12th grader preparing for the May ЭЕШ.",
              "5-р сарын ЭЕШ-д бэлтгэж буй 12-р ангийн сурагчийн ердийн төлөвлөгөө.",
            )}
          </p>
        </div>

        <div className="max-w-2xl">
          {timeline.map((item, i) => {
            const content = lang === "mn" ? item.mn : item.en;
            const isLast = i === timeline.length - 1;
            return (
              <div key={item.en.month} className="flex gap-4">
                <div className="flex flex-col items-center">
                  <div
                    className="w-10 h-10 rounded-md flex items-center justify-center flex-shrink-0 mono tabular text-[13px]"
                    style={{
                      background: isLast ? "var(--accent-wash)" : "var(--bg-2)",
                      border: `1px solid ${isLast ? "var(--accent-line)" : "var(--line)"}`,
                      color: isLast ? "var(--accent)" : "var(--fg-2)",
                    }}
                  >
                    {String(i + 1).padStart(2, "0")}
                  </div>
                  {!isLast && <div className="w-px flex-1 my-1" style={{ background: "var(--line)" }} />}
                </div>
                <div className="pb-8">
                  <p className="serif" style={{ fontWeight: 400, fontSize: 18, color: "var(--fg)" }}>{content.month}</p>
                  <p className="text-[14px] mt-1" style={{ color: "var(--fg-2)" }}>{content.task}</p>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {/* Resources */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12" style={{ borderTop: "1px solid var(--line)" }}>
        <div className="mb-8">
          <div className="eyebrow mb-3">{t("04 · External resources", "04 · Гадны нөөц")}</div>
          <h2 className="serif" style={{ fontWeight: 400, fontSize: "clamp(32px, 4.5vw, 52px)", letterSpacing: "-0.03em", color: "var(--fg)" }}>
            {t("Recommended ", "Санал болгох ")}
            <em className="serif-italic" style={{ color: "var(--accent)" }}>{t("study tools", "хэрэгслүүд")}</em>
            .
          </h2>
          <p className="serif mt-4 max-w-2xl" style={{ fontSize: 16, lineHeight: 1.55, color: "var(--fg-1)" }}>
            {t(
              "Free external resources to supplement your ЭЕШ practice — the best free math learning tools on the internet.",
              "ЭЕШ дадлагаа нөхөх үнэгүй гадны нөөцүүд — интернетийн шилдэг үнэгүй математик хэрэгслүүд.",
            )}
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {resources.map((r) => {
            const Icon = r.icon;
            const content = lang === "mn" ? r.mn : r.en;
            return (
              <a
                key={r.url}
                href={r.url}
                target="_blank"
                rel="noopener noreferrer"
                className="card-edit p-5 flex items-start gap-3 group"
              >
                <div
                  className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0"
                  style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
                >
                  <Icon className="h-4 w-4" />
                </div>
                <div className="flex-1 min-w-0">
                  <p className="serif flex items-center gap-1.5" style={{ fontWeight: 400, fontSize: 16, color: "var(--fg)" }}>
                    <span className="truncate">{content.name}</span>
                    <ExternalLink className="h-3 w-3 flex-shrink-0" style={{ color: "var(--fg-3)" }} />
                  </p>
                  <p className="text-[12px] mt-1 leading-relaxed" style={{ color: "var(--fg-2)" }}>{content.desc}</p>
                </div>
              </a>
            );
          })}
        </div>
      </section>

      {/* International */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12" style={{ borderTop: "1px solid var(--line)" }}>
        <div className="card-edit p-8 sm:p-10 max-w-3xl mx-auto text-center">
          <div className="eyebrow mb-3">{t("Beyond the ЭЕШ", "ЭЕШ-аас гадна")}</div>
          <h3 className="serif" style={{ fontWeight: 400, fontSize: "clamp(24px, 3vw, 32px)", letterSpacing: "-0.02em", color: "var(--fg)" }}>
            {t("Studying abroad? We prep ", "Гадаадад суралцаж байна уу? Олон улсын ")}
            <em className="serif-italic" style={{ color: "var(--accent)" }}>{t("international exams", "шалгалтанд ч")}</em>
            {t(" too.", " бэлтгэдэг.")}
          </h3>
          <p className="text-[14px] mt-3 max-w-xl mx-auto" style={{ color: "var(--fg-2)" }}>
            {t(
              "SAT, ACT, AP Calculus, IB Math — native problem coverage of every curriculum, in Mongolian or English.",
              "SAT, ACT, AP Calculus, IB Math — хөтөлбөр бүрд зориулсан бодлогын сан, Монгол эсвэл Англи хэлээр.",
            )}
          </p>
          <Link href="/courses" className="btn btn-line mt-5 inline-flex">
            {t("Browse curricula", "Хөтөлбөр үзэх")}
            <ArrowRight className="ml-1 h-3.5 w-3.5" />
          </Link>
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
