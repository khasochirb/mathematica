#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the two authoring briefs for one topic.

    python3 scripts/i18n/mn_brief.py <corpus> <slug>
    python3 scripts/i18n/mn_brief.py --queue N     # the next N in exam-weight order

Writes memory/mn-briefs/<corpus>-<slug>/{teacher,build}.md

WHY TWO DOCUMENTS. docs/MONGOLIAN.md: "a teacher-facing document (what to teach,
the lessons, locked terms, register, notation rules that affect writing) and a
Build-facing one (JSON skeleton, ids, check[], gates, commit format). A maths
teacher will not write sympy assertions — you write those from the examples they
give you."

The first sample brief mixed both and was therefore wrong for both readers: it
asked a maths teacher to care about `problemId` stability, and buried the
pedagogy under JSON.

WHAT IS MECHANICAL AND WHAT IS NOT. This extracts the PEDAGOGICAL SPINE from the
English source — objectives, key ideas, the mistakes each lesson warns about,
the shape of each worked example — and lays it out as source material. It does
not write the brief's argument for what matters most; that is a judgement call
per topic, and the generated file marks the place for it explicitly rather than
pretending a template made it.

THE ENGLISH IS NEVER QUOTED AS PROSE TO RENDER. Objectives and key ideas appear
under "what the student must end up able to do", phrased as outcomes, because a
teacher handed English sentences will translate them — which is the one thing
this programme exists to prevent.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "memory", "mn-briefs")

# Section headings the shipped mirrors already use. Matching them is what makes
# the site read as one product rather than a series of separate translations.
LOCKED_SECTIONS = [
    ("Worked examples", "Бодсон жишээнүүд"),
    ("Try it yourself", "Өөрөө туршиж үз"),
    ("Quick check", "Түргэн шалгалт"),
    ("Play with it", "Тоглож үз"),
    ("Fun fact", "Сонирхолтой баримт"),
    ("Recap", "Эргэн дүгнэлт"),
    ("What you learned", "Юу сурснаа эргэн харъя"),
]


def load_theses():
    """The judgement half of each brief, kept as data so a regeneration cannot
    destroy it — the same reason MN mirrors are never hand-edited."""
    p = os.path.join(ROOT, "data", "i18n", "mn-brief-theses.json")
    if not os.path.exists(p):
        return {}
    return json.load(open(p, encoding="utf8")).get("theses", {})


def load_glossary():
    p = os.path.join(ROOT, "data", "i18n", "mn-glossary-proposal.json")
    if not os.path.exists(p):
        return {}
    return {t["en"].lower(): t for t in json.load(open(p, encoding="utf8"))["terms"]}


def salient_text(topic: dict) -> str:
    """The topic's HIGH-SIGNAL text: what it is about, not every word in it.

    Matching the glossary against the whole JSON blob puts "area", "mean" and
    "geometry" into a brief for quadratic equations, because those words appear
    once each somewhere in a word problem. A brief whose vocabulary list is
    mostly noise is a list the writer stops reading.

    Titles, objectives, key ideas and fact headings are what the topic is
    ABOUT — that is the vocabulary its writer will actually reach for.
    """
    bits = [topic.get("title", ""), topic.get("blurb", "")]
    for l in topic.get("lessons", []):
        bits += [l.get("title", ""), l.get("objective", ""), l.get("keyIdea", "")]
        for f in l.get("facts", []) or []:
            bits.append(f.get("title", ""))
    return " ".join(bits).lower()


def terms_in(topic: dict, glossary: dict):
    """Glossary terms this topic is actually about, ranked by centrality."""
    text = salient_text(topic)
    found = []
    for en, t in glossary.items():
        if len(en) < 4:
            continue
        if re.search(r"\b" + re.escape(en) + r"(s|es|ing)?\b", text):
            found.append(t)
    found.sort(key=lambda t: -(t.get("rank", 0) * 4 + min(t.get("uses", 0), 300)))
    return found


