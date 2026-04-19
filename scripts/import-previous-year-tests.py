#!/usr/bin/env python3
"""Convert 2024/2025 ЭЕШ CSVs into the Question JSON format used by the practice site.

Input CSVs sit at ~/Desktop/{2024,2025}{A,B,C,D}.csv.
Output JSON files are written to data/questions/{2024,2025}{a,b,c,d}.json.

Topics in the CSVs are a mix of Mongolian and English — we normalize them onto the
existing English keys in lib/esh-questions.ts (TOPIC_LABELS).
"""

import csv, json, os, sys

TOPIC_MAP = {
    "algebra": "algebra",
    "calculus": "calculus",
    "combinatorics": "combinatorics",
    "geometry": "geometry",
    "linear algebra": "other",
    "number theory": "other",
    "probability": "probability",
    "set theory": "other",
    "statistics": "statistics",
    "trigonometry": "trigonometry",
    "Алгебр": "algebra",
    "Анализ": "calculus",
    "Аналитик геометр": "geometry",
    "Арифметик": "algebra",
    "Вектор": "geometry",
    "Геометр": "geometry",
    "Комбинаторик": "combinatorics",
    "Комплекс тоо": "other",
    "Магадлал": "probability",
    "Математик анализ": "calculus",
    "Матриц": "other",
    "Олонлог": "other",
    "Статистик": "statistics",
    "Тригонометр": "trigonometry",
    "Функц": "functions",
}

DESKTOP = os.path.expanduser("~/Desktop")
TESTS = [f"{y}{v}" for y in (2024, 2025) for v in "ABCD"]


def difficulty_for(q_num: int) -> int:
    if q_num <= 12:
        return 1
    if q_num <= 24:
        return 2
    return 3


def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(project_root, "data", "questions")
    os.makedirs(out_dir, exist_ok=True)

    unknown_topics = set()

    for test in TESTS:
        src = os.path.join(DESKTOP, f"{test}.csv")
        if not os.path.exists(src):
            print(f"  skip {test}: {src} not found")
            continue

        year = int(test[:4])
        variant = test[4]
        questions = []

        with open(src, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, start=1):
                raw_topic = row["topic"].strip()
                topic = TOPIC_MAP.get(raw_topic)
                if topic is None:
                    unknown_topics.add(raw_topic)
                    topic = "other"

                questions.append({
                    "source": f"Test-{test}-Q{i}",
                    "testNumber": year,
                    "testVariant": variant,
                    "questionNumber": i,
                    "type": row.get("answer_type", "MCQ").strip() or "MCQ",
                    "topic": topic,
                    "subtopic": row.get("subtopic", "").strip(),
                    "difficulty": difficulty_for(i),
                    "body": row["question"],
                    "options": {
                        "A": row["option_a"],
                        "B": row["option_b"],
                        "C": row["option_c"],
                        "D": row["option_d"],
                        "E": row["option_e"],
                    },
                    "answer": row["correct_answer"].strip().upper(),
                    "solution": row.get("notes", "").strip(),
                })

        out_path = os.path.join(out_dir, f"{test.lower()}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(questions, f, ensure_ascii=False, indent=2)
        print(f"  {test}: wrote {len(questions)} questions → {out_path}")

    if unknown_topics:
        print("\n  WARNING — unmapped topics (defaulted to 'other'):")
        for t in sorted(unknown_topics):
            print(f"    {t!r}")


if __name__ == "__main__":
    main()
