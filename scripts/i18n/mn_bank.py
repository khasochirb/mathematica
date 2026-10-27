#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mongolian problem bank: per-unit rewrite tables -> one generated mirror per subject.

    python3 scripts/i18n/mn_bank.py extract  <corpus> <unit>   # English of one unit, for the writer
    python3 scripts/i18n/mn_bank.py check    <corpus> <unit>   # gate one unit's table, write nothing
    python3 scripts/i18n/mn_bank.py assemble <corpus>          # every finished unit -> the mirror
    python3 scripts/i18n/mn_bank.py show     <corpus> <unit> [n] # English beside Mongolian, n per form
    python3 scripts/i18n/mn_bank.py register                   # regenerate lib/bank-data-mn.ts
    python3 scripts/i18n/mn_bank.py status                     # coverage per subject

WHY PER UNIT. A subject holds 500–3,700 variants; one writer cannot hold that,
and a unit (~100–500 variants) is what a writer can rewrite and re-read. The
mirror is still one file per subject so the loader stays a lookup.

TABLE: i18n/bank-tables/<corpus>/<unit>.mn.json (committed; the mirror is
generated from it and never hand-edited):

    {
      "unit":  {"title": "…", "blurb": "…"},
      "forms": {
        "<formId>": {
          "title": "…", "skill": "…",
          "variants": {
            "<variantId>": {"statement": "…", "options": ["…","…","…","…"],
                            "explanation": "…", "labels": {"<geo label>": "…"}}
          }
        }
      }
    }

and, once per subject, i18n/bank-tables/<corpus>/_topic.mn.json with
{"title": "…", "blurb": "…"}.

WHAT THE GATE HOLDS FIXED. Bank answers are graded against a stored key and
re-verified by check[], so a rewrite may change words but never numbers:

  * every form and variant of the unit is present (a unit ships whole or not at all);
  * a statement keeps exactly the English's maths ($…$ segments, as a multiset)
    and the English's digits outside maths;
  * an option that is maths only stays byte-identical; options keep their order,
    so correctIndex is untouched by construction;
  * an explanation keeps every maths segment the English has;
  * no Cyrillic inside maths except inside \\text{}; no leftover English prose.

