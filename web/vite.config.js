import { defineConfig } from 'vite';
import solidPlugin from 'vite-plugin-solid';
import htmlPurge from 'vite-plugin-purgecss'


export default defineConfig({
  plugins: [solidPlugin(), htmlPurge()],
  server: {
    port: 3000,
  },
  build: {
    target: 'esnext',
  },
});
