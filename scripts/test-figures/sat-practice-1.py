#!/usr/bin/env python3
"""
Figure generator for SAT Math Practice Test 1.

Rules per practice-test-authoring §8: monochrome black-on-white line art
(the site dark-mode inverts figures), EXACT geometry computed from the
same parameter values as the question stems in
scripts/test-builders/sat-practice-1.py, matplotlib only, dpi 200,
tight bbox, target ≤ 50 KB each. Output: public/sat-figures/*.png.

Run AFTER the builder verifies, then re-run the builder so it reads the
true pixel dimensions back via PIL.
"""

import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

REPO = Path(__file__).resolve().parent.parent.parent
OUT = REPO / "public" / "sat-figures"
OUT.mkdir(parents=True, exist_ok=True)

BLACK = "#000000"
plt.rcParams.update({
    "font.size": 13, "text.color": BLACK, "axes.edgecolor": BLACK,
    "axes.labelcolor": BLACK, "xtick.color": BLACK, "ytick.color": BLACK,
    "mathtext.default": "it",
})


def save(fig, name: str) -> None:
    path = OUT / f"{name}.png"
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    kb = path.stat().st_size / 1024
    flag = "" if kb <= 50 else "  << OVER 50KB"
    print(f"  {name}.png  {kb:.1f} KB{flag}")


def clean_axes(ax):
    ax.set_axis_off()
    ax.set_aspect("equal")


def graph_axes(ax, xlim, ylim, xticks=(), yticks=(), xnudge=None):
    """Axis pair with arrowheads through the origin, ticked values only.
    xnudge maps a tick value to a horizontal label offset, used to slide
    a label sideways when the curve passes through the tick."""
    xnudge = xnudge or {}
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("auto")
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.annotate("", xy=(xlim[1], 0), xytext=(xlim[0], 0),
                arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=1.2))
    ax.annotate("", xy=(0, ylim[1]), xytext=(0, ylim[0]),
                arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=1.2))
    ax.text(xlim[1], -0.04*(ylim[1]-ylim[0]), "$x$", ha="left", va="top")
    ax.text(0.015*(xlim[1]-xlim[0]), ylim[1], "$y$", ha="left", va="top")
    tick = 0.012 * (ylim[1] - ylim[0])
    for t in xticks:
        ax.plot([t, t], [-tick, tick], color=BLACK, lw=1)
        ax.text(t + xnudge.get(t, 0), -3.2*tick, str(t), ha="center",
                va="top", fontsize=12)
    tickx = 0.012 * (xlim[1] - xlim[0])
    for t in yticks:
        ax.plot([-tickx, tickx], [t, t], color=BLACK, lw=1)
        ax.text(-2.2*tickx, t, str(t), ha="right", va="center", fontsize=12)


def two_way_table(name, col_heads, row_heads, cells, title):
    """Pure line-art two-way table: rows × cols of ints, plus totals."""
    rows = [list(r) + [sum(r)] for r in cells]
    col_tot = [sum(c) for c in zip(*cells)] + [sum(sum(r) for r in cells)]
    heads = col_heads + ["Total"]
    labels = row_heads + ["Total"]
    # Per-column widths sized to the longest text in the column so long
    # headers ("Owns a dog", "30 or older") never overflow their cells.
    def w(texts):
        return max(1.3, 0.26 * max(len(str(t)) for t in texts) + 0.8)
    widths = [w(labels + [""])]
    for j, h in enumerate(heads):
        col_vals = [h] + [str(r[j]) for r in rows + [col_tot]]
        widths.append(w(col_vals))
    xs_edge = [0.0]
    for cw_ in widths:
        xs_edge.append(xs_edge[-1] + cw_)
    total_w = xs_edge[-1]
    n_c, n_r = len(widths), len(rows) + 2
    ch = 0.62
    fig, ax = plt.subplots(figsize=(total_w * 0.62, n_r * ch * 0.62 + 0.3))
    for i in range(n_r + 1):
        lw = 1.6 if i in (0, 1, n_r - 1, n_r) else 0.8
        ax.plot([0, total_w], [-i * ch, -i * ch], color=BLACK, lw=lw)
    for j in range(n_c + 1):
        lw = 1.6 if j in (0, 1, n_c) else 0.8
        ax.plot([xs_edge[j], xs_edge[j]], [0, -n_r * ch], color=BLACK, lw=lw)

    def put(r, c, text, bold=False):
        cx = (xs_edge[c] + xs_edge[c + 1]) / 2
        ax.text(cx, -(r + 0.5) * ch, text, ha="center",
                va="center", fontsize=13,
                fontweight="bold" if bold else "normal")

    for j, h in enumerate(heads):
        put(0, j + 1, h, bold=True)
    values = rows + [col_tot]
    for i, (lab, vals) in enumerate(zip(labels, values)):
        put(i + 1, 0, lab, bold=(lab == "Total"))
        for j, v in enumerate(vals):
            put(i + 1, j + 1, str(v))
    ax.text(0, 0.35, title, fontsize=13, fontweight="bold", ha="left")
    ax.set_xlim(-0.1, total_w + 0.1)
    ax.set_ylim(-n_r * ch - 0.1, 0.75)
    clean_axes(ax)
    save(fig, name)


