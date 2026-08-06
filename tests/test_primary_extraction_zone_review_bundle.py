from __future__ import annotations

import csv
import html
import inspect
from pathlib import Path

from scripts.tools.build_primary_extraction_zone_review_bundle import (
    DEFAULT_OUTPUT,
    EXPECTED_THREE_VARIANT_ZONE_COUNTS,
    TABLE_VARIANTS,
    _coordinate_zones,
    render_pre_result_tables,
)


ROOT = Path(__file__).resolve().parents[1]
TABLE_ROOT = (
    ROOT
    / "sharepacks/_replay_rpattern_current/2026-03-09/"
    "Connecticut4/tables"
)


def test_default_package_is_nested_beside_original_review() -> None:
    assert DEFAULT_OUTPUT.name == "EXTERNAL_REVIEW_READY"
    assert DEFAULT_OUTPUT.parent.name == (
        "PRIMARY_EXTRACTION_ZONE_REVIEW__2026-03-09"
    )


def test_pre_result_table_renderer_has_no_result_parameter() -> None:
    parameters = inspect.signature(render_pre_result_tables).parameters
    assert "winner" not in parameters
    assert "target" not in parameters


def test_locked_zone_coordinates_match_authoritative_contract() -> None:
    for set_name in ("Set3", "Set2", "Set1"):
        for column in (7, 6, 5):
            assert _coordinate_zones(
                set_name=set_name,
                draw="Draw1",
                row_type="R2",
                column=column,
            ) == ("ZONE_1",)

    expected_zone_2 = {
        "Draw2": {6, 5, 4},
        "Draw3": {5, 4, 3, 2},
        "Draw4": {4, 3, 2},
        "Draw5": {3, 2, 1},
        "Draw6": {2, 1},
        "Draw7": {1},
    }
    for draw, columns in expected_zone_2.items():
        for column in columns:
            assert _coordinate_zones(
                set_name="Set1",
                draw=draw,
                row_type="R8",
                column=column,
            ) == ("ZONE_2",)

    assert _coordinate_zones(
        set_name="Set1", draw="Draw1", row_type="R4", column=4
    ) == ()
    assert _coordinate_zones(
        set_name="Set2", draw="Draw1", row_type="R4", column=4
    ) == ()
    assert _coordinate_zones(
        set_name="Set1", draw="Draw3", row_type="R6", column=6
    ) == ()
    assert _coordinate_zones(
        set_name="Set1", draw="Draw3", row_type="R6", column=1
    ) == ()


def test_pre_result_table_renderer_preserves_all_frozen_cells(
    tmp_path: Path,
) -> None:
    sources = {
        variant: TABLE_ROOT / f"{variant}_Combined.csv"
        for variant in TABLE_VARIANTS
    }
    output = tmp_path / "tables.html"
    receipt = render_pre_result_tables(
        state="Connecticut4",
        table_sources=sources,
        output_path=output,
    )
    rendered = output.read_text(encoding="utf-8")
    lowered = rendered.lower()

    assert receipt["claim_class"] == (
        "FROZEN_PRE_RESULT_TABLE_VIEW_RECONSTRUCTION"
    )
    assert "hit-winner" not in lowered
    assert "hit-family" not in lowered
    assert "dr-winner" not in lowered
    assert "winner overlay" not in lowered
    assert receipt["zone_overlay"] == EXPECTED_THREE_VARIANT_ZONE_COUNTS
    assert rendered.count('data-extraction-zones="') == 300
    assert rendered.count('data-extraction-zones="ZONE_1 ZONE_2"') == 0
    assert "Zone 3 is a" in rendered

    for variant, source in sources.items():
        with source.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        assert receipt["sources"][variant.lower()]["row_count"] == len(rows)
        assert len(rows) == 45
        for row in rows:
            for value in row.values():
                assert html.escape(str(value or "")) in rendered
