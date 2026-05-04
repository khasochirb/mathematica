// T2 render verification — exercises the same regex + KaTeX path as
// components/esh/MathText.tsx against every merged solution. Reports:
//   1. coverage: total spans found (display $$, inline $, bold **)
//   2. success criteria: all v2 leads produce <strong>, math produces
//      <span class="katex">, no literal $ or ** leaks
//   3. parse errors: any KaTeX failure that would fall back to <code class="text-red-400">
//   4. random sample of 20 rendered HTML snippets across files
//
// Run: node scripts/verify-v2-render.mjs

import katex from "katex";
import fs from "node:fs";
import path from "node:path";

const JSON_DIR = path.resolve("data/questions");

// Mirror the exact regex from components/esh/MathText.tsx
const SPLIT_RE = /(\$\$[^$]+\$\$|\$[^$]+\$|\*\*[^*]+\*\*)/g;

function renderSolution(text) {
  const parts = text.split(SPLIT_RE);
  const errors = [];
  const html = parts
    .map((part) => {
      if (part.startsWith("$$") && part.endsWith("$$")) {
        const latex = part.slice(2, -2);
        try {
          return katex.renderToString(latex, {
            throwOnError: true,
            displayMode: true,
          });
        } catch (e) {
          errors.push({ type: "display", latex, msg: e.message });
          // Fallback path mirrors MathText.tsx's <code class="text-red-400">
          return `<code class="text-red-400">${latex}</code>`;
        }
      }
      if (part.startsWith("$") && part.endsWith("$")) {
        const latex = part.slice(1, -1);
        try {
          return katex.renderToString(latex, {
            throwOnError: true,
            displayMode: false,
          });
        } catch (e) {
          errors.push({ type: "inline", latex, msg: e.message });
          return `<code class="text-red-400">${latex}</code>`;
        }
      }
      if (part.startsWith("**") && part.endsWith("**")) {
        return `<strong>${part.slice(2, -2)}</strong>`;
      }
      // Plain text
      return part;
    })
    .join("");
  return { html, errors };
}

const stats = {
  totalQuestions: 0,
  totalSolutions: 0,
  withBoldLead: 0,
  withInlineMath: 0,
  withDisplayMath: 0,
  withBoldAnswer: 0,
  parseErrors: [],
  literalDollarLeaks: [],
  literalStarLeaks: [],
};

const samples = [];

const files = fs.readdirSync(JSON_DIR).filter((f) => f.endsWith(".json")).sort();
for (const f of files) {
  const data = JSON.parse(fs.readFileSync(path.join(JSON_DIR, f), "utf-8"));
  for (const q of data) {
    stats.totalQuestions++;
    const sol = q.solution;
    if (!sol) continue;
    stats.totalSolutions++;

    const { html, errors } = renderSolution(sol);

    if (sol.startsWith("**Бодолт.**")) stats.withBoldLead++;
    if (/\*\*[A-E]\*\*/.test(sol)) stats.withBoldAnswer++;
    if (sol.includes("$$")) stats.withDisplayMath++;
    if (/\$[^$]+\$/.test(sol)) stats.withInlineMath++;

    for (const e of errors) {
      stats.parseErrors.push({ source: q.source, ...e });
    }

    // Strip rendered tags and check for literal $ or ** leaks. After rendering,
    // the HTML should contain $ only inside KaTeX-rendered output (which uses
    // its own MathML/HTML for math, not literal $). Strip <span class="katex">...</span>
    // blocks fully, then any remaining $ or ** is a leak.
    const stripped = html
      .replace(/<span class="katex">[\s\S]*?<\/span><\/span>/g, "") // KaTeX wraps in nested spans
      .replace(/<span class="katex-display">[\s\S]*?<\/span><\/span>/g, "")
      .replace(/<span class="katex"[^>]*>[\s\S]*?<\/span>/g, "")
      .replace(/<strong>[^<]*<\/strong>/g, "")
      .replace(/<code class="text-red-400">[\s\S]*?<\/code>/g, "");
    if (stripped.includes("$")) {
      stats.literalDollarLeaks.push({ source: q.source, stripped: stripped.slice(0, 200) });
    }
    if (stripped.includes("**")) {
      stats.literalStarLeaks.push({ source: q.source, stripped: stripped.slice(0, 200) });
    }

    if (samples.length < 20 && Math.random() < 0.02) {
      samples.push({ source: q.source, file: f, sol, html: html.slice(0, 500) });
    }
  }
}

console.log("=== Coverage ===");
console.log(`Total questions: ${stats.totalQuestions}`);
console.log(`Solutions populated: ${stats.totalSolutions}`);
console.log(`With **Бодолт.** bold lead: ${stats.withBoldLead}`);
console.log(`With bold A/B/C/D/E answer: ${stats.withBoldAnswer}`);
console.log(`With inline $...$ math: ${stats.withInlineMath}`);
console.log(`With display $$...$$ math: ${stats.withDisplayMath}`);

console.log("\n=== Success criteria ===");
console.log(`KaTeX parse errors: ${stats.parseErrors.length}`);
console.log(`Literal $ leaks (post-render): ${stats.literalDollarLeaks.length}`);
console.log(`Literal ** leaks (post-render): ${stats.literalStarLeaks.length}`);

if (stats.parseErrors.length > 0) {
  console.log("\n=== KaTeX parse errors ===");
  for (const e of stats.parseErrors.slice(0, 50)) {
    console.log(`  [${e.type}] ${e.source}`);
    console.log(`    latex: ${e.latex.slice(0, 200)}`);
    console.log(`    msg:   ${e.msg.slice(0, 200)}`);
  }
  if (stats.parseErrors.length > 50) {
    console.log(`  ... ${stats.parseErrors.length - 50} more`);
  }
}

if (stats.literalDollarLeaks.length > 0) {
  console.log("\n=== Literal $ leaks ===");
  for (const l of stats.literalDollarLeaks.slice(0, 20)) {
    console.log(`  ${l.source}: ${l.stripped}`);
  }
}

if (stats.literalStarLeaks.length > 0) {
  console.log("\n=== Literal ** leaks ===");
  for (const l of stats.literalStarLeaks.slice(0, 20)) {
    console.log(`  ${l.source}: ${l.stripped}`);
  }
}

console.log("\n=== Random rendered samples (20) ===");
for (const s of samples) {
  console.log(`\n--- ${s.source} (${s.file}) ---`);
  console.log(`SOURCE: ${s.sol.slice(0, 200)}`);
  console.log(`HTML:   ${s.html.slice(0, 300).replace(/\n/g, "\\n")}`);
}

const exitCode = stats.parseErrors.length + stats.literalDollarLeaks.length + stats.literalStarLeaks.length === 0 ? 0 : 1;
console.log(`\n=== Exit ${exitCode} ===`);
process.exit(exitCode);
