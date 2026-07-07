# Exotic Thinking

Exotic Thinking is an agent skill for applying nonstandard reasoning lenses to
difficult problems without pretending the lens itself is evidence.

The lenses are structural prompts. They help expose missing evidence, strange
asymmetries, predictive consequences, and meta-level mistakes. They do not
create truth.

## Use It When

- Debugging has stalled under the ordinary frame.
- A strategy, postmortem, or architecture decision has hidden assumptions.
- A research synthesis needs several ways to notice gaps.
- A plan seems locally coherent but might be missing the negative space.
- Reasoning quality itself needs review.

Do not use every lens by default. Pick one to three that attack the actual
uncertainty.

## What The Package Includes

- `SKILL.md` - the lens-selection procedure and guardrails.
- `references/paradigm-catalog.md` - the eight lens catalog with prompts,
  failure modes, and output patterns.
- `scripts/self_test.py` - regression checks for catalog coverage, output shape,
  and no-magic-tool guardrails.
- `agents/openai.yaml` - skill metadata for runtimes that display skill cards.
- `SHA256SUMS.txt` - drift manifest.

## The Eight Lenses

| Lens | Question it asks |
|---|---|
| Abductive reasoning | What explanation best accounts for observations and absences? |
| Negative-space thinking | What should be present but is missing? |
| Predictive reasoning | What should happen next if this model is true? |
| Asymmetric belief | Which branch is more costly if wrong? |
| External memory binding | What prior artifact should anchor this reasoning? |
| Concurrent reasoning | Which branches can be explored independently? |
| Split reasoning | What is the object-level move and the meta-level correction? |
| Stigmergic thinking | What traces left by prior work should guide the next move? |

## Output Shape

```text
Lens:
Question asked:
Evidence considered:
Finding:
Decision impact:
Check or next action:
Unverified remainder:
```

If a lens changes the decision, follow it with an ordinary failable check.

## Install As An Agent Skill

```bash
git clone https://github.com/ap7x42a/exotic-thinking.git
cp -a exotic-thinking ~/.codex/skills/exotic-thinking
```

For project-local skill surfaces, copy the directory into the location your
runtime uses, such as `.agents/skills/exotic-thinking`.

## Verify The Package

```bash
python3 scripts/self_test.py
sha256sum -c SHA256SUMS.txt
```

## Limits

This is not a creativity costume or a substitute for verification. Lens outputs
are hypotheses, gaps, predictions, or anchors until evidence upgrades them.
