"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { chrome } from "@/lib/i18n/chrome";
import { useLang } from "@/lib/lang-context";
import { getAlg2Unit, getAlg2Lesson } from "@/lib/genmath-data/algebra-2";
import LessonPlayer from "@/components/genmath/interactive/LessonPlayer";
import ContentGate from "@/components/genmath/ContentGate";

// An Algebra 2 lesson — the same paced interactive player the grade hubs
// use, pointed at this course's units.
function Alg2LessonPageInner() {
  const params = useParams();
  const { lang } = useLang();
  const unitSlug = params.unit as string;
  const lessonSlug = params.lesson as string;

  const unit = getAlg2Unit(unitSlug);
  const lesson = getAlg2Lesson(unitSlug, lessonSlug);

  if (!lesson || !unit || !lesson.interactive) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <div className="text-center">
          <p className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
            Lesson <em className="serif-italic" style={{ color: "var(--accent)" }}>not found</em>.
          </p>
          <Link href={`/math/algebra-2/${unitSlug}`} className="btn btn-line mt-5 inline-flex items-center gap-1.5">
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
      baseHref={`/math/algebra-2/${unitSlug}`}
      crumb={`Algebra 2 · Unit ${unit.unit} · ${unit.title}`}
    />
  );
}

// Content requires an account; the hub and unit pages above stay public.
export default function Alg2LessonPage() {
  const params = useParams();
  const { lang } = useLang();
  const unitSlug = params.unit as string;
  return (
    <ContentGate courseKey="algebra-2" topicSlug={unitSlug} backHref={`/math/algebra-2/${unitSlug}`} backLabel={chrome("Back to unit", lang)}>
      <Alg2LessonPageInner />
    </ContentGate>
  );
}
