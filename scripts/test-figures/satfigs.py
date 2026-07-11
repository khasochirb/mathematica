"""
satfigs — the SAT figure TOOL LIBRARY.

Parametric, exact-geometry matplotlib tools for practice-test figures.
A test's figure script should be nothing but calls into this module with
the SAME parameter values its builder script uses — that is what makes a
figure provably consistent with its stem. Add new tools here; never fork
per-test drawing code.

House rules (practice-test-authoring §8, enforced by convention here):
- Pure black-on-white line art (site dark mode inverts the image).
  Gridlines may use gray >= 0.85. No color, no alpha.
- Geometry is EXACT: every angle, length ratio, curve, and data mark is
  computed from the passed parameters, never sketched.
- save() targets <= 50 KB at dpi 200 and prints a warning past that.
- Label only what the stem references; NEVER print the answer.

Tool inventory (each returns nothing; writes public/sat-figures/<name>.png):
  graph_axes(ax, ...)        arrowed x/y axes with chosen tick labels
  scatter(...)               scatterplot, optional best-fit/overlay line
  lines_graph(...)           y = mx + b lines on a light grid (systems)
  curve_graph(...)           any y = f(x) curve(s) on arrowed axes
  value_table(...)           x / f(x) two-row table
  two_way_table(...)         categorical two-way table with totals
  bar_chart(...)             labeled category bars
  histogram(...)             touching frequency bars over a numeric axis
  box_plot(...)              five-number-summary box-and-whisker
  number_line(...)           inequality-solution ray with open/closed dot
  angle_pair(...)            angles on a straight line at a vertex
  transversal(...)           two parallel lines cut by a transversal
  inscribed_circle(...)      central + inscribed angle on a circle
  composite_area(...)        rectangle with a right triangle on top
  cylinder(...)              right circular cylinder with r/h labels
  right_triangle(...)        right triangle, optional angle mark + labels
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
GRID = "0.85"  # lightest allowed gray for gridlines
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


def clean_axes(ax, aspect="equal"):
    ax.set_axis_off()
    ax.set_aspect(aspect)


def graph_axes(ax, xlim, ylim, xticks=(), yticks=(), xnudge=None,
               xlabel="$x$", ylabel="$y$"):
    """Arrowed axes through the origin with ONLY the ticks the problem
    references. xnudge maps tick -> horizontal label offset for ticks a
    curve passes through."""
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
    ax.text(xlim[1], -0.04 * (ylim[1] - ylim[0]), xlabel, ha="left", va="top")
    ax.text(0.015 * (xlim[1] - xlim[0]), ylim[1], ylabel, ha="left", va="top")
    tick = 0.012 * (ylim[1] - ylim[0])
    for t in xticks:
        ax.plot([t, t], [-tick, tick], color=BLACK, lw=1)
        ax.text(t + xnudge.get(t, 0), -3.2 * tick, str(t), ha="center",
                va="top", fontsize=12)
    tickx = 0.012 * (xlim[1] - xlim[0])
    for t in yticks:
        ax.plot([-tickx, tickx], [t, t], color=BLACK, lw=1)
        ax.text(-2.2 * tickx, t, str(t), ha="right", va="center", fontsize=12)


def scatter(name, pts, line=None, xlim=None, ylim=None, xticks=(),
            yticks=(), xlabel=None, ylabel=None, figsize=(4.6, 4.0)):
    """Scatterplot. line=(m, b) overlays y = mx + b across the x-range.
    xlabel/ylabel are axis captions (e.g. "Days"), drawn outside."""
    fig, ax = plt.subplots(figsize=figsize)
    if line is not None:
        m, b = line
        xs = np.linspace(0, xlim[1] * 0.94, 2)
        ax.plot(xs, m * xs + b, color=BLACK, lw=1.4)
    for px, py in pts:
        ax.plot([px], [py], "o", ms=5, color=BLACK)
    graph_axes(ax, xlim, ylim, xticks=xticks, yticks=yticks)
    if xlabel:
        ax.text((xlim[0] + xlim[1]) / 2, ylim[0] - 0.02 * (ylim[1] - ylim[0]),
                xlabel, ha="center", va="top", fontsize=12)
    if ylabel:
        ax.text(xlim[0] - 0.06 * (xlim[1] - xlim[0]), (ylim[0] + ylim[1]) / 2,
                ylabel, rotation=90, va="center", fontsize=12)
    save(fig, name)


def lines_graph(name, lines, xlim, ylim, mark=None, figsize=(4.4, 4.4)):
    """Lines y = m x + b on a unit grid (for reading a system's solution).
    lines: list of (m, b). mark: (x, y) intersection dot."""
    fig, ax = plt.subplots(figsize=figsize)
    for gx in range(int(math.ceil(xlim[0])), int(xlim[1]) + 1):
        ax.plot([gx, gx], [ylim[0], ylim[1]], color=GRID, lw=0.7, zorder=0)
    for gy in range(int(math.ceil(ylim[0])), int(ylim[1]) + 1):
        ax.plot([xlim[0], xlim[1]], [gy, gy], color=GRID, lw=0.7, zorder=0)
    xs = np.linspace(xlim[0] + 0.3, xlim[1] - 0.3, 2)
    for m, b in lines:
        ax.plot(xs, m * xs + b, color=BLACK, lw=1.6, zorder=2)
    if mark:
        ax.plot([mark[0]], [mark[1]], "o", ms=6, color=BLACK, zorder=3)
    graph_axes(ax, xlim, ylim,
               xticks=range(int(math.ceil(xlim[0])) + 1, int(xlim[1])),
               yticks=range(int(math.ceil(ylim[0])) + 1, int(ylim[1])))
    ax.set_aspect("equal")
    save(fig, name)


def curve_graph(name, fns, xlim, ylim, xticks=(), yticks=(), marks=(),
                xnudge=None, figsize=(4.6, 4.2), samples=400):
    """One or more true-function curves y = f(x). fns: list of
    (callable, x_from, x_to). marks: points to dot."""
    fig, ax = plt.subplots(figsize=figsize)
    for fn, a, b in fns:
        xs = np.linspace(a, b, samples)
        ax.plot(xs, [fn(v) for v in xs], color=BLACK, lw=1.6)
    for mx, my in marks:
        ax.plot([mx], [my], "o", ms=4, color=BLACK)
    graph_axes(ax, xlim, ylim, xticks=xticks, yticks=yticks, xnudge=xnudge)
    save(fig, name)


def _table_grid(ax, widths, n_r, ch=0.62, heavy_rows=(), heavy_cols=()):
    xs_edge = [0.0]
    for w in widths:
        xs_edge.append(xs_edge[-1] + w)
    total_w = xs_edge[-1]
    for i in range(n_r + 1):
        lw = 1.6 if i in heavy_rows else 0.8
        ax.plot([0, total_w], [-i * ch, -i * ch], color=BLACK, lw=lw)
    for j in range(len(widths) + 1):
        lw = 1.6 if j in heavy_cols else 0.8
        ax.plot([xs_edge[j], xs_edge[j]], [0, -n_r * ch], color=BLACK, lw=lw)
    return xs_edge, total_w, ch


def _cell_w(texts):
    return max(1.3, 0.26 * max(len(str(t)) for t in texts) + 0.8)


def value_table(name, x_label, xs, y_label, ys, title=None):
    """Two-row function table: a header row of x-values and a row of
    f(x)-values, with row labels on the left."""
    assert len(xs) == len(ys)
    widths = [_cell_w([x_label, y_label])] + \
             [_cell_w([a, b]) for a, b in zip(xs, ys)]
    n_r = 2
    fig, ax = plt.subplots(figsize=(sum(widths) * 0.62, n_r * 0.62 * 0.62 + 0.55))
    xs_edge, total_w, ch = _table_grid(ax, widths, n_r,
                                       heavy_rows=(0, 1, 2), heavy_cols=(0, 1, len(widths)))

    def put(r, c, text, bold=False):
        cx = (xs_edge[c] + xs_edge[c + 1]) / 2
        ax.text(cx, -(r + 0.5) * ch, str(text), ha="center", va="center",
                fontsize=13, fontweight="bold" if bold else "normal")

    put(0, 0, x_label, bold=True)
    put(1, 0, y_label, bold=True)
    for j, (a, b) in enumerate(zip(xs, ys)):
        put(0, j + 1, a)
        put(1, j + 1, b)
    if title:
        ax.text(0, 0.35, title, fontsize=13, fontweight="bold", ha="left")
    ax.set_xlim(-0.1, total_w + 0.1)
    ax.set_ylim(-n_r * ch - 0.1, 0.75 if title else 0.25)
    clean_axes(ax)
    save(fig, name)


def two_way_table(name, col_heads, row_heads, cells, title):
    """Categorical two-way table with row/column totals computed here —
    the caller passes only the inner cells, so totals can never disagree."""
    rows = [list(r) + [sum(r)] for r in cells]
    col_tot = [sum(c) for c in zip(*cells)] + [sum(sum(r) for r in cells)]
    heads = col_heads + ["Total"]
    labels = row_heads + ["Total"]
    widths = [_cell_w(labels + [""])]
    for j, h in enumerate(heads):
        widths.append(_cell_w([h] + [str(r[j]) for r in rows + [col_tot]]))
    n_r = len(rows) + 2
    fig, ax = plt.subplots(figsize=(sum(widths) * 0.62, n_r * 0.62 * 0.62 + 0.3))
    xs_edge, total_w, ch = _table_grid(ax, widths, n_r,
                                       heavy_rows=(0, 1, n_r - 1, n_r),
                                       heavy_cols=(0, 1, len(widths)))

    def put(r, c, text, bold=False):
        cx = (xs_edge[c] + xs_edge[c + 1]) / 2
        ax.text(cx, -(r + 0.5) * ch, str(text), ha="center", va="center",
                fontsize=13, fontweight="bold" if bold else "normal")

    for j, h in enumerate(heads):
        put(0, j + 1, h, bold=True)
    for i, (lab, vals) in enumerate(zip(labels, rows + [col_tot])):
        put(i + 1, 0, lab, bold=(lab == "Total"))
        for j, v in enumerate(vals):
            put(i + 1, j + 1, v)
    ax.text(0, 0.35, title, fontsize=13, fontweight="bold", ha="left")
    ax.set_xlim(-0.1, total_w + 0.1)
    ax.set_ylim(-n_r * ch - 0.1, 0.75)
    clean_axes(ax)
    save(fig, name)


def bar_chart(name, categories, values, ylabel, ytick_step, title=None,
              figsize=(5.0, 3.4)):
    """Separated category bars (hollow, black outline) with light
    horizontal gridlines at each ytick so values are readable."""
    fig, ax = plt.subplots(figsize=figsize)
    top = max(values) * 1.15
    for gy in range(ytick_step, int(top) + 1, ytick_step):
        ax.plot([-0.55, len(categories) - 0.45], [gy, gy], color=GRID,
                lw=0.8, zorder=0)
        ax.text(-0.62, gy, str(gy), ha="right", va="center", fontsize=11)
    for i, v in enumerate(values):
        ax.bar(i, v, width=0.62, facecolor="white", edgecolor=BLACK,
               lw=1.4, zorder=2)
        ax.text(i, -top * 0.04, categories[i], ha="center", va="top",
                fontsize=12)
    ax.plot([-0.55, len(categories) - 0.45], [0, 0], color=BLACK, lw=1.4)
    ax.text(-1.15, top / 2, ylabel, rotation=90, va="center", fontsize=12)
    if title:
        ax.text(-0.55, top * 1.03, title, fontsize=13, fontweight="bold")
    ax.set_xlim(-1.35, len(categories) - 0.3)
    ax.set_ylim(-top * 0.16, top * 1.12)
    clean_axes(ax, aspect="auto")
    save(fig, name)


def histogram(name, starts, counts, xlabel, ylabel, ytick_step=1,
              figsize=(5.0, 3.4)):
    """Touching frequency bars: starts[i] labels the left edge of bar i;
    a final edge label of starts[-1]+width closes the axis. Bar width is
    the spacing of consecutive starts (must be uniform)."""
    w = starts[1] - starts[0]
    assert all(b - a == w for a, b in zip(starts, starts[1:]))
    fig, ax = plt.subplots(figsize=figsize)
    top = max(counts) * 1.15
    for gy in range(ytick_step, int(top) + 1, ytick_step):
        ax.plot([starts[0] - w * 0.3, starts[-1] + w * 1.3], [gy, gy],
                color=GRID, lw=0.8, zorder=0)
        ax.text(starts[0] - w * 0.45, gy, str(gy), ha="right", va="center",
                fontsize=11)
    for s, c in zip(starts, counts):
        ax.bar(s, c, width=w, align="edge", facecolor="white",
               edgecolor=BLACK, lw=1.4, zorder=2)
    for edge in list(starts) + [starts[-1] + w]:
        ax.text(edge, -top * 0.04, str(edge), ha="center", va="top",
                fontsize=12)
    ax.plot([starts[0] - w * 0.3, starts[-1] + w * 1.3], [0, 0],
            color=BLACK, lw=1.4)
    ax.text((starts[0] + starts[-1] + w) / 2, -top * 0.22, xlabel,
            ha="center", va="top", fontsize=12)
    ax.text(starts[0] - w * 1.05, top / 2, ylabel, rotation=90,
            va="center", fontsize=12)
    ax.set_xlim(starts[0] - w * 1.25, starts[-1] + w * 1.45)
    ax.set_ylim(-top * 0.34, top * 1.1)
    clean_axes(ax, aspect="auto")
    save(fig, name)


def box_plot(name, five, lo, hi, tick_step, xlabel, figsize=(5.2, 2.2)):
    """Box-and-whisker from an exact five-number summary
    (min, Q1, median, Q3, max) over a labeled number line."""
    mn, q1, med, q3, mx = five
    assert mn <= q1 <= med <= q3 <= mx
    fig, ax = plt.subplots(figsize=figsize)
    y, h = 0.55, 0.32
    ax.plot([q1, q3, q3, q1, q1], [y - h, y - h, y + h, y + h, y - h],
            color=BLACK, lw=1.5)
    ax.plot([med, med], [y - h, y + h], color=BLACK, lw=1.5)
    ax.plot([mn, q1], [y, y], color=BLACK, lw=1.3)
    ax.plot([q3, mx], [y, y], color=BLACK, lw=1.3)
    for wv in (mn, mx):
        ax.plot([wv, wv], [y - h * 0.55, y + h * 0.55], color=BLACK, lw=1.3)
    ax.plot([lo, hi], [0, 0], color=BLACK, lw=1.3)
    for t in range(lo, hi + 1, tick_step):
        ax.plot([t, t], [-0.035, 0.035], color=BLACK, lw=1)
        ax.text(t, -0.1, str(t), ha="center", va="top", fontsize=12)
    ax.text((lo + hi) / 2, -0.32, xlabel, ha="center", va="top", fontsize=12)
    ax.set_xlim(lo - tick_step * 0.6, hi + tick_step * 0.6)
    ax.set_ylim(-0.5, 1.05)
    clean_axes(ax, aspect="auto")
    save(fig, name)


def number_line(name, point, closed, direction, lo, hi, figsize=(5.2, 1.4)):
    """Inequality-solution graph: closed (filled) or open circle at
    `point`, ray toward direction "right" or "left"."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.annotate("", xy=(hi + 0.6, 0), xytext=(lo - 0.6, 0),
                arrowprops=dict(arrowstyle="<|-|>", color=BLACK, lw=1.2))
    for t in range(lo, hi + 1):
        ax.plot([t, t], [-0.05, 0.05], color=BLACK, lw=1)
        ax.text(t, -0.14, str(t), ha="center", va="top", fontsize=12)
    end = hi + 0.45 if direction == "right" else lo - 0.45
    ax.annotate("", xy=(end, 0.30), xytext=(point, 0.30),
                arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=2.2))
    face = BLACK if closed else "white"
    ax.plot([point], [0.30], "o", ms=10, markerfacecolor=face,
            markeredgecolor=BLACK, markeredgewidth=1.6, zorder=3)
    ax.set_xlim(lo - 1, hi + 1)
    ax.set_ylim(-0.4, 0.75)
    clean_axes(ax, aspect="auto")
    save(fig, name)


