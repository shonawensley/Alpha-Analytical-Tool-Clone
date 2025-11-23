from __future__ import annotations

from pathlib import Path

from alpha_analytical.hot_zones import (
    load_table_env_from_json,
    HotZoneScanner,
    HotZoneWeights,
)

FIXTURE = Path("tests/fixtures/hot_zones/Sample_tables.json")

def test_hot_zones_scanner_basic(tmp_path):
    env = load_table_env_from_json(FIXTURE)
    scanner = HotZoneScanner(env, weights=HotZoneWeights())
    per_items, tops = scanner.scan()
    assert per_items, "Should emit per-item rows"
    assert tops, "Should emit top candidates"
    assert any(row.col1_arrival or row.precol1_funnel for row in per_items)
    assert any(top.hot_hits >= 1 for top in tops)
