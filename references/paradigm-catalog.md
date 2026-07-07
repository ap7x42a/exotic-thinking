# Paradigm Catalog

## Abductive Reasoning

Use when observations need an explanation. Include absences: what did not happen
can be as important as what did. Compare explanations by coverage, simplicity,
and testable predictions.

## Negative-Space Thinking

Use when the missing thing matters: absent logs, absent tests, absent failure
signals, absent user paths, absent owners. Ask what a healthy system would have
left behind.

## Predictive Reasoning

Use when a theory needs a forward test. If this explanation is true, what should
happen next, what should be measurable, or what should fail under a countercase?

## Asymmetric Belief

Use when branches have different costs if wrong. A 60% likely low-cost branch may
matter less than a 30% likely branch with catastrophic downside.

## External Memory Binding

Use when reasoning should be anchored to prior artifacts: specs, decisions,
tests, incident reports, measurements, or handoffs. Name the artifact and what
it constrains.

## Concurrent Reasoning

Use when independent branches can be explored without sharing mutable state.
Separate hypotheses, assign checks, and merge only after each branch reports
receipts.

## Split Reasoning

Use when the object-level task and the meta-level process both matter. Example:
fix the bug, and also fix the test gap that let the bug survive.

## Stigmergic Thinking

Use when prior work left traces: TODOs, retries, scaffolding, logs, abandoned
branches, metrics, or operator notes. Treat traces as evidence to inspect, not
orders to obey.
