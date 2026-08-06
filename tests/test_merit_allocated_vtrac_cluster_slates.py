import copy

import pytest

from scripts.tools.grade_merit_allocated_vtrac_cluster_slate import (
    grade_merit_slate,
)
from scripts.tools.merit_allocated_vtrac_cluster_slates import (
    ARTIFACT_TYPE,
    build_merit_allocated_slate,
    scan_pattern_tables,
)


def _pattern_tables():
    sections = {}
    primary_by_row = {
        "R2": "168168",
        "R4": "681681",
        "R6": "816816",
        "R8": "668668",
    }
    secondary_by_row = {
        "R2": "901901",
        "R4": "019019",
        "R6": "109109",
        "R8": "096096",
    }
    for variant in ("Midday", "Evening", "Combined"):
        rows = {
            row: [
                primary,
                primary,
                primary,
                secondary_by_row[row],
                secondary_by_row[row],
                secondary_by_row[row],
                primary,
            ]
            for row, primary in primary_by_row.items()
        }
        sections[variant] = {
            "sets": {
                "Set1": {
                    "Draw1": {
                        "draw_data": [
                            "591591591",
                            "591591591",
                            "591591591",
                            "591591591",
                            "591591591",
                            "591591591",
                            "591591591",
                        ],
                        "pattern_variations": rows,
                        "metadata": {},
                    }
                }
            }
        }
    return {"state_name": "Demo4", "sections": sections}


def _candidate_universe():
    return {
        "schema_version": "1.0",
        "state_key": "Demo4",
        "results_date": "2026-07-25",
        "history_date": "2026-07-24",
        "profile": "tool_only",
        "contains_winners_artifacts": False,
        "leakage_issues": [],
        "packs": [
            {
                "method_id": "stable_top",
                "pack_id": "stable:Combined:one",
                "variant": "Combined",
                "combos": ["168", "668", "901", "019"],
                "canonicals": ["168", "668", "019"],
            }
        ],
    }


def _arena():
    return {
        "metadata": {
            "state_key": "Demo4",
            "results_date": "2026-07-25",
            "history_date": "2026-07-24",
            "profile": "tool_only",
            "contains_winners_artifacts": False,
        },
        "arena_synthesis": {
            "dominant_vtrac_indices": [
                {
                    "value": "18",
                    "support_count": 20,
                    "string_source_count": 12,
                    "context_source_count": 4,
                    "score_total": 500,
                    "example_literals": ["168", "668"],
                },
                {
                    "value": "9",
                    "support_count": 12,
                    "string_source_count": 8,
                    "context_source_count": 3,
                    "score_total": 300,
                    "example_literals": ["901", "019", "109", "096"],
                },
            ],
            "vtrac_literal_watchlist": [
                {
                    "vtrac_index": "18",
                    "candidate_canonicals": ["168", "668", "118", "366"],
                    "example_literals": ["168", "668"],
                },
                {
                    "vtrac_index": "9",
                    "candidate_canonicals": ["019", "069", "014", "159"],
                    "example_literals": ["901", "019", "109", "096"],
                },
            ],
            "dominant_canonicals": [
                {"value": "168", "example_literals": ["168"]},
                {"value": "019", "example_literals": ["901"]},
            ],
            "context_reinforced_canonicals": [],
        },
    }


def _sandbox():
    return {
        "metadata": {
            "state_key": "Demo4",
            "results_date": "2026-07-25",
            "history_date": "2026-07-24",
            "profile": "tool_only",
            "contains_winners_artifacts": False,
        },
        "brain1_core": {
            "dominant_canonicals": ["168", "019"],
            "context_reinforced_canonicals": ["668"],
            "secondary_canonicals": ["069"],
            "survivor_frontier_canonicals": ["019"],
            "survivor_last_remaining_canonicals": [],
        },
        "brain2_context": {
            "positional_shortlist_top": [
                {"combo": "168", "canonical": "168", "score": 20},
                {"combo": "901", "canonical": "019", "score": 12},
            ],
            "blackapple_recommended_canonicals": ["014"],
            "due_double_example_canonicals": [],
            "profit_alert_implied_canonicals": ["168"],
        },
        "sandbox_hypotheses": {
            "diagnostic_vt_box_seed": [
                {"value": "18", "support_count": 3},
                {"value": "9", "support_count": 2},
            ],
            "diagnostic_boxed_seed": [
                {"value": "168", "support_count": 4},
                {"value": "019", "support_count": 3},
                {"value": "069", "support_count": 2},
            ],
            "diagnostic_straight_seed": [
                {"value": "168", "support_count": 2},
                {"value": "901", "support_count": 2},
            ],
        },
    }


def _aux_summary():
    return {
        "state": "Demo4",
        "date": "2026-07-25",
        "positional": {
            "shortlist_report": {
                "candidates": [
                    {"combo": "168", "score": 20},
                    {"combo": "901", "score": 12},
                ]
            }
        },
        "blackapple": {
            "top_by_variant": {
                "combined": [{"combo": "014", "score": 3}],
            }
        },
    }


def _build():
    return build_merit_allocated_slate(
        pattern_tables=_pattern_tables(),
        candidate_universe=_candidate_universe(),
        aggregated_arena=_arena(),
        translation_sandbox=_sandbox(),
        aux_summary=_aux_summary(),
        target_period="Day",
        maximum_clusters=2,
        width_cap=12,
    )


