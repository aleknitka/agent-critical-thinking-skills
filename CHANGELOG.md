# Changelog

All notable changes to `agent-critical-thinking-skills` follow Keep a Changelog and align with the `plugin.json` / `marketplace.json` versions.

## [0.9.0] — 2026-11-11

### Added

- **8 critical-thinking skills** completing the ranked track from `research/critical-thinking/plan.md` (coverage audit: Facione / Paul–Elder / Halpern gap):
  1. `evidence-appraisal` — source tier × recency × directness × bias → strength 1–5 + next probe (`scripts/evidence.py`)
  2. `argument-mapping` — Toulmin parse + validity tag (deductive/inductive/abductive) (`scripts/argmap.py`)
  3. `fallacy-bias-spotting` — 20 fallacies × 20 biases → Hit/Maybe/No + de-bias (`scripts/fallacy.py`, 40-entry `references/catalog.md`)
  4. `bayesian-updating` — prior → likelihood ratio → posterior + base-rate flag + VOI (`scripts/bayes.py`)
  5. `socratic-elenchus` — definition → counterexample → revision → operational definition (`scripts/elenchus.py`)
  6. `steelman-red-team` — strongest ¬P + 5 attack vectors + pre-commit falsifier (`scripts/redteam.py`)
  7. `calibration-forecasting` — Brier-scored forecasts + calibration curve + 3 live predictions (`scripts/calibrate.py`)
  8. `decision-analysis` — EV sheet (options × outcomes × p × u) + sensitivity sweep + probe (`scripts/decide.py`)
- `thinking-router` — 5-bucket router adding **sharper judgment** (Facione evaluation) alongside better question / broader perspectives / stronger options (`scripts/route.py`, 8-method `references/catalog.md`, scoring `references/routing.md`). Harness-agnostic (Claude Code + Codex + OMP/Pi via `npx skills add`).
- 9 critical board templates in `workspace/` — `evidence-appraisal`, `argument-mapping`, `fallacy-bias`, `bayesian-updating`, `socratic-elenchus`, `steelman-red-team`, `calibration-forecasting`, `decision-analysis`, `critical-router` — plus schema enum and `workspace/app.js` wiring. Complements the 18 creative templates (27 total).
- `examples/gallery.md` — critical-track gallery: 4 sections, runnable prompts per skill, offline helper examples with exact CLI invocations, and a copy-paste end-to-end router chain. Codex note and cross-links.
- Full progressive-disclosure reference layer (18 `references/*.md`: scorecard, toulmin, catalog, bayes, elenchus, steelman, calibration, decision, routing, + 9 `provenance.md` with Sio & Lortie-Forgues 2024 g≈0.30 disclosure).

### Changed

- `README.md` — install for Claude Code + Codex, 8-skill table, 5th-bucket explanation, workspace/Gallery/Provenance guidance.
- `workspace/boards/_schema.json` — enum now includes 9 critical templates (27 total with creative track).

### Fixed

- `.claude-plugin/marketplace.json` + `.omp-plugin/marketplace.json` + `plugins/critical-thinking-skills/.claude-plugin/plugin.json` — version `0.1.0` → `0.9.0`, description reflects shipped 8 skills + router.
- `pyproject.toml` — `0.1.0` → `0.9.0`.

### Notes

- All helpers are offline, stdlib-only, deterministic (`--json`/`--list`/`--help` where applicable). `python3 scripts/validate.py` passes (frontmatter `name==dir`, description ≤1024 chars, body ≤500 lines, links resolve).
- Built with 9 sub-agents (one per skill + router). Full session transcript: `.omp/agent/sessions/-agent-critical-thinking-skills/<session>.jsonl`.

## [0.1.0] — 2026-11-11

- Scaffolded from `agent-creative-thinking-skills` architecture (templates, scripts, workspace, marketplace).
- Added `research/critical-thinking/plan.md` (8-skill ranked track: evidence-appraisal, argument-mapping, fallacy-bias-spotting, bayesian-updating, socratic-elenchus, steelman-red-team, calibration-forecasting, decision-analysis).
