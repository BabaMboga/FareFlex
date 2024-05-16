import withFonts from 'next-fonts';

const nextConfig = {
  webpack(config, options) {
    return config;
  }
};

export default withFonts(nextConfig);