def angle_pair(name, known_deg, known_label, unknown_label, figsize=(4.8, 2.9)):
    """Two angles on a straight line: a ray from the vertex at the EXACT
    angle 180 - known_deg... no — the ray sits at `known_deg` from the
    positive x-axis is wrong for labeling; we draw the ray so the RIGHT
    side angle equals known_deg and the left side is its supplement."""
    theta = math.radians(known_deg)
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot([-4.6, 4.6], [0, 0], color=BLACK, lw=1.6)
    ax.plot([0, 3.8 * math.cos(theta)], [0, 3.8 * math.sin(theta)],
            color=BLACK, lw=1.6)
    for r, a1, a2 in [(0.85, 0, known_deg), (1.05, known_deg, 180)]:
        th = np.linspace(math.radians(a1), math.radians(a2), 60)
        ax.plot(r * np.cos(th), r * np.sin(th), color=BLACK, lw=1.0)
    mid_r = math.radians(known_deg / 2)
    ax.text(1.7 * math.cos(mid_r), 1.7 * math.sin(mid_r) - 0.12, known_label,
            ha="center", fontsize=13)
    mid_l = math.radians((known_deg + 180) / 2)
    ax.text(1.75 * math.cos(mid_l), 1.75 * math.sin(mid_l), unknown_label,
            ha="center", fontsize=13)
    ax.plot([0], [0], "o", ms=4, color=BLACK)
    ax.set_xlim(-4.9, 4.9)
    ax.set_ylim(-0.75, 4.0)
    clean_axes(ax)
    save(fig, name)


def transversal(name, top_label, bottom_label, slope_deg=62,
                figsize=(5.0, 3.6)):
    """Two horizontal parallel lines cut by a transversal. Labels go on
    the SAME-SIDE INTERIOR angles (right of the transversal): top_label
    at the upper line, bottom_label at the lower line."""
    t = math.radians(slope_deg)
    y_top, y_bot = 2.6, 0.0
    # transversal passes through (0, 0) on the bottom line
    x_top = y_top / math.tan(t)
    fig, ax = plt.subplots(figsize=figsize)
    for y in (y_top, y_bot):
        ax.plot([-4.4, 6.2], [y, y], color=BLACK, lw=1.5)
    ax.plot([-1.3 * math.cos(t) , x_top + 1.3 * math.cos(t)],
            [-1.3 * math.sin(t), y_top + 1.3 * math.sin(t)],
            color=BLACK, lw=1.5)
    ax.text(6.4, y_top, "$\\ell$", fontsize=13, va="center")
    ax.text(6.4, y_bot, "$m$", fontsize=13, va="center")
    # interior-right angle at the top line: between transversal-down and +x
    th_top = np.linspace(math.radians(slope_deg - 180), 0, 70)
    ax.plot(x_top + 0.8 * np.cos(th_top), y_top + 0.8 * np.sin(th_top),
            color=BLACK, lw=1.0)
    ax.text(x_top + 1.5, y_top - 0.75, top_label, fontsize=13, ha="center")
    # interior-right angle at the bottom line: between +x and transversal-up
    th_bot = np.linspace(0, math.radians(slope_deg), 70)
    ax.plot(0.8 * np.cos(th_bot), 0.8 * np.sin(th_bot), color=BLACK, lw=1.0)
    ax.text(1.05, y_bot + 0.55, bottom_label, fontsize=13, ha="left")
    ax.set_xlim(-4.7, 7.3)
    ax.set_ylim(-1.15, y_top + 1.25)
    clean_axes(ax)
    save(fig, name)


