"use client";

import { type GeoDiagramSpec, type GeoPointSpec, type GeoObjectSpec } from "@/lib/genmath-interactive";

// The static geometry renderer — the drawing engine for the Geometry course.
// Takes a declarative spec (named points + segments/rays/lines/angle arcs) in
// abstract units (y up) and renders a clean SVG. Reused by:
//   - the "geo" figure mode (worked examples / try-its),
//   - GeoCanvas and the other geometry interactives, via the exported pieces.

export const GEO_ACCENT = "#e8913c";
export const GEO_BLUE = "#5b8def";

// ---------------------------------------------------------------------------
// Shared drawing pieces (exported for the interactive components)
// ---------------------------------------------------------------------------

// Arrowhead as a small polygon at (x, y) pointing along `deg` (SVG coords).
export function ArrowHead({ x, y, deg, color }: { x: number; y: number; deg: number; color: string }) {
  return (
    <polygon
      points="0,-3.6 8,0 0,3.6"
      transform={`translate(${x}, ${y}) rotate(${deg})`}
      fill={color}
    />
  );
}

// A labelled point dot.
export function PointDot({ x, y, label, dx = 0, dy = 0 }: { x: number; y: number; label?: string; dx?: number; dy?: number }) {
  return (
    <g>
      <circle cx={x} cy={y} r={3.4} fill="var(--fg)" />
      {label && (
        <text x={x + 7 + dx} y={y - 7 + dy} fontSize="13" fontStyle="italic" fontFamily="serif" fill="var(--fg)">
          {label}
        </text>
      )}
    </g>
  );
}

// SVG path for an arc of radius r at center (cx, cy) from angle a1 to a2
// (degrees, screen coords — y already flipped). Always the short way round.
export function arcPath(cx: number, cy: number, r: number, a1: number, a2: number): string {
  let d = a2 - a1;
  while (d < -180) d += 360;
  while (d > 180) d -= 360;
  const end = a1 + d;
  const rad = (v: number) => (v * Math.PI) / 180;
  const x1 = cx + r * Math.cos(rad(a1));
  const y1 = cy + r * Math.sin(rad(a1));
  const x2 = cx + r * Math.cos(rad(end));
  const y2 = cy + r * Math.sin(rad(end));
  const large = Math.abs(d) > 180 ? 1 : 0;
  const sweep = d > 0 ? 1 : 0;
  return `M ${x1} ${y1} A ${r} ${r} 0 ${large} ${sweep} ${x2} ${y2}`;
}

// Filled pie wedge for the same arc — used to wash a highlighted angle's
// interior so there is no ambiguity about WHICH angle is meant.
export function sectorPath(cx: number, cy: number, r: number, a1: number, a2: number): string {
  let d = a2 - a1;
  while (d < -180) d += 360;
  while (d > 180) d -= 360;
  const end = a1 + d;
  const rad = (v: number) => (v * Math.PI) / 180;
  const x1 = cx + r * Math.cos(rad(a1));
  const y1 = cy + r * Math.sin(rad(a1));
  const x2 = cx + r * Math.cos(rad(end));
  const y2 = cy + r * Math.sin(rad(end));
  const sweep = d > 0 ? 1 : 0;
  return `M ${cx} ${cy} L ${x1} ${y1} A ${r} ${r} 0 0 ${sweep} ${x2} ${y2} Z`;
}

// Congruence tick marks across the midpoint of a segment.
export function Ticks({ x1, y1, x2, y2, count, color }: { x1: number; y1: number; x2: number; y2: number; count: number; color: string }) {
  const mx = (x1 + x2) / 2;
  const my = (y1 + y2) / 2;
  const ang = Math.atan2(y2 - y1, x2 - x1);
  const px = Math.cos(ang + Math.PI / 2);
  const py = Math.sin(ang + Math.PI / 2);
  const ux = Math.cos(ang);
  const uy = Math.sin(ang);
  const marks = [];
  for (let i = 0; i < count; i++) {
    const off = (i - (count - 1) / 2) * 5;
    marks.push(
      <line
        key={i}
        x1={mx + ux * off - px * 5}
        y1={my + uy * off - py * 5}
        x2={mx + ux * off + px * 5}
        y2={my + uy * off + py * 5}
        stroke={color}
        strokeWidth={1.6}
      />
    );
  }
  return <>{marks}</>;
}

// ---------------------------------------------------------------------------
// The static diagram
// ---------------------------------------------------------------------------

