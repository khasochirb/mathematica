"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import {
  CourseHubPage,
  CourseUnitPage,
  CourseLessonPage,
  CoursePracticePage,
  CourseTestPage,
} from "@/components/course/CourseShell";
import { satCourseDef } from "@/lib/sat-course";

// The SAT course routes carry the domain as a URL segment, so the CourseDef
// is resolved per request — same thin-wrapper pattern as the ЭШ courses
// (components/esh/course/EshCoursePages.tsx), English chrome throughout.

function DomainMissing() {
  return (
    <div
      className="min-h-screen pt-20 flex items-center justify-center"
      style={{ background: "var(--bg)" }}
    >
      <div className="text-center">
        <p className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
          Domain <em className="serif-italic" style={{ color: "var(--accent)" }}>not found</em>.
        </p>
        <Link href="/practice/sat/learn" className="btn btn-line mt-5 inline-flex items-center gap-1.5">
          <ArrowLeft className="h-3.5 w-3.5" /> Back to the course
        </Link>
      </div>
    </div>
  );
}

function useSatCourse() {
  const params = useParams();
  return satCourseDef(params.domain as string);
}

export function SatDomainPage() {
  const course = useSatCourse();
  if (!course) return <DomainMissing />;
  return <CourseHubPage course={course} />;
}

export function SatUnitPage() {
  const course = useSatCourse();
  if (!course) return <DomainMissing />;
  return <CourseUnitPage course={course} />;
}

export function SatLessonPage() {
  const course = useSatCourse();
  if (!course) return <DomainMissing />;
  return <CourseLessonPage course={course} />;
}

export function SatPracticePage() {
  const course = useSatCourse();
  if (!course) return <DomainMissing />;
  return <CoursePracticePage course={course} />;
}

export function SatTestPage() {
  const course = useSatCourse();
  if (!course) return <DomainMissing />;
  return <CourseTestPage course={course} />;
}
