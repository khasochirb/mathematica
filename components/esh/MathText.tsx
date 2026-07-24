"use client";

import katex from "katex";
import "katex/dist/katex.min.css";

interface MathTextProps {
  text: string;
  className?: string;
}

// A literal dollar sign is written as `\$` in source. We swap it for a private-
// use sentinel BEFORE the math split so it can never be mistaken for a `$...$`
// delimiter, then restore it (as a plain `$` in text, or `\$` inside KaTeX).
// Strings without `\$` are untouched, so existing math content is unaffected.
const DOLLAR_SENTINEL = "";

export default function MathText({ text, className = "" }: MathTextProps) {
  const escaped = text.replace(/\\\$/g, DOLLAR_SENTINEL);

  // Split on display math ($$...$$), inline math ($...$), and bold (**...**).
  // Display-math alternative comes first so the longer pattern wins leftmost-first
  // alternation on `$$...$$` strings (otherwise the inline `$...$` alternative would
  // steal the leading `$` and leave a stray trailing `$$` after the match).
  const parts = escaped.split(/(\$\$[^$]+\$\$|\$[^$]+\$|\*\*[^*]+\*\*)/g);
  // Plain text renders raw, so LaTeX-style escapes that are harmless inside
  // math ("20\%") would show their backslash. Unescape them in text segments;
  // math segments keep the escape for KaTeX.
  const restoreText = (s: string) =>
    s.split(DOLLAR_SENTINEL).join("$").replace(/\\([%#&])/g, "$1");
  const restoreMath = (s: string) => s.split(DOLLAR_SENTINEL).join("\\$");

  return (
    <span className={className}>
      {parts.map((part, i) => {
        if (part.startsWith("$$") && part.endsWith("$$")) {
          const latex = restoreMath(part.slice(2, -2));
          try {
            const html = katex.renderToString(latex, {
              throwOnError: false,
              displayMode: true,
            });
            return (
              <span key={i} dangerouslySetInnerHTML={{ __html: html }} />
            );
          } catch {
            return <code key={i} className="text-red-400">{latex}</code>;
          }
        }
        if (part.startsWith("$") && part.endsWith("$")) {
          const latex = restoreMath(part.slice(1, -1));
          try {
            const html = katex.renderToString(latex, {
              throwOnError: false,
              displayMode: false,
            });
            return (
              <span key={i} dangerouslySetInnerHTML={{ __html: html }} />
            );
          } catch {
            return <code key={i} className="text-red-400">{latex}</code>;
          }
        }
        if (part.startsWith("**") && part.endsWith("**")) {
          return <strong key={i}>{restoreText(part.slice(2, -2))}</strong>;
        }
        return <span key={i}>{restoreText(part)}</span>;
      })}
    </span>
  );
}
