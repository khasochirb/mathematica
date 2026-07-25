"""Figures for AA HL Practice Papers 1 & 2 (testId ib-hl-practice-5).

matplotlib from the SAME parameters as the builder scripts, pure
black-on-white line art (dark mode inverts), exact geometry, dpi=200,
tight bbox, <= 50 KB each.

Output: public/ib-figures/ib-aahl-p1-t5-q9.png   (region under
                                                  x sqrt(4 - x^2), 0..2)
        public/ib-figures/ib-aahl-p2-t5-q8.png   (cost curve with its
                                                  minimum)
        public/ib-figures/ib-aahl-p2-t5-q9.png   (quadrilateral field
                                                  ABCD split by BD)
"""
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "public", "ib-figures")
os.makedirs(OUT, exist_ok=True)

BLACK, WHITE, LIGHT = "#000000", "#ffffff", "0.90"


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    kb = os.path.getsize(path) / 1024
    print(f"{name}: {kb:.1f} KB")
    assert kb <= 50, f"{name} exceeds 50 KB"


def arrow_axes(ax, xlim, ylim, xlabel="$x$", ylabel="$y$"):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    ax.annotate("", xy=(xlim[1], 0), xytext=(xlim[0], 0),
                arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=1.2))
    ax.annotate("", xy=(0, ylim[1]), xytext=(0, ylim[0]),
                arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=1.2))
    ax.text(xlim[1], -0.05 * (ylim[1] - ylim[0]), xlabel, ha="center",
            va="top", fontsize=13, color=BLACK)
    ax.text(0.02 * (xlim[1] - xlim[0]), ylim[1], ylabel, ha="left",
            va="center", fontsize=13, color=BLACK)


# ── P1 Q9: region under y = x sqrt(4 - x^2) from x = 0 to x = 2 ────────
def p1_q9():
    # The curve starts and ends on the axis (x = 0 and x = 2) and peaks at
    # x = sqrt(2) with y = 2 — the values parts (a) and (c) ask for, so
    # none of them is printed on the figure.
    assert abs(math.sqrt(2) * math.sqrt(4 - 2) - 2) < 1e-12
    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    xs = np.linspace(0, 2, 400)
    ys = xs * np.sqrt(np.clip(4 - xs ** 2, 0, None))
    ax.plot(xs, ys, color=BLACK, lw=1.6)
    ax.fill_between(xs, ys, color=LIGHT, edgecolor=BLACK, lw=0.6,
                    hatch="///")
    ax.text(2, -0.12, "$2$", ha="center", va="top", fontsize=12,
            color=BLACK)
    ax.text(1.05, 0.75, "$R$", ha="center", va="center", fontsize=13,
            color=BLACK)
    ax.text(1.35, 2.05, "$y = x\\sqrt{4 - x^{2}}$", ha="left", va="center",
            fontsize=12, color=BLACK)
    arrow_axes(ax, (-0.25, 3.4), (-0.28, 2.6))
    save(fig, "ib-aahl-p1-t5-q9.png")


# ── P2 Q8: average cost C(x) = 0.5x + 200/x + 8 with its minimum ──────
def p2_q8():
    # The minimum sits at x = 20 (C'(x) = 0.5 - 200/x^2), which is what
    # part (c) asks for, so the figure marks only the axes.
    assert abs(0.5 - 200 / 20 ** 2) < 1e-12
    fig, ax = plt.subplots(figsize=(5.0, 3.2))
    xs = np.linspace(4, 60, 500)
    ys = 0.5 * xs + 200 / xs + 8
    ax.plot(xs, ys, color=BLACK, lw=1.6)
    for gy in (20, 30, 40, 50):
        ax.plot([0, 62], [gy, gy], color="0.88", lw=0.8, zorder=0)
        ax.text(-1.2, gy, str(gy), ha="right", va="center", fontsize=11,
                color=BLACK)
    for gx in (10, 20, 30, 40, 50, 60):
        ax.plot([gx, gx], [-0.9, 0.9], color=BLACK, lw=1.0)
        ax.text(gx, -2.2, str(gx), ha="center", va="top", fontsize=11,
                color=BLACK)
    ax.plot([0, 64], [0, 0], color=BLACK, lw=1.3)
    ax.plot([0, 0], [0, 56], color=BLACK, lw=1.3)
    ax.text(32, -7.5, "$x$ (units produced, in hundreds)", ha="center",
            va="top", fontsize=12, color=BLACK)
    ax.text(-9.5, 30, "$C$ (dollars)", rotation=90, va="center",
            fontsize=12, color=BLACK)
    ax.set_xlim(-13, 66)
    ax.set_ylim(-11, 58)
    ax.axis("off")
    save(fig, "ib-aahl-p2-t5-q8.png")


# ── P2 Q9: quadrilateral field ABCD with the diagonal BD ──────────────
def p2_q9():
    # Triangle ABD has AB = 40, AD = 55, angle A = 62 degrees; triangle
    # BCD has BC = 45 and CD = 38.  BD is shared, so it is drawn as the
    # diagonal and only the four sides plus angle A are labelled.
    AB, AD, A_deg, BC, CD = 40.0, 55.0, 62.0, 45.0, 38.0
    th = math.radians(A_deg)
    BD = math.sqrt(AB ** 2 + AD ** 2 - 2 * AB * AD * math.cos(th))
    assert BD + BC > CD and BC + CD > BD          # triangle BCD is possible
    A = np.array([0.0, 0.0])
    D = np.array([AD, 0.0])
    B = np.array([AB * math.cos(th), AB * math.sin(th)])
    # place C on the far side of BD from A
    dBD = (D - B) / BD
    perp = np.array([dBD[1], -dBD[0]])
    tt = (BC ** 2 - CD ** 2 + BD ** 2) / (2 * BD)
    hh = math.sqrt(max(BC ** 2 - tt ** 2, 0))
    C = B + tt * dBD + hh * perp
    assert abs(np.linalg.norm(C - B) - BC) < 1e-9
    assert abs(np.linalg.norm(C - D) - CD) < 1e-9
    fig, ax = plt.subplots(figsize=(4.8, 3.8))
    quad = np.array([A, B, C, D, A])
    ax.plot(quad[:, 0], quad[:, 1], color=BLACK, lw=1.6)
    ax.plot([B[0], D[0]], [B[1], D[1]], color=BLACK, lw=1.1, ls="--")
    for P, lab, off in [(A, "$A$", (-3.5, -2.5)), (B, "$B$", (-4.5, 1.5)),
                        (C, "$C$", (1.5, 1.5)), (D, "$D$", (1.5, -2.5))]:
        ax.text(P[0] + off[0], P[1] + off[1], lab, fontsize=13, color=BLACK)
    for P, Q, lab, off in [(A, B, "$40$", (-4.5, 0)), (B, C, "$45$", (0, 2.5)),
                           (C, D, "$38$", (3.0, 0)), (A, D, "$55$", (0, -3.5))]:
        M = (P + Q) / 2
        ax.text(M[0] + off[0], M[1] + off[1], lab, ha="center", va="center",
                fontsize=12, color=BLACK)
    arc = np.linspace(0, th, 60)
    rr = 9.0
    ax.plot(rr * np.cos(arc), rr * np.sin(arc), color=BLACK, lw=1.0)
    ax.text(rr * 1.55 * math.cos(th / 2), rr * 1.55 * math.sin(th / 2),
            "$62^\\circ$", ha="center", va="center", fontsize=12,
            color=BLACK)
    ax.set_aspect("equal")
    ax.axis("off")
    xs = [A[0], B[0], C[0], D[0]]
    ys = [A[1], B[1], C[1], D[1]]
    ax.set_xlim(min(xs) - 9, max(xs) + 9)
    ax.set_ylim(min(ys) - 8, max(ys) + 8)
    save(fig, "ib-aahl-p2-t5-q9.png")


if __name__ == "__main__":
    p1_q9()
    p2_q8()
    p2_q9()
