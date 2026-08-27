// Chrome vocabulary — Mongolian for the navigation, buttons, labels, headers,
// units, and empty/error states that are currently hardcoded English.
//
// ═══ STATUS: DRAFT, NOT WIRED. Awaiting Khas's corrections. ═══
//
// Nothing imports this yet, deliberately. Wiring it before the wording is
// approved would put un-reviewed Mongolian in front of students, and the
// wording is the part only a Mongolian speaker can settle. Once corrected,
// this becomes the dictionary the ~120 English-only pages read from.
//
// WHERE THE WORDS COME FROM. Every entry is marked:
//   SITE  — this exact English string already has a Mongolian on the site,
//           copied verbatim. Two Mongolian words for one English word is how
//           a product starts feeling machine-made, so these are not up for
//           debate unless the existing usage is itself wrong. Mechanically
//           verified against every en/mn pair in the bilingual files.
//   DERIV — built from a RELATED site string, not copied from an exact match
//           («Unit» from «Нэгжээр»/«Хамгийн сул нэгж»). The stem is
//           established; the form is mine, so the ending may be wrong.
//   GLOSS — fixed by the mn-translation glossary or by ministry order А/492.
//           Not free to change without changing the glossary.
//   NEW   — proposed here. THESE ARE THE ONES TO CORRECT. They are modelled
//           on the SITE entries' register and morphology, but I do not speak
//           Mongolian and cannot judge whether they read naturally.
//   VOICE — NOT MINE TO WRITE, and `mn` is deliberately empty. Per
//           docs/MONGOLIAN.md, anything that persuades or speaks to a student
//           is Khas's, and Claude never proposes a draft for it — a draft
//           anchors the writing, which is the whole reason for the rule.
//           Nine strings moved here on 26 Aug; my earlier Mongolian for them
//           is withdrawn, not offered. See memory/mn-group1-audits.md §3.
//
// REGISTER: «та», formal. Khas, 26 Aug 2026 — "чи is usually not used for
// customers. it is not suitable." A student here is a customer, and the voice
// strings Khas wrote confirm it: «Танд чухал зүйл», «Таны баталгаажуулах
// холбоосны хугацаа дууссан байна».
//
// THIS REVERSES what the mn-translation skill says, and the skill is wrong.
// It reads "friendly-instructional «чи» ... never formal «та»", which is how
// grades 6 and 7 came to be written in «чи» — 267 strings. Grade 8, which the
// register audit flagged as off-register for using «та», turns out to have
// been right. See memory/mn-group1-audits.md §1 and the ruling recorded there.
//
// Guillemets «...» for quotes.
//
// COUNTS are occurrences of the English string across the non-bilingual
// files, measured 26 Aug 2026. They rank the work: "Unit" at 36 is worth
// more than any singleton.

export type ChromeEntry = {
  en: string;
  mn: string;
  /** SITE = verbatim from the site · DERIV = built from a related site string · GLOSS = glossary-locked · NEW = proposed, please correct · VOICE = Khas writes it, `mn` is deliberately empty */
  src: "SITE" | "DERIV" | "GLOSS" | "NEW" | "VOICE";
  /** occurrences across English-only files */
  n?: number;
  /** why this wording, where it is not obvious */
  note?: string;
};

// ---------------------------------------------------------------------------
// 1. Structure words — the course skeleton. Highest-frequency, so the most
//    important to get right; a wrong word here is wrong on 36 pages.
// ---------------------------------------------------------------------------
export const STRUCTURE: ChromeEntry[] = [
  { en: "Unit", mn: "Нэгж", src: "DERIV", n: 36, note: 'from "By unit"→«Нэгжээр», "Weakest unit"→«Хамгийн сул нэгж»' },
  { en: "Lesson", mn: "Хичээл", src: "DERIV", n: 15 },
  { en: "Lessons", mn: "Хичээлүүд", src: "NEW", n: 15, note: 'site has "Lessons"→«Хичээл» (unmarked plural) as a TAB label; as a countable heading the plural may read better — your call which wins' },
  { en: "Topic", mn: "Сэдэв", src: "SITE", n: 9 },
  { en: "Courses", mn: "Курсууд", src: "SITE", n: 9 },
  { en: "Practice", mn: "Дасгал", src: "SITE", n: 15 },
  { en: "Test yourself", mn: "Өөрийгөө шалга", src: "SITE", n: 15 },
  { en: "Problem bank", mn: "Бодлогын сан", src: "SITE", n: 2 },
  { en: "Premium", mn: "Премиум", src: "SITE", n: 3 },
  { en: "Contact", mn: "Холбоо барих", src: "SITE", n: 3 },
];

