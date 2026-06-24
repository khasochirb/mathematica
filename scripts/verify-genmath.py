#!/usr/bin/env python3
"""
General Math content-integrity gate.

For every topic marked status == "published", asserts:
  - every lesson has a non-empty concreteComparison (hard content-bar requirement);
  - every problem (lesson.workedExamples, lesson.tryIt, topic.practice,
    topic.testYourself) has id / statement / solution and a NON-EMPTY `check`;
  - every interactive tapQuestion step has options / correctIndex / explanation
    and a NON-EMPTY `check`;
  - every `check` string sympifies to a boolean that is True.

No published answer (static or interactive) ships without a passing sympy
hard-assert. Exits non-zero on any failure. Placeholder topics are skipped.

Run: npm run verify:genmath
"""
import glob
import json
import os
import sys

from sympy import sympify

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_GLOB = os.path.join(ROOT, "data", "genmath", "**", "*.json")

failures = []
topics_checked = 0
problems_checked = 0
tapq_checked = 0
checks_run = 0


def run_checks(label, checks):
    global checks_run
    for expr in checks:
        checks_run += 1
        try:
            result = sympify(expr)
        except Exception as e:  # noqa: BLE001
            failures.append(f"{label}: check did not sympify: {expr!r} ({e})")
            continue
        try:
            ok = bool(result) is True
        except TypeError:
            ok = False
        if not ok:
            failures.append(f"{label}: check is NOT True: {expr!r} -> {result!r}")


def check_problem(topic_slug, where, problem):
    global problems_checked
    pid = problem.get("id", "<no-id>")
    label = f"{topic_slug} / {where} / {pid}"
    for field in ("id", "statement", "solution"):
        if not problem.get(field):
            failures.append(f"{label}: missing '{field}'")
    checks = problem.get("check")
    if not isinstance(checks, list) or len(checks) == 0:
        failures.append(f"{label}: missing non-empty 'check' (every published problem must be sympy-verified)")
        return
    problems_checked += 1
    run_checks(label, checks)


def check_tap_question(topic_slug, where, step):
    global tapq_checked
    label = f"{topic_slug} / {where} / tapQuestion"
    opts = step.get("options")
    ci = step.get("correctIndex")
    if not isinstance(opts, list) or len(opts) < 2:
        failures.append(f"{label}: needs at least 2 options")
    elif not isinstance(ci, int) or not (0 <= ci < len(opts)):
        failures.append(f"{label}: correctIndex {ci!r} out of range")
    if not step.get("prompt"):
        failures.append(f"{label}: missing prompt")
    if not step.get("explanation"):
        failures.append(f"{label}: missing explanation")
    checks = step.get("check")
    if not isinstance(checks, list) or len(checks) == 0:
        failures.append(f"{label}: missing non-empty 'check'")
        return
    tapq_checked += 1
    run_checks(label, checks)


def main():
    global topics_checked
    files = sorted(glob.glob(DATA_GLOB, recursive=True))
    if not files:
        print("No genmath data files found.", file=sys.stderr)
        sys.exit(1)

    published = []
    for path in files:
        with open(path, "r", encoding="utf-8") as fh:
            topic = json.load(fh)
        if topic.get("status") != "published":
            continue
        published.append(topic.get("slug", os.path.basename(path)))
        topics_checked += 1
        slug = topic.get("slug", "<no-slug>")

        for lesson in topic.get("lessons", []):
            lslug = lesson.get("slug", "<no-lesson-slug>")
            cc = lesson.get("concreteComparison", "")
            if not isinstance(cc, str) or cc.strip() == "":
                failures.append(f"{slug} / {lslug}: concreteComparison is required and must not be empty")
            for ex in lesson.get("workedExamples", []):
                check_problem(slug, f"{lslug}:worked", ex)
            for ex in lesson.get("tryIt", []):
                check_problem(slug, f"{lslug}:tryIt", ex)
            for s in (lesson.get("interactive") or {}).get("steps", []):
                if s.get("kind") == "tapQuestion":
                    check_tap_question(slug, f"{lslug}:interactive", s)

        for ex in topic.get("practice", []):
            check_problem(slug, "practice", ex)
        for ex in topic.get("testYourself", []):
            check_problem(slug, "testYourself", ex)

    if topics_checked == 0:
        print("verify:genmath — no published topics found (nothing gated).")
        sys.exit(0)

    print(f"verify:genmath — published topics: {', '.join(published)}")
    print(f"  problems: {problems_checked}   tap-questions: {tapq_checked}   sympy checks run: {checks_run}")

    if failures:
        print(f"\nFAILED — {len(failures)} issue(s):", file=sys.stderr)
        for f in failures:
            print(f"  ✗ {f}", file=sys.stderr)
        sys.exit(1)

    print("  ✓ all checks passed")
    sys.exit(0)


if __name__ == "__main__":
    main()
