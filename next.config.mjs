/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [],
  },
  async redirects() {
    return [
      { source: "/ai", destination: "/practice", permanent: false },
      { source: "/ai/:path*", destination: "/practice", permanent: false },
      { source: "/progress", destination: "/dashboard", permanent: false },
      { source: "/progress/:path*", destination: "/dashboard", permanent: false },
      { source: "/upgrade", destination: "/", permanent: false },
      { source: "/upgrade/:path*", destination: "/", permanent: false },
    ];
  },
};

export default nextConfig;
