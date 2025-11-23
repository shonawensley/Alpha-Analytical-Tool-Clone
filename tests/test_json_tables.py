from __future__ import annotations

import json
from pathlib import Path

from utils.json_tables import build_json_tables_from_csv

CSV_CONTENT = """Set,Draw,RowType,7,6,5,4,3,2,1
Set1,Draw1,draw_data,100,200,300,400,500,600,700
Set1,Draw1,R2,1*,2,3,4,5,6,7
Set1,Draw1,R4,8,9*,10,11,12,13,14
"""


def _write_section(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(CSV_CONTENT)


def test_build_json_tables_from_csv(tmp_path):
    tables_dir = tmp_path / "Connecticut4"
    for section in ("Midday", "Evening", "Combined"):
        _write_section(tables_dir / f"{section}_Combined.csv")
    out_root = tmp_path / "json"
    json_path = build_json_tables_from_csv("Connecticut4", str(tables_dir), str(out_root))
    data = json.loads(Path(json_path).read_text())
    assert data["state_name"] == "Connecticut4"
    combined = data["sections"]["Combined"]["sets"]["Set1"]["Draw1"]
    assert combined["draw_data"][0] == "100"
    assert combined["pattern_variations"]["R2"][0] == "1*"
    assert combined["metadata"]["is_hot_zone"] is True
