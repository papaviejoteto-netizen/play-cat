// Use a Node adapter so server-side routes (+page.server.ts) and
// actions (form handlers) continue to work at runtime. If you
// plan to deploy to a serverless platform, consider using the
// matching adapter (e.g. @sveltejs/adapter-vercel / netlify).
import adapter from '@sveltejs/adapter-node';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://svelte.dev/docs/kit/integrations
	// for more information about preprocessors
	preprocess: vitePreprocess(),
	kit: { adapter: adapter() }
};

export default config;
