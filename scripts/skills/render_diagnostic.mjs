// Render the paper diagnostic to four print-ready PDFs.
//
// KaTeX renders the maths server-side into static HTML+CSS (no scripts, no
// fonts fetched at print time), then headless Chromium prints it. That keeps
// the output identical wherever it is produced, which matters for something
// a centre will photocopy 200 times.
//
// Option order is SHUFFLED here, deterministically per item id. The builder
// authors every correct answer as option A for readability; a paper where the
// answer is always A would be marked by pattern, not by mathematics. The
// answer key and the entry form are generated from the SAME shuffle, so they
// cannot disagree with the question sheet.
//
// Run: node scripts/skills/render_diagnostic.mjs

import fs from "node:fs";
import path from "node:path";
import katex from "katex";
import { chromium } from "playwright";

const ROOT = path.resolve(import.meta.dirname, "../..");
const D = JSON.parse(fs.readFileSync(path.join(ROOT, "data/skills/paper-diagnostic.json"), "utf8"));
const KATEX_CSS = fs.readFileSync(path.join(ROOT, "node_modules/katex/dist/katex.min.css"), "utf8");
const OUT = path.join(ROOT, "docs/diagnostic");
fs.mkdirSync(OUT, { recursive: true });

// FNV-1a, same shuffle key the placement bank uses, so "deterministic per id"
// means the same thing across the codebase.
// "A10" must not sort before "A8". Compare the numeric suffix, not the string.
const seq = (id) => parseInt(id.replace(/^[A-Z]+/, ""), 10);
const byTierThenSeq = (a, b) => a.tier - b.tier || seq(a.id) - seq(b.id);

function keyOf(id) {
  let h = 2166136261 >>> 0;
  for (const c of id) h = Math.imul(h ^ c.charCodeAt(0), 16777619) >>> 0;
  return h >>> 0;
}
function shuffled(item, salt) {
  const letters = ["A", "B", "C", "D"];
  const order = [...letters];
  let seed = keyOf(item.id + ":" + salt);
  for (let i = order.length - 1; i > 0; i--) {
    seed = (Math.imul(seed, 1103515245) + 12345) & 0x7fffffff;
    const j = seed % (i + 1);
    [order[i], order[j]] = [order[j], order[i]];
  }
  // order[k] is the ORIGINAL letter now shown in position k.
  const shown = order.map((orig, k) => ({
    letter: letters[k],
    text: item.options[orig],
    original: orig,
    isAnswer: orig === item.answer,
  }));
  return { shown, answerLetter: shown.find((o) => o.isAnswer).letter };
}

// $...$ inline / $$...$$ display, rendered to static markup.
function math(s) {
  return String(s)
    .replace(/\$\$([^$]+)\$\$/g, (_, t) =>
      katex.renderToString(t, { displayMode: true, throwOnError: false }))
    .replace(/\$([^$]+)\$/g, (_, t) =>
      katex.renderToString(t, { displayMode: false, throwOnError: false }));
}
const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

const CSS = `
${KATEX_CSS}
@page { size: A4; margin: 16mm 14mm; }
* { box-sizing: border-box; }
body { font-family: "Times New Roman", Times, serif; font-size: 11.5pt; line-height: 1.45;
       color: #000; background: #fff; margin: 0; }
h1 { font-size: 17pt; margin: 0 0 2mm; letter-spacing: -0.01em; }
h2 { font-size: 12.5pt; margin: 7mm 0 2.5mm; padding-bottom: 1mm;
     border-bottom: 1.2pt solid #000; text-transform: uppercase; letter-spacing: 0.06em; }
.sub { font-size: 9.5pt; color: #333; margin: 0 0 4mm; }
.rule { border: 1pt solid #000; padding: 3mm 4mm; margin: 0 0 5mm; font-size: 10pt; }
.rule b { text-transform: uppercase; letter-spacing: 0.05em; font-size: 9pt; }
.item { margin: 0 0 4.5mm; page-break-inside: avoid; }
.q { display: flex; gap: 3mm; }
.n { font-weight: bold; min-width: 9mm; }
.opts { display: grid; grid-template-columns: 1fr 1fr; gap: 0.8mm 5mm; margin: 1.5mm 0 0 12mm; }
.opt { font-size: 11pt; }
.opt b { font-weight: bold; margin-right: 1.5mm; }
table { width: 100%; border-collapse: collapse; font-size: 9.5pt; }
th, td { border: 0.6pt solid #000; padding: 1.4mm 2mm; text-align: left; vertical-align: top; }
th { background: #eee; font-weight: bold; font-size: 8.5pt; text-transform: uppercase;
     letter-spacing: 0.04em; }
td.c { text-align: center; font-weight: bold; }
td.box { text-align: center; height: 8mm; }
.mono { font-family: "Courier New", monospace; font-size: 8.5pt; }
.small { font-size: 9pt; color: #333; }
.warn { border: 1.5pt solid #000; padding: 3mm 4mm; margin: 0 0 5mm; font-size: 9.5pt;
        background: #f2f2f2; }
.ladder { margin: 0 0 4mm; page-break-inside: avoid; }
.ladder h3 { font-size: 11pt; margin: 0 0 1.5mm; }
.verdict { border: 1.2pt solid #000; padding: 2mm 3mm; margin-top: 2mm; font-size: 9.5pt; }
.foot { margin-top: 6mm; font-size: 8.5pt; color: #444; border-top: 0.6pt solid #999;
        padding-top: 2mm; }
.pagebreak { page-break-before: always; }
`;

