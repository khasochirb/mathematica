#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Structural + age-fit gate for the Grade 3 corpus.

The checks live in scripts/primary_check.py, shared with Grade 4 so the
rules cannot drift between the two primary years. Grade 3's knob is its
number ceiling: nothing above 1000 in student-facing prose, which is the
mechanical expression of "Grade 3 sits one rung BELOW Grade 4". A lesson
that quietly reaches for four-digit numbers fails the build.

Run: python3 scripts/grade3/check_grade3.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from primary_check import run  # noqa: E402

if __name__ == "__main__":
    sys.exit(run(grade=3, ceiling=1000))
