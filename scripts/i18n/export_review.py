#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Export every English / Mongolian text pair for outside review.

    npx tsx --tsconfig tsconfig.json scripts/i18n/dump-ts-pairs.ts > <dir>/ts-pairs.json
    python3 scripts/i18n/export_review.py <dir>

Writes into <dir>:
  mongolian-review.xlsx   one sheet per area (Lessons, Problem bank, Placement,
                          Exams, UI strings), frozen header, filterable
  csv/<area>.csv          the same rows as UTF-8 CSV (with BOM, opens in Excel)

Every row: area, course, unit/topic, item, field, English, Mongolian, plus a
stable `key` (corpus + JSON path or id) so a reviewer's comment can be traced
back to the exact string. Read-only: nothing in the repo is changed.
"""
import csv
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "scripts", "i18n"))
import mn_slots  # noqa: E402

COLS = ["area", "course", "unit / topic", "item", "field", "english", "mongolian", "key"]


def get_path(obj, path):
    cur = obj
    for p in path.split("/"):
        cur = cur[int(p)] if isinstance(cur, list) else cur[p]
    return cur


def lessons():
    rows = []
    for table in sorted(glob.glob(os.path.join(ROOT, "i18n", "mn-tables", "*", "*.mn.json"))):
        corpus = os.path.basename(os.path.dirname(table))
        slug = os.path.basename(table)[: -len(".mn.json")]
        src, _, out = mn_slots.paths(corpus, slug)
        if not (os.path.exists(src) and os.path.exists(out)):
            continue
        en = json.load(open(src, encoding="utf-8"))
        mn = json.load(open(out, encoding="utf-8"))
        lesson_titles = [l.get("title", "") for l in en.get("lessons", [])]
        for path, e in mn_slots.slots(en):
            try:
                m = get_path(mn, path)
            except (KeyError, IndexError, ValueError, TypeError):
                m = ""
            parts = path.split("/")
            if parts[0] == "lessons":
                li = int(parts[1])
                item = f"Lesson {li + 1}: {lesson_titles[li]}" if li < len(lesson_titles) else f"Lesson {li + 1}"
                field = "/".join(parts[2:])
            else:
                item, field = parts[0], "/".join(parts[1:]) or parts[0]
            rows.append(["Lessons", corpus, en.get("title", slug), item, field, e, m if isinstance(m, str) else json.dumps(m, ensure_ascii=False), f"{corpus}/{slug}#{path}"])
    return rows


def bank():
    rows = []
    for mnp in sorted(glob.glob(os.path.join(ROOT, "data", "problembank-mn", "*.json"))):
        corpus = os.path.basename(mnp)[:-5]
        en = json.load(open(os.path.join(ROOT, "data", "problembank", f"{corpus}.json"), encoding="utf-8"))
        mn = json.load(open(mnp, encoding="utf-8"))
        def add(unit, item, field, e, m, key):
            rows.append(["Problem bank", corpus, unit, item, field, e, m, key])
        add("", "subject", "title", en.get("title", ""), mn.get("title", ""), f"{corpus}#title")
        add("", "subject", "blurb", en.get("blurb", ""), mn.get("blurb", ""), f"{corpus}#blurb")
        mnu = {u["id"]: u for u in mn["units"]}
        utitle = {u["id"]: u["title"] for u in en["units"]}
        for u in en["units"]:
            mu = mnu.get(u["id"], {})
            add(u["title"], "unit", "title", u["title"], mu.get("title", ""), f"{corpus}/{u['id']}#title")
            if u.get("blurb"):
                add(u["title"], "unit", "blurb", u["blurb"], mu.get("blurb", ""), f"{corpus}/{u['id']}#blurb")
        mnf = {(f["unit"], f["id"]): f for f in mn["forms"]}
        for f in en["forms"]:
            mf = mnf.get((f["unit"], f["id"]))
            if not mf:
                continue
            ut = utitle.get(f["unit"], f["unit"])
            fk = f"{corpus}/{f['unit']}/{f['id']}"
            add(ut, f"type: {f['title']}", "type title", f["title"], mf["title"], f"{fk}#title")
            add(ut, f"type: {f['title']}", "key idea", f.get("skill", ""), mf.get("skill", ""), f"{fk}#skill")
            for i, line in enumerate(f.get("method") or []):
                add(ut, f"type: {f['title']}", f"method {i + 1}", line, (mf.get("method") or [""] * 99)[i], f"{fk}#method/{i}")
            mv = {v["id"]: v for v in mf["variants"]}
            for v in f["variants"]:
                m = mv.get(v["id"])
                if not m:
                    continue
                vk = f"{fk}/{v['id']}"
                it = v["id"]
                add(ut, it, "statement", v["statement"], m["statement"], f"{vk}#statement")
                for i, (eo, mo) in enumerate(zip(v["options"], m["options"])):
                    tag = " (correct)" if i == v["correctIndex"] else ""
                    add(ut, it, f"option {i + 1}{tag}", eo, mo, f"{vk}#options/{i}")
                add(ut, it, "explanation", v["explanation"], m["explanation"], f"{vk}#explanation")
                for i, h in enumerate(v.get("hints") or []):
                    add(ut, it, f"hint {i + 1}", h, (m.get("hints") or [""] * 9)[i], f"{vk}#hints/{i}")
                for i, st in enumerate(v.get("steps") or []):
                    ms = (m.get("steps") or [{}] * 20)[i]
                    add(ut, it, f"step {i + 1}", st.get("do", ""), ms.get("do", ""), f"{vk}#steps/{i}/do")
                    if st.get("why"):
                        add(ut, it, f"step {i + 1} why", st["why"], ms.get("why", ""), f"{vk}#steps/{i}/why")
                for i, w in enumerate(v.get("whyWrong") or []):
                    if w is None:
                        continue
                    add(ut, it, f"why option {i + 1} is wrong", w, (m.get("whyWrong") or [None] * 9)[i] or "", f"{vk}#whyWrong/{i}")
    return rows


def exams():
    rows = []
    for p in sorted(glob.glob(os.path.join(ROOT, "data", "course-exams-mn", "*.json"))):
        eid = os.path.basename(p)[:-5]
        en = json.load(open(os.path.join(ROOT, "data", "course-exams", f"{eid}.json"), encoding="utf-8"))["meta"]
        mn = json.load(open(p, encoding="utf-8"))["meta"]
        for k in ("courseTitle", "label", "intro"):
            rows.append(["Exams", en["course"], eid, "paper", k, en[k], mn[k], f"exam/{eid}#{k}"])
    return rows


def placement(dump):
    return [["Placement", f"grade placement {r['bank']}", r["topic"], r["id"], r["field"], r["en"], r["mn"],
             f"placement/{r['bank']}/{r['id']}#{r['field']}"] for r in dump["placement"]]


# UI strings written inline in components: `mn ? "…" : "…"`, `<T en="…" mn="…">`.
TERNARY = re.compile(r'\bmn\s*\?\s*(["`])((?:(?!\1).){1,600}?)\1\s*:\s*(["`])((?:(?!\3).){1,600}?)\3', re.S)
TCOMP = re.compile(r'<T\s+en=(["{`])(.+?)["}`]\s+mn=(["{`])(.+?)["}`]', re.S)


def ui(dump):
    rows = [["UI strings", "site dictionary", "", r["en"], "approved " + r["approved"] if r["approved"] else "",
             r["en"], r["mn"], f"chrome#{r['en']}"] for r in dump["chrome"]]
    seen = set()
    for p in sorted(glob.glob(os.path.join(ROOT, "app", "**", "*.tsx"), recursive=True)
                    + glob.glob(os.path.join(ROOT, "components", "**", "*.tsx"), recursive=True)):
        rel = os.path.relpath(p, ROOT)
        src = open(p, encoding="utf-8").read()
        for m in TERNARY.finditer(src):
            mn_s, en_s = m.group(2), m.group(4)
            if not re.search(r"[А-Яа-яӨөҮү]", mn_s):
                continue
            line = src.count("\n", 0, m.start()) + 1
            k = (rel, en_s, mn_s)
            if k in seen:
                continue
            seen.add(k)
            rows.append(["UI strings", "page text", rel, f"line {line}", "", " ".join(en_s.split()), " ".join(mn_s.split()), f"{rel}:{line}"])
        for m in TCOMP.finditer(src):
            line = src.count("\n", 0, m.start()) + 1
            rows.append(["UI strings", "page text", rel, f"line {line}", "", m.group(2), m.group(4), f"{rel}:{line}"])
    return rows


MATHSEG = re.compile(r"\$\$[^$]+\$\$|\$[^$]+\$")


def has_words(s):
    """True when a reader sees words, not just maths or numbers."""
    return bool(re.search(r"[A-Za-zА-Яа-яӨөҮү]{2,}", MATHSEG.sub(" ", (s or "").replace("\\$", ""))))


def main():
    out = sys.argv[1]
    dump = json.load(open(os.path.join(out, "ts-pairs.json"), encoding="utf-8"))
    sheets = {
        "Lessons": lessons(),
        "Problem bank": bank(),
        "Placement": placement(dump),
        "Exams": exams(),
        "UI strings": ui(dump),
    }
    # Maths-only strings ($-5$, $x = 3$) have nothing to translate and are
    # identical by design; listing 100k of them buries the text to review.
    for name in sheets:
        sheets[name] = [r for r in sheets[name]
                        if (has_words(r[5]) or has_words(r[6])) and not r[4].endswith("latex")]
    os.makedirs(os.path.join(out, "csv"), exist_ok=True)
    for name, rows in sheets.items():
        fn = os.path.join(out, "csv", name.lower().replace(" ", "-") + ".csv")
        with open(fn, "w", encoding="utf-8-sig", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(COLS)
            w.writerows(rows)
        print(f"{name}: {len(rows)} rows -> {os.path.relpath(fn, out)}")
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Alignment, Font
    except ImportError:
        print("openpyxl not installed: CSVs only")
        return
    wb = Workbook(write_only=False)
    wb.remove(wb.active)
    widths = [12, 16, 28, 28, 18, 60, 60, 40]
    for name, rows in sheets.items():
        ws = wb.create_sheet(name)
        ws.append(COLS)
        for c in ws[1]:
            c.font = Font(bold=True)
        for r in rows:
            ws.append([x[:32000] if isinstance(x, str) else x for x in r])
        for i, wdt in enumerate(widths):
            ws.column_dimensions[chr(65 + i)].width = wdt
        for col in ("F", "G"):
            for c in ws[col][1:2000]:
                c.alignment = Alignment(wrap_text=True, vertical="top")
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = ws.dimensions
    dest = os.path.join(out, "mongolian-review.xlsx")
    wb.save(dest)
    print("wrote", dest)


if __name__ == "__main__":
    main()