# ── M1 Q5: right triangle, legs 9 and 12 ──────────────────────────────
def m1_q05():
    a, b = 12, 9                      # base 12, height 9 — exact legs
    fig, ax = plt.subplots(figsize=(4.4, 3.6))
    ax.plot([0, a, 0, 0], [0, 0, b, 0], color=BLACK, lw=1.6)
    s = 0.55                          # right-angle mark at the origin
    ax.plot([s, s, 0], [0, s, s], color=BLACK, lw=1.1)
    ax.text(a / 2, -0.45, "12", ha="center", va="top", fontsize=14)
    ax.text(-0.45, b / 2, "9", ha="right", va="center", fontsize=14)
    ax.set_xlim(-1.6, a + 0.8)
    ax.set_ylim(-1.4, b + 0.8)
    clean_axes(ax)
    save(fig, "sat-p1-m1-q05")


# ── M1 Q10: parabola y = x² − 6x + 5 ─────────────────────────────────
def m1_q10():
    fig, ax = plt.subplots(figsize=(4.6, 4.2))
    xs = np.linspace(-0.8, 6.8, 400)
    ax.plot(xs, xs**2 - 6*xs + 5, color=BLACK, lw=1.6)
    graph_axes(ax, (-2, 7.6), (-5.6, 8.5), xticks=(1, 3, 5), yticks=(-4, 5))
    ax.plot([3], [-4], "o", ms=4, color=BLACK)
    save(fig, "sat-p1-m1-q10")


# ── M1 Q11: dot plot, 11 values ───────────────────────────────────────
def m1_q11():
    data = {3: 2, 4: 3, 5: 2, 6: 3, 7: 0, 8: 1}   # 11 dots, matches stem
    assert sum(data.values()) == 11
    fig, ax = plt.subplots(figsize=(4.8, 2.6))
    ax.plot([2.5, 8.5], [0, 0], color=BLACK, lw=1.4)
    for v, n in data.items():
        ax.plot([v, v], [-0.06, 0.06], color=BLACK, lw=1.1)
        ax.text(v, -0.16, str(v), ha="center", va="top", fontsize=13)
        for i in range(n):
            ax.plot([v], [0.28 + 0.3 * i], "o", ms=7, color=BLACK)
    ax.text(5.5, -0.55, "Books read", ha="center", va="top", fontsize=13)
    ax.set_xlim(2.2, 8.8)
    ax.set_ylim(-0.85, 1.6)
    clean_axes(ax)
    ax.set_aspect("auto")
    save(fig, "sat-p1-m1-q11")


# ── M1 Q14: triangle with angles x, 2x, x+20 (=40, 80, 60: exact) ─────
def m1_q14():
    A, Bang, Cang = 40, 80, 60        # x = 40 → drawn to scale
    assert A + Bang + Cang == 180
    c = 6.0                            # AB along the base
    Apt, Bpt = np.array([0, 0]), np.array([c, 0])
    b_len = c * math.sin(math.radians(Bang)) / math.sin(math.radians(Cang))
    Cpt = Apt + b_len * np.array([math.cos(math.radians(A)),
                                  math.sin(math.radians(A))])
    fig, ax = plt.subplots(figsize=(4.8, 3.6))
    tri = np.array([Apt, Bpt, Cpt, Apt])
    ax.plot(tri[:, 0], tri[:, 1], color=BLACK, lw=1.6)
    ax.text(Apt[0] + 0.95, Apt[1] + 0.28, "$x°$", fontsize=14)
    ax.text(Bpt[0] - 1.55, Bpt[1] + 0.28, "$2x°$", fontsize=14)
    # apex label tucked inside the triangle along the angle bisector
    vCA = (Apt - Cpt) / np.linalg.norm(Apt - Cpt)
    vCB = (Bpt - Cpt) / np.linalg.norm(Bpt - Cpt)
    bis = vCA + vCB
    bis = bis / np.linalg.norm(bis)
    lab = Cpt + 1.55 * bis
    ax.text(lab[0], lab[1], "$(x + 20)°$", ha="center", va="center",
            fontsize=13)
    ax.set_xlim(-0.7, c + 0.7)
    ax.set_ylim(-0.6, Cpt[1] + 0.7)
    clean_axes(ax)
    save(fig, "sat-p1-m1-q14")


# ── M1 Q17: two-way table, travel by class ────────────────────────────
def m1_q17():
    two_way_table("sat-p1-m1-q17",
                  ["Bus", "Car", "Walk"], ["Junior", "Senior"],
                  [[28, 20, 12], [22, 23, 15]],
                  "Travel method, by class")


# ── M2E Q2: scatter + best fit y = 2.5x + 10, point (8, 26) ──────────
def m2e_q02():
    pts = [(1, 13.5), (2, 14), (3, 18.5), (4, 19), (5, 23.5), (6, 24),
           (7, 28.5), (8, 26), (9, 33.5), (10, 34)]
    fig, ax = plt.subplots(figsize=(4.6, 4.0))
    xs = np.linspace(0, 11, 2)
    ax.plot(xs, 2.5*xs + 10, color=BLACK, lw=1.4)
    for px, py in pts:
        ax.plot([px], [py], "o", ms=5, color=BLACK)
    graph_axes(ax, (-1.2, 12), (-4, 42), xticks=(2, 4, 6, 8, 10),
               yticks=(10, 20, 30, 40))
    save(fig, "sat-p1-m2e-q02")


# ── M2E Q5: rectangular prism 8 × 5 × 4 ───────────────────────────────
def m2e_q05():
    L, W, H = 8, 5, 4
    dx, dy = 0.42 * W, 0.30 * W       # oblique offset for depth
    fig, ax = plt.subplots(figsize=(4.8, 3.4))
    f = [(0, 0), (L, 0), (L, H), (0, H)]                     # front face
    g = [(p[0] + dx, p[1] + dy) for p in f]                  # back face
    for face in (f,):
        xs_, ys_ = zip(*(face + [face[0]]))
        ax.plot(xs_, ys_, color=BLACK, lw=1.6)
    for a, b in [(f[1], g[1]), (f[2], g[2]), (f[3], g[3])]:  # visible depth
        ax.plot([a[0], b[0]], [a[1], b[1]], color=BLACK, lw=1.6)
    ax.plot([g[1][0], g[2][0]], [g[1][1], g[2][1]], color=BLACK, lw=1.6)
    ax.plot([g[2][0], g[3][0]], [g[2][1], g[3][1]], color=BLACK, lw=1.6)
    for a, b in [(f[0], g[0]), (g[0], g[1]), (g[0], g[3])]:  # hidden edges
        ax.plot([a[0], b[0]], [a[1], b[1]], color=BLACK, lw=1.0, ls=(0, (4, 3)))
    ax.text(L/2, -0.4, "8", ha="center", va="top", fontsize=14)
    ax.text(L + dx/2 + 0.35, dy/2 - 0.30, "5", ha="left", fontsize=14)
    ax.text(-0.4, H/2, "4", ha="right", va="center", fontsize=14)
    ax.set_xlim(-1.2, L + dx + 1.0)
    ax.set_ylim(-1.1, H + dy + 0.6)
    clean_axes(ax)
    save(fig, "sat-p1-m2e-q05")