const page = (title, body) =>
  `<meta charset="utf-8"><title>${esc(title)}</title><style>${CSS}</style>${body}`;

const byStrand = (s) => D.items.filter((i) => i.strand === s);
// A marker must not be able to guess the key, so the shuffle salt is CHOSEN:
// try a few and keep the one whose answer-letter histogram is flattest and
// whose longest same-letter run is shortest. Deterministic — the same salt
// comes out every run, so the key and the paper can never drift apart.
function score(salt) {
  const letters = D.items.map((i) => shuffled(i, salt).answerLetter);
  const h = { A: 0, B: 0, C: 0, D: 0 };
  for (const l of letters) h[l]++;
  const spread = Math.max(...Object.values(h)) - Math.min(...Object.values(h));
  let run = 1, worst = 1;
  for (let i = 1; i < letters.length; i++) {
    run = letters[i] === letters[i - 1] ? run + 1 : 1;
    worst = Math.max(worst, run);
  }
  return spread * 10 + worst;
}
let SALT = 0;
for (let s2 = 1; s2 < 400; s2++) if (score(s2) < score(SALT)) SALT = s2;
const SHUF = Object.fromEntries(D.items.map((i) => [i.id, shuffled(i, SALT)]));

// Item numbers run 1..30 in printed order, which is strand by strand, tier by
// tier. The entry form keys on the ITEM ID, not the number, so a re-ordering
// can never silently re-point a student's answer at another skill.
const PRINT_ORDER = D.strandOrder.flatMap((s) =>
  byStrand(s).sort(byTierThenSeq));
const NUM = Object.fromEntries(PRINT_ORDER.map((i, k) => [i.id, k + 1]));

// ---------------------------------------------------------------- 1. paper
function questionSheet() {
  let b = `<h1>${esc(D.title)}</h1>
<p class="sub">Diagnostic paper · 30 questions · no calculator · 60 minutes</p>
<div class="rule"><b>Instructions.</b><br>
Answer every question. Choose ONE option and write its letter in the box on
your answer sheet. There is no penalty for a wrong answer, so do not leave a
question blank — but if you are guessing, say so on the answer sheet, because
this paper is here to find out what to teach you, not to rank you.</div>`;
  for (const s of D.strandOrder) {
    b += `<h2>${esc(D.strandTitles[s])}</h2>`;
    for (const it of byStrand(s).sort(byTierThenSeq)) {
      const { shown } = SHUF[it.id];
      b += `<div class="item"><div class="q"><span class="n">${NUM[it.id]}.</span>
<span>${math(it.body)}</span></div><div class="opts">` +
        shown.map((o) => `<div class="opt"><b>${o.letter}.</b> ${math(o.text)}</div>`).join("") +
        `</div></div>`;
    }
  }
  b += `<div class="foot">Mongol Potential · ЭШ diagnostic · item text pending Mongolian
authoring (Phase 3)</div>`;
  return page("ЭШ Diagnostic — Question Sheet", b);
}

