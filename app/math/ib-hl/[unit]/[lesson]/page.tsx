"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { getIbHlUnit, getIbHlLesson } from "@/lib/genmath-lessons";
import LessonPlayer from "@/components/genmath/interactive/LessonPlayer";
import ContentGate from "@/components/genmath/ContentGate";

// An IB SL lesson — the same paced interactive player the grade hubs
// use, pointed at this course's units.
function IbHlLessonPageInner() {
  const params = useParams();
  const unitSlug = params.unit as string;
  const lessonSlug = params.lesson as string;

  const unit = getIbHlUnit(unitSlug);
  const lesson = getIbHlLesson(unitSlug, lessonSlug);

  if (!lesson || !unit || !lesson.interactive) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <div className="text-center">
          <p className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
            Lesson <em className="serif-italic" style={{ color: "var(--accent)" }}>not found</em>.
          </p>
          <Link href={`/math/ib-hl/${unitSlug}`} className="btn btn-line mt-5 inline-flex items-center gap-1.5">
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
      baseHref={`/math/ib-hl/${unitSlug}`}
      crumb={`IB Math HL · Topic ${unit.unit} · ${unit.title}`}
    />
  );
}

// Content requires an account; the hub and unit pages above stay public.
export default function IbHlLessonPage() {
  const params = useParams();
  const unitSlug = params.unit as string;
  return (
    <ContentGate backHref={`/math/ib-hl/${unitSlug}`} backLabel="Back to unit">
      <IbHlLessonPageInner />
    </ContentGate>
  );
}
