# Calibration & Forecasting — Method

From Tetlock & Gardner (2015) *Superforecasting*; Brier (1950); Kahneman on overconfidence.

## Brier score

For forecasts `p_i` in [0,1] with outcomes `o_i` in {0,1}:

```
Brier = mean((p - o)^2)    in [0,1], lower is better
```

- Perfect: 0. Baseline "always 0.5": 0.25. "Always base rate r": `r(1-r)` in expectation.
- Skill score: `1 - Brier / Brier_baseline` (positive means better than baseline).

## Calibration vs resolution

- **Calibration:** do events given p≈0.7 happen ~70% of the time? Plot mean p per bin vs observed frequency; diagonal = calibrated.
- **Resolution (sharpness):** are forecasts away from 0.5 (useful) or vague?

Bins convention: [0,0.2), [0.2,0.4), [0.4,0.6), [0.6,0.8), [0.8,1.0].

## Reference class

Before adjusting for case specifics, state the base rate: "what fraction of comparable cases did X?" Overconfidence usually enters before the adjustment, not after.

## Overconfidence

Kahneman — most forecasts are too narrow and too certain. Guardrails: never 0 or 1; write a resolvable claim with date and criterion; let the score do the talking.

## Two worked examples

1. Claims at 0.7, outcomes 1,0,1,1,0 → Brier = ((.09)+(.49)+(.09)+(.09)+(.49))/5 = 0.25. Baseline 0.25 → skill 0. Needs more than 5 forecasts to judge.
2. Well-calibrated 0.8 forecaster over 100 cases → ~80 hits; same mean accuracy but better Brier than a 0.6/0.9 mixture that averages 0.8 — calibration rewards honest binning.
