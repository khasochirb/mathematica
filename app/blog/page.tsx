import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight, BookOpen } from "lucide-react";

export const metadata: Metadata = {
  title: "Blog",
  description: "Math tips, study strategies, and insights for Mongolian students and families — coming soon.",
};

export default function BlogPage() {
  return (
    <div className="min-h-screen pt-24 pb-16" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="eyebrow mb-2">Editorial · Journal</div>
        <h1
          className="serif"
          style={{
            fontWeight: 400,
            fontSize: "clamp(40px, 6vw, 64px)",
            letterSpacing: "-0.04em",
            lineHeight: 0.98,
            color: "var(--fg)",
          }}
        >
          Math <em className="serif-italic" style={{ color: "var(--accent)" }}>insights</em> &amp; study tips
        </h1>
        <p className="mt-5 text-[16px] leading-relaxed max-w-2xl" style={{ color: "var(--fg-2)" }}>
          Articles for Mongolian students and families navigating math education in the US and beyond.
        </p>

        <div
          className="card-edit mt-12 p-10 text-center"
          style={{ background: "var(--bg-1)" }}
        >
          <div
            className="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-5"
            style={{
              background: "var(--accent-wash)",
              border: "1px solid var(--accent-line)",
              color: "var(--accent)",
            }}
          >
            <BookOpen className="h-7 w-7" />
          </div>
          <div className="eyebrow mb-2">Status</div>
          <h2
            className="serif"
            style={{ fontWeight: 400, fontSize: 32, letterSpacing: "-0.02em", color: "var(--fg)" }}
          >
            Coming soon.
          </h2>
          <p className="text-[14px] mt-3 max-w-md mx-auto" style={{ color: "var(--fg-2)" }}>
            We&apos;re working on articles covering SAT prep strategies, AMC competition tips, bridging
            Mongolian and American math curricula, and more.
          </p>
          <Link href="/contact" className="btn btn-primary mt-7 inline-flex">
            Get notified
            <ArrowRight className="ml-1 h-3.5 w-3.5" />
          </Link>
        </div>
      </div>
    </div>
  );
}
