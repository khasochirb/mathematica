#!/usr/bin/env python3
"""
Generate an HTML review page from the extracted JSONL problems file.
Renders math with KaTeX for visual spot-checking.
"""

import argparse
import json
import html
import os


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="mn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Problem Review — {total} problems from {pages} pages</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f8f9fa; color: #1a1a1a; padding: 20px; max-width: 900px; margin: 0 auto; }}
  h1 {{ font-size: 1.5rem; margin-bottom: 8px; }}
  .stats {{ color: #666; margin-bottom: 24px; font-size: 0.9rem; }}
  .page-group {{ margin-bottom: 32px; }}
  .page-header {{ font-size: 1.1rem; font-weight: 700; color: #333; padding: 8px 12px; background: #e9ecef; border-radius: 8px; margin-bottom: 12px; position: sticky; top: 0; z-index: 10; }}
  .problem {{ background: #fff; border: 1px solid #dee2e6; border-radius: 8px; padding: 16px; margin-bottom: 8px; }}
  .problem.needs-review {{ border-left: 4px solid #ffc107; }}
  .problem.has-error {{ border-left: 4px solid #dc3545; }}
  .problem-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }}
  .source-label {{ font-size: 0.8rem; font-weight: 600; color: #495057; }}
  .badges {{ display: flex; gap: 6px; }}
  .badge {{ font-size: 0.7rem; padding: 2px 8px; border-radius: 12px; font-weight: 600; }}
  .badge-type {{ background: #e3f2fd; color: #1565c0; }}
  .badge-diff {{ background: #f3e5f5; color: #7b1fa2; }}
  .badge-topic {{ background: #e8f5e9; color: #2e7d32; }}
  .badge-review {{ background: #fff3e0; color: #e65100; }}
  .question {{ font-size: 0.95rem; line-height: 1.6; margin-bottom: 10px; }}
  .options {{ list-style: none; padding-left: 0; }}
  .options li {{ padding: 4px 0; font-size: 0.9rem; }}
  .answer {{ font-size: 0.85rem; color: #388e3c; font-weight: 600; margin-top: 6px; }}
  .error-msg {{ font-size: 0.85rem; color: #dc3545; font-style: italic; }}
  .filters {{ margin-bottom: 20px; display: flex; gap: 8px; flex-wrap: wrap; }}
  .filters button {{ padding: 6px 14px; border: 1px solid #dee2e6; border-radius: 20px; background: #fff; cursor: pointer; font-size: 0.8rem; }}
  .filters button.active {{ background: #1565c0; color: #fff; border-color: #1565c0; }}
</style>
</head>
<body>
<h1>Problem Review</h1>
<div class="stats">{total} problems across {pages} pages &middot; {needs_review} need review &middot; {errors} errors</div>

<div class="filters">
  <button class="active" onclick="filterProblems('all')">All ({total})</button>
  <button onclick="filterProblems('needs-review')">Needs Review ({needs_review})</button>
  <button onclick="filterProblems('has-error')">Errors ({errors})</button>
  <button onclick="filterProblems('MCQ')">MCQ</button>
  <button onclick="filterProblems('NUMERIC')">Numeric</button>
</div>

{content}

<script>
document.addEventListener("DOMContentLoaded", function() {{
  renderMathInElement(document.body, {{
    delimiters: [
      {{left: "$$", right: "$$", display: true}},
      {{left: "$", right: "$", display: false}},
      {{left: "\\\\(", right: "\\\\)", display: false}},
      {{left: "\\\\[", right: "\\\\]", display: true}}
    ],
    throwOnError: false
  }});
}});

function filterProblems(type) {{
  document.querySelectorAll('.filters button').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
  document.querySelectorAll('.problem').forEach(el => {{
    if (type === 'all') {{ el.style.display = ''; return; }}
    if (type === 'needs-review') {{ el.style.display = el.classList.contains('needs-review') ? '' : 'none'; return; }}
    if (type === 'has-error') {{ el.style.display = el.classList.contains('has-error') ? '' : 'none'; return; }}
    el.style.display = el.dataset.type === type ? '' : 'none';
  }});
}}
</script>
</body>
</html>"""


def escape(text: str) -> str:
    """HTML-escape text but preserve $ delimiters for KaTeX."""
    return html.escape(text).replace("\\\\", "\\")


def render_problem(p: dict) -> str:
    classes = ["problem"]
    if p.get("correct_answer") == "NEEDS_REVIEW":
        classes.append("needs-review")

    badges = []
    badges.append(f'<span class="badge badge-type">{p.get("answer_type", "?")}</span>')
    badges.append(f'<span class="badge badge-diff">Diff {p.get("difficulty", "?")}</span>')
    if p.get("topic_hint"):
        badges.append(f'<span class="badge badge-topic">{escape(p["topic_hint"])}</span>')
    if p.get("correct_answer") == "NEEDS_REVIEW":
        badges.append('<span class="badge badge-review">NEEDS REVIEW</span>')

    parts = [
        f'<div class="{" ".join(classes)}" data-type="{p.get("answer_type", "")}">',
        '<div class="problem-header">',
        f'  <span class="source-label">{escape(p.get("source_label", ""))}</span>',
        f'  <div class="badges">{"".join(badges)}</div>',
        '</div>',
        f'<div class="question">{escape(p.get("question", ""))}</div>',
    ]

    if p.get("options"):
        parts.append('<ul class="options">')
        for opt in p["options"]:
            parts.append(f"  <li>{escape(opt)}</li>")
        parts.append("</ul>")

    if p.get("correct_answer"):
        parts.append(f'<div class="answer">Answer: {escape(p["correct_answer"])}</div>')

    parts.append("</div>")
    return "\n".join(parts)


def main():
    parser = argparse.ArgumentParser(description="Generate HTML review page from JSONL")
    parser.add_argument("jsonl_path", help="Path to the problems JSONL file")
    parser.add_argument(
        "-o", "--output", default="review.html",
        help="Output HTML file (default: review.html)"
    )
    args = parser.parse_args()

    if not os.path.isfile(args.jsonl_path):
        print(f"Error: file not found: {args.jsonl_path}")
        return

    pages = []
    with open(args.jsonl_path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                pages.append(json.loads(line))

    pages.sort(key=lambda x: x.get("source_page", 0))

    total = 0
    needs_review = 0
    errors = 0
    content_parts = []

    for page_data in pages:
        page_num = page_data.get("source_page", "?")
        problems = page_data.get("problems", [])
        error = page_data.get("_error")

        if error:
            errors += 1
            content_parts.append(f'<div class="page-group">')
            content_parts.append(f'<div class="page-header">Page {page_num}</div>')
            content_parts.append(f'<div class="problem has-error"><div class="error-msg">Error: {escape(error)}</div></div>')
            content_parts.append("</div>")
            continue

        if not problems:
            continue

        content_parts.append(f'<div class="page-group">')
        content_parts.append(f'<div class="page-header">Page {page_num} — {len(problems)} problems</div>')

        for p in problems:
            total += 1
            if p.get("correct_answer") == "NEEDS_REVIEW":
                needs_review += 1
            content_parts.append(render_problem(p))

        content_parts.append("</div>")

    html_content = HTML_TEMPLATE.format(
        total=total,
        pages=len(pages),
        needs_review=needs_review,
        errors=errors,
        content="\n".join(content_parts),
    )

    with open(args.output, "w") as f:
        f.write(html_content)

    print(f"Generated {args.output}")
    print(f"  {total} problems from {len(pages)} pages")
    print(f"  {needs_review} need review, {errors} errors")


if __name__ == "__main__":
    main()
