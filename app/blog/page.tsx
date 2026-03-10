import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight, Clock } from "lucide-react";

export const metadata: Metadata = {
  title: "Blog",
  description: "Math tips, study strategies, and insights for Mongolian students and families.",
};

const posts = [
  {
    slug: "how-to-prepare-for-sat-math",
    title: "How to Prepare for SAT Math as a Mongolian Student",
    excerpt:
      "A step-by-step guide to the SAT Math section, including the most commonly tested topics and strategies that work especially well for students coming from Mongolian math backgrounds.",
    category: "SAT Prep",
    date: "March 2026",
    readTime: "8 min read",
    color: "bg-primary-100 text-primary-700",
  },
  {
    slug: "amc-preparation-guide",
    title: "AMC 8 / 10 Preparation: Where to Start",
    excerpt:
      "The AMC competitions are a great way to challenge yourself and build deep problem-solving skills. Here's how to get started, what resources to use, and how we approach olympiad training.",
    category: "Competition Math",
    date: "February 2026",
    readTime: "10 min read",
    color: "bg-amber-100 text-amber-700",
  },
  {
    slug: "mongolian-math-education",
    title: "Bridging Mongolian and American Math Education",
    excerpt:
      "Mongolian students often arrive in the US with strong computational skills but different notation and curriculum structures. Here's how we help students bridge that gap smoothly.",
    category: "Education",
    date: "January 2026",
    readTime: "6 min read",
    color: "bg-green-100 text-green-700",
  },
  {
    slug: "building-math-confidence",
    title: "Building Math Confidence in Students Who \"Hate Math\"",
    excerpt:
      "Math anxiety is real, but it's not permanent. We share the techniques our tutors use to rebuild confidence and transform reluctant learners into enthusiastic problem-solvers.",
    category: "Learning",
    date: "December 2025",
    readTime: "7 min read",
    color: "bg-purple-100 text-purple-700",
  },
  {
    slug: "ap-calculus-vs-ib-math",
    title: "AP Calculus vs. IB Mathematics: Which is Right for You?",
    excerpt:
      "A practical comparison of AP Calculus AB/BC and IB Math AA/AI, helping students and families decide which path makes more sense for college applications and future studies.",
    category: "AP & IB",
    date: "November 2025",
    readTime: "9 min read",
    color: "bg-primary-100 text-primary-700",
  },
  {
    slug: "time-zones-online-tutoring",
    title: "Making Online Tutoring Work Across Time Zones",
    excerpt:
      "Our families span from California to Ulaanbaatar. Here's how we structure sessions, set expectations, and keep students engaged regardless of where they are in the world.",
    category: "Tutoring Tips",
    date: "October 2025",
    readTime: "5 min read",
    color: "bg-blue-100 text-blue-700",
  },
];

export default function BlogPage() {
  const [featured, ...rest] = posts;

  return (
    <>
      {/* Hero */}
      <section className="bg-gradient-to-br from-primary-800 to-primary-600 text-white pt-32 pb-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="badge bg-white/15 text-white mx-auto mb-4">Blog</div>
          <h1 className="text-4xl sm:text-5xl font-bold mb-4">Math insights & study tips</h1>
          <p className="text-blue-100 text-lg max-w-xl mx-auto">
            Articles for Mongolian students and families navigating math education in the US and beyond.
          </p>
        </div>
      </section>

      <section className="section bg-white">
        <div className="container-lg">
          {/* Featured post */}
          <div className="card hover:shadow-lg transition-shadow mb-12 group">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
              <div className="aspect-video bg-gradient-to-br from-primary-100 to-primary-200 rounded-xl flex items-center justify-center">
                <span className="text-6xl">📚</span>
              </div>
              <div>
                <div className="flex items-center gap-3 mb-4">
                  <span className={`badge ${featured.color} text-xs`}>{featured.category}</span>
                  <span className="text-gray-400 text-xs">{featured.date}</span>
                  <span className="flex items-center gap-1 text-gray-400 text-xs">
                    <Clock className="h-3 w-3" />
                    {featured.readTime}
                  </span>
                </div>
                <h2 className="text-2xl font-bold text-gray-900 mb-3 group-hover:text-primary-600 transition-colors">
                  {featured.title}
                </h2>
                <p className="text-gray-500 leading-relaxed mb-5">{featured.excerpt}</p>
                <Link
                  href={`/blog/${featured.slug}`}
                  className="btn-primary text-sm py-2 px-5"
                >
                  Read Article
                  <ArrowRight className="ml-1.5 h-3.5 w-3.5" />
                </Link>
              </div>
            </div>
          </div>

          {/* Rest of posts */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {rest.map((post) => (
              <Link
                key={post.slug}
                href={`/blog/${post.slug}`}
                className="card hover:shadow-md hover:border-primary-200 transition-all group flex flex-col"
              >
                <div className="aspect-video bg-gradient-to-br from-gray-50 to-gray-100 rounded-xl flex items-center justify-center mb-4 text-4xl">
                  📖
                </div>
                <div className="flex items-center gap-2 mb-3">
                  <span className={`badge ${post.color} text-xs`}>{post.category}</span>
                  <span className="flex items-center gap-1 text-gray-400 text-xs ml-auto">
                    <Clock className="h-3 w-3" />
                    {post.readTime}
                  </span>
                </div>
                <h3 className="font-bold text-gray-900 mb-2 group-hover:text-primary-600 transition-colors flex-1">
                  {post.title}
                </h3>
                <p className="text-gray-500 text-sm line-clamp-2 mb-3">{post.excerpt}</p>
                <p className="text-gray-400 text-xs">{post.date}</p>
              </Link>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}
