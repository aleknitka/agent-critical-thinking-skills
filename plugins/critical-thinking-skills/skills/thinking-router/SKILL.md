---
name: thinking-router
description: Route to the right critical skill — triage into sharper judgment / better question / more ideas / broader perspectives / stronger options, score 8 methods, shortlist 1-2 with user confirmation. Use when unsure which critical skill fits or need a handoff. Triggers: "which skill", "which method", "route this", "not sure which fits", "help me choose a tool".
---

# Thinking Router (Critical Track)

With 8 critical skills sharing vocabulary ("evidence", "argument", "bias"), the router makes the split legible. It scores the prompt against five buckets, ranks the 8 methods, and hands off to 1–2 skills with user confirmation — never auto-running a method the user did not choose.

## Buckets → Skills

| Bucket | Sharpens | Methods |
|---|---|---|
| **Sharper judgment** | is the reasoning sound? | all 8, especially evidence-appraisal, argument-mapping, fallacy-bias-spotting |
| **Better question** | are we asking the right thing? | evidence-appraisal, argument-mapping, socratic-elenchus |
| **Broader perspectives** | what view are we missing? | fallacy-bias-spotting, steelman-red-team |
| **Stronger options** | which bet is best? | bayesian-updating, calibration-forecasting, decision-analysis |
| **More ideas** | (creative counterpart) | not in this track — see `agent-creative-thinking-skills` |

## Process

1. **Intake.** One paragraph: goal, stakes, and where you feel stuck.
2. **Score.** Keyword + intent signals per bucket (see [references/routing.md](references/routing.md)). Normalize to 0–1.
3. **Rank 8 methods** by bucket fit × stakes. Keep top 2–3; tie-break by specificity (precise trigger beats generic "help me think").
4. **Shortlist + handoff.** Present 1–2 recommendations with one line each ("because … → artifact …"). Ask "proceed with X?" Carry the intake forward — do not make the user restate it.

## Artifact

Ranked list (3 max): rank, skill, bucket, one-line why, artifact preview. No method is run without confirmation.

Helper: `python scripts/route.py --text "…" --json` (or `--list` for the catalog).

## Going deeper

- Catalog of 8 methods with triggers and artifacts: [references/catalog.md](references/catalog.md)
- Scoring rubric and worked routings: [references/routing.md](references/routing.md)
