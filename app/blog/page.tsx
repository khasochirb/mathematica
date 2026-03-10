import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight, BookOpen } from "lucide-react";

export const metadata: Metadata = {
  title: "Blog",
  description: "Math tips, study strategies, and insights for Mongolian students and families — coming soon.",
};

export default function BlogPage() {
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
          <div className="max-w-lg mx-auto text-center py-16">
            <div className="w-20 h-20 bg-primary-50 rounded-full flex items-center justify-center mx-auto mb-6">
              <BookOpen className="h-10 w-10 text-primary-400" />
            </div>
            <h2 className="text-2xl font-bold text-gray-900 mb-3">Coming Soon</h2>
            <p className="text-gray-500 leading-relaxed mb-8">
              We're working on articles covering SAT prep strategies, AMC competition tips, bridging
              Mongolian and American math curricula, and more. Check back soon!
            </p>
            <Link href="/contact" className="btn-primary text-base px-8 py-3">
              Get Notified
              <ArrowRight className="ml-2 h-4 w-4" />
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
