import { defineConfig } from "vitest/config";
import path from "node:path";

export default defineConfig({
  test: {
    // Node env by default. Tests that need DOM should set
    //   /** @vitest-environment jsdom */
    // at the top of the file.
    environment: "node",
    include: ["scripts/**/*.test.ts", "lib/**/*.test.ts"],
    reporters: ["default"],
  },
  // tsconfig sets jsx: "preserve" for Next; tests that server-render TSX
  // components (scripts/verify-primary-figures.test.ts) need it compiled.
  // vitest 4 runs on rolldown-vite, whose transformer is oxc, not esbuild.
  oxc: {
    jsx: { runtime: "automatic" },
  },
  resolve: {
    // Mirror the tsconfig "@/" alias so imports in tests match app code.
    alias: {
      "@": path.resolve(__dirname, "."),
    },
  },
});