def inscribed_circle(name, central_deg, central_label, inscribed_label,
                     r=3.0, figsize=(4.4, 4.4)):
    """Circle with center O: central angle AOB = central_deg (marked) and
    inscribed angle ACB from a point C on the major arc (marked). The
    inscribed angle is exactly half the central angle by construction."""
    a1, a2 = 90 - central_deg / 2, 90 + central_deg / 2
    A = np.array([r * math.cos(math.radians(a1)), r * math.sin(math.radians(a1))])
    B = np.array([r * math.cos(math.radians(a2)), r * math.sin(math.radians(a2))])
    C = np.array([0, -r])
    fig, ax = plt.subplots(figsize=figsize)
    th = np.linspace(0, 2 * math.pi, 400)
    ax.plot(r * np.cos(th), r * np.sin(th), color=BLACK, lw=1.5)
    for P in (A, B):
        ax.plot([0, P[0]], [0, P[1]], color=BLACK, lw=1.3)
        ax.plot([C[0], P[0]], [C[1], P[1]], color=BLACK, lw=1.3)
    ax.plot([0], [0], "o", ms=4, color=BLACK)
    arc = np.linspace(math.radians(a1), math.radians(a2), 60)
    ax.plot(0.62 * np.cos(arc), 0.62 * np.sin(arc), color=BLACK, lw=1.0)
    ax.text(0, 1.05, central_label, ha="center", fontsize=12)
    # inscribed angle arc at C
    vA, vB = A - C, B - C
    angA = math.degrees(math.atan2(vA[1], vA[0]))
    angB = math.degrees(math.atan2(vB[1], vB[0]))
    lo_, hi_ = min(angA, angB), max(angA, angB)
    arc2 = np.linspace(math.radians(lo_), math.radians(hi_), 60)
    ax.plot(C[0] + 0.8 * np.cos(arc2), C[1] + 0.8 * np.sin(arc2),
            color=BLACK, lw=1.0)
    ax.text(C[0], C[1] + 1.12, inscribed_label, ha="center", fontsize=12)
    ax.text(-0.02, -0.42, "$O$", ha="center", fontsize=13)
    ax.text(A[0] + 0.28, A[1] + 0.18, "$B$", fontsize=13)
    ax.text(B[0] - 0.32, B[1] + 0.18, "$A$", fontsize=13)
    ax.text(C[0] + 0.05, C[1] - 0.5, "$C$", ha="center", fontsize=13)
    ax.set_xlim(-r - 1, r + 1)
    ax.set_ylim(-r - 1.3, r + 1.2)
    clean_axes(ax)
    save(fig, name)