def study_map_hits(slug: str):
    """ЭШ skills whose study destination is this topic.

    NOTE this reads lib/skill-study-map.ts, which is keyed by the QUESTION-BANK
    taxonomy (underscore ids like `linear_inequality`), NOT by the 184-node
    skill graph in 011_seed_esh_graph.sql (hyphen ids). Only 7 of 51 keys
    reconcile between them. So a hit here tells the writer who arrives at this
    topic; it does not connect to the graph's exam weights.
    """
    src = open(os.path.join(ROOT, "lib", "skill-study-map.ts"), encoding="utf8").read()
    out = []
    for m in re.finditer(r"(\w+):\s*\{\s*primary:\s*\{\s*label:\s*\"([^\"]*)\",\s*href:\s*\"([^\"]*)\"", src):
        if m.group(3).rstrip("/").endswith("/" + slug):
            out.append((m.group(1), m.group(2), "primary"))
    for m in re.finditer(r"(\w+):\s*\{[^}]*links:\s*\[([^\]]*)\]", src, re.S):
        if "/" + slug in m.group(2):
            lbl = re.search(r'label:\s*"([^"]*)"', m.group(2))
            out.append((m.group(1), lbl.group(1) if lbl else "", "prerequisite"))
    return out


def teacher_brief(corpus, topic, glossary, theses=None):
    slug = topic["slug"]
    L = topic["lessons"]
    allg = terms_in(topic, glossary)
    poly = [t for t in allg if t.get("polysemous")]
    g = poly + [t for t in allg if not t.get("polysemous")][:14]
    hits = study_map_hits(slug)

    out = []
    w = out.append
    w(f"# MN authoring brief — {topic.get('title', slug)}")
    w("")
    w(f"**Topic** `{corpus}/{slug}` · **{len(L)} lessons** · "
      f"{sum(len(l.get('workedExamples', [])) for l in L)} worked examples · "
      f"{len(topic.get('practice', []))} practice · {len(topic.get('testYourself', []))} test-yourself")
    w("")
    w("---")
    w("")
    w("## You are not translating. You are teaching.")
    w("")
    w("Do not open the English topic and render it sentence by sentence — that")
    w("produces the stiff textbook Mongolian this whole programme exists to avoid.")
    w("Read this brief, decide how **you** would teach these lessons to a Mongolian")
    w("student, and write that.")
    w("")
    w("A different sentence count is expected. Different worked examples are")
    w("allowed. A different order *inside* a lesson is yours to choose. A different")
    w("explanation, a different analogy, a different joke — that is the point.")
    w("")
    w("What you may not change is in the Build brief, and Build enforces it. You do")
    w("not need to read that document.")
    w("")
    w("---")
    w("")
    w("## What this topic must teach")
    w("")
    th = (theses or {}).get(f"{corpus}/{slug}")
    if th:
        w("A student finishes this topic holding these ideas. Everything else in the")
        w("brief serves them.")
        w("")
        for i, c in enumerate(th.get("carries", []), 1):
            w(f"{i}. {c}")
            w("")
        if th.get("breaks"):
            w(f"**The error to design against:** {th['breaks']}")
            w("")
        w("If your Mongolian version lands those and a student can do the practice")
        w("set, the topic is right — however you got there.")
        w("")
    else:
        w("> **← the argument for what matters most in this topic is not written yet.**")
        w("> Two or three ideas that carry the topic, and the place students reliably")
        w("> break, go in `data/i18n/mn-brief-theses.json` under the key")
        w(f"> `{corpus}/{slug}`. That is a judgement call per topic and a template")
        w("> cannot fake it — the outcomes below are the raw material for it, not a")
        w("> substitute.")
        w("")
    w("Each lesson, and what the student must end up able to do:")
    w("")
    for i, l in enumerate(L, 1):
        w(f"### {i}. `{l['slug']}`")
        w("")
        if l.get("objective"):
            w(f"**Able to:** {l['objective']}")
            w("")
        if l.get("keyIdea"):
            w(f"**The idea that carries it:** {l['keyIdea']}")
            w("")
        cm = l.get("commonMistakes") or []
        if cm:
            w("**Where students break** — the English warns about these, and they are")
            w("worth keeping however you phrase them:")
            for m in cm:
                t = m.get("text") or ""
                w(f"- {t}")
            w("")
        we = l.get("workedExamples") or []
        if we:
            w(f"**{len(we)} worked examples.** Yours to choose — different numbers, a")
            w("different context, a Mongolian setting instead of an American one. What")
            w("each must *do* is fixed:")
            for e in we:
                w(f"- `{e.get('id')}` — {(e.get('statement') or '')[:150]}")
            w("")
        ti = l.get("tryIt") or []
        if ti:
            w(f"**{len(ti)} try-it problems**, same freedom and same condition.")
            w("")
    w("---")
    w("")
    w("## What you owe for every example you change")
    w("")
    w("A worked example or try-it problem with different numbers needs a new")
    w("**check** — a line of maths that says what must be true, so we can verify it")
    w("mechanically without a second person re-solving it.")
    w("")
    w("**You do not write these.** Write the example and its answer in plain")
    w("Mongolian, and Build turns it into the assertion. If an example's answer")
    w("cannot be stated exactly, the example is not ready.")
    w("")
    w("**Practice and test-yourself problems are different: do not change their")
    w("numbers.** Those are graded against a stored answer key and every student's")
    w("history is keyed to them. Rewrite the *wording* freely; leave the maths.")
    w("")
    w("---")
    w("")
    w("## Money")
    w("")
    w("Worked examples and try-it problems use **₮ (tögrög)** with realistic")
    w("Mongolian amounts. Rewrite the numbers to suit; Build rewrites the check.")
    w("")
    w("Practice and test-yourself keep their original currency and figures,")
    w("because they are graded.")
    w("")
    w("---")
    w("")
    w("## Terms that are not yours to choose")
    w("")
    if g:
        w("Fixed by ministry order А/492 or by Mongolian already shipped on the site.")
        w("Using a different word for one of these is the fastest way to make the site")
        w("feel like two different products.")
        w("")
        w("| English | Use | Why |")
        w("|---|---|---|")
        for t in g:
            why = {"ministry": "ministry standard", "glossary": "glossary",
                   "shipped": "already on the site", "proposal": "**proposed — tell us if it is wrong**"}[t["provenance"]]
            w(f"| {t['en']} | **{t['mn']}** | {why} |")
        w("")
        if poly:
            w("### Careful — English uses one word where Mongolian uses two")
            w("")
            w("These are the ones that go wrong silently. The word above is the sense")
            w("this topic most likely means; check it against what you are actually")
            w("writing, and say so if the topic needs the other one.")
            w("")
            for t in poly:
                w(f"**{t['en']}** — proposed **{t['mn']}**")
                w("")
                w(f"> {(t.get('note') or '').strip()}")
                w("")
    else:
        w("_No glossary terms matched this topic — check `data/i18n/mn-glossary-proposal.json` by hand._")
        w("")
    w("**Section headings** are fixed too, because the shipped lessons already use")
    w("them and a student should meet the same words in every lesson:")
    w("")
    w(" · ".join(f"**{mn}**" for _, mn in LOCKED_SECTIONS))
    w("")
    w("Introducing a term that is not here? Tell us — it goes in the glossary so the")
    w("next topic uses the same word.")
    w("")
    w("---")
    w("")
    w("## What to hand back")
    w("")
    w("Plain text or a document — **not** JSON, and nothing needs to look like")
    w("code. One block per lesson, in the order above. Use the lesson\u2019s slug as")
    w("its heading so Build can match it up; everything else is prose.")
    w("")
    w("```")
    for l in L[:2]:
        w(f"## {l['slug']}")
        w("")
        w("TITLE:      <the lesson title in Mongolian>")
        w("OBJECTIVE:  <what the student can do after it, one sentence>")
        w("KEY IDEA:   <the one sentence that carries the lesson>")
        w("")
        w("TEACHING:")
        w("<your explanation. As many paragraphs as it takes — more than the")
        w("English, fewer, in a different order. Blank line between paragraphs.>")
        w("")
        w("MISTAKES:")
        w("- <a mistake students make, and why>")
        w("")
        for e in (l.get("workedExamples") or [])[:1]:
            w(f"WORKED {e.get('id')}:")
            w("  PROBLEM:  <the question, your numbers>")
            w("  WORKING:  <how it is solved, step by step>")
            w("  ANSWER:   <the answer, exactly>")
            w("")
        for e in (l.get("tryIt") or [])[:1]:
            w(f"TRY {e.get('id')}:")
            w("  PROBLEM:  <the question>")
            w("  ANSWER:   <the answer, exactly>")
            w("")
    w("...and so on for the remaining lessons.")
    w("```")
    w("")
    w("**Keep the ids** (`" + (L[0].get("workedExamples") or [{}])[0].get("id","...") + "` and so on) exactly")
    w("as they appear. They are how the site connects your example to the student")
    w("who answered it; the numbers inside are yours to change, the id is not.")
    w("")
    w("**The ANSWER line matters more than it looks.** Build turns it into a check")
    w("the computer runs, so it has to be exact \u2014 write $\\frac{3}{4}$ or")
    w("$2\\sqrt{5}$ rather than 0.75 or 4.47, unless the answer really is a")
    w("rounded decimal, in which case say so.")
    w("")
    w("For the practice and test-yourself sets at the end of the topic, hand back")
    w("**only the wording** \u2014 their numbers and answers stay as they are.")
    w("")
    w("---")
    w("")
    w("## How it should sound")
    w("")
    w("**«та», formal.** A student on this product is a customer, and «чи» is not")
    w("suitable for one. Formal is not the same as stiff — the English has jokes and")
    w("energy, and that should survive. Do not flatten it into textbook prose.")
    w("")
    w("Quotes take «...». Proper names take their standard Mongolian forms. Product")
    w("names and symbols stay Latin.")
    w("")
    w("> Note if you have seen earlier material: grades 6 and 7 are written in «чи»,")
    w("> which is now the wrong register. Do not copy their tone.")
    w("")
    w("---")
    w("")
    w("## Writing maths")
    w("")
    w("Only the rules that change what you type:")
    w("")
    w("1. **Do not put Mongolian words inside a formula.** Write the formula in")
    w("   symbols and the words outside it. (If a word truly must sit inside one,")
    w("   mark it and Build will wrap it correctly.)")
    w("2. **Letters stay Latin** — `x`, `h`, point names, function names — even in")
    w("   Mongolian prose. Gloss one on first use if it helps.")
    w("3. **Bold is `**like this**`.** Single asterisks do not work and will appear")
    w("   on screen as asterisks.")
    w("4. **Units:** см, кг, мл read fine in a sentence.")
    if hits:
        w("")
        w("---")
        w("")
        w("## Who arrives here")
        w("")
        w("The site sends students to this topic when the analytics find a weakness in:")
        w("")
        for sid, label, kind in hits:
            w(f"- **{label or sid}** ({kind})")
        w("")
        w("So write for a student meeting this for the first time *and* for an exam")
        w("candidate sent back to repair a gap.")
    w("")
    return "\n".join(out) + "\n"


