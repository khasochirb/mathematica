#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Voice gate for a Mongolian lesson table: catches the marks of translated prose.

    python3 scripts/i18n/mn_voice.py check <corpus> <slug>   # errors + warnings, writes nothing
    python3 scripts/i18n/mn_voice.py show  <corpus> <slug> [path-substring]
                                                             # English beside Mongolian, per slot

WHY. The structural gates (mn_slots.py, mn_skeleton.py, verify-genmath) prove a
mirror has the right shape and true maths. None of them can tell that
«ЯГ ЭНЭ хөдөлгөөн (ижил өөрчлөлт, хоёр талд) бол тэгшитгэл бодох онолын бүхий л
агуулга» is English wearing Mongolian words, and that sentence shipped. Khas,
29 Oct 2026: "it doesnt have to be like english because it is a whole another
language". This gate catches what a script CAN see; a writer still has to read
every lesson aloud.

ERRORS (the slot must be rewritten):
  * a Cyrillic word in capitals, 5+ letters («ХОЁУЛАНД»): English CAPS emphasis
    copied over. Mongolian prose emphasises with word order or **bold**.
  * an em-dash «—» in prose (English aside punctuation).
  * a phrase on the CALQUES list below: each one shipped and each one is a
    word-for-word English construction.
  * a maths segment of the English slot missing from the Mongolian slot
    (lesson prose may ADD maths, never drop the English's).
WARNINGS (read the slot again):
  * a long sentence (over 30 words): English packs clauses; Mongolian splits.
  * parentheses holding prose: usually an English aside.
"""
import collections
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "scripts", "i18n"))
import mn_slots  # noqa: E402

MATH = re.compile(r"\$\$[^$]+\$\$|\$[^$]+\$")
CAPS = re.compile(r"\b[А-ЯЁӨҮ]{5,}\b")

# Each of these shipped and reads as translated. Lower-case match on prose.
CALQUES = [
    ("аль хэдийн мэдэж", "'you already know': say what to do instead"),
    ("онолын бүхий л агуулга", "'the whole theory of': state the idea plainly"),
    ("бүхий л агуулга", "'the whole content of'"),
    ("рефлекс болго", "'make it a reflex'"),
    ("ачаа биш", "'not a chore'"),
    ("гутлаа тайлдаг", "the shoes-and-socks idiom is English"),
    ("шударга хуваарилалт", "'fair share' as a phrase"),
    ("шинэ нөхцөл, ижил", "'new situation, same rule' slogan"),
    ("гэнэт", "'suddenly' as a narrative beat"),
    ("цэвэрхэн алхам", "'clean step'"),
    ("сөрөг нутаг", "'negative territory'"),
    ("юу үлдэх вэ", "'what sticks' as a recap title: «Санаж авах зүйлс»"),
    ("нууцлаг", "'mystery': just say «хайрцаг» / «үл мэдэгдэх тоо»"),
    ("тоглоом ", "'Play' eyebrow: «Туршаад үз» / «Жинлүүр дээр»"),
    ("гб ", "'ГБ': write «гигабайт» (Khas, 29 Oct: nobody says ГБ)"),
    ("гб.", "'ГБ': write «гигабайт»"),
    ("ажиглаарай", "'watch/notice': «хараарай» or say what happens"),
    ("гэдэг нь … гэсэн үг", None),
]
CALQUES = [(c, why) for c, why in CALQUES if why]


def prose(s):
    return MATH.sub(" ", s.replace("\\$", ""))


def check(corpus, slug):
    src, table, _ = mn_slots.paths(corpus, slug)
    topic = json.load(open(src, encoding="utf-8"))
    tab = json.load(open(table, encoding="utf-8"))
    strings = tab.get("strings", {})
    en = dict(mn_slots.slots(topic))
    errors, warns = [], []
    for p, v in strings.items():
        if not isinstance(v, str):
            continue
        t = prose(v)
        low = t.lower()
        for m in CAPS.findall(t):
            errors.append(f"CAPS {p}: «{m}»")
        if "—" in t:
            errors.append(f"EM-DASH {p}: {v[:70]!r}")
        for c, why in CALQUES:
            if c in low:
                errors.append(f"CALQUE {p}: «{c}» ({why})")
        if p in en:
            want = collections.Counter(MATH.findall(en[p].replace("\\$", "")))
            have = collections.Counter(MATH.findall(v.replace("\\$", "")))
            lost = want - have
            if lost:
                errors.append(f"MATHS DROPPED {p}: {list(lost)[:3]}")
        for sent in re.split(r"[.?!]\s", t):
            if len(sent.split()) > 30:
                warns.append(f"LONG SENTENCE {p}: {sent[:60]!r}…")
        for par in re.findall(r"\(([^()]*)\)", t):
            if len(re.findall(r"[а-яөүё]{3,}", par.lower())) >= 3:
                warns.append(f"PROSE IN PARENTHESES {p}: ({par[:50]})")
    return errors, warns


def main():
    if len(sys.argv) < 4 or sys.argv[1] not in {"check", "show"}:
        print(__doc__)
        return 2
    cmd, corpus, slug = sys.argv[1:4]
    if cmd == "show":
        src, table, _ = mn_slots.paths(corpus, slug)
        topic = json.load(open(src, encoding="utf-8"))
        tab = json.load(open(table, encoding="utf-8"))["strings"]
        needle = sys.argv[4] if len(sys.argv) > 4 else ""
        for p, e in mn_slots.slots(topic):
            if needle in p:
                print(f"--- {p}\nEN {e}\nMN {tab.get(p, '<missing>')}\n")
        return 0
    errors, warns = check(corpus, slug)
    for w in warns[:30]:
        print("  warn:", w)
    for e in errors[:80]:
        print("  ERROR:", e)
    print(f"{'FAIL' if errors else 'OK'} {corpus}/{slug}: {len(errors)} errors, {len(warns)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
