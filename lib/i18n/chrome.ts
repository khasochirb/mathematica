// Chrome vocabulary — Mongolian for the navigation, buttons, labels, headers,
// units, and empty/error states that are currently hardcoded English.
//
// ═══ STATUS: WIRED ON THE BRANCH. NOT DEPLOYED. ═══
//
// Khas confirmed the two glossary terms the chrome depends on (`focus`,
// `test`) and wrote the voice strings, so group 1 wiring has started. The
// pages read from `chrome()` below.
//
// NOTHING HERE HAS SHIPPED. docs/MONGOLIAN.md: "Never deploy unreviewed
// Mongolian." Wiring on the branch is how the wording becomes reviewable at
// all — it renders on the preview URL where Khas can read it in place, which
// a table of 91 strings cannot show. Production still serves English on these
// pages until a deploy is explicitly asked for.
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

  // Site nav — the footer's link columns. The HEADER already carried Mongolian
  // for four of these inline (components/layout/Header.tsx, the `nav` object);
  // those are copied VERBATIM rather than re-worded, because two Mongolian
  // labels for one destination is precisely how a product starts feeling
  // machine-made. The footer had no `lang` at all before this.
  { en: "1-on-1 Tutoring", mn: "Ганцаарчилсан хичээл", src: "SITE", n: 2, note: "verbatim from Header.tsx nav.tutoring" },
  { en: "About Us", mn: "Бидний тухай", src: "SITE", n: 2, note: "verbatim from Header.tsx nav.about; app/about uses the same" },
  { en: "Contact Us", mn: "Холбоо барих", src: "SITE", n: 2, note: 'same wording as the existing "Contact" entry — one destination, one label' },
  { en: "Careers", mn: "Ажлын байр", src: "SITE", n: 1, note: 'verbatim from app/about ("02 · Ажлын байр")' },
  { en: "Blog", mn: "Блог", src: "NEW", n: 2 },
  { en: "Privacy Policy", mn: "Нууцлалын бодлого", src: "NEW", n: 2 },
  { en: "Terms of Service", mn: "Үйлчилгээний нөхцөл", src: "NEW", n: 2 },
  { en: "Practice by Topic", mn: "Сэдвээр дасгал хийх", src: "DERIV", n: 1, note: 'built from "Topic"→«Сэдэв» + "Practice"→«Дасгал»; the instrumental -ээр is mine' },
  { en: "Previous Year Tests", mn: "Өмнөх жилүүдийн шалгалт", src: "NEW", n: 1, note: "the real ЭШ past papers, NOT «жишиг тест» (mock) — Khas used «жишиг тест» for the mock-test voice string, so the two must stay distinguishable" },
  { en: "ЭШ Hub", mn: "ЭШ хэсэг", src: "DERIV", n: 1, note: 'matches the existing "Back to the SAT hub"→«SAT хэсэг рүү буцах»' },
  { en: "ЭШ Study by Topic", mn: "ЭШ сэдэв тус бүрээр", src: "NEW", n: 1 },

  // Footer column headings.

  // SAT and IB hub chrome. NOTE THE RULE THIS OBEYS: content language is a
  // property of the hub (memory/expansion-vision.md §4.7, locked) — the SAT and
  // IB hubs serve their content in English on purpose, because realism is the
  // point, and "navigation chrome is what the EN/MN toggle controls, never
  // content". So the LABELS below translate and the official course names do
  // NOT: "Analysis & Approaches SL", "Applications & Interpretation SL",
  // "Digital SAT · Math" are IB's and College Board's own names for the things
  // and are deliberately absent from this dictionary.
  { en: "Practice by topic", mn: "Сэдвээр дасгал хийх", src: "DERIV", n: 2, note: "lowercase-t twin of \"Practice by Topic\" — the footer uses one casing and the hubs the other; chrome() is case-sensitive, so both keys must exist" },
  { en: "Practice tests", mn: "Жишиг тестүүд", src: "DERIV", n: 2, note: "Khas's mock-test voice string uses «жишиг тест»" },
  { en: "Foundations", mn: "Суурь мэдлэг", src: "NEW", n: 2 },
  { en: "Progress", mn: "Ахиц", src: "NEW", n: 3 },
  { en: "See the full report", mn: "Бүрэн тайланг үзэх", src: "NEW", n: 2 },
  { en: "SAT Math Hub", mn: "SAT Math хэсэг", src: "DERIV", n: 1, note: "SAT/IB course names stay Latin; only «хэсэг» is translated" },
  { en: "IB Math Hub", mn: "IB Math хэсэг", src: "DERIV", n: 1 },
  { en: "SAT Math course", mn: "SAT Math курс", src: "DERIV", n: 1 },
  { en: "IB Math courses", mn: "IB Math курсууд", src: "DERIV", n: 1 },
  { en: "IB Math — Courses", mn: "IB Math — Курсууд", src: "DERIV", n: 1 },
  { en: "SAT Math practice", mn: "SAT Math дасгал", src: "DERIV", n: 1 },
  { en: "IB Math practice", mn: "IB Math дасгал", src: "DERIV", n: 1 },
  { en: "Your SAT performance", mn: "Таны SAT-ийн гүйцэтгэл", src: "NEW", n: 1 },
  { en: "Your IB performance", mn: "Таны IB-ийн гүйцэтгэл", src: "NEW", n: 1 },
  { en: "Live", mn: "Нээлттэй", src: "NEW", n: 4, note: "status badge, the counterpart of «Удахгүй» (Soon) which Khas wrote — he may want to write this one too" },
  { en: "New", mn: "Шинэ", src: "NEW", n: 2 },
  { en: "Free", mn: "Үнэгүй", src: "DERIV", n: 1, note: "from Khas's «Үнэгүй нэгд» (Free to join)" },

  // Footer column headings.
  { en: "Programs", mn: "Хөтөлбөр", src: "NEW", n: 1 },
  { en: "Company", mn: "Компани", src: "NEW", n: 1 },
  { en: "Support", mn: "Тусламж", src: "NEW", n: 1 },
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

  // Header controls. These are aria-labels — never rendered as visible text,
  // but read aloud by a screen reader, so a Mongolian student using one
  // currently hears the whole site chrome in English. No precedent existed for
  // any of them; all four are mine.
  { en: "Toggle language", mn: "Хэл солих", src: "NEW", n: 1 },
  { en: "Toggle menu", mn: "Цэс нээх, хаах", src: "NEW", n: 1 },
  { en: "Toggle theme", mn: "Дэлгэцийн горим солих", src: "NEW", n: 1, note: "light/dark, not a visual «загвар» — confirm the wording" },
  { en: "User menu", mn: "Хэрэглэгчийн цэс", src: "NEW", n: 1 },
  { en: "Switch to light mode", mn: "Цайвар горимд шилжих", src: "NEW", n: 1 },
  { en: "Switch to dark mode", mn: "Бараан горимд шилжих", src: "NEW", n: 1 },
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

  // SAT / IB hub descriptions. Sentences that describe and sell a course —
  // VOICE by docs/MONGOLIAN.md, so `mn` stays empty and chrome() renders the
  // English until Khas writes them. Listed here rather than left loose in the
  // pages so the outstanding voice work is one reviewable queue.
  { en: "The complete AA SL syllabus · 5 topics · one lesson per subtopic code", mn: "", src: "VOICE", n: 2 },
  { en: "The AHL extension on top of AA SL · proof, complex numbers, 3D vectors, deeper calculus", mn: "", src: "VOICE", n: 2 },
  { en: "The complete AI SL syllabus · calculator-always, modelling-first · 5 topics", mn: "", src: "VOICE", n: 2 },
  { en: "4 College Board domains · 27 units · lessons, practice, unit tests", mn: "", src: "VOICE", n: 1 },
  { en: "Drill the 4 domains · a similar problem after every miss", mn: "", src: "VOICE", n: 1 },
  { en: "Drill the 5 syllabus topics · a similar problem after every miss", mn: "", src: "VOICE", n: 1 },
  { en: "General Math courses — every topic from zero", mn: "", src: "VOICE", n: 2 },
  { en: "Per-domain accuracy and your weakest areas, once you've taken a test", mn: "", src: "VOICE", n: 1 },
  { en: "Per-component accuracy and weakest areas, once you start practicing", mn: "", src: "VOICE", n: 1 },
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


