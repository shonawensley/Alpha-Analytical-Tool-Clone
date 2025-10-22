import pandas as pd

from modules.vtrac_enhanced.evidence import (
    BoxKey,
    build_grid,
)
from modules.vtrac_matchers import build_winner_targets


def _load_fixture_tables():
    base = "tests/fixtures/vtrac/SampleState"
    tables = {
        "Combined_combined": pd.read_csv(f"{base}/SampleState_Combined_combined.csv", dtype=str).fillna(""),
        "Midday_combined": pd.read_csv(f"{base}/SampleState_Midday_combined.csv", dtype=str).fillna(""),
        "Evening_combined": pd.read_csv(f"{base}/SampleState_Evening_combined.csv", dtype=str).fillna(""),
    }
    return tables


def test_build_grid_and_evaluate_exact_matches():
    tables = _load_fixture_tables()
    grid = build_grid(tables)
    targets = build_winner_targets("059", ["059", "095", "509", "590", "905", "950"])
    grid.evaluate(targets)

    box_key = BoxKey(variant="Combined", set_name="Set1", draw="Draw1", column=2)
    assert box_key in grid.boxes

    box = grid.boxes[box_key]
    exact_summary = box.summary["exact"]
    assert exact_summary.present is True
    assert exact_summary.first_row == "R2"
    assert exact_summary.count >= 2
    assert exact_summary.final_row in {"R4", "R6", "R8"}

    r2_cell = box.cells["R2"]
    highlighted = r2_cell.render_highlighted()
    assert '<span class="hit-winner">0</span>' in highlighted or '<span class="hit-winner">059</span>' in highlighted


def test_grid_captures_hot_level_and_digits():
    tables = _load_fixture_tables()
    grid = build_grid(tables)
    box_key = BoxKey(variant="Combined", set_name="Set1", draw="Draw1", column=5)
    box = grid.boxes[box_key]
    r2_cell = box.cells["R2"]
    assert r2_cell.digits == "905"
    assert r2_cell.hot_level == 0

    # Midday R2 column 2 should also capture digits
    box_midday = grid.boxes[BoxKey("Midday", "Set1", "Draw1", 2)]
    assert box_midday.cells["R2"].digits == "059"
