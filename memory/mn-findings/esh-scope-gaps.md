# ЭШ course — coverage gaps against the ministry standard

Findings made while grounding Mongolian rewrites. **None of these is a
translation problem.** They are product findings that surfaced because the
rewrite pass reads each topic against ministry order А/492 and the 54 past
papers before writing a word, which nothing else in the pipeline does.

Recorded here rather than fixed: adding a lesson is not a rewrite, and the
draft skeleton is fixed by `mn_skeleton.py` on purpose.

---

## G1 · Objective 10.5д is claimed by a unit that does not teach it

**Status: open. Found 30 Aug 2026.**

`lib/esh-course.ts:197` maps the unit `exponential-functions` to three ministry
objectives:

| code | elective | text |
|---|---|---|
| 10.3г | **no** | «$y=a^x$ хэлбэрийн функцийн графикийг утгын хүснэгт ашиглан байгуулах, энд $a$ — эерэг тоо» |
| 10.3е | yes | «$y=ka^x$ хэлбэрийн функцийн графикийг утгын хүснэгт ашиглан байгуулах» |
| 10.5д | **no** | «Илтгэгч тэгшитгэлийг графикийн болон орлуулах аргаар бодох» |

**10.5д is non-elective and nothing in the ЭШ course teaches it.** The unit
resolves to `data/genmath/10/exponential-functions.json`, in which the strings
`equation`, `solve`, `substitut` and `same base` each appear **zero times**.
Grepping `lib/esh-course.ts` shows `10.5д` claimed by this unit and no other,
so a student following the course never meets exponential equations.

Two smaller notes on the same mapping:

- 10.3г and 10.3е both ask for a graph built **from a table of values**. The
  topic uses tables only to *classify* linear vs exponential. The Mongolian
  rewrite turns lesson 1's table work toward reading the function off the
  table, which is as close as a rewrite can legitimately get, but it does not
  add the graph-construction the objectives ask for.
- The unit's other four lessons — growth and decay, exponential vs linear,
  compound interest, half-life — map to no ministry objective in this list and
  match no question in the bank. They earn their place in Grade 10 General
  Math, which is the course this topic primarily serves; they are simply not
  ЭШ preparation.

**Options, for Khas:** extend the unit with a lesson on solving
$a^x = b$ by matching bases and by substitution; or re-map 10.5д onto a
different unit that does teach it; or accept the gap deliberately and record
that. All three are decisions, not fixes — which is why this sits here.

---

## How these were found, so the next session can repeat it

```bash
# what the exam actually tests, by tag
python3 - <<'PY'
import glob, json, collections
c = collections.Counter()
for f in glob.glob('data/questions/*.json'):
    def w(o):
        if isinstance(o, dict):
            if 'body' in o and 'answer' in o:
                c[(o.get('skill_tag'), o.get('topic'))] += 1
            for v in o.values(): w(v)
        elif isinstance(o, list):
            for v in o: w(v)
    w(json.load(open(f, encoding='utf-8')))
print(c.most_common(30))
PY

# what the ministry requires of a unit, by objective code
grep -n '"<unit-slug>"' lib/esh-course.ts        # -> the codes
# then look each code up in data/esh/moe-curriculum.json
```
