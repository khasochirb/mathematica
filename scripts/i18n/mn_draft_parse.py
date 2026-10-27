#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse a Mongolian draft (memory/mn-drafts/<corpus>-<slug>.md) into
{json path: Mongolian string}, the input mn_slots.py's table is built from.

    python3 scripts/i18n/mn_draft_parse.py <corpus> <slug> [out.json]

Written for the draft format of memory/mn-drafts/9-equations-and-formulas.md
(the pilot, 27 Oct 2026). Drafts by different writers vary in small ways; a
helper that meets a variation copies this file to its scratch directory and
adapts the copy. Every structural count is asserted against the English, so
a format mismatch stops loudly instead of shifting strings by one slot.
"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CORPUS, SLUG = sys.argv[1], sys.argv[2]
OUT = sys.argv[3] if len(sys.argv) > 3 else os.path.join(ROOT, "i18n-work", f"{CORPUS}__{SLUG}.draft.json")
draft = open(os.path.join(ROOT, "memory", "mn-drafts", f"{CORPUS}-{SLUG}.md"), encoding="utf-8").read()
en = json.load(open(os.path.join(ROOT, "data", "genmath", CORPUS, f"{SLUG}.json"), encoding="utf-8"))
out = {}

def para(lines):
    return " ".join(l.strip() for l in lines if l.strip()).strip()

def split_sections(block):
    """split block into {name: [lines]} keyed by '**name**' header lines"""
    secs, cur = {}, None
    for l in block.split("\n"):
        m = re.fullmatch(r"\*\*(\w+)\*\*\s*", l.strip())
        if m and m.group(1) in {"concreteComparison","objective","concept","keyIdea","facts","workedExamples","commonMistakes","tryIt"}:
            cur = m.group(1); secs[cur] = []; continue
        if l.startswith("### Interactive"):
            cur = "interactive"; secs[cur] = []; continue
        if cur: secs[cur].append(l)
    return secs

def items(lines, start_re):
    res, cur = [], None
    for l in lines:
        if re.match(start_re, l):
            if cur is not None: res.append(cur)
            cur = [re.sub(start_re, "", l, count=1)]
        elif cur is not None and (l.startswith("---") or l.startswith("#")):
            res.append(cur); cur = None
        elif cur is not None and l.strip() and not l.startswith(">"):
            cur.append(l)
        elif cur is not None and not l.strip():
            pass
    if cur is not None: res.append(cur)
    return [para(x) for x in res]

def table_rows(lines):
    rows = []
    for l in lines:
        if l.startswith("|") and not l.startswith("|---") and not l.startswith("| title") and not l.startswith("| #"):
            # " | " separates cells; a literal pipe inside a cell is written \| (README).
            cells = [c.strip().replace("\\|", "|") for c in l.strip().strip("|").split(" | ")]
            rows.append(cells)
    return rows

def unbt(s):
    s = s.strip()
    return s[1:-1] if s.startswith("`") and s.endswith("`") else s

# topic
out["title"] = re.search(r"\*\*TITLE:\*\* (.+)", draft).group(1).strip()
m = re.search(r"\*\*BLURB:\*\* ([\s\S]+?)\n\n", draft)
out["blurb"] = para(m.group(1).split("\n"))

lesson_blocks = re.split(r"\n## Lesson \d+ — ", draft)[1:]
lesson_blocks[-1] = re.split(r"\n## (?:PRACTICE|Practice)", lesson_blocks[-1])[0]
assert len(lesson_blocks) == len(en["lessons"])

def id_items(lines, field):
    """- `id` — **statement:** ... **solution:** ...  (or no statement label)"""
    res = {}
    for it in items(lines, r"^- `"):
        mid = re.match(r"([\w-]+)` — (.*)", it)
        pid, rest = mid.group(1), mid.group(2)
        rest = re.sub(r"^\*\*statement:\*\* ", "", rest)
        st, sol = rest.split(" **solution:** ")
        res[pid] = (st.strip(), sol.strip())
    return res

