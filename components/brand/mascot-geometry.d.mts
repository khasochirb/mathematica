// Types for the shared mascot geometry module (see mascot-geometry.mjs).
export const VIEWBOX: string;
export const MARK_VIEWBOX: string;
export const HEAD: { cx: number; cy: number; r: number };
export const RAY_WIDTH: number;
export type PoseName =
  | "idle"
  | "wave"
  | "celebrate"
  | "think"
  | "point"
  | "sleep"
  | "walk";
export const POSES: Record<PoseName, unknown>;
export const POSE_NAMES: PoseName[];
export function mascotMarkup(poseName: PoseName, color: string): string;
export function markMarkup(color: string): string;
