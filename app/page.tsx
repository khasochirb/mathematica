"use client";

import Link from "next/link";
import {
  BookOpen,
  Trophy,
  Globe,
  Star,
  ArrowRight,
  CheckCircle,
  Brain,
  Flame,
  BarChart3,
  Sparkles,
  Zap,
  Target,
  GraduationCap,
  Users,
  TrendingUp,
} from "lucide-react";
import { T } from "@/components/T";
import { useLang } from "@/lib/lang-context";

const features = [
  {
    icon: BookOpen,
    en: { title: "ЭЕШ & International Exams", description: "Structured prep for Mongolia's ЭЕШ entrance exam plus AP, IB, and SAT—covering every exam Mongolian students face." },
    mn: { title: "ЭЕШ ба олон улсын шалгалт", description: "Монголын ЭЕШ элсэлтийн шалгалт, мөн AP, IB, SAT зэрэг Монгол сурагчдын өгдөг бүх шалгалтын бүтэцтэй бэлтгэл." },
    gradient: "from-primary-500 to-primary-400",
    iconColor: "text-primary-400",
  },
  {
    icon: Globe,
    en: { title: "Personal & Flexible", description: "One-on-one tutoring, AI-powered self-study, flexible scheduling across time zones—goals tailored to each learner." },
    mn: { title: "Хувийн ба уян хатан", description: "Нэг-нэгтэй хичээл, AI-д суурилсан бие даасан суралцах, цагийн бүсийг харгалзсан уян хуваарь—хүн бүрийн зорилгод тохирсон." },
    gradient: "from-accent-cyan to-cyan-400",
    iconColor: "text-accent-cyan",
  },
  {
    icon: Star,
    en: { title: "Made for Mongolians", description: "Problems rooted in Mongolian context, culture, and curriculum—whether you're in Ulaanbaatar or abroad, learning feels relevant." },
    mn: { title: "Монголчуудад зориулсан", description: "Монгол орчин, соёл, хөтөлбөрт суурилсан бодлогууд—Улаанбаатарт ч, гадаадад ч суралцах нь утга учиртай байна." },
    gradient: "from-accent-gold to-amber-400",
    iconColor: "text-accent-gold",
  },
];

const mathlyFeatures = [
  { icon: Brain, en: { label: "Adaptive Problems", desc: "AI adjusts difficulty to your level" }, mn: { label: "Дасан зохицох бодлогууд", desc: "AI таны түвшинд тохирсон хүндрэл тохируулна" } },
  { icon: Flame, en: { label: "Daily Streaks", desc: "Build consistent practice habits" }, mn: { label: "Өдөр тутмын дараалал", desc: "Тогтмол дадлагын дадал бий болго" } },
  { icon: BarChart3, en: { label: "Progress Tracking", desc: "See your growth over time" }, mn: { label: "Дэвшлийн хяналт", desc: "Цаг хугацааны явцад өөрийн өсөлтийг харна" } },
  { icon: Trophy, en: { label: "Achievements", desc: "Earn rewards as you improve" }, mn: { label: "Амжилтууд", desc: "Дэвшихийн хэрээр шагнал авна" } },
];

const grades = [
  { en: { label: "Algebra", range: "~25% of exam" }, mn: { label: "Алгебр", range: "Шалгалтын ~25%" }, href: "/courses#algebra", icon: Sparkles },
  { en: { label: "Functions", range: "~20% of exam" }, mn: { label: "Функц", range: "Шалгалтын ~20%" }, href: "/courses#functions", icon: TrendingUp },
  { en: { label: "Geometry", range: "~20% of exam" }, mn: { label: "Геометр", range: "Шалгалтын ~20%" }, href: "/courses#geometry", icon: Target },
  { en: { label: "Trigonometry", range: "~10% of exam" }, mn: { label: "Тригонометр", range: "Шалгалтын ~10%" }, href: "/courses#trigonometry", icon: Zap },
  { en: { label: "Calculus", range: "~10% of exam" }, mn: { label: "Анализ", range: "Шалгалтын ~10%" }, href: "/courses#calculus", icon: GraduationCap },
];