// ---------------------------------------------------------------------------
// 2. Navigation — "Back to X". The site's one established pattern is
//    "Back to practice" → «Дасгал руу буцах», i.e. <target> + руу буцах.
//    Every entry below follows it. Note that Mongolian directional case
//    varies with the final sound of the noun (руу / рүү), which is exactly
//    the kind of thing I will have got wrong somewhere.
// ---------------------------------------------------------------------------
export const NAV: ChromeEntry[] = [
  { en: "Back", mn: "Буцах", src: "NEW", n: 5 },
  { en: "Back to the course", mn: "Курс руу буцах", src: "NEW", n: 35, note: "the single most common chrome string on the site" },
  { en: "Back to unit", mn: "Нэгж рүү буцах", src: "NEW", n: 12, note: "рүү not руу after front-vowel «нэгж» — please confirm" },
  { en: "Back to topic", mn: "Сэдэв рүү буцах", src: "NEW", n: 3 },
  { en: "Back to Grade 10", mn: "10-р анги руу буцах", src: "NEW", n: 3 },
  { en: "Back to Grade 11", mn: "11-р анги руу буцах", src: "NEW", n: 3 },
  { en: "Back to Grade 12", mn: "12-р анги руу буцах", src: "NEW", n: 3 },
  { en: "Back to Geometry", mn: "Геометр рүү буцах", src: "NEW", n: 3 },
  { en: "Back to the SAT hub", mn: "SAT хэсэг рүү буцах", src: "NEW", n: 1, note: "SAT stays Latin (glossary rule 2)" },
  { en: "Back to the IB hub", mn: "IB хэсэг рүү буцах", src: "NEW", n: 1 },
  { en: "Next", mn: "Дараах", src: "DERIV", n: 4, note: 'site has "Next →"→«Дараах →»' },
  { en: "Previous", mn: "Өмнөх", src: "NEW", n: 2 },
  { en: "Next step", mn: "Дараагийн алхам", src: "NEW", n: 2 },
  { en: "Start", mn: "Эхлэх", src: "SITE", n: 15 },
  { en: "Continue", mn: "Үргэлжлүүлэх", src: "SITE" },
  { en: "Soon", mn: "Удахгүй", src: "VOICE", n: 15, note: "badge on unbuilt doors (rule 7 legacy tier) — must read as a promise, not an apology" },
];

// ---------------------------------------------------------------------------
// 3. Buttons and controls, including the interactive widgets' own controls.
// ---------------------------------------------------------------------------
export const CONTROLS: ChromeEntry[] = [
  { en: "Reset", mn: "Дахин эхлэх", src: "NEW", n: 20, note: "«Цэвэрлэх» (clear) would be wrong — these widgets return to a start state, they do not empty" },
  { en: "Check", mn: "Шалгах", src: "NEW", n: 2 },
  { en: "Move left", mn: "Зүүн тийш", src: "NEW", n: 2 },
  { en: "Move right", mn: "Баруун тийш", src: "NEW", n: 2 },
  { en: "Larger", mn: "Томсгох", src: "NEW", n: 5, note: "verb (do this) not adjective — these are buttons" },
  { en: "Smaller", mn: "Жижигрүүлэх", src: "NEW", n: 5 },
  { en: "Show solution", mn: "Бодолтыг харах", src: "NEW", note: 'site has "Review the solution"→«Бодолтыг дахин үзэх»; first viewing is харах not дахин үзэх' },
  { en: "Hide", mn: "Нуух", src: "NEW" },
  { en: "Hide solution", mn: "Бодолтыг нуух", src: "NEW" },
  { en: "Review every question", mn: "Бодлого бүрийг эргэн харах", src: "NEW", n: 2 },
  { en: "Take the placement test", mn: "Түвшин тогтоох тест өгөх", src: "SITE", n: 5 },
  { en: "Orbit again", mn: "Дахин эргүүлэх", src: "NEW", n: 2 },
  { en: "Race again", mn: "Дахин уралдуулах", src: "NEW", n: 2 },
  { en: "Compound again", mn: "Дахин хүү бодох", src: "NEW", n: 1 },
  { en: "Rotate line", mn: "Шулууныг эргүүлэх", src: "NEW", n: 2 },
  { en: "Tilt transversal", mn: "Огтлогчийг налуулах", src: "NEW", n: 2, note: "«огтлогч» = transversal; confirm against the ministry standard's geometry vocabulary" },
  { en: "Add column", mn: "Багана нэмэх", src: "NEW", n: 1 },
];

