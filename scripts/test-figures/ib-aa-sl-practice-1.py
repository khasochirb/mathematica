"""Figures for AA SL Practice Papers 1 & 2 (testId ib-practice-1).

House rules (practice-test-authoring §8): matplotlib from the SAME parameters
as the builder scripts, pure black-on-white line art (dark mode inverts),
exact geometry, dpi=200, tight bbox, target <= 50 KB each.

Output: public/ib-figures/ib-aasl-p1-t1-q7.png   (triangle + sector)
        public/ib-figures/ib-aasl-p1-t1-q9.png   (cubic, shaded region R)
        public/ib-figures/ib-aasl-p2-t1-q4.png   (circle sector + segment)
        public/ib-figures/ib-aasl-p2-t1-q9.png   (x e^{-0.4x}, shaded area)
"""
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
    ax.text(xlim[1], -0.04 * (ylim[1] - ylim[0]), xlabel, ha="center",
            va="top", fontsize=13, color=BLACK)
    ax.text(0.02 * (xlim[1] - xlim[0]), ylim[1], ylabel, ha="left",
            va="center", fontsize=13, color=BLACK)


# ── P1 Q7: triangle ABC, sector centre A radius 5 (AB=8, AC=5, A=pi/3) ───
def p1_q7():
    AB, AC, angA = 8.0, 5.0, np.pi / 3          # same parameters as the builder
    A = np.array([0.0, 0.0])
    B = np.array([AB, 0.0])
    C = np.array([AC * np.cos(angA), AC * np.sin(angA)])
    D = np.array([AC, 0.0])                     # AD = 5 on [AB]

    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    ax.set_aspect("equal")
    ax.axis("off")

    # sector fill (light, hatched) then triangle edges on top
    th = np.linspace(0.0, angA, 200)
    sx = np.concatenate([[A[0]], AC * np.cos(th), [A[0]]])
    sy = np.concatenate([[A[1]], AC * np.sin(th), [A[1]]])
    ax.fill(sx, sy, facecolor=LIGHT, edgecolor=BLACK, lw=1.0, hatch="///")

    tri = np.array([A, B, C, A])
    ax.plot(tri[:, 0], tri[:, 1], color=BLACK, lw=1.6)

    # vertex labels
    ax.text(A[0] - 0.25, A[1] - 0.1, "$A$", fontsize=14, ha="right", va="top")
    ax.text(B[0] + 0.25, B[1] - 0.1, "$B$", fontsize=14, ha="left", va="top")
    ax.text(C[0], C[1] + 0.22, "$C$", fontsize=14, ha="center", va="bottom")
    ax.text(D[0] + 0.05, D[1] - 0.12, "$D$", fontsize=14, ha="center", va="top")

    # side labels — only the GIVEN lengths (never BC: it is a 'show that')
    ax.text((A[0] + B[0]) / 2, -0.55, "$8$ cm", fontsize=13, ha="center")
    mid_ac = (A + C) / 2
    ax.text(mid_ac[0] - 0.3, mid_ac[1] + 0.15, "$5$ cm", fontsize=13,
            ha="right", va="bottom", rotation=60)

    # angle mark at A
    tha = np.linspace(0.0, angA, 60)
    ax.plot(1.1 * np.cos(tha), 1.1 * np.sin(tha), color=BLACK, lw=1.0)
    ax.text(1.62 * np.cos(angA / 2), 1.62 * np.sin(angA / 2),
            r"$\frac{\pi}{3}$", fontsize=14, ha="center", va="center")

    ax.set_xlim(-1.0, 9.0)
    ax.set_ylim(-1.2, 5.2)
    save(fig, "ib-aasl-p1-t1-q7.png")


# ── P1 Q9: y = x^3 - 6x^2 + 9x with region R shaded on [0, 3] ────────────
def p1_q9():
    def f(t):
        return t**3 - 6 * t**2 + 9 * t

    xs = np.linspace(-0.55, 4.25, 500)
    fig, ax = plt.subplots(figsize=(6.0, 4.4))
    arrow_axes(ax, (-1.0, 4.7), (-3.2, 5.6))

    xr = np.linspace(0.0, 3.0, 300)
    ax.fill_between(xr, 0, f(xr), facecolor=LIGHT, edgecolor="none")
    ax.plot(xs, f(xs), color=BLACK, lw=1.8)
    ax.text(1.35, 1.15, "$R$", fontsize=15, ha="center", va="center")
    ax.text(-0.12, -0.15, "$O$", fontsize=13, ha="right", va="top")
    ax.text(3.9, 4.9, "$C$", fontsize=13, ha="center", va="center")
    save(fig, "ib-aasl-p1-t1-q9.png")


