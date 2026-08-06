from __future__ import annotations

import math

from src.utils.extract_data import _clean_cell, _format_draw
from src.utils.table_generator import build_combined_table
from utils.extract_data import _clean_cell as _legacy_clean_cell
from utils.extract_data import _format_draw as _legacy_format_draw
from utils.table_generator import mark_hot_zones as _legacy_mark_hot_zones


def _row(table, row_type):
    return table.loc[table["RowType"] == row_type].iloc[0]


def test_pattern_strings_preserve_source_length_and_draws_remain_fixed_width():
    section_data = {
        "Set3": {
            "Draw1": {
                "draw_data": ["6", "54", "096", "", None, math.nan, "210"],
                "R2": ["6", "54", "096", "", None, math.nan, "210"],
                "R4": ["6", "54", "096", "", None, math.nan, "210"],
                "R6": ["6", "54", "096", "", None, math.nan, "210"],
                "R8": ["6", "54", "096", "", None, math.nan, "210"],
            }
        }
    }

    table = build_combined_table(section_data)
    draw = _row(table, "draw_data")
    pattern = _row(table, "R2")

    assert list(draw[["7", "6", "5", "4", "3", "2", "1"]]) == [
        "006",
        "054",
        "096",
        "",
        "",
        "",
        "210",
    ]
    assert list(pattern[["7", "6", "5", "4", "3", "2", "1"]]) == [
        "6",
        "54",
        "096",
        "",
        "",
        "",
        "210*",
    ]


def test_single_digit_consensus_remains_single_digit():
    section_data = {
        "Set2": {
            "Draw1": {
                "draw_data": ["100"] * 7,
                "R2": ["123", "123", "123", "6", "6", "6", "6"],
                "R4": ["123", "123", "123", "6", "6", "6", "6"],
                "R6": ["123", "123", "123", "6", "6", "6", "6"],
                "R8": ["123", "123", "123", "6", "6", "6", "6"],
            }
        }
    }

    table = build_combined_table(section_data)
    for row_type in ("R2", "R4", "R6", "R8"):
        row = _row(table, row_type)
        assert row["1"] == "6*"
        assert row["2"] == "6*"


def test_extractor_helpers_do_not_materialize_missing_values():
    for value in (None, math.nan, "nan", "<NA>", "None", ""):
        assert _clean_cell(value) == ""
        assert _format_draw(value) == ""
        assert _legacy_clean_cell(value) == ""
        assert _legacy_format_draw(value) == ""

    assert _clean_cell("6") == "6"
    assert _clean_cell("54") == "54"
    assert _clean_cell("096") == "096"
    assert _format_draw("6") == "006"
    assert _format_draw("54") == "054"
    assert _format_draw("096") == "096"
    assert _legacy_format_draw("6") == "006"


def test_legacy_hot_zone_marker_does_not_create_content_in_blank_cells():
    values = ["123", "456", "789", "", "", "", ""]
    marked = _legacy_mark_hot_zones("Set2", "Draw1", "R2", values)
    assert marked == values
