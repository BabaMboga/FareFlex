// postcss.config.mjs

import autoprefixer from 'autoprefixer';
import cssnano from 'cssnano';

export default {
  plugins: [
    autoprefixer,
    cssnano({
      preset: 'default',
    }),
  ],
};

module.exports = {};