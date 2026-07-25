#!/usr/bin/env python3
"""Shared authoring helpers for the Integrated Mathematics courses (IM1-IM3).

Every unit builder imports these so the schema, the sympy gate and the JSON
writing behave identically across the three courses. Nothing here is
course-specific: the builders supply the mathematics, this file supplies the
scaffolding and refuses to write a file whose checks do not hold.

The contract mirrors scripts/verify-genmath.py: every workedExample, tryIt,
practice, testYourself and tapQuestion carries a non-empty `check` list, and
every entry must sympify to True. Asserting here as well as in the gate means
a broken problem crashes at authoring time, before it can reach a JSON file.
"""
import json
import os

from sympy import sympify  # noqa: F401  (re-exported for builders)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def out_path(course, unit_slug):
    """data/genmath/<course>/<unit>.json — e.g. ("integrated-1", "quantities")."""
    return os.path.join(ROOT, "data", "genmath", course, f"{unit_slug}.json")


def assert_checks(where, checks):
    """Every check must sympify to True. Anything else stops the build."""
    if not checks:
        raise SystemExit(f"{where}: empty check list")
    for expr in checks:
        try:
            value = sympify(expr)
        except Exception as exc:  # noqa: BLE001 — surface the raw sympy error
            raise SystemExit(f"{where}: check does not sympify: {expr!r} ({exc})")
        # Mirror scripts/verify-genmath.py exactly: sympy returns BooleanTrue,
        # not Python True, and an undecidable relational raises on bool().
        try:
            ok = bool(value) is True
        except TypeError:
            ok = False
        if not ok:
            raise SystemExit(f"{where}: check is not True: {expr!r} -> {value!r}")


def problem(pid, statement, solution, check, **extra):
    """A worked example / practice / test problem, verified on construction."""
    assert_checks(pid, check)
    return {"id": pid, "statement": statement, "solution": solution, "check": check, **extra}


def tap(title, prompt, options, correct_index, explanation, check, **extra):
    """A tapQuestion step. The correct option is verified, not asserted."""
    if not 0 <= correct_index < len(options):
        raise SystemExit(f"{title}: correctIndex {correct_index} out of range")
    if len(set(options)) != len(options):
        raise SystemExit(f"{title}: duplicate option text")
    assert_checks(title, check)
    return {
        "kind": "tapQuestion",
        "title": title,
        "prompt": prompt,
        "options": options,
        "correctIndex": correct_index,
        "explanation": explanation,
        "check": check,
        **extra,
    }


def lesson(slug, title, concrete, objective, concept, key_idea, facts, worked, mistakes, try_it, steps):
    """Assemble a lesson, checking the pieces the gate will later re-check."""
    if not concrete.strip():
        raise SystemExit(f"{slug}: concreteComparison is required")
    if not worked:
        raise SystemExit(f"{slug}: at least one worked example is required")
    if not try_it:
        raise SystemExit(f"{slug}: at least one tryIt is required")
    return {
        "slug": slug,
        "title": title,
        "concreteComparison": concrete,
        "objective": objective,
        "concept": concept,
        "keyIdea": key_idea,
        "facts": facts,
        "workedExamples": worked,
        "commonMistakes": mistakes,
        "tryIt": try_it,
        "interactive": {"steps": steps},
    }


def mistake(text, correction):
    return {"text": text, "correction": correction, "authored": True}


def fact(title, latex, explanation):
    return {"title": title, "latex": latex, "explanation": explanation}


def write_unit(course, slug, title, unit_number, blurb, builds_on, lessons, practice, test):
    """Write the unit JSON, after a final sweep over every check in the file."""
    for p in practice:
        assert_checks(p["id"], p.get("check"))
    for p in test:
        assert_checks(p["id"], p.get("check"))

    n_checks = 0
    for les in lessons:
        for group in ("workedExamples", "tryIt"):
            for p in les[group]:
                n_checks += len(p["check"])
        for step in les["interactive"]["steps"]:
            if step["kind"] == "tapQuestion":
                n_checks += len(step["check"])
    n_checks += sum(len(p["check"]) for p in practice)
    n_checks += sum(len(p["check"]) for p in test)

    data = {
        "slug": slug,
        "title": title,
        "unit": unit_number,
        "status": "published",
        "blurb": blurb,
        "buildsOn": builds_on,
        "lessons": lessons,
        "practice": practice,
        "testYourself": test,
    }

    path = out_path(course, slug)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print(
        f"wrote {os.path.relpath(path, ROOT)} — {len(lessons)} lessons, "
        f"{len(practice)} practice, {len(test)} test, {n_checks} sympy checks"
    )
