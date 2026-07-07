"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import MathText from "@/components/esh/MathText";
import Section from "@/components/lesson/Section";
import FactCard from "@/components/lesson/FactCard";
import WorkedExampleCard from "@/components/lesson/WorkedExampleCard";
import RevealProblemCard from "@/components/lesson/RevealProblemCard";
import CommonMistakesList from "@/components/lesson/CommonMistakesList";
import { getGenMathTopicLocalized } from "@/lib/genmath-lessons";
import LessonPlayer from "@/components/genmath/interactive/LessonPlayer";
import ContentGate from "@/components/genmath/ContentGate";
import { useLang } from "@/lib/lang-context";

function GenMathLessonPageInner() {
  const params = useParams();
  const topicSlug = params.topic as string;
  const lessonSlug = params.lesson as string;
  const { lang } = useLang();

  const topic = getGenMathTopicLocalized(topicSlug, lang);
  const lesson = topic?.lessons.find((l) => l.slug === lessonSlug) ?? null;
  const mn = lang === "mn";
  const REVEAL_LABELS = mn
    ? { reveal: "Бодолтыг харах", hide: "Нуух", revealAria: "Бодолтыг харах", hideAria: "Бодолтыг нуух" }
    : { reveal: "Show solution", hide: "Hide", revealAria: "Show solution", hideAria: "Hide solution" };

  if (!lesson || !topic) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <div className="text-center">
          <p className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
            Lesson <em className="serif-italic" style={{ color: "var(--accent)" }}>not found</em>.
          </p>
          <Link
            href={`/math/9/${topicSlug}`}
            className="btn btn-line mt-5 inline-flex items-center gap-1.5"
          >
            <ArrowLeft className="h-3.5 w-3.5" /> Back to topic
          </Link>
        </div>
      </div>
    );
  }

  // Interactive lessons (e.g. Ratios) render the paced player; all other
  // lessons keep the static scroll renderer below. No regression.
  if (lesson.interactive) {
    return <LessonPlayer lesson={lesson} topicSlug={topicSlug} topicTitle={topic.title} baseHref={`/math/9/${topicSlug}`} crumb={`${mn ? "Ерөнхий математик · 9-р анги" : "General Math · Grade 9"} · ${topic.title}`} />;
  }

  const hasAuthoredMistakes = lesson.commonMistakes.some((m) => m.authored);

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        {/* Back + eyebrow */}
        <div className="flex items-center gap-3 mb-6">
          <Link
            href={`/math/9/${topicSlug}`}
            className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">{mn ? "Ерөнхий математик · 9-р анги" : "General Math · Grade 9"} · {topic.title}</div>
        </div>

        {/* Lesson title */}
        <h1
          className="serif"
          style={{
            fontWeight: 400,
            fontSize: "clamp(32px, 5vw, 56px)",
            letterSpacing: "-0.04em",
            lineHeight: 1,
            color: "var(--fg)",
          }}
        >
          {lesson.title}
        </h1>

        {/* 01 · Real-world picture — ALWAYS shown */}
        <Section n="01" label="Real-world picture">
          <p className="font-sans" style={{ fontSize: 17, lineHeight: 1.55, color: "var(--fg-1)" }}>
            <MathText text={lesson.concreteComparison} />
          </p>
        </Section>

        {/* 02 · What you'll learn */}
        <Section n="02" label="What you'll learn">
          <p className="font-sans" style={{ fontSize: 17, lineHeight: 1.55, color: "var(--fg-1)" }}>
            {lesson.objective}
          </p>
        </Section>

        {/* 03 · The idea */}
        <Section n="03" label="The idea">
          <div className="space-y-4">
            {lesson.concept.map((para, i) => (
              <p key={i} className="font-sans" style={{ fontSize: 17, lineHeight: 1.6, color: "var(--fg-1)" }}>
                <MathText text={para} />
              </p>
            ))}
          </div>
          {lesson.keyIdea && (
            <div
              className="card-edit p-4 mt-4"
              style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
            >
              <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>Key idea</div>
              <p className="text-[14px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
                <MathText text={lesson.keyIdea} />
              </p>
            </div>
          )}
        </Section>

        {/* 04 · Try this (optional) */}
        {lesson.tryThis && (
          <Section n="04" label="Try this">
            <div
              className="card-edit p-5"
              style={{ background: "var(--bg-1)" }}
            >
              <p
                className="serif mb-2"
                style={{ fontWeight: 400, fontSize: 16, color: "var(--accent)" }}
              >
                {lesson.tryThis.title}
              </p>
              <p className="text-[14px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
                <MathText text={lesson.tryThis.body} />
              </p>
            </div>
          </Section>
        )}

        {/* 05 · Key facts (optional) */}
        {lesson.facts && lesson.facts.length > 0 && (
          <Section n="05" label="Key facts">
            <div className="space-y-3">
              {lesson.facts.map((fact, i) => (
                <FactCard key={i} fact={fact} />
              ))}
            </div>
          </Section>
        )}

        {/* 06 · Worked examples */}
        <Section n="06" label="Worked examples">
          <div className="space-y-4">
            {lesson.workedExamples.map((problem, i) => (
              <WorkedExampleCard key={problem.id} problem={problem} index={i} />
            ))}
          </div>
        </Section>

        {/* 07 · Watch out (only if there are authored mistakes) */}
        {hasAuthoredMistakes && (
          <Section n="07" label="Watch out">
            <CommonMistakesList mistakes={lesson.commonMistakes} />
          </Section>
        )}

        {/* 08 · Your turn */}
        <Section n="08" label="Your turn">
          <div className="space-y-4">
            {lesson.tryIt.map((problem, i) => (
              <RevealProblemCard
                key={problem.id}
                problem={problem}
                index={i}
                labels={REVEAL_LABELS}
              />
            ))}
          </div>
        </Section>
      </div>
    </div>
  );
}

// Content requires an account; the hub and topic pages above stay public.
export default function GenMathLessonPage() {
  const params = useParams();
  const topicSlug = params.topic as string;
  return (
    <ContentGate backHref={`/math/9/${topicSlug}`} backLabel="Back to topic">
      <GenMathLessonPageInner />
    </ContentGate>
  );
}
