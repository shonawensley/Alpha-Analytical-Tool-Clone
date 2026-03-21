from scripts.tools.summarize_aggregated_arena_bridge_family_modes import (
    _family_mode_summary,
    _mode_hint,
    _sample_band,
)


def test_sample_band_respects_thresholds() -> None:
    assert _sample_band(1, thin_threshold=3, measured_threshold=5) == "thin"
    assert _sample_band(3, thin_threshold=3, measured_threshold=5) == "provisional"
    assert _sample_band(5, thin_threshold=3, measured_threshold=5) == "measured"


def test_mode_hint_distinguishes_same_day_and_future_day_shapes() -> None:
    assert _mode_hint(1, 0, 0, 0, 0) == "same_day_only"
    assert _mode_hint(0, 0, 0, 1, 0) == "future_day_only"
    assert _mode_hint(1, 0, 0, 0, 1) == "same_day_mixed"
    assert _mode_hint(0, 0, 0, 1, 1) == "future_day_mixed"
    assert _mode_hint(1, 0, 0, 1, 1) == "mixed_all_modes"


def test_family_mode_summary_builds_ratios_and_labels() -> None:
    rows = [
        {"source_mix": "aux_overdue+aux_badge", "outcome": "Midday", "box_resolution_profile": "direct_same_outcome"},
        {"source_mix": "aux_overdue+aux_badge", "outcome": "Midday", "box_resolution_profile": "miss"},
        {"source_mix": "aux_overdue+aux_badge", "outcome": "Midday", "box_resolution_profile": "same_day_carryforward"},
        {"source_mix": "due_doubles+aux_badge", "outcome": "Evening", "box_resolution_profile": "future_day_decay"},
    ]

    summary = _family_mode_summary(rows, thin_threshold=3, measured_threshold=5)

    assert summary == [
        {
            "source_mix": "aux_overdue+aux_badge",
            "outcome": "Midday",
            "rows": "3",
            "sample_band": "provisional",
            "mode_hint": "same_day_mixed",
            "same_day_any": "2/3",
            "resolved_any": "2/3",
            "direct_same_outcome": "1/3",
            "same_day_precursor_plus_same_day": "0/3",
            "same_day_carryforward": "1/3",
            "future_day_decay": "0/3",
            "miss": "1/3",
        },
        {
            "source_mix": "due_doubles+aux_badge",
            "outcome": "Evening",
            "rows": "1",
            "sample_band": "thin",
            "mode_hint": "future_day_only",
            "same_day_any": "0/1",
            "resolved_any": "1/1",
            "direct_same_outcome": "0/1",
            "same_day_precursor_plus_same_day": "0/1",
            "same_day_carryforward": "0/1",
            "future_day_decay": "1/1",
            "miss": "0/1",
        },
    ]
