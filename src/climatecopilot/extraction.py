"""Evidence-first extraction building blocks for the early-stage prototype.

This module deliberately uses simple rules rather than pretending to call an LLM.
It provides a small contract that a future LLM adapter can be evaluated against.
"""

from dataclasses import asdict, dataclass
import re
from typing import Optional


@dataclass(frozen=True)
class ComplianceRisk:
    """A risk with a source-backed claim and an explicit unknown action."""

    risk: str
    evidence: str
    required_action: str = "Not specified."

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


def extract_compliance_risk(report: str) -> Optional[ComplianceRisk]:
    """Extract the supported missing-label example from an inspection report.

    The rule is intentionally narrow: returning ``None`` is preferable to
    inventing a risk when the report does not match the supported pattern.
    """

    match = re.search(
        r"(?P<evidence>[^.]*\b(?:solvent|chemical)\s+waste\b[^.]*\bwithout\b"
        r"[^.]*\bhazard labels?\b[^.]*)[.]?",
        report,
        flags=re.IGNORECASE,
    )
    if not match:
        return None

    evidence = match.group("evidence").strip().rstrip(".") + "."
    return ComplianceRisk(
        risk="Missing hazard labels on solvent waste containers",
        evidence=evidence,
    )


def validate_evidence(result: ComplianceRisk, source_text: str) -> bool:
    """Return whether the reported evidence is present verbatim in the source."""

    return result.evidence.rstrip(".").lower() in source_text.lower()
