#!/usr/bin/env python3
"""Mechanical checks on a Mongolian rewrite DRAFT, before Build assembles it.

The drafts are markdown, not JSON, so mn_skeleton.py cannot see them yet — but
the failures it catches are cheapest to fix while the prose is still being
written. This checks what is checkable at draft stage:

  CYR-IN-MATH   Cyrillic inside $...$ outside \text{}  (breaks KaTeX)
  REGISTER      informal pronouns, against the «та» ruling
  EMPHASIS      single-asterisk, which MathText renders literally
  RUSSIAN       Russian words that share the Cyrillic alphabet and so pass
                every other check. «ЛЮБОЙ» reached a finished draft this way:
                it looks Mongolian to a spellcheck-free eye and is invisible to
                a CYR-IN-MATH scan. The list is short and covers the function
                words most likely to slip, not Russian generally.
  IMPERATIVE    ADVISORY, never fatal. Bare imperatives addressed to a student
                contradict the «та» ruling — but most hits are legitimate:
                imperative headings are normal in both languages, and terse
                rule statements («Ганцаарчилсан хас хос нэм» is *singles minus
                pairs plus triple*, arithmetic nouns rather than commands) read
                correctly. A check that mostly cries wolf gets switched off, so
                this one reports and lets a human judge.

  IDS           every problem id present exactly as the English source has it,
                and none invented
  SKELETON      per lesson: step kinds in order, and for BOTH interactive
                question shapes — tapQuestion steps and tryItSet problems —
                the option counts and correct index, all identical to the
                English source. The draft marks the two differently
                (**options**/**correctIndex** vs **choices**/**answerIndex**)
                so a topic containing both cannot have one silently checked
                against the other's source steps.

Commentary sections (the per-lesson "What makes this a rewrite" paragraphs and
the trailing Notes) are excluded — they are never copied into JSON, and judging
them produces false positives that train the reader to ignore the output.

    python3 scripts/i18n/mn_draft_check.py <corpus> <slug>
"""
import json, re, sys, pathlib

CYR = re.compile('[А-Яа-яЁёӨөҮү]')
INFORMAL = [r'\bчи\b', r'\bчиний\b', r'\bчамд\b', r'\bчамайг\b', r'\bчамаас\b']

# Russian function words with no Mongolian reading. Deliberately short: a long
# list would collide with real Mongolian words and get switched off.
# Bare imperative stems. Advisory only — see the docstring.
BARE = ['зур', 'тоол', 'шалга', 'бич', 'хялбарчил', 'ангил', 'сур', 'бод',
        'оруул', 'нэм', 'хас', 'тайл', 'өргө', 'сонго']
# Coined rule names. These are labels, not instructions to the reader.
COINED = ['нэгийг нэм', 'төвийг хас']

RUSSIAN = ['любой', 'любые', 'если', 'который', 'которые', 'потому', 'этот',
           'эта', 'это', 'все', 'всё', 'где', 'когда', 'очень', 'может',
           'должен', 'также', 'таким', 'своих', 'после', 'через', 'между']

# ---------------------------------------------------------------- voice rules
# Added 15 Sep 2026 from docs/mn-voice-reference.md, which is derived from 1,047
# English sentences printed beside their published Mongolian rendering. The
# point of putting them here rather than in prose: terminology was already
# mechanical (mn_terms.py) while voice was not, so a draft could pass every gate
# and still read as translated. These are the rules from that file that a script
# can actually judge.
#
# NOT encoded, deliberately: clause order (§1), the naming verbs (§2), `юм` (§4)
# and "be more explicit than the English" (§10). Those need a reader. A check
# that guessed at them would cry wolf and get switched off, which is how the
# IMPERATIVE advisory nearly went.

# §9 — the em dash appears ONCE in 1,147 published passages. Mongolian glosses
# with ( ) and asides with [ ]. Advisory, not fatal: the existing drafts carry
# 864 of them, and a gate that is red from birth is a gate nobody reads (the
# same reasoning the EMPHASIS rule records).
EMDASH_SCAFFOLD = re.compile(
    r'—\s*\*\*(correctIndex|answerIndex|problemId|statement|solution|correction|'
    r'text|options|choices|prompt|explanation|body|teach|points|config|title|eyebrow)')

# §7 — decimal COMMA, thousands SPACE. 56 comma-decimals against 5 period ones.
# Only judged outside $...$: inside math the decimal point is LaTeX, and a comma
# there would change what KaTeX renders and desync the English mirror.
DECIMAL_POINT = re.compile(r'(?<![\w.])\d+\.\d+(?![\w.])')

# §8 — case suffixes on numerals and Latin symbols take a hyphen (264 uses).
NO_HYPHEN_SUFFIX = re.compile(r'(?<=[A-Za-z0-9])(ийн|ыг|ийг|аас|ээс|оос|өөс|тай|той|тэй)\b')

# Smell test §3 — оюутан is a university student; this site's readers are at
# school. Matched on the stem so the oblique forms (оюутны, оюутанд) are seen.
STUDENT_WORD = re.compile(r'оюутн|оюутан')


def content_of(src: str) -> str:
    # Content starts at the topic-level strings (TITLE/BLURB ship) when a draft
    # has them, and at the first lesson otherwise. Without the fallback, the
    # four drafts written before that heading existed had their English header
    # and Terminology table judged as if they were Mongolian that ships — which
    # is how a note reading *eliminating the unknown* drew an EMPHASIS finding.
    if '## Topic-level strings' in src:
        body = src.split('## Topic-level strings', 1)[1]
    else:
        # Lookahead, so the heading itself survives the split: the em-dash
        # check recognises a heading by the «## » in front of it, and slicing
        # that off left «1 — Нэг ба хоёр алхамт тэгшитгэл» looking like prose.
        body = re.split(r'\n(?=## Lesson )', src, maxsplit=1)[-1]
    body = body.split('## Notes for Build', 1)[0]
    # The trailing questions-for-Khas section is commentary and never ships, so
    # judging it produces findings that cannot be acted on. It quotes the very
    # wording it is asking about — a note explaining why «оюутан» was removed
    # failed the оюутан check three times over, which is exactly the "trains the
    # reader to ignore the output" failure this function already guards against.
    body = body.split('## Notes for Khas', 1)[0]
    # Both commentary headings used across the drafts. A heading this misses
    # leaves English commentary inside the "content" the checks judge, which
    # showed up as four phantom EMPHASIS failures on the first topic to use the
    # second wording.
    return re.sub(r'\*\*(?:What makes this a rewrite|Rewrite thesis)\.\*\*.*?(?=\n\*\*TITLE:)',
                  '', body, flags=re.S)


def check(corpus: str, slug: str) -> int:
    root = pathlib.Path(__file__).resolve().parents[2]
    draft = root / 'memory' / 'mn-drafts' / f'{corpus}-{slug}.md'
    source = root / 'data' / 'genmath' / corpus / f'{slug}.json'
    if not draft.exists():
        print(f'no draft: {draft}'); return 1
    content = content_of(draft.read_text(encoding='utf-8'))
    d = json.loads(source.read_text(encoding='utf-8'))
    fails = []

    for m in re.finditer(r'(?<!\\)\$([^$\n]+?)(?<!\\)\$', content):
        if CYR.search(re.sub(r'\\text\{[^}]*\}', '', m.group(1))):
            fails.append(f'CYR-IN-MATH: ${m.group(1)}$')

    for w in INFORMAL:
        for m in re.finditer(w, content):
            fails.append(f'REGISTER: ...{content[max(0, m.start()-40):m.end()+15]}...')

    for w in RUSSIAN:
        for m in re.finditer(r'\b' + w + r'\b', content, re.I):
            fails.append(f'RUSSIAN: «{content[m.start():m.end()]}» in '
                         f'...{content[max(0, m.start()-45):m.end()+25]}...')

    prose = re.sub(r'\$[^$\n]*\$', '', content)
    for m in re.finditer(r'(?<![*\\])\*(?!\*)([^*\n]{1,80})\*(?!\*)', prose):
        fails.append(f'EMPHASIS: *{m.group(1)}*')

    want = []
    for l in d['lessons']:
        want += [p['id'] for p in l['workedExamples']] + [p['id'] for p in l['tryIt']]
    want += [p['id'] for p in d['practice']] + [p['id'] for p in d['testYourself']]
    stem = want[0].rsplit('-', 2)[0] if want else ''
    fails += [f'MISSING ID: {i}' for i in want if i not in content]
    fails += [f'UNKNOWN ID: {i}' for i in
              sorted(set(re.findall(re.escape(stem) + r'-[a-z0-9\-]+', content)) - set(want))]

    tables = re.findall(r'### Interactive.*?\n\n((?:\|.*\n)+)', content)
    if len(tables) != len(d['lessons']):
        fails.append(f'LESSONS: {len(tables)} step tables for {len(d["lessons"])} lessons')
    for l, tbl in zip(d['lessons'], tables):
        kinds = [r.split('|')[2].strip() for r in tbl.strip().split('\n')[2:]]
        src_kinds = [s['kind'] for s in l['interactive']['steps']]
        if kinds != src_kinds:
            fails.append(f'STEP KINDS {l["slug"]}: {kinds} != {src_kinds}')
        else:
            print(f'  {l["slug"]:34s} {len(kinds)} steps, kinds match')
        # tapQuestion steps, and tryItSet problems, checked separately.
        src_tap = [s for s in l['interactive']['steps'] if s['kind'] == 'tapQuestion']
        src_try = [p for s in l['interactive']['steps'] if s['kind'] == 'tryItSet'
                   for p in s.get('problems', [])]
        for label, src, pat in (
            ('TAP', src_tap, r'\*\*options\*\*(.*?)—\s*\*\*correctIndex (\d+)\*\*'),
            ('TRYSET', src_try, r'\*\*choices\*\*(.*?)—\s*\*\*answerIndex (\d+)\*\*'),
        ):
            drafted = re.findall(pat, tbl)
            if len(src) != len(drafted):
                fails.append(f'{label} COUNT {l["slug"]}: {len(drafted)} != {len(src)}')
                continue
            for q, (opts, ci) in zip(src, drafted):
                name = q.get('title') or q.get('prompt', '')[:34]
                n = len(opts.split('` · `'))
                if n != len(q['options']):
                    fails.append(f'{label} OPTION COUNT {l["slug"]}/{name}: {n} != {len(q["options"])}')
                if int(ci) != q['correctIndex']:
                    fails.append(f'{label} CORRECT INDEX {l["slug"]}/{name}: {ci} != {q["correctIndex"]}')

    # ---- voice, per docs/mn-voice-reference.md ----------------------------
    # Judge PROSE only. Two things are stripped first, both machinery rather
    # than copy (rule 12 — translate copy, not machinery):
    #   $...$  math, where the decimal point is LaTeX, not Mongolian punctuation
    #   `...`  ids, slugs, latex and widget config — `b: 0.5` is a config value
    #          a student never reads, and comma-ising it would break the widget.
    # The \$ lookbehind matters: an escaped dollar is a literal currency sign,
    # and pairing it with a real delimiter swallows the prose between them and
    # spills the math out. A price line («\$800 үнэтэй утас … $V = 800(0.75)^t$»)
    # reported two decimal points that were inside math all along.
    prose_only = re.sub(r'`[^`\n]*`', '',
                        re.sub(r'(?<!\\)\$[^$\n]*?(?<!\\)\$', '', content))

    for m in DECIMAL_POINT.finditer(prose_only):
        ctx = ' '.join(prose_only[max(0, m.start() - 40):m.end() + 20].split())
        fails.append(f'DECIMAL POINT (§7 wants a comma): «{m.group(0)}» in ...{ctx}...')

    for m in NO_HYPHEN_SUFFIX.finditer(prose_only):
        ctx = ' '.join(prose_only[max(0, m.start() - 30):m.end() + 10].split())
        fails.append(f'UNHYPHENATED SUFFIX (§8): ...{ctx}...')

    for m in STUDENT_WORD.finditer(prose_only):
        ctx = ' '.join(prose_only[max(0, m.start() - 45):m.end() + 30].split())
        fails.append(f'ОЮУТАН (smell test §3 — school readers are «сурагч»): ...{ctx}...')

    emdash = []
    for m in re.finditer('—', content):
        after, before = content[m.start():m.start() + 40], content[:m.start()]
        if EMDASH_SCAFFOLD.match(after) or re.search(r'`\s*$', before[-60:]):
            continue          # this draft's own table syntax, which the parser above reads
        if re.search(r'(?:^|\n)#{1,4} [^\n]*$', before):
            continue          # a markdown heading («## Lesson 2 — Онцгой үржвэрүүд»):
                              # the draft's own outline, not a string that ships
        if CYR.search(before[-30:]) or CYR.search(after[1:30]):
            emdash.append(' '.join(content[max(0, m.start() - 45):m.start() + 45].split()))

    advisory = []
    for w in BARE:
        for m in re.finditer(r'(?<![а-яөүёА-ЯӨҮЁ])' + w + r'(?![а-яөүёА-ЯӨҮЁ])', content):
            ctx = ' '.join(content[max(0, m.start()-55):m.end()+8].split())
            if not any(c in ctx for c in COINED):
                advisory.append(f'«{w}» ...{ctx[-58:]}')

    print(f'\n  ids {len(want) - sum(f.startswith("MISSING") for f in fails)}/{len(want)}')
    if emdash:
        print(f'\n  {len(emdash)} em-dash parenthetical(s) in Mongolian prose — ADVISORY '
              f'(voice reference §9: one in 1,147 published passages; use ( ) or [ ], '
              f'or restructure with тул / учраас / бөгөөд / Иймд):')
        for e in emdash[:8]:
            print(f'    {e}')
        if len(emdash) > 8:
            print(f'    ... and {len(emdash) - 8} more')
    if advisory:
        print(f'\n  {len(advisory)} bare imperative(s) — ADVISORY, judge each:')
        for a in advisory:
            print(f'    {a}')
    if fails:
        print(f'\n--- {len(fails)} finding(s) ---')
        for f in fails:
            print(' ', f)
        return 1
    print('\n  ALL DRAFT CHECKS PASS')
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('usage: mn_draft_check.py <corpus> <slug>')
    raise SystemExit(check(sys.argv[1], sys.argv[2]))
