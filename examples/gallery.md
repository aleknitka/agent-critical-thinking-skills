# Example Gallery — Critical-Thinking Skills

One runnable prompt per skill plus an end-to-end chain. Copy the prompt into Codex or Claude Code after installing `critical-thinking-skills`; the listed skill(s) will handle the rest. Helpers are offline under `plugins/critical-thinking-skills/skills/<skill>/scripts/`.

> New? Start with **Quick start** below, then pick one category. Unsure which fits → run `thinking-router` (critical) first.

## Quick start (60 s)

```
# Claude Code
/plugin marketplace add aleknitka/agent-critical-thinking-skills
/plugin install critical-thinking-skills@agent-critical-thinking-skills

# Codex / Pi / any skills.sh harness
npx skills add aleknitka/agent-critical-thinking-skills
# Codex also discovers plugins/critical-thinking-skills/skills/*/SKILL.md from the skills path — no extra config.

# Then in any conversation:
> Help me think critically about this claim — not sure which method fits.
# → thinking-router (critical) triages into sharper judgment / better question / broader perspectives / stronger options
#   and hands off to 1–2 skills with your confirmation. Intake is carried forward.
```

Offline helpers you can run without an agent:

```bash
python plugins/critical-thinking-skills/skills/thinking-router/scripts/route.py --text "is this source credible, does the argument follow?"
python plugins/critical-thinking-skills/skills/evidence-appraisal/scripts/evidence.py --claim "X reduces Y by 20%" --tier rct --n 200 --json
python plugins/critical-thinking-skills/skills/bayesian-updating/scripts/bayes.py --prior 0.1 --lr 9 --json
python plugins/critical-thinking-skills/skills/fallacy-bias-spotting/scripts/fallacy.py --text "We tried it once and it failed, so it will always fail" --json
```

---

## 1 · Is the reasoning sound? — Sharper judgment

### Evidence appraisal — how much is this source worth?

**Prompt:**
> A vendor claims "our onboarding lifts 30-day retention 20% (n=40, blog post, 2019, surrogate metric)." Should we bet the quarter on it?

**Skill:** `evidence-appraisal` → tier (blog 1) × recency (−0.75) × indirect (−0.5) × bias (high −1) → strength ~1.0 + next probe ("find the RCT or preregistered replication").  
**Helper:** `python plugins/critical-thinking-skills/skills/evidence-appraisal/scripts/evidence.py --claim "onboarding lifts retention 20%" --tier blog --n 40 --recency 7 --directness indirect --bias high --json`  
**Expected artifact:** one-row scorecard (tier/N/effect/p/bias/strength) + the one probe that would move it one point.

### Argument mapping — does the reason support the claim?

**Prompt:**
> "All birds fly; penguins are birds; therefore penguins fly" — and our memo: "Retention dropped after the redesign, so the redesign caused it." Map both.

**Skill:** `argument-mapping` → Toulmin parse (claim/grounds/warrant/backing/qualifier/rebuttal) → validity tag (deductive valid/invalid, inductive strong/weak, abductive best/plausible).  
**Helper:** `python plugins/critical-thinking-skills/skills/argument-mapping/scripts/argmap.py --text "All birds fly; penguins are birds; therefore penguins fly" --json`  
**Expected artifact:** 6-column map + verdict `invalid — warrant "all birds fly" is false` or `gap — warrant W needed`.

### Fallacy & bias spotting — name the failure mode

**Prompt:**
> "We tried the new invite once and it failed, so it will always fail. Everyone knows it." What breaks here?

**Skill:** `fallacy-bias-spotting` → scan 20 fallacies × 20 biases → Hit/Maybe/No (keep ≤3) + one-line why + de-bias move (consider the opposite / base rate / reference class).  
**Helper:** `python plugins/critical-thinking-skills/skills/fallacy-bias-spotting/scripts/fallacy.py --text "We tried it once and it failed, so it will always fail" --json` (or `--list` for the 40-item catalog)  
**Expected artifact:** annotated draft with 2–3 highest-risk tags (e.g. hasty generalization, availability) + fixed revision.

---

## 2 · Are we asking the right thing? — Better question

### Socratic elenchus — what do you mean by X, precisely?

**Prompt:**
> The brief says "improve engagement." What do we actually mean? No slogans — one testable sentence that would survive a counterexample.

**Skill:** `socratic-elenchus` → definition → counterexample (over/under-inclusive) → revision → operational definition + judge-agreement test.  
**Helper:** `python plugins/critical-thinking-skills/skills/socratic-elenchus/scripts/elenchus.py --term "engagement" --definition "users like the product" --json`  
**Expected artifact:** term card (term → initial def → counterexample → revised one-sentence def → measurement/decision rule + test).

### Evidence + argument + Socratic (chain)

**Prompt:**
> Before we pick a solution, clarify "activation" and check whether our evidence for "invites carry intent" even supports the claim.

**Chain:** `socratic-elenchus` (operationalize "activation") → `evidence-appraisal` (score the invite-intent source) → `argument-mapping` (does the warrant "invite intent → activation" hold?).