const testimonials = [
  {
    en: { quote: "My daughter was struggling with math and wasn't confident going to class. Now she finishes her homework without problems.", author: "Misheel's Mom" },
    mn: { quote: "Охин маань математикт хэцүүдэж байсан бөгөөд ангид итгэлтэй явдаггүй байсан. Одоо гэрийн даалгаврыг асуудалгүй дуусгадаг болсон.", author: "Мишээлийн ээж" },
    accent: "primary",
  },
  {
    en: { quote: "She didn't like mathematics at all, but now the first homework she wants to finish is math. She's always excited to join tutoring sessions.", author: "Ari's Mom" },
    mn: { quote: "Математикийг огт дургүй байсан, харин одоо хамгийн түрүүнд математикийн гэрийн даалгавраа хийдэг болсон. Хичээлдээ үргэлж тэсэн ядан яардаг.", author: "Арийн ээж" },
    accent: "cyan",
  },
  {
    en: { quote: "Our son loves going to school already knowing the material and coming back with interesting questions for the tutor.", author: "Subedei's Mom" },
    mn: { quote: "Хүү маань сургуульд материалаа мэдэж очиж, багшид сонирхолтой асуултуудтай эргэж ирдэгт дуртай болсон.", author: "Субэдэйн ээж" },
    accent: "gold",
  },
];

const examTypes = ["ЭЕШ Математик", "SAT Math", "ACT Math", "AP Calculus", "IB Math", "Math Olympiad", "GRE Quant", "PSAT / NMSQT"];


