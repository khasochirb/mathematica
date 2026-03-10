import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight, BookOpen, Trophy, Target, Star } from "lucide-react";

export const metadata: Metadata = {
  title: "Exam Prep",
  description: "Expert preparation for SAT, ACT, AP, IB, AMC, and other math exams for Mongolian students.",
};

const exams = [
  {
    id: "sat",
    title: "SAT Math",
    icon: "📐",
    description:
      "Targeted prep covering algebra, advanced math, and problem-solving strategies for College Board's SAT. We focus on the specific question types and time management skills needed to maximize your score.",
    topics: ["Heart of Algebra", "Passport to Advanced Math", "Additional Topics", "Data Analysis"],
    cta: "Start SAT Prep",
  },
  {
    id: "act",
    title: "ACT Math",
    icon: "📊",
    description:
      "Comprehensive ACT Math prep covering all 60 questions in 60 minutes. We build speed and accuracy across pre-algebra, algebra, coordinate geometry, plane geometry, and trigonometry.",
    topics: ["Pre-Algebra", "Elementary Algebra", "Intermediate Algebra", "Geometry", "Trigonometry"],
    cta: "Start ACT Prep",
  },
  {
    id: "ap",
    title: "AP Math",
    icon: "🎓",
    description:
      "Rigorous preparation for AP Calculus AB/BC, AP Statistics, and AP Precalculus. We align with College Board's curriculum framework and provide practice with released FRQs and MCQs.",
    topics: ["Calculus AB", "Calculus BC", "Statistics", "Precalculus"],
    cta: "Start AP Prep",
  },
  {
    id: "ib",
    title: "IB Mathematics",
    icon: "🌍",
    description:
      "Expert support for IB Math AA and IB Math AI at both Standard and Higher Level. Our tutors are experienced with IB's unique internal assessment requirements and exploration projects.",
    topics: ["Analysis & Approaches SL/HL", "Applications & Interpretation SL/HL", "Internal Assessment"],
    cta: "Start IB Prep",
  },
  {
    id: "olympiad",
    title: "Math Olympiad",
    icon: "🏆",
    description:
      "Specialized training for AMC 8/10/12, AIME, MATHCOUNTS, and international olympiad competitions. We develop problem-solving intuition through classic competition problems and proof techniques.",
    topics: ["AMC 8 / 10 / 12", "AIME", "MATHCOUNTS", "USA(J)MO"],
    cta: "Start Olympiad Prep",
  },
  {
    id: "psat",
    title: "PSAT / NMSQT",
    icon: "🎯",
    description:
      "Strategic PSAT prep for the National Merit Scholarship Qualifying Test. We focus on the exact content areas and difficulty levels of the PSAT to help students qualify for National Merit recognition.",
    topics: ["Algebra", "Advanced Math", "Problem-Solving", "Data Analysis"],
    cta: "Start PSAT Prep",
  },
  {
    id: "gre",
    title: "GRE Quant",
    icon: "📈",
    description:
      "Focused GRE Quantitative Reasoning preparation for graduate school applicants. We cover arithmetic, algebra, geometry, and data analysis, with extensive practice on quantitative comparison and data interpretation.",
    topics: ["Arithmetic", "Algebra", "Geometry", "Data Analysis"],
    cta: "Start GRE Prep",
  },
  {
    id: "gmat",
    title: "GMAT Quant",
    icon: "💼",
    description:
      "Expert GMAT Quantitative preparation for business school candidates. We cover Problem Solving and Data Sufficiency question types with strategies for the GMAT Focus Edition format.",
    topics: ["Problem Solving", "Data Sufficiency", "Number Properties", "Statistics"],
    cta: "Start GMAT Prep",
  },
  {
    id: "igcse",
    title: "IGCSE / GCSE Math",
    icon: "📚",
    description:
      "Comprehensive preparation for Cambridge IGCSE and GCSE Mathematics at all tiers. We cover the full syllabus and provide past paper practice for both Cambridge and Edexcel specifications.",
    topics: ["Number", "Algebra", "Geometry", "Statistics & Probability"],
    cta: "Start IGCSE Prep",
  },
];

export default function ExamPrepPage() {
  return (
    <>
      {/* Hero */}
      <section className="bg-gradient-to-br from-primary-900 to-primary-700 text-white pt-32 pb-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="badge bg-white/15 text-white mx-auto mb-4">Exam Preparation</div>
          <h1 className="text-4xl sm:text-5xl font-bold mb-5">
            Ace the exams that matter
          </h1>
          <p className="text-blue-100 text-lg max-w-2xl mx-auto leading-relaxed">
            Expert-led preparation for every major math exam—from standardized tests to
            international olympiads. Our bilingual tutors know exactly what it takes to succeed.
          </p>
        </div>
      </section>

      {/* Exam cards */}
      <section className="section bg-white">
        <div className="container-lg">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {exams.map((exam) => (
              <div
                key={exam.id}
                id={exam.id}
                className="card hover:shadow-lg hover:border-primary-200 transition-all group flex flex-col"
              >
                <div className="text-4xl mb-4">{exam.icon}</div>
                <h3 className="text-xl font-bold text-gray-900 mb-3 group-hover:text-primary-600 transition-colors">
                  {exam.title}
                </h3>
                <p className="text-gray-500 text-sm leading-relaxed mb-4 flex-1">
                  {exam.description}
                </p>
                <div className="flex flex-wrap gap-2 mb-5">
                  {exam.topics.map((t) => (
                    <span key={t} className="badge bg-primary-50 text-primary-700 text-xs">
                      {t}
                    </span>
                  ))}
                </div>
                <Link
                  href="/contact"
                  className="btn-secondary text-sm py-2 text-center"
                >
                  {exam.cta}
                  <ArrowRight className="ml-1.5 h-3.5 w-3.5" />
                </Link>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Why us */}
      <section className="section bg-gray-50">
        <div className="container-lg">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-3">Why Mongol Potential for exam prep?</h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {[
              {
                icon: Target,
                title: "Score-focused approach",
                desc: "We analyze each exam's exact format and teach the fastest, most reliable strategies for every question type.",
              },
              {
                icon: BookOpen,
                title: "Official materials",
                desc: "Practice with real past papers and official released exams—not generic problem banks.",
              },
              {
                icon: Trophy,
                title: "Proven results",
                desc: "Students consistently improve their scores by 100+ SAT points or 3+ ACT points within 3 months.",
              },
            ].map((item) => {
              const Icon = item.icon;
              return (
                <div key={item.title} className="card text-center">
                  <div className="inline-flex p-3 bg-primary-50 rounded-xl mb-4">
                    <Icon className="h-6 w-6 text-primary-600" />
                  </div>
                  <h3 className="font-bold text-gray-900 mb-2">{item.title}</h3>
                  <p className="text-gray-500 text-sm">{item.desc}</p>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="section bg-primary-600">
        <div className="container-lg text-center">
          <h2 className="text-3xl font-bold text-white mb-4">Ready to start prep?</h2>
          <p className="text-blue-100 mb-8">
            Book a free consultation and we'll build a personalized study plan for your exam.
          </p>
          <Link href="/contact" className="btn-white text-base px-8 py-3.5">
            Book Free Consultation
            <ArrowRight className="ml-2 h-4 w-4" />
          </Link>
        </div>
      </section>
    </>
  );
}
