import { i as resolve_route, j as initial_base, b as base } from './routing-vTSQcIgq.js';
import { J as try_get_request_store } from './context-DzB0Gc18.js';

function resolve(id, params) {
  const resolved = resolve_route(
    id,
    /** @type {Record<string, string>} */
    params
  );
  {
    const store = try_get_request_store();
    if (store && !store.state.prerendering?.fallback) {
      const after_base = store.event.url.pathname.slice(initial_base.length);
      const segments = after_base.split("/").slice(2);
      const prefix = segments.map(() => "..").join("/") || ".";
      return prefix + resolved;
    }
  }
  return base + resolved;
}

export { resolve as r };
//# sourceMappingURL=server2-DV0Rj6fy.js.map
