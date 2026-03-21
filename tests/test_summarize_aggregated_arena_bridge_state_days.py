from scripts.tools.summarize_aggregated_arena_bridge_state_days import (
    _collapse_state_days,
    _group_state_days,
    _outcome_span,
    _state_day_profile,
)


def test_state_day_profile_prioritizes_same_day_over_future() -> None:
    assert _state_day_profile(["future_day_decay", "miss"]) == "future_day_state"
    assert _state_day_profile(["future_day_decay", "same_day_carryforward"]) == "same_day_state"
    assert _state_day_profile(["miss"]) == "miss"


def test_outcome_span_handles_single_and_dual_outcomes() -> None:
    assert _outcome_span(["Midday"]) == "Midday"
    assert _outcome_span(["Evening"]) == "Evening"
    assert _outcome_span(["Midday", "Evening"]) == "Midday+Evening"


def test_collapse_state_days_merges_duplicate_state_day_family_rows() -> None:
    rows = [
        {
            "source_mix": "aux_overdue+aux_badge",
            "date": "2025-12-31",
            "state_key": "Virginia4",
            "window": "w1",
            "outcome": "Midday",
            "box_resolution_profile": "same_day_carryforward",
            "first_box_event": "2025-12-31 Evening 636",
        },
        {
            "source_mix": "aux_overdue+aux_badge",
            "date": "2025-12-31",
            "state_key": "Virginia4",
            "window": "w1",
            "outcome": "Evening",
            "box_resolution_profile": "direct_same_outcome",
            "first_box_event": "2025-12-31 Evening 636",
        },
        {
            "source_mix": "profit_alert+aux_badge",
            "date": "2026-01-16",
            "state_key": "Florida4",
            "window": "w2",
            "outcome": "Midday",
            "box_resolution_profile": "future_day_decay",
            "first_box_event": "2026-01-17 Evening 273",
        },
    ]

    collapsed = _collapse_state_days(rows)

    assert collapsed == [
        {
            "source_mix": "aux_overdue+aux_badge",
            "date": "2025-12-31",
            "state_key": "Virginia4",
            "window_count": "1",
            "row_count": "2",
            "outcome_span": "Midday+Evening",
            "state_day_profile": "same_day_state",
            "same_day_state": "1",
            "future_day_state": "0",
            "miss_state": "0",
            "first_box_event": "2025-12-31 Evening 636",
        },
        {
            "source_mix": "profit_alert+aux_badge",
            "date": "2026-01-16",
            "state_key": "Florida4",
            "window_count": "1",
            "row_count": "1",
            "outcome_span": "Midday",
            "state_day_profile": "future_day_state",
            "same_day_state": "0",
            "future_day_state": "1",
            "miss_state": "0",
            "first_box_event": "2026-01-17 Evening 273",
        },
    ]


def test_group_state_days_summarizes_family_ratios() -> None:
    rows = [
        {"source_mix": "A", "same_day_state": "1", "future_day_state": "0", "miss_state": "0"},
        {"source_mix": "A", "same_day_state": "0", "future_day_state": "1", "miss_state": "0"},
        {"source_mix": "A", "same_day_state": "0", "future_day_state": "0", "miss_state": "1"},
        {"source_mix": "B", "same_day_state": "1", "future_day_state": "0", "miss_state": "0"},
    ]

    grouped = _group_state_days(rows, key="source_mix")

    assert grouped == [
        {
            "source_mix": "A",
            "state_days": "3",
            "same_day_state": "1/3",
            "future_day_state": "1/3",
            "miss_state": "1/3",
        },
        {
            "source_mix": "B",
            "state_days": "1",
            "same_day_state": "1/1",
            "future_day_state": "0/1",
            "miss_state": "0/1",
        },
    ]