def composite_area(name, rect_w, rect_h, tri_h, figsize=(4.6, 4.0)):
    """Rectangle rect_w x rect_h with a right triangle on its full top
    side (right angle at the top-right corner, height tri_h). Labels the
    three given dimensions; dashed interior top edge of the rectangle."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot([0, rect_w, rect_w, 0, 0],
            [0, 0, rect_h, rect_h, 0], color=BLACK, lw=1.6)
    # triangle: hypotenuse from top-left corner to apex above top-right
    ax.plot([0, rect_w], [rect_h, rect_h + tri_h], color=BLACK, lw=1.6)
    ax.plot([rect_w, rect_w], [rect_h, rect_h + tri_h], color=BLACK, lw=1.6)
    s = 0.4
    ax.plot([rect_w - s, rect_w - s, rect_w],
            [rect_h, rect_h + s, rect_h + s], color=BLACK, lw=1.0)
    ax.text(rect_w / 2, -0.35, str(rect_w), ha="center", va="top", fontsize=14)
    ax.text(-0.35, rect_h / 2, str(rect_h), ha="right", va="center", fontsize=14)
    ax.text(rect_w + 0.35, rect_h + tri_h / 2, str(tri_h), ha="left",
            va="center", fontsize=14)
    ax.set_xlim(-1.5, rect_w + 1.6)
    ax.set_ylim(-1.3, rect_h + tri_h + 0.6)
    clean_axes(ax)
    save(fig, name)


def cylinder(name, r_label, h_label, r=3.0, h=7.0, figsize=(3.4, 4.0)):
    """Right circular cylinder with base-radius and height labels.
    Pass r_label=None to omit the radius segment entirely (e.g. when the
    radius is what the student must find)."""
    ry = 0.5
    fig, ax = plt.subplots(figsize=figsize)
    th = np.linspace(0, 2 * math.pi, 200)
    ax.plot(r * np.cos(th), h + ry * np.sin(th), color=BLACK, lw=1.4)
    half = np.linspace(math.pi, 2 * math.pi, 100)
    ax.plot(r * np.cos(half), ry * np.sin(half), color=BLACK, lw=1.4)
    ax.plot(r * np.cos(half[::-1]), -ry * np.sin(half[::-1]), color=BLACK,
            lw=1.0, ls=(0, (4, 3)))
    ax.plot([-r, -r], [0, h], color=BLACK, lw=1.4)
    ax.plot([r, r], [0, h], color=BLACK, lw=1.4)
    if r_label:
        ax.plot([0, r], [0, 0], color=BLACK, lw=1.1)
        ax.text(r / 2, -0.85, r_label, ha="center", fontsize=13)
    ax.plot([-r - 0.6, -r - 0.6], [0, h], color=BLACK, lw=0.9)
    ax.text(-r - 1.0, h / 2, h_label, ha="right", va="center", fontsize=13)
    ax.set_xlim(-r - 2.2, r + 0.9)
    ax.set_ylim(-1.7, h + 1.1)
    clean_axes(ax)
    save(fig, name)


def right_triangle(name, base, height, base_label=None, height_label=None,
                   hyp_label=None, theta_at=None, theta_label="$\\theta$",
                   figsize=(4.6, 3.4)):
    """Right triangle with legs `base` (horizontal) and `height`
    (vertical, on the RIGHT side), right angle at bottom-right. Optional
    side labels and an angle mark at "bottom-left" (between base and
    hypotenuse) or "top" (between height and hypotenuse). Drawn to scale
    from the exact leg values."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot([0, base, base, 0], [0, 0, height, 0], color=BLACK, lw=1.6)
    s = min(base, height) * 0.09
    ax.plot([base - s, base - s, base], [0, s, s], color=BLACK, lw=1.0)
    if base_label:
        ax.text(base / 2, -height * 0.06, base_label, ha="center", va="top",
                fontsize=14)
    if height_label:
        ax.text(base + base * 0.03, height / 2, height_label, ha="left",
                va="center", fontsize=14)
    if hyp_label:
        ax.text(base / 2 - base * 0.06, height / 2 + height * 0.1, hyp_label,
                ha="right", va="bottom", fontsize=14)
    if theta_at == "bottom-left":
        ang = math.degrees(math.atan2(height, base))
        th = np.linspace(0, math.radians(ang), 50)
        rr = base * 0.18
        ax.plot(rr * np.cos(th), rr * np.sin(th), color=BLACK, lw=1.0)
        mid = math.radians(ang / 2)
        ax.text(rr * 1.75 * math.cos(mid), rr * 1.55 * math.sin(mid),
                theta_label, fontsize=13, ha="center", va="center")
    elif theta_at == "top":
        vdown = -90.0
        vhyp = math.degrees(math.atan2(-height, -base))
        th = np.linspace(math.radians(vhyp), math.radians(vdown), 50)
        rr = height * 0.2
        ax.plot(base + rr * np.cos(th), height + rr * np.sin(th),
                color=BLACK, lw=1.0)
        mid = math.radians((vhyp + vdown) / 2)
        ax.text(base + rr * 1.8 * math.cos(mid), height + rr * 1.8 * math.sin(mid),
                theta_label, fontsize=13, ha="center", va="center")
    ax.set_xlim(-base * 0.12, base * 1.18)
    ax.set_ylim(-height * 0.18, height * 1.12)
    clean_axes(ax)
    save(fig, name)