// Spec authors write "accent"/"blue" as semantic colors; anything else is a
// raw CSS color passed to the SVG stroke.
function resolveColor(c: string | undefined, fallback: string): string {
  if (!c) return fallback;
  if (c === "accent") return GEO_ACCENT;
  if (c === "blue") return GEO_BLUE;
  return c;
}

export default function GeoDiagram({ spec }: { spec: GeoDiagramSpec }) {
  const { points, objects, hidePoints = [], height = 200 } = spec;
  // entrance choreography timing: each object draws in ~0.1s after the last;
  // point dots and labels pop once the strokes are on screen
  const delay = (i: number, extra = 0) => ({ animationDelay: `${(i * 0.1 + extra).toFixed(2)}s` } as React.CSSProperties);
  const dotDelay = objects.length * 0.1 + 0.15;
  const byId = new Map(points.map((p) => [p.id, p]));
  const get = (id: string): GeoPointSpec => byId.get(id) ?? { id, x: 0, y: 0 };

  // Bounding box in diagram units, padded.
  const xs = points.map((p) => p.x);
  const ys = points.map((p) => p.y);
  const minX = Math.min(...xs) - 1.2;
  const maxX = Math.max(...xs) + 1.2;
  const minY = Math.min(...ys) - 1.2;
  const maxY = Math.max(...ys) + 1.2;

  const W = 320;
  const scale = Math.min(W / (maxX - minX), height / (maxY - minY));
  const H = Math.min(height, (maxY - minY) * scale + 8);

  // diagram units (y up) -> svg px (y down)
  const px = (x: number) => (x - minX) * scale;
  const py = (y: number) => H - (y - minY) * scale;

  // Direction of ray at->through, in SVG degrees.
  const dirDeg = (at: GeoPointSpec, through: GeoPointSpec) =>
    (Math.atan2(py(through.y) - py(at.y), px(through.x) - px(at.x)) * 180) / Math.PI;

  // Figure centroid in screen px — side labels sit on the side of their
  // segment that faces AWAY from it, i.e. outside the figure.
  const cxAll = points.reduce((s, p) => s + px(p.x), 0) / Math.max(points.length, 1);
  const cyAll = points.reduce((s, p) => s + py(p.y), 0) / Math.max(points.length, 1);

  const sideLabel = (x1: number, y1: number, x2: number, y2: number, label: string, color: string, i: number) => {
    const len = Math.hypot(x2 - x1, y2 - y1);
    if (len < 1) return null;
    const mx = (x1 + x2) / 2;
    const my = (y1 + y2) / 2;
    let nx = -(y2 - y1) / len;
    let ny = (x2 - x1) / len;
    if (nx * (mx - cxAll) + ny * (my - cyAll) < 0) {
      nx = -nx;
      ny = -ny;
    }
    return (
      <text
        className="gm-fade"
        style={delay(i, 0.3)}
        x={mx + nx * 13}
        y={my + ny * 13 + 4}
        fontSize="12.5"
        textAnchor="middle"
        fontFamily="serif"
        fill={color}
      >
        {label}
      </text>
    );
  };

  const renderObject = (o: GeoObjectSpec, i: number) => {
    if (o.kind === "angle") {
      const at = get(o.at);
      const a1 = dirDeg(at, get(o.from));
      const a2 = dirDeg(at, get(o.to));
      const color = resolveColor(o.color, GEO_ACCENT);
      const r = (o.radius ?? 0.8) * scale;
      if (o.right) {
        // small square corner
        const rad = (v: number) => (v * Math.PI) / 180;
        const s = Math.min(r, 14);
        const u1 = { x: Math.cos(rad(a1)), y: Math.sin(rad(a1)) };
        const u2 = { x: Math.cos(rad(a2)), y: Math.sin(rad(a2)) };
        const c = { x: px(at.x), y: py(at.y) };
        const p1 = { x: c.x + u1.x * s, y: c.y + u1.y * s };
        const p2 = { x: c.x + (u1.x + u2.x) * s, y: c.y + (u1.y + u2.y) * s };
        const p3 = { x: c.x + u2.x * s, y: c.y + u2.y * s };
        return <path key={i} className="gm-arc-sweep" pathLength={1} style={delay(i)} d={`M ${p1.x} ${p1.y} L ${p2.x} ${p2.y} L ${p3.x} ${p3.y}`} fill="none" stroke={color} strokeWidth={1.6} />;
      }
      // label position: middle of the arc, a bit outside
      let d = a2 - a1;
      while (d < -180) d += 360;
      while (d > 180) d -= 360;
      const mid = ((a1 + a1 + d) / 2 * Math.PI) / 180;
      return (
        <g key={i}>
          <path className="gm-arc-sweep" pathLength={1} style={delay(i)} d={arcPath(px(at.x), py(at.y), Math.min(r, 22), a1, a2)} fill="none" stroke={color} strokeWidth={1.8} />
          {o.label && (
            <text
              className="gm-fade"
              style={delay(i, 0.3)}
              x={px(at.x) + Math.cos(mid) * (Math.min(r, 22) + 11)}
              y={py(at.y) + Math.sin(mid) * (Math.min(r, 22) + 11) + 4}
              fontSize="11"
              textAnchor="middle"
              fill={color}
            >
              {o.label}
            </text>
          )}
        </g>
      );
    }

    const from = get(o.from);
    const to = get(o.to);
    const color = resolveColor(o.color, "var(--fg-1)");
    const x1 = px(from.x), y1 = py(from.y), x2 = px(to.x), y2 = py(to.y);
    const dash = o.dashed ? "5 4" : undefined;
    const labelColor = o.color ? color : "var(--fg)";

    if (o.kind === "segment") {
      return (
        <g key={i}>
          {dash
            ? <line className="gm-fade" style={delay(i)} x1={x1} y1={y1} x2={x2} y2={y2} stroke={color} strokeWidth={2} strokeDasharray={dash} />
            : <line className="gm-arc-sweep" pathLength={1} style={delay(i)} x1={x1} y1={y1} x2={x2} y2={y2} stroke={color} strokeWidth={2} />}
          {o.ticks ? <g className="gm-fade" style={delay(i, 0.3)}><Ticks x1={x1} y1={y1} x2={x2} y2={y2} count={o.ticks} color={color} /></g> : null}
          {o.label ? sideLabel(x1, y1, x2, y2, o.label, labelColor, i) : null}
        </g>
      );
    }
    if (o.kind === "ray") {
      const deg = dirDeg(from, to);
      // arrowhead sits just inside the viewBox edge — draw at `to` extended a bit
      const ax = x2 + Math.cos((deg * Math.PI) / 180) * 26;
      const ay = y2 + Math.sin((deg * Math.PI) / 180) * 26;
      return (
        <g key={i}>
          {dash
            ? <line className="gm-fade" style={delay(i)} x1={x1} y1={y1} x2={ax} y2={ay} stroke={color} strokeWidth={2} strokeDasharray={dash} />
            : <line className="gm-arc-sweep" pathLength={1} style={delay(i)} x1={x1} y1={y1} x2={ax} y2={ay} stroke={color} strokeWidth={2} />}
          <g className="gm-fade" style={delay(i, 0.25)}><ArrowHead x={ax} y={ay} deg={deg} color={color} /></g>
          {o.label ? sideLabel(x1, y1, x2, y2, o.label, labelColor, i) : null}
        </g>
      );
    }
    // line: extend both directions with arrowheads
    const degF = dirDeg(from, to);
    const ax2 = x2 + Math.cos((degF * Math.PI) / 180) * 26;
    const ay2 = y2 + Math.sin((degF * Math.PI) / 180) * 26;
    const ax1 = x1 - Math.cos((degF * Math.PI) / 180) * 26;
    const ay1 = y1 - Math.sin((degF * Math.PI) / 180) * 26;
    return (
      <g key={i}>
        {dash
          ? <line className="gm-fade" style={delay(i)} x1={ax1} y1={ay1} x2={ax2} y2={ay2} stroke={color} strokeWidth={2} strokeDasharray={dash} />
          : <line className="gm-arc-sweep" pathLength={1} style={delay(i)} x1={ax1} y1={ay1} x2={ax2} y2={ay2} stroke={color} strokeWidth={2} />}
        <g className="gm-fade" style={delay(i, 0.25)}><ArrowHead x={ax2} y={ay2} deg={degF} color={color} /></g>
        <g className="gm-fade" style={delay(i, 0.25)}><ArrowHead x={ax1} y={ay1} deg={degF + 180} color={color} /></g>
        {o.label ? sideLabel(x1, y1, x2, y2, o.label, labelColor, i) : null}
      </g>
    );
  };

  return (
    <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340 }} role="img" aria-label="Geometry diagram">
      {objects.map(renderObject)}
      {points
        .filter((p) => !hidePoints.includes(p.id) && p.label !== "")
        .map((p) => (
          <g key={p.id} className="gm-fade" style={{ animationDelay: `${dotDelay.toFixed(2)}s` }}>
            <PointDot x={px(p.x)} y={py(p.y)} label={p.label ?? p.id} dx={(p.labelDx ?? 0) * scale * 0.1} dy={-(p.labelDy ?? 0) * scale * 0.1} />
          </g>
        ))}
    </svg>
  );
}
