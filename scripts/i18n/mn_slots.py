#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble a REWRITTEN Mongolian mirror from a path-keyed table.

    python3 scripts/i18n/mn_slots.py extract  <corpus> <slug>   # list every text slot
    python3 scripts/i18n/mn_slots.py assemble <corpus> <slug>   # table -> mirror JSON
    python3 scripts/i18n/mn_slots.py status   <corpus> <slug>   # coverage only, writes nothing

WHY THIS EXISTS. mn_apply.py is a translation machine: one Mongolian string per
English string in one walker order, and its walker skips fields (teach `body`,
recap `bullets`; review pile 6bi). A rewrite keeps the skeleton (ids, step
kinds, every count: mn_skeleton.py) but needs every prose slot reachable and
needs to change a few non-string values: a rescaled worked example's `check[]`,
a widget's currency. So the table here is keyed by JSON PATH, not by walker
index, and it carries an `overrides` section for non-string values.

TABLE: i18n/mn-tables/<corpus>/<slug>.mn.json (committed; it is the source the
mirror is generated from, so a mirror is never hand-edited):

    {
      "strings":   { "lessons/0/title": "…", "lessons/0/interactive/3/beats/1": "…" },
      "overrides": { "lessons/0/workedExamples/1/check": ["Eq(...)"] ,
                     "lessons/3/interactive/2/config/currency": "₮" }
    }

