"""Figures for AA SL Practice Papers 1 & 2 (testId ib-practice-4).

matplotlib from the SAME parameters as the builder scripts, pure
black-on-white line art (dark mode inverts), exact geometry, dpi=200,
tight bbox, <= 50 KB each.

Output: public/ib-figures/ib-aasl-p1-t4-q7.png  (3-4-5 cuboid)
        public/ib-figures/ib-aasl-p1-t4-q9.png  (cubic x^3-3x^2+2x, shaded)
        public/ib-figures/ib-aasl-p2-t4-q3.png  (triangle, cosine rule)
        public/ib-figures/ib-aasl-p2-t4-q7.png  (sinusoidal model)
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


# ── P1 Q7: cuboid 3 (AB) x 4 (BC) x 5 (CG), oblique projection ──────────
def p1_q7():
    # base ABCD: A(0,0) B(3,0) C(3,4) D(0,4) in plan; oblique offset for depth
    dx, dy = 1.5, 1.1  # oblique shift for the "up/back" direction is height
    W, D, H = 3.0, 4.0, 5.0
    # 2D screen coords: x_screen = X + ox*Zdepth ; use simple isometric-ish
    ox, oy = 0.55, 0.42

    def P(X, Y, Z):
        return (X + ox * Y, Z + oy * Y)
    A = P(0, 0, 0); B = P(W, 0, 0); C = P(W, D, 0); Dd = P(0, D, 0)
    E = P(0, 0, H); Fp = P(W, 0, H); G = P(W, D, H); Hh = P(0, D, H)
    fig, ax = plt.subplots(figsize=(4.4, 4.0))

    def edge(p, q, style="-", lw=1.5):
        ax.plot([p[0], q[0]], [p[1], q[1]], style, color=BLACK, lw=lw)
    # visible edges
    for p, q in [(A, B), (B, C), (A, Dd), (A, E), (B, Fp), (C, G), (Dd, Hh),
                 (E, Fp), (Fp, G), (G, Hh), (E, Hh)]:
        edge(p, q)
    edge(C, Dd, style="--", lw=1.0)  # hidden base edge
    # diagonals
    edge(A, C, style="-", lw=1.3)   # base diagonal AC
    edge(A, G, style="-", lw=1.6)   # space diagonal AG
    labels = {"$A$": A, "$B$": B, "$C$": C, "$D$": Dd, "$E$": E, "$F$": Fp,
              "$G$": G, "$H$": Hh}
    offs = {"$A$": (-0.18, -0.22), "$B$": (0.08, -0.22), "$C$": (0.12, -0.05),
            "$D$": (-0.28, 0.0), "$E$": (-0.2, 0.1), "$F$": (0.1, 0.1),
            "$G$": (0.12, 0.08), "$H$": (-0.28, 0.08)}
    for t, p in labels.items():
        o = offs[t]
        ax.text(p[0] + o[0], p[1] + o[1], t, fontsize=12, color=BLACK)
    # side labels
    ax.text((A[0] + B[0]) / 2, A[1] - 0.28, "$3$", ha="center", va="top",
            fontsize=12, color=BLACK)
    ax.text((B[0] + C[0]) / 2 + 0.12, (B[1] + C[1]) / 2 - 0.12, "$4$",
            ha="left", va="center", fontsize=12, color=BLACK)
    ax.text(C[0] + 0.12, (C[1] + G[1]) / 2, "$5$", ha="left", va="center",
            fontsize=12, color=BLACK)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-0.8, W + ox * D + 0.9)
    ax.set_ylim(-0.8, H + oy * D + 0.7)
    save(fig, "ib-aasl-p1-t4-q7.png")


# ── P1 Q9: cubic y = x^3 - 3x^2 + 2x, region on [0, 2] shaded ───────────
def p1_q9():
    fig, ax = plt.subplots(figsize=(4.8, 3.2))
    xs = np.linspace(-0.35, 2.35, 500)
    ys = xs ** 3 - 3 * xs ** 2 + 2 * xs
    ax.plot(xs, ys, color=BLACK, lw=1.6)
    xa = np.linspace(0, 1, 120)
    ax.fill_between(xa, xa ** 3 - 3 * xa ** 2 + 2 * xa, color=LIGHT,
                    edgecolor=BLACK, lw=0.6, hatch="///")
    xb = np.linspace(1, 2, 120)
    ax.fill_between(xb, xb ** 3 - 3 * xb ** 2 + 2 * xb, color=LIGHT,
                    edgecolor=BLACK, lw=0.6, hatch="///")
    for xv in (0, 1, 2):
        ax.plot([xv], [0], "o", ms=4, color=BLACK)
        ax.text(xv, -0.12, f"${xv}$", ha="center", va="top", fontsize=12,
                color=BLACK)
    ax.text(1.7, 0.55, "$y = x^3 - 3x^2 + 2x$", ha="left", va="center",
            fontsize=12, color=BLACK)
    arrow_axes(ax, (-0.55, 2.55), (-0.55, 0.9))
    save(fig, "ib-aasl-p1-t4-q9.png")


# ── P2 Q3: triangle with AB = 7, AC = 9, angle A = 52 deg (cosine rule) ─
def p2_q3():
    A = np.array([0.0, 0.0])
    B = np.array([7.0, 0.0])
    th = math.radians(52.0)
    C = 9.0 * np.array([math.cos(th), math.sin(th)])
    fig, ax = plt.subplots(figsize=(4.4, 3.2))
    tri = np.array([A, B, C, A])
    ax.plot(tri[:, 0], tri[:, 1], color=BLACK, lw=1.5)
    arc = np.linspace(0, th, 60)
    ax.plot(1.3 * np.cos(arc), 1.3 * np.sin(arc), color=BLACK, lw=1.0)
    ax.text(1.7, 0.7, "$52^\\circ$", fontsize=12, color=BLACK)
    ax.text(-0.25, -0.05, "$A$", ha="right", va="top", fontsize=13, color=BLACK)
    ax.text(7.15, -0.05, "$B$", ha="left", va="top", fontsize=13, color=BLACK)
    ax.text(C[0] + 0.1, C[1] + 0.1, "$C$", ha="left", va="bottom",
            fontsize=13, color=BLACK)
    ax.text(3.5, -0.4, "$7$ cm", ha="center", va="top", fontsize=12, color=BLACK)
    mid = (A + C) / 2
    ax.text(mid[0] - 0.35, mid[1] + 0.2, "$9$ cm", ha="right", va="bottom",
            fontsize=12, color=BLACK)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.2, 8.2)
    ax.set_ylim(-1.2, 7.8)
    save(fig, "ib-aasl-p2-t4-q3.png")


# ── P2 Q7: temperature model T = 8 sin(pi/6 (t-3)) + 15, t in [0, 24] ───
def p2_q7():
    fig, ax = plt.subplots(figsize=(5.2, 3.0))
    ts = np.linspace(0, 24, 500)
    T = 8 * np.sin(math.pi / 6 * (ts - 3)) + 15
    ax.plot(ts, T, color=BLACK, lw=1.6)
    for gy in (7, 15, 23):
        ax.plot([0, 24], [gy, gy], color="0.8", lw=0.7, zorder=0)
        ax.text(-0.6, gy, str(gy), ha="right", va="center", fontsize=10,
                color=BLACK)
    for gx in (0, 6, 12, 18, 24):
        ax.text(gx, 4.6, str(gx), ha="center", va="top", fontsize=10,
                color=BLACK)
    ax.text(12, 1.8, "$t$ (hours)", ha="center", va="top", fontsize=12,
            color=BLACK)
    ax.text(-2.4, 15, "T (°C)", rotation=90, va="center",
            fontsize=12, color=BLACK)
    ax.set_xlim(-0.5, 25)
    ax.set_ylim(4, 25)
    ax.axis("off")
    ax.annotate("", xy=(25, 5.5), xytext=(0, 5.5),
                arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=1.1))
    ax.annotate("", xy=(0, 25), xytext=(0, 5.5),
                arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=1.1))
    save(fig, "ib-aasl-p2-t4-q7.png")


if __name__ == "__main__":
    p1_q7()
    p1_q9()
    p2_q3()
    p2_q7()
