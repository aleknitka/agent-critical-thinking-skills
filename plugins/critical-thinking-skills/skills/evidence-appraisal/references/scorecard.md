# Evidence Scorecard

## Tier table

| Tier | Base | Typical artifact | What it buys | Common failure |
|---|---|---|---|---|
| meta-analysis / systematic review | 5 | preregistered synthesis, forest plot | aggregation over bias, power | publication bias, p-hacked primaries |
| RCT / controlled experiment | 4 | randomized, blinded where possible | causal identification | wrong population, small n, no blinding |
| observational (cohort, pre/post with controls) | 3 | regression, diff-in-diff, matching | real-world effect, larger n | confounding, selection |
| case study / single instance | 2 | narrative + trace | existence proof, mechanism hint | no counterfactual, cherry-picked |
| expert opinion / survey | 1.5 | authority statement | plausibility, prior | incentives, no evidence shown |
| blog / anecdote / AI output | 1 | assertion | hypothesis only | no checkable trace |

Modifiers (applied after tier base):

- **Recency:** -0.25 per 4 years beyond 2 years old, capped -1. Use publication or data-collection date, whichever is newer.
- **Directness:** indirect (surrogate outcome, different population/setting) -0.5.
- **Bias risk:** low 0 / medium -0.5 / high -1. See checklist below.

Formula: `strength = clamp(tier_base - recency - indirect - bias, 1, 5)`.

## 5-point interpretation

- 4.5-5 decision-grade; cite and act.
- 3.5-4.4 usable with one caveat or replication.
- 2.5-3.4 suggestive; do not carry a high-stakes decision alone.
- 1.5-2.4 hypothesis; seek a better design.
- 1-1.4 anecdote/opinion; label as such.

## Bias checklist (mark H/M/L)

- Selection / survivorship (who is missing?)
- Funding / incentives (who benefits if believed?)
- p-hacking / HARKing / outcome switching
- Confounding not adjusted for
- Small-n / wide interval
- Publication / reporting bias (only positives cited)

## OpenAlex optional

If a DOI is given, `scripts/evidence.py` can accept `--openalex` to hint at citation count, but scoring stays offline — no network required for the score.

## One-row scorecard template

| Claim | Source (tier, N) | Effect | Year / direct? | Bias | Strength | Next probe |
|---|---|---|---|---|---|---|
| X reduces Y by 20% in Z | RCT n=200 | d=0.3, p=0.04 | 2024 direct | M | 3.5 | find replication / preregistration |
