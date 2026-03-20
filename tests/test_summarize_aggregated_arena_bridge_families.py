from __future__ import annotations

import csv
from pathlib import Path

from scripts.tools.summarize_aggregated_arena_bridge_families import (
    _group_summary,
    _normalize_rows,
    _write_csv,
)


def _write_input_csv(path: Path, rows) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        if fieldnames:
            writer.writeheader()
            for row in rows:
                writer.writerow(row)


def test_normalize_rows_filters_rule_and_adds_window(tmp_path: Path) -> None:
    csv_path = tmp_path / "window_a.csv"
    _write_input_csv(
        csv_path,
        [
            {"rule_name": "top4_perm", "source_mix": "aux_overdue+aux_badge", "outcome": "Evening", "box_resolution_profile": "direct_same_outcome"},
            {"rule_name": "top3_perm", "source_mix": "due_doubles+aux_badge", "outcome": "Midday", "box_resolution_profile": "future_day_decay"},
        ],
    )

    rows = _normalize_rows([csv_path], rule_name="top4_perm")

    assert len(rows) == 1
    assert rows[0]["source_mix"] == "aux_overdue+aux_badge"
    assert rows[0]["window"] == "window_a"


def test_group_summary_counts_resolution_profiles() -> None:
    rows = [
        {"source_mix": "A", "box_resolution_profile": "direct_same_outcome"},
        {"source_mix": "A", "box_resolution_profile": "same_day_carryforward"},
        {"source_mix": "A", "box_resolution_profile": "miss"},
        {"source_mix": "B", "box_resolution_profile": "future_day_decay"},
    ]

    grouped = _group_summary(rows, key="source_mix")

    assert grouped == [
        {
            "source_mix": "A",
            "rows": "3",
            "direct_same_outcome": "1/3",
            "same_day_precursor_plus_same_day": "0/3",
            "same_day_carryforward": "1/3",
            "future_day_decay": "0/3",
            "miss": "1/3",
        },
        {
            "source_mix": "B",
            "rows": "1",
            "direct_same_outcome": "0/1",
            "same_day_precursor_plus_same_day": "0/1",
            "same_day_carryforward": "0/1",
            "future_day_decay": "1/1",
            "miss": "0/1",
        },
    ]


def test_write_csv_supports_union_of_fields(tmp_path: Path) -> None:
    out = tmp_path / "summary.csv"
    _write_csv(
        out,
        [
            {"group": "family", "source_mix": "A", "rows": "1"},
            {"group": "outcome", "outcome": "Evening", "rows": "2"},
        ],
    )

    text = out.read_text(encoding="utf-8")
    assert "source_mix" in text
    assert "outcome" in text
