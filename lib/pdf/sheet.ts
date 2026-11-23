// Builds the printable worksheet model from the same data the site renders.
//
// Pure apart from the (static, bundled) data imports, so the numbering and
// answer key are unit-testable. SERVER ONLY in practice: the print page calls
// it in a server component and hands the result to the client renderer, so
// the whole corpus never ships to the browser.

import type { FigureSpec, GeoDiagramSpec } from "@/lib/genmath-interactive";
import {
  type BankForm,
  type BankTopic,
  LEVEL_LABELS,
  localizeTopic,
  unitForms,
} from "@/lib/problem-bank";
import { getBankMirrorMn, getBankTopic, getIbBankTopic, getSatBankTopic } from "@/lib/bank-data";
import { formAnswerMode, seededOptionOrder } from "@/lib/bank-answer";
import { buildSlots, spreadIndex } from "@/lib/bank-slots";
import { getCourseExam } from "@/lib/course-exam";
import { EXAMS_MN } from "@/lib/course-exam-mn";
import { getTestInfo } from "@/lib/esh-questions";
import { getTestSection2, parseSlotLabel } from "@/lib/esh-section2";
import type { PdfOptions } from "./options";

export type SheetImage = { src: string; width: number; height: number; alt: string };

export type SheetItem = {
  /** The number the site shows ("7", "2.3"). */
  n: string;
  /** A heading printed before this item (a part or exam section). */
  heading?: string;
  /** Shared context printed above the item (ЭШ section 2). */
  context?: string;
  statement: string;
  options?: { label: string; text: string }[];
  geoFigure?: GeoDiagramSpec;
  figure?: FigureSpec;
  image?: SheetImage;
  /** Answer-key text (may hold $…$ maths). */
  answer: string;
};

export type Sheet = {
  lang: "mn" | "en";
  title: string;
  subtitle: string;
  items: SheetItem[];
  /** Site path with the step-by-step solutions, printed with the key. */
  solutionsPath: string;
  /** "browse": solutions open problem by problem on that page.
   *  "sit": the paper is sat online first, then every solution is shown. */
  solutionsMode: "browse" | "sit";
};

const LETTERS = ["A", "B", "C", "D", "E", "F"];

// ---------------------------------------------------------------------------
// Problem bank unit
// ---------------------------------------------------------------------------

export function resolveBank(slug: string): { topic: BankTopic; unitPath: (unit: string) => string } | null {
  const course = getBankTopic(slug);
  if (course) return { topic: course, unitPath: (u) => `/math/problem-bank/${slug}/${u}` };
  if (slug === "sat") return { topic: getSatBankTopic(), unitPath: (u) => `/practice/sat/bank/${u}` };
  if (slug === "ib-sl" || slug === "ib-hl") {
    const tier = slug === "ib-sl" ? "sl" : "hl";
    return { topic: getIbBankTopic(tier), unitPath: (u) => `/practice/ib/bank/${tier}/${u}` };
  }
  return null;
}

/** The unit's forms in the browse page's order for a level filter. */
export function orderedForms(topic: BankTopic, unitId: string, level: 0 | 1 | 2 | 3): BankForm[] {
  return unitForms(topic, unitId)
    .filter((f) => level === 0 || f.level === level)
    .sort((a, b) => a.level - b.level);
}

function bankSheet(o: PdfOptions & { source: { kind: "bank" } }): Sheet | null {
  const s = o.source;
  const found = resolveBank(s.bank);
  if (!found) return null;
  const topic = o.lang === "mn" ? localizeTopic(found.topic, getBankMirrorMn(found.topic.slug)) : found.topic;
  const unit = topic.units.find((u) => u.id === s.unit);
  if (!unit) return null;
  const forms = orderedForms(topic, unit.id, s.level);
  if (forms.length === 0) return null;
  const maxRounds = forms.reduce((m, f) => Math.max(m, f.variants.length), 0);
  let slots = buildSlots(forms, maxRounds);
  if (s.count !== "all") slots = slots.slice(0, s.count);

  const items: SheetItem[] = slots.map((slot, i) => {
    const form = slot.form;
    const v = form.variants[spreadIndex(slot.round, form.variants.length)] ?? form.variants[0];
    if (v.answerFormat === "self") {
      return { n: String(i + 1), statement: v.statement, geoFigure: v.geoFigure, figure: v.figure, answer: v.modelAnswer ?? "" };
    }
    const correct = v.options[v.correctIndex] ?? "";
    if (formAnswerMode(form) === "numeric") {
      return { n: String(i + 1), statement: v.statement, geoFigure: v.geoFigure, figure: v.figure, answer: correct };
    }
    // Same salt as the browse page's AnswerPrompt, so the letters match.
    const disp = seededOptionOrder(v, v.id);
    return {
      n: String(i + 1),
      statement: v.statement,
      options: disp.options.map((text, k) => ({ label: LETTERS[k], text })),
      geoFigure: v.geoFigure,
      figure: v.figure,
      answer: `${LETTERS[disp.correctIndex]}) ${disp.options[disp.correctIndex]}`,
    };
  });

  const mn = o.lang === "mn";
  const levelNote = s.level === 0 ? "" : ` · ${mn ? `Түвшин ${s.level}` : LEVEL_LABELS[s.level]}`;
  return {
    lang: o.lang,
    title: unit.title,
    subtitle: `${mn ? topic.titleMn || topic.title : topic.title}${levelNote}`,
    items,
    solutionsPath: found.unitPath(unit.id),
    solutionsMode: "browse",
  };
}