for li, blk in enumerate(lesson_blocks):
    E = en["lessons"][li]; P = f"lessons/{li}"
    head = blk.split("\n")[0]
    out[f"{P}/title"] = re.match(r"(.+?) \(`", head).group(1)
    assert f"`{E['slug']}`" in head, head
    S = split_sections(blk)
    for k in ("concreteComparison", "objective", "keyIdea"):
        out[f"{P}/{k}"] = para(S[k])
    con = items(S["concept"], r"^\d+\. ")
    assert len(con) == len(E["concept"]), (li, len(con))
    for i, c in enumerate(con): out[f"{P}/concept/{i}"] = c
    fr = table_rows(S["facts"]); assert len(fr) == len(E["facts"])
    for i, (t, lx, ex) in enumerate(fr):
        out[f"{P}/facts/{i}/title"] = t; out[f"{P}/facts/{i}/latex"] = unbt(lx); out[f"{P}/facts/{i}/explanation"] = ex
    for field in ("workedExamples", "tryIt"):
        d = id_items(S[field], field)
        assert [x["id"] for x in E[field]] == list(d), (li, field, list(d))
        for i, x in enumerate(E[field]):
            out[f"{P}/{field}/{i}/statement"], out[f"{P}/{field}/{i}/solution"] = d[x["id"]]
    cm = items(S["commonMistakes"], r"^- \*\*text:\*\* ")
    assert len(cm) == len(E["commonMistakes"])
    for i, c in enumerate(cm):
        t, cor = c.split(" **correction:** ")
        out[f"{P}/commonMistakes/{i}/text"] = t; out[f"{P}/commonMistakes/{i}/correction"] = cor
    rows = table_rows(S["interactive"])
    steps = E["interactive"]["steps"]; assert len(rows) == len(steps)
    for (num, kind, cell), st in zip(rows, steps):
        si = int(num); assert kind == st["kind"], (li, si, kind)
        Q = f"{P}/interactive/steps/{si}"
        parts = cell.split("<br>")
        m = re.fullmatch(r"\*\*eyebrow\*\* (.+?) · \*\*title\*\* (.+)", parts[0])
        out[f"{Q}/eyebrow"], out[f"{Q}/title"] = m.group(1), m.group(2)
        for part in parts[1:]:
            fm = re.match(r"\*\*(\w+)\*\* ?(.*)", part)
            f, val = fm.group(1), fm.group(2)
            if f == "config": continue
            if f in ("teach", "body", "intro", "prompt", "explanation"):
                out[f"{Q}/{f}"] = val
            elif f in ("beats", "points"):
                vs = val.split(" · "); assert len(vs) == len(st[f]), (li, si, f, len(vs))
                for i, v in enumerate(vs): out[f"{Q}/{f}/{i}"] = v
            elif f == "options":
                opts, ci = re.fullmatch(r"(.+) — \*\*correctIndex (\d)\*\*", val).groups()
                vs = re.findall(r"`([^`]*)`", opts); assert len(vs) == len(st["options"]) and int(ci) == st["correctIndex"]
                for i, v in enumerate(vs): out[f"{Q}/options/{i}"] = v
            elif re.fullmatch(r"ex\d", f):
                k = int(f[2:]) - 1; ex = st["examples"][k]
                body, ans = val.split(" · **хариу** ")
                segs = body.split(" · алхам: ")
                assert len(segs) - 1 == len(ex["steps"]), (li, si, f)
                out[f"{Q}/examples/{k}/prompt"] = segs[0]
                for i, s in enumerate(segs[1:]): out[f"{Q}/examples/{k}/steps/{i}"] = s
                out[f"{Q}/examples/{k}/answer"] = ans
            elif re.fullmatch(r"p\d", f):
                k = int(f[1:]) - 1; pr = st["problems"][k]
                mm = re.fullmatch(r"(.+?) — \*\*choices\*\* (.+?) — \*\*answerIndex (\d)\*\* — (.+)", val)
                pq, ch, ai, ex = mm.groups()
                vs = re.findall(r"`([^`]*)`", ch); assert len(vs) == len(pr["options"]) and int(ai) == pr["correctIndex"]
                out[f"{Q}/problems/{k}/prompt"] = pq
                for i, v in enumerate(vs): out[f"{Q}/problems/{k}/options/{i}"] = v
                out[f"{Q}/problems/{k}/explanation"] = ex
            else:
                raise SystemExit(f"unknown field {f} at {Q}")

tail = re.split(r"\n## (?:PRACTICE|Practice)", draft, maxsplit=1)[1]
pr_block, ty_block = re.split(r"\n## (?:TEST YOURSELF|Test yourself)", tail, maxsplit=1)
ty_block = re.split(r"\n## Notes", ty_block)[0]
for field, blk in (("practice", pr_block), ("testYourself", ty_block)):
    d = id_items(blk.split("\n"), field)
    assert [x["id"] for x in en[field]] == list(d), field
    for i, x in enumerate(en[field]):
        out[f"{field}/{i}/statement"], out[f"{field}/{i}/solution"] = d[x["id"]]

os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "draft values")
