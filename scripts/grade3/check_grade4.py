#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Structural + age-fit gate for the Grade 4 corpus.

The checks live in scripts/primary_check.py, shared with the other
primary-band years so the rules cannot drift between grades. Grade 4's
knob is its number ceiling: nothing above 10 000 in student-facing prose.

Run: python3 scripts/grade3/check_grade4.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from primary_check import run  # noqa: E402

if __name__ == "__main__":
    sys.exit(run(grade=4, ceiling=10000))
