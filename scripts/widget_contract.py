# -*- coding: utf-8 -*-
"""The interactive-widget config contract, DERIVED from the TypeScript.

A widget step whose config does not match its `<Kind>Config` interface does
not crash — React destructures the missing key, gets `undefined`, and renders
a silently wrong widget. Five such steps shipped to production before the gate
that reads this module existed.

The contract therefore is not written down anywhere by hand. The discriminated
union at the bottom of lib/genmath-interactive.ts maps each step kind to its
config interface, and the interface itself says which keys are required (no
`?`) and which take a fixed set of string literals. Parsing that is the only
way the checks cannot drift from the components.

Two callers share this one implementation:
  - scripts/verify-genmath.py — the repo-wide gate, over every shipped JSON.
  - scripts/im/imbuild.py     — the builder, so an author fails at build time
                                rather than at gate time.

Before this module existed imbuild.py carried its own hand-listed allowlist,
which had already drifted (it rejected `coef` on balanceScale, a key the
interface has always declared, and knew nothing of roughly half the kinds).
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IFACE_SRC = os.path.join(ROOT, "lib", "genmath-interactive.ts")

_KIND_TO_CONFIG = re.compile(
    r'\|\s*\{\s*kind:\s*"([A-Za-z0-9]+)";[^}]*?config:\s*(\w+Config)\s*\}'
)
_FIELD = re.compile(r"(\w+)(\?)?:\s*([^;]+);")
_STRING_UNION = re.compile(r'(\s*"[^"]+"\s*\|?)+')


def _drop_nested(body):
    """Erase brace-nested types so inline shapes ({ x: number; y: number }[])
    do not leak their inner fields into the top-level field list."""
    out, depth = [], 0
    for ch in body:
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            out.append("X")
        elif depth == 0:
            out.append(ch)
    return "".join(out)


def load_widget_contract(on_error=None):
    """kind -> {field: (required, allowed_literals or None)}.

    `on_error` receives a message for each union member whose config interface
    is missing; callers decide whether that is fatal.
    """
    with open(IFACE_SRC, "r", encoding="utf-8") as fh:
        src = fh.read()
    contract = {}
    for kind, cfg_name in _KIND_TO_CONFIG.findall(src):
        m = re.search(r"export interface " + cfg_name + r"\s*\{\n(.*?)\n\}", src, re.S)
        if not m:
            if on_error:
                on_error(f"widget contract: no interface {cfg_name} for kind {kind!r}")
            continue
        body = _drop_nested(re.sub(r"//[^\n]*", "", m.group(1)))
        fields = {}
        for name, optional, ty in _FIELD.findall(body):
            ty = ty.strip()
            literals = re.findall(r'"([^"]+)"', ty)
            enum = literals if literals and _STRING_UNION.fullmatch(ty) else None
            fields[name] = (optional == "", enum)
        contract[kind] = fields
    return contract


def config_problems(contract, kind, config):
    """Everything wrong with one widget step's config, as a list of strings.

    Returns [] for a step kind that carries no config (teach, tip, worked …),
    so callers can pass every step in without pre-filtering.
    """
    fields = contract.get(kind)
    if fields is None:
        return []
    if not isinstance(config, dict):
        return ["widget step has no config object"]
    problems = []
    for name, (required, enum) in fields.items():
        if required and name not in config:
            problems.append(f"config missing required key {name!r}")
        if enum and name in config and config[name] not in enum:
            problems.append(f"config[{name!r}] = {config[name]!r} is not one of {enum}")
    for name in config:
        if name not in fields:
            problems.append(
                f"config has unknown key {name!r} — the component ignores it, so the "
                f"widget silently renders a default"
            )
    return problems
