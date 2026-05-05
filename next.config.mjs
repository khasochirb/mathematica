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
      // /practice/esh/previous-years folded into /practice/esh/test?type=previous
      // during the ЭЕШ Hub IA refactor. 301 (permanent: true) because the route
      // is gone for good — preserves any external bookmarks / search links.
      {
        source: "/practice/esh/previous-years",
        destination: "/practice/esh/test?type=previous",
        permanent: true,
      },
    ];
  },
};

export default nextConfig;
