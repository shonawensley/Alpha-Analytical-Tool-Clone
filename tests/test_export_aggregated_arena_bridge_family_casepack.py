from pathlib import Path

from scripts.tools.export_aggregated_arena_bridge_family_casepack import (
    _group_rows,
    _load_rows,
    _render_md,
)


def _write_csv(path: Path, rows):
    header = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(",".join(header) + "\n")
        for row in rows:
            handle.write(",".join(str(row[key]) for key in header) + "\n")


def test_load_rows_filters_rule_and_adds_window(tmp_path):
    csv_path = tmp_path / "2026-01-21_to_2026-01-22__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_STRICT_ROWS.csv"
    _write_csv(
        csv_path,
        [
            {
                "rule_name": "top3_perm",
                "source_mix": "aux_overdue+aux_badge",
                "state_key": "Florida4",
            },
            {
                "rule_name": "top4_perm",
                "source_mix": "aux_overdue+aux_badge",
                "state_key": "Virginia4",
            },
        ],
    )

    rows = _load_rows([csv_path], "top4_perm")

    assert len(rows) == 1
    assert rows[0]["state_key"] == "Virginia4"
    assert rows[0]["window"] == "2026-01-21_to_2026-01-22"


def test_group_rows_orders_rows_by_window_date_state_outcome():
    grouped = _group_rows(
        [
            {
                "source_mix": "aux_overdue+aux_badge",
                "window": "b",
                "date": "2026-01-02",
                "state_key": "Virginia4",
                "outcome": "Evening",
            },
            {
                "source_mix": "aux_overdue+aux_badge",
                "window": "a",
                "date": "2026-01-01",
                "state_key": "Florida4",
                "outcome": "Midday",
            },
        ]
    )

    rows = grouped["aux_overdue+aux_badge"]
    assert rows[0]["window"] == "a"
    assert rows[1]["window"] == "b"


def test_render_md_includes_resolution_summary_and_rows():
    grouped = {
        "aux_overdue+aux_badge": [
            {
                "window": "2026-01-21_to_2026-01-22",
                "date": "2026-01-21",
                "state_key": "Florida4",
                "outcome": "Midday",
                "gap_detail": "lane_alive_literal_missing_front3",
                "arena_vtrac_rank": "3",
                "box_resolution_profile": "miss",
                "first_box_event": "",
                "watch_items_used": "4",
                "watchlist_canonical_count": "11",
                "baseline_same_day_literal": "0",
            },
            {
                "window": "2026-01-18_to_2026-01-20",
                "date": "2026-01-18",
                "state_key": "Virginia4",
                "outcome": "Evening",
                "gap_detail": "lane_alive_literal_missing_front5",
                "arena_vtrac_rank": "4",
                "box_resolution_profile": "direct_same_outcome",
                "first_box_event": "2026-01-18 Evening 123",
                "watch_items_used": "4",
                "watchlist_canonical_count": "9",
                "baseline_same_day_literal": "0",
            },
        ]
    }

    md = _render_md(grouped, ["aux_overdue+aux_badge"], "top4_perm")

    assert "Resolution profile: `1` direct" in md
    assert "`1` miss" in md
    assert "2026-01-18_to_2026-01-20" in md
    assert "2026-01-21_to_2026-01-22" in md
    assert "2026-01-18 Evening 123" in md
