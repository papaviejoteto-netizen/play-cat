const manifest = (() => {
function __memo(fn) {
	let value;
	return () => value ??= (value = fn());
}

return {
	appDir: "_app",
	appPath: "_app",
	assets: new Set(["favicon.svg","robots.txt"]),
	mimeTypes: {".svg":"image/svg+xml",".txt":"text/plain"},
	_: {
		client: {start:"_app/immutable/entry/start.B3XfCDUp.js",app:"_app/immutable/entry/app.B4Nyib-v.js",imports:["_app/immutable/entry/start.B3XfCDUp.js","_app/immutable/chunks/BX0c1fD1.js","_app/immutable/chunks/BJMOgyk6.js","_app/immutable/chunks/B64TLU0q.js","_app/immutable/chunks/YwOi7tgn.js","_app/immutable/chunks/CYHOywpD.js","_app/immutable/entry/app.B4Nyib-v.js","_app/immutable/chunks/B64TLU0q.js","_app/immutable/chunks/YwOi7tgn.js","_app/immutable/chunks/DsnmJJEf.js","_app/immutable/chunks/BJMOgyk6.js","_app/immutable/chunks/C4t6inGP.js"],stylesheets:[],fonts:[],uses_env_dynamic_public:false},
		nodes: [
			__memo(() => import('./chunks/0-CKoGZA8_.js')),
			__memo(() => import('./chunks/1-BeWT4Z_e.js')),
			__memo(() => import('./chunks/4-PZaYyRb2.js'))
		],
		remotes: {
			
		},
		routes: [
			{
				id: "/sverdle",
				pattern: /^\/sverdle\/?$/,
				params: [],
				page: { layouts: [0,], errors: [1,], leaf: 2 },
				endpoint: null
			}
		],
		prerendered_routes: new Set(["/","/about","/sverdle/how-to-play"]),
		matchers: async () => {
			
			return {  };
		},
		server_assets: {}
	}
}
})();

const prerendered = new Set(["/","/about","/sverdle/how-to-play"]);

const base = "";

export { base, manifest, prerendered };
//# sourceMappingURL=manifest.js.map