// ---------------------------------------------------------------------------
// Course exam
// ---------------------------------------------------------------------------

function examSheet(o: PdfOptions & { source: { kind: "exam" } }): Sheet | null {
  const en = getCourseExam(o.source.examId);
  if (!en) return null;
  const exam = (o.lang === "mn" ? EXAMS_MN[o.source.examId] : null) ?? en;
  const mn = o.lang === "mn" && exam !== en;
  const items: SheetItem[] = exam.questions.map((q, i) => ({
    n: String(i + 1),
    statement: q.statement,
    options: q.options.map((text, k) => ({ label: LETTERS[k], text })),
    geoFigure: q.geoFigure,
    answer: `${LETTERS[q.correctIndex]}) ${q.options[q.correctIndex]}`,
  }));
  const minutes = exam.meta.minutes;
  return {
    lang: mn ? "mn" : "en",
    title: exam.meta.label,
    subtitle: [
      exam.meta.label.includes(exam.meta.courseTitle) ? null : exam.meta.courseTitle,
      mn ? `${items.length} бодлого` : `${items.length} questions`,
      mn ? `${minutes} минут` : `${minutes} minutes`,
    ]
      .filter(Boolean)
      .join(" · "),
    items,
    solutionsPath: `/math/${en.meta.course}/exam`,
    solutionsMode: "sit",
  };
}

// ---------------------------------------------------------------------------
// ЭШ paper (Mongolian only)
// ---------------------------------------------------------------------------

/** `[a]` slots shown as boxes, as on the site's section 2 card. */
export function boxSlots(text: string): string {
  return text.replace(/\[([A-Za-z0-9]+)\]/g, (_m, label: string) => {
    const { prefix, varPart } = parseSlotLabel(label);
    return `${prefix}\\boxed{${varPart}}`;
  });
}

function eshSheet(o: PdfOptions & { source: { kind: "esh" } }): Sheet | null {
  const info = getTestInfo(o.source.testKey);
  if (!info) return null;
  const items: SheetItem[] = info.data.map((q, i) => {
    const entries = Object.entries(q.options ?? {});
    const answerText = q.options?.[q.answer];
    return {
      n: String(q.questionNumber ?? i + 1),
      heading: i === 0 ? "I хэсэг" : undefined,
      statement: q.body,
      options: entries.length ? entries.map(([label, text]) => ({ label, text })) : undefined,
      image: q.figure
        ? { src: q.figure.src, width: q.figure.width, height: q.figure.height, alt: q.figure.alt_mn }
        : undefined,
      answer: answerText ? `${q.answer}) ${answerText}` : q.answer,
    };
  });
  const s2 = getTestSection2(o.source.testKey) ?? [];
  let lastProblem = "";
  s2.forEach((it, i) => {
    const first = it.problem !== lastProblem;
    lastProblem = it.problem;
    items.push({
      n: `${it.problem}.${it.subproblem}`,
      heading: i === 0 ? "II хэсэг" : undefined,
      context: first ? it.context : undefined,
      statement: boxSlots(it.instruction),
      image: first && it.figure
        ? { src: it.figure.src, width: it.figure.width, height: it.figure.height, alt: it.figure.alt_mn }
        : undefined,
      answer: it.slots.map((sl) => `$${sl.label} = ${sl.answer}$`).join(", "),
    });
  });
  return {
    lang: "mn",
    title: info.label,
    subtitle: s2.length
      ? `I хэсэг: ${info.data.length} бодлого · II хэсэг: ${new Set(s2.map((x) => x.problem)).size} бодлого`
      : `${info.data.length} бодлого`,
    items,
    // The list, not the paper: opening the paper itself starts the timer.
    solutionsPath: `/practice/esh/test?type=${info.isPracticeSet ? "practice" : "previous"}`,
    solutionsMode: "sit",
  };
}

export function buildSheet(o: PdfOptions): Sheet | null {
  const s = o.source;
  if (s.kind === "bank") return bankSheet({ ...o, source: s });
  if (s.kind === "exam") return examSheet({ ...o, source: s });
  return eshSheet({ ...o, source: s });
}