`strings` must cover every slot `extract` lists (copy the English for a slot that
must stay as it is, e.g. a proper name). `overrides` may target any existing
path, string or not. Every check[] that ends up in the mirror is re-run by
`npm run verify:genmath`, and `mn_skeleton.py` gates the structure.
"""
import copy
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TABLES = os.path.join(ROOT, "i18n", "mn-tables")

# Keys whose string values are code, ids or enums, never prose.
DENY = {
    "check", "kind", "id", "problemId", "slug", "mode", "color", "from", "to", "at",
    "status", "hidePoints", "solid", "transform", "op", "type", "varName", "show",
    "pattern", "highlight", "dataset", "reflectAxis", "knownSide", "center", "shape",
    "place", "area", "total", "src", "href", "icon", "widget", "skill_id", "skillId",
    "expr",  # LaTeX source of an orderOfOps stage, never prose
}
CYR = re.compile(r"[А-Яа-яЁёӨөҮү]")
MATH = re.compile(r"\$\$[^$]+\$\$|\$[^$]+\$")
TEXT_ARG = re.compile(r"\\(?:text|textbf|mathrm|operatorname)\{([^{}]*)\}")


def has_prose(s: str) -> bool:
    """True when a reader would see words: Latin letters outside maths, or inside \\text{}."""
    s2 = s.replace("\\$", "")
    outside = MATH.sub("", s2)
    if re.search(r"[A-Za-z]{2,}", outside):
        return True
    for m in MATH.findall(s2):
        for arg in TEXT_ARG.findall(m):
            if re.search(r"[A-Za-z]{2,}", arg):
                return True
    return False


def slots(topic):
    out = []

    def w(o, path, key):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in DENY:
                    continue
                w(v, f"{path}/{k}" if path else k, k)
        elif isinstance(o, list):
            for i, v in enumerate(o):
                w(v, f"{path}/{i}", key)
        elif isinstance(o, str) and has_prose(o):
            out.append((path, o))

    w(topic, "", None)
    return out


def get_parent(obj, path):
    parts = path.split("/")
    cur = obj
    for p in parts[:-1]:
        cur = cur[int(p)] if isinstance(cur, list) else cur[p]
    last = parts[-1]
    return cur, (int(last) if isinstance(cur, list) else last)


def exists(obj, path):
    try:
        parent, k = get_parent(obj, path)
        if isinstance(parent, list):
            return 0 <= k < len(parent)
        return k in parent
    except (KeyError, IndexError, ValueError, TypeError):
        return False


def cyr_in_math(s):
    for m in MATH.findall(s.replace("\\$", "")):
        body = m
        while True:
            nb = TEXT_ARG.sub("", body)
            if nb == body:
                break
            body = nb
        if CYR.search(body):
            return True
    return False


def paths(corpus, slug):
    src = os.path.join(ROOT, "data", "genmath", corpus, f"{slug}.json")
    table = os.path.join(TABLES, corpus, f"{slug}.mn.json")
    out = os.path.join(ROOT, "data", "genmath", f"{corpus}-mn", f"{slug}.json")
    return src, table, out


def cmd_extract(corpus, slug):
    src, table, _ = paths(corpus, slug)
    topic = json.load(open(src, encoding="utf-8"))
    sl = slots(topic)
    os.makedirs(os.path.join(ROOT, "i18n-work"), exist_ok=True)
    dest = os.path.join(ROOT, "i18n-work", f"{corpus}__{slug}.slots.json")
    json.dump([{"p": p, "en": s} for p, s in sl], open(dest, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"{len(sl)} slots -> {dest}")
    print(f"table goes to {table}")


def load_and_check(corpus, slug):
    src, table, out = paths(corpus, slug)
    topic = json.load(open(src, encoding="utf-8"))
    tab = json.load(open(table, encoding="utf-8"))
    strings = tab.get("strings", {})
    overrides = tab.get("overrides", {})
    errors, warns = [], []
    want = dict(slots(topic))
    missing = [p for p in want if p not in strings]
    unknown = [p for p in strings if p not in want and not exists(topic, p)]
    for p in missing:
        errors.append(f"MISSING slot {p}: {want[p][:60]!r}")
    for p in unknown:
        errors.append(f"UNKNOWN path {p}")
    for p in overrides:
        if not exists(topic, p):
            errors.append(f"UNKNOWN override path {p}")
    mn = copy.deepcopy(topic)
    for p, v in strings.items():
        if p in unknown:
            continue
        parent, k = get_parent(mn, p)
        parent[k] = v
    for p, v in overrides.items():
        if exists(mn, p):
            parent, k = get_parent(mn, p)
            parent[k] = v
    untouched = 0
    for p, en in want.items():
        v = strings.get(p)
        if v is None:
            continue
        if not isinstance(v, str):
            errors.append(f"NOT A STRING at {p}")
            continue
        if cyr_in_math(v):
            errors.append(f"CYR-IN-MATH {p}: {v[:70]!r}")
        if v == en and re.search(r"[A-Za-z]{3,}\s+[A-Za-z]{3,}\s+[A-Za-z]{3,}", MATH.sub("", en)):
            untouched += 1
            warns.append(f"STILL ENGLISH {p}: {en[:60]!r}")
        if "*" in v.replace("**", "") and "*" not in en.replace("**", "") and "\\*" not in v:
            if not re.search(r"[<>=!]|\*\s*\d|\d\s*\*", v):
                warns.append(f"SINGLE-ASTERISK {p}: {v[:60]!r}")
    return mn, out, want, errors, warns


def cmd_assemble(corpus, slug, write=True):
    mn, out, want, errors, warns = load_and_check(corpus, slug)
    for w in warns[:40]:
        print("  warn:", w)
    if len(warns) > 40:
        print(f"  … {len(warns) - 40} more warnings")
    if errors:
        for e in errors[:60]:
            print("  ERROR:", e)
        print(f"FAIL {corpus}/{slug}: {len(errors)} errors")
        return 1
    if write:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        json.dump(mn, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        open(out, "a", encoding="utf-8").write("\n")
        print(f"WROTE {os.path.relpath(out, ROOT)} ({len(want)} slots, {len(warns)} warnings)")
    else:
        print(f"OK {corpus}/{slug} ({len(want)} slots, {len(warns)} warnings)")
    return 0


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in {"extract", "assemble", "status"}:
        print(__doc__)
        return 2
    cmd, corpus, slug = sys.argv[1:]
    if cmd == "extract":
        cmd_extract(corpus, slug)
        return 0
    return cmd_assemble(corpus, slug, write=(cmd == "assemble"))


if __name__ == "__main__":
    sys.exit(main())
