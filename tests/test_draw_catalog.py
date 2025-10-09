import pytest
from pathlib import Path

from modules.draw_catalog import draws_since_last_double, scan_draw_files


def test_draws_since_last_double_detects_recent_double():
    draws = ["789", "441", "230", "115"]
    ds, combo = draws_since_last_double(draws)
    assert ds == 1
    assert combo == "441"


def test_draws_since_last_double_handles_no_double():
    draws = ["123", "456", "789"]
    ds, combo = draws_since_last_double(draws)
    assert ds == len(draws)
    assert combo is None
    ds_empty, combo_empty = draws_since_last_double([])
    assert ds_empty == 0
    assert combo_empty is None


def test_scan_draw_files_tracks_snapshot(tmp_path: Path):
    csv_main = tmp_path / "Alpha_draws.csv"
    csv_midday = tmp_path / "Alpha_Midday_draws.csv"
    csv_main.write_text("Draw\n123\n456\n", encoding="utf-8")
    csv_midday.write_text("Draw\n987\n", encoding="utf-8")

    snapshot1, states1 = scan_draw_files([tmp_path])
    assert states1 == ["Alpha"]
    assert str(csv_main.resolve()) in snapshot1

    csv_main.write_text("Draw\n999\n123\n456\n", encoding="utf-8")
    snapshot2, states2 = scan_draw_files([tmp_path])
    assert states2 == ["Alpha"]
    assert snapshot2 != snapshot1
