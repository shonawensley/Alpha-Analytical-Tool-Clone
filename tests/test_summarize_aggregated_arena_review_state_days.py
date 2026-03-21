from scripts.tools.summarize_aggregated_arena_review_state_days import (
    _collapse_state_days,
    _group_counts,
    _group_gap_class,
    _outcome_span,
)


def test_outcome_span_prefers_combined_label() -> None:
    assert _outcome_span(["Midday", "Evening"]) == "Midday+Evening"
    assert _outcome_span(["Evening"]) == "Evening"


def test_collapse_state_days_uses_best_gap_class_and_any_presence_flags() -> None:
    rows = [
        {
            "date": "2026-01-01",
            "state_key": "Florida4",
            "window": "w1",
            "outcome": "Midday",
            "gap_class": "arena_present_but_underweighted",
            "gap_detail": "lane_alive_literal_missing_front3",
            "arena_canonical_any_present": "1",
            "arena_vtrac_any_present": "1",
            "arena_family_any_present": "0",
            "winner_canonical_context_reinforced": "0",
            "winner_vtrac_context_reinforced": "1",
            "winner_family_context_reinforced": "0",
            "winner_canonical_profit_alert_present": "0",
            "winner_vtrac_profit_alert_present": "0",
            "winner_canonical_due_doubles_present": "0",
            "winner_vtrac_due_doubles_present": "0",
            "winner_canonical_blackapple_present": "0",
            "winner_vtrac_blackapple_present": "0",
            "winner_canonical_aux_badge_present": "0",
            "winner_vtrac_aux_badge_present": "1",
            "winner_vtrac_aux_overdue_present": "0",
            "winner_vtrac_repeat_watch_present": "0",
            "candidate_universe_straight_present": "0",
            "candidate_universe_box_present": "0",
            "play_card_straight_present": "0",
            "play_card_box_present": "0",
        },
        {
            "date": "2026-01-01",
            "state_key": "Florida4",
            "window": "w1",
            "outcome": "Evening",
            "gap_class": "downstream_present",
            "gap_detail": "downstream_closed",
            "arena_canonical_any_present": "0",
            "arena_vtrac_any_present": "1",
            "arena_family_any_present": "1",
            "winner_canonical_context_reinforced": "0",
            "winner_vtrac_context_reinforced": "0",
            "winner_family_context_reinforced": "0",
            "winner_canonical_profit_alert_present": "1",
            "winner_vtrac_profit_alert_present": "0",
            "winner_canonical_due_doubles_present": "0",
            "winner_vtrac_due_doubles_present": "0",
            "winner_canonical_blackapple_present": "0",
            "winner_vtrac_blackapple_present": "0",
            "winner_canonical_aux_badge_present": "0",
            "winner_vtrac_aux_badge_present": "0",
            "winner_vtrac_aux_overdue_present": "0",
            "winner_vtrac_repeat_watch_present": "0",
            "candidate_universe_straight_present": "1",
            "candidate_universe_box_present": "0",
            "play_card_straight_present": "0",
            "play_card_box_present": "0",
        },
    ]

    collapsed = _collapse_state_days(rows)

    assert collapsed == [
        {
            "date": "2026-01-01",
            "state_key": "Florida4",
            "window_count": "1",
            "outcome_rows": "2",
            "outcome_span": "Midday+Evening",
            "state_day_gap_class": "downstream_present",
            "state_day_gap_detail": "downstream_closed",
            "arena_canonical_state_present": "1",
            "arena_vtrac_state_present": "1",
            "arena_family_state_present": "1",
            "context_reinforced_state": "1",
            "profit_alert_state": "1",
            "due_doubles_state": "0",
            "blackapple_state": "0",
            "aux_badge_state": "1",
            "aux_overdue_state": "0",
            "repeat_watch_state": "0",
            "candidate_universe_literal_state": "1",
            "play_card_literal_state": "0",
            "downstream_literal_state": "1",
        }
    ]


def test_group_gap_class_and_outcome_span_counts() -> None:
    rows = [
        {
            "state_day_gap_class": "downstream_present",
            "outcome_span": "Midday+Evening",
            "arena_canonical_state_present": "1",
            "arena_vtrac_state_present": "1",
            "arena_family_state_present": "1",
            "context_reinforced_state": "1",
            "downstream_literal_state": "1",
        },
        {
            "state_day_gap_class": "arena_missing",
            "outcome_span": "Evening",
            "arena_canonical_state_present": "0",
            "arena_vtrac_state_present": "0",
            "arena_family_state_present": "0",
            "context_reinforced_state": "0",
            "downstream_literal_state": "0",
        },
    ]

    gap = _group_gap_class(rows)
    span = _group_counts(rows, key="outcome_span")

    assert gap == [
        {"state_day_gap_class": "arena_missing", "state_days": "1", "share": "1/2"},
        {"state_day_gap_class": "downstream_present", "state_days": "1", "share": "1/2"},
    ] or gap == [
        {"state_day_gap_class": "downstream_present", "state_days": "1", "share": "1/2"},
        {"state_day_gap_class": "arena_missing", "state_days": "1", "share": "1/2"},
    ]
    assert span == [
        {
            "outcome_span": "Evening",
            "state_days": "1",
            "arena_canonical_state_present": "0/1",
            "arena_vtrac_state_present": "0/1",
            "arena_family_state_present": "0/1",
            "context_reinforced_state": "0/1",
            "downstream_literal_state": "0/1",
        },
        {
            "outcome_span": "Midday+Evening",
            "state_days": "1",
            "arena_canonical_state_present": "1/1",
            "arena_vtrac_state_present": "1/1",
            "arena_family_state_present": "1/1",
            "context_reinforced_state": "1/1",
            "downstream_literal_state": "1/1",
        },
    ]
