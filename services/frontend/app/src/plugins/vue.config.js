// vue.config.js

const webpack = require('./webpack');

module.exports = {

    publicPath: process.env.NODE_ENV === 'production' ? '/public/' : '/',
    chainWebpack: config => {
        config.resolve.alias.set('vue$', 'vue/dist/vue.runtime.esm.js');
        config.module
            .rule('svg')
            .use('file-loader')
            .loader('file-loader')
            .tap(options => {
                // Modify the options as needed
                return options;
            });
    },
    css: {
        loaderOptions: {
            scss: {
                additionalData: `
                    @import "@/styles/variables.scss";
                    @import "@/styles/mixins.scss";
                `,
            },
        },
    },
    configureWebpack: {
        plugins: [
            // Other plugins
            new webpack.ProvidePlugin({
                process: 'process/browser',
                Buffer: ['buffer', 'Buffer'],
            }),
        ],
        resolve: {
            fallback: {
                "crypto": require.resolve("crypto-browserify"),
                "stream": require.resolve('stream-browserify'),
                "buffer": require.resolve("buffer/"),
            },

            alias: {
                'bitcoinjs-lib': 'bitcoinjs-lib', // Adjust the path based on your project structure
            },
        }
    }
};


// This configuration will ensure that Vue 3 is used as the runtime-only build in your project, which is what you want when working with Vue 3.

// Make sure that you've also updated your project to use Vue 3 and BootstrapVue for Vue 3 as mentioned in the previous responses to ensure compatibility.