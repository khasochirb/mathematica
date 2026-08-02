"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft, ArrowRight } from "lucide-react";
import MathText from "@/components/esh/MathText";
import { getQuestionsByTopic } from "@/lib/esh-questions";
import { getLesson } from "@/lib/esh-lessons";
import LessonWorkedExamples from "@/components/esh/lesson/LessonWorkedExamples";
import LessonTryIt from "@/components/esh/lesson/LessonTryIt";
import LessonCommonMistakes from "@/components/esh/lesson/LessonCommonMistakes";
import Section from "@/components/lesson/Section";
import FactCard from "@/components/lesson/FactCard";
import { CourseSpineList } from "@/components/course/CourseShell";
import { eshCourseDef, getEshTopicCourse, liveUnitCount } from "@/lib/esh-course";
import topicsData from "@/data/learn/topics.json";

// One ЭЕШ exam topic. The course spine comes FIRST — this page used to be a
// formula sheet, and the formula sheet is now the reference you keep open
// beside the course rather than the whole of what the topic offers.

type LegacyTopic = {
  title: string;
  overview: string;
  formulas: { title: string; latex: string }[];
  tips: string[];
};

export default function TopicLearnPage() {
  const params = useParams();
  const topicSlug = params.topicSlug as string;

  const course = getEshTopicCourse(topicSlug);
  const courseDef = eshCourseDef(topicSlug);
  const lesson = getLesson(topicSlug);
  const data = (topicsData as Record<string, LegacyTopic>)[topicSlug];
  const questionCount = getQuestionsByTopic(topicSlug).length;

  if (!course && !data && !lesson) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <div className="text-center">
          <p className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
            Сэдэв <em className="serif-italic" style={{ color: "var(--accent)" }}>олдсонгүй</em>.
          </p>
          <Link href="/practice/esh/learn" className="btn btn-line mt-5 inline-flex">
            <ArrowLeft className="mr-1 h-3.5 w-3.5" /> Буцах
          </Link>
        </div>
      </div>
    );
  }

  const title = course?.title ?? data?.title ?? lesson?.title ?? "";
  const live = liveUnitCount(topicSlug);
  const total = course?.units.length ?? 0;

  // Section numbers are assigned in render order, so the page reads 01, 02,
  // 03 … whichever of the optional blocks a topic actually has.
  let n = 0;
  const num = () => String(++n).padStart(2, "0");

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-12">
        <div className="flex items-center gap-3 mb-6">
          <Link
            href="/practice/esh/learn"
            className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">ЭЕШ · Суралцах · {questionCount} бодлого</div>
        </div>

        <h1
          className="serif"
          style={{
            fontWeight: 400,
            fontSize: "clamp(36px, 5vw, 56px)",
            letterSpacing: "-0.04em",
            lineHeight: 1,
            color: "var(--fg)",
          }}
        >
          {title}
        </h1>
        {course && (
          <p className="mt-4" style={{ color: "var(--fg-1)", fontSize: 17, lineHeight: 1.55, maxWidth: "58ch" }}>
            {course.intro}
          </p>
        )}

        {/* The course itself. (The legacy formula sheet and tips that used
            to follow were cut 2026-08-01 by owner decision — the course
            teaches; the problem bank below is where the numbers get used.) */}
        {course && courseDef && (
          <Section n={num()} label="Курс">
            <p className="text-[13px] mb-4" style={{ color: "var(--fg-2)" }}>
              {live > 0
                ? `${total} нэгжээс ${live} нь бэлэн — хичээл, дадлага, өөрийгөө шалгах тесттэй. Хичээлүүд одоогоор англи хэлээр; монгол орчуулга дараа нэмэгдэнэ.`
                : `${total} нэгж бэлтгэгдэж байна.`}
            </p>
            <CourseSpineList course={courseDef} />
          </Section>
        )}

        {/* Problem bank — directly below the course, per owner decision. */}
        <Section n={num()} label="Бодлогын сан">
          <Link
            href="/practice/esh/practice"
            className="card-edit p-5 flex items-center gap-4 group"
            style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
          >
            <div className="flex-1">
              <p className="serif" style={{ fontWeight: 400, fontSize: 18, color: "var(--fg)" }}>
                Энэ сэдвээр <em className="serif-italic" style={{ color: "var(--accent)" }}>дадлага</em> хийх
              </p>
              <p className="mono text-[11px] mt-1" style={{ color: "var(--fg-2)", letterSpacing: "0.04em" }}>
                {questionCount} БОДЛОГО БЭЛЭН
              </p>
            </div>
            <ArrowRight className="w-5 h-5 flex-shrink-0" style={{ color: "var(--accent)" }} />
          </Link>
        </Section>

        {/* The hand-authored ЭЕШ lesson, where one exists for this topic. */}
        {lesson && (
          <>
            <Section n={num()} label="Зорилго">
              <p className="font-sans" style={{ fontSize: 17, lineHeight: 1.55, color: "var(--fg-1)" }}>
                {lesson.objective}
              </p>
            </Section>

            <Section n={num()} label="Үзэл баримтлал">
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
                  <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>
                    Гол санаа
                  </div>
                  <p className="text-[14px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
                    <MathText text={lesson.keyIdea} />
                  </p>
                </div>
              )}
            </Section>

            <Section n={num()} label="Томьёо ба тодорхойлолт">
              <div className="space-y-3">
                {lesson.formulas.map((f, i) => (
                  <FactCard key={i} fact={f} />
                ))}
              </div>
            </Section>

            <Section n={num()} label="Бодсон жишээ">
              <LessonWorkedExamples lesson={lesson} />
            </Section>

            {lesson.commonMistakes.some((m) => m.authored) && (
              <Section n={num()} label="Түгээмэл алдаа">
                <LessonCommonMistakes lesson={lesson} />
              </Section>
            )}

            <Section n={num()} label="Өөрөө бод">
              <LessonTryIt lesson={lesson} />
            </Section>
          </>
        )}

      </div>
    </div>
  );
}
