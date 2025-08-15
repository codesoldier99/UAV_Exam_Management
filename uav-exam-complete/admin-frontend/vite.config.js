import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0',
    port: 3000,
    strictPort: true,
    cors: true,
    hmr: {
      host: '3000-ihtigz7469bhdlgh2ck6z-6532622b.e2b.dev',
      clientPort: 443,
      protocol: 'wss'
    },
    // Custom middleware to bypass host checking
    middlewareMode: false,
    fs: {
      strict: false
    }
  },
  define: {
    __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: false,
  },
  // Add this to handle the host checking
  appType: 'spa'
})