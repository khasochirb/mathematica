"""Figures for AA HL Practice Papers 1 & 2 (testId ib-hl-practice-3).

matplotlib from the SAME parameters as the builder scripts, pure
black-on-white line art (dark mode inverts), exact geometry, dpi=200,
tight bbox, <= 50 KB each.

Output: public/ib-figures/ib-aahl-p1-t3-q9.png   (region under x e^-x, 0..1)
        public/ib-figures/ib-aahl-p2-t3-q8.png   (region between y = x^2 and
                                                  y = 6x - x^2)
        public/ib-figures/ib-aahl-p2-t3-q9.png   (tide model d = 12 + 4 sin)
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


# ── P1 Q9: region R under y = x e^(-x) from x = 0 to x = 1 ──────────────
def p1_q9():
    # The maximum sits at x = 1 (f'(x) = (1-x)e^-x), so the shaded region
    # ends exactly at the peak — that is what makes the picture readable.
    assert abs((1 - 1) * math.exp(-1)) < 1e-12
    fig, ax = plt.subplots(figsize=(4.8, 3.0))
    xs = np.linspace(0, 4.0, 400)
    ys = xs * np.exp(-xs)
    ax.plot(xs, ys, color=BLACK, lw=1.6)
    xr = np.linspace(0, 1, 200)
    ax.fill_between(xr, xr * np.exp(-xr), color=LIGHT, edgecolor=BLACK,
                    lw=0.6, hatch="///")
    peak = 1 * math.exp(-1)
    ax.plot([1, 1], [0, peak], color=BLACK, lw=1.0)
    ax.text(1, -0.022, "$1$", ha="center", va="top", fontsize=12, color=BLACK)
    ax.text(0.55, 0.10, "$R$", ha="center", va="center", fontsize=13,
            color=BLACK)
    ax.text(2.3, 0.20, "$y = x\\mathrm{e}^{-x}$", ha="left", va="center",
            fontsize=12, color=BLACK)
    arrow_axes(ax, (-0.25, 4.3), (-0.06, 0.46))
    save(fig, "ib-aahl-p1-t3-q9.png")


# ── P2 Q8: region between y = x^2 and y = 6x - x^2 ─────────────────────
def p2_q8():
    # The curves meet where x^2 = 6x - x^2, i.e. at x = 0 and x = 3.
    assert 0 ** 2 == 6 * 0 - 0 ** 2 and 3 ** 2 == 6 * 3 - 3 ** 2
    fig, ax = plt.subplots(figsize=(4.6, 3.6))
    xs = np.linspace(-0.6, 4.0, 500)
    ax.plot(xs, xs ** 2, color=BLACK, lw=1.6)
    ax.plot(xs, 6 * xs - xs ** 2, color=BLACK, lw=1.6)
    xr = np.linspace(0, 3, 300)
    ax.fill_between(xr, xr ** 2, 6 * xr - xr ** 2, color=LIGHT,
                    edgecolor=BLACK, lw=0.6, hatch="///")
    for px, py, lab, dx, dy in [(0, 0, "$O$", -0.28, -0.9),
                                (3, 9, "$(3, 9)$", 0.15, 0.4)]:
        ax.plot([px], [py], "o", ms=4, color=BLACK)
        ax.text(px + dx, py + dy, lab, fontsize=12, color=BLACK)
    ax.text(3.5, 12.6, "$y = x^{2}$", fontsize=12, color=BLACK)
    ax.text(3.35, 5.0, "$y = 6x - x^{2}$", fontsize=12, color=BLACK)
    arrow_axes(ax, (-1.0, 5.2), (-2.0, 15.0))
    save(fig, "ib-aahl-p2-t3-q8.png")


# ── P2 Q9: harbour depth d(t) = 12 + 4 sin(pi t / 6) over 24 hours ──────
def p2_q9():
    # Period 12 h, max 16 m at t = 3, min 8 m at t = 9 — the values the
    # question asks for, so none of them is printed on the figure.
    assert abs((12 + 4 * math.sin(math.pi * 3 / 6)) - 16) < 1e-12
    fig, ax = plt.subplots(figsize=(5.4, 3.0))
    ts = np.linspace(0, 24, 600)
    ds = 12 + 4 * np.sin(np.pi * ts / 6)
    ax.plot(ts, ds, color=BLACK, lw=1.6)
    for gy in (8, 12, 16):
        ax.plot([0, 24], [gy, gy], color="0.85", lw=0.8, zorder=0)
        ax.text(-0.5, gy, str(gy), ha="right", va="center", fontsize=11,
                color=BLACK)
    for gt in (0, 6, 12, 18, 24):
        ax.plot([gt, gt], [5.9, 6.1], color=BLACK, lw=1.0)
        ax.text(gt, 5.6, str(gt), ha="center", va="top", fontsize=11,
                color=BLACK)
    ax.plot([0, 24.8], [6, 6], color=BLACK, lw=1.3)
    ax.plot([0, 0], [6, 17.6], color=BLACK, lw=1.3)
    ax.text(12, 4.7, "$t$ (hours after midnight)", ha="center", va="top",
            fontsize=12, color=BLACK)
    ax.text(-2.4, 12, "$d$ (metres)", rotation=90, va="center", fontsize=12,
            color=BLACK)
    ax.set_xlim(-3.2, 25.6)
    ax.set_ylim(4.2, 18.0)
    ax.axis("off")
    save(fig, "ib-aahl-p2-t3-q9.png")


if __name__ == "__main__":
    p1_q9()
    p2_q8()
    p2_q9()
