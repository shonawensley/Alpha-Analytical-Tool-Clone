from __future__ import annotations

import json
from pathlib import Path

from core import pipeline_runner as pr


def test_describe_workbook(tmp_path):
    excel = tmp_path / "Pick3StatsC4.xlsm"
    excel.write_text("dummy")
    info = pr._describe_workbook(str(excel))
    assert info["exists"] is True
    assert info["path"].endswith("Pick3StatsC4.xlsm")
    assert info["size"] == 5


def test_manifest_roundtrip(tmp_path, monkeypatch):
    manifest_path = tmp_path / "tables_manifest.json"
    monkeypatch.setattr(pr, "MANIFEST_PATH", manifest_path)
    sample = {"workbook": {"path": "demo"}, "states": {}, "generated_at": "now"}
    pr._write_manifest(sample)
    assert manifest_path.exists()
    data = json.loads(manifest_path.read_text())
    assert data == sample
    loaded = pr._load_manifest()
    assert loaded == sample


def test_purge_state_tables(tmp_path):
    state_dir = tmp_path / "Connecticut4"
    state_dir.mkdir()
    csv = state_dir / "Combined_Combined.csv"
    csv.write_text("a,b")
    pr._purge_state_tables(str(state_dir))
    assert not csv.exists()
