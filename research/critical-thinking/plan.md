# Critical-Thinking Track — Plan for `thinking-skills`

**Question:** repo is `thinking-skills` but 40/40 are creative-leaning. Is there a critical-thinking gap? What would a complementary track look like?

**Verdict: Yes — systematic gap.** Current catalog = 88% generative/divergent. Critical core is thin, covered only at the edges.

## 1. Coverage audit (40 skills → critical frameworks)

Frameworks: **Facione** (6: interpretation, analysis, evaluation, inference, explanation, self-regulation), **Paul-Elder** (8 elements × 9 standards), **Halpern** (verbal reasoning, argument analysis, hypothesis testing, likelihood, decision making).

| Buckets | Creative share | Critical share |
|---|---|---|
| Reframe (6) | 1 (lateral) | 5 partial (challenge-assumptions, first-principles, question-storming, abstraction-laddering, inversion) |
| Generate (14 incl. 4 ext) | 13 | 1 (systematic-inventive-thinking has constraint discipline) |
| Explore (10 incl. 3 ext) | 7 | 3 partial (stakeholder-perspectives, six-hats Black, causal-loop partial causality) |
| Harden / Decide (8 incl. 2 ext) | 2 | 6 partial (double-diamond, triz, premortem, portfolio, NGT, dot-voting — but all *ranking*, not *epistemic* evaluation) |

**Covered (thinly):**
- Assumptions → `challenge-assumptions` (hidden-belief inventory, no formal argument map)
- Point-of-view → `stakeholder-perspectives`, `six-thinking-hats` (serial modes, no steelman discipline)
- Implications → `futures-wheel`, `scenario-planning` (consequence rings, not logical entailment)
- Systems inference → `causal-loop-diagram` (feedback, not deductive validity)
- Decision packaging → `options-portfolio`, `dot-voting`, `NGT` (votes, not EV/expected utility)

**Partial / weak:**
- Facione *analysis/evaluation/explanation*: no argument structure, no warrant/backing check
- Paul-Elder *information/concepts/inference*: no source credibility, no definitional clarity, no validity check
- Halpern *hypothesis testing / likelihood*: `premortem` touches calibration, but no base-rate / Bayesian move
- Self-regulation: six-hats Blue + premortem hint at metacognition, no calibration log

**Absent (8 clean gaps):**
1. **Evidence appraisal** (is this source/claim worth how much?)
2. **Argument mapping & validity** (does the reason actually support the claim?)
3. **Fallacy & cognitive-bias detection** (named failure modes)
4. **Probabilistic / Bayesian updating** (base rates, likelihood ratios)
5. **Socratic conceptual clarity** (what do you mean by X, precisely?)
6. **Steelman & red-team** (strongest counter-position, not strawman)
7. **Calibration & forecasting** (confidence vs accuracy, Tetlock)
8. **Decision analysis & measurement validity** (EV, operationalization, Goodhart)

No existing skill prevents: *sounding persuasive while being invalid, citing a weak source as strong, updating too far or not at all, using an undefined term through a whole meeting, strawmanning the dissent, or choosing without pricing risk.*

## 2. Why a critical track — and why not just "more creative"

- **Demand:** your stated audience = "any knowledge worker who wants better results from AI — brainstorming *and* development, evaluation, mental experiments." Creative alone leaves evaluation to vibes.
- **Evidence:** Sio & Lortie-Forgues 2024 (meta, 169 studies): creativity-training raw g≈0.53 deflates to 0.29–0.32 after bias correction. Halpern-style critical-thinking instruction shows similar modest but *transferable* gains when framed as explicit procedures with practice — exactly the skill format this repo already scales. Teaching a named fallacy or a Bayes update is more scriptable for agents than "be more critical."
- **Agent fit:** critical moves are highly automatable — classify argument structure, score source credibility, compute a likelihood ratio, surface a steelman — all offline, seeded, `scripts/*.py` friendly. Creative generation already has this; critical evaluation is the missing complement.
- **Non-overlap discipline:** each proposed skill below is bounded against its nearest creative neighbor (e.g., `steelman-red-team ≠ premortem`, `evidence-appraisal ≠ analogical-thinking`, `bayesian-updating ≠ scenario-planning`).