The mirror copies ids, correctIndex, check[] and level from the English, so
`scripts/verify-problembank.py`-style checks still hold for it.
"""
import collections
import copy
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "data", "problembank")
OUT = os.path.join(ROOT, "data", "problembank-mn")
TABLES = os.path.join(ROOT, "i18n", "bank-tables")

MATH = re.compile(r"\$\$[^$]+\$\$|\$[^$]+\$")
TEXT_ARG = re.compile(r"\\(?:text|textbf|mathrm|operatorname)\{([^{}]*)\}")
CYR = re.compile(r"[А-Яа-яЁёӨөҮү]")
# Latin words a Mongolian sentence may legitimately carry: units, symbols,
# proper names. Anything else of 3+ letters outside maths is leftover English.
LATIN_OK = {
    "cm", "mm", "km", "kg", "ml", "km/h", "m/s", "mph", "SI", "GPS", "NASA", "DNA", "PIN",
    "sin", "cos", "tan", "tg", "ctg", "log", "ln", "lim", "max", "min", "mod", "gcd", "lcm",
    "BMI", "USB", "GB", "MB", "TV", "ID", "QR", "PDF", "SAT", "IQ", "CO",
}


def strip_math(s):
    return MATH.sub(" ", s.replace("\\$", ""))


def maths(s):
    return [m for m in MATH.findall(s.replace("\\$", "\x00")) ]


def digits(s):
    # digits outside maths, with thousands separators (",", " ", thin space) removed
    t = strip_math(s)
    t = re.sub(r"(?<=\d)[ ,\u202f\u00a0](?=\d{3}\b)", "", t)
    return sorted(re.findall(r"\d+(?:[.,]\d+)?", t))


def norm_num(x):
    return x.replace(",", ".")


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


def english_left(s):
    words = re.findall(r"[A-Za-z][A-Za-z'’-]{2,}", strip_math(s))
    return [w for w in words if w not in LATIN_OK and w.lower() not in LATIN_OK]


def load_src(corpus):
    return json.load(open(os.path.join(SRC, f"{corpus}.json"), encoding="utf-8"))


def unit_forms(topic, unit):
    return [f for f in topic["forms"] if f["unit"] == unit]


def table_path(corpus, unit):
    return os.path.join(TABLES, corpus, f"{unit}.mn.json")


def cmd_extract(corpus, unit):
    t = load_src(corpus)
    u = next((x for x in t["units"] if x["id"] == unit), None)
    if not u:
        raise SystemExit(f"no unit {unit} in {corpus}")
    forms = unit_forms(t, unit)
    out = {"unit": u, "forms": [{k: v for k, v in f.items()} for f in forms]}
    for f in out["forms"]:
        for v in f["variants"]:
            v.pop("check", None)
    os.makedirs(os.path.join(ROOT, "i18n-work"), exist_ok=True)
    dest = os.path.join(ROOT, "i18n-work", f"bank__{corpus}__{unit}.en.json")
    json.dump(out, open(dest, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    nv = sum(len(f["variants"]) for f in forms)
    print(f"{len(forms)} forms, {nv} variants -> {dest}")
    print(f"table goes to {table_path(corpus, unit)}")


def geo_labels(v):
    labels = []
    g = v.get("geoFigure") or {}
    for key in ("points", "objects", "labels"):
        for o in g.get(key, []) or []:
            if isinstance(o, dict) and isinstance(o.get("label"), str):
                labels.append(o["label"])
            if isinstance(o, dict) and isinstance(o.get("text"), str):
                labels.append(o["text"])
    return labels


def check_unit(corpus, unit, t=None, quiet=False):
    t = t or load_src(corpus)
    p = table_path(corpus, unit)
    if not os.path.exists(p):
        return None, [f"no table {os.path.relpath(p, ROOT)}"], []
    tab = json.load(open(p, encoding="utf-8"))
    errs, warns = [], []
    tu = tab.get("unit", {})
    for k in ("title",):
        if not tu.get(k):
            errs.append(f"unit.{k} missing")
    tf = tab.get("forms", {})
    for f in unit_forms(t, unit):
        mf = tf.get(f["id"])
        if not mf:
            errs.append(f"form {f['id']} missing")
            continue
        for k in ("title", "skill"):
            if not mf.get(k):
                errs.append(f"{f['id']}.{k} missing")
            elif english_left(mf[k]):
                warns.append(f"{f['id']}.{k} still English? {english_left(mf[k])[:4]}")
        mv = mf.get("variants", {})
        for v in f["variants"]:
            vid = v["id"]
            m = mv.get(vid)
            where = f"{f['id']}/{vid}"
            if not m:
                errs.append(f"{where} missing")
                continue
            st, ex, op = m.get("statement", ""), m.get("explanation", ""), m.get("options", [])
            if not st or not ex:
                errs.append(f"{where}: statement/explanation empty")
                continue
            if len(op) != len(v["options"]):
                errs.append(f"{where}: {len(op)} options, English has {len(v['options'])}")
                continue
            if collections.Counter(maths(st)) != collections.Counter(maths(v["statement"])):
                errs.append(f"{where}: statement maths differ\n      en {maths(v['statement'])}\n      mn {maths(st)}")
            if [norm_num(x) for x in digits(st)] != [norm_num(x) for x in digits(v["statement"])]:
                errs.append(f"{where}: statement numbers differ en {digits(v['statement'])} mn {digits(st)}")
            missing = [x for x in set(maths(v["explanation"])) if x not in set(maths(ex))]
            if missing:
                errs.append(f"{where}: explanation drops maths {missing[:3]}")
            for i, (eo, mo) in enumerate(zip(v["options"], op)):
                if not strip_math(eo).strip() and eo != mo:
                    errs.append(f"{where}: option {i} is maths only and must stay identical ({eo!r} -> {mo!r})")
                elif strip_math(eo).strip():
                    if collections.Counter(maths(eo)) != collections.Counter(maths(mo)):
                        errs.append(f"{where}: option {i} maths differ ({eo!r} -> {mo!r})")
                    if [norm_num(x) for x in digits(eo)] != [norm_num(x) for x in digits(mo)]:
                        errs.append(f"{where}: option {i} numbers differ ({eo!r} -> {mo!r})")
            for s in [st, ex, *op]:
                if cyr_in_math(s):
                    errs.append(f"{where}: Cyrillic inside maths: {s[:70]!r}")
                if "*" in s.replace("**", ""):
                    warns.append(f"{where}: single asterisk")
                if "—" in s:
                    warns.append(f"{where}: em-dash (rephrase; no em-dash asides in Mongolian)")
                left = english_left(s)
                if left:
                    warns.append(f"{where}: English left {left[:4]}")
            labels = m.get("labels", {})
            for lab in geo_labels(v):
                if re.search(r"[A-Za-z]{3,}", lab) and lab not in labels:
                    warns.append(f"{where}: figure label {lab!r} not rewritten")
    if not quiet:
        for w in warns[:30]:
            print("  warn:", w)
        if len(warns) > 30:
            print(f"  … {len(warns) - 30} more warnings")
        for e in errs[:40]:
            print("  ERROR:", e)
        if len(errs) > 40:
            print(f"  … {len(errs) - 40} more errors")
    return tab, errs, warns


def apply_labels(g, labels):
    g = copy.deepcopy(g)
    for key in ("points", "objects", "labels"):
        for o in g.get(key, []) or []:
            if isinstance(o, dict):
                for k in ("label", "text"):
                    if isinstance(o.get(k), str) and o[k] in labels:
                        o[k] = labels[o[k]]
    return g


def cmd_assemble(corpus):
    t = load_src(corpus)
    mn = {k: copy.deepcopy(v) for k, v in t.items() if k != "forms"}
    topic_tab = os.path.join(TABLES, corpus, "_topic.mn.json")
    if os.path.exists(topic_tab):
        tt = json.load(open(topic_tab, encoding="utf-8"))
        mn["title"] = tt.get("title", mn.get("titleMn") or mn["title"])
        mn["blurb"] = tt.get("blurb", mn["blurb"])
    elif mn.get("titleMn"):
        mn["title"] = mn["titleMn"]
    mn["forms"] = []
    done, failed = [], []
    for u in mn["units"]:
        tab, errs, _ = check_unit(corpus, u["id"], t, quiet=True)
        if tab is None:
            continue
        if errs:
            failed.append((u["id"], len(errs)))
            continue
        u["title"] = tab["unit"]["title"]
        if tab["unit"].get("blurb"):
            u["blurb"] = tab["unit"]["blurb"]
        for f in unit_forms(t, u["id"]):
            mf = tab["forms"][f["id"]]
            nf = copy.deepcopy(f)
            nf["title"], nf["skill"] = mf["title"], mf["skill"]
            for v in nf["variants"]:
                m = mf["variants"][v["id"]]
                v["statement"], v["explanation"], v["options"] = m["statement"], m["explanation"], m["options"]
                if v.get("geoFigure") and m.get("labels"):
                    v["geoFigure"] = apply_labels(v["geoFigure"], m["labels"])
            mn["forms"].append(nf)
        done.append(u["id"])
    if failed:
        print("NOT INCLUDED (gate errors):", ", ".join(f"{u} ({n})" for u, n in failed))
    if not done:
        print(f"{corpus}: no finished unit, mirror not written")
        return 1 if failed else 0
    os.makedirs(OUT, exist_ok=True)
    dest = os.path.join(OUT, f"{corpus}.json")
    json.dump(mn, open(dest, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(dest, "a", encoding="utf-8").write("\n")
    nv = sum(len(f["variants"]) for f in mn["forms"])
    print(f"WROTE {os.path.relpath(dest, ROOT)}: {len(done)}/{len(mn['units'])} units, {nv} variants")
    cmd_register()
    return 1 if failed else 0


REGISTRY = os.path.join(ROOT, "lib", "bank-data-mn.ts")


def cmd_register():
    """Rewrite lib/bank-data-mn.ts: one static import per mirror on disk.

    Generated, like the lesson registry (mn_register.py): a mirror that exists
    is reachable, one that does not is never imported. Server-only, like
    lib/bank-data.ts, which is its only importer.
    """
    names = sorted(f[:-5] for f in os.listdir(OUT) if f.endswith(".json")) if os.path.isdir(OUT) else []
    ident = lambda c: "mn" + "".join(p[:1].upper() + p[1:] for p in re.split(r"[^A-Za-z0-9]+", c) if p)
    lines = [
        "// GENERATED by scripts/i18n/mn_bank.py — do not edit by hand.",
        "// The Mongolian problem-bank mirrors on disk. SERVER-SIDE ONLY: imported by",
        "// lib/bank-data.ts alone (same boundary, same reason: lib/bank-split.test.ts).",
        "",
        'import type { BankTopic } from "@/lib/problem-bank";',
    ]
    lines += [f'import {ident(c)} from "@/data/problembank-mn/{c}.json";' for c in names]
    lines += ["", "export const BANK_MN: Record<string, BankTopic> = {"]
    lines += [f'  "{c}": {ident(c)} as unknown as BankTopic,' for c in names]
    lines += ["};", ""]
    new = "\n".join(lines)
    old = open(REGISTRY, encoding="utf-8").read() if os.path.exists(REGISTRY) else ""
    if new != old:
        open(REGISTRY, "w", encoding="utf-8").write(new)
        print(f"registered {len(names)} mirror(s) in lib/bank-data-mn.ts")


def cmd_show(corpus, unit, n=3):
    """English beside Mongolian for the first n variants of every form (brief step 6)."""
    t = load_src(corpus)
    tab = json.load(open(table_path(corpus, unit), encoding="utf-8"))
    for f in unit_forms(t, unit):
        mf = tab["forms"].get(f["id"], {})
        print(f"\n=== {f['id']}  {f['title']}  ->  {mf.get('title')}\n    skill: {f['skill']}  ->  {mf.get('skill')}")
        for v in f["variants"][:n]:
            m = mf.get("variants", {}).get(v["id"], {})
            print(f"  [{v['id']}]")
            print(f"    EN {v['statement']}\n    MN {m.get('statement')}")
            if any(strip_math(o).strip() for o in v["options"]):
                print(f"    EN opts {v['options']}\n    MN opts {m.get('options')}")
            print(f"    EN expl {v['explanation']}\n    MN expl {m.get('explanation')}")


def cmd_status():
    for fn in sorted(os.listdir(SRC)):
        corpus = fn[:-5]
        t = load_src(corpus)
        have = [u["id"] for u in t["units"] if os.path.exists(table_path(corpus, u["id"]))]
        if have:
            print(f"{corpus:18} {len(have)}/{len(t['units'])} unit tables")


def main():
    a = sys.argv[1:]
    if a[:1] == ["extract"] and len(a) == 3:
        return cmd_extract(a[1], a[2]) or 0
    if a[:1] == ["check"] and len(a) == 3:
        _, errs, warns = check_unit(a[1], a[2])
        print(("FAIL" if errs else "OK"), f"{a[1]}/{a[2]}: {len(errs)} errors, {len(warns)} warnings")
        return 1 if errs else 0
    if a[:1] == ["assemble"] and len(a) == 2:
        return cmd_assemble(a[1])
    if a[:1] == ["show"] and len(a) in (3, 4):
        return cmd_show(a[1], a[2], int(a[3]) if len(a) == 4 else 3) or 0
    if a[:1] == ["register"]:
        return cmd_register() or 0
    if a[:1] == ["status"]:
        return cmd_status() or 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
