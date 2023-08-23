const path = require('path');

module.exports = {
    target: 'node',
    entry: './hexin-v.wencai',
    output: {
      filename: 'hexin-v.bundle.wencai',
      path: __dirname,
    },
    externals: {
      'canvas': 'commonjs canvas'
    },
    optimization: {
      minimize: false
    },
    node: {
      __dirname: false,
      __filename: false,
    }
  };
