import json
import subprocess
import sys
from pathlib import Path


def run_script(target_dir: Path) -> subprocess.CompletedProcess:
    cmd = [
        sys.executable,
        "TOOLS/vtrac_score_and_export.py",
        str(target_dir),
        "--output",
        str(target_dir),
    ]
    return subprocess.run(cmd, check=True, cwd=Path(__file__).resolve().parents[1])


def read_outputs(target_dir: Path):
    json_path = target_dir / "vtrac_compact_report.json"
    csv_path = target_dir / "vtrac_compact_report.csv"
    assert json_path.exists(), "JSON output missing"
    assert csv_path.exists(), "CSV output missing"

    rows = json.loads(json_path.read_text())
    return rows


def test_vtrac_score_and_export(tmp_path: Path):
    repo_root = Path(__file__).resolve().parents[1]
    fixture_dir = repo_root / "tests" / "fixtures" / "vtrac_validation"

    for rel_path in fixture_dir.rglob("*"):
        if rel_path.is_dir():
            continue
        target_file = tmp_path / rel_path.relative_to(fixture_dir)
        target_file.parent.mkdir(parents=True, exist_ok=True)
        target_file.write_text(rel_path.read_text())

    run_script(tmp_path)
    rows = read_outputs(tmp_path)

    assert len(rows) == 2

    combined = next(r for r in rows if r["section"] == "Combined")
    midday = next(r for r in rows if r["section"] == "Midday")

    # Combined has overlap > 0, should not be flagged as rescue and should rank higher.
    assert combined["overlap"] == 2
    assert combined["tier"] == "B"
    assert "weak_positive_rescue" not in combined["flags"]

    # Midday overlap=0 but consensus/stability should trigger rescue flag.
    assert midday["overlap"] == 0
    assert "weak_positive_rescue" in midday["flags"]
    assert midday["tier"] == "Z"

    # Recommended tokens capped and present.
    assert len(combined["recommended_tokens"]) <= 3
    assert len(midday["recommended_tokens"]) <= 3

    # Combined score should exceed rescue section score.
    assert combined["confidence_score"] > midday["confidence_score"]
