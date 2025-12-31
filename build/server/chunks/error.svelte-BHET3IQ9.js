import { C as escape_html } from './context-DzB0Gc18.js';
import { p as page } from './index3-CUiBG-V_.js';
import './state.svelte-CohGVeLh.js';
import './index-DaD05ukK.js';

function Error($$renderer, $$props) {
  $$renderer.component(($$renderer2) => {
    $$renderer2.push(`<h1>${escape_html(page.status)}</h1> <p>${escape_html(page.error?.message)}</p>`);
  });
}

export { Error as default };
//# sourceMappingURL=error.svelte-BHET3IQ9.js.map
