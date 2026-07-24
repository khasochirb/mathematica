"""Figures for AA HL Practice Papers 1 & 2 (testId ib-hl-practice-2).

matplotlib from the SAME parameters as the builder scripts, pure
black-on-white line art (dark mode inverts), exact geometry, dpi=200,
tight bbox, <= 50 KB each.

Output: public/ib-figures/ib-aahl-p1-t2-q9.png   (region under x/sqrt(x^2+4))
        public/ib-figures/ib-aahl-p2-t2-q1.png   (triangle sides 8, 11, 15)
        public/ib-figures/ib-aahl-p2-t2-q9.png   (cylindrical can, r and h)
        public/ib-figures/ib-aahl-p2-t2-q10.png  (bearings P -> Q -> R)
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


# ── P1 Q9: region under y = x/sqrt(x^2+4), 0 <= x <= 2 sqrt(3) ───────────
def p1_q9():
    fig, ax = plt.subplots(figsize=(4.8, 3.0))
    xhi = 2 * math.sqrt(3)
    xs = np.linspace(0, 4.2, 400)
    ys = xs / np.sqrt(xs ** 2 + 4)
    ax.plot(xs, ys, color=BLACK, lw=1.6)
    xr = np.linspace(0, xhi, 200)
    ax.fill_between(xr, xr / np.sqrt(xr ** 2 + 4), color=LIGHT,
                    edgecolor=BLACK, lw=0.6, hatch="///")
    ax.plot([xhi, xhi], [0, xhi / math.sqrt(xhi ** 2 + 4)], color=BLACK, lw=1.0)
    ax.text(xhi, -0.06, "$2\\sqrt{3}$", ha="center", va="top", fontsize=12,
            color=BLACK)
    ax.text(1.4, 0.32, "$R$", ha="center", va="center", fontsize=13,
            color=BLACK)
    ax.text(3.2, 0.72, "$y = \\dfrac{x}{\\sqrt{x^2+4}}$", ha="left",
            va="center", fontsize=12, color=BLACK)
    arrow_axes(ax, (-0.4, 4.5), (-0.15, 1.0))
    save(fig, "ib-aahl-p1-t2-q9.png")


# ── P2 Q1: triangle with sides 8, 11, 15 ────────────────────────────────
def p2_q1():
    # place side of length 15 on the base from A(0,0) to B(15,0); C from the
    # two other sides: AC = 11, BC = 8.
    a, b, c = 8.0, 11.0, 15.0   # BC, AC, AB
    cx = (b ** 2 - a ** 2 + c ** 2) / (2 * c)
    cy = math.sqrt(max(b ** 2 - cx ** 2, 0))
    A = np.array([0.0, 0.0]); B = np.array([c, 0.0]); C = np.array([cx, cy])
    fig, ax = plt.subplots(figsize=(4.6, 3.0))
    tri = np.array([A, B, C, A])
    ax.plot(tri[:, 0], tri[:, 1], color=BLACK, lw=1.5)
    ax.text(-0.35, -0.05, "$A$", ha="right", va="top", fontsize=13, color=BLACK)
    ax.text(c + 0.2, -0.05, "$B$", ha="left", va="top", fontsize=13, color=BLACK)
    ax.text(C[0], C[1] + 0.25, "$C$", ha="center", va="bottom", fontsize=13,
            color=BLACK)
    ax.text(c / 2, -0.35, "$15$", ha="center", va="top", fontsize=12,
            color=BLACK)
    mAC = (A + C) / 2
    ax.text(mAC[0] - 0.3, mAC[1] + 0.2, "$11$", ha="right", va="bottom",
            fontsize=12, color=BLACK)
    mBC = (B + C) / 2
    ax.text(mBC[0] + 0.3, mBC[1] + 0.2, "$8$", ha="left", va="bottom",
            fontsize=12, color=BLACK)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.2, c + 1.2)
    ax.set_ylim(-1.2, cy + 1.0)
    save(fig, "ib-aahl-p2-t2-q1.png")


# ── P2 Q9: cylindrical can with radius r and height h ───────────────────
def p2_q9():
    fig, ax = plt.subplots(figsize=(3.2, 4.0))
    rw, hh = 1.5, 3.4     # drawing proportions only (not to the exact scale)
    ell_h = 0.42
    # top and bottom ellipses
    th = np.linspace(0, 2 * math.pi, 200)
    ax.plot(rw * np.cos(th), hh + ell_h * np.sin(th), color=BLACK, lw=1.5)
    ax.plot(rw * np.cos(th), 0 + ell_h * np.sin(th), color=BLACK, lw=1.5)
    # sides
    ax.plot([-rw, -rw], [0, hh], color=BLACK, lw=1.5)
    ax.plot([rw, rw], [0, hh], color=BLACK, lw=1.5)
    # radius on the top
    ax.plot([0, rw], [hh, hh], color=BLACK, lw=1.0)
    ax.text(rw / 2, hh + 0.12, "$r$", ha="center", va="bottom", fontsize=13,
            color=BLACK)
    ax.plot([0], [hh], "o", ms=3, color=BLACK)
    # height
    ax.annotate("", xy=(rw + 0.5, hh), xytext=(rw + 0.5, 0),
                arrowprops=dict(arrowstyle="<|-|>", color=BLACK, lw=1.0))
    ax.text(rw + 0.65, hh / 2, "$h$", ha="left", va="center", fontsize=13,
            color=BLACK)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-rw - 0.5, rw + 1.3)
    ax.set_ylim(-ell_h - 0.4, hh + ell_h + 0.5)
    save(fig, "ib-aahl-p2-t2-q9.png")


# ── P2 Q10: bearings P -> Q (060, 20 km) -> R (130, 15 km) ──────────────
def p2_q10():
    P = np.array([0.0, 0.0])
    b1 = math.radians(60)   # bearing measured clockwise from North (y-axis)
    Q = P + 20 * np.array([math.sin(b1), math.cos(b1)])
    b2 = math.radians(130)
    R = Q + 15 * np.array([math.sin(b2), math.cos(b2)])
    fig, ax = plt.subplots(figsize=(4.4, 4.2))
    ax.plot([P[0], Q[0]], [P[1], Q[1]], color=BLACK, lw=1.6)
    ax.plot([Q[0], R[0]], [Q[1], R[1]], color=BLACK, lw=1.6)
    ax.plot([P[0], R[0]], [P[1], R[1]], color=BLACK, lw=1.0, ls="--")
    # North arrows at P and Q
    for X in (P, Q):
        ax.annotate("", xy=(X[0], X[1] + 6), xytext=(X[0], X[1]),
                    arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=1.0))
        ax.text(X[0], X[1] + 6.4, "N", ha="center", va="bottom", fontsize=10,
                color=BLACK)
    for X, name, off in [(P, "$P$", (-0.8, -1.2)), (Q, "$Q$", (0.6, 0.2)),
                         (R, "$R$", (0.6, -0.6))]:
        ax.text(X[0] + off[0], X[1] + off[1], name, fontsize=13, color=BLACK)
    ax.text((P[0] + Q[0]) / 2 - 1.2, (P[1] + Q[1]) / 2, "$20$", fontsize=12,
            color=BLACK)
    ax.text((Q[0] + R[0]) / 2 + 0.3, (Q[1] + R[1]) / 2, "$15$", fontsize=12,
            color=BLACK)
    ax.set_aspect("equal")
    ax.axis("off")
    xs = [P[0], Q[0], R[0]]; ys = [P[1], Q[1], R[1]]
    ax.set_xlim(min(xs) - 3, max(xs) + 4)
    ax.set_ylim(min(ys) - 3, max(ys) + 8)
    save(fig, "ib-aahl-p2-t2-q10.png")


if __name__ == "__main__":
    p1_q9()
    p2_q1()
    p2_q9()
    p2_q10()
