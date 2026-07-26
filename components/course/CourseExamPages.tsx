import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft, Clock, Layers, FileText } from "lucide-react";
import ExamRunner from "@/components/course/ExamRunner";
import { getCourseExam, getCourseExams } from "@/lib/course-exam";

// Server components for the two exam routes. The runner itself is a client
// component; these only resolve the exam and render chrome, which keeps the
// 204-question payload off every course page that merely LINKS to an exam.

export function generateExamParams(course: string) {
  return getCourseExams(course).map((e) => ({ examId: e.meta.examId }));
}

export function CourseExamListPage({ course }: { course: string }) {
  const exams = getCourseExams(course);
  if (exams.length === 0) notFound();
  const title = exams[0].meta.courseTitle;

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        <div className="flex items-center gap-3 mb-6">
          <Link
            className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
            href={`/math/${course}`}
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">{title}</div>
        </div>

        <h1
          className="serif"
          style={{ fontWeight: 400, fontSize: "clamp(30px,5vw,50px)", letterSpacing: "-0.04em", lineHeight: 1.05, color: "var(--fg)" }}
        >
          Practice Exams
        </h1>
        <p className="mt-4 mb-8" style={{ color: "var(--fg-1)", fontSize: 17, maxWidth: "56ch" }}>
          {exams[0].meta.intro} The three papers share no questions, so you can sit all of them.
        </p>

        <ol className="space-y-3">
          {exams.map((e, i) => (
            <li key={e.meta.examId}>
              <Link
                className="card-edit p-5 flex items-start gap-4 transition-colors"
                style={{ textDecoration: "none" }}
                href={`/math/${course}/exam/${e.meta.examId}`}
              >
                <span
                  className="mono text-[11px] flex-shrink-0 tabular mt-1"
                  style={{ color: "var(--accent)", letterSpacing: "0.04em", minWidth: 24 }}
                >
                  {String(i + 1).padStart(2, "0")}
                </span>
                <span className="flex-1 min-w-0">
                  <span
                    className="serif block"
                    style={{ fontWeight: 400, fontSize: 18, letterSpacing: "-0.01em", color: "var(--fg)" }}
                  >
                    {e.meta.label}
                  </span>
                  <span className="flex gap-4 mt-2 text-[12px]" style={{ color: "var(--fg-2)" }}>
                    <span className="flex items-center gap-1.5">
                      <FileText className="w-3.5 h-3.5" /> {e.meta.totalQuestions} questions
                    </span>
                    <span className="flex items-center gap-1.5">
                      <Layers className="w-3.5 h-3.5" /> {e.meta.unitsCovered} units
                    </span>
                    <span className="flex items-center gap-1.5">
                      <Clock className="w-3.5 h-3.5" /> ~{e.meta.minutes} min
                    </span>
                  </span>
                </span>
                <span
                  className="mono text-[10px] uppercase mt-1 flex-shrink-0"
                  style={{ color: "var(--accent)", letterSpacing: "0.08em" }}
                >
                  Start
                </span>
              </Link>
            </li>
          ))}
        </ol>
      </div>
    </div>
  );
}

export function CourseExamPage({ examId }: { examId: string }) {
  const exam = getCourseExam(examId);
  if (!exam) notFound();
  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <ExamRunner exam={exam} />
    </div>
  );
}