def build_brief(corpus, topic):
    slug = topic["slug"]
    L = topic["lessons"]
    out = []
    w = out.append
    w(f"# Build brief — `{corpus}/{slug}`")
    w("")
    w("The machine half. The writer never reads this.")
    w("")
    w(f"**Source** `data/genmath/{corpus}/{slug}.json` → "
      f"**write** `data/genmath/{corpus}-mn/{slug}.json`")
    w("")
    w("---")
    w("")
    w("## The skeleton — enforced by `mn_skeleton.py`")
    w("")
    w(f"- topic slug `{slug}`, status `{topic.get('status')}` — unchanged")
    w(f"- **{len(L)} lessons**, these slugs, this order:")
    for i, l in enumerate(L, 1):
        w(f"  {i}. `{l['slug']}`")
    w("")
    w("Per lesson, ids and counts that must survive verbatim:")
    w("")
    w("| lesson | workedExamples | tryIt | step kinds | tapQuestion options |")
    w("|---|---|---|---|---|")
    for l in L:
        steps = l.get("interactive", {}).get("steps", []) or []
        we = ", ".join(f"`{e.get('id')}`" for e in l.get("workedExamples", []) or []) or "—"
        ti = ", ".join(f"`{e.get('id')}`" for e in l.get("tryIt", []) or []) or "—"
        kinds = len(steps)
        opts = [len(s.get("options", [])) for s in steps if s.get("kind") == "tapQuestion"]
        w(f"| `{l['slug']}` | {we} | {ti} | {kinds} steps, sequence fixed | {opts or '—'} |")
    w("")
    w(f"- `practice`: {len(topic.get('practice', []))} items — "
      f"{', '.join('`' + (p.get('id') or '') + '`' for p in topic.get('practice', []))}")
    w(f"- `testYourself`: {len(topic.get('testYourself', []))} items — "
      f"{', '.join('`' + (p.get('id') or '') + '`' for p in topic.get('testYourself', []))}")
    w("")
    w("**Ids are load-bearing twice over.** Interactive steps of kind `worked` and")
    w("`tryIt` carry no content — they reference their problem by `problemId`")
    w("(`lib/genmath-interactive.ts:1284`), and every student attempt is recorded")
    w("against that id (`lib/api.ts:174`). A rewritten example may change its")
    w("numbers entirely; changing its **id** breaks the widget and detaches the")
    w("student's history from the problem it belongs to.")
    w("")
    w("**Step `kind` sequences are design, not language.** Each kind is a different")
    w("React component; reordering them changes what is on screen.")
    w("")
    w("---")
    w("")
    w("## check[] — Build writes these, not the writer")
    w("")
    w("The writer supplies each rewritten example and its answer in Mongolian. Build")
    w("turns that into sympy assertions, one per numeric claim the solution makes.")
    w("Exact objects only — `Rational(1,3)` not `0.333`, `sqrt(2)` not `1.414`. If")
    w("the shipped answer is rounded, assert the rounding.")
    w("")
    w("Every item that carries a `check[]` in the English **must** carry one in the")
    w("Mongolian; `mn_skeleton.py` fails on a lost one. Contents are never compared —")
    w("a rewritten example is *required* to bring new assertions.")
    w("")
    w("**Currency:** worked examples and tryIt move to ₮ and the check is rewritten")
    w("to match. `practice` and `testYourself` keep their original figures — they are")
    w("graded against a stored key.")
    w("")
    w("---")
    w("")
    w("## Order of operations")
    w("")
    w("1. Writer returns Mongolian prose plus each changed example with its answer.")
    w("2. Build writes the `check[]` blocks and assembles the JSON.")
    w("3. **Khas reads the Mongolian.** The gates check maths and glossary; nothing")
    w("   checks whether the prose is any good. This step is not optional and comes")
    w("   *before* anything is applied.")
    w("4. Apply, then gate:")
    w("")
    w("```")
    w(f"python3 scripts/i18n/mn_skeleton.py {corpus} {slug}")
    w("npm run verify:genmath")
    w("npm run verify:mn-terms")
    w("npx tsc --noEmit && npx vitest run")
    w("```")
    w("")
    w(f"5. Register in `lib/genmath-data/{corpus}.ts` — add the import and the")
    w("   MN map entry. **Course-local, never the aggregator's slug-keyed map**")
    w("   (`lib/genmath-mn-collision.test.ts` explains why).")
    w("")
    w("---")
    w("")
    w("## Commit")
    w("")
    w("```")
    w(f"{corpus} MN: {slug} rewrite")
    w("```")
    w("")
    w("One topic per commit.")
    w("")
    return "\n".join(out) + "\n"


def generate(corpus, slug, glossary, theses=None):
    p = os.path.join(ROOT, "data", "genmath", corpus, f"{slug}.json")
    topic = json.load(open(p, encoding="utf8"))
    d = os.path.join(OUT, f"{corpus}-{slug}")
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "teacher.md"), "w", encoding="utf8").write(teacher_brief(corpus, topic, glossary, theses))
    open(os.path.join(d, "build.md"), "w", encoding="utf8").write(build_brief(corpus, topic))
    return d


def main():
    args = sys.argv[1:]
    if not args:
        raise SystemExit(__doc__)
    glossary = load_glossary()
    theses = load_theses()
    if args[0] == "--queue":
        n = int(args[1]) if len(args) > 1 else 5
        q = json.load(open(os.path.join(ROOT, "data", "i18n", "mn-brief-queue.json"), encoding="utf8"))
        todo = [r for r in q["queue"] if not r["hasMn"]][:n]
        for r in todo:
            print("wrote", generate(r["corpus"], r["slug"], glossary, theses))
        return 0
    print("wrote", generate(args[0], args[1], glossary, theses))
    return 0


if __name__ == "__main__":
    sys.exit(main())
