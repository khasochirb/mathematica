#!/usr/bin/env python3
"""Band exit exams — three per band, at the band's exit grade.

Resource blueprint: every school band carries a placement diagnostic at the
top (entry) and IM-style full-course exams at the bottom (exit). The exit
level of a band IS its final grade — Grade 9 for Mid school, Grade 12 for
High school, the two transition years families prepare hardest for — so the
band exams are full-coverage exams over those grades' banks
(scripts/pb/grade9.py, grade12.py).

Selection is the proven IM machinery (scripts/exams/build_im_exams.py):
every unit represented with a laddered difficulty block, archetype spread,
and the three exams pairwise disjoint. Run AFTER build_problembank.py.

Run: python3 scripts/exams/build_band_exams.py   (then npm run verify:exams)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import build_im_exams as im

BAND_COURSES = [
    {
        "slug": "9",
        "title": "Grade 9",
        "minutes": 45,
        "intro": ("The Mid school band's exit exam: every Grade 9 topic is represented, "
                  "so the result shows exactly which topics still need another pass "
                  "before high school."),
    },
    {
        "slug": "12",
        "title": "Grade 12",
        "minutes": 45,
        "intro": ("The High school band's exit exam: every Grade 12 topic is "
                  "represented, so the result shows exactly which topics still need "
                  "another pass — the same map ЭЕШ prep starts from."),
    },
]


def main():
    total = 0
    for course in BAND_COURSES:
        for eid, nq, nu, figs, lv in im.build_course(course):
            total += nq
            print("wrote %s.json — %d questions across %d units, %d with figures "
                  "(L1 %d / L2 %d / L3 %d)" % (eid, nq, nu, figs, lv[1], lv[2], lv[3]))
    print("TOTAL: %d exams, %d questions" % (len(BAND_COURSES) * im.N_EXAMS, total))


if __name__ == "__main__":
    main()
