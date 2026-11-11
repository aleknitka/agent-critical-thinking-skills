# Steelman, Red-Team, and Pre-commit

## Steelman vs strawman

- **Strawman:** restate the rival claim in its weakest form, then refute that.
- **Steelman:** restate the rival claim `¬P` in its strongest form — stronger than any critic has put it — with its best premises and the concessions it is owed. Test: *would a smart proponent of ¬P sign this as fair?*

Technique: principle of charity (Davidson). Write ¬P as one sentence, then 3 premises that would make it true and one concession `P` must grant.

## Adversarial collaboration

Tetlock — adversarial collaboration: both sides agree beforehand on what evidence would change the answer. Zenko (2015) *Red Team Field Guide*: red-team the claim, not the claimant; rank attack vectors by severity.

## Five attack vectors

1. **Evidence** — weakest empirical link; what would an expert cite against it?
2. **Logic** — hidden premise, equivocation, correlation-as-cause, base-rate skip.
3. **Incentives** — who benefits if P is believed? Does that shape what is shown?
4. **Alternative explanation** — what other cause produces the same observation?
5. **Cost** — what does P cost if wrong (money, trust, optionality, irreversibility)?

Rank each: fatal / serious / survivable. Fix or price the top two.

## Falsification pre-commit (Popper)

Before defending `P`, write: "I abandon `P` if ___ by ___ (date/threshold)." Name the observation you would otherwise rationalize. If nothing could change your mind, the claim is identity, not belief.

## Worked example 1

Claim `P`: "Our new onboarding lifts 30-day retention 10%."

- Steelman `¬P`: "The lift is cohort noise; onboarding changes do not move 30-day retention without an intent-carrying invite."
  - Premises: early adopters self-selected; invite carries no intent signal; no holdout isolates the change.
  - Concession owed: activation did rise — but activation ≠ retention.
- Attacks: evidence — pilot n small, no prereg. Logic — post hoc. Alternative — seasonal cohort. Incentives — shipping bias. Cost — rollout hides real fix.
- Falsifier: holdout of one full cohort shows <2 pp lift at p>0.2 by 2026-12-31.

## Worked example 2

Claim `P`: "Remote work hurts productivity."

- Steelman: "Measured productivity in complex collaborative work is lower when co-location cues and informal coordination are removed, holding selection constant."
- Attacks: evidence — measure is proxies; logic — selection (who is remote?); alternative — tooling/management; incentives — office lease; cost — talent loss if wrong.