def test_pattern_scan_excludes_draw_data_from_strict_merit():
    profiles = scan_pattern_tables(_pattern_tables())
    index9_literals = profiles[9]["literals"]

    assert "591" not in index9_literals
    assert "901" in index9_literals
    assert "096" in index9_literals


def test_multi_cluster_route_protects_primary_and_secondary_vtrac_clusters():
    payload = _build()
    boxed = payload["surfaces"]["BOXED12"]
    straight = payload["surfaces"]["STRAIGHT12"]
    selected = payload["pattern_scan_receipt"]["selected_vtrac_indices"]

    assert payload["artifact_type"] == ARTIFACT_TYPE
    assert selected == [18, 9]
    assert boxed["candidate_count"] <= 12
    assert straight["candidate_count"] <= 12
    assert {row["vtrac_index"] for row in boxed["candidates"]} == {18, 9}
    assert {row["vtrac_index"] for row in straight["candidates"]} == {18, 9}
    assert "019" in {row["canonical"] for row in boxed["candidates"]}
    assert payload["evidence_safety"]["draw_data_scanned"] is False


def test_straight_surface_can_translate_a_strict_vcode_into_a_boxed_lane_mate():
    payload = _build()
    by_literal = {
        row["literal"]: row
        for row in payload["surfaces"]["STRAIGHT12"]["candidates"]
    }

    assert "091" in by_literal
    assert "ordered_lane_mate" in by_literal["091"]["generation_types"]
    assert by_literal["091"]["ordered_vcode"] == "v152"
    assert by_literal["091"]["canonical"] == "019"
    if "591" in by_literal:
        assert by_literal["591"]["is_direct_pattern"] is False
        assert by_literal["591"]["pattern_receipt"]["pattern_cell_count"] == 0


def test_route_is_deterministic_and_does_not_force_more_than_caps():
    first = _build()
    second = _build()

    assert first["cluster_ledger"] == second["cluster_ledger"]
    assert first["surfaces"] == second["surfaces"]
    for surface in first["surfaces"].values():
        assert surface["candidate_count"] <= surface["width_cap"]
        assert all(
            row["allocated_count"] <= 6
            for row in surface["allocation_by_cluster"]
        )


def test_deep_review_mapping_keeps_boxed_and_straight_routes_separate():
    payload = _build()
    routes = payload["deep_review_mapping"]["surface_routes"]

    assert routes["BOXED12"]["route_family"] == "BOX_DIVERSIFIED"
    assert routes["BOXED12"]["play_mode"] == "BOX"
    assert routes["BOXED12"]["members_locator"].endswith("[*].canonical")
    assert routes["STRAIGHT12"]["route_family"] == "STR_DIVERSIFIED"
    assert routes["STRAIGHT12"]["play_mode"] == "STRAIGHT"
    assert routes["STRAIGHT12"]["members_locator"].endswith("[*].literal")
    assert (
        routes["BOXED12"]["generator_identity"]
        != routes["STRAIGHT12"]["generator_identity"]
    )


def test_weak_cluster_fails_structural_gate_even_with_aux_candidate():
    tables = _pattern_tables()
    weak = "225"
    tables["sections"]["Combined"]["sets"]["Set1"]["Draw1"]["pattern_variations"][
        "R2"
    ][0] += weak
    sandbox = _sandbox()
    sandbox["brain2_context"]["blackapple_recommended_canonicals"].append(weak)

    payload = build_merit_allocated_slate(
        pattern_tables=tables,
        candidate_universe=_candidate_universe(),
        aggregated_arena=_arena(),
        translation_sandbox=sandbox,
        aux_summary=_aux_summary(),
        maximum_clusters=4,
    )
    weak_row = next(
        row for row in payload["cluster_ledger"] if row["vtrac_index"] == 10
    )

    assert weak_row["eligible"] is False
    assert weak_row["selected"] is False


def test_shadow_mode_rejects_winner_side_pattern_path(tmp_path):
    with pytest.raises(ValueError, match="winner-side"):
        build_merit_allocated_slate(
            pattern_tables=_pattern_tables(),
            candidate_universe=_candidate_universe(),
            aggregated_arena=_arena(),
            translation_sandbox=_sandbox(),
            tables_path=tmp_path / "winner_tables.json",
            run_mode="shadow",
        )


def test_grader_separates_boxed_and_straight_results():
    slate = {
        "artifact_type": ARTIFACT_TYPE,
        "metadata": {
            "state_key": "Demo4",
            "results_date": "2026-07-25",
        },
        "pattern_scan_receipt": {
            "selected_vtrac_indices": [18, 9],
        },
        "surfaces": {
            "BOXED12": {
                "candidate_count": 2,
                "straight_equivalent_lines": 12,
                "candidates": [
                    {"canonical": "168", "vtrac_index": 18},
                    {"canonical": "019", "vtrac_index": 9},
                ],
            },
            "STRAIGHT12": {
                "candidate_count": 2,
                "candidates": [
                    {"literal": "901", "canonical": "019", "vtrac_index": 9},
                    {"literal": "091", "canonical": "019", "vtrac_index": 9},
                ],
            },
        },
    }
    grade = grade_merit_slate(copy.deepcopy(slate), winner="091", period="Evening")

    assert grade["winner_cluster_selected"] is True
    assert grade["surface_grades"]["BOXED12"]["match_class"] == "CANONICAL_BOX"
    assert grade["surface_grades"]["STRAIGHT12"]["match_class"] == "STRAIGHT"