# ── P2 Q4: circle centre O, r = 6.4, sector angle 1.35 rad, segment ──────
def p2_q4():
    r, theta = 6.4, 1.35                        # same parameters as the builder
    O = np.array([0.0, 0.0])
    # symmetric about the x-axis for a balanced diagram
    a0, a1 = -theta / 2, theta / 2
    A = r * np.array([np.cos(a0), np.sin(a0)])
    B = r * np.array([np.cos(a1), np.sin(a1)])

    fig, ax = plt.subplots(figsize=(5.6, 4.6))
    ax.set_aspect("equal")
    ax.axis("off")

    # full circle, thin
    tc = np.linspace(0, 2 * np.pi, 400)
    ax.plot(r * np.cos(tc), r * np.sin(tc), color=BLACK, lw=0.9)

    # segment fill: region between chord AB and arc AB
    ts = np.linspace(a0, a1, 200)
    seg_x = np.concatenate([r * np.cos(ts), [A[0]]])
    seg_y = np.concatenate([r * np.sin(ts), [A[1]]])
    ax.fill(seg_x, seg_y, facecolor=LIGHT, edgecolor="none", hatch="///")

    # radii and chord
    ax.plot([O[0], A[0]], [O[1], A[1]], color=BLACK, lw=1.5)
    ax.plot([O[0], B[0]], [O[1], B[1]], color=BLACK, lw=1.5)
    ax.plot([A[0], B[0]], [A[1], B[1]], color=BLACK, lw=1.5)

    # labels
    ax.text(O[0] - 0.3, O[1], "$O$", fontsize=14, ha="right", va="center")
    ax.text(A[0] + 0.25, A[1] - 0.15, "$A$", fontsize=14, ha="left", va="top")
    ax.text(B[0] + 0.25, B[1] + 0.15, "$B$", fontsize=14, ha="left", va="bottom")
    mid = (O + A) / 2
    ax.text(mid[0] - 0.15, mid[1] - 0.35, "$6.4$ cm", fontsize=12,
            ha="center", va="top", rotation=np.degrees(a0))

    # angle mark
    ta = np.linspace(a0, a1, 60)
    ax.plot(1.15 * np.cos(ta), 1.15 * np.sin(ta), color=BLACK, lw=1.0)
    ax.text(1.85, 0.0, "$1.35$", fontsize=12, ha="left", va="center")

    ax.set_xlim(-7.4, 7.6)
    ax.set_ylim(-7.2, 7.2)
    save(fig, "ib-aasl-p2-t1-q4.png")


# ── P2 Q9: f(x) = x e^{-0.4x}, area shaded on [0, 5], dashed x = 5 ───────
def p2_q9():
    def f(t):
        return t * np.exp(-0.4 * t)             # same parameters as the builder

    xs = np.linspace(0.0, 7.6, 500)
    fig, ax = plt.subplots(figsize=(6.2, 4.0))
    arrow_axes(ax, (-0.7, 8.2), (-0.22, 1.25), ylabel="$y$")

    xr = np.linspace(0.0, 5.0, 300)
    ax.fill_between(xr, 0, f(xr), facecolor=LIGHT, edgecolor="none")
    ax.plot(xs, f(xs), color=BLACK, lw=1.8)
    ax.plot([5, 5], [0, f(5.0)], color=BLACK, lw=1.2, ls=(0, (5, 4)))
    ax.text(5.0, -0.05, "$5$", fontsize=13, ha="center", va="top")
    ax.text(-0.08, -0.05, "$O$", fontsize=13, ha="right", va="top")
    ax.text(6.9, 0.42, "$y = f(x)$", fontsize=13, ha="left", va="center")
    save(fig, "ib-aasl-p2-t1-q9.png")


if __name__ == "__main__":
    p1_q7()
    p1_q9()
    p2_q4()
    p2_q9()
