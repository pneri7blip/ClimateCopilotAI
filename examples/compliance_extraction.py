"""Run with: PYTHONPATH=src python examples/compliance_extraction.py"""

import json

from climatecopilot import extract_compliance_risk, validate_evidence


REPORT = "Two containers of solvent waste were found without the required hazard labels."


def main() -> None:
    result = extract_compliance_risk(REPORT)
    if result is None:
        print("No supported risk found.")
        return

    print(json.dumps({**result.to_dict(), "evidence_valid": validate_evidence(result, REPORT)}, indent=2))


if __name__ == "__main__":
    main()
