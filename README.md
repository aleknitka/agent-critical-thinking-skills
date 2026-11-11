# agent-critical-thinking-skills

Critical-thinking micro-skills for AI harnesses — the evaluative counterpart to `agent-creative-thinking-skills`.

> **Planned track (8 skills):** `evidence-appraisal` → `argument-mapping` → `fallacy-bias-spotting` → `bayesian-updating` → `socratic-elenchus` → `steelman-red-team` → `calibration-forecasting` → `decision-analysis` — plus a 5th router bucket `sharper judgment`.

See `research/critical-thinking/plan.md` for the Facione / Paul-Elder / Halpern gap analysis and ranked proposal.

## Status

Scaffolded — plan moved from `agent-creative-thinking-skills` (see commit). Architecture copied (templates, scripts, workspace, marketplace). First skills to be built as `v0.1.0`.

## Layout

Same as `agent-creative-thinking-skills`: `plugins/critical-thinking-skills/skills/<skill>/SKILL.md` + `references/` + `scripts/*.py` + `scripts/validate.py`.

## Adding a skill

1. `cp -r templates/skill plugins/critical-thinking-skills/skills/<name>`
2. Edit `SKILL.md`; `name` must equal directory name.
3. `python3 scripts/validate.py`
4. Bump `version` in both `plugin.json` and `marketplace.json`.
