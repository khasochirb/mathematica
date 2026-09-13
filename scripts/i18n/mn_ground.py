#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify a proposed Mongolian glossary against the evidence it claims.

    python3 scripts/i18n/mn_ground.py <proposals.json>

WHY THIS EXISTS. Every proposed term carries a provenance label — "ministry",
"glossary", "shipped" or "proposal" — and the owner reads that label to decide
where to spend their correction time. A label that overclaims is worse than no
label at all: it routes the owner AWAY from the entry that most needs them.

On the 91-string chrome batch, checking labels this way caught eight entries
claimed as established that were only derived from a related string. Doing it
by eye over ~800 rows is not a plan.

WHAT IT CHECKS. For each row, whether the proposed Mongolian actually occurs in
the source its provenance names:

  ministry  -> data/esh/moe-curriculum.json (order A/492) section titles and
               objective texts
  glossary  -> the GLOSSARY values in scripts/i18n/mn_terms.py
  shipped   -> the Mongolian side of the already-shipped MN mirrors

MATCHING IS STEM-BASED, NOT EXACT. Mongolian is agglutinative: a term appears
in running ministry prose with case and number suffixes attached
(тэгшитгэл / тэгшитгэлийн / тэгшитгэлүүд). An exact substring test would report
a correctly-sourced term as ungrounded, so each content word is matched on a
stem prefix. The trade is deliberate: this tool is tuned to avoid FALSE ALARMS,
because an alarm the owner learns to ignore is worse than a missed one. A
"grounded" verdict therefore means "the source plausibly contains this", not
"the source contains exactly this".

Exit status is always 0 — this reports, it does not gate. Terminology is the
owner's call, and a script must not block their queue on its own stemming.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "scripts", "i18n"))

CYR = re.compile(r"[А-Яа-яЁёӨөҮү]+")
# Grammatical words that carry no terminological weight; matching on them would
# make almost anything look grounded.
FUNCTION_WORDS = {
    "ба", "буюу", "болон", "нь", "юм", "энэ", "тэр", "бол", "гэж", "дээр",
    "доор", "тул", "учир", "хэрэв", "бүр", "бүх", "зарим", "аль", "ямар",
    "хийх", "байх", "болох", "гэсэн", "тухай", "хоёр", "гурав", "нэг",
}
STEM_MIN = 5  # a content word matches on this many leading characters


def stem(word: str) -> str:
    return word[:STEM_MIN] if len(word) > STEM_MIN else word


def content_stems(mn: str):
    """Stems of the terminologically meaningful words in a Mongolian string."""
    out = []
    for w in CYR.findall(mn.lower()):
        if w in FUNCTION_WORDS or len(w) < 3:
            continue
        out.append(stem(w))
    return out


def haystack_tokens(text: str):
    """The source as an ORDERED token list, for phrase-adjacency matching.

    Word-presence alone is not enough for a multi-word term. "мод диаграм"
    (tree diagram) was reported as present in the ministry standard because
    "модны" occurs in 10.15б and "диаграмм" in 10.13в — different sentences,
    different concepts. The standard's actual term for a tree diagram is
    "модны схем", so the site's glossary contradicts it, and a scattered-word
    match hid exactly the disagreement this tool exists to find.
    """
    return CYR.findall(text.lower())


def haystack_stems(text: str) -> set:
    """The PREFIX set of a source document, computed once.

    Tokenised, NOT a raw string. Substring matching against the raw text is
    what a first version of this did, and it grounded 100 out of 100 glossary
    terms in the ministry standard — including "цайны мөнгө" (tip) and
    "мод диаграм" (tree diagram), which are primary-school concepts that a
    grade 10-12 standard does not contain. The cause: a short stem like "мод"
    matches inside any longer word that happens to contain those letters. A
    check that grounds everything detects nothing.

    Prefixes rather than one fixed-length stem, because truncating to a fixed
    length is asymmetric and produces FALSE ALARMS. "тэгш хэм" (symmetry) is
    ministry 10.11, where it appears inflected as "тэгш хэмээр". Truncating
    both to five characters gives "хэм" on one side (too short to cut) and
    "хэмээ" on the other, which do not compare equal — so a correctly-sourced
    term was reported as an overclaim. Indexing every 3-to-5 character prefix
    of every source word makes the comparison symmetric: a short query word
    matches the longer inflected form it is a prefix of.
    """
    out = set()
    for w in CYR.findall(text.lower()):
        for k in (3, 4, STEM_MIN):
            if len(w) >= k:
                out.add(w[:k])
    return out


def _pref(w: str) -> str:
    return w[: min(len(w), STEM_MIN)]


