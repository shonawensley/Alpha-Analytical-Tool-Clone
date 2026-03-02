import json
import subprocess
import sys
from pathlib import Path

import pytest

from modules import vtrac_enhanced as ve


FIXTURE_STATE = "SampleState"
FIXTURE_ROOT = Path("tests/fixtures/vtrac/SampleState")


def _build_engine_input() -> ve.EngineInput:
    return ve.build_engine_input_from_tables(FIXTURE_STATE, tables_root=FIXTURE_ROOT.parent)


def test_run_analysis_orders_indices(tmp_path):
    engine_input = _build_engine_input()
    output = ve.run_analysis(engine_input)

    assert output.indices_ranked, "Expected indices to be ranked"
    top = output.indices_ranked[0]
    assert top.index == 5, f"Expected index 5 to score highest, got {top.index}"
    assert top.score > 0
    assert any(candidate.straight == "059" for candidate in top.straights)

    bundle = ve.write_prediction_bundle(
        "TestState",
        output,
        analysis_root=tmp_path,
        engine_input=engine_input,
    )
    data = json.loads(bundle.read_text(encoding="utf-8"))
    assert data["indices_ranked"][0]["index"] == 5
    assert data["straights_ranked"], "Expected straight candidates in bundle"
    summaries = data.get("section_summaries")
    assert summaries, "section_summaries should be present in bundle"
    for section_name in ("Midday", "Evening", "Combined"):
        assert section_name in summaries, f"{section_name} summary missing"
        section = summaries[section_name]
        metrics = section.get("analyzer_metrics")
        assert metrics is not None, f"{section_name} analyzer metrics missing"
        for key in ("indices_considered", "mask_drop_count", "reduction_hits", "mirror_supported", "double_hits", "top_straights"):
            assert key in metrics, f"{section_name} missing '{key}' metric"
        assert isinstance(metrics["top_straights"], list)


def test_mask_digit_suggestion():
    engine_input = _build_engine_input()
    mask = ve.suggested_mask_digits(engine_input.recent_draws)
    assert mask == {"4", "3", "8"}


def test_cli_smoke(tmp_path, monkeypatch):
    cmd = [
        sys.executable,
        "TOOLS/vtrac_enhanced_cli.py",
        "--state",
        FIXTURE_STATE,
        "--tables-root",
        str(FIXTURE_ROOT.parent),
        "--analysis-root",
        str(tmp_path),
    ]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    assert "Bundle written to" in result.stdout
    bundles = sorted(tmp_path.glob("vtrac/SampleState/*.json"))
    assert bundles, "CLI did not write prediction bundle"
