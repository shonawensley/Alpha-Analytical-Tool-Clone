#!/usr/bin/env python3
"""
Run the Hot Zones engine for a given state/date using the JSON table mirror.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from utils import path_handler as ph
from alpha_analytical.hot_zones import (
    load_table_env_from_json,
    HotZoneScanner,
    HotScanConfig,
    HotZoneWeights,
    write_hotzones_artifacts,
    write_winner_map,
)

def resolve_json_path(state: str, path: str | None) -> Path:
    if path:
        return Path(path)
    root = Path(ph.get_json_tables_dir())
    return root / f"{state}_tables.json"

def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Hot Zones analyzer for a state/date.")
    parser.add_argument("--state", required=True)
    parser.add_argument("--date", required=True, help="Date label for outputs (e.g., 2025-06-24)")
    parser.add_argument("--json", help="Explicit path to <STATE>_tables.json (defaults to data/outputs/json_tables/...)")
    parser.add_argument("--out-dir", help="Output base (defaults to data/outputs/analysis/hot_zones/<STATE>/)")
    parser.add_argument("--winners-dir", help="Optional overrides for winner map output")
    args = parser.parse_args()

    state = args.state
    json_path = resolve_json_path(state, args.json)
    out_dir = args.out_dir or ph.get_analysis_dir("hot_zones", state)
    winners_dir = args.winners_dir or out_dir

    env = load_table_env_from_json(json_path)
    scanner = HotZoneScanner(env, HotScanConfig(), HotZoneWeights())
    per_items, tops = scanner.scan()

    meta = {
        "state": state,
        "date": args.date,
        "json_source": str(json_path),
        "per_item_rows": len(per_items),
        "top_rows": len(tops),
    }
    artifacts = write_hotzones_artifacts(state, out_dir, per_items, tops, meta)
    winner_map = write_winner_map(state, args.date, winners_dir, tops)

    print("Per-item CSV:", artifacts.per_item_csv)
    print("Top candidates CSV:", artifacts.top_csv)
    print("Meta JSON:", artifacts.meta_json)
    print("Winner map:", winner_map)

if __name__ == "__main__":
    main()
