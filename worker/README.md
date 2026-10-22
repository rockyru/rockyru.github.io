# Chat Worker for rmbergonia.com

Answers questions on the homepage chat from the site's own content (`knowledge.md`) using Claude. The API key lives only in Cloudflare as a Worker secret.

## First-time setup

```sh
cd worker
npm install
npx wrangler login                      # opens the browser once
npx wrangler secret put ANTHROPIC_API_KEY
npx wrangler deploy
```

`wrangler.toml` routes `rmbergonia.com/api/chat*` to the Worker, so the page calls `/api/chat` on the same origin. The zone must be on the same Cloudflare account.

## Local development

```sh
cd worker
echo 'ANTHROPIC_API_KEY=sk-ant-...' > .dev.vars   # git-ignored
npm run dev                                      # http://127.0.0.1:8787
```

Serve the site from the repo root (`python3 -m http.server 8080`) and the page will call the local Worker automatically.

## Updating the content

Edit `knowledge.md` and redeploy. The scripted answers in `index.html` mirror the same facts, so update both when something changes.

## Model and cost

`CLAUDE_MODEL` in `wrangler.toml` defaults to `claude-haiku-5-5` with low effort and a 450-token output cap. The system prompt is cached, so most of each request is served at the cached rate. Switch to `claude-opus-5-5` in `wrangler.toml` if you want richer answers at a higher price.