// ---------------------------------------------------------------------------
// 8. Interactive-widget accessibility text — aria-labels on the controls and
//    alt text on the figures. NEVER VISIBLE, and therefore invisible to any
//    audit of on-screen strings: a Mongolian student using a screen reader
//    hears every one of these in English while the page around them is
//    Mongolian. The widgets are the part of a lesson a student actually
//    touches, so this is the accessibility half of the same work.
//
//    THE CASE ENDINGS ARE THE RISK HERE. Mongolian accusative (-ийг/-ыг/-г)
//    agrees with the vowel of the noun it attaches to, and there are ~60 of
//    them below. Assume some are wrong.
// ---------------------------------------------------------------------------
export const WIDGETS: ChromeEntry[] = [
  { en: "Increase angle", mn: "Өнцгийг ихэсгэх", src: "NEW" },
  { en: "Decrease angle", mn: "Өнцгийг багасгах", src: "NEW" },
  { en: "Larger angle", mn: "Илүү том өнцөг", src: "NEW" },
  { en: "Smaller angle", mn: "Илүү жижиг өнцөг", src: "NEW" },
  { en: "Open the angle", mn: "Өнцгийг нээх", src: "NEW" },
  { en: "Close the angle", mn: "Өнцгийг хаах", src: "NEW" },
  { en: "Increase scale", mn: "Масштабыг ихэсгэх", src: "GLOSS", note: "«масштаб» is glossary-locked" },
  { en: "Decrease scale", mn: "Масштабыг багасгах", src: "GLOSS" },
  { en: "Increase base b", mn: "b суурийг ихэсгэх", src: "DERIV", note: "«суурь» = base; the letter stays Latin (glossary rule 2)" },
  { en: "Decrease base b", mn: "b суурийг багасгах", src: "DERIV" },
  { en: "Increase start a", mn: "a эхний утгыг ихэсгэх", src: "DERIV" },
  { en: "Decrease start a", mn: "a эхний утгыг багасгах", src: "DERIV" },
  { en: "Bigger number", mn: "Том тоо", src: "NEW" },
  { en: "Smaller number", mn: "Жижиг тоо", src: "NEW" },
  { en: "More", mn: "Илүү олон", src: "NEW" },
  { en: "Fewer", mn: "Цөөн", src: "NEW" },
  { en: "More columns", mn: "Багана нэмэх", src: "DERIV", note: "same Mongolian as \"Add column\" — both buttons do the same thing in different widgets" },
  { en: "Fewer columns", mn: "Багана хасах", src: "DERIV" },
  { en: "Remove column", mn: "Багана устгах", src: "NEW" },
  { en: "More pieces", mn: "Хэсгийг нэмэх", src: "NEW" },
  { en: "Fewer pieces", mn: "Хэсгийг хасах", src: "NEW" },
  { en: "More sides", mn: "Талыг нэмэх", src: "NEW" },
  { en: "Fewer sides", mn: "Талыг хасах", src: "NEW" },
  { en: "More units", mn: "Нэгжийг нэмэх", src: "DERIV", note: "«нэгж» from the Unit entry" },
  { en: "Fewer units", mn: "Нэгжийг хасах", src: "DERIV" },
  { en: "More batches", mn: "Багцыг нэмэх", src: "NEW" },
  { en: "Fewer batches", mn: "Багцыг хасах", src: "NEW" },
  { en: "More x", mn: "x-ийг нэмэх", src: "NEW" },
  { en: "Fewer x", mn: "x-ийг хасах", src: "NEW" },
  { en: "Up", mn: "Дээш", src: "NEW" },
  { en: "Down", mn: "Доош", src: "NEW" },
  { en: "Move x left", mn: "x-ийг зүүн тийш зөөх", src: "NEW" },
  { en: "Move x right", mn: "x-ийг баруун тийш зөөх", src: "NEW" },
  { en: "Move B left", mn: "B-г зүүн тийш зөөх", src: "NEW" },
  { en: "Move B right", mn: "B-г баруун тийш зөөх", src: "NEW" },
  { en: "Slide ruler left", mn: "Шугамыг зүүн тийш гулсуулах", src: "NEW" },
  { en: "Slide ruler right", mn: "Шугамыг баруун тийш гулсуулах", src: "NEW" },
  { en: "Pull the dot back", mn: "Цэгийг буцааж татах", src: "NEW" },
  { en: "Pull the dot right", mn: "Цэгийг баруун тийш татах", src: "NEW" },
  { en: "Raise the ray", mn: "Цацрагийг дээш өргөх", src: "NEW", note: "«цацраг» = ray; 0 hits in the ЭШ bank, standard geometry term" },
  { en: "Lower the ray", mn: "Цацрагийг доош буулгах", src: "NEW" },
  { en: "Raise the percent", mn: "Хувийг нэмэгдүүлэх", src: "GLOSS", note: "«хувь» is glossary-locked" },
  { en: "Lower the percent", mn: "Хувийг бууруулах", src: "GLOSS" },
  { en: "Flip sign", mn: "Тэмдгийг солих", src: "GLOSS", note: "«тэмдэг» = sign, ministry" },
  { en: "Flip leading sign", mn: "Тэргүүлэх тэмдгийг солих", src: "DERIV" },
  { en: "Hide a diagonal", mn: "Диагоналыг нуух", src: "NEW" },
  { en: "Reveal the next diagonal", mn: "Дараагийн диагоналыг харуулах", src: "NEW" },
  { en: "Reset pattern", mn: "Хэв маягийг дахин эхлүүлэх", src: "DERIV", note: "«дахин эхлэх» from the Reset entry" },
  { en: "Reset tree", mn: "Модыг дахин эхлүүлэх", src: "DERIV" },
  { en: "Reset proof", mn: "Баталгааг дахин эхлүүлэх", src: "DERIV" },
  { en: "Reset tests", mn: "Шалгалтыг дахин эхлүүлэх", src: "DERIV" },
  { en: "Replay the approach", mn: "Ойртолтыг дахин тоглуулах", src: "NEW" },
  { en: "Replay the sweep", mn: "Эргэлтийг дахин тоглуулах", src: "NEW", note: "the widget sweeps an angle round; «эргэлт» describes what is replayed" },
  { en: "Replay the tear", mn: "Тасдалтыг дахин тоглуулах", src: "NEW", note: "the triangle's corners tear off and tile a straight line" },
  { en: "Roll again", mn: "Дахин шидэх", src: "NEW" },
  { en: "Throw again", mn: "Дахин шидэх", src: "NEW", note: "same action as Roll again, same Mongolian" },
  { en: "Wrap one radian", mn: "Нэг радиан ороох", src: "GLOSS", note: "«радиан» ministry" },
  { en: "Unwrap one radian", mn: "Нэг радиан тайлах", src: "GLOSS" },
  { en: "Exit lesson", mn: "Хичээлээс гарах", src: "DERIV" },
  { en: "Tree diagram", mn: "Модны схем", src: "GLOSS", note: "Khas confirmed «модны схем», correcting the skill glossary's «мод диаграм»" },
  { en: "Dot plot", mn: "Цэгэн график", src: "SITE", note: "shipped mirrors use this. А/492 has «цэгэн диаграм» for dot plot and «цэгэн диаграмм» for scatter plot — one doubled м apart, which would ship two charts under near-identical names. Following the site; flagged for Khas." },
  { en: "Scatter plot", mn: "Хамаарлын график", src: "SITE", note: "shipped grade-8 mirror; keeps it distinct from the dot plot" },
  { en: "Histogram", mn: "Гистограмм", src: "GLOSS", note: "ministry А/492" },
  { en: "Boxplot", mn: "Хайрцган диаграмм", src: "GLOSS", note: "ministry «box plot»" },
  { en: "Normal curve", mn: "Хэвийн тархалтын муруй", src: "DERIV", note: "from the ministry's «хэвийн тархалт»" },
  { en: "Venn diagram with counts", mn: "Тоотой Венн диаграмм", src: "DERIV", note: "«Венн диаграмм» is the ЭШ bank's spelling" },
  { en: "Pascal's triangle", mn: "Паскалийн гурвалжин", src: "GLOSS", note: "proper names take standard Mongolian Cyrillic (Паскаль)" },
  { en: "Factor tree", mn: "Үржигдэхүүнд задлах мод", src: "NEW", note: "FACTOR IS POLYSEMOUS (R9): a factor TREE decomposes into prime factors → «үржигдэхүүн», while a factor RAINBOW pairs divisors → «хуваагч». The two widgets need the two different words." },
  { en: "Factor rainbow", mn: "Хуваагчийн солонго", src: "NEW", note: "see Factor tree — this one pairs divisors, so «хуваагч»" },
  { en: "Area under a curve", mn: "Муруйн доорх талбай", src: "NEW" },
  { en: "Coordinate grid", mn: "Координатын тор", src: "NEW" },
  { en: "Coordinate geometry figure", mn: "Координатын геометрийн зураг", src: "NEW" },
  { en: "Geometry diagram", mn: "Геометрийн зураг", src: "NEW" },
  { en: "Path-counting grid", mn: "Зам тоолох тор", src: "NEW" },
  { en: "Probability distribution bars", mn: "Магадлалын тархалтын багана", src: "GLOSS", note: "«магадлал» glossary" },
  { en: "Binomial distribution bars", mn: "Бином тархалтын багана", src: "DERIV" },
  { en: "Sampling distribution dots", mn: "Түүврийн тархалтын цэгүүд", src: "GLOSS", note: "«түүвэр» glossary" },
  { en: "Running relative frequency chart", mn: "Харьцангуй давтамжийн явцын график", src: "NEW" },
  { en: "A parabola on a coordinate grid", mn: "Координатын тор дээрх парабол", src: "DERIV" },
  { en: "A ball flying along a parabolic arc", mn: "Параболын нумаар нисэж буй бөмбөг", src: "NEW" },
  { en: "A bank balance compounding year by year", mn: "Жил бүр нийлмэлжиж буй банкны үлдэгдэл", src: "NEW" },
  { en: "A complex number plotted on the Argand diagram", mn: "Арганы диаграмм дээр байрлуулсан комплекс тоо", src: "NEW", note: "Argand → Арган" },
  { en: "A conic section on a grid", mn: "Тор дээрх конус огтлол", src: "NEW" },
  { en: "A curve with a tangent or secant line", mn: "Шүргэгч эсвэл огтлогч шулуунтай муруй", src: "NEW" },
  { en: "A function graph with points approaching a target x-value", mn: "Зорилтот x утга руу ойртож буй цэгүүдтэй функцийн график", src: "NEW" },
  { en: "A point on the unit circle with its coordinates", mn: "Нэгж радиустай тойрог дээрх цэг ба түүний координат", src: "GLOSS", note: "ministry «нэгж радиустай тойрог»" },
  { en: "A point orbiting a circle traces a sine wave", mn: "Тойргийг тойрон эргэх цэг синус долгион зурна", src: "NEW" },
  { en: "A polynomial curve on a grid", mn: "Тор дээрх олон гишүүнтийн муруй", src: "GLOSS", note: "«олон гишүүнт» ministry" },
  { en: "An exponential curve on a grid", mn: "Тор дээрх илтгэгч муруй", src: "GLOSS", note: "«илтгэгч» per the exponential-functions draft" },
  { en: "An exponential racing a straight line", mn: "Шулуунтай уралдаж буй илтгэгч функц", src: "DERIV" },
  { en: "Powers of a complex number spiralling on the Argand diagram", mn: "Арганы диаграмм дээр мушгирч буй комплекс тооны зэргүүд", src: "NEW" },
  { en: "Radius lengths wrapping around a circle", mn: "Тойргийг тойрон ороож буй радиусын урт", src: "NEW" },
  { en: "The nth roots of a complex number forming a regular polygon on a circle", mn: "Тойрог дээр зөв олон өнцөгт үүсгэж буй комплекс тооны n-р язгуурууд", src: "NEW" },
  { en: "Transformation on the coordinate plane", mn: "Координатын хавтгай дээрх хувиргалт", src: "NEW" },
  { en: "Two lines on a coordinate grid", mn: "Координатын тор дээрх хоёр шулуун", src: "DERIV" },
  { en: "Vectors as arrows on a grid", mn: "Тор дээрх сум хэлбэрийн векторууд", src: "GLOSS", note: "«вектор» ministry" },
];

