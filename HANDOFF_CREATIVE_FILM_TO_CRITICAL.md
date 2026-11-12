# Handoff — replicate `agent-creative-thinking-skills` launch film in `agent-critical-thinking-skills`

> **From:** `lionfish` worktree (`agent-creative-thinking-skills`) — `/home/alek/orca/workspaces/agent-creative-thinking-skills/lionfish`  
> **Date:** 2026-11-12  
> **Source of truth:** `/home/alek/orca/workspaces/agent-creative-thinking-skills/.hyperframes-launch/index.html` (36s, 6×6s, full-bleed) + renders `..._08-34-50.mp4` → `assets/launch.gif` 960×540 432f 5.0 MB  
> **Please apply the same treatment to this repo's `.hyperframes-launch/index.html`** and redeliver the GIF/README. Do not diverge visually — keep the dark hyperframes look, just swap copy.

---

## 1. Why

GitHub shows the GIF in a small box (~480px wide). The old 12s cut cycled every ~2s, smallest type ~17–22px at 1920 → ~8–11px at 960 GIF → illegible. EU Art.50 voluntary disclosure was also requested. Fix = longer holds + much larger type that fills the frame.

## 2. What creative now looks like (copy this system)

**Duration:** `12s → 36s`, 6 screens, each **>5s hold** (hook 6.0s / count 6.0s / 4-cards 6.0s / board 6.0s / CTA 7.0s / EU end 5.0s).  
**Composition:** `#root 1920×1080`, `data-duration="36"`, `data-start="0,6,12,18,24,31"`.  
**Type (final, full-bleed):**

| token | size |
|---|---|
| `.h1` | 118px 900 -0.045em lh 0.88 |
| `.eyebrow` | 52px 700 0.14em `#22d3ee` |
| `.sub` | 48px #cbd5e1 max-w 1680 |
| `count 40/38` | 148px 900 |
| `micro-methods + router` | 46px 800 |
| `27 base …` | 32px mono 0.05em |
| `tagline` | 36px #cbd5e1 |
| `.card` | 460×480 pad 32×26 gap 16 |
| `.card .k` | 40px 700 0.14em |
| `.card .t` | 58px 900 -0.03em lh0.96 |
| `.card .d` | 42px 500 lh1.28 #fff |
| `.board` | 1840×760 r24, `h4 36px`, `.note 42px 800 pad 22×24` |
| `.code` | 48px pad 28×36 min-w 1240 |
| `.pill` | 36px 900 + `small 26px` |
| `boardCap` | 30px 0.08em |
| `endTitle`/`endSub` | 48px / 28px 0.1em |
| EU badge | `assets/eu-ai/eu-ai-generated-white.svg` 720×228 `drop-shadow(0 8px 24px rgba(0,0,0,.35))` + label `human-guided · OMP + Muse Spark · ~95% AI` 26px #cbd5e1 |

**Timeline (GSAP, paused):** each clip fades in at `_start+0.05` and fades out at `_start+duration-0.35`, so the hold is solid. See source file for exact `tl.fromTo` lines (search `// hook 0–6` etc.).

**End card (EU):**
```html
<div id="end" class="clip" data-start="31" data-duration="5">
  <div id="endAi" style="display:flex;flex-direction:column;align-items:center;gap:12px">
    <img id="euBadge" src="assets/eu-ai/eu-ai-generated-white.svg" alt="EU AI GENERATED — Art. 50 voluntary disclosure" width="720" height="228" style="width:720px;height:auto;display:block;filter: drop-shadow(0 8px 24px rgba(0,0,0,0.35));"/>
    <div id="endAiLabel" style="font-family:var(--font-mono);font-size:26px;letter-spacing:0.06em;color:#cbd5e1;text-transform:uppercase">human-guided · OMP + Muse Spark · ~95% AI</div>
  </div>
</div>
```
Animates `tl.fromTo("#endAi",{opacity:0,scale:0.96},{scale:1},31.45)` + label `31.7`.

**Assets added:**
- `assets/eu-ai/` — 12 files from EU official ZIPs `document/129546` (SVG) / `document/129547` (PNG): `eu-ai-generated-*`, `eu-ai-basic-*`, `eu-ai-white/black.svg`. Copied to `.hyperframes-launch/assets/eu-ai/eu-ai-generated-white.svg` for render.
- `assets/badges/` — `cc0-ai-assisted-claude.svg`, `cc0-ai-coded-claude.svg` (CC0 `mau-vera/built-with-ai-badges`).
- Same copied to `lionfish/assets/`.

**README (both repos):**
- Top badge row: `[![Built with AI — human-guided](https://img.shields.io/badge/Built%20with%20AI-human--guided%20%E2%80%A2%20OMP%20%2B%20Muse%20Spark%20%E2%80%A2%20~95%25%20AI-8b5cf6)](https://github.com/aleknitka/agent-creative-thinking-skills)` (or `agent-critical-thinking-skills` for this repo)
- Image alt: `![Launch film — 40 methods in 36 seconds](assets/launch.gif)` → for **this repo** use `![Launch film — 8 skills (8 + router) in 36 seconds](assets/launch.gif)` (or `9 skills` as currently: keep consistent)
- New section `## Transparency · AI disclosure — EU AI Act Art. 50` — table with EU icon inline (`assets/eu-ai/eu-ai-generated-black.svg`) + links to `digital-strategy.ec.europa.eu/.../eu-icons-labelling-ai-generated-content`, Code of Practice §2, both ZIPs, explains `AI GENERATED` white-on-dark / black-on-light, free no-attribution, voluntary (not deepfake/public-interest text, enforcement 2 Aug 2026 €15M/3%), where shown (README + end card + shared artefacts) + CC0 note for `assets/badges/`. **Copy the full block verbatim from creative's `README.md:179-205`** and adapt repo URL.

**Render chain (verified):**
```bash
cd .hyperframes-launch && npx --yes hyperframes@0.9.19 check
npx --yes hyperframes@0.9.19 render            # → renders/.hyperframes-launch_*.mp4 3.9 MB 36.0s 1080f
cp renders/.*.mp4 /tmp/hyperframes-launch.mp4   # note dotfile
ffmpeg -y -i /tmp/hyperframes-launch.mp4 -vf "fps=12,scale=960:-1:flags=lanczos,palettegen=max_colors=256" /tmp/palette.png
ffmpeg -y -i /tmp/hyperframes-launch.mp4 -i /tmp/palette.png -lavfi "fps=12,scale=960:-1:flags=lanczos [x]; [x][1:v] paletteuse=dither=bayer:bayer_scale=3" /tmp/launch_full.gif
cp /tmp/launch_full.gif assets/launch.gif
npx --yes hyperframes@0.9.19 snapshot --at 2,8,14,20,27,33  # verify 6 holds + legibility
```
GIF is 960×540 432 frames at 12fps, 5.0 MB (<10 MB GitHub limit), `check` 0 errors. Snapshot `contact-sheet.jpg` is `af62be8c-…` for creative — reproduce similar for critical.

---

## 3. What to do in this repo (`agent-critical-thinking-skills`)

1. **Copy assets** (or re-fetch):
   ```bash
   mkdir -p assets/eu-ai assets/badges .hyperframes-launch/assets/eu-ai
   cp -r /home/alek/orca/workspaces/agent-creative-thinking-skills/assets/eu-ai/* assets/eu-ai/
   cp -r /home/alek/orca/workspaces/agent-creative-thinking-skills/assets/badges/* assets/badges/ 2>/dev/null || true
   cp assets/eu-ai/eu-ai-generated-white.svg .hyperframes-launch/assets/eu-ai/
   ```
   Alternatively re-download EU ZIPs: `https://ec.europa.eu/newsroom/dae/redirection/document/129546` (SVG) + `129547` (PNG). Licence: free, no attribution.

2. **Replace `.hyperframes-launch/index.html`** visually with the 36s full-bleed version. Easiest: copy creative's file wholesale then **swap copy only**:
   - Keep your 5 buckets / CTA but reuse sizes/timings. Current critical copy to preserve:
     - Hook: `eyebrow "for anyone who decides with an AI"` / `h1 "Your AI says yes<br><em>too quickly</em>"` / `sub "Not more ideas. Sharper judgment — a scorecard, a map, a probe …"`
     - Count: `8/9` + `micro-methods + router` + `8 evaluative + sharper judgment · 5 buckets` + `tagline "Offline helpers · deterministic · no hallucinated sources · Claude Code + Codex + OMP"`
     - 4 cards: `sharper judgment / Is it sound? / evidence appraisal…` / `better question / Are we asking it right? / socratic…` / `broader views / What are we missing? / steelman…` / `stronger bets / Which bet is best? / Bayes…`  (keep `c1…c4`)
     - Board: 5 lanes `Claim / Source / Strength 1–5 / Fallacy / Probe` with your notes + `boardCap "claim → source tier → strength → fallacy → probe · 5 buckets · offline JSON boards"`
     - CTA: `/plugin marketplace add aleknitka/agent-critical-thinking-skills` etc. + `pill "no hallucinating sources"`
     - End: `agent-critical-thinking-skills` / `8 skills + router · 5 buckets · Codex + Claude Code · MIT` + same EU badge block (keep `human-guided · OMP + Muse Spark · ~95% AI`)
   - Keep all CSS + timeline structure from creative's file (already 36s-ready). Just update strings.

   Source file path to copy: `/home/alek/orca/workspaces/agent-creative-thinking-skills/.hyperframes-launch/index.html` (13803 bytes, `data-duration 36`).

3. **Patch `README.md`:**
   - Badge row → `OMP + Muse Spark` variant with this repo's name.
   - Image alt/duration → `36 seconds`.
   - Insert the full `## Transparency · AI disclosure — EU AI Act Art. 50` block (adapt URLs to `agent-critical-thinking-skills`).

4. **Render + GIF + snapshot** using the chain above. Verify each of the 6 screens is readable at 480px wide (contact sheet), then copy GIF to `assets/launch.gif`. MP4 stays in `renders/` + `/tmp/hyperframes-launch.mp4`.

5. **Check:** `hyperframes check` should be `0 errors`, `Contrast 19/19 pass` (creative) — critical currently has similar, should stay clean. `snapshot --at 2,8,14,20,27,33` must show no overflow.

---

## 4. References

- Creative's final contact sheet: `/home/alek/orca/workspaces/agent-creative-thinking-skills/.hyperframes-launch/.hyperframes/artifacts/snapshots/af62be8c-05da-4a7a-9047-c706f94f204e/contact-sheet.jpg` (7 frames inc. 35.75)
- Creative's render: `renders/.hyperframes-launch_2026-11-12_08-34-50.mp4` + `/tmp/hyperframes-launch.mp4`
- Creative's GIF: `/home/alek/orca/workspaces/agent-creative-thinking-skills/assets/launch.gif` + `lionfish/assets/launch.gif`
- EU icons page: https://digital-strategy.ec.europa.eu/en/policies/eu-icons-labelling-ai-generated-content
- Code of Practice: https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content
- EU ZIPs: https://ec.europa.eu/newsroom/dae/redirection/document/129546 (SVG) and .../129547 (PNG)
- Disclosure badges: https://disclosingai.com/ (CC0 `mau-vera/built-with-ai-badges`)
- Wording requested: `AI generated OMP + Meta Muse Spark` → rendered as `human-guided · OMP + Muse Spark · ~95% AI`

---

**After delivering**, delete this handoff or keep as `research/critical-thinking/plan.md` reference. View the result via `README.md:7` GIF or `file:///home/alek/agent-critical-thinking-skills/assets/launch.gif` and `npx hyperframes preview --background`.
