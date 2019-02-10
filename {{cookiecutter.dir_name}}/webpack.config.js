const webpack = require('webpack');
const path = require('path')

const config = {
    entry:  path.join(__dirname, '/{{cookiecutter.app_name}}/js/Index.jsx'),
    output: {
      path: path.join(__dirname, '/{{cookiecutter.app_name}}/static/js/'),
      filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
    module: {
        rules: [
          {
            test: /\.jsx?/,
            exclude: /node_modules/,
            use: 'babel-loader'
          }
        ]
    }
};

module.exports = config;
