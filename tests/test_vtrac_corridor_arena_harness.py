from scripts.tools.create_vtrac_corridor_arena_harness import (
    CLASS_ARENA_BOXED_CORRIDOR_CAPTURE,
    CLASS_ARENA_ORDERED_LANE_CAPTURE,
    CLASS_DRAW_DATA_INFLATED,
    CLASS_ENHANCED_INDEX_CAPTURE,
    CLASS_NOT_CAPTURED,
    CLASS_RENDERER_GAP,
    CLASS_SOURCE_INDEX_MISMATCH,
    CLASS_WINNER_LENS_ONLY,
    _iter_winner_jsons,
    classify_case,
)


def test_classify_case_marks_ordered_and_boxed_capture() -> None:
    labels = classify_case(
        ordered_lane_match=True,
        boxed_corridor_match=True,
        enhanced_index_rank=5,
        winner_pattern_hits=12,
        renderer_gap=True,
        draw_data_inflation_warning=True,
        source_index_mismatch_count=2,
    )

    assert CLASS_ARENA_ORDERED_LANE_CAPTURE in labels
    assert CLASS_ARENA_BOXED_CORRIDOR_CAPTURE in labels
    assert CLASS_ENHANCED_INDEX_CAPTURE in labels
    assert CLASS_RENDERER_GAP in labels
    assert CLASS_DRAW_DATA_INFLATED in labels
    assert CLASS_SOURCE_INDEX_MISMATCH in labels
    assert CLASS_WINNER_LENS_ONLY not in labels


def test_classify_case_marks_winner_lens_only_when_arena_misses() -> None:
    labels = classify_case(
        ordered_lane_match=False,
        boxed_corridor_match=False,
        enhanced_index_rank=None,
        winner_pattern_hits=8,
        renderer_gap=False,
        draw_data_inflation_warning=False,
        source_index_mismatch_count=0,
    )

    assert labels == [CLASS_WINNER_LENS_ONLY]


def test_classify_case_marks_not_captured_when_no_signal() -> None:
    labels = classify_case(
        ordered_lane_match=False,
        boxed_corridor_match=False,
        enhanced_index_rank=None,
        winner_pattern_hits=0,
        renderer_gap=False,
        draw_data_inflation_warning=False,
        source_index_mismatch_count=0,
    )

    assert labels == [CLASS_NOT_CAPTURED]


def test_winner_inventory_deduplicates_timestamped_artifacts(tmp_path) -> None:
    state_dir = tmp_path / "2026-03-09" / "Connecticut4"
    state_dir.mkdir(parents=True)
    first = state_dir / "Connecticut4_vtrac9_winner_091_20260101.json"
    latest = state_dir / "Connecticut4_vtrac9_winner_091_20260102.json"
    first.write_text("{}", encoding="utf-8")
    latest.write_text("{}", encoding="utf-8")

    paths, duplicates = _iter_winner_jsons(tmp_path, "2026-03-09", [])

    assert paths == [latest]
    assert len(duplicates) == 1
    assert duplicates[0]["winner"] == "091"
    assert duplicates[0]["selection_policy"] == (
        "lexicographically_latest_filename"
    )
