from __future__ import annotations

from scripts.tools.analyze_aggregated_arena_bridge_corpus import (
    _group_counts,
    _matches_focus_gate,
    _normalize_row,
    _outcome_class,
    _rank_band,
    _watchlist_band,
)


def test_outcome_class_prefers_same_day_over_decay() -> None:
    row = {
        "same_day_box_hit": "1",
        "same_day_exact_hit": "0",
        "within_3d_box_hit": "1",
        "within_3d_exact_hit": "1",
    }
    assert _outcome_class(row) == "same_day"


def test_rank_and_watchlist_bands() -> None:
    assert _rank_band(3) == "front3"
    assert _rank_band(5) == "front5"
    assert _rank_band(9) == "wider"
    assert _rank_band(None) == "unknown"

    assert _watchlist_band(10) == "small"
    assert _watchlist_band(11) == "medium"
    assert _watchlist_band(14) == "large"
    assert _watchlist_band(None) == "unknown"


def test_normalize_row_adds_window_and_bands() -> None:
    row = {
        "rule_name": "top4_perm",
        "source_mix": "aux_overdue+aux_badge",
        "arena_vtrac_rank": "4",
        "watchlist_canonical_count": "13",
        "box_resolution_profile": "future_day_decay",
        "same_day_box_hit": "0",
        "same_day_exact_hit": "0",
        "within_3d_box_hit": "1",
        "within_3d_exact_hit": "0",
    }
    out = _normalize_row(row, window="W1")
    assert out["window"] == "W1"
    assert out["outcome_class"] == "decay_only"
    assert out["arena_vtrac_rank_band"] == "front5"
    assert out["watchlist_band"] == "medium"
    assert out["box_resolution_profile"] == "future_day_decay"


def test_matches_focus_gate_requires_gap_and_rank() -> None:
    row = {
        "gap_detail": "lane_alive_literal_missing_front3",
        "arena_vtrac_rank": "3",
    }
    assert _matches_focus_gate(row, gap_details=["lane_alive_literal_missing_front3"], max_vtrac_rank=5) is True
    assert _matches_focus_gate(row, gap_details=["family_alive_literal_missing_front5"], max_vtrac_rank=5) is False
    assert _matches_focus_gate(row, gap_details=["lane_alive_literal_missing_front3"], max_vtrac_rank=2) is False


def test_group_counts_summarizes_outcome_classes() -> None:
    rows = [
        {"outcome": "Midday", "outcome_class": "same_day"},
        {"outcome": "Midday", "outcome_class": "miss"},
        {"outcome": "Evening", "outcome_class": "decay_only"},
    ]
    grouped = _group_counts(rows, key="outcome")
    assert grouped == [
        {"outcome": "Evening", "rows": "1", "same_day": "0/1", "decay_only": "1/1", "miss": "0/1"},
        {"outcome": "Midday", "rows": "2", "same_day": "1/2", "decay_only": "0/2", "miss": "1/2"},
    ]
