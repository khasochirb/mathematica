"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { getGeometryUnit, getGeometryLesson } from "@/lib/genmath-lessons";
import LessonPlayer from "@/components/genmath/interactive/LessonPlayer";

// A Geometry lesson — the same paced interactive player the grade hubs use,
// pointed at the geometry course's units.
export default function GeometryLessonPage() {
  const params = useParams();
  const unitSlug = params.unit as string;
  const lessonSlug = params.lesson as string;

  const unit = getGeometryUnit(unitSlug);
  const lesson = getGeometryLesson(unitSlug, lessonSlug);

  if (!lesson || !unit || !lesson.interactive) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <div className="text-center">
          <p className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
            Lesson <em className="serif-italic" style={{ color: "var(--accent)" }}>not found</em>.
          </p>
          <Link href={`/math/geometry/${unitSlug}`} className="btn btn-line mt-5 inline-flex items-center gap-1.5">
            <ArrowLeft className="h-3.5 w-3.5" /> Back to unit
          </Link>
        </div>
      </div>
    );
  }

  return (
    <LessonPlayer
      lesson={lesson}
      topicSlug={unitSlug}
      topicTitle={unit.title}
      baseHref={`/math/geometry/${unitSlug}`}
      crumb={`Geometry · Unit ${unit.unit} · ${unit.title}`}
    />
  );
}
