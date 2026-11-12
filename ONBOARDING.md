# Onboarding — Critical Thinking Skills

You have a claim, a source, or a decision and you need to know whether it survives. This repo gives you eight evaluative methods plus a router, as portable `SKILL.md` files any agent harness can load — and offline helpers that produce the artifacts without an agent.

Three steps, each one copy-paste block. Stop when your question is answered. Full catalog and worked routes: [`thinking-router/references/catalog.md`](plugins/critical-thinking-skills/skills/thinking-router/references/catalog.md).

## Step 0 — 60 seconds: route one prompt (no agent)

No install, no network. Route the question before choosing a method:

```bash
python3 plugins/critical-thinking-skills/skills/thinking-router/scripts/route.py \
  --text "is this source credible, does the argument follow?" --json
```

Real output, trimmed to the decision fields:

```json
{
  "bucket": "sharper_judgment",
  "primary_bucket_label": "sharper judgment",
  "confidence": "high",
  "shortlist": ["evidence-appraisal", "argument-mapping"],
  "handoff": "Route: sharper judgment -> evidence-appraisal, argument-mapping"
}
```

That is the whole loop: `sharper_judgment` → `evidence-appraisal` first, `argument-mapping` as runner-up. The router scores five buckets — sharper judgment, better question, broader perspectives, stronger options, more ideas — and shortlists 1–2 methods. If `more ideas` wins, it hands off to the creative track instead. Read the routing rubric: [`thinking-router/references/routing.md`](plugins/critical-thinking-skills/skills/thinking-router/references/routing.md).

## Step 1 — 15 minutes: one skill, one artifact

Pick the bucket that matches your question and run exactly one helper. Every helper is offline and returns the artifact as text or `--json`.

### Sharper judgment → `evidence-appraisal`

Your claim: *"X reduces Y by 20% (n=40 blog post)."* Score it:

```bash
python3 plugins/critical-thinking-skills/skills/evidence-appraisal/scripts/evidence.py \
  --claim "Onboarding lifts 90-day retention by 20%" \
  --tier blog --n 40 --recency 7 --directness indirect --json
```

Expected artifact — a one-row scorecard with:

```json
"strength": 1.0,
"label": "anecdote/opinion: label it as such",
"next_probe": "find the primary study the post cites; score that instead"
```

Strength 1.0 is the point: a blog-tier, 7-year-old, surrogate metric buys almost nothing. The `next_probe` is your next action — find the RCT or preregistration. Re-run with `--tier rct --n 200` and watch the row move.

### Better question → `socratic-elenchus`

Your key term is undefined: *"engagement."*

```bash
python3 plugins/critical-thinking-skills/skills/socratic-elenchus/scripts/elenchus.py \
  --term "engagement" --definition "engagement = clicks per session" \
  --counterexample "a rage-click is a click but not engagement"
```

Expected artifact — a term card: diagnostics (circular? measurable?), definition tests, counterexample probes, and a fill-in operational definition. Complete it with indicator, unit, threshold, source, baseline window, and the observation that would count against it. Two informed people must apply it identically.

### Stronger bets → `decision-analysis`

Your choice: *Ship vs Wait*, with the retention bet on the line.

```bash
python3 plugins/critical-thinking-skills/skills/decision-analysis/scripts/decide.py \
  --options "Ship,Wait" --outcomes "hit,miss" --probs "0.6,0.4" \
  --utilities "100,0;20,20" --sensitivity
```

Expected artifact — an EV table with sensitivity:

```text
| Ship | 100 | 0 | 60.00 | 1 |
| Wait |  20 | 20 | 20.00 | 2 |
Rank stability: stable. Probe the largest swing first.
```

The ±20% sweep says the `hit` probability swings Ship's EV by 24 points — so the evidence score from Step 1, not the utility numbers, is what decides this bet.

## Step 2 — 60 minutes: chain skills on a claim you brought

Routing is cheap; a wrong frame is not. Take a real claim from your work — a vendor deck, a paper abstract, a metric your team repeats — and chain four methods, keeping each artifact separate:

1. `socratic-elenchus` — define the contested term operationally.
2. `evidence-appraisal` — score the source that asserts the claim.
3. `argument-mapping` — map claim → grounds → warrant; tag valid / plausible / gap.
4. `steelman-red-team` — strongest case for ¬P, then the pre-committed falsifier.

Each skill's process is in its `SKILL.md`; each helper is under `plugins/critical-thinking-skills/skills/<skill>/scripts/`. Record the chain on the board — one lane per method, filled in order:

```bash
open workspace/index.html     # macOS; xdg-open on Linux
# pick "critical-router" in the template dropdown → apply template → add notes
```

`workspace/boards/critical-onboarding.json` ships pre-filled: the claim in **Intake**, the score in **Sharper judgment**, the term question in **Better question**, the steelman in **Broader view**, the falsifying probe in **Stronger options**. Load it with `workspace/index.html?board=critical-onboarding`; edits persist to localStorage and export back to the file.

## Same prompts in Claude Code and Codex

The `SKILL.md` files are harness-agnostic; the helper commands are plain Python 3 with no network access. One install, either harness:

```bash
# Claude Code
/plugin marketplace add aleknitka/agent-critical-thinking-skills
/plugin install critical-thinking-skills@agent-critical-thinking-skills

# Codex / Pi / skills.sh
npx skills add aleknitka/agent-critical-thinking-skills
```

Run `python3 scripts/validate.py` after any edit — it checks manifests, frontmatter, and progressive-disclosure limits. More runnable examples: [`examples/gallery.md`](examples/gallery.md). Design rationale and the evidence-base caveats (Sio & Lortie-Forgues 2024, deflated g≈0.30): [`research/critical-thinking/plan.md`](research/critical-thinking/plan.md).
