import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight, CheckCircle, Clock, Globe, Star, User } from "lucide-react";

export const metadata: Metadata = {
  title: "1-on-1 Tutoring",
  description:
    "Personalized math tutoring for Mongolian students worldwide. Expert tutors aligned with AP, IB, and US curricula.",
};

const benefits = [
  "Sessions scheduled around your time zone",
  "Tutors fluent in English and Mongolian",
  "Curriculum-aligned to AP, IB, US state standards",
  "Progress reports after every session",
  "Flexible cancellation with 24-hour notice",
  "Free introductory session available",
];

const subjects = [
  { name: "Algebra I & II", level: "Middle–High School" },
  { name: "Geometry", level: "Middle–High School" },
  { name: "Pre-Calculus", level: "High School" },
  { name: "Calculus AB/BC", level: "AP / High School" },
  { name: "Statistics", level: "AP / High School" },
  { name: "SAT / ACT Math", level: "Test Prep" },
  { name: "IB Mathematics", level: "IB Diploma" },
  { name: "Math Olympiad", level: "Competition" },
  { name: "Elementary Math", level: "Grades 2–5" },
  { name: "Middle School Math", level: "Grades 6–8" },
];

const steps = [
  { step: "1", title: "Tell us about your needs", desc: "Fill out a short form about your grade, goals, and schedule." },
  { step: "2", title: "Get matched with a tutor", desc: "We pair you with a bilingual tutor who fits your curriculum and timezone." },
  { step: "3", title: "Start your free intro session", desc: "Meet your tutor, set goals, and experience our approach—at no cost." },
  { step: "4", title: "Build a weekly routine", desc: "Consistent 1-on-1 sessions that track progress and adapt to your growth." },
];

export default function TutoringPage() {
  return (
    <>
      {/* Hero */}
      <section className="bg-gradient-to-br from-primary-800 to-primary-600 text-white pt-32 pb-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-2xl">
            <div className="badge bg-white/15 text-white mb-4">1-on-1 Tutoring</div>
            <h1 className="text-4xl sm:text-5xl font-bold mb-5">
              Expert math tutoring, tailored for you
            </h1>
            <p className="text-blue-100 text-lg leading-relaxed mb-8">
              Personalized one-on-one sessions with bilingual tutors who understand both Mongolian
              students' backgrounds and the demands of US and international curricula.
            </p>
            <Link href="/contact" className="btn-white text-base px-8 py-3.5">
              Book a Free Intro Session
              <ArrowRight className="ml-2 h-4 w-4" />
            </Link>
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="bg-white border-b border-gray-100 py-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-8 text-center">
            {[
              { value: "500+", label: "Students Helped" },
              { value: "4.9★", label: "Average Rating" },
              { value: "15+", label: "Subjects Covered" },
              { value: "100%", label: "Bilingual Sessions" },
            ].map((s) => (
              <div key={s.label}>
                <p className="text-3xl font-bold text-primary-600">{s.value}</p>
                <p className="text-gray-500 text-sm mt-1">{s.label}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* How it works */}
      <section className="section bg-gray-50">
        <div className="container-lg">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-3">How it works</h2>
            <p className="text-gray-500">Get started in four simple steps</p>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {steps.map((s) => (
              <div key={s.step} className="card text-center">
                <div className="w-10 h-10 rounded-full bg-primary-600 text-white font-bold flex items-center justify-center mx-auto mb-4">
                  {s.step}
                </div>
                <h3 className="font-semibold text-gray-900 mb-2">{s.title}</h3>
                <p className="text-gray-500 text-sm">{s.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Benefits + subjects */}
      <section className="section bg-white">
        <div className="container-lg">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-16">
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-6">What's included</h2>
              <ul className="space-y-3">
                {benefits.map((b) => (
                  <li key={b} className="flex items-center gap-3 text-gray-700">
                    <CheckCircle className="h-5 w-5 text-accent-green flex-shrink-0" />
                    {b}
                  </li>
                ))}
              </ul>

              <div className="mt-8 p-5 bg-primary-50 rounded-2xl border border-primary-100">
                <div className="flex items-center gap-3 mb-2">
                  <Globe className="h-5 w-5 text-primary-600" />
                  <span className="font-semibold text-primary-800">Serving all time zones</span>
                </div>
                <p className="text-primary-700 text-sm">
                  Our tutors are available from San Francisco to Ulaanbaatar—we schedule sessions at
                  times that work for your family.
                </p>
              </div>
            </div>

            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-6">Subjects we cover</h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {subjects.map((s) => (
                  <div key={s.name} className="flex items-start gap-3 p-3 bg-gray-50 rounded-xl">
                    <Star className="h-4 w-4 text-accent-amber flex-shrink-0 mt-0.5" />
                    <div>
                      <p className="font-medium text-gray-900 text-sm">{s.name}</p>
                      <p className="text-gray-400 text-xs">{s.level}</p>
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
            Ready to find your perfect tutor?
          </h2>
          <p className="text-blue-100 mb-8 text-lg">
            Contact us today and we'll match you with the right tutor within 24 hours.
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <Link href="/contact" className="btn-white text-base px-8 py-3.5">
              Get Started Free
              <ArrowRight className="ml-2 h-4 w-4" />
            </Link>
            <a href="tel:+14153367764" className="inline-flex items-center gap-2 px-8 py-3.5 border-2 border-white/40 text-white font-semibold rounded-lg hover:bg-white/10 transition-colors text-base">
              <Clock className="h-4 w-4" />
              Call +1 (415) 336-7764
            </a>
          </div>
        </div>
      </section>
    </>
  );
}