---

## 3 · What view are we missing? — Broader perspectives

### Steelman & red-team — what's the strongest case against us?

**Prompt:**
> We believe "remote work hurts productivity." Steelman the best case for the other side, then red-team us — and name what would make us abandon the claim.

**Skill:** `steelman-red-team` → strongest ¬P + charity test ("would its proponent sign this?") → 5 attack vectors (evidence/logic/incentives/alternative/cost) ranked fatal/serious/survivable → falsifier pre-commit.  
**Helper:** `python plugins/critical-thinking-skills/skills/steelman-red-team/scripts/redteam.py --claim "Remote work hurts productivity" --json`  
**Expected artifact:** steelman statement + 3–5 attack rows + `I abandon P if ___ by ___` + the result we'd be tempted to explain away.

---

## 4 · Which bet is best? — Stronger options

### Bayesian updating — how much should this evidence move us?

**Prompt:**
> Base rate of this kind of lift is 10%. A pilot with LR 9 just came back positive. How much should we update? And is it worth another probe?

**Skill:** `bayesian-updating` → prior (from base rate) → likelihood ratio → posterior in odds form + base-rate flag + value of information.  
**Helpers:**
```bash
python plugins/critical-thinking-skills/skills/bayesian-updating/scripts/bayes.py --prior 0.1 --lr 9 --json
python plugins/critical-thinking-skills/skills/bayesian-updating/scripts/bayes.py --prior 0.01 --sensitivity 0.9 --specificity 0.8 --json
python plugins/critical-thinking-skills/skills/bayesian-updating/scripts/bayes.py --prior 0.2 --lrs "4,0.5,2" --base-rate --json
```
**Expected artifact:** prior → LR → posterior table + `naive LR/(1+LR)` gap + decision threshold + next probe worth it?

### Calibration & forecasting — are we calibrated or just confident?

**Prompt:**
> We said "70% chance we ship by June 30." Are we 70% right when we say 70%? Score us and give us a log we can actually keep.

**Skill:** `calibration-forecasting` → resolvable dated forecasts (p in 0.01–0.99) → resolve vs criteria → Brier score + skill vs base rate + calibration curve (bins 0–0.2 … 0.8–1.0).  
**Helper:** `python plugins/critical-thinking-skills/skills/calibration-forecasting/scripts/calibrate.py --demo --json` (or `--forecasts log.json --markdown`)  
**Expected artifact:** forecast log (prediction / p / resolves / o / Brier) + Brier + skill score + per-bin gaps + 3 new live predictions.

### Decision analysis — which option bets best?

**Prompt:**
> Ship now vs wait a quarter: hit/miss at 60/40, utilities 100/0 vs 20/20. Price the bet and tell us what would flip it.

**Skill:** `decision-analysis` → options × outcomes × probabilities × utilities → EV + ranking + margin → sensitivity sweep (±20%, tornado) → recommendation + cheapest probe + pre-committed decision rule.  
**Helper:** `python plugins/critical-thinking-skills/skills/decision-analysis/scripts/decide.py --options "Ship,Wait" --outcomes "hit,miss" --probs "0.6,0.4" --utilities "100,0;20,20" --json --sensitivity`  
**Expected artifact:** EV table + ranking with gap + tornado (ordered by EV swing, flips marked) + probe.

---

## End-to-end chain (copy-paste ready)

> You are the `thinking-router` (critical). Triage whether we need sharper judgment, a better question, a broader perspective, or stronger options for: "Onboarding drops 32% before first value; invites carry no intent, activation is uninstrumented, and a vendor blog claims a 20% lift (n=40)." Score 8 methods, shortlist 2–3, then hand off to the primary with user confirmation. If we pick evidence-appraisal, carry the intake forward; end with a probe.
>
> After the router hands off, continue as that skill and produce its artifact (scorecard, map, scan, posterior, definition, steelman, Brier log, or EV sheet) — one step at a time.

---

## Where to look next

- Method catalog with triggers + 5th-bucket map: `plugins/critical-thinking-skills/skills/thinking-router/references/catalog.md`
- Routing rubric and worked routings: `plugins/critical-thinking-skills/skills/thinking-router/references/routing.md`
- Agent↔human board (9 critical templates): `workspace/index.html` → template picker → `critical-router`, `evidence-appraisal`, etc. (agents read/write `workspace/boards/<id>.json`)
- Offline helpers: `plugins/critical-thinking-skills/skills/<skill>/scripts/` (`--help`, `--json`, `--list` where applicable)
- Design principles + provenance (with evidence honesty): each skill's `references/provenance.md`

---

## Cross-harness note — Codex

All 8 `SKILL.md` files are harness-agnostic (Claude Code, Codex, OMP, Pi all load them from `plugins/critical-thinking-skills/skills/*/SKILL.md`). No workflow file is required; the router composes skills by handoff. If you use Codex, add this repo to your skills path or install via `npx skills add` — the helpers are the same `python scripts/*.py` offline tools.
