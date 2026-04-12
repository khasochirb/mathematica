#!/usr/bin/env python3
"""
Extract math problems from page images using Anthropic Claude vision API.

Reads PNG images from a folder, sends each to Claude (claude-haiku-4-5),
and writes structured JSONL output (one JSON object per page).
"""

import argparse
import base64
import glob
import json
import os
import sys
import time
from collections import deque

import anthropic


SYSTEM_PROMPT = """You are an expert at reading Mongolian math exam papers. You will be given a scanned page image from a Mongolian ЭЕШ (university entrance exam) practice booklet.

Your job is to extract EVERY math problem visible on the page into structured JSON.

Rules:
1. Preserve all mathematical notation using LaTeX with $...$ delimiters. Never simplify or reorder expressions.
2. For fractions use \\frac{a}{b}, for roots use \\sqrt{}, for powers use ^{}, etc.
3. If the page contains Part 1 (multiple choice), set answer_type to "MCQ" and list all options (A through E) in the options array.
4. If the page contains Part 2 (fill-in-the-blank / free response), set answer_type to "NUMERIC" or "NUMERIC_RANGE" as appropriate. Set options to null.
5. For correct_answer: if you can confidently determine the answer, provide it. Otherwise set it to "NEEDS_REVIEW".
6. topic_hint should be a short English label like "algebra", "trigonometry", "geometry", "calculus", "probability", "statistics", "vectors", "matrices", "complex numbers", "sequences", "functions", "inequalities", "logarithms", "combinatorics", etc.
7. difficulty should be 1-5 based on your assessment (1=easy, 5=very hard).
8. source_label should identify the test and question, e.g. "Test 1A, Q3" or "Test 5B, Q12".
9. If the page has no math problems (e.g. cover page, blank page, instructions only), return an empty problems array.
10. Mongolian text should be preserved as-is (UTF-8). Do not translate it.

Return ONLY valid JSON with this exact structure (no markdown fences, no extra text):
{
  "problems": [
    {
      "question": "LaTeX string with $...$ notation for math",
      "answer_type": "MCQ" | "NUMERIC" | "NUMERIC_RANGE",
      "options": ["A. ...", "B. ...", "C. ...", "D. ...", "E. ..."] or null,
      "correct_answer": "string or NEEDS_REVIEW",
      "topic_hint": "short English topic label",
      "difficulty": 1-5,
      "source_label": "e.g. Test 3A, Q7"
    }
  ]
}"""


class RateLimiter:
    """Sliding-window rate limiter."""

    def __init__(self, limit: int = 50, window: float = 60.0):
        self.limit = limit
        self.window = window
        self.timestamps: deque = deque()

    def wait(self):
        now = time.time()
        while self.timestamps and self.timestamps[0] <= now - self.window:
            self.timestamps.popleft()
        if len(self.timestamps) >= self.limit:
            sleep_until = self.timestamps[0] + self.window
            wait_time = sleep_until - now + 0.1
            if wait_time > 0:
                print(f"    Rate limit — waiting {wait_time:.1f}s...", flush=True)
                time.sleep(wait_time)
        self.timestamps.append(time.time())


def encode_image(path: str) -> str:
    with open(path, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")


def extract_page(client: anthropic.Anthropic, image_path: str, model: str) -> dict:
    b64 = encode_image(image_path)
    ext = os.path.splitext(image_path)[1].lower()
    media_type = "image/png" if ext == ".png" else "image/jpeg"

    response = client.messages.create(
        model=model,
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": b64,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Extract all math problems from this exam page. Return JSON only.",
                    },
                ],
            }
        ],
    )

    text = response.content[0].text.strip()
    # Strip markdown fences if the model wraps them
    if text.startswith("```"):
        first_nl = text.find("\n")
        text = text[first_nl + 1:] if first_nl != -1 else text[3:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()

    return json.loads(text)


def main():
    parser = argparse.ArgumentParser(
        description="Extract math problems from page images using Claude vision"
    )
    parser.add_argument("image_dir", help="Directory containing PNG page images")
    parser.add_argument(
        "-o", "--output", default="problems.jsonl",
        help="Output JSONL file path (default: problems.jsonl)"
    )
    parser.add_argument(
        "--model", default="claude-haiku-4-5-20241022",
        help="Anthropic model to use (default: claude-haiku-4-5-20241022)"
    )
    parser.add_argument(
        "--start-page", type=int, default=None,
        help="Start from this page number (matches page_NNNN.png naming)"
    )
    parser.add_argument(
        "--end-page", type=int, default=None,
        help="End at this page number (inclusive)"
    )
    parser.add_argument(
        "--rpm", type=int, default=50,
        help="Max requests per minute (default: 50)"
    )
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    rate_limiter = RateLimiter(limit=args.rpm, window=60.0)

    # Find all page images sorted by name
    patterns = [os.path.join(args.image_dir, f"page_*.{ext}") for ext in ("png", "jpg", "jpeg")]
    image_files = sorted(set(f for p in patterns for f in glob.glob(p)))

    if not image_files:
        print(f"No page images found in {args.image_dir}")
        sys.exit(1)

    # Filter by page range if specified
    if args.start_page or args.end_page:
        filtered = []
        for f in image_files:
            basename = os.path.splitext(os.path.basename(f))[0]
            try:
                page_num = int(basename.split("_")[1])
            except (IndexError, ValueError):
                continue
            if args.start_page and page_num < args.start_page:
                continue
            if args.end_page and page_num > args.end_page:
                continue
            filtered.append(f)
        image_files = filtered

    print(f"Processing {len(image_files)} images with model {args.model}")
    print(f"Rate limit: {args.rpm} requests/minute")
    print(f"Output: {args.output}")

    # Load existing results to support resuming
    existing_pages = set()
    if os.path.isfile(args.output):
        with open(args.output, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        obj = json.loads(line)
                        if not obj.get("_error"):
                            existing_pages.add(obj.get("source_page"))
                    except json.JSONDecodeError:
                        pass
        if existing_pages:
            print(f"Resuming — {len(existing_pages)} pages already processed successfully")

    with open(args.output, "a") as out_f:
        for i, img_path in enumerate(image_files):
            basename = os.path.splitext(os.path.basename(img_path))[0]
            try:
                page_num = int(basename.split("_")[1])
            except (IndexError, ValueError):
                page_num = i + 1

            if page_num in existing_pages:
                print(f"  [{i+1}/{len(image_files)}] Page {page_num} — already done, skipping")
                continue

            print(f"  [{i+1}/{len(image_files)}] Page {page_num} — extracting...", end=" ", flush=True)

            rate_limiter.wait()

            try:
                result = extract_page(client, img_path, args.model)
                record = {
                    "source_page": page_num,
                    "problems": result.get("problems", []),
                }
                out_f.write(json.dumps(record, ensure_ascii=False) + "\n")
                out_f.flush()
                n = len(record["problems"])
                print(f"OK — {n} problem{'s' if n != 1 else ''}")
            except json.JSONDecodeError as e:
                print(f"JSON parse error: {e}")
                error_record = {
                    "source_page": page_num,
                    "problems": [],
                    "_error": f"JSON parse error: {e}",
                }
                out_f.write(json.dumps(error_record, ensure_ascii=False) + "\n")
                out_f.flush()
            except anthropic.APIError as e:
                print(f"API error: {e}")
                error_record = {
                    "source_page": page_num,
                    "problems": [],
                    "_error": f"API error: {e}",
                }
                out_f.write(json.dumps(error_record, ensure_ascii=False) + "\n")
                out_f.flush()

    print(f"\nDone — results written to {args.output}")


if __name__ == "__main__":
    main()
