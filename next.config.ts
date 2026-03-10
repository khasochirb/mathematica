import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  transpilePackages: ["@mathly/shared"],
  images: {
    remotePatterns: [],
  },
};

export default nextConfig;
