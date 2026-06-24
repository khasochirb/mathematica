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
import topicsData from "@/data/learn/topics.json";

type LegacyTopic = {
  title: string;
  overview: string;
  formulas: { title: string; latex: string }[];
  tips: string[];
};

export default function TopicLearnPage() {
  const params = useParams();
  const topicSlug = params.topicSlug as string;
  const lesson = getLesson(topicSlug);
  const questionCount = getQuestionsByTopic(topicSlug).length;

  if (lesson) {
    return (
      <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-12">
          <div className="flex items-center gap-3 mb-6">
            <Link href="/practice/esh/learn" className="p-2 rounded-md transition-colors"
              style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
              <ArrowLeft className="w-4 h-4" />
            </Link>
            <div className="eyebrow">ЭЕШ · Суралцах · {questionCount} бодлого</div>
          </div>

          <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(36px, 5vw, 56px)", letterSpacing: "-0.04em", lineHeight: 1, color: "var(--fg)" }}>
            {lesson.title}
          </h1>
          {lesson.subtitle && (
            <p className="serif mt-2" style={{ fontSize: 18, color: "var(--fg-2)" }}>{lesson.subtitle}</p>
          )}

          <Section n="01" label="Зорилго">
            <p className="serif" style={{ fontSize: 17, lineHeight: 1.55, color: "var(--fg-1)" }}>{lesson.objective}</p>
          </Section>

          <Section n="02" label="Үзэл баримтлал">
            <div className="space-y-4">
              {lesson.concept.map((para, i) => (
                <p key={i} className="serif" style={{ fontSize: 17, lineHeight: 1.6, color: "var(--fg-1)" }}>
                  <MathText text={para} />
                </p>
              ))}
            </div>
            {lesson.keyIdea && (
              <div className="card-edit p-4 mt-4" style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}>
                <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>Гол санаа</div>
                <p className="text-[14px] leading-relaxed" style={{ color: "var(--fg-1)" }}><MathText text={lesson.keyIdea} /></p>
              </div>
            )}
          </Section>

          <Section n="03" label="Томьёо ба тодорхойлолт">
            <div className="space-y-3">
              {lesson.formulas.map((f, i) => (
                <FactCard key={i} fact={f} />
              ))}
            </div>
          </Section>

          <Section n="04" label="Бодсон жишээ">
            <LessonWorkedExamples lesson={lesson} />
          </Section>

          {lesson.commonMistakes.some((m) => m.authored) && (
            <Section n="05" label="Түгээмэл алдаа">
              <LessonCommonMistakes lesson={lesson} />
            </Section>
          )}

          <Section n="06" label="Өөрөө бод">
            <LessonTryIt lesson={lesson} />
          </Section>
        </div>
      </div>
    );
  }

  // ---- Legacy fallback (topics.json 3-section view) ----
  const data = (topicsData as Record<string, LegacyTopic>)[topicSlug];
  if (!data) {
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

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-12">
        <div className="flex items-center gap-3 mb-6">
          <Link href="/practice/esh/learn" className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">ЭЕШ · Суралцах · {questionCount} бодлого</div>
        </div>
        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(36px, 5vw, 56px)", letterSpacing: "-0.04em", lineHeight: 1, color: "var(--fg)" }}>
          {data.title}
        </h1>
        <Section n="01" label="Тойм">
          <p className="serif" style={{ fontSize: 17, lineHeight: 1.55, color: "var(--fg-1)" }}>{data.overview}</p>
        </Section>
        <Section n="02" label="Гол томьёонууд">
          <div className="space-y-3">
            {data.formulas.map((formula, i) => (
              <div key={i} className="card-edit p-5">
                <div className="flex items-baseline gap-3 mb-2">
                  <span className="mono text-[10px]" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>{String(i + 1).padStart(2, "0")}</span>
                  <p className="serif" style={{ fontWeight: 400, fontSize: 14, color: "var(--accent)" }}>{formula.title}</p>
                </div>
                <div className="q-math text-[15px]" style={{ color: "var(--fg)" }}><MathText text={formula.latex} /></div>
              </div>
            ))}
          </div>
        </Section>
        <Section n="03" label="Зөвлөгөө">
          <ul className="card-edit p-2">
            {data.tips.map((tip, i) => (
              <li key={i} className="flex items-start gap-3 px-4 py-3" style={{ borderBottom: i < data.tips.length - 1 ? "1px solid var(--line)" : "none" }}>
                <span className="mono tabular text-[10px] mt-1 flex-shrink-0" style={{ color: "var(--accent)", letterSpacing: "0.06em" }}>{String(i + 1).padStart(2, "0")}</span>
                <p className="text-[14px] leading-relaxed" style={{ color: "var(--fg-1)" }}>{tip}</p>
              </li>
            ))}
          </ul>
        </Section>
        <Link href="/practice/esh/practice" className="card-edit p-5 flex items-center gap-4 mt-10 group"
          style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}>
          <div className="flex-1">
            <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>Дараа нь</div>
            <p className="serif" style={{ fontWeight: 400, fontSize: 18, color: "var(--fg)" }}>
              Энэ сэдвээр <em className="serif-italic" style={{ color: "var(--accent)" }}>дадлага</em> хийх
            </p>
            <p className="mono text-[11px] mt-1" style={{ color: "var(--fg-2)", letterSpacing: "0.04em" }}>{questionCount} БОДЛОГО БЭЛЭН</p>
          </div>
          <ArrowRight className="w-5 h-5 flex-shrink-0" style={{ color: "var(--accent)" }} />
        </Link>
      </div>
    </div>
  );
}
