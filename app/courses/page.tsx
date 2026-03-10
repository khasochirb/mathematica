import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight } from "lucide-react";

export const metadata: Metadata = {
  title: "Grade Levels",
  description: "Math tutoring for every age group—elementary through adult learners.",
};

const levels = [
  {
    id: "elementary",
    emoji: "🧒",
    label: "Elementary School",
    range: "Grades 2–5 · Ages 7–11",
    description:
      "We build strong foundations in arithmetic, number sense, and early problem-solving. Our approach makes math fun and culturally relevant, using Mongolian stories and everyday contexts to spark curiosity.",
    topics: [
      "Number sense & place value",
      "Addition, subtraction, multiplication, division",
      "Fractions and decimals",
      "Basic geometry and measurement",
      "Word problems and logical reasoning",
    ],
  },
  {
    id: "middle",
    emoji: "🏫",
    label: "Middle School",
    range: "Grades 6–8 · Ages 11–14",
    description:
      "The years when students either gain confidence in math or lose it. We ensure students develop algebraic thinking, master ratios and proportions, and are fully prepared for high school mathematics.",
    topics: [
      "Pre-Algebra and introductory Algebra",
      "Ratios, rates, and proportional reasoning",
      "Geometry and the coordinate plane",
      "Statistics and probability",
      "MATHCOUNTS / AMC 8 competition prep",
    ],
  },
  {
    id: "high",
    emoji: "🎓",
    label: "High School",
    range: "Grades 9–12 · Ages 14–18",
    description:
      "We support students through the full high school math sequence and beyond—including advanced courses and test preparation. Our tutors help students excel in class and on standardized exams.",
    topics: [
      "Algebra I & II",
      "Geometry",
      "Pre-Calculus and Trigonometry",
      "AP Calculus AB / BC",
      "AP Statistics",
      "SAT, ACT, and PSAT prep",
    ],
  },
  {
    id: "college",
    emoji: "🏛️",
    label: "College",
    range: "Undergraduate · Ages 18+",
    description:
      "College-level math can be demanding. We help undergraduates navigate calculus sequences, linear algebra, differential equations, and proof-based courses with confidence.",
    topics: [
      "Calculus I, II, III",
      "Linear Algebra",
      "Differential Equations",
      "Discrete Mathematics",
      "Statistics and Probability",
      "GRE / GMAT Quantitative prep",
    ],
  },
  {
    id: "adult",
    emoji: "👔",
    label: "Adult Learning",
    range: "All ages · Professional & personal goals",
    description:
      "It's never too late to learn math. Whether you're returning to school, preparing for a professional exam, or simply want to fill gaps from years ago, we meet you exactly where you are.",
    topics: [
      "Foundational arithmetic and algebra review",
      "GED Math preparation",
      "GRE / GMAT prep for career transitions",
      "Statistics for data and business",
      "Personalized curriculum for any goal",
    ],
  },
];

export default function CoursesPage() {
  return (
    <>
      {/* Hero */}
      <section className="bg-gradient-to-br from-primary-800 to-primary-600 text-white pt-32 pb-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="badge bg-white/15 text-white mx-auto mb-4">Grade Levels</div>
          <h1 className="text-4xl sm:text-5xl font-bold mb-5">
            Math tutoring for every age group
          </h1>
          <p className="text-blue-100 text-lg max-w-xl mx-auto">
            We believe everyone can learn. World-class online tutoring from 2nd grade through
            adulthood.
          </p>
        </div>
      </section>

      {/* Jump links */}
      <div className="sticky top-16 z-40 bg-white border-b border-gray-100 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex gap-1 overflow-x-auto py-3 no-scrollbar">
            {levels.map((l) => (
              <a
                key={l.id}
                href={`#${l.id}`}
                className="flex-shrink-0 px-4 py-1.5 rounded-full text-sm font-medium text-gray-600 hover:text-primary-600 hover:bg-primary-50 transition-colors whitespace-nowrap"
              >
                {l.emoji} {l.label}
              </a>
            ))}
          </div>
        </div>
      </div>

      {/* Level sections */}
      <div className="bg-white">
        {levels.map((level, idx) => (
          <section
            key={level.id}
            id={level.id}
            className={`section ${idx % 2 === 0 ? "bg-white" : "bg-gray-50"}`}
          >
            <div className="container-lg">
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                <div className={idx % 2 !== 0 ? "lg:order-2" : ""}>
                  <div className="text-5xl mb-4">{level.emoji}</div>
                  <div className="badge bg-primary-100 text-primary-700 mb-3">{level.range}</div>
                  <h2 className="text-3xl font-bold text-gray-900 mb-4">{level.label}</h2>
                  <p className="text-gray-600 leading-relaxed mb-6">{level.description}</p>
                  <Link href="/contact" className="btn-primary">
                    Get Started
                    <ArrowRight className="ml-2 h-4 w-4" />
                  </Link>
                </div>

                <div className={idx % 2 !== 0 ? "lg:order-1" : ""}>
                  <div className="card bg-gray-50 border-gray-100">
                    <h3 className="font-semibold text-gray-900 mb-4">Topics we cover</h3>
                    <ul className="space-y-2.5">
                      {level.topics.map((t) => (
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
        ))}
      </div>

      {/* CTA */}
      <section className="section bg-primary-600">
        <div className="container-lg text-center">
          <h2 className="text-3xl font-bold text-white mb-4">Not sure which program fits?</h2>
          <p className="text-blue-100 mb-8">
            Contact us and we'll recommend the right level and approach for your student.
          </p>
          <Link href="/contact" className="btn-white text-base px-8 py-3.5">
            Talk to Us
            <ArrowRight className="ml-2 h-4 w-4" />
          </Link>
        </div>
      </section>
    </>
  );
}
