"use client";

import katex from "katex";
import "katex/dist/katex.min.css";

interface MathTextProps {
  text: string;
  className?: string;
}

export default function MathText({ text, className = "" }: MathTextProps) {
  // Split on display math ($$...$$), inline math ($...$), and bold (**...**).
  // Display-math alternative comes first so the longer pattern wins leftmost-first
  // alternation on `$$...$$` strings (otherwise the inline `$...$` alternative would
  // steal the leading `$` and leave a stray trailing `$$` after the match).
  const parts = text.split(/(\$\$[^$]+\$\$|\$[^$]+\$|\*\*[^*]+\*\*)/g);

  return (
    <span className={className}>
      {parts.map((part, i) => {
        if (part.startsWith("$$") && part.endsWith("$$")) {
          const latex = part.slice(2, -2);
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
          const latex = part.slice(1, -1);
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
          return <strong key={i}>{part.slice(2, -2)}</strong>;
        }
        return <span key={i}>{part}</span>;
      })}
    </span>
  );
}
