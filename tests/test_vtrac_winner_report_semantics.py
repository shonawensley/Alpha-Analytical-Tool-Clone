import pandas as pd

from src.core import module_c_vtrac as report


NUMERIC_COLUMNS = ["7", "6", "5", "4", "3", "2", "1"]


def _table(rows):
    records = []
    for row_type, values in rows:
        record = {
            "Set": "Set1",
            "Draw": "Draw1",
            "RowType": row_type,
        }
        record.update({column: "" for column in NUMERIC_COLUMNS})
        record.update(values)
        records.append(record)
    return pd.DataFrame.from_records(records)


def _three_variant_tables():
    return {
        "Midday_combined": _table(
            [
                ("draw_data", {"1": "591"}),
                ("R2", {"2": "019"}),
                ("R4", {"2": "019"}),
                ("R6", {"2": "019"}),
                ("R8", {"2": "019"}),
            ]
        ),
        "Evening_combined": _table(
            [
                ("draw_data", {"1": "591"}),
                ("R2", {"2": "096**"}),
                ("R4", {"2": "7096**"}),
                ("R6", {"2": "901"}),
                ("R8", {"2": "019"}),
            ]
        ),
        "Combined_combined": _table(
            [
                ("draw_data", {"1": "591"}),
                ("R2", {"2": "019"}),
                ("R4", {"2": "901"}),
                ("R6", {"2": "109"}),
                ("R8", {"2": "019"}),
            ]
        ),
    }


def test_report_statistics_preserve_legacy_and_split_populations():
    tables = _three_variant_tables()
    patterns = {"019", "096"}

    statistics = report.build_report_statistics(tables, patterns)
    legacy_occurrence, _ = report.count_patterns_in_table(
        tables["Combined_combined"], patterns
    )

    assert (
        statistics["legacy_combined_all_rows"]["pattern_occurrence"]
        == legacy_occurrence
    )
    assert (
        statistics["variants"]["Evening"]["r_pattern"][
            "pattern_occurrence"
        ]["096"]
        == 2
    )
    assert (
        statistics["variants"]["Evening"]["draw_data"][
            "pattern_occurrence"
        ]["096"]
        == 0
    )
    assert (
        statistics["all_variant"]["r_pattern"]["variants_present"]["096"]
        == ["Evening"]
    )
    assert "independent support" in (
        statistics["all_variant"]["r_pattern"]["independence_warning"]
    )


def test_connecticut_fixture_uses_modern_v152_lane_and_preserves_legacy_marker():
    lane = report.build_ordered_lane_report(
        "091", _three_variant_tables(), legacy_vt_pair=None
    )

    assert lane["ordered_vcode"] == "v152"
    assert lane["boxed_vtrac_index"] == 9
    assert lane["lane_members"] == [
        "041",
        "046",
        "091",
        "096",
        "541",
        "546",
        "591",
        "596",
    ]
    assert lane["variants"]["Evening"]["r_pattern"]["occurrence_total"] == 2
    assert lane["variants"]["Evening"]["draw_data"]["occurrence_total"] == 1
    assert lane["legacy_marker"]["status"] == "UNAVAILABLE"


def test_ordered_lane_calculation_generalizes_beyond_connecticut():
    tables = {
        f"{variant}_combined": _table(
            [
                ("draw_data", {"1": "004"}),
                ("R2", {"2": "559"}),
                ("R4", {"2": "059"}),
                ("R6", {"2": "509"}),
                ("R8", {"2": "554"}),
            ]
        )
        for variant in ("Midday", "Evening", "Combined")
    }

    lane = report.build_ordered_lane_report("559", tables)

    assert lane["ordered_vcode"] == "v115"
    assert lane["boxed_vtrac_index"] is not None
    assert lane["lane_members"] == [
        "004",
        "009",
        "054",
        "059",
        "504",
        "509",
        "554",
        "559",
    ]
    assert lane["variants"]["Midday"]["r_pattern"]["occurrence_total"] == 4


def test_json_and_html_render_new_contract_without_removing_legacy_stats():
    tables = _three_variant_tables()
    patterns = {"019", "096"}

    payload = report.generate_index_json_report(
        "FixtureState",
        9,
        patterns,
        tables,
        score=0,
        rank=0,
        timestamp="TEST",
        winner_combo="091",
    )
    html = report.generate_index_html_report(
        "FixtureState",
        9,
        patterns,
        tables,
        score=0,
        rank=0,
        timestamp="TEST",
        winner_combo="091",
    )

    assert payload["report_schema_version"] == "winner_report_semantics_v2"
    assert "stats" in payload
    assert payload["ordered_vtrac_lane"]["ordered_vcode"] == "v152"
    assert payload["stats_by_variant"]["variants"]["Evening"]["r_pattern"][
        "pattern_occurrence"
    ]["096"] == 2
    assert "Ordered Three-Position VTRAC Lane" in html
    assert "Legacy Combined/All-Row Statistics" in html
    assert "not independent support" in html
