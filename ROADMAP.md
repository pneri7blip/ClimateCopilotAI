# ClimateCopilot AI Roadmap

This roadmap describes a small, honest path from the current prototype to an evaluable AI workflow. Completed items refer only to behavior present in the repository.

## Phase 1 — Foundation (current)

- [x] Define an environmental/compliance workflow direction
- [x] Define a structured `ComplianceRisk` output
- [x] Preserve source evidence in the output
- [x] Return no finding for unsupported text instead of inventing one
- [x] Add a runnable example and unit tests

## Phase 2 — Prototype

- [ ] Add document ingestion while preserving source boundaries
- [ ] Expand the set of supported compliance-risk patterns
- [ ] Add an optional LLM adapter with schema-constrained output
- [ ] Add human-reviewable structured report generation

## Phase 3 — Evaluation

- [ ] Build a representative labelled dataset
- [ ] Measure extraction accuracy and evidence recall
- [ ] Test hallucination resistance and handling of `Not specified.`
- [ ] Compare prompting strategies and models

## Explicitly out of scope for now

Dashboards, authentication, databases, public APIs, automated decisions, and production deployment are not current objectives. They should not be added before the extraction contract and evaluation methodology are reliable.