// ------------------------------------------------------------- 2. answer key
function answerKey() {
  let b = `<h1>Answer Key</h1>
<p class="sub">${esc(D.title)} · 30 items · every answer computed and machine-verified</p>
<div class="warn"><b>Not for students.</b> Option order on the question sheet is
shuffled per item; the letters below are the letters as printed. If the
question sheet is ever regenerated, regenerate this key with it.</div>`;
  for (const s of D.strandOrder) {
    b += `<h2>${esc(D.strandTitles[s])}</h2><table>
<tr><th style="width:8%">No.</th><th style="width:8%">Ans</th><th style="width:6%">Tier</th>
<th style="width:26%">Skill</th><th>Working</th></tr>`;
    for (const it of byStrand(s).sort(byTierThenSeq)) {
      b += `<tr><td class="c">${NUM[it.id]}</td><td class="c">${SHUF[it.id].answerLetter}</td>
<td class="c">${it.tier}</td><td class="mono">${esc(it.skill_id)}</td>
<td>${math(it.solution)}</td></tr>`;
    }
    b += `</table>`;
  }
  b += `<div class="pagebreak"></div><h1>What each wrong answer means</h1>
<p class="sub">Every distractor was built from one specific mistake. A class that
picks the same wrong option is a class with one teachable gap, not a class that
guessed — so this table is worth reading before you re-teach anything.</p>`;
  for (const s of D.strandOrder) {
    b += `<h2>${esc(D.strandTitles[s])}</h2><table>
<tr><th style="width:8%">No.</th><th style="width:8%">Option</th><th>The mistake it comes from</th></tr>`;
    for (const it of byStrand(s).sort(byTierThenSeq)) {
      for (const o of SHUF[it.id].shown.filter((o2) => !o2.isAnswer)) {
        b += `<tr><td class="c">${NUM[it.id]}</td><td class="c">${o.letter}</td>
<td>${math(it.errors[o.original])}</td></tr>`;
      }
    }
    b += `</table>`;
  }
  return page("ЭШ Diagnostic — Answer Key", b);
}

// ----------------------------------------------------------- 3. marking sheet
function markingSheet() {
  let b = `<h1>Marking Sheet</h1>
<p class="sub">One sheet per student · ${esc(D.title)}</p>
<div class="rule"><b>How to mark.</b><br>
The paper cannot adapt, so you do. Work through each strand from the bottom
tier up.<br><br>
<b style="letter-spacing:0.05em">A student clears a tier by getting MORE THAN HALF of its
items right.</b><br><br>
Stop climbing at the first tier they do not clear. The strand result is the
highest tier they cleared — <b>0</b> means they did not clear tier 1, and that
is a real result, not a failure to record.<br><br>
A tier only counts if the tier below it was cleared. A student who misses tier 1
but happens to get a tier-3 item right has guessed; do not promote them on it.</div>
<table><tr><th style="width:34%">Student name</th><td></td>
<th style="width:16%">Date</th><td></td></tr></table><br>`;

  for (const s of D.strandOrder) {
    const tiers = D.ladders[s];
    b += `<div class="ladder"><h3>${esc(D.strandTitles[s])}</h3><table>
<tr><th style="width:12%">Tier</th><th>Question numbers — tick each one correct</th>
<th style="width:14%">Correct</th><th style="width:16%">Clears at</th>
<th style="width:12%">Cleared?</th></tr>`;
    for (const t of Object.keys(tiers).sort()) {
      const info = tiers[t];
      const nums = info.items.map((id) => NUM[id]).sort((p, q) => p - q);
      b += `<tr><td class="c">${t}</td>
<td>${nums.map((n) => `${n} <span style="letter-spacing:0.3em">☐</span>`).join("&nbsp;&nbsp;&nbsp;")}</td>
<td class="box"></td><td class="c">${info.clear_at} of ${info.items.length}</td>
<td class="box"></td></tr>`;
    }
    b += `</table><div class="verdict"><b>${esc(D.strandTitles[s])} result:</b>
highest tier cleared = <span style="letter-spacing:0.5em">&nbsp;0&nbsp;&nbsp;1&nbsp;&nbsp;2&nbsp;&nbsp;3&nbsp;</span>
(circle one)</div></div>`;
  }

  b += `<div class="pagebreak"></div><h1>Reading the result</h1>
<table><tr><th style="width:14%">Tier</th><th>What it means and where the student starts</th></tr>
<tr><td class="c">0</td><td>The foundations of this strand are not in place. Start at the
beginning of the strand — not at revision, at teaching.</td></tr>
<tr><td class="c">1</td><td>Routine one-step work is secure. Start where two ideas have to be
chained together.</td></tr>
<tr><td class="c">2</td><td>Standard exam work is secure. Start on the harder material —
the multi-step and unfamiliar-setup questions.</td></tr>
<tr><td class="c">3</td><td>Secure across the strand at diagnostic level. Move to past-paper
practice and use class time on the other strands.</td></tr></table>
<p class="small" style="margin-top:4mm">The five strand results are independent
and usually differ. A student at tier 3 in algebra and tier 0 in geometry is
common and is exactly the situation this paper exists to find; teach to the
lower number, not to an average of the five.</p>
<div class="warn"><b>Thin tiers are fragile — treat them as provisional.</b>
Items are allocated by how much of the exam each strand is worth, so Analysis,
Probability &amp; Statistics and Combinatorics have tiers of only one or two
items. On a two-item tier "more than half" means both, so a single careless slip
costs a whole tier. Where a strand result rests on one or two items and it
disagrees with what you see from the student in class, trust the class. Algebra
and Geometry &amp; Trigonometry carry three or four items a tier and are the two
results to lean on.</div>
<div class="warn"><b>What this paper does not tell you.</b> Thirty items place a
student per STRAND. They do not give a per-skill profile — for that a student
needs the adaptive test, which asks a different next question depending on what
they just did. Do not read a single item as evidence about a single skill.</div>`;
  return page("ЭШ Diagnostic — Marking Sheet", b);
}

