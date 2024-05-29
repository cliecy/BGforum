const path = require('path');

module.exports = {
    entry: '/src/index.ts',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js'
    },
    module: {
        rules: [
            {test: /\.ts$/, use: 'ts-loader'}
        ]
    },
    resolve: {
        extensions: ['.jsx', '.ts', '.tsx', '...']
    }
};