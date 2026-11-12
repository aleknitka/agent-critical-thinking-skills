# agent-critical-thinking-skills

[![GitHub release](https://img.shields.io/github/v/release/aleknitka/agent-critical-thinking-skills)](https://github.com/aleknitka/agent-critical-thinking-skills/releases) [![skills.sh](https://skills-badge.vercel.app/badge/aleknitka/agent-critical-thinking-skills)](https://www.skills.sh/aleknitka/agent-critical-thinking-skills) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Claude Code](https://img.shields.io/badge/Claude%20Code-marketplace-8b5cf6?logo=anthropic)](https://code.claude.com/docs/en/plugin-marketplaces) [![Codex](https://img.shields.io/badge/Codex-skills-000000?logo=openai)](https://developers.openai.com/codex/skills) [![OMP & Pi](https://img.shields.io/badge/OMP%20%26%20Pi-marketplace-ff6b35)](https://openai.github.io/openai-skills)

> **Make any AI a sharper judge.** 8 evaluative methods + a router — the 5th bucket `sharper judgment` — that turn "is this credible / does this follow / what are we missing" into a scorecard, a map, or a priced bet — plus the probe that proves it.

![Launch film — 8 + router in 42 seconds](assets/launch.gif)

No prompt engineering. Works with Claude Code, Codex, and any harness that loads skills. One sharp instruction → a concrete artifact → a tiny experiment.

```bash
# Claude Code
/plugin marketplace add aleknitka/agent-critical-thinking-skills
/plugin install critical-thinking-skills@agent-critical-thinking-skills
# Pi / any skills.sh harness
npx skills add aleknitka/agent-critical-thinking-skills
# Offline — no agent needed
uv run python plugins/critical-thinking-skills/skills/thinking-router/scripts/route.py --text "is this source credible, does the argument follow?"
# → thinking-router triages into sharper judgment / better question / … and hands off with your okay
```

## Why this?

`agent-creative-thinking-skills` gives breadth — more ideas. This gives accountability — fewer, sharper judgments before you commit.

- **Routed.** A 5-bucket router scores your question and shortlists 1–2 methods.
- **Artifact, not advice.** Every method ends in something checkable: a scorecard, a map, a Brier score, an EV sheet — plus the probe that would falsify it.
- **Offline.** Helpers are `scripts/*.py` (`--json`/`--help`) — deterministic, no network.

## In 60 seconds

1. Ask the router one sentence — get Primary / Alternate + why.
2. Run one skill (10 min): one claim + source → scorecard / map / posterior + next probe.
3. Ship a probe: "holdout one cohort; if lift <2pp at p>0.2, keep the sceptical hypothesis."

```bash
python plugins/critical-thinking-skills/skills/evidence-appraisal/scripts/evidence.py --claim "Onboarding lifts retention 20% (n=40, blog)" --tier blog --n 40 --recency 7 --json
# → strength 1.0 · next probe: find the RCT
```

## Toolkit — 8 skills + a router

| Skill | Does | When |
|---|---|---|
| `evidence-appraisal` | tier × recency × bias → strength 1–5 + probe | A claim cites a source |
| `argument-mapping` | Toulmin map + validity tag | Does it actually follow? |
| `fallacy-bias-spotting` | 40 checks → Hit/Maybe + de-bias | Feels right but might be wrong |
| `socratic-elenchus` | definition → counterexample → operational def | A term is vague |
| `steelman-red-team` | strongest ¬P + 5 attacks + falsifier | Your critique is weak |
| `bayesian-updating` | prior → LR → posterior + base-rate flag | How much to update? |
| `calibration-forecasting` | Brier + calibration curve | Confidence ≠ accuracy |
| `decision-analysis` | EV sheet + sensitivity + probe | Which bet? |
| `thinking-router` | 5 buckets → Primary/Alternate + handoff | Not sure which fits |

The 5th bucket `sharper judgment` (Facione / Paul–Elder) is where `evidence-appraisal`, `argument-mapping`, `fallacy-bias-spotting` live — "is the reasoning sound?" — before better question / broader perspectives / stronger options.

Workspace: `workspace/index.html` — sticky notes + board that humans and agents share (`workspace/boards/<id>.json`). 9 critical templates.

## Gallery

[`examples/gallery.md`](examples/gallery.md) — one copy-paste prompt per skill + end-to-end chain. Onboarding: [`ONBOARDING.md`](ONBOARDING.md) (60s → 15min → 60min). Triggers & artifacts: [`thinking-router/references/catalog.md`](plugins/critical-thinking-skills/skills/thinking-router/references/catalog.md).

## Status

- `0.9.0` · MIT · `uv` or Python ≥3.13, any modern browser for the board.
- `scripts/validate.py` gates every release. Film: `assets/launch.gif` (960×540, 42s).

## Transparency

Human-guided, ~95% AI-generated (OMP + Muse Spark). ![EU AI Generated](assets/eu-ai/eu-ai-generated-black.svg) [EU Art. 50](https://digital-strategy.ec.europa.eu/en/policies/eu-icons-labelling-ai-generated-content) — mark at `assets/eu-ai/`, film end card, and on shared artefacts. Badges: [`assets/badges/`](assets/badges/) (CC0).

---

Layout rules: [`CLAUDE.md`](CLAUDE.md) · New skill: `cp -r templates/skill plugins/critical-thinking-skills/skills/<name>` → `python3 scripts/validate.py`
