"use client";

import Link from "next/link";
import { listGrades } from "@/lib/genmath-lessons";

export default function MathLandingPage() {
  const grades = listGrades();

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 pb-16">
        {/* Header */}
        <div className="eyebrow mb-4">General Math · Grades 6–12</div>
        <h1
          className="serif"
          style={{
            fontWeight: 400,
            fontSize: "clamp(36px, 5vw, 64px)",
            letterSpacing: "-0.04em",
            lineHeight: 1,
            color: "var(--fg)",
          }}
        >
          General Math
        </h1>
        <p
          className="mt-4 mb-10"
          style={{ color: "var(--fg-1)", fontSize: 17, maxWidth: "52ch" }}
        >
          Structured lessons, worked examples, and practice — from Grade 6 through Grade 12.
          Start with Grade 6 now; more grades coming soon.
        </p>

        {/* Subject courses */}
        <div className="eyebrow mb-4">Courses</div>
        <div className="mb-10">
          <Link
            href="/math/geometry"
            className="card-edit p-6 flex flex-col gap-2 transition-colors"
            style={{ textDecoration: "none" }}
            onMouseEnter={(e) => {
              (e.currentTarget as HTMLAnchorElement).style.borderColor = "var(--accent-line)";
              (e.currentTarget as HTMLAnchorElement).style.background = "var(--accent-wash)";
            }}
            onMouseLeave={(e) => {
              (e.currentTarget as HTMLAnchorElement).style.borderColor = "";
              (e.currentTarget as HTMLAnchorElement).style.background = "";
            }}
          >
            <span
              className="mono text-[10px] uppercase"
              style={{ color: "var(--accent)", letterSpacing: "0.08em" }}
            >
              New · Full course
            </span>
            <span
              className="serif"
              style={{ fontSize: 32, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)" }}
            >
              Geometry
            </span>
            <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
              From points and lines to proof, circles, and trigonometry — taught from zero,
              one continuous track. 13 units.
            </span>
          </Link>
        </div>

        {/* Grade cards */}
        <div className="eyebrow mb-4">By grade</div>
        <div
          className="grid gap-4"
          style={{ gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))" }}
        >
          {grades.map(({ grade, active }) =>
            active ? (
              <Link
                key={grade}
                href={`/math/${grade}`}
                className="card-edit p-6 flex flex-col gap-2 transition-colors"
                style={{ textDecoration: "none" }}
                onMouseEnter={(e) => {
                  (e.currentTarget as HTMLAnchorElement).style.borderColor = "var(--accent-line)";
                  (e.currentTarget as HTMLAnchorElement).style.background = "var(--accent-wash)";
                }}
                onMouseLeave={(e) => {
                  (e.currentTarget as HTMLAnchorElement).style.borderColor = "";
                  (e.currentTarget as HTMLAnchorElement).style.background = "";
                }}
              >
                <span
                  className="mono text-[10px] uppercase"
                  style={{ color: "var(--accent)", letterSpacing: "0.08em" }}
                >
                  Active
                </span>
                <span
                  className="serif"
                  style={{ fontSize: 32, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)" }}
                >
                  Grade {grade}
                </span>
                <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
                  10 topics
                </span>
              </Link>
            ) : (
              <div
                key={grade}
                className="card-edit p-6 flex flex-col gap-2"
                style={{ opacity: 0.45, cursor: "default" }}
              >
                <span
                  className="mono text-[10px] uppercase"
                  style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}
                >
                  Coming soon
                </span>
                <span
                  className="serif"
                  style={{ fontSize: 32, fontWeight: 400, letterSpacing: "-0.02em", color: "var(--fg)" }}
                >
                  Grade {grade}
                </span>
              </div>
            )
          )}
        </div>
      </div>
    </div>
  );
}