## 3. Ranked critical track — 8 skills (proposed 0.9.0–1.0.0)

Ranked by: evidence base × non-overlap × agent-scriptability × offline helper leverage.

| Rank | Slug | Family | When to use | One-line artifact | Why build (gap + fit) | Key refs |
|---|---|---|---|---|---|---|
| 1 | `evidence-appraisal` | Evaluation (Facione/Paul-Elder *information*) | A claim cites a source — how much should you trust it? | Source scorecard + claim strength (1–5) + what would change your mind | **Largest gap.** `papers.md` has 20 papers but no skill uses them; every generative skill can hallucinate citations. Highest agent leverage: metadata → score. | Facione 1990 Delphi; Paul-Elder *information*; Ioannidis 2005; OpenAlex `W4407*` methods |
| 2 | `argument-mapping` | Analysis | A paragraph sounds persuasive — does it *follow*? | Claim–reason–warrant–backing map + validity tag (deductive/inductive/abductive) | Directly fills Facione *analysis*; nothing maps structure today. Prevents rhetoric→truth slippage. | Toulmin 1958; Walton 2008 *Informal Logic*; Ennis 1987 |
| 3 | `fallacy-bias-spotting` | Self-regulation | Draft feels right but might be systematically wrong | Annotated fallacy/bias sheet (20 fallacies × 20 biases, Hit/Maybe/No) + de-bias prompt | Most teachable critical skill (naming beats nagging). Halpern core; scannable by agent. | Kahneman 2011; Tversky & Kahneman 1974; Hamblin 1970; Halpern 2014 |
| 4 | `bayesian-updating` | Inference / Likelihood | Prior belief + new evidence → how much to move? | Prior → likelihood ratio → posterior + base-rate check + value of information | Scenario-planning does *possibilities*; this does *probabilities*. Agent can compute. | Bayes; Tetlock 2005/2015; Kahneman Ch.30 |
| 5 | `socratic-elenchus` | Conceptual clarity | A key term is used but never defined | Socratic chain: definition → counterexample → revision → operational definition | Paul-Elder *concepts* is entirely absent. Grosu? No — pure. | Paul & Elder 2006; Ennis 1996 |
| 6 | `steelman-red-team` | Fair-minded evaluation | Critique feels weak / strawman; need strongest counter | Steelman (strongest P) + red-team attack + pre-commit to what would falsify | `premortem` = "we failed"; this = "they're right." Covers intellectual empathy. | Paul-Elder fair-mindedness; Red Team Field Guide (Zenko 2015); Tetlock *adversarial collaboration* |
| 7 | `calibration-forecasting` | Self-regulation | Confidence ≠ accuracy; need accountable forecasts | Brier-scored forecast + calibration curve + 3 testable predictions | Extends `premortem` from one hindsight to repeated foresight. Agent can track. | Tetlock & Gardner 2015; Kahneman *overconfidence*; Facione self-regulation |
| 8 | `decision-analysis` | Decision making | Choose under uncertainty with stakes | EV sheet (options × outcomes × probs × utilities) + sensitivity + next probe | `options-portfolio` keeps *variety*; this prices *risk*. Complements, not duplicates. | Halpern Ch.10; Howard & Matheson 1984; Arkes & Blumer |

Runners-up (v1.1): `measurement-validity` (operationalization, construct validity, Goodhart — Stevens 1946) and `dialectical-reasoning` (thesis–antithesis–synthesis).

### Router placement

Current router has 4 buckets: better question / more ideas / broader perspectives / stronger options. Critical skills distribute, but a **5th bucket `sharper judgment`** (Facione evaluation + Paul-Elder standards) makes the split legible and lets `thinking-router` score distinctly:

