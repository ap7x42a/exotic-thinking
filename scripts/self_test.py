#!/usr/bin/env python3
"""Self-test for the public exotic-thinking skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LENSES = [
    "Abductive",
    "Negative-space",
    "Predictive",
    "Asymmetric belief",
    "External memory binding",
    "Concurrent",
    "Split",
    "Stigmergic",
]


def main() -> int:
    failures: list[str] = []
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    catalog = (ROOT / "references" / "paradigm-catalog.md").read_text(encoding="utf-8")

    for lens in LENSES:
        if re.search(re.escape(lens), skill, re.IGNORECASE) is None:
            failures.append(f"SKILL.md missing lens: {lens}")
        if re.search(re.escape(lens), catalog, re.IGNORECASE) is None:
            failures.append(f"catalog missing lens: {lens}")

    for phrase in (
        "These lenses do not generate truth",
        "Do not treat a lens name as evidence",
        "Output Shape",
        "Done Means",
    ):
        if phrase not in skill:
            failures.append(f"missing guardrail phrase: {phrase}")

    banned = ("NeuroLedger", "MCP", "Smarty", "neuroledger-core", "GrimWatch")
    for token in banned:
        if token in skill or token in catalog:
            failures.append(f"project-specific token leaked: {token}")

    if failures:
        print("SELF-TEST FAILED")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("SELF-TEST PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