export default function HomePage() {
  const { lang } = useLang();

  return (
    <>
      {/* ─── HERO ─── */}
      <section className="relative bg-surface-900 text-white pt-28 pb-28 overflow-hidden">
        {/* Background effects */}
        <div className="absolute inset-0 bg-grid animate-grid-fade" />
        <div className="absolute inset-0 glow-top-right" />
        <div className="absolute inset-0 glow-bottom-left" />
        <div className="absolute top-20 left-[10%] w-72 h-72 rounded-full bg-primary-500/[0.07] blur-[100px] animate-float" />
        <div className="absolute bottom-20 right-[15%] w-64 h-64 rounded-full bg-accent-cyan/[0.06] blur-[80px] animate-float-delayed" />
        <div className="mongolian-vertical">ᠮᠣᠩᠭᠣᠯ ᠫᠣᠲ᠋ᠧᠨᠼᠢᠶᠠᠯ ᠠᠻᠠᠳ᠋ᠧᠮᠢ</div>

        {/* Decorative geometric elements */}
        <div className="absolute top-32 right-[20%] w-px h-32 bg-gradient-to-b from-primary-500/30 to-transparent hidden lg:block" />
        <div className="absolute top-48 right-[20%] w-16 h-px bg-gradient-to-r from-primary-500/30 to-transparent hidden lg:block" />
        <div className="absolute bottom-40 left-[8%] w-3 h-3 rounded-full border border-accent-cyan/30 hidden lg:block animate-glow-pulse" />
        <div className="absolute top-40 left-[30%] w-2 h-2 rounded-full bg-primary-400/30 hidden lg:block" />

        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-3xl">
            <div className="badge-glow mb-6">
              <Sparkles className="h-3.5 w-3.5 mr-1.5 text-primary-400" />
              <span className="text-sm">
                <T en="ЭЕШ Prep & Math Education for All Mongolians" mn="ЭЕШ бэлтгэл ба бүх Монголчуудад зориулсан математик" />
              </span>
            </div>

            <h1 className="font-display text-5xl sm:text-6xl lg:text-7xl font-bold leading-[1.1] mb-6 tracking-tight">
              <T en="High-quality math for" mn="Бүх Монгол сурагчдад" />{" "}
              <span className="gradient-text">
                <T en="every Mongolian student" mn="өндөр чанартай математик" />
              </span>
            </h1>

            <p className="text-lg sm:text-xl text-gray-400 leading-relaxed mb-10 max-w-2xl">
              <T
                en="Ace the ЭЕШ with thousands of practice problems, or get one-on-one tutoring for AP, IB, SAT, and more. Built by Mongolians, for Mongolians—wherever you study."
                mn="Мянга мянган дадлагын бодлогоор ЭЕШ-д бэлтгэ, эсвэл AP, IB, SAT зэрэг шалгалтанд нэг-нэгтэй хичээл ав. Монголчуудаас Монголчуудад—хаана ч сурч байсан."
              />
            </p>

            <div className="flex flex-wrap gap-4">
              <Link href="/practice/esh" className="btn-primary text-base px-8 py-3.5">
                <T en="Start ЭЕШ Prep" mn="ЭЕШ бэлтгэл эхлэх" />
                <ArrowRight className="ml-2 h-4 w-4" />
              </Link>
              <Link href="/tutoring" className="btn-secondary text-base px-8 py-3.5">
                <T en="Find a Tutor" mn="Багшаа олох" />
              </Link>
            </div>

            <div className="mt-10 flex flex-wrap gap-6 text-sm text-gray-500">
              {[
                { en: "Free ЭЕШ practice problems", mn: "Үнэгүй ЭЕШ дадлагын бодлогууд" },
                { en: "1-on-1 tutoring available", mn: "Нэг-нэгтэй хичээл боломжтой" },
                { en: "Works anywhere in the world", mn: "Дэлхийн хаанаас ч ажилладаг" },
              ].map((item) => (
                <span key={item.en} className="flex items-center gap-1.5">
                  <CheckCircle className="h-4 w-4 text-accent-emerald" />
                  <span className="text-gray-400">{lang === "mn" ? item.mn : item.en}</span>
                </span>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* ─── MISSION / FEATURES ─── */}
      <section className="section-dark">
        <div className="absolute inset-0 bg-grid opacity-50" />
        <div className="container-lg relative">
          <div className="text-center mb-16">
            <div className="badge-glow mb-4 mx-auto w-fit">
              <T en="Our Mission" mn="Бидний зорилго" />
            </div>
            <h2 className="font-display text-3xl sm:text-4xl lg:text-5xl font-bold text-white mb-5">
              <T en="Empowering Mongolian students" mn="Монгол сурагчдыг чадавхжуулж" />{" "}
              <span className="gradient-text-warm">
                <T en="everywhere" mn="хаана ч байсан" />
              </span>
            </h2>
            <p className="text-gray-400 max-w-2xl mx-auto text-lg leading-relaxed">
              <T
                en="Whether you're preparing for the ЭЕШ in Ulaanbaatar, studying at an international school, or growing up abroad—every Mongolian student deserves world-class math education and the confidence to succeed."
                mn="Улаанбаатарт ЭЕШ-д бэлтгэж байгаа ч, олон улсын сургуульд суралцаж байгаа ч, гадаадад өсч байгаа ч—Монгол сурагч бүр дэлхийн түвшний математикийн боловсрол, амжилтанд хүрэх итгэлийг авах эрхтэй."
              />
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {features.map((f) => {
              const Icon = f.icon;
              const content = lang === "mn" ? f.mn : f.en;
              return (
                <div key={f.en.title} className="card-glass-glow group border-glow">
                  <div className={`inline-flex p-3 rounded-xl bg-gradient-to-br ${f.gradient} bg-opacity-10 mb-5`}>
                    <Icon className="h-6 w-6 text-white" />
                  </div>
                  <h3 className="text-lg font-display font-semibold text-white mb-3 group-hover:text-primary-300 transition-colors">
                    {content.title}
                  </h3>
                  <p className="text-gray-400 text-sm leading-relaxed">{content.description}</p>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* ─── AI PRACTICE PLATFORM ─── */}
      <section className="section-darker">
        <div className="absolute inset-0 glow-bottom-left" />
        <div className="container-lg relative">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div>
              <div className="badge-glow mb-4">
                <Zap className="h-3.5 w-3.5 mr-1.5 text-accent-cyan" />
                <T en="AI-Powered Practice" mn="AI-д суурилсан дадлага" />
              </div>
              <h2 className="font-display text-3xl sm:text-4xl font-bold text-white mb-5">
                <T en="Practice math with " mn="Дасан зохицох " />
                <span className="gradient-text">
                  <T en="adaptive AI" mn="AI-тай математик дадла" />
                </span>
              </h2>
              <p className="text-gray-400 text-lg leading-relaxed mb-8">
                <T
                  en="Our Mathly practice platform adapts to your level, giving you problems that challenge you just the right amount. Get AI-powered hints, track your streaks, and earn achievements as you improve."
                  mn="Mathly дадлагын платформ таны түвшинд дасан зохицож, яг хангалттай хэмжээгээр танд сорилт болсон бодлогуудыг өгдөг. AI-ийн зөвлөмж авч, дараалалаа хянаж, дэвшихийн хэрээр амжилтаа цуглуул."
                />
              </p>

              <div className="grid grid-cols-2 gap-4 mb-8">
                {mathlyFeatures.map((f) => {
                  const Icon = f.icon;
                  const content = lang === "mn" ? f.mn : f.en;
                  return (
                    <div key={f.en.label} className="flex items-start gap-3 group">
                      <div className="p-2 bg-primary-500/10 border border-primary-400/10 rounded-lg flex-shrink-0 group-hover:bg-primary-500/20 transition-colors">
                        <Icon className="h-4 w-4 text-primary-400" />
                      </div>
                      <div>
                        <p className="font-semibold text-gray-200 text-sm">{content.label}</p>
                        <p className="text-gray-500 text-xs">{content.desc}</p>
                      </div>
                    </div>
                  );
                })}
              </div>

              <Link href="/practice" className="btn-glow text-base px-8 py-3.5">
                <T en="Start Practicing Free" mn="Үнэгүй дадлага эхлэх" />
                <ArrowRight className="ml-2 h-4 w-4" />
              </Link>
            </div>

            {/* Practice card preview */}
            <div className="relative">
              <div className="card-glass border-glow p-0 overflow-hidden">
                <div className="p-6">
                  <div className="flex items-center justify-between mb-4">
                    <div>
                      <p className="text-xs text-gray-500 font-medium tracking-wider">ALGEBRA &middot; LEVEL 3</p>
                      <p className="font-semibold text-gray-200 text-sm mt-0.5">
                        <T en="Problem 4 of 10" mn="4-р бодлого / 10-аас" />
                      </p>
                    </div>
                    <div className="flex items-center gap-3">
                      <span className="text-orange-400 font-bold text-sm flex items-center gap-1">
                        <Flame className="h-3.5 w-3.5" /> 7
                      </span>
                      <span className="text-primary-400 font-bold text-sm flex items-center gap-1">
                        <Star className="h-3.5 w-3.5" /> 420 XP
                      </span>
                    </div>
                  </div>
                  <div className="h-1.5 bg-white/[0.06] rounded-full mb-6">
                    <div className="h-full w-2/5 bg-gradient-to-r from-primary-500 to-accent-cyan rounded-full" />
                  </div>
                  <div className="bg-white/[0.04] border border-white/[0.06] rounded-xl p-4 mb-4">
                    <p className="text-gray-200 font-medium text-sm leading-relaxed">
                      If 3x + 7 = 22, what is the value of 6x − 4?
                    </p>
                  </div>
                  <div className="grid grid-cols-2 gap-2 mb-4">
                    {["A. 20", "B. 26", "C. 30", "D. 34"].map((opt, i) => (
                      <button
                        key={opt}
                        className={`px-3 py-2.5 rounded-xl text-sm font-medium border transition-all text-left ${
                          i === 1
                            ? "bg-primary-500/20 text-primary-300 border-primary-400/30"
                            : "border-white/[0.08] text-gray-400 hover:border-primary-400/20 hover:bg-primary-500/5"
                        }`}
                      >
                        {opt}
                      </button>
                    ))}
                  </div>
                  <button className="w-full btn-primary py-2.5 text-sm">
                    <T en="Submit Answer" mn="Хариулт илгээх" />
                  </button>
                </div>
              </div>
              {/* Floating XP badge */}
              <div className="absolute -top-3 -right-3 bg-gradient-to-r from-accent-gold to-orange-400 text-white rounded-xl px-3 py-1.5 text-xs font-bold shadow-lg shadow-accent-gold/30">
                +15 XP
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ─── EXAM PREP ─── */}
      <section className="section-dark">
        <div className="absolute inset-0 glow-top-right" />
        <div className="container-lg relative">
          <div className="text-center mb-12">
            <div className="badge-glow mb-4 mx-auto w-fit">
              <GraduationCap className="h-3.5 w-3.5 mr-1.5 text-primary-400" />
              <T en="Test Preparation" mn="Шалгалтын бэлтгэл" />
            </div>
            <h2 className="font-display text-3xl sm:text-4xl font-bold text-white mb-4">
              <T en="ЭЕШ and exam prep " mn="ЭЕШ болон шалгалтын бэлтгэл " />
              <span className="gradient-text">
                <T en="you can trust" mn="найдаж болохуйц" />
              </span>
            </h2>
            <p className="text-gray-400 max-w-xl mx-auto">
              <T
                en="Thousands of real ЭЕШ-style problems with step-by-step solutions, plus expert prep for SAT, AP, IB, and other international exams."
                mn="Мянга мянган жинхэнэ ЭЕШ маягийн бодлогууд алхам алхмаар бодолттой, мөн SAT, AP, IB зэрэг олон улсын шалгалтын мэргэжлийн бэлтгэл."
              />
            </p>
          </div>
          <div className="flex flex-wrap justify-center gap-3 mb-10">
            {examTypes.map((exam) => (
              <Link
                key={exam}
                href="/exam-prep"
                className="px-5 py-2.5 bg-primary-500/10 text-primary-300 border border-primary-400/15 rounded-xl text-sm font-medium hover:bg-primary-500/20 hover:border-primary-400/30 transition-all duration-300"
              >
                {exam}
              </Link>
            ))}
          </div>
          <div className="text-center">
            <Link href="/exam-prep" className="btn-primary text-base">
              <T en="View All Exam Programs" mn="Бүх шалгалтын хөтөлбөрийг харах" />
              <ArrowRight className="ml-2 h-4 w-4" />
            </Link>
          </div>
        </div>
      </section>

      {/* ─── GRADE LEVELS ─── */}
      <section className="section-darker">
        <div className="absolute inset-0 bg-grid opacity-30" />
        <div className="container-lg relative">
          <div className="text-center mb-12">
            <h2 className="font-display text-3xl sm:text-4xl font-bold text-white mb-4">
              <T en="Practice by " mn="Сэдвээр " />
              <span className="gradient-text">
                <T en="topic" mn="дадлага хийх" />
              </span>
            </h2>
            <p className="text-gray-400 max-w-lg mx-auto">
              <T
                en="The ЭЕШ math exam covers these core areas. Pick any topic and start practicing right away."
                mn="ЭЕШ математикийн шалгалт эдгээр үндсэн чиглэлүүдийг хамардаг. Аль ч сэдвийг сонгоод шууд дадлага хий."
              />
            </p>
          </div>
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-4">
            {grades.map((g) => {
              const content = lang === "mn" ? g.mn : g.en;
              const Icon = g.icon;
              return (
                <Link
                  key={g.href}
                  href={g.href}
                  className="card-glass-glow text-center group"
                >
                  <div className="inline-flex p-2.5 rounded-xl bg-primary-500/10 mb-3 group-hover:bg-primary-500/20 transition-colors">
                    <Icon className="h-5 w-5 text-primary-400" />
                  </div>
                  <p className="font-display font-semibold text-gray-200 group-hover:text-primary-300 transition-colors">
                    {content.label}
                  </p>
                  <p className="text-gray-500 text-xs mt-1">{content.range}</p>
                </Link>
              );
            })}
          </div>
        </div>
      </section>

      {/* ─── TESTIMONIALS ─── */}
      <section className="section-dark">
        <div className="absolute inset-0 glow-bottom-left" />
        <div className="container-lg relative">
          <div className="text-center mb-12">
            <div className="badge-glow mb-4 mx-auto w-fit">
              <Users className="h-3.5 w-3.5 mr-1.5 text-primary-400" />
              <T en="Testimonials" mn="Санал сэтгэгдэл" />
            </div>
            <h2 className="font-display text-3xl sm:text-4xl font-bold text-white mb-4">
              <T en="Success stories from " mn="Манай оюутнуудын " />
              <span className="gradient-text">
                <T en="our students" mn="амжилтын түүхүүд" />
              </span>
            </h2>
            <p className="text-gray-400">
              <T en="Real words from Mongolian families using our tutoring service" mn="Манай хичээлийн үйлчилгээг ашиглаж буй Монгол гэр бүлүүдийн жинхэнэ үгс" />
            </p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {testimonials.map((t) => {
              const content = lang === "mn" ? t.mn : t.en;
              const borderColor =
                t.accent === "primary" ? "border-l-primary-500/60" :
                t.accent === "cyan" ? "border-l-accent-cyan/60" :
                "border-l-accent-gold/60";
              return (
                <div
                  key={t.en.author}
                  className={`card-glass border-l-2 ${borderColor}`}
                >
                  <p className="text-gray-300 leading-relaxed mb-5 text-sm italic">&ldquo;{content.quote}&rdquo;</p>
                  <p className="font-display font-semibold text-gray-200 text-sm">&mdash; {content.author}</p>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* ─── CTA ─── */}
      <section className="section relative overflow-hidden">
        {/* Background */}
        <div className="absolute inset-0 bg-gradient-to-br from-primary-950 via-primary-900 to-surface-900" />
        <div className="absolute inset-0 bg-grid opacity-30" />
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-primary-500/[0.12] blur-[120px] rounded-full" />

        <div className="container-lg text-center relative">
          <h2 className="font-display text-3xl sm:text-4xl lg:text-5xl font-bold text-white mb-5">
            <T en="Ready to " mn="Боломжоо нээхэд " />
            <span className="gradient-text">
              <T en="reach your potential?" mn="бэлэн үү?" />
            </span>
          </h2>
          <p className="text-gray-400 text-lg mb-10 max-w-xl mx-auto">
            <T
              en="Join thousands of Mongolian students who are mastering math—from ЭЕШ prep to international exams and beyond."
              mn="Математикийг эзэмшиж буй мянга мянган Монгол сурагчидтай нэгдээрэй—ЭЕШ бэлтгэлээс олон улсын шалгалт хүртэл."
            />
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <Link href="/practice/esh" className="btn-white text-base px-8 py-3.5">
              <T en="Start ЭЕШ Prep" mn="ЭЕШ бэлтгэл эхлэх" />
              <ArrowRight className="ml-2 h-4 w-4" />
            </Link>
            <Link href="/tutoring" className="btn-secondary text-base px-8 py-3.5">
              <T en="Find a Tutor" mn="Багшаа олох" />
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
