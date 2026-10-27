#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Case endings for a whole number written in digits: `suffix(12, "gen")` -> "ын".

Python twin of lib/i18n/mn-numerals.ts, for writers who generate many
Mongolian strings from one template (the problem bank: one form, dozens of
numbers). The ending agrees with the numeral AS SPOKEN, not its digits, and
attaches with a hyphen (docs/mn-voice-reference.md §8): «12-ын», «6-гийн»,
«20-ийн».

The spoken number ends in its last non-zero place: 12 -> хоёр, 40 -> дөч,
300 -> зуу, 5000 -> мянга. Only «12-ын» (хоёр) is confirmed by Khas
(13 Sep 2026); the other rows are the standard forms, and CONFIDENT marks the
ones taken straight from the voice reference's corpus counts. Prefer a
sentence that needs no ending on a changing number («4 ба 6 тооны …»);
use this only where the ending is unavoidable, and never hand-type an ending
into a template.

Cases: gen (-ын/-ийн), acc (-ыг/-ийг), dat (-д/-т), abl (-аас/-ээс…), com (-тай/-тэй/-той),
ins (-аар/-ээр…).
"""

# last spoken word -> {case: ending}. Genitives match lib/i18n/mn-numerals.ts.
WORD = {
    "тэг":    {"gen": "ийн", "acc": "ийг", "dat": "т",  "abl": "ээс", "com": "тэй"},
    "нэг":    {"gen": "ийн", "acc": "ийг", "dat": "д",  "abl": "ээс", "com": "тэй"},
    "хоёр":   {"gen": "ын",  "acc": "ыг",  "dat": "т",  "abl": "оос", "com": "той"},
    "гурав":  {"gen": "ын",  "acc": "ыг",  "dat": "д",  "abl": "аас", "com": "тай"},
    "дөрөв":  {"gen": "ийн", "acc": "ийг", "dat": "т",  "abl": "өөс", "com": "тэй"},
    "тав":    {"gen": "ын",  "acc": "ыг",  "dat": "д",  "abl": "аас", "com": "тай"},
    "зургаа": {"gen": "гийн", "acc": "г",  "dat": "д",  "abl": "гаас", "com": "тай"},
    "долоо":  {"gen": "гийн", "acc": "г",  "dat": "д",  "abl": "гоос", "com": "той"},
    "найм":   {"gen": "ын",  "acc": "ыг",  "dat": "д",  "abl": "аас", "com": "тай"},
    "ес":     {"gen": "ийн", "acc": "ийг", "dat": "д",  "abl": "өөс", "com": "тэй"},
    "арав":   {"gen": "ын",  "acc": "ыг",  "dat": "д",  "abl": "аас", "com": "тай"},
    "хорь":   {"gen": "ийн", "acc": "ийг", "dat": "д",  "abl": "иос", "com": "той"},
    "гуч":    {"gen": "ийн", "acc": "ийг", "dat": "ид", "abl": "аас", "com": "тай"},
    "дөч":    {"gen": "ийн", "acc": "ийг", "dat": "ид", "abl": "өөс", "com": "тэй"},
    "тавь":   {"gen": "ийн", "acc": "ийг", "dat": "д",  "abl": "иас", "com": "тай"},
    "жар":    {"gen": "ын",  "acc": "ыг",  "dat": "т",  "abl": "аас", "com": "тай"},
    "дал":    {"gen": "ын",  "acc": "ыг",  "dat": "д",  "abl": "аас", "com": "тай"},
    "ная":    {"gen": "гийн", "acc": "г",  "dat": "д",  "abl": "гаас", "com": "тай"},
    "ер":     {"gen": "ийн", "acc": "ийг", "dat": "т",  "abl": "өөс", "com": "тэй"},
    "зуу":    {"gen": "ны",  "acc": "г",   "dat": "нд", "abl": "наас", "com": "тай"},  # hidden н: зууны
    "мянга":  {"gen": "ын",  "acc": "ыг",  "dat": "д",  "abl": "аас", "com": "тай"},
    "сая":    {"gen": "ын",  "acc": "ыг",  "dat": "д",  "abl": "аас", "com": "тай"},
}
UNITS = ["тэг", "нэг", "хоёр", "гурав", "дөрөв", "тав", "зургаа", "долоо", "найм", "ес"]
TENS = [None, "арав", "хорь", "гуч", "дөч", "тавь", "жар", "дал", "ная", "ер"]


def last_word(n: int) -> str:
    n = abs(int(n))
    if n == 0:
        return "тэг"
    if n % 10:
        return UNITS[n % 10]
    if n % 100:
        return TENS[(n % 100) // 10]
    if n % 1000:
        return "зуу"
    if n % 1_000_000:
        return "мянга"
    return "сая"


def suffix(n, case: str) -> str:
    """The ending alone: suffix(12, 'gen') -> 'ын'.

    "ins" (instrumental, «-аар/-ээр/-оор/-өөр»: «5-аар их», «7-гоор үржүүлэх») is the
    ablative with its final с turned to р, which holds for every row here.
    """
    if case == "ins":
        return WORD[last_word(n)]["abl"][:-1] + "р"
    return WORD[last_word(n)][case]


# An angle is read "<number> градус", so its ending follows градус, never the number.
DEGREE = {"gen": "ын", "acc": "ыг", "dat": "т", "abl": "аас", "com": "тай", "ins": "аар"}


def with_case(n, case: str, math: bool = True, degree: bool = False) -> str:
    """The number with its hyphenated ending: with_case(12, 'gen') -> '$12$-ын'.

    degree=True for an angle: with_case(25, 'gen', degree=True) -> '$25°$-ын'.
    """
    if degree:
        body = f"${n}°$" if math else f"{n}°"
        return f"{body}-{DEGREE[case]}"
    body = f"${n}$" if math else str(n)
    return f"{body}-{suffix(n, case)}"


if __name__ == "__main__":
    for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000):
        print(n, {c: suffix(n, c) for c in ("gen", "acc", "dat", "abl", "com")})
