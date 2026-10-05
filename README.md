# ClimateCopilot AI

**An early-stage, evidence-first workflow prototype for environmental compliance.**

ClimateCopilot explores how AI-assisted workflows could help environmental consultants turn inspection notes into structured, reviewable findings. The repository currently contains a small, dependency-free extraction scaffold: it recognizes one supported hazard-label example, preserves the matching source evidence, defaults unspecified actions to `Not specified.`, and validates that the evidence came from the input text.

> **Status: early-stage prototype.** This is a learning and workflow-design project, not a production compliance system and not a substitute for professional environmental judgment.

## Why this problem matters

Environmental compliance work often starts with inspection reports, PDFs, spreadsheets, emails, and other unstructured information. A useful assistant should make findings easier to review without hiding the source text or inventing actions that were not stated.

## Current approach

The project uses a deliberately small contract that a future LLM adapter could be evaluated against:

1. Accept inspection text.
2. Extract a structured risk only when the supported pattern is present.
3. Preserve the source evidence.
4. Represent unknown actions explicitly as `Not specified.`
5. Reject unsupported text instead of fabricating a finding.
6. Validate that the evidence is present in the source.

The current implementation is **deterministic Python rules**, not a live LLM integration. That boundary is intentional: it keeps the demo honest and makes the expected behavior easy to test before adding model variability.

## Example workflow

```text
Inspection report
        ↓
Supported-pattern extraction
        ↓
Structured compliance risk
        ↓
Evidence validation
        ↓
Reviewable JSON output
```

### Example

**Input**

```text
Two containers of solvent waste were found without the required hazard labels.
```

**Structured output**

```json
{
  "risk": "Missing hazard labels on solvent waste containers",
  "evidence": "Two containers of solvent waste were found without the required hazard labels.",
  "required_action": "Not specified.",
  "evidence_valid": true
}
```

Run the example locally:

```bash
PYTHONPATH=src python examples/compliance_extraction.py
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

## What is actually built

- A small `ComplianceRisk` structured output contract.
- A narrow extraction example with a safe `None` result for unsupported text.
- Verbatim evidence preservation and source validation.
- A runnable example and three unit tests.
- The original sample climate-data module and console program are preserved as early project history.

## Current limitations

- There is no LLM/API integration yet.
- The extractor supports one intentionally narrow example; it is not a general compliance parser.
- There is no PDF, spreadsheet, email, or document ingestion.
- There is no production deployment, dashboard, database, authentication, or public API.
- Extraction quality depends on the eventual underlying model and evaluation data.
- The prototype does not replace professional environmental/compliance judgment.
- A representative labelled dataset and additional validation are required before real-world use.

## Roadmap

### Phase 1 — Foundation

- [x] Define an environmental/compliance workflow direction
- [x] Define a structured risk output
- [x] Create a small evidence-first extraction scaffold
- [x] Add tests for unsupported input and evidence validation

### Phase 2 — Prototype

- [ ] Add document ingestion with clear source boundaries
- [ ] Expand risk extraction beyond the single demo pattern
- [ ] Add an optional LLM adapter with structured-output constraints
- [ ] Generate reviewable structured reports

### Phase 3 — Evaluation

- [ ] Build a representative evaluation dataset
- [ ] Measure extraction accuracy and evidence recall
- [ ] Test hallucination resistance and unsupported-action handling
- [ ] Compare prompting strategies once an LLM adapter exists

## Repository structure

```text
.
├── README.md
├── ROADMAP.md
├── climate_data.py
├── main.py
├── pyproject.toml
├── examples/
│   └── compliance_extraction.py
├── src/
│   └── climatecopilot/
│       ├── __init__.py
│       └── extraction.py
└── tests/
    └── test_extraction.py
```

## Future work

The highest-value next step is not more interface code: it is a small, labelled evaluation set that can compare model outputs against source evidence and the expected schema. An LLM adapter should only be added after those checks are defined.

## License

No license has been added yet. Until one is chosen, reuse and redistribution rights should not be assumed.