// -------------------------------------------------------------- 4. entry form
function entryForm() {
  let b = `<h1>Data Entry Form</h1>
<p class="sub">One row per item · type this into the system in Phase 1</p>
<div class="warn"><b>This form is the reason September's data survives.</b> Every
item is bound to one skill id below. Enter the option the student actually
chose, not just whether it was right — the wrong option identifies the specific
mistake, and that is the difference between "weak at algebra" and "multiplies
before resolving the bracket".</div>
<table><tr><th style="width:30%">Student name</th><td></td>
<th style="width:14%">Date</th><td></td></tr></table><br>
<table>
<tr><th style="width:7%">No.</th><th style="width:9%">Item</th><th style="width:34%">skill_id</th>
<th style="width:12%">Tier</th><th style="width:14%">Chose</th><th style="width:12%">Correct?</th></tr>`;
  for (const it of PRINT_ORDER) {
    b += `<tr><td class="c">${NUM[it.id]}</td><td class="mono">${esc(it.id)}</td>
<td class="mono">${esc(it.skill_id)}</td><td class="c">${it.tier}</td>
<td class="box"></td><td class="box"></td></tr>`;
  }
  b += `</table>
<p class="small" style="margin-top:4mm">Strand results from the marking sheet:
&nbsp; Algebra ☐ &nbsp; Geometry &amp; Trig ☐ &nbsp; Analysis ☐ &nbsp;
Prob &amp; Stats ☐ &nbsp; Combinatorics ☐</p>
<div class="foot">Item ids are stable. If the question sheet is regenerated the
numbers may move but the ids will not, so enter by ID where the two disagree.</div>`;
  return page("ЭШ Diagnostic — Entry Form", b);
}

const DOCS = [
  ["01-question-sheet", questionSheet()],
  ["02-answer-key", answerKey()],
  ["03-marking-sheet", markingSheet()],
  ["04-entry-form", entryForm()],
];

const browser = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium" });
const pg = await browser.newPage();
for (const [name, html] of DOCS) {
  const htmlPath = path.join(OUT, `${name}.html`);
  fs.writeFileSync(htmlPath, html);
  await pg.goto("file://" + htmlPath, { waitUntil: "load" });
  await pg.pdf({
    path: path.join(OUT, `${name}.pdf`),
    format: "A4",
    printBackground: true,
    margin: { top: "16mm", bottom: "16mm", left: "14mm", right: "14mm" },
  });
  const kb = (fs.statSync(path.join(OUT, `${name}.pdf`)).size / 1024).toFixed(0);
  console.log(`  ${name}.pdf  ${kb} KB`);
}
await browser.close();

// The answer letters must not be lopsided — a marker should not be able to
// guess the key. Report the histogram so a bad shuffle is visible, not hidden.
const hist = {};
for (const it of D.items) {
  const l = SHUF[it.id].answerLetter;
  hist[l] = (hist[l] || 0) + 1;
}
console.log(`  salt ${SALT} chosen from 400 candidates`);
console.log("  answer histogram:", JSON.stringify(hist));
let run = 1, worst = 1;
for (let i = 1; i < PRINT_ORDER.length; i++) {
  run = SHUF[PRINT_ORDER[i].id].answerLetter === SHUF[PRINT_ORDER[i - 1].id].answerLetter
    ? run + 1 : 1;
  worst = Math.max(worst, run);
}
console.log(`  longest run of the same letter: ${worst}`);
