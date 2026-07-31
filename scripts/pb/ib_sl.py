# -*- coding: utf-8 -*-
"""ib-sl bank — thin wrapper; the generators live in scripts/pb/ib.py."""
import os
import sys

PB = os.path.dirname(os.path.abspath(__file__))
if PB not in sys.path:
    sys.path.insert(0, PB)

import ib


def build():
    return ib.build_sl()
