import json
import subprocess
import sys
from pathlib import Path


def run_script(target_dir: Path, config: Path) -> None:
    cmd = [
        sys.executable,
        "TOOLS/vtrac_score_and_export.py",
        str(target_dir),
        "--out-dir",
        str(target_dir),
        "--config",
        str(config),
    ]
    subprocess.run(cmd, check=True, cwd=Path(__file__).resolve().parents[1])


def read_outputs(target_dir: Path):
    json_path = target_dir / "vtrac_compact_report.json"
    csv_path = target_dir / "vtrac_compact_report.csv"
    assert json_path.exists(), "JSON output missing"
    assert csv_path.exists(), "CSV output missing"
    return json.loads(json_path.read_text())


def test_vtrac_score_and_export(tmp_path: Path):
    repo_root = Path(__file__).resolve().parents[1]
    fixture_dir = repo_root / "tests" / "fixtures" / "vtrac_validation"

    for rel_path in fixture_dir.rglob("*"):
        if rel_path.is_dir():
            continue
        target_file = tmp_path / rel_path.relative_to(fixture_dir)
        target_file.parent.mkdir(parents=True, exist_ok=True)
        target_file.write_text(rel_path.read_text())

    demo_report = tmp_path / "DemoState4" / "validation_report.json"
    payload = json.loads(demo_report.read_text())
    analyzer_path = tmp_path / "DemoState4_analyzer.json"
    payload.setdefault("analyzer_jsons", {})["primary"] = str(analyzer_path)
    demo_report.write_text(json.dumps(payload))
    analyzer_path.write_text(
        json.dumps(
            {
                "indices_ranked": [
                    {"index": 16, "score": 25.0, "evidence": {"raw": {"sections": ["Combined"]}}},
                    {"index": 5, "score": 10.0, "evidence": {"raw": {"sections": ["Midday"]}}},
                ]
            }
        )
    )

    config_path = tmp_path / "config.json"
    config_path.write_text(
        json.dumps(
            {
                "weights": {"overlap": 4.0},
                "section_priors": {"Midday": 1.25},
                "state_priors": {"DemoState4": 0.95},
            }
        )
    )

    run_script(tmp_path, config_path)
    data = read_outputs(tmp_path)
    rows = data["sections"]
    states = data["states"]

    assert data["scorer_version"]
    assert data["run_date_utc"].endswith("Z")
    assert len(rows) == 2
    assert len(states) == 1

    rows_by_section = {row["section"]: row for row in rows}
    combined = rows_by_section["Combined"]
    midday = rows_by_section["Midday"]
    top_indices = states[0]["top_indices_by_state"]
    assert len(top_indices) == 2
    assert top_indices[0]["index"] == 16
    assert top_indices[0]["source_section"] == "Combined"

    # Combined keeps strong overlap score and no rescue.
    assert combined["overlap"] == 3
    assert combined["tier"] == "B+"
    assert "weak_positive_rescue" not in combined["flags"]
    assert combined["mirror_supported"] is True
    assert "overlap" in combined["why"]

    # Midday overlap=0 but consensus/stability triggers rescue and section prior override.
    assert midday["overlap"] == 0
    assert "weak_positive_rescue" in midday["flags"]
    assert midday["tier"] == "Z"
    assert abs(midday["section_prior"] - 1.25) < 1e-6
    assert "rescue_multiplier" in midday["why"]

    # Cross-section echo should count analyzer-only shared token (VAnalyzerShared).
    assert combined["cross_section_echo"] >= 1

    # Recommended tokens are capped and include analyzer/winners union.
    assert 0 < len(combined["recommended_tokens"]) <= 3
    assert "VAnalyzerShared" in combined["recommended_tokens"]

    # State prior from config applied.
    assert abs(combined["state_prior"] - 0.95) < 1e-6
    assert abs(midday["state_prior"] - 0.95) < 1e-6

    # Combined score should exceed rescue section score.
    assert combined["confidence_score"] > midday["confidence_score"]