# ── M2E Q8: exterior angle 140°, remote interiors 85° and x° ─────────
def m2e_q08():
    intC, angA, angB = 40, 85, 55     # 140 exterior at C; 85 + 55 = 140
    assert intC + angA + angB == 180
    Apt = np.array([0.0, 0.0])
    Cpt = np.array([6.0, 0.0])
    Dpt = np.array([8.6, 0.0])        # extension beyond C
    # B: ray from A at 85° meets ray from C at 180 − 40 = 140°
    tA = math.tan(math.radians(angA))
    tC = math.tan(math.radians(180 - intC))
    xB = (tC * Cpt[0]) / (tC - tA)
    yB = tA * xB
    Bpt = np.array([xB, yB])
    fig, ax = plt.subplots(figsize=(5.2, 4.2))
    ax.plot([Apt[0], Dpt[0]], [0, 0], color=BLACK, lw=1.6)
    ax.plot([Apt[0], Bpt[0]], [Apt[1], Bpt[1]], color=BLACK, lw=1.6)
    ax.plot([Cpt[0], Bpt[0]], [Cpt[1], Bpt[1]], color=BLACK, lw=1.6)
    # angle arcs
    for ctr, th1, th2, r, label, lx, ly in [
            (Apt, 0, angA, 0.9, "$85°$", 1.35, 0.42),
            (Cpt, 180 - intC, 180, 0.8, "", 0, 0),
            (Cpt, 0, 180 - intC, 1.05, "$140°$", 1.6, 0.72),
            (Bpt, 0, 0, 0, "$x°$", 0, 0)]:
        if th2 > th1:
            th = np.linspace(math.radians(th1), math.radians(th2), 60)
            ax.plot(ctr[0] + r*np.cos(th), ctr[1] + r*np.sin(th),
                    color=BLACK, lw=1.0)
        if label == "$85°$":
            ax.text(ctr[0] + lx, ctr[1] + ly, label, fontsize=13)
        elif label == "$140°$":
            ax.text(ctr[0] + lx, ctr[1] + ly, label, fontsize=13)
    # x° label tucked inside angle B
    vBA = Apt - Bpt
    vBC = Cpt - Bpt
    bis = vBA / np.linalg.norm(vBA) + vBC / np.linalg.norm(vBC)
    bis = bis / np.linalg.norm(bis)
    ax.text(*(Bpt + 1.15 * bis), "$x°$", fontsize=13, ha="center")
    ax.set_xlim(-0.8, 9.2)
    ax.set_ylim(-0.7, yB + 0.7)
    clean_axes(ax)
    save(fig, "sat-p1-m2e-q08")


# ── M2E Q10: parabola y = −(x−2)² + 9 ────────────────────────────────
def m2e_q10():
    fig, ax = plt.subplots(figsize=(4.6, 4.2))
    xs = np.linspace(-1.7, 5.7, 400)
    ax.plot(xs, -(xs - 2)**2 + 9, color=BLACK, lw=1.6)
    graph_axes(ax, (-3, 6.6), (-5.5, 10.6), xticks=(-1, 2, 5),
               yticks=(5, 9), xnudge={-1: -0.35, 5: 0.35})
    ax.plot([2], [9], "o", ms=4, color=BLACK)
    save(fig, "sat-p1-m2e-q10")


