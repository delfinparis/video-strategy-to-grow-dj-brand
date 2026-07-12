# JoinKale Wheel Prototype

Standalone version of the "What I want most right now" spin-wheel concept for the top of joinkale.com. This is the same interactive prototype from Claude, exported as a plain static page so it can be hosted on a live URL.

- `index.html` — the whole thing (self-contained: HTML, CSS, JS all inline, no build step, no dependencies).

## Put it live on Vercel (free)

1. Push this branch (already done).
2. Go to https://vercel.com/new and import `delfinparis/video-strategy-to-grow-dj-brand`.
3. In the import screen:
   - **Root Directory** → click *Edit* → select `prototypes/joinkale-wheel`
   - **Framework Preset** → `Other`
   - Leave build/output empty (it's a static file).
4. **Deploy.** You'll get a live `*.vercel.app` URL in about a minute. Share that with anyone.

Every future push to the branch redeploys automatically.

## Or deploy from the command line

```
cd prototypes/joinkale-wheel
npx vercel --prod
```
(First run walks you through a one-time login.)
