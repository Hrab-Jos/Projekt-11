const path = require('path');

module.exports = {
  entry: './react/index.js',
  mode: 'production',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'static'),
  },
    module: {
      rules: [
        {
          test: /\.jsx?$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader",
            options: {
              cacheDirectory: true,
              cacheCompression: false,
            }
          }
        }
      ]
    },
    resolve: {
      extensions: [".js", ".jsx"]
     }
};