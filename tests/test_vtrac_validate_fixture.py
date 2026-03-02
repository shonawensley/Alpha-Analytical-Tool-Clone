import json
import subprocess
import sys
from pathlib import Path

import pytest

FIXTURE_ROOT = Path("tests/fixtures/vtrac_validation")
OUTPUT_ROOT = Path("data/outputs/analysis/vtrac_validation")


@pytest.mark.parametrize("state", ["Delaware4", "Florida4"])
def test_validator_fixture_parity(state, tmp_path):
    winners_dir = FIXTURE_ROOT / state
    analyzer_json = winners_dir / "analyzer.json"
    assert winners_dir.exists(), f"Fixture directory missing for {state}"
    assert analyzer_json.exists(), f"Analyzer fixture missing for {state}"

    cmd = [
        sys.executable,
        str(Path("TOOLS") / "vtrac_validate.py"),
        "--state",
        state,
        "--winners-dir",
        str(winners_dir),
        "--analysis-json",
        str(analyzer_json),
    ]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    assert "Wrote:" in result.stdout

    report_path = OUTPUT_ROOT / state / "validation_report.json"
    assert report_path.exists(), f"Validator report not written for {state}"
    report = json.loads(report_path.read_text(encoding="utf-8"))

    sections = report.get("sections", {})
    assert sections, "Sections missing in validator report"
    for section_name in ("Midday", "Evening", "Combined"):
        section = sections.get(section_name)
        assert section is not None, f"{section_name} section missing in report"
        metrics_map = section.get("analyzer_metrics", {})
        assert metrics_map, f"{section_name} analyzer metrics missing"
        assert "primary" in metrics_map, f"{section_name} metrics missing 'primary' label"
        metrics = metrics_map["primary"]
        for key in ("indices_considered", "mask_drop_count", "reduction_hits", "mirror_supported", "double_hits", "top_straights"):
            assert key in metrics, f"{section_name} metrics missing '{key}'"
        straights_map = section.get("analyzer_straights", {})
        assert "primary" in straights_map, f"{section_name} straights missing 'primary' label"
    straight_occurrences = report.get("straight_occurrences")
    assert straight_occurrences is not None, "Straight occurrences missing in report"
