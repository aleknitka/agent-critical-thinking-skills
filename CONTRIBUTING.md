# Contributing

Critical-thinking micro-skills for agent harnesses. One skill = one directory: a lean `SKILL.md`, `references/` loaded on demand, `scripts/` offline helpers.

## Progressive disclosure (non-negotiable)

1. **Frontmatter `description`** is always in context. Say what the skill does and when to use it, with trigger phrases. Max 1024 chars.
2. **`SKILL.md` body** loads on trigger. Keep it a process: target under 80 lines, hard cap 500. No essays.
3. **`references/*.md`** load only when needed. One topic per file, linked directly from `SKILL.md`, no nested chains.

Start from [templates/skill/SKILL.md](templates/skill/SKILL.md).

## Add a skill

```bash
cp -r templates/skill plugins/critical-thinking-skills/skills/<name>
```

1. **`SKILL.md`** — `name` must equal the directory name, lowercase-hyphenated. Every relative link must resolve.
2. **`references/provenance.md`** — trace the method to its lineage (Facione, Paul-Elder, Halpern, or the nearest primary source) and state the honest limits: no RCT behind the weights, tier ≠ truth, heuristic not measurement.
3. **`references/<topic>.md`** — one topic per file, linked from `SKILL.md`.
4. **`scripts/*.py`** — offline, stdlib only, no network. Support `--json`, `--help`, and `--list` where a catalog exists. Return non-zero on bad input. `chmod +x`.
5. **Workspace board** (only if the skill needs lanes) — add an entry to `TEMPLATES` in [workspace/app.js](workspace/app.js) and to the `template` enum in [workspace/boards/_schema.json](workspace/boards/_schema.json).
6. **Validate** — `python3 scripts/validate.py` must print `OK`.

## Version bump — all four manifests

Adding a skill or changing behavior bumps every manifest in lockstep:

- `plugins/critical-thinking-skills/.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`
- `.omp-plugin/marketplace.json`
- `pyproject.toml`

## Harness-agnostic

`SKILL.md` is plain Markdown plus YAML frontmatter — no harness API, no tool names. The same file works in Claude Code (`/plugin install`), Codex/OMP/Pi (`npx skills add`), and any harness that discovers `skills/*/SKILL.md`. Keep harness-specific glue out of a skill.

## Writing style

Terse, evidence-first. Name the failure mode the skill prevents, show the artifact it produces, then the probe that would falsify it. Bullets over paragraphs. No marketing filler, no "unlock", no hype adjectives.

## Other contributions

- **Board templates** — a new lane set in `workspace/` needs both the app template and the schema enum.
- **Router coverage** — new trigger phrasing or a missing hand-off goes in `thinking-router` and its `references/catalog.md`.
- **Bug reports** — include the exact command, the output, and expected vs actual. A failing helper is a test case, not an opinion.

## PR checklist

- `python3 scripts/validate.py` prints `OK`
- no `__pycache__`, `*.pyc`, `.venv`, or secrets in the diff
- helpers are executable and run with stdlib only (`python3 <script> --help`)
- `references/provenance.md` cites lineage and discloses limits honestly
- README and CHANGELOG updated when user-facing behavior changes

## Repo map

```
plugins/critical-thinking-skills/skills/<skill>/   SKILL.md, references/, scripts/
templates/skill/                                   new-skill scaffold
workspace/                                         shared boards + vanilla-JS UI
scripts/validate.py                                manifests, frontmatter, links
research/critical-thinking/plan.md                 coverage audit + ranking rationale
```

Why these 8 skills and not others: [research/critical-thinking/plan.md](research/critical-thinking/plan.md) (Facione / Paul-Elder / Halpern gap analysis).
