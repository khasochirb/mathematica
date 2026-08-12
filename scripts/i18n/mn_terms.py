#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mongolian mathematical terminology — the ministry's wording, enforced.

Mongolia's Ministry of Education fixes the vocabulary of school mathematics
in the grade 10-12 standard (order А/492, 2019-08-01; the syllabus itself is
parsed into data/esh/moe-curriculum.json). Where the ministry has a word, we
use the ministry's word: a student who meets "тэнцэтгэл биш" in class and
"тэнцэтгэл бус" on this site has been given two names for one thing, and the
site is the one that is wrong.

This module is the enforceable half of the glossary in the `mn-translation`
skill. It exists because translation tables live in a gitignored work
directory: once a topic is translated the table is usually gone, so a
terminology error in a shipped MN mirror cannot be fixed by "regenerate from
the table" and would otherwise be fixed by hand and silently reintroduced.

  python3 scripts/i18n/mn_terms.py --check    # gate: non-ministry wording
  python3 scripts/i18n/mn_terms.py --fix      # apply, re-appliably

`--fix` is idempotent and safe to re-run after any regeneration, which is
what keeps it inside the pipeline rather than a hand edit of generated JSON.
"""
import argparse
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# (wrong form, ministry form, where the ministry uses it, note)
# Only entries where the ministry's own text settles the question. A term the
# standard does not contain does NOT belong here — this list is evidence, not
# preference.
CORRECTIONS = [
    ("тэнцэтгэл бус", "тэнцэтгэл биш", "10.5, 11.1, 12.1",
     "The standard writes 'тэнцэтгэл биш' 13 times and 'тэнцэтгэл бус' never."),
]

# Terms the ministry uses that a translator is likely to improvise around.
# Not enforced (many have legitimate inflected forms) — this is the reference
# half, kept next to the enforced half so the two cannot drift apart.
GLOSSARY = {
    # Algebra — АЛГЕБР
    "power, exponent": "зэрэг; илтгэгч (rational exponent: рационал илтгэгч)",
    "expression": "илэрхийлэл",
    "factorise": "үржигдэхүүн болгон задлах",
    "algebraic fraction": "алгебрын бутархай",
    "equation": "тэгшитгэл",
    "inequality": "тэнцэтгэл биш",
    "system of equations": "тэгшитгэлийн систем",
    "completing the square": "бүтэн квадрат ялгах",
    "discriminant / analysing the roots": "шийдийг шинжлэх",
    "polynomial": "олон гишүүнт",
    "quotient and remainder": "ногдвор ба үлдэгдэл",
    "partial fractions": "тодорхой бус коэффициентийн арга",
    "set": "олонлог",
    "matrix": "матриц",
    "determinant": "тодорхойлогч",
    "inverse matrix": "урвуу матриц",
    "Gaussian elimination": "Гауссын арга",
    "Cramer's rule": "Крамерын дүрэм",
    "complex number": "комплекс тоо",
    "real and imaginary part": "бодит ба хуурмаг хэсэг",
    "conjugate": "хосмог",
    "modulus": "модул",
    # Functions — ФУНКЦ БА ГРАФИК
    "function": "функц",
    "domain": "тодорхойлогдох муж",
    "range": "утгын муж; дүр",
    "composite function": "давхар функц",
    "inverse function": "урвуу функц",
    "one-to-one": "харилцан нэг утгатай",
    "increasing / decreasing": "өсөх / буурах",
    "even / odd function": "тэгш / сондгой функц",
    "asymptote-free wording for graphs": "графикийг тоймлон зурах (sketch)",
    "logarithm": "логарифм",
    "sequence": "дараалал",
    "series": "цуваа",
    "progression": "прогресс",
    "binomial expansion": "бином задаргаа",
    "convergence": "нийлэлт (нийлэх нөхцөл)",
    "mathematical induction": "математик индукц",
    # Geometry & trigonometry — ГЕОМЕТР БА ТРИГОНОМЕТР
    "chord, tangent, secant": "хөвч, шүргэгч, огтлогч",
    "inscribed angle": "тойрогт багтсан өнцөг",
    "locus": "цэгийн геометр байр",
    "gradient / slope": "налалт",
    "vector": "вектор",
    "collinear": "коллинеар",
    "scalar product": "скаляр үржвэр",
    "basis vectors": "суурь вектор",
    "transformation": "хувиргалт",
    "reflection": "тэгш хэмээр хувиргах",
    "translation": "параллель зөөлт",
    "rotation": "эргүүлэлт",
    "enlargement / homothety": "гомотет",
    "cross-section": "хавтгай огтлол",
    "arc length": "нумын урт",
    "sector": "сектор",
    "radian": "радиан",
    "identity": "адилтгал",
    "compound-angle formula": "нийлбэр, ялгаврын томьёо",
    "double-angle formula": "давхар өнцгийн томьёо",
    "auxiliary angle": "туслах өнцөг",
    "skew lines": "солбисон шулуун",
    "plane (in space)": "хавтгай",
    # Analysis — АНАЛИЗЫН ЭХЛЭЛ
    "derivative": "уламжлал",
    "differentiate": "дифференциалчлах",
    "tangent and normal": "шүргэгч ба нормал",
    "rate of change": "өөрчлөлтийн хурд",
    "stationary / extremum point": "экстремум цэг",
    "concave / convex": "хотгор / гүдгэр",
    "point of inflection": "нугаралтын цэг",
    "second derivative": "II эрэмбийн уламжлал",
    "integral": "интеграл",
    "definite integral": "тодорхой интеграл",
    "integration by parts": "хэсэгчлэн интегралчлах",
    "substitution": "орлуулгын арга",
    "trapezium rule": "трапецын дүрэм",
    "solid of revolution": "эргэлтийн бие",
    "differential equation": "дифференциал тэгшитгэл",
    "general / particular solution": "ерөнхий / тухайн шийд",
    # Probability & statistics — МАГАДЛАЛ, СТАТИСТИК
    "grouped data": "бүлэглэсэн өгөгдөл",
    "histogram": "гистограмм",
    "scatter plot": "цэгэн диаграмм",
    "correlation": "корреляц",
    "cumulative frequency": "хуримтлагдсан давтамж",
    "quartile": "квартил",
    "interquartile range": "квартил хоорондын далайц",
    "stem-and-leaf": "иш навчны диаграмм",
    "box plot": "хайрцган диаграмм",
    "variance": "дисперс",
    "standard deviation": "стандарт хазайлт",
    "permutation": "сэлгэмэл",
    "combination": "хэсэглэл",
    "factorial": "факториал",
    "mutually exclusive / not": "нийцгүй / нийцтэй үзэгдэл",
    "independent / dependent": "үл хамаарах / хамаарах",
    "conditional probability": "нөхцөлт магадлал",
    "tree diagram": "модны схем",
    "discrete random variable": "дискрет санамсаргүй хувьсагч",
    "expected value": "математик дундаж",
    "binomial distribution": "бином тархалт",
    "normal distribution": "хэвийн тархалт",
    "geometric probability": "геометр магадлал",
}

MN_GLOBS = [
    "data/genmath/*-mn/*.json",
    "data/questions/**/*.json",
    "data/esh/*.json",
]


def mn_files():
    seen = []
    for pat in MN_GLOBS:
        for path in glob.glob(os.path.join(ROOT, pat), recursive=True):
            if path.endswith("moe-curriculum.json"):
                continue          # the ministry's own text is the authority
            seen.append(path)
    return sorted(set(seen))


def scan():
    hits = []
    for path in mn_files():
        text = open(path, encoding="utf-8").read()
        for wrong, right, where, _note in CORRECTIONS:
            n = len(re.findall(re.escape(wrong), text))
            if n:
                hits.append((path, wrong, right, where, n))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true", help="apply the corrections")
    ap.add_argument("--check", action="store_true", help="fail on non-ministry wording")
    args = ap.parse_args()
    if not (args.fix or args.check):
        args.check = True

    hits = scan()
    if args.fix:
        changed = 0
        for path, wrong, right, _where, _n in hits:
            text = open(path, encoding="utf-8").read()
            open(path, "w", encoding="utf-8").write(text.replace(wrong, right))
            changed += 1
        print("mn_terms --fix: rewrote %d file(s)" % changed)
        hits = scan()

    if hits:
        print("mn_terms: %d file(s) use wording the ministry standard does not:"
              % len({h[0] for h in hits}))
        for path, wrong, right, where, n in hits:
            print("  %s: %r x%d -> %r (ministry: %s)"
                  % (os.path.relpath(path, ROOT), wrong, n, right, where))
        return 1
    print("mn_terms: %d file(s) checked, %d enforced term(s), %d glossary entries — clean"
          % (len(mn_files()), len(CORRECTIONS), len(GLOSSARY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
