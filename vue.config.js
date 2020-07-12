module.exports = {
  devServer: {
    proxy: {
      '/api*': {
        // Forward frontend dev server request for /api to flask dev server
        target: 'http://localhost:5000/'
      }
    }
  },
  publicPath: process.env.NODE_ENV === 'production'
    ? '/eternity/'
    : '/'
}