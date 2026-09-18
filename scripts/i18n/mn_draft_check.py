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
# with ( ) and asides with [ ].
#
# This started advisory because the drafts carried 864 of them and a gate that
# is red from birth is a gate nobody reads (the same reasoning the EMPHASIS rule
# records). All thirteen drafts reached zero on 16 Sep 2026, so the reason to
# keep it advisory is gone and it is FATAL now. An advisory nobody has to act on
# is how the count got to 864 in the first place.
# The `(?:<br>)?` is not a loophole: inside a step table a cell's fields are
# separated by `<br>` exactly as they are separated by a space elsewhere, so
# «… нь —<br>**options**» is the same scaffolding as «… нь — **options**». Four
# tapQuestion prompts in geometry/foundations were charged for the draft's own
# table syntax because the separator happened to be a line break.
EMDASH_SCAFFOLD = re.compile(
    r'—\s*(?:<br>)?\s*\*\*(correctIndex|answerIndex|problemId|statement|solution|'
    r'correction|text|options|choices|prompt|explanation|body|teach|points|config|'
    r'title|eyebrow|given|prove|rows|intro)')

# §7 — decimal COMMA, thousands SPACE. 56 comma-decimals against 5 period ones.
# Only judged outside $...$: inside math the decimal point is LaTeX, and a comma
# there would change what KaTeX renders and desync the English mirror.
DECIMAL_POINT = re.compile(r'(?<![\w.])\d+\.\d+(?![\w.])')

# §7 again, the other side of it. Review pile item 2d holds math-mode decimals
# at the English's period until Khas rules on 178 of them, and item 2c holds
# thousands separators at `{,}` because that is what the English writes. So a
# `{,}` inside $...$ is correct when the English has one and wrong when the
# English has a period there — the second is item 2d applied to one instance,
# which is worse than either policy applied uniformly. Twelve had crept in
# across three drafts, four of them inside answer options, and a `$b \le 16{,}25$`
# earlier had to be reverted for the same reason. Judged against the English
# rather than by shape, because `109{,}350` and `2{,}5` look alike to a regex.
MATH_COMMA = re.compile(r'\d+(?:\{,\}\d+)+')

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


def in_facts_block(content: str, pos: int) -> bool:
    """True when pos sits inside a **FACTS:** list of the compressed ЭШ draft
    format, which ends at the next bold ALL-CAPS section heading."""
    start = content.rfind('**FACTS:**', 0, pos)
    if start == -1:
        return False
    nxt = re.search(r'\n\*\*[A-ZА-Я][A-ZА-Я ]+:\*\*', content[start + 10:pos])
    return nxt is None


def check(corpus: str, slug: str) -> int:
    root = pathlib.Path(__file__).resolve().parents[2]
    draft = root / 'memory' / 'mn-drafts' / f'{corpus}-{slug}.md'
    source = root / 'data' / 'genmath' / corpus / f'{slug}.json'
    if not draft.exists():
        print(f'no draft: {draft}'); return 1
    content = content_of(draft.read_text(encoding='utf-8'))
    d = json.loads(source.read_text(encoding='utf-8'))
    fails = []
    notes = []          # true but not actionable by the draft; printed, never fatal

    # A draft is hand-wrapped at 79 columns, so it is easy to break a line in
    # the middle of $...$. The delimiters then re-pair across the wrap — the
    # closing `$` of one span joins the opening `$` of the next — and the prose
    # caught between them is reported as Cyrillic inside maths. That misnames
    # the fault three times over: nothing is wrong with the maths, the wrap is.
    # Checked first so the accurate message is the one the writer reads.
    for n, ln in enumerate(content.split('\n'), 1):
        if len(re.findall(r'(?<!\\)\$', ln)) % 2:
            fails.append(f'MATH SPANS A LINE BREAK (line {n} of the content, '
                         f'rewrap so $...$ stays on one line): {ln.strip()[:70]}')

    for m in re.finditer(r'(?<!\\)\$([^$\n]+?)(?<!\\)\$', content):
        if CYR.search(re.sub(r'\\text\{[^}]*\}', '', m.group(1))):
            fails.append(f'CYR-IN-MATH: ${m.group(1)}$')

    src_text = source.read_text(encoding='utf-8')
    for m in re.finditer(r'(?<!\\)\$([^$\n]+?)(?<!\\)\$', content):
        for c in MATH_COMMA.finditer(m.group(1)):
            period = c.group(0).replace('{,}', '.')
            if period in src_text:
                fails.append(f'MATH DECIMAL COMMA (review pile 2d is NOT applied): '
                             f'«{c.group(0)}» in ${m.group(1)}$')

    # OBJECTIVE MATH MODE. Every lesson route renders `{lesson.objective}` as a
    # bare string — app/math/<grade>/[topic]/[lesson]/page.tsx and the ЭШ learn
    # page alike — while `keyIdea` right beside it goes through <MathText>. So
    # `$...$` in an objective ships the delimiters and the LaTeX source to the
    # student, visibly. The English already does this 190 times across 69 data
    # files (logged for a ship-mode session as review-pile 6d); what a draft
    # must never do is ADD it where the English wrote plain text, because that
    # makes the mirror strictly worse than the page it mirrors. Same shape as
    # the EMPHASIS check above: mirroring is fine, introducing is not.
    drafted_obj = re.findall(r'\*\*objective\*\*\s*\n\n(.+?)\n\n', content, re.S)
    src_obj = [(l.get('slug'), l.get('objective') or '') for l in d.get('lessons') or []]
    if len(drafted_obj) == len(src_obj):
        for (s, en), mn in zip(src_obj, drafted_obj):
            if '$' in mn and '$' not in en:
                fails.append(f'OBJECTIVE MATH MODE {s}: the draft adds $...$ where the '
                             f'English objective is plain text, and objectives do not '
                             f'render maths — «{" ".join(mn.split())[:70]}»')

    for w in INFORMAL:
        for m in re.finditer(w, content):
            fails.append(f'REGISTER: ...{content[max(0, m.start()-40):m.end()+15]}...')

    for w in RUSSIAN:
        for m in re.finditer(r'\b' + w + r'\b', content, re.I):
            fails.append(f'RUSSIAN: «{content[m.start():m.end()]}» in '
                         f'...{content[max(0, m.start()-45):m.end()+25]}...')

    # EMPHASIS. `mn-translation` §5: "Single *italics* in EN may carry over only
    # where EN had it; never introduce new single-asterisk." A flat count could
    # not tell those two apart, so every carried-over italic read as a failure —
    # geometry/foundations drew seven findings for mirroring the English exactly.
    # Counting the source's own italics separates them.
    #
    # Worth knowing while reading this: components/esh/MathText.tsx, which
    # genmath renders through, splits on `$$`, `$` and `**` only, so a single
    # asterisk ships as a literal asterisk TODAY — in English and in the four
    # shipped Mongolian mirrors alike (3,024 strings across 68 data files).
    # That is a renderer bug, not a translation one, and stripping the italics
    # out of the Mongolian would lose emphasis the English keeps. Logged for a
    # ship-mode session; this check only guards against adding more.
    prose = re.sub(r'\$[^$\n]*\$', '', content)
    ital = re.compile(r'(?<![*\\])\*(?!\*)([^*\n]{1,80})\*(?!\*)')
    drafted_ital = [m.group(1) for m in ital.finditer(prose)]
    src_ital = []

    def _walk_ital(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k not in ('check', 'verify'):
                    _walk_ital(v)
        elif isinstance(o, list):
            for v in o:
                _walk_ital(v)
        elif isinstance(o, str):
            src_ital.extend(ital.findall(re.sub(r'\$[^$\n]*\$', '', o)))

    _walk_ital(d)
    if len(drafted_ital) > len(src_ital):
        for w in drafted_ital:
            fails.append(f'EMPHASIS INTRODUCED: *{w}* '
                         f'({len(drafted_ital)} in the draft, {len(src_ital)} in the English)')
    elif drafted_ital:
        notes.append(f'emphasis: {len(drafted_ital)} single-asterisk italics carried over '
                     f'from the English\'s {len(src_ital)} (MathText renders them literally '
                     f'until the renderer learns italics)')

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
                cells = [o.strip().strip('`') for o in opts.split('·')]
                n = len(opts.split('` · `'))
                if n != len(q['options']):
                    fails.append(f'{label} OPTION COUNT {l["slug"]}/{name}: {n} != {len(q["options"])}')
                if int(ci) != q['correctIndex']:
                    fails.append(f'{label} CORRECT INDEX {l["slug"]}/{name}: {ci} != {q["correctIndex"]}')
                # Option ORDER. mn_apply swaps strings in place, so a reordered
                # option list desyncs the mirror from correctIndex silently. The
                # index check above only catches a reorder that MOVED the answer;
                # five reorderings in geometry/foundations were caught that way,
                # and a sixth that kept the index would not have been.
                #
                # Judged as a PERMUTATION, not position by position. Plenty of
                # options differ from the English on purpose — the ЭШ drafts
                # write intervals `]a, b[`, prefer \varnothing to \emptyset, and
                # escape `\|` because a bare pipe would end the markdown table
                # cell — and a straight equality check reported all of those as
                # errors. A permutation is the one shape that is never a
                # translation decision: the same options, moved.
                if n == len(q['options']):
                    now = [c.replace(r'\|', '|') for c in cells]
                    if sorted(now) == sorted(q['options']) and now != q['options']:
                        fails.append(f'{label} OPTION ORDER {l["slug"]}/{name}: '
                                     f'reordered — {now} vs {q["options"]}')

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
        if re.search(r'\*\*(?:answer|correct)Index \d+\*\*\s*$', before):
            continue          # the SECOND dash in «— **answerIndex 0** — explanation»:
                              # the older drafts separate the key from its
                              # explanation that way, so it is scaffolding too
        if re.match(r'—\s*`', after):
            continue          # «**title** Нөхцөлөөс жагсаалт руу — `esh-sets-l1-we1`»:
                              # the ЭШ drafts point at a problem id this way
        if re.search(r'\*\*[a-z][\w-]*\d\*\*\s*$', before):
            continue          # «**esh-sets-p2** — …», «**ef-pr1** — …»: a bold
                              # problem id followed by its statement. Matched by
                              # shape (lowercase token ending in a digit) so the
                              # rule is not per-corpus.
        if in_facts_block(content, m.start()) and (
                re.search(r'(?:\*\*|\$)\s*$', before) or re.match(r'—\s*\n', after)):
            continue          # a FACTS row in the compressed ЭШ format is
                              # «N. **label** — $latex$ — explanation», i.e. the
                              # algebra drafts' three-column fact table written
                              # inline. Those two dashes are column separators.
                              # Only inside the block: «**«Аль нь ч биш»** — …»
                              # in ordinary prose is a real parenthetical.
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
    fails += [f'EM-DASH PARENTHETICAL (§9): ...{e}...' for e in emdash]
    if advisory:
        print(f'\n  {len(advisory)} bare imperative(s) — ADVISORY, judge each:')
        for a in advisory:
            print(f'    {a}')
    for n in notes:
        print(f'\n  NOTE: {n}')
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
