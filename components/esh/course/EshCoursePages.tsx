"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import {
  CourseUnitPage,
  CourseLessonPage,
  CoursePracticePage,
  CourseTestPage,
} from "@/components/course/CourseShell";
import { eshCourseDef } from "@/lib/esh-course";

// The ЭЕШ course routes are one level deeper than the /math ones — the topic
// is a URL segment, so the CourseDef has to be resolved per request rather
// than imported as a constant. These thin wrappers do that resolution and
// hand the shared shell its course.

function TopicMissing() {
  return (
    <div
      className="min-h-screen pt-20 flex items-center justify-center"
      style={{ background: "var(--bg)" }}
    >
      <div className="text-center">
        <p className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
          Сэдэв{" "}
          <em className="serif-italic" style={{ color: "var(--accent)" }}>
            олдсонгүй
          </em>
          .
        </p>
        <Link href="/practice/esh/learn" className="btn btn-line mt-5 inline-flex items-center gap-1.5">
          <ArrowLeft className="h-3.5 w-3.5" /> Суралцах хэсэг рүү буцах
        </Link>
      </div>
    </div>
  );
}

function useEshCourse() {
  const params = useParams();
  return eshCourseDef(params.topicSlug as string);
}

export function EshUnitPage() {
  const course = useEshCourse();
  if (!course) return <TopicMissing />;
  return <CourseUnitPage course={course} />;
}

export function EshLessonPage() {
  const course = useEshCourse();
  if (!course) return <TopicMissing />;
  return <CourseLessonPage course={course} />;
}

export function EshPracticePage() {
  const course = useEshCourse();
  if (!course) return <TopicMissing />;
  return <CoursePracticePage course={course} />;
}

export function EshTestPage() {
  const course = useEshCourse();
  if (!course) return <TopicMissing />;
  return <CourseTestPage course={course} />;
}