def grounded_in(mn: str, source) -> bool:
    """True when the source contains `mn` as a PHRASE, allowing inflection.

    `source` is (prefix_set, token_list) from prepare().

    Two things have to be true at once, and each is a bug this tool already
    made once:

      every content word must be present     — 'нийлмэл' alone does not ground
                                               'нийлмэл дүрсийн талбай'
      and they must be NEAR ONE ANOTHER      — 'мод' in one objective plus
                                               'диаграмм' in another does not
                                               ground 'мод диаграм'

    Inflection is handled by prefix comparison in both directions, because
    Mongolian attaches case and number endings to the term itself: the query
    'хэм' must match the source's 'хэмээр', and the query 'тэгшитгэлийн' must
    match the source's 'тэгшитгэл'.
    """
    prefixes, tokens = source
    stems = content_stems(mn)
    if not stems:
        return False
    if not all(s in prefixes for s in stems):
        return False
    if len(stems) == 1:
        return True

    # Phrase check: all words inside one window. The window allows a couple of
    # intervening words, because Mongolian inserts genitive/adjectival material
    # inside a term ("тойргийн нумын урт" for "arc length").
    window = len(stems) + 3
    first = stems[0]
    for i, tok in enumerate(tokens):
        if not (tok.startswith(first) or first.startswith(_pref(tok))):
            continue
        chunk = tokens[i : i + window]
        if all(
            any(t.startswith(s) or s.startswith(_pref(t)) for t in chunk)
            for s in stems
        ):
            return True
    return False


def load_sources():
    moe = json.load(open(os.path.join(ROOT, "data", "esh", "moe-curriculum.json"), encoding="utf8"))
    ministry = " ".join(
        [s["title"] for s in moe["sections"]]
        + [o["text"] for s in moe["sections"] for o in s["objectives"]]
    )

    import mn_terms  # noqa: E402
    glossary = " ".join(mn_terms.GLOSSARY.values())

    shipped = shipped_corpus()
    return (prepare(ministry), prepare(glossary), prepare(shipped))


def prepare(text: str):
    """A source, ready to match against: (prefix set, ordered token list)."""
    return (haystack_stems(text), haystack_tokens(text))


def shipped_corpus() -> str:
    """Every word of Mongolian the site has actually published.

    TWO sources, and the second is the larger one:

      data/genmath/*-mn/**       the 25 translated General Math mirrors
      data/questions/**          the ESh bank — 20 real past papers with
                                 authored Mongolian solutions, ~449k characters

    The ESh bank matters more than its size suggests. It is Mongolian-FIRST
    content (the hub's content language is Mongolian by locked decision), not
    translated, so its vocabulary is what a Mongolian maths writer actually
    reaches for rather than what a translator produced. For terminology
    evidence that is the better witness of the two.

    Read from the repo rather than a passed-in file so the checker cannot be
    run against a stale or partial corpus by accident. $MN_SHIPPED_PAIRS still
    overrides, for checking a proposal against some other body of text.
    """
    override = os.environ.get("MN_SHIPPED_PAIRS", "")
    if override and os.path.exists(override):
        return " ".join(p.get("mn", "") for p in json.load(open(override, encoding="utf8")))

    import glob

    out = []
    for path in glob.glob(os.path.join(ROOT, "data", "genmath", "*-mn", "*.json")):
        out.append(open(path, encoding="utf8").read())
    for path in glob.glob(os.path.join(ROOT, "data", "questions", "**", "*.json"), recursive=True):
        out.append(open(path, encoding="utf8").read())
    return " ".join(out)


