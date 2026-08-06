"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { getIbAiSlUnit, getIbAiSlLesson } from "@/lib/genmath-data/ib-ai-sl";
import LessonPlayer from "@/components/genmath/interactive/LessonPlayer";
import ContentGate from "@/components/genmath/ContentGate";

// An IB AI SL lesson — the same paced interactive player the grade hubs
// use, pointed at this course's units.
function IbAiSlLessonPageInner() {
  const params = useParams();
  const unitSlug = params.unit as string;
  const lessonSlug = params.lesson as string;

  const unit = getIbAiSlUnit(unitSlug);
  const lesson = getIbAiSlLesson(unitSlug, lessonSlug);

  if (!lesson || !unit || !lesson.interactive) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <div className="text-center">
          <p className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
            Lesson <em className="serif-italic" style={{ color: "var(--accent)" }}>not found</em>.
          </p>
          <Link href={`/math/ib-ai-sl/${unitSlug}`} className="btn btn-line mt-5 inline-flex items-center gap-1.5">
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
      baseHref={`/math/ib-ai-sl/${unitSlug}`}
      crumb={`IB Math AI SL · Topic ${unit.unit} · ${unit.title}`}
    />
  );
}

// Content requires an account; the hub and unit pages above stay public.
export default function IbAiSlLessonPage() {
  const params = useParams();
  const unitSlug = params.unit as string;
  return (
    <ContentGate courseKey="ib-ai-sl" topicSlug={unitSlug} backHref={`/math/ib-ai-sl/${unitSlug}`} backLabel="Back to unit">
      <IbAiSlLessonPageInner />
    </ContentGate>
  );
}
