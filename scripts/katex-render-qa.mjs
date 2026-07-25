// KaTeX render QA for content JSON, mirroring components/esh/MathText.tsx exactly.
// Walks every renderable string in the given topic files, splits it with the
// SAME regex the component uses, renders each math segment through KaTeX with
// throwOnError:false, and fails on any katex-error span (the red text that
// would appear in production) or unbalanced delimiter.
import katex from "katex";
import fs from "node:fs";

const DOLLAR_SENTINEL = "";
const files = process.argv.slice(2);
if (!files.length) {
  console.error("usage: node katex-qa.mjs <topic.json> ...");
  process.exit(1);
}

const failures = [];
let strings = 0;
let mathSegments = 0;

function renderCheck(where, text) {
  if (typeof text !== "string" || !text.includes("$")) return;
  strings++;
  const escaped = text.replace(/\\\$/g, DOLLAR_SENTINEL);

  // Delimiter parity: after removing the escaped-dollar sentinel, every
  // remaining $ must pair up. An odd count means a missing delimiter.
  const dollars = (escaped.match(/\$/g) || []).length;
  if (dollars % 2 !== 0) {
    failures.push(`${where}: odd number of $ delimiters (${dollars})`);
    return;
  }

  const parts = escaped.split(/(\$\$[^$]+\$\$|\$[^$]+\$|\*\*[^*]+\*\*)/g);
  for (const part of parts) {
    const isDisplay = part.startsWith("$$") && part.endsWith("$$");
    const isInline = !isDisplay && part.startsWith("$") && part.endsWith("$");
    if (!isDisplay && !isInline) {
      if (part.startsWith("**") && part.endsWith("**")) {
        // Bold content renders as plain text, so a lone currency $ inside it
        // is fine — but a complete $...$ pair means math was swallowed by the
        // bold token and will show up as literal dollar signs.
        if (/\$\$[^$]+\$\$|\$[^$]+\$/.test(part.slice(2, -2))) {
          failures.push(`${where}: bold swallows inline math: ${part.slice(0, 70)}`);
        }
        continue;
      }
      // A stray $ surviving in a text segment means the splitter did not treat
      // it as math — exactly what renders as a literal dollar in production.
      if (part.includes("$")) failures.push(`${where}: stray $ in text segment: ${part.slice(0, 70)}`);
      continue;
    }
    const latex = (isDisplay ? part.slice(2, -2) : part.slice(1, -1))
      .split(DOLLAR_SENTINEL)
      .join("\\$");
    mathSegments++;
    let html;
    try {
      html = katex.renderToString(latex, { throwOnError: false, displayMode: isDisplay });
    } catch (e) {
      failures.push(`${where}: KaTeX threw on ${latex.slice(0, 70)} (${e.message.slice(0, 80)})`);
      continue;
    }
    if (html.includes("katex-error")) {
      failures.push(`${where}: renders as katex-error: ${latex.slice(0, 90)}`);
    }
    // Characters KaTeX has no glyph for draw a blank box with only a console
    // warning — no error node — so the check above cannot see them. The check
    // mark ✓ has metrics and Cyrillic in \text{} falls back to a browser
    // font; these two genuinely vanish:
    for (const ch of "₮✗") {
      if (latex.includes(ch)) failures.push(`${where}: KaTeX cannot draw '${ch}' in math: ${latex.slice(0, 70)}`);
    }
  }
}

// Every field the lesson UI passes through MathText.
function walkProblem(where, p) {
  renderCheck(`${where}/${p.id}:statement`, p.statement);
  renderCheck(`${where}/${p.id}:solution`, p.solution);
}

for (const file of files) {
  const topic = JSON.parse(fs.readFileSync(file, "utf8"));
  const slug = topic.slug;
  renderCheck(`${slug}:blurb`, topic.blurb);
  renderCheck(`${slug}:buildsOn`, topic.buildsOn);

  for (const l of topic.lessons || []) {
    const w = `${slug}/${l.slug}`;
    for (const f of ["concreteComparison", "objective", "keyIdea"]) renderCheck(`${w}:${f}`, l[f]);
    for (const [i, c] of (l.concept || []).entries()) renderCheck(`${w}:concept[${i}]`, c);
    for (const [i, f] of (l.facts || []).entries()) {
      renderCheck(`${w}:facts[${i}].title`, f.title);
      // facts[].latex carries two conventions. Grade files store a MathText
      // string ($-delimited, possibly mixed with prose) which FactCard passes
      // to MathText RAW — so it must be checked raw, not $$-wrapped. Course
      // files store bare LaTeX with no $ at all; those are validated wrapped,
      // which is how any future renderer would display them.
      if (typeof f.latex === "string" && f.latex.replace(/\\\$/g, "").includes("$")) {
        renderCheck(`${w}:facts[${i}].latex`, f.latex);
      } else {
        renderCheck(`${w}:facts[${i}].latex`, f.latex ? `$$${f.latex}$$` : undefined);
      }
      renderCheck(`${w}:facts[${i}].explanation`, f.explanation);
    }
    for (const [i, m] of (l.commonMistakes || []).entries()) {
      renderCheck(`${w}:mistakes[${i}].text`, m.text);
      renderCheck(`${w}:mistakes[${i}].correction`, m.correction);
    }
    for (const p of l.workedExamples || []) walkProblem(`${w}:worked`, p);
    for (const p of l.tryIt || []) walkProblem(`${w}:tryIt`, p);
    for (const [i, s] of (l.interactive?.steps || []).entries()) {
      const sw = `${w}:step[${i}]:${s.kind}`;
      for (const f of ["title", "body", "teach", "eyebrow", "prompt", "explanation"]) renderCheck(`${sw}.${f}`, s[f]);
      for (const [j, o] of (s.options || []).entries()) renderCheck(`${sw}.options[${j}]`, o);
      for (const [j, pt] of (s.points || []).entries()) renderCheck(`${sw}.points[${j}]`, pt);
      const rows = Array.isArray(s.config?.rows) ? s.config.rows : [];
      for (const [j, r] of rows.entries()) {
        renderCheck(`${sw}.rows[${j}].statement`, r.statement);
        renderCheck(`${sw}.rows[${j}].reason`, r.reason);
      }
      renderCheck(`${sw}.config.given`, s.config?.given);
      renderCheck(`${sw}.config.prove`, s.config?.prove);
      renderCheck(`${sw}.config.caption`, s.config?.caption);
    }
  }
  for (const p of topic.practice || []) walkProblem(`${slug}:practice`, p);
  for (const p of topic.testYourself || []) walkProblem(`${slug}:testYourself`, p);
}

console.log(`katex QA: ${strings} strings containing math, ${mathSegments} math segments rendered`);
if (failures.length) {
  console.log(`\nFAILURES (${failures.length}):`);
  for (const f of failures.slice(0, 60)) console.log("  x " + f);
  process.exit(1);
}
console.log("  clean: every math segment renders without a katex-error node");
