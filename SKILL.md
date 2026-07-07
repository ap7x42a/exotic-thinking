---
name: exotic-thinking
description: >-
  Use when a problem benefits from nonstandard reasoning lenses: abductive,
  negative-space, predictive, asymmetric-belief, external-memory-binding,
  concurrent, split-level, or stigmergic thinking. Apply these as structural
  analysis prompts, not as magical tools. Useful for difficult debugging,
  strategy, research synthesis, postmortems, architecture, and reviewing
  reasoning for gaps or hidden assumptions.
metadata:
  self_test: "python3 scripts/self_test.py"
---

# Exotic Thinking

Exotic thinking is a set of reasoning lenses. Each lens asks a different
question about the same problem structure. The point is not to sound unusual; it
is to expose gaps that a single ordinary frame tends to hide.

Use one to three lenses that fit the task. Do not run all eight by default.

## The Eight Lenses

See `references/paradigm-catalog.md` for details.

| Lens | Use it to ask |
|---|---|
| Abductive reasoning | What explanation best accounts for the observations and absences? |
| Negative-space thinking | What should be present but is missing? |
| Predictive reasoning | What should happen next if this model is true? |
| Asymmetric belief | Which branch carries more consequence if wrong? |
| External memory binding | What prior artifact should anchor this reasoning? |
| Concurrent reasoning | Which branches can be explored independently? |
| Split reasoning | What is the object-level move and what is the meta-level correction? |
| Stigmergic thinking | What traces left by prior work should guide the next move? |

## Procedure

1. State the ordinary frame first: the problem, evidence, and current favorite
   explanation.
2. Choose the lens or lenses that attack the weakest part of that frame.
3. For each lens, produce concrete observations, not vibes.
4. Mark outputs as hypotheses, gaps, predictions, or anchors.
5. Run a failable check when a lens changes the decision.
6. Synthesize: what changed, what stayed unproven, and what action follows.

## Guardrails

- These lenses do not generate truth. They generate structured questions.
- Do not treat a lens name as evidence.
- Do not invent hidden systems, actors, or motives without evidence.
- Do not replace ordinary verification with exotic vocabulary.
- Prefer the smallest lens that exposes the actual uncertainty.

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

## Done Means

- The selected lenses match the uncertainty.
- Each finding maps back to evidence or is explicitly marked as a hypothesis.
- At least one ordinary verification step follows any decision-changing finding.
- The final synthesis is actionable and does not overclaim.
