import json
import subprocess
from pathlib import Path

try:
    import jsonschema  # type: ignore
except ImportError:
    jsonschema = None

ROOT = Path(__file__).resolve().parents[2]
REPORT_DIR = ROOT / "reports" / "control_center"
SCHEMA_PATH = REPORT_DIR / "alert_schema.json"


def test_snapshot_schema(tmp_path):
    results_file = ROOT / "data" / "results" / "2025-06-21.txt"
    assert results_file.exists(), "Expected results file missing"
    # Run the snapshot script into temp report dir
    out = subprocess.run(
        ["python3", str(ROOT / "scripts" / "tools" / "cc_sanity_snapshot.py"), "--results-file", str(results_file)],
        capture_output=True,
        text=True,
        check=True,
    )
    # Find latest snapshot in report dir
    snaps = sorted(REPORT_DIR.glob("cc_snapshot_*.json"))
    assert snaps, "No snapshot generated"
    latest = snaps[-1]
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    data = json.loads(latest.read_text(encoding="utf-8"))
    if jsonschema is None:
        print("jsonschema not installed; skipping validation")
    else:
        for alert in data.get("alerts", []):
            jsonschema.validate(instance=alert, schema=schema)


if __name__ == "__main__":
    test_snapshot_schema(Path())
