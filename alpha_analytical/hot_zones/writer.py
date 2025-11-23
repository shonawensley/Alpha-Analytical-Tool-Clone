from __future__ import annotations

import csv
import json
from dataclasses import asdict
from pathlib import Path
from typing import Iterable, List, Sequence

from .scanner import PerItemRow, TopCandidateRow

class HotZonesArtifacts:
    def __init__(self, per_item_csv: Path, top_csv: Path, meta_json: Path):
        self.per_item_csv = per_item_csv
        self.top_csv = top_csv
        self.meta_json = meta_json

def _write_csv(path: Path, rows: Iterable[dict], header: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(header))
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def write_hotzones_artifacts(state: str, out_dir: str, per_items: List[PerItemRow], tops: List[TopCandidateRow], meta: dict) -> HotZonesArtifacts:
    base = Path(out_dir)
    per_item_csv = base / f"{state}_hot_zones_per_lane.csv"
    top_csv = base / f"{state}_hot_zones_top_lanes.csv"
    meta_json = base / f"{state}_hot_zones_meta.json"

    _write_csv(per_item_csv, (asdict(row) for row in per_items), PerItemRow.__annotations__.keys())
    _write_csv(top_csv, (asdict(row) for row in tops), TopCandidateRow.__annotations__.keys())
    meta_json.parent.mkdir(parents=True, exist_ok=True)
    meta_json.write_text(json.dumps(meta, indent=2))

    return HotZonesArtifacts(per_item_csv, top_csv, meta_json)

def write_winner_map(state: str, date_stamp: str, out_dir: str, tops: List[TopCandidateRow], limit: int = 20) -> Path:
    base = Path(out_dir)
    base.mkdir(parents=True, exist_ok=True)
    json_path = base / f"{date_stamp}_hot_zones_winner_map.json"
    csv_path = base / f"{date_stamp}_hot_zones_winner_map.csv"
    entries = [
        {
            "state": state,
            "date": date_stamp,
            **asdict(row),
        }
        for row in tops[:limit]
    ]
    json_path.write_text(json.dumps(entries, indent=2))
    if entries:
        _write_csv(csv_path, entries, entries[0].keys())
    else:
        _write_csv(csv_path, [], ["state"])
    return json_path
