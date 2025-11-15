from pathlib import Path

import pandas as pd

from alpha_analytical.digit_reduction.analyzer_v2.winners_overlay import WinnerSpec, build_winner_map

FIXTURE_ROOT = Path(__file__).resolve().parents[1] / "fixtures" / "digit_mini"


def test_digit_mini_fixture_preserves_vt_and_ls_flags(tmp_path: Path) -> None:
    per_item_path = FIXTURE_ROOT / "training_sets" / "TestState" / "analyzer_v2" / "TestState_analyzer_v2_per_item.csv"
    df = pd.read_csv(per_item_path)
    row = df.iloc[0]
    assert int(row["vt_only_lane"]) == 1
    assert int(row["funnel_precol1"]) == 1
    assert int(row["ls_col_42"]) == 1
    assert int(row["dr.win_vt_boxed"]) == 1
    assert int(row["dr.win_vt_straight"]) == 0

    training_log = FIXTURE_ROOT / "TestState_digit_reduction_log.json"
    spec = WinnerSpec(combo="577")
    wmap = build_winner_map(training_log, spec, variant="Combined")
    assert wmap["items"], "Fixture winner map should contain at least one row"
    payload = wmap["items"][0]
    assert payload["final_vt_boxed"] == 1
    assert payload["final_vt_straight"] == 1