// ---------------------------------------------------------------------------
// 4. Lesson section headings. These recur inside every lesson page, so they
//    set the reading rhythm more than any other group. The mn-translation
//    glossary already fixes several — those are GLOSS and are not negotiable
//    here, because the shipped grade 6/7/8 mirrors already use them.
// ---------------------------------------------------------------------------
export const SECTIONS: ChromeEntry[] = [
  { en: "Worked examples", mn: "Бодсон жишээнүүд", src: "GLOSS", n: 3 },
  { en: "Try this", mn: "Өөрөө туршиж үз", src: "GLOSS", n: 3 },
  { en: "Your turn", mn: "Өөрөө туршиж үз", src: "GLOSS", n: 3, note: "EN uses two headings for one idea; the glossary has one. Flagging rather than inventing a second — do you want them distinguished?" },
  { en: "Quick check", mn: "Түргэн шалгалт", src: "GLOSS" },
  { en: "Play with it", mn: "Тоглож үз", src: "GLOSS" },
  { en: "Fun fact", mn: "Сонирхолтой баримт", src: "GLOSS" },
  { en: "Recap", mn: "Эргэн дүгнэлт", src: "GLOSS" },
  { en: "What you learned", mn: "Юу сурснаа эргэн харъя", src: "GLOSS" },
  { en: "What you'll learn", mn: "Юу сурах вэ", src: "NEW", n: 3, note: "the glossary's «Юу сурснаа эргэн харъя» is past-tense (end of lesson); this is the start-of-lesson heading and needs its own future form" },
  { en: "Key idea", mn: "Гол санаа", src: "NEW", n: 3 },
  { en: "The idea", mn: "Санаа нь", src: "NEW", n: 3 },
  { en: "Key facts", mn: "Гол баримтууд", src: "NEW", n: 3 },
  { en: "Watch out", mn: "Болгоомжил", src: "NEW", n: 3, note: "heads the common-mistakes block" },
  { en: "Real-world picture", mn: "Бодит амьдрал дээр", src: "NEW", n: 3 },
  { en: "Builds on", mn: "Уг нь тулгуурлах", src: "NEW", n: 12, note: "LOW CONFIDENCE. Labels the prerequisite list on a unit page. Wants a natural Mongolian phrase for «you need this first», not a literal rendering of the English metaphor — please rewrite freely." },
  { en: "Focus first on", mn: "Түрүүнд анхаарах зүйл", src: "VOICE", n: 5, note: 'site: "Focus units"→«Анхаарах нэгжүүд»' },
  { en: "Important for you", mn: "Танд чухал зүйл", src: "VOICE", n: 4, note: "recommendation banner. Khas wrote this; «танд» is correct — see the register ruling in the header." },
  { en: "Ready to check yourself?", mn: "Өөрийгөө шалгаад үзэх үү?", src: "VOICE", n: 12 },
  { en: "Self-graded", mn: "Өөрийгөө дүгнэ", src: "SITE", n: 15 },
];

