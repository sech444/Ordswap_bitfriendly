const path = require('path');
const NodePolyfillPlugin = require("node-polyfill-webpack-plugin");
const webpack = require('webpack');
const Dotenv = require('dotenv-webpack');
const stdLibBrowser = require('node-stdlib-browser');
const { NodeProtocolUrlPlugin } = require('node-stdlib-browser/helpers/webpack/plugin');


module.exports = {
    mode: 'development',
    target: "web",
    entry: '/vite.config.js',
    experiments: {
        asyncWebAssembly: true,
        buildHttp: {
            allowedUris: ['https://bitfriendly.me', 'https://www.bitfriendly.me', 'http://localhost'], // replace with your actual URI
        },
        layers: true,
        lazyCompilation: true,
        outputModule: true,
        syncWebAssembly: true,
        topLevelAwait: true,
    },
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist'),
    },
    module: {
        rules: [{
                test: /\.css$/i,
                use: ['style-loader', 'css-loader'],
            },
            {
                test: /\.wasm$/,
                type: 'webassembly/async',
            },
            {
                test: /\.js$/i,
                use: ['babel-loader'],
            },
            {
                test: /\.(png|svg|jpg|gif)$/i,
                type: 'asset/resource',
            },
            {
                test: /\.wasm$/,
                loader: 'wasm-loader',
            },
            {
                test: /\.wasm$/,
                type: "asset/inline",
            },
            {
                test: /\.m?js$/,
                resolve: {
                    fullySpecified: false,
                },
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                  compilerOptions: {
                    // Treat any tag with "jsx" prop as JSX
                     isCustomElement: tag => tag === 'jsx',
                  }
                }
              },
        ],
    },
    resolve: {
        modules: [path.resolve(__dirname, 'app'), 'node_modules'],
        fullySpecified: false,
        fallback: {
            "crypto": require.resolve('crypto-browserify'),
            "stream": require.resolve('stream-browserify'),
            "buffer": require.resolve("buffer/"),
            "path": require.resolve("path-browserify"),
        },
        alias: {
            'vue$': 'vue/dist/vue.esm-browser.js',
            'vue': '@vue/runtime-dom',
            '@': path.resolve(__dirname, 'src'),
            'fs': stdLibBrowser.fs,
            'path': stdLibBrowser.path,
            // add other aliases as needed
        },
        extensions: ['.tsx', '.ts', '.js', '.vue'],
    },
    plugins: [
        new NodePolyfillPlugin(),

        new NodeProtocolUrlPlugin(),
        new webpack.ProvidePlugin({
            process: 'process/browser',
            Buffer: 'buffer/',
        }),
    ]
};