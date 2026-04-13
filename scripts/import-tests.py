#!/usr/bin/env python3
"""
Import test questions from a CSV file into JSON files for the ESH practice page.

Usage:
  python3 scripts/import-tests.py path/to/tests.csv [--overwrite]

CSV columns: file, index, test_id, question, option_a-option_e, correct_answer, answer_type, topic, subtopic, notes

test_id formats (both are handled):
  - "Test-4A-Q1" (old format, question number embedded)
  - "7A" (new format, just test name; index column = 0-35)

Output: data/questions/test{id}.json for each new test found.
Existing JSON files are skipped unless --overwrite is passed.
"""

import csv, json, os, re, sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/import-tests.py <csv_path> [--overwrite]")
        sys.exit(1)

    csv_path = sys.argv[1]
    overwrite = "--overwrite" in sys.argv

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    out_dir = os.path.join(project_root, "data", "questions")
    os.makedirs(out_dir, exist_ok=True)

    rows_by_test = {}
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tid = row["test_id"].strip()

            if tid.startswith("Test-"):
                parts = tid.split("-")
                test_name = parts[1]
                q_num = int(parts[2].replace("Q", ""))
            else:
                test_name = tid.upper()
                q_num = int(row["index"]) + 1

            match = re.match(r"(\d+)([AB])", test_name)
            if not match:
                print(f"  Warning: skipping unrecognized test_id '{tid}'")
                continue

            test_number = int(match.group(1))
            test_variant = match.group(2)

            if q_num <= 12:
                diff = 1
            elif q_num <= 24:
                diff = 2
            else:
                diff = 3

            entry = {
                "source": f"Test-{test_name}-Q{q_num}",
                "testNumber": test_number,
                "testVariant": test_variant,
                "questionNumber": q_num,
                "type": row.get("answer_type", "MCQ"),
                "topic": row.get("topic", ""),
                "subtopic": row.get("subtopic", ""),
                "difficulty": diff,
                "body": row["question"],
                "options": {
                    "A": row["option_a"],
                    "B": row["option_b"],
                    "C": row["option_c"],
                    "D": row["option_d"],
                    "E": row["option_e"],
                },
                "answer": row["correct_answer"],
                "solution": "",
            }
            rows_by_test.setdefault(test_name, []).append(entry)

    for test_name in rows_by_test:
        rows_by_test[test_name].sort(key=lambda x: x["questionNumber"])

    existing = set()
    for f in os.listdir(out_dir):
        if f.endswith(".json"):
            existing.add(f.replace("test", "").replace(".json", "").upper())

    written = []
    for test_name in sorted(rows_by_test.keys()):
        if test_name in existing and not overwrite:
            print(f"  {test_name}: already exists, skipping (use --overwrite to replace)")
            continue
        fname = os.path.join(out_dir, f"test{test_name.lower()}.json")
        data = rows_by_test[test_name]
        with open(fname, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"  {test_name}: wrote {len(data)} questions to {fname}")
        written.append(test_name)

    if written:
        print(f"\nDone! New tests: {', '.join(written)}")
        print("Remember to add imports and entries in app/practice/esh/page.tsx")
    else:
        print("\nNo new tests to write.")


if __name__ == "__main__":
    main()
