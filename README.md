# agent-critical-thinking-skills

[![GitHub release](https://img.shields.io/github/v/release/aleknitka/agent-critical-thinking-skills)](https://github.com/aleknitka/agent-critical-thinking-skills/releases) [![skills.sh](https://skills-badge.vercel.app/badge/aleknitka/agent-critical-thinking-skills)](https://www.skills.sh/aleknitka/agent-critical-thinking-skills) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Claude Code](https://img.shields.io/badge/Claude%20Code-marketplace-8b5cf6?logo=anthropic)](https://code.claude.com/docs/en/plugin-marketplaces) [![Codex](https://img.shields.io/badge/Codex-skills-000000?logo=openai)](https://developers.openai.com/codex/skills) [![OMP & Pi](https://img.shields.io/badge/OMP%20%26%20Pi-marketplace-ff6b35)](https://openai.github.io/openai-skills)

> **Make any AI a sharper judge.** 8 evaluative micro-methods + a router — with a 5th bucket `sharper judgment` — that turn "is this credible / does this follow / what are we missing" into a scorecard, a map, a bias scan, or a priced bet — plus the probe that proves it.

![Launch film — 8 + router in 42 seconds](assets/launch.gif)

No prompt engineering. Works with Claude Code, Codex, and any harness that loads skills. Every method: one sharp instruction → a concrete artifact → a tiny experiment.

```bash
# Claude Code
/plugin marketplace add aleknitka/agent-critical-thinking-skills
/plugin install critical-thinking-skills@agent-critical-thinking-skills
# OMP (same catalog — .omp-plugin/marketplace.json now shipped)
/marketplace add aleknitka/agent-critical-thinking-skills
/marketplace install critical-thinking-skills@agent-critical-thinking-skills
# Pi / any skills.sh harness
npx skills add aleknitka/agent-critical-thinking-skills
# Run offline helpers with uv (pip also works)
uv run python plugins/critical-thinking-skills/skills/thinking-router/scripts/route.py --text "is this source credible, does the argument follow?"
# then in any conversation:
> Help me think critically about this claim — not sure which method fits.
# → thinking-router triages into sharper judgment / better question / broader perspectives / stronger options
#   and hands off to 1–2 methods with your okay.
```

**Try without an agent (offline, deterministic, no network — `uv` or `python`):**
```bash
uv run python plugins/critical-thinking-skills/skills/thinking-router/scripts/route.py --text "is this source credible, does the argument follow?"
uv run python plugins/critical-thinking-skills/skills/evidence-appraisal/scripts/evidence.py --claim "X reduces Y by 20%" --tier rct --n 200 --json
uv run python plugins/critical-thinking-skills/skills/bayesian-updating/scripts/bayes.py --prior 0.1 --lr 9 --json
# pip fallback: python plugins/critical-thinking-skills/skills/.../scripts/*.py --help
```

60s proof — no agent, no network:
```bash
uv run python plugins/critical-thinking-skills/skills/thinking-router/scripts/route.py \
  --text "is this source credible, does the argument follow?" --json
# → "primary_bucket": "sharper_judgment", "confidence": "high"
# → 1. evidence-appraisal  score 1.00 → source scorecard + strength 1–5
# → 2. argument-mapping    score 0.57 → Toulmin map + validity tag
```

---

## Why this, not just "more ideas"?

`agent-creative-thinking-skills` gives you breadth — more frames, more lenses, more options. This does the opposite: it makes your judgment *narrower and more accountable* before you commit. Every skill forces a falsifiable artifact so you can see whether the reasoning survives contact with evidence.

- **Routed, not scattered.** A 5-bucket router (`sharper judgment` + 4 creative buckets) scores your brief and shortlists 1–2 methods — so you don't method-shop from 9 tabs.
- **Artifact, not advice.** Each skill ends in something you can hand to someone: a tier→strength scorecard, a Toulmin map with a validity tag, a 40-tag bias scan, a posterior with a base-rate flag, an operational definition, a steelman with a falsifier, a Brier log, an EV sheet with a tornado — plus the probe that proves it.
- **Offline & deterministic.** `scripts/*.py` (`--json`/`--list`/`--help`) run with no network and no guesswork; re-run with the same inputs and you get the same score.
- **Human + agent board.** A vanilla-JS workspace (`workspace/index.html`) — sticky notes, lanes, votes — that both sides read/write (`workspace/boards/<id>.json`). 9 critical templates + 18 creative templates.

**When to use something else:** you need a generative burst (use `agent-creative-thinking-skills`), a one-off writing polish (use a copilot), a validated simulator (build a model, not a 5-lane board), or real user interviews (do interviews, not `stakeholder-perspectives` hypotheses). [Full triage in each `references/provenance.md`.](plugins/critical-thinking-skills/skills/thinking-router/references/catalog.md)

---

## What you get in 60 seconds

1. **Tell the router one sentence** about what's stuck. It returns *Primary / Alternate / Not now* with why.
2. **Run the skill** for 10–20 min: you do the intake (one claim + source), it does the scoring/mapping, you harvest the artifact + next probe.
3. **Ship a probe:** "we'll check the RCT / holdout one cohort; if lift <2pp at p>0.2 we keep the sceptical hypothesis."

Small example (no install):

```bash
python plugins/critical-thinking-skills/skills/evidence-appraisal/scripts/evidence.py --claim "Onboarding lifts retention 20% (n=40, blog)" --tier blog --n 40 --recency 7 --directness indirect --json
# → strength 1.0 / hypothesis · next probe: find the RCT / preregistered replication
```

Full method list and triggers: [`plugins/critical-thinking-skills/skills/thinking-router/references/catalog.md`](plugins/critical-thinking-skills/skills/thinking-router/references/catalog.md).

---

## The toolkit — 8 skills + a router

Every skill follows progressive disclosure: `SKILL.md` (lean process, always loaded) → `references/*.md` (on demand) → `scripts/*.py` (offline helpers). No bundled worksheets.

### Sharper judgment — is the reasoning sound?

| Skill | What it does | Use when | Source |
|---|---|---|---|
| `evidence-appraisal` | Source tier × recency × directness × bias → strength 1–5 + next probe | A claim cites a source — how much is it worth? | [Facione / Paul–Elder / Ioannidis](plugins/critical-thinking-skills/skills/evidence-appraisal/references/provenance.md) |
| `argument-mapping` | Toulmin parse (claim/grounds/warrant/backing/qualifier/rebuttal) + validity tag | Paragraph sounds persuasive — does it follow? | [Toulmin / Walton](plugins/critical-thinking-skills/skills/argument-mapping/references/provenance.md) |
| `fallacy-bias-spotting` | 20 fallacies × 20 biases → Hit/Maybe/No + de-bias move | Draft feels right but may be systematically wrong | [Kahneman / Tversky](plugins/critical-thinking-skills/skills/fallacy-bias-spotting/references/provenance.md) |

### Better question — are we asking the right thing?

| Skill | What it does | Use when | Source |
|---|---|---|---|
| `socratic-elenchus` | Definition → counterexample → revision → operational definition | A key term is used but never defined | [Paul–Elder / Ennis](plugins/critical-thinking-skills/skills/socratic-elenchus/references/provenance.md) |

### Broader perspectives — what view are we missing?

| Skill | What it does | Use when | Source |
|---|---|---|---|
| `steelman-red-team` | Strongest ¬P + 5 attack vectors + pre-commit falsifier | Critique feels weak / you may be strawmanning | [Zenko / Tetlock](plugins/critical-thinking-skills/skills/steelman-red-team/references/provenance.md) |

### Stronger options — which bet is best?

| Skill | What it does | Use when | Source |
|---|---|---|---|
| `bayesian-updating` | Prior → likelihood ratio → posterior + base-rate flag + VOI | Prior + new evidence → how much to move? | [Bayes / Tetlock](plugins/critical-thinking-skills/skills/bayesian-updating/references/provenance.md) |
| `calibration-forecasting` | Brier-scored forecasts + calibration curve + 3 live predictions | Confidence ≠ accuracy; need accountable forecasts | [Brier / Tetlock](plugins/critical-thinking-skills/skills/calibration-forecasting/references/provenance.md) |
| `decision-analysis` | EV sheet (options × outcomes × p × u) + sensitivity + probe | Choose under uncertainty with stakes | [Howard & Matheson](plugins/critical-thinking-skills/skills/decision-analysis/references/provenance.md) |

### The 5th bucket

The creative track routes into *better question / more ideas / broader perspectives / stronger options*. The critical track keeps those four and adds **sharper judgment** (Facione evaluation + Paul–Elder standards) — where `evidence-appraisal`, `argument-mapping`, and `fallacy-bias-spotting` live by default. The router surfaces this bucket first so "is this sound?" has a name:

```
sharper judgment → is the reasoning sound? (evidence-appraisal, argument-mapping, fallacy-bias-spotting, …)
better question  → are we asking the right thing? (socratic-elenchus, evidence-appraisal)
broader perspectives → what view are we missing? (steelman-red-team, fallacy-bias-spotting)
stronger options → which bet is best? (bayesian-updating, calibration-forecasting, decision-analysis)
more ideas       → (creative counterpart — not in this track)
```

### Progressive disclosure

```
Frontmatter `description` — always in context; says what + when + triggers (≤1024 chars)
  ↓ triggers
SKILL.md body — lean process, artifact, guardrails (<80 lines here; hard cap 500)
  ↓ on demand
references/*.md — one topic per file (scorecard, toulmin, bayes, catalog, provenance …)
scripts/*.py   — offline helpers ( --json / --list / --help, deterministic, stdlib only )
```

### Router & shared surface

| | What it does | Use when |
|---|---|---|
| `thinking-router` | Scores 5 buckets → Primary/Alternate/Not now + handoff (carries intake) | "Help me think critically" / unsure which method fits |
| **Workspace** | Browser board — notes, lanes, drawing, votes, timer, file I/O | Human + agent on one board (`critical-router` + 8 method templates) |

Critical templates: `evidence-appraisal` · `argument-mapping` · `fallacy-bias` · `bayesian-updating` · `socratic-elenchus` · `steelman-red-team` · `calibration-forecasting` · `decision-analysis` · `critical-router` (+ 18 creative templates).

---

## Gallery — copy-paste prompts

**Start here:** [`examples/gallery.md`](examples/gallery.md) — 60-s quick start → one prompt per bucket → end-to-end `router → skill → probe` chain → offline helpers. Onboarding (60s → 15min → 60min): [`ONBOARDING.md`](ONBOARDING.md).

```bash
uv run python plugins/critical-thinking-skills/skills/thinking-router/scripts/route.py --text "is this source credible, does the argument follow?"
uv run python plugins/critical-thinking-skills/skills/evidence-appraisal/scripts/evidence.py --claim "X reduces Y by 20%" --tier blog --n 40 --recency 7 --json
uv run python plugins/critical-thinking-skills/skills/fallacy-bias-spotting/scripts/fallacy.py --text "We tried it once and it failed, so it will always fail" --json
```

---

## Who this is for (and not for)

**For:** anyone who works with an AI and wants better judgment — product, design, research, strategy, teaching, ops, solo or team. The creative track is for divergence; this one is for evaluation. Use both: diverge, then stress-test.

**Not for:** replacing user research, stakeholder interviews, or a validated model. Many skills deliberately produce *hypotheses labeled with strength 1–5* — they make the probe clearer, they don't replace evidence. Every `references/provenance.md` discloses limits; see `research/critical-thinking/plan.md` (Sio & Lortie-Forgues 2024 deflated g≈0.30).

---

## Status, licence, and maintenance

- **Status:** actively maintained, `0.9.0` — breaking changes bump minor while pre-1.0; every skill ships with `references/provenance.md`.
- **Licence:** MIT (see `LICENSE`).
- **Requirements:** `uv` (or Python ≥3.13) for `scripts/*.py` (`uv sync` once, then `uv run python …`); Claude Code, Codex, OMP or Pi for `SKILL.md` auto-loading; workspace needs any modern browser, no build, no deps.
- **Releases:** [`CHANGELOG.md`](CHANGELOG.md) — `scripts/validate.py` gates every release (`OK` on 9 skills, 5-bucket router). Launch film: `assets/launch.gif` (960×540, 42s, 2.0M, ~7s/slide) + HyperFrames source in `.hyperframes-launch/index.html`.

---

## Transparency · AI disclosure — EU AI Act Art. 50

**Human-guided, ~95% AI-generated — OMP + Meta Muse Spark (muse-spark-1.2).** This repo, its docs, skills, and the launch film were generated with AI (OpenAI Codex / OMP harness + Meta Muse Spark as coding agent) under human guidance, review and editorial control. All content remains the author's responsibility.

<table>
<tr>
<td width="220">

**EU official disclosure — voluntary.**

[![EU — AI Generated — light](assets/eu-ai/eu-ai-generated-black.svg)](https://digital-strategy.ec.europa.eu/en/policies/eu-icons-labelling-ai-generated-content)
</td>
<td>

[EU Icons for labelling AI-generated content](https://digital-strategy.ec.europa.eu/en/policies/eu-icons-labelling-ai-generated-content) — official set for **Article 50 AI Act** + [Code of Practice §2](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content) (enforcement 2 Aug 2026, penalties to €15M / 3% turnover). The icons are **free to use without attribution** (Commission/AI Office). This project is not a deepfake nor a publication informing the public on matters of public interest, so the legal labelling duty does not strictly apply — we disclose voluntarily for transparency.

- **Mark used here:** `AI GENERATED` (white pill · black text for dark backgrounds · black pill for light) — variant reproduced locally at [`assets/eu-ai/`](assets/eu-ai/) from the official [SVG ZIP](https://ec.europa.eu/newsroom/dae/redirection/document/129546) / [PNG ZIP](https://ec.europa.eu/newsroom/dae/redirection/document/129547). (`AI` + `AI MODIFIED` variants also available.)
- **Where shown:** README transparency section, launch film end card (12s), and as an embedded mark on AI-generated artefacts when shared.

</td>
</tr>
</table>

**Development transparency (CC0):** model-level badge via [AI Disclosure Badges](https://disclosingai.com/) ([mau-vera/built-with-ai-badges](https://github.com/mau-vera/built-with-ai-badges), CC0) — local copies in [`assets/badges/`](assets/badges/), adapted from `AI Assisted · Claude` to **AI Assisted · OMP + Muse Spark · human-guided**.

> *No validator, no compliance checklist — a voluntary "nutrition label" for how this was made.*

---

## Contributing & docs furniture

- Layout & progressive-disclosure rules: [`CLAUDE.md`](CLAUDE.md)
- Onboarding (60s → 15min → 60min): [`ONBOARDING.md`](ONBOARDING.md)
- Start a new skill: `cp -r templates/skill plugins/critical-thinking-skills/skills/<name>` → `python3 scripts/validate.py`
- Full docs: `research/critical-thinking/plan.md` + `examples/gallery.md` + `workspace/index.html?board=critical-onboarding`