# ── M2E Q14: circle, 60° sector hatched ───────────────────────────────
def m2e_q14():
    r = 6
    fig, ax = plt.subplots(figsize=(4.2, 4.2))
    th = np.linspace(0, 2 * math.pi, 400)
    ax.plot(r*np.cos(th), r*np.sin(th), color=BLACK, lw=1.6)
    a1, a2 = math.radians(20), math.radians(80)    # 60° sector
    A = np.array([r*math.cos(a1), r*math.sin(a1)])
    B = np.array([r*math.cos(a2), r*math.sin(a2)])
    wedge_th = np.linspace(a1, a2, 80)
    xs_ = np.concatenate([[0], r*np.cos(wedge_th), [0]])
    ys_ = np.concatenate([[0], r*np.sin(wedge_th), [0]])
    ax.fill(xs_, ys_, facecolor="none", edgecolor=BLACK, lw=1.4,
            hatch="///")
    ax.plot([0], [0], "o", ms=4, color=BLACK)
    ax.text(-0.25, -0.75, "$O$", fontsize=14)
    ax.text(A[0] + 0.35, A[1], "$A$", fontsize=14)
    ax.text(B[0] - 0.1, B[1] + 0.35, "$B$", fontsize=14)
    mid = math.radians(-130)
    ax.plot([0, r*math.cos(mid)], [0, r*math.sin(mid)], color=BLACK, lw=1.2)
    ax.text(r*math.cos(mid)/2 - 0.75, r*math.sin(mid)/2 - 0.15, "6",
            fontsize=14)
    lab = math.radians(50)
    ax.text(2.6*math.cos(lab) - 0.35, 2.6*math.sin(lab) - 0.20, "$60°$",
            fontsize=12)
    ax.set_xlim(-r - 1.2, r + 1.4)
    ax.set_ylim(-r - 1.2, r + 1.2)
    clean_axes(ax)
    save(fig, "sat-p1-m2e-q14")


# ── M2E Q17: two-way table, dog ownership by grade ────────────────────
def m2e_q17():
    two_way_table("sat-p1-m2e-q17",
                  ["Owns a dog", "Does not"], ["Grade 9", "Grade 10"],
                  [[18, 22], [25, 15]],
                  "Dog ownership, by grade")


# ── M2H Q2: scatter + best fit y = 4x + 20 ────────────────────────────
def m2h_q02():
    pts = [(1, 26), (2, 26), (3, 34), (4, 34), (5, 42), (6, 42),
           (7, 50), (8, 50), (9, 58), (10, 58)]
    fig, ax = plt.subplots(figsize=(4.6, 4.0))
    xs = np.linspace(0, 11.5, 2)
    ax.plot(xs, 4*xs + 20, color=BLACK, lw=1.4)
    for px, py in pts:
        ax.plot([px], [py], "o", ms=5, color=BLACK)
    graph_axes(ax, (-1.2, 12.6), (-7, 74), xticks=(2, 4, 6, 8, 10),
               yticks=(20, 40, 60))
    ax.text(6.2, -14.5, "Days", ha="center", fontsize=12)
    ax.text(-2.35, 33, "Height (mm)", rotation=90, va="center", fontsize=12)
    save(fig, "sat-p1-m2h-q02")


# ── M2H Q5: cylinder and cone, r = 3, h = 8 ───────────────────────────
def m2h_q05():
    r, h = 3, 8
    ry = 0.55                          # ellipse minor axis for perspective
    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    th = np.linspace(0, 2*math.pi, 200)
    # cylinder at x-center 0
    ax.plot(r*np.cos(th), h + ry*np.sin(th), color=BLACK, lw=1.4)
    half = np.linspace(math.pi, 2*math.pi, 100)
    ax.plot(r*np.cos(half), ry*np.sin(half), color=BLACK, lw=1.4)
    ax.plot(r*np.cos(half[::-1]), -ry*np.sin(half[::-1]), color=BLACK,
            lw=1.0, ls=(0, (4, 3)))
    ax.plot([-r, -r], [0, h], color=BLACK, lw=1.4)
    ax.plot([r, r], [0, h], color=BLACK, lw=1.4)
    ax.plot([0, r], [0, 0], color=BLACK, lw=1.1)
    ax.text(r/2, -0.85, "3", ha="center", fontsize=13)
    ax.plot([-r - 0.6, -r - 0.6], [0, h], color=BLACK, lw=0.9)
    ax.text(-r - 1.0, h/2, "8", ha="right", va="center", fontsize=13)
    # cone at x-center 9
    cx = 9
    apex = (cx, h)
    ax.plot(cx + r*np.cos(half), ry*np.sin(half), color=BLACK, lw=1.4)
    ax.plot(cx + r*np.cos(half[::-1]), -ry*np.sin(half[::-1]), color=BLACK,
            lw=1.0, ls=(0, (4, 3)))
    ax.plot([cx - r, apex[0]], [0, apex[1]], color=BLACK, lw=1.4)
    ax.plot([cx + r, apex[0]], [0, apex[1]], color=BLACK, lw=1.4)
    ax.plot([cx, cx + r], [0, 0], color=BLACK, lw=1.1)
    ax.text(cx + r/2, -0.85, "3", ha="center", fontsize=13)
    ax.plot([cx, cx], [0, h], color=BLACK, lw=0.9, ls=(0, (4, 3)))
    ax.text(cx + 0.25, h/2, "8", ha="left", va="center", fontsize=13)
    ax.set_xlim(-r - 2.2, cx + r + 1.0)
    ax.set_ylim(-1.7, h + 1.2)
    clean_axes(ax)
    save(fig, "sat-p1-m2h-q05")


