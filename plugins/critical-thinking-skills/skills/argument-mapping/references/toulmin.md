# Toulmin Model — Six Slots

From Toulmin (1958) *The Uses of Argument*; modernized by Walton (2008) and Ennis.

| Slot | Question it answers | Marks in text |
|---|---|---|
| **Claim** | What is being sold? | "therefore", "so", "hence", "should" |
| **Grounds** | What facts/reasons are offered? | data, examples, observations, premises |
| **Warrant** | What bridge rule turns grounds into claim? | often unstated — "if grounds then claim" |
| **Backing** | Why is the warrant credible? | law, mechanism, study, principle |
| **Qualifier** | How strongly is the claim held? | "probably", "certainly", "in most cases", absence = "always" |
| **Rebuttal** | When does it fail? | "unless", "except when", "if not" |

## How to use

1. Copy one sentence per slot. If a slot is empty, write "unstated".
2. The warrant is the test: state it as "if G then C" and ask whether you believe it. Most invalid arguments have a false or overbroad warrant, not false grounds.
3. Validity tag follows from warrant + backing:
   - **Deductive:** premises guarantee the conclusion? valid / invalid (+ counterexample).
   - **Inductive:** premises make it probable? strong / weak (sample size, representativeness).
   - **Abductive:** is this the best explanation among rivals? best / plausible / weak.

## Worked examples

### 1. Deductive (invalid)

Text: "All birds fly. Penguins are birds. Therefore penguins fly."

- Claim: penguins fly.
- Grounds: all birds fly; penguins are birds.
- Warrant: if all birds fly and X is a bird, X flies.
- Backing: "birds fly" — false universal premise.
- Qualifier: none → "always".
- Rebuttal: flightless birds.
- Verdict: **invalid — warrant false** (false universal). Counterexample: penguin.

### 2. Inductive (weak)

Text: "This feature worked for 3 early adopters, so it will work for all users."

- Claim: the feature will work for all users.
- Grounds: 3 early adopters succeeded.
- Warrant: what holds for 3 early adopters holds for all users.
- Backing: none.
- Qualifier: "will" (certainty).
- Rebuttal: later adopters differ in intent, skill.
- Verdict: **weak inductive — warrant overgeneralizes** (needs base rate, larger sample, backing). Gap: "early adopters represent the population".

### 3. Abductive (plausible, not best)

Text: "Retention dropped after the redesign, so the redesign caused it."

- Claim: redesign caused the retention drop.
- Grounds: timing correlation.
- Warrant: post hoc → causation (correlation implies cause).
- Backing: none beyond sequence.
- Qualifier: implied "therefore caused".
- Rebuttal: seasonality, invite quality, cohort mix.
- Verdict: **weak causal abduction — correlation ≠ causation**. Needs rival explanations tested; plausible but not best until alternatives eliminated.
