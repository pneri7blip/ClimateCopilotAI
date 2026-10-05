import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from climatecopilot import extract_compliance_risk, validate_evidence


class ExtractionTests(unittest.TestCase):
    def test_extracts_supported_risk_and_preserves_evidence(self):
        report = "Two containers of solvent waste were found without the required hazard labels."
        result = extract_compliance_risk(report)

        self.assertIsNotNone(result)
        self.assertEqual(result.risk, "Missing hazard labels on solvent waste containers")
        self.assertEqual(result.evidence, report)
        self.assertEqual(result.required_action, "Not specified.")
        self.assertTrue(validate_evidence(result, report))

    def test_does_not_invent_risk_for_unmatched_text(self):
        self.assertIsNone(extract_compliance_risk("The site visit was completed."))

    def test_evidence_validation_rejects_unrelated_source(self):
        result = extract_compliance_risk(
            "Two containers of solvent waste were found without the required hazard labels."
        )
        self.assertFalse(validate_evidence(result, "No compliance finding was recorded."))


if __name__ == "__main__":
    unittest.main()