// ---------------------------------------------------------------------------
// 5. Forms, auth, and field labels.
// ---------------------------------------------------------------------------
export const FORMS: ChromeEntry[] = [
  { en: "Email", mn: "И-мэйл", src: "SITE" },
  { en: "Username", mn: "Хэрэглэгчийн нэр", src: "SITE" },
  { en: "Password", mn: "Нууц үг", src: "DERIV", n: 2, note: "established in DeleteAccountPanel" },
  { en: "Full name", mn: "Бүтэн нэр", src: "NEW" },
  { en: "Your answer", mn: "Таны хариу", src: "SITE", n: 3 },
  { en: "first number", mn: "эхний тоо", src: "NEW", n: 2 },
  { en: "second number", mn: "хоёр дахь тоо", src: "NEW", n: 2 },
  { en: "At least 8 characters", mn: "Дор хаяж 8 тэмдэгт", src: "NEW" },
  { en: "Free to join", mn: "Үнэгүй нэгд", src: "VOICE" },
  { en: "Sign up again", mn: "Дахин бүртгүүлэх", src: "NEW", n: 2 },
  { en: "Choose your level", mn: "Өөрийн анги, түвшинээ сонгох", src: "VOICE", n: 1 },
  { en: "you@example.com", mn: "you@example.com", src: "NEW", n: 2, note: "placeholder stays Latin — it is an example address, not prose" },
];

// ---------------------------------------------------------------------------
// 6. Empty and error states. The ones that matter most and get looked at
//    least: a student meets these when something has already gone wrong.
//    Tone target — say what happened and what to do, never blame the reader.
// ---------------------------------------------------------------------------
export const STATES: ChromeEntry[] = [
  { en: "Unit not found", mn: "Нэгж олдсонгүй", src: "DERIV", note: 'from "Question not found"→«Бодлого олдсонгүй»' },
  { en: "Lesson not found", mn: "Хичээл олдсонгүй", src: "DERIV" },
  { en: "Topic not found", mn: "Сэдэв олдсонгүй", src: "DERIV" },
  { en: "Coming soon.", mn: "Удахгүй нэмэгдэнэ.", src: "NEW", n: 1 },
  {
    en: "Complete a mock test and your trajectory appears here.",
    mn: "Жишиг тестнээс гүйцэтгээд аялалаа эхлүүлээрэй",
    src: "VOICE",
    n: 1,
    note: 'built from the established "Complete a test to plot your trajectory."→«Графикийг үзэхийн тулд тест дуусгана уу.» and "Score trajectory"→«Онооны өсөлт»',
  },
  {
    en: "Your confirmation link expired. Enter your email to resend.",
    mn: "Таны баталгаажуулах холбоосны хугацаа дууссан байна",
    src: "VOICE",
  },
  { en: "Confirmation email sent. Check your inbox.", mn: "", src: "VOICE" },
];

// ---------------------------------------------------------------------------
// 7. Measures and column headers.
// ---------------------------------------------------------------------------
export const MEASURES: ChromeEntry[] = [
  { en: "Accuracy", mn: "Зөв хариулсан хувь", src: "SITE", n: 1 },
  { en: "Complete", mn: "Дууссан", src: "NEW", n: 1 },
  { en: "Actions", mn: "Үйлдэл", src: "NEW", n: 1 },
  { en: "By unit", mn: "Нэгжээр", src: "SITE", n: 2 },
  { en: "By domain", mn: "Хэсгээр", src: "NEW", n: 2 },
  { en: "By syllabus topic", mn: "Хөтөлбөрийн сэдвээр", src: "NEW", n: 1 },
  { en: "All units", mn: "Бүх нэгж", src: "NEW", n: 1 },
  { en: "All levels", mn: "Бүх түвшин", src: "NEW", n: 1 },
  { en: "Factors of", mn: "-ын хуваагчид", src: "NEW", n: 3, note: "GRAMMAR HAZARD: EN composes «Factors of » + number at runtime. Mongolian puts the number first and the suffix varies with it (12-ын, 15-ын, 20-ын). Needs a function, not a string — flagging so the wiring is built right." },
  { en: "Multiples of", mn: "-ын үржвэрүүд", src: "NEW", n: 3, note: "same hazard as above" },
];

export const ALL_CHROME = [
  ...STRUCTURE,
  ...NAV,
  ...CONTROLS,
  ...SECTIONS,
  ...FORMS,
  ...STATES,
  ...MEASURES,
];
