#!/usr/bin/env python3
"""Measure the real ЭШ topic weights from the past papers.

The old /practice/esh/topics page shipped hand-invented weights ("Algebra
~25%") that were never checked against anything. Every question now carries a
canonical topic (scripts/esh/normalize_question_topics.py), so the honest
number is one GROUP BY away: this script counts the questions of the 20 real
past papers (2021-2025, sections 1 and 2 — the premium tests are excluded,
they are our own authoring and would bias the measurement) per main topic and
per subtopic, and writes data/esh/exam-weights.json for the page to import.

The domain layer is parsed out of lib/esh-questions.ts (ESH_DOMAINS), so the
taxonomy has exactly one definition. scripts/verify-esh-question-topics.test.ts
recomputes these counts from the question files and fails if this JSON is
stale — regenerate it whenever questions or the taxonomy change.

Run: python3 scripts/esh/build_exam_weights.py
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
QDIR = os.path.join(ROOT, "data", "questions")
OUT = os.path.join(ROOT, "data", "esh", "exam-weights.json")

# Real past papers: 20YYx.json and 20YYx-section2.json. Premium tests
# (test1a.json ... test7b.json) are deliberately not counted.
PAST_PAPER = re.compile(r"^20\d\d[a-z](-section2)?\.json$")


def load_domains():
    ts = open(os.path.join(ROOT, "lib", "esh-questions.ts"), encoding="utf-8").read()
    m = re.search(r"export const ESH_DOMAINS: EshDomain\[\] = \[(.*?)\n\];", ts, re.S)
    if not m:
        raise SystemExit("ESH_DOMAINS not found in lib/esh-questions.ts")
    domains = []
    for block in re.finditer(r"\{\s*key: \"([a-z_]+)\",(.*?)topics: \[(.*?)\]", m.group(1), re.S):
        key, _mid, topics_src = block.groups()
        topics = re.findall(r"\"([a-z_]+)\"", topics_src)
        domains.append({"key": key, "topics": topics})
    if len(domains) != 5:
        raise SystemExit(f"expected 5 domains, parsed {len(domains)}")
    return domains


def main():
    domains = load_domains()
    topic_to_domain = {t: d["key"] for d in domains for t in d["topics"]}

    per_topic = {}
    papers = set()
    total = 0
    for name in sorted(os.listdir(QDIR)):
        if not PAST_PAPER.match(name):
            continue
        papers.add(name.replace("-section2", ""))
        for q in json.load(open(os.path.join(QDIR, name), encoding="utf-8")):
            topic = q["topic"]
            if topic not in topic_to_domain:
                raise SystemExit(f"{name} {q.get('source')}: non-canonical topic {topic!r} "
                                 f"— run scripts/esh/normalize_question_topics.py first")
            per_topic[topic] = per_topic.get(topic, 0) + 1
            total += 1

    def pct(n):
        return round(100.0 * n / total, 1)

    data = {
        "note": "Measured from the real past papers only (sections 1 and 2); "
                "premium tests are excluded so our own authoring cannot bias "
                "the weights. Regenerate with scripts/esh/build_exam_weights.py.",
        "basedOn": {"papers": len(papers), "questions": total},
        "domains": [
            {
                "key": d["key"],
                "count": sum(per_topic.get(t, 0) for t in d["topics"]),
                "sharePct": pct(sum(per_topic.get(t, 0) for t in d["topics"])),
                "topics": [
                    {"topic": t, "count": per_topic.get(t, 0), "sharePct": pct(per_topic.get(t, 0))}
                    for t in d["topics"]
                ],
            }
            for d in domains
        ],
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    shares = ", ".join(f"{d['key']} {d['sharePct']}%" for d in data["domains"])
    print(f"wrote data/esh/exam-weights.json — {len(papers)} papers, {total} questions: {shares}")


if __name__ == "__main__":
    main()