export const ALL_CHROME: ChromeEntry[] = [
  ...STRUCTURE,
  ...NAV,
  ...CONTROLS,
  ...SECTIONS,
  ...FORMS,
  ...STATES,
  ...MEASURES,
  ...WIDGETS,
];

// ---------------------------------------------------------------------------
// Lookup
// ---------------------------------------------------------------------------

const MN_BY_EN: Record<string, string> = {};
for (const e of ALL_CHROME) {
  // An entry with no Mongolian is not a gap to paper over — VOICE entries are
  // deliberately empty until Khas writes them. Leaving them out of the map
  // makes chrome() fall through to English, which is the honest rendering.
  if (e.mn) MN_BY_EN[e.en] = e.mn;
}

// Case-insensitive index, consulted only when the exact key misses.
//
// The same label is written with different capitalisation in different places
// — the footer has "Practice by Topic", the SAT and IB hubs have "Practice by
// topic", the SAT learn page has "SAT Math Course" against the hub's "SAT Math
// course". Each mismatch renders English and looks exactly like a page nobody
// has wired yet, which is the one failure mode this dictionary exists to
// remove. Requiring an entry per casing would mean the same Mongolian written
// two or three times, free to drift apart.
//
// This is safe because the chrome test asserts that keys differing only by
// case never carry different Mongolian.
const MN_BY_EN_LOWER: Record<string, string> = {};
for (const e of ALL_CHROME) {
  if (e.mn) MN_BY_EN_LOWER[e.en.toLowerCase()] = e.mn;
}

/**
 * The English string in the reader's language.
 *
 * FALLS BACK TO ENGLISH, ALWAYS. A missing entry renders the English rather
 * than a blank or a key, because a page that silently loses its labels is
 * harder to notice than one that is half-translated — and this dictionary is
 * deliberately incomplete while the voice strings are outstanding.
 *
 * Never call this with an interpolated string. Mongolian suffixes agree with
 * what they attach to, so a composed string cannot be looked up; see
 * `memory/mn-group1-audits.md` §2 for the two sites that need a function
 * instead.
 */
export function chrome(en: string, lang: string): string {
  if (lang !== "mn") return en;
  return MN_BY_EN[en] ?? MN_BY_EN_LOWER[en.toLowerCase()] ?? en;
}

/** Entries still waiting on Khas — used by the coverage test, not by pages. */
export function untranslated(): ChromeEntry[] {
  return ALL_CHROME.filter((e) => !e.mn);
}