# ── M2H Q8: triangle ABC with DE ∥ BC (ratio 1:3 exact) ──────────────
def m2h_q08():
    Bpt = np.array([0.0, 0.0])
    Cpt = np.array([7.8, 0.0])
    Apt = np.array([2.6, 5.7])
    Dpt = Apt + (Bpt - Apt) / 3        # AD/AB = 4/12 = 1/3 exact
    Ept = Apt + (Cpt - Apt) / 3
    fig, ax = plt.subplots(figsize=(4.8, 4.0))
    tri = np.array([Apt, Bpt, Cpt, Apt])
    ax.plot(tri[:, 0], tri[:, 1], color=BLACK, lw=1.6)
    ax.plot([Dpt[0], Ept[0]], [Dpt[1], Ept[1]], color=BLACK, lw=1.4)
    for p, lab, dx, dy in [(Apt, "$A$", 0, 0.35), (Bpt, "$B$", -0.42, -0.18),
                           (Cpt, "$C$", 0.30, -0.18), (Dpt, "$D$", -0.5, 0),
                           (Ept, "$E$", 0.42, 0)]:
        ax.text(p[0] + dx, p[1] + dy, lab, fontsize=14, ha="center")
    # label only lengths the statement references: AD = 4, DE = 6.
    # (AB = 12 is given in the text; DB is the classic trap, so it stays
    # unlabeled — the figure must not privilege either reading.)
    mAD = (Apt + Dpt) / 2
    ax.text(mAD[0] - 0.45, mAD[1], "4", fontsize=13, ha="right")
    mDE = (Dpt + Ept) / 2
    ax.text(mDE[0], mDE[1] + 0.3, "6", fontsize=13, ha="center")
    ax.set_xlim(-1.4, 8.8)
    ax.set_ylim(-0.9, 6.5)
    clean_axes(ax)
    save(fig, "sat-p1-m2h-q08")


# ── M2H Q10: parabola y = 2(x+1)(x−4) ────────────────────────────────
def m2h_q10():
    fig, ax = plt.subplots(figsize=(4.6, 4.4))
    xs = np.linspace(-2.1, 5.1, 400)
    ax.plot(xs, 2*(xs + 1)*(xs - 4), color=BLACK, lw=1.6)
    graph_axes(ax, (-3.4, 6.4), (-15.5, 14.5), xticks=(-1, 4),
               yticks=(-8,), xnudge={-1: -0.45, 4: 0.45})
    save(fig, "sat-p1-m2h-q10")


# ── M2H Q17: two-way table, survey by age ─────────────────────────────
def m2h_q17():
    two_way_table("sat-p1-m2h-q17",
                  ["Yes", "No"], ["Under 30", "30 or older"],
                  [[30, 50], [72, 48]],
                  "Survey response, by age group")


if __name__ == "__main__":
    print("generating SAT practice test 1 figures:")
    m1_q05(); m1_q10(); m1_q11(); m1_q14(); m1_q17()
    m2e_q02(); m2e_q05(); m2e_q08(); m2e_q10(); m2e_q14(); m2e_q17()
    m2h_q02(); m2h_q05(); m2h_q08(); m2h_q10(); m2h_q17()
    print("done — re-run the builder to embed true pixel dimensions.")
