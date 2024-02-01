// webpack.config.js

const path = require('path');
const NodePolyfillPlugin = require("node-polyfill-webpack-plugin");
const webpack = require('webpack');
const Dotenv = require('dotenv-webpack');
const stdLibBrowser = require('node-stdlib-browser');
const {
    NodeProtocolUrlPlugin
} = require('node-stdlib-browser/helpers/webpack/plugin');


module.exports = {
    target: "web",
    entry: './app/src/main.js',
    experiments: {
        asyncWebAssembly: true,
        buildHttp: true,
        layers: true,
        lazyCompilation: true,
        outputModule: true,
        syncWebAssembly: true,
        topLevelAwait: true,
    },
    node: {
        path: true,
        crypto: true,
        fs: 'empty',
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
                type: 'webassembly/async', // Set the module type for WebAssembly
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
                loader: 'wasm-loader'
            },
            {
                test: /\.wasm$/,
                type: "asset/inline",
            },
            {
                test: /\.m?js$/,
                resolve: {
                    fullySpecified: false
                }
            }
        ],
    },
    resolve: {
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
            'alias': 'stdLibBrowser',
            "crypto": require.resolve('crypto-browserify'),
            "stream": require.resolve('stream-browserify'),
            "buffer": require.resolve("buffer/"),
            "path": require.resolve("path-browserify"),
        },
        extensions: ['.tsx', '.ts', '.js', '.vue'],


        plugins: [

            new NodePolyfillPlugin(),
            new webpack.DefinePlugin({
                'process.env.NODE_ENV': JSON.stringify('production')
            }),

            new Dotenv({
                path: './.env',
            }),
            new NodeProtocolUrlPlugin(),
            new webpack.ProvidePlugin({
                process: stdLibBrowser.process,
                Buffer: [stdLibBrowser.buffer, 'Buffer']
            })
        ]
    }
}