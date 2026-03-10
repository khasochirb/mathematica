"use client";

import Link from "next/link";
import { ArrowRight, CheckCircle, Clock, Globe, Star } from "lucide-react";
import { T } from "@/components/T";
import { useLang } from "@/lib/lang-context";

const benefits = [
  { en: "Sessions scheduled around your time zone", mn: "Таны цагийн бүсэд тохирсон хуваарь" },
  { en: "Tutors fluent in English and Mongolian", mn: "Англи, Монгол хэлд чөлөөтэй багш нар" },
  { en: "Curriculum-aligned to AP, IB, US state standards", mn: "AP, IB, АНУ-ын стандартад нийцсэн хөтөлбөр" },
  { en: "Progress reports after every session", mn: "Хичээл бүрийн дараах дэвшлийн тайлан" },
  { en: "Flexible cancellation with 24-hour notice", mn: "24 цагийн урьдчилсан мэдэгдэлтэй уян хатан цуцлалт" },
  { en: "Free introductory session available", mn: "Үнэгүй танилцах хичээл боломжтой" },
];

const subjects = [
  { name: "Algebra I & II", en: "Middle–High School", mn: "Дунд–Ахлах сургууль" },
  { name: "Geometry", en: "Middle–High School", mn: "Дунд–Ахлах сургууль" },
  { name: "Pre-Calculus", en: "High School", mn: "Ахлах сургууль" },
  { name: "Calculus AB/BC", en: "AP / High School", mn: "AP / Ахлах сургууль" },
  { name: "Statistics", en: "AP / High School", mn: "AP / Ахлах сургууль" },
  { name: "SAT / ACT Math", en: "Test Prep", mn: "Шалгалтын бэлтгэл" },
  { name: "IB Mathematics", en: "IB Diploma", mn: "IB Диплом" },
  { name: "Math Olympiad", en: "Competition", mn: "Олимпиад" },
  { name: "Elementary Math", en: "Grades 2–5", mn: "2–5-р анги" },
  { name: "Middle School Math", en: "Grades 6–8", mn: "6–8-р анги" },
];

const steps = [
  {
    step: "1",
    en: { title: "Tell us about your needs", desc: "Fill out a short form about your grade, goals, and schedule." },
    mn: { title: "Хэрэгцээгээ хэлнэ үү", desc: "Ангийн түвшин, зорилго, хуваарийн талаарх богино маягтыг бөглөнө үү." },
  },
  {
    step: "2",
    en: { title: "Get matched with a tutor", desc: "We pair you with a bilingual tutor who fits your curriculum and timezone." },
    mn: { title: "Багштай тааруулна", desc: "Хөтөлбөр, цагийн бүстэй тохирсон хоёр хэлтэй багштай холбоно." },
  },
  {
    step: "3",
    en: { title: "Start your free intro session", desc: "Meet your tutor, set goals, and experience our approach—at no cost." },
    mn: { title: "Үнэгүй танилцах хичээл эхлэх", desc: "Багштайгаа танилцаж, зорилго тавьж, арга барилыг туршиж үзнэ—үнэгүй." },
  },
  {
    step: "4",
    en: { title: "Build a weekly routine", desc: "Consistent 1-on-1 sessions that track progress and adapt to your growth." },
    mn: { title: "7 хоногийн дэглэм бий болго", desc: "Дэвшлийг хянаж, өсөлтөд дасан зохицох тогтмол 1:1 хичээлүүд." },
  },
];

const stats = [
  { value: "500+", en: "Students Helped", mn: "Тусалсан оюутан" },
  { value: "4.9★", en: "Average Rating", mn: "Дундаж үнэлгээ" },
  { value: "15+", en: "Subjects Covered", mn: "Хамрагдсан хичээл" },
  { value: "100%", en: "Bilingual Sessions", mn: "Хоёр хэлний хичээл" },
];

export default function TutoringPage() {
  const { lang } = useLang();

  return (
    <>
      {/* Hero */}
      <section className="bg-gradient-to-br from-primary-800 to-primary-600 text-white pt-32 pb-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-2xl">
            <div className="badge bg-white/15 text-white mb-4">
              <T en="1-on-1 Tutoring" mn="1:1 Хувийн хичээл" />
            </div>
            <h1 className="text-4xl sm:text-5xl font-bold mb-5">
              <T en="Expert math tutoring, tailored for you" mn="Таны хэрэгцээнд зориулсан мэргэжлийн математикийн хичээл" />
            </h1>
            <p className="text-blue-100 text-lg leading-relaxed mb-8">
              <T
                en="Personalized one-on-one sessions with bilingual tutors who understand both Mongolian students' backgrounds and the demands of US and international curricula."
                mn="Монгол оюутнуудын суурийг болон АНУ, олон улсын хөтөлбөрийн шаардлагыг ойлгодог хоёр хэлтэй багш нартай хувийн нэг-нэгтэй хичээлүүд."
              />
            </p>
            <Link href="/contact" className="btn-white text-base px-8 py-3.5">
              <T en="Book a Free Intro Session" mn="Үнэгүй танилцах хичээл захиалах" />
              <ArrowRight className="ml-2 h-4 w-4" />
            </Link>
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="bg-white border-b border-gray-100 py-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-8 text-center">
            {stats.map((s) => (
              <div key={s.value}>
                <p className="text-3xl font-bold text-primary-600">{s.value}</p>
                <p className="text-gray-500 text-sm mt-1">{lang === "mn" ? s.mn : s.en}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* How it works */}
      <section className="section bg-gray-50">
        <div className="container-lg">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-3">
              <T en="How it works" mn="Хэрхэн ажилладаг вэ" />
            </h2>
            <p className="text-gray-500">
              <T en="Get started in four simple steps" mn="Дөрвөн энгийн алхамаар эхэл" />
            </p>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {steps.map((s) => {
              const content = lang === "mn" ? s.mn : s.en;
              return (
                <div key={s.step} className="card text-center">
                  <div className="w-10 h-10 rounded-full bg-primary-600 text-white font-bold flex items-center justify-center mx-auto mb-4">
                    {s.step}
                  </div>
                  <h3 className="font-semibold text-gray-900 mb-2">{content.title}</h3>
                  <p className="text-gray-500 text-sm">{content.desc}</p>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Benefits + subjects */}
      <section className="section bg-white">
        <div className="container-lg">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-16">
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-6">
                <T en="What's included" mn="Юу орсон байдаг вэ" />
              </h2>
              <ul className="space-y-3">
                {benefits.map((b) => (
                  <li key={b.en} className="flex items-center gap-3 text-gray-700">
                    <CheckCircle className="h-5 w-5 text-accent-green flex-shrink-0" />
                    {lang === "mn" ? b.mn : b.en}
                  </li>
                ))}
              </ul>

              <div className="mt-8 p-5 bg-primary-50 rounded-2xl border border-primary-100">
                <div className="flex items-center gap-3 mb-2">
                  <Globe className="h-5 w-5 text-primary-600" />
                  <span className="font-semibold text-primary-800">
                    <T en="Serving all time zones" mn="Бүх цагийн бүсэд үйлчилдэг" />
                  </span>
                </div>
                <p className="text-primary-700 text-sm">
                  <T
                    en="Our tutors are available from San Francisco to Ulaanbaatar—we schedule sessions at times that work for your family."
                    mn="Манай багш нар Сан-Францискогоос Улаанбаатар хүртэл боломжтой—гэр бүлд тохирсон цагт хичээлийг товлоно."
                  />
                </p>
              </div>
            </div>

            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-6">
                <T en="Subjects we cover" mn="Бидний заадаг хичээлүүд" />
              </h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {subjects.map((s) => (
                  <div key={s.name} className="flex items-start gap-3 p-3 bg-gray-50 rounded-xl">
                    <Star className="h-4 w-4 text-accent-amber flex-shrink-0 mt-0.5" />
                    <div>
                      <p className="font-medium text-gray-900 text-sm">{s.name}</p>
                      <p className="text-gray-400 text-xs">{lang === "mn" ? s.mn : s.en}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="section bg-primary-600">
        <div className="container-lg text-center">
          <h2 className="text-3xl font-bold text-white mb-4">
            <T en="Ready to find your perfect tutor?" mn="Өөртөө тохирсон багшаа олоход бэлэн үү?" />
          </h2>
          <p className="text-blue-100 mb-8 text-lg">
            <T
              en="Contact us today and we'll match you with the right tutor within 24 hours."
              mn="Өнөөдөр бидэнтэй холбогдоорой, 24 цагийн дотор тохирсон багштай таарна."
            />
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <Link href="/contact" className="btn-white text-base px-8 py-3.5">
              <T en="Get Started Free" mn="Үнэгүй эхлэх" />
              <ArrowRight className="ml-2 h-4 w-4" />
            </Link>
            <a href="tel:+14159818165" className="inline-flex items-center gap-2 px-8 py-3.5 border-2 border-white/40 text-white font-semibold rounded-lg hover:bg-white/10 transition-colors text-base">
              <Clock className="h-4 w-4" />
              +1 (415) 981-8165
            </a>
          </div>
        </div>
      </section>
    </>
  );
}
