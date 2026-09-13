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
    # Regex, because a plain substring replace would turn an already-correct
    # 'диаграмм' into 'диаграммм' on the second run, and --fix must stay
    # idempotent. The lookahead also carries the inflected forms across:
    # 'диаграмын' -> 'диаграммын', 'диаграмд' -> 'диаграммд'.
    (r"диаграм(?!м)", "диаграмм", "10.13в, 11.11а",
     "The standard writes 'диаграмм' in all four of its uses -- 'Цэгэн диаграмм', "
     "'Эйлер-Веннийн диаграмм', 'Иш навчны диаграмм', 'хайрцган диаграммыг' -- and "
     "single-m never. The mirrors had it the other way round, 58 to 7."),
]

# Khas's rulings. NOT ministry evidence, which is why they are not in
# CORRECTIONS above: that list claims to be settled by the standard's own text,
# and diluting it would make every entry in it less trustworthy.
#
# (wrong form, ruled form, date, note)
OWNER_CORRECTIONS = [
    # "pattern is зүй тогтол period. never хэв маяг." -- 13 Sep 2026.
    # Ordered longest-first: 'Хэв маягийг' must match before 'Хэв маяг'.
    # The accusative drops the stem vowel (тогтол -> тогтл-), which is Khas's
    # own form from «Зүй тогтлыг дахин эхлүүлэх».
    (r"Хэв маягийг(?![а-яөүё])", "Зүй тогтлыг", "2026-09-13", "pattern, accusative"),
    (r"хэв маягийг(?![а-яөүё])", "зүй тогтлыг", "2026-09-13", "pattern, accusative"),
    (r"Хэв маяг(?![а-яөүё])", "Зүй тогтол", "2026-09-13", "pattern, nominative"),
    (r"хэв маяг(?![а-яөүё])", "зүй тогтол", "2026-09-13", "pattern, nominative"),
]

# Inflected forms of a ruled term that have NO mapping yet.
#
# Mongolian obliques are not substring swaps -- 'хэв маягийг' becomes
# 'зүй тогтлыг', with the stem vowel dropping -- so each form needs its own
# ruling. Until one exists, a file containing any of these is skipped ENTIRELY
# rather than half-converted: a lesson carrying both «зүй тогтол» and
# «хэв маяг» reads worse than one consistently using the old word, and would
# also hide the remaining work by making the count look almost done.
PENDING_FORMS = [
    r"хэв маягаар(?![а-яөүё])",
    r"хэв маягаас(?![а-яөүё])",
    r"хэв маяггүйгээр(?![а-яөүё])",
    r"хэв маяггүй(?![а-яөүё])",
    r"хэв маягт(?![а-яөүё])",
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


def _rx(pattern):
    """Treat an entry as a regex if it looks like one, else as a literal.

    The original entries were plain strings and must keep working; the newer
    ones need lookaheads to stay idempotent and to avoid matching a longer
    word they are a prefix of.
    """
    return pattern if re.search(r"[()\[\]?*+|\\]", pattern) else re.escape(pattern)


def blocked_files():
    """Files holding an inflected form nobody has ruled on yet.

    Returned so --fix can leave them completely alone. Half-converting a
    lesson is worse than not touching it.
    """
    out = {}
    for path in mn_files():
        text = open(path, encoding="utf-8").read()
        found = []
        for pat in PENDING_FORMS:
            found += re.findall(pat, text)
        if found:
            out[path] = sorted(set(found))
    return out


def scan(skip=()):
    hits = []
    for path in mn_files():
        if path in skip:
            continue
        text = open(path, encoding="utf-8").read()
        for wrong, right, where, _note in CORRECTIONS:
            n = len(re.findall(_rx(wrong), text))
            if n:
                hits.append((path, wrong, right, where, n))
        for wrong, right, when, note in OWNER_CORRECTIONS:
            n = len(re.findall(_rx(wrong), text))
            if n:
                hits.append((path, wrong, right, "Khas %s (%s)" % (when, note), n))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true", help="apply the corrections")
    ap.add_argument("--check", action="store_true", help="fail on non-ministry wording")
    args = ap.parse_args()
    if not (args.fix or args.check):
        args.check = True

    blocked = blocked_files()
    hits = scan(skip=blocked)

    if args.fix:
        changed = set()
        for path, wrong, right, _where, _n in hits:
            text = open(path, encoding="utf-8").read()
            open(path, "w", encoding="utf-8").write(re.sub(_rx(wrong), right, text))
            changed.add(path)
        print("mn_terms --fix: rewrote %d file(s)" % len(changed))
        hits = scan(skip=blocked)

    if blocked:
        print("mn_terms: %d file(s) held back -- an inflected form has no ruling yet:"
              % len(blocked))
        for path, forms in sorted(blocked.items()):
            print("  %s: %s" % (os.path.relpath(path, ROOT), ", ".join(repr(f) for f in forms)))
        print("  (skipped whole, not half-converted -- see PENDING_FORMS)")

    if hits:
        print("mn_terms: %d file(s) use wording that has been ruled against:"
              % len({h[0] for h in hits}))
        for path, wrong, right, where, n in hits:
            # `where` already names its own authority for owner rulings; only
            # the ministry entries need the label adding, and conflating the
            # two is the thing OWNER_CORRECTIONS exists to prevent.
            src = where if where.startswith("Khas") else "ministry: %s" % where
            print("  %s: %r x%d -> %r (%s)"
                  % (os.path.relpath(path, ROOT), wrong, n, right, src))
        return 1
    print("mn_terms: %d file(s) checked, %d enforced term(s), %d glossary entries — clean"
          % (len(mn_files()), len(CORRECTIONS), len(GLOSSARY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