def selftest() -> int:
    """Prove the matcher still discriminates.

    The first version of grounded_in() matched stems as raw substrings against
    the source text and reported EVERY term as grounded in the ministry
    standard. It passed a smoke test — the fabricated control was still caught,
    because its letters appear nowhere — and was only caught by asking whether
    a grade 10-12 standard could really contain "tip" and "tree diagram".

    So a smoke test is not enough here. The failure mode of this tool is
    grounding too much, and that is invisible unless something asserts that
    specific out-of-scope terms come back ABSENT. That is what this does.
    """
    ministry, glossary, shipped = load_sources()

    # Primary-school vocabulary. A grade 10-12 standard does not teach these.
    #
    # "tree diagram" was on this list and did NOT belong: the standard covers it
    # three times (10.15б, 11.13д, 12.15а). It calls it "модны схем" — so the
    # site's glossary term "мод диаграм" disagrees with the ministry, which is a
    # finding, not a control. Both forms are asserted below instead.
    must_be_absent = [
        ("tip", "цайны мөнгө"),
        ("capture-recapture", "барих дахин барих"),
        ("net of a solid", "дэлгээс"),
        ("expected count", "хүлээгдэх тоо"),
        ("commission", "шимтгэл"),
        ("markup", "нэмэгдэл"),
    ]
    # Core upper-secondary vocabulary. The standard certainly contains these.
    must_be_present = [
        ("derivative", "уламжлал"),
        ("integral", "интеграл"),
        ("matrix", "матриц"),
        ("probability", "магадлал"),
        ("inequality", "тэнцэтгэл биш"),
        ("logarithm", "логарифм"),
    ]
    # Not Mongolian at all — must never ground anywhere.
    fabricated = [("nonsense", "зөгнөлт хуурмаг үг")]

    # PHRASE ADJACENCY. The standard has "модны схем" for a tree diagram and
    # separately has "диаграмм" (10.13в, 11.11а). A checker that only asks
    # whether each word occurs SOMEWHERE grounds the site's "мод диаграм" by
    # stitching those two together, and hides the disagreement. The ministry's
    # own form must ground; the site's must not.
    phrase_pairs = [
        ("tree diagram — ministry form", "модны схем", True),
        ("tree diagram — site glossary form", "мод диаграм", False),
    ]

    failures = []
    # A source that silently fails to load makes every claim against it look
    # like an overclaim — the loudest possible wrong answer. Assert each one
    # actually has content before trusting any verdict computed from it.
    for name, src, floor in (("ministry", ministry, 300), ("glossary", glossary, 100), ("shipped", shipped, 2000)):
        if len(src[0]) < floor:
            failures.append(f"SOURCE EMPTY: {name} loaded only {len(src[0])} prefixes (expected >{floor})")
    # The grade 6-8 vocabulary below is absent from the STANDARD but present in
    # the shipped corpus, which is what makes the two sources independent.
    for en, mn in must_be_absent:
        if not grounded_in(mn, shipped):
            failures.append(f"SHIPPED GAP: «{mn}» ({en}) is published content but the corpus missed it")
    for en, mn in must_be_absent:
        if grounded_in(mn, ministry):
            failures.append(f"OVER-GROUNDED: «{mn}» ({en}) matched the grade 10-12 standard")
    for en, mn in must_be_present:
        if not grounded_in(mn, ministry):
            failures.append(f"UNDER-GROUNDED: «{mn}» ({en}) did not match the standard")
    for en, mn in fabricated:
        if grounded_in(mn, ministry) or grounded_in(mn, glossary) or (shipped[1] and grounded_in(mn, shipped)):
            failures.append(f"FALSE POSITIVE: fabricated «{mn}» matched a source")
    for en, mn, want in phrase_pairs:
        if grounded_in(mn, ministry) != want:
            verb = "did not match" if want else "matched"
            failures.append(f"PHRASE CHECK: «{mn}» ({en}) {verb} the standard")

    if failures:
        print("mn_ground selftest FAILED:")
        for f in failures:
            print("  " + f)
        return 1
    print(
        f"mn_ground selftest ok — {len(must_be_absent)} out-of-scope terms absent, "
        f"{len(must_be_present)} core terms present, {len(phrase_pairs)} phrase-adjacency "
        f"controls correct, fabricated control rejected"
    )
    return 0


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    if sys.argv[1] == "--selftest":
        return selftest()
    rows = json.load(open(sys.argv[1], encoding="utf8"))
    ministry, glossary, shipped = load_sources()
    if not shipped:
        print("note: MN_SHIPPED_PAIRS unset — 'shipped' claims cannot be checked\n")

    sources = {"ministry": ministry, "glossary": glossary, "shipped": shipped}
    overclaimed, ungrounded, ok = [], [], 0

    for r in rows:
        key = r.get("en") or r.get("id") or "?"
        mn, prov = r.get("mn", ""), r.get("provenance", "proposal")
        hits = [name for name, hay in sources.items() if hay[1] and grounded_in(mn, hay)]

        if prov == "proposal":
            # A "proposal" that turns out to BE in a source is good news, not an
            # error — it means the guess matched the standard. Report it so the
            # label (and its confidence) can be upgraded.
            if hits:
                ungrounded.append((key, mn, prov, f"actually found in: {', '.join(hits)}"))
            else:
                ok += 1
        elif prov in sources and sources[prov] and prov not in hits:
            alt = f"; found instead in: {', '.join(hits)}" if hits else "; found in no source"
            overclaimed.append((key, mn, prov, f'claims "{prov}" but not found there{alt}'))
        else:
            ok += 1

    print(f"rows: {len(rows)}   consistent: {ok}   OVERCLAIMED: {len(overclaimed)}   upgradable: {len(ungrounded)}")
    if overclaimed:
        print("\n── OVERCLAIMED — the label sends the owner the wrong way ──")
        for k, mn, prov, why in overclaimed:
            print(f"  {k}\n      «{mn}»  {why}")
    if ungrounded:
        print("\n── UPGRADABLE — labelled 'proposal' but a source has it ──")
        for k, mn, prov, why in ungrounded:
            print(f"  {k}\n      «{mn}»  {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
