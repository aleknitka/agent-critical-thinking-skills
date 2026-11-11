# Routing — Scoring Rubric

## Buckets

Five buckets; every prompt is scored 0-1 per bucket by keyword + intent cues, then methods are ranked within buckets.

| Bucket | Cues |
|---|---|
| sharper_judgment | credible, source, evidence quality, valid, fallacy, bias, warrant, argument, trust, proof |
| better_question | define, what do you mean, vague, ambiguous, concept, precisely, operationalize, clarify, question |
| broader_perspectives | other side, counter, steelman, red team, dissent, alternative view, strawman, adversarial |
| stronger_options | prior, base rate, Bayes, update, confidence, forecast, Brier, expected value, choose, bet, uncertainty |
| more_ideas | generate, brainstorm, ideas, creative, variations (→ creative track, out of scope) |

## Scoring

Keyword hits per skill normalized by trigger-list length + intent overlap with bucket; top bucket seeds the shortlist, second bucket is the runner-up. Tie-break: more specific trigger wins (e.g. "Brier score" > "confidence").

## Worked routings

1. "Is this blog a good source for the claim that X reduces Y?" → sharper_judgment → evidence-appraisal (primary), fallacy-bias-spotting (Maybe).
2. "Does this reasoning actually follow?" → sharper_judgment → argument-mapping, fallacy-bias-spotting.
3. "What do we even mean by engagement?" → better_question → socratic-elenchus.
4. "Steel-man the opposition before we commit." → broader_perspectives → steelman-red-team.
5. "How much should this trial move our belief? Prior 10%, new LR 9?" → stronger_options → bayesian-updating.

Helper `scripts/route.py` implements this rubric heuristically.
