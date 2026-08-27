"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { chrome } from "@/lib/i18n/chrome";
import { getAlg1UnitLocalized, getAlg1LessonLocalized } from "@/lib/genmath-data/algebra-1";
import { useLang } from "@/lib/lang-context";
import LessonPlayer from "@/components/genmath/interactive/LessonPlayer";
import ContentGate from "@/components/genmath/ContentGate";

// An Algebra 1 lesson — the same paced interactive player the grade hubs
// use, pointed at this course's units.
function Alg1LessonPageInner() {
  const params = useParams();
  const { lang } = useLang();
  const unitSlug = params.unit as string;
  const lessonSlug = params.lesson as string;

  const unit = getAlg1UnitLocalized(unitSlug, lang);
  const lesson = getAlg1LessonLocalized(unitSlug, lessonSlug, lang);

  if (!lesson || !unit || !lesson.interactive) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <div className="text-center">
          <p className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
            Lesson <em className="serif-italic" style={{ color: "var(--accent)" }}>not found</em>.
          </p>
          <Link href={`/math/algebra-1/${unitSlug}`} className="btn btn-line mt-5 inline-flex items-center gap-1.5">
            <ArrowLeft className="h-3.5 w-3.5" /> {chrome("Back to unit", lang)}
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
      baseHref={`/math/algebra-1/${unitSlug}`}
      crumb={`Algebra 1 · Unit ${unit.unit} · ${unit.title}`}
    />
  );
}

// Content requires an account; the hub and unit pages above stay public.
export default function Alg1LessonPage() {
  const params = useParams();
  const { lang } = useLang();
  const unitSlug = params.unit as string;
  return (
    <ContentGate courseKey="algebra-1" topicSlug={unitSlug} backHref={`/math/algebra-1/${unitSlug}`} backLabel={chrome("Back to unit", lang)}>
      <Alg1LessonPageInner />
    </ContentGate>
  );
}