- `evidence-appraisal`, `argument-mapping`, `socratic-elenchus` → **better question** (reframe with rigor) *and* `sharper judgment`
- `bayesian-updating`, `calibration-forecasting`, `decision-analysis` → **stronger options** *and* `sharper judgment`
- `fallacy-bias-spotting`, `steelman-red-team` → **broader perspectives** *and* `sharper judgment`

Catalog goes 38 methods → **46** (8 added); skills 40 → **48**. Keep creative:critical ≈ 1:1 at the router, not 9:1.

## 4. Top-3 detailed (intake → artifact → helper)

### 1) `evidence-appraisal` — "is this worth how much?"

- **Failure it prevents:** treating a blog post, a preprint, and a meta-analysis as equal citations.
- **Intake (3 min):** claim as 1 sentence + cited source type + what hangs on it.
- **Process:** source tier (meta > RCT > observational > case > expert/blog) × recency × directness × bias risk → claim strength 1–5 + *what evidence would move it one point*.
- **Artifact:** one-row scorecard per claim (tier, N, effect, p/bias, strength, next probe).
- **Helper:** `scripts/evidence.py --claim "X" --source doi:… --tier preprint --json` → score + checklist (OpenAlex lookup optional).

### 2) `argument-mapping` — "does the reason support the claim?"

- **Failure:** persuasive paragraph with no valid inference.
- **Process:** Toulmin parse (claim, grounds, warrant, backing, qualifier, rebuttal) → validity tag (deductive=valid/invalid, inductive=strong/weak) → missing warrant hunt.
- **Artifact:** map table (6 columns) + verdict: `valid / plausible / gap — warrant W needed`.
- **Helper:** `scripts/argmap.py --text "…" --json` → labeled spans + fallacy hint.

### 3) `fallacy-bias-spotting` — "name the failure mode"

- **Failure:** systematic error invisible because unnamed.
- **Process:** scan against 20 fallacies (strawman, equivocation, post hoc…) + 20 biases (anchoring, availability…) → tag Hit/Maybe/No + one-line why + de-bias move (e.g., "consider the opposite").
- **Artifact:** annotated draft with 2–3 highest-risk tags + fixed revision.
- **Helper:** `scripts/fallacy.py --text "…" --list --json` — seeded word-bank stimulus if needed.

## 5. Provenance & evidence honesty

- Do **not** promise large creativity gains: cite Sio 2024 deflated g≈0.3 (see `papers.md:29`).
- Trace every critical move to *provenance.md*: Toulmin/Walton for argument, Kahneman/Tversky for bias, Bayes/Tetlock for updating, Paul-Elder for Socratic/steelman — same disclosure discipline as the 11 research extensions.
- Flag `papers.md` gap §3 honestly: "no RCTs isolating SCAMPER/morph/futures-wheel" extends to any new critical skill; present as structured heuristics, not proven boosters.

## 6. Minimal plan (what to ship, in order)

1. **Ship `evidence-appraisal` + `argument-mapping`** first (6 families → 0 critical; these two close analysis+evaluation cheapest).
2. **Then `fallacy-bias-spotting` + `bayesian-updating`** (highest agent-scriptability).
3. **Then `socratic-elenchus` + `steelman-red-team`** (dialogical pair).
4. **Finally `calibration-forecasting` + `decision-analysis`** (quantified track, needs the first six as prerequisites).

Update `thinking-router` catalog 38→46, README toolkit + extended table (now 13 research-sourced with these 8), gallery §5→§6 with critical prompts, `CHANGELOG [0.9.0]` with evidence citations, bump `0.8.0→0.9.0`.

If bounded: ship 1+3 (`evidence-appraisal` + `fallacy-bias-spotting`) — they close the widest gaps with zero overlap and maximal offline helper reuse.

**Referred to if asked:** `megamouth/research/critical-thinking/evaluations/` (full Facione×Paul-Elder×Halpern mapping per skill) + `.agents/skills/literature-search-openalex` for OpenAlex IDs.
