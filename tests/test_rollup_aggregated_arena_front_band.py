from __future__ import annotations

import csv
from pathlib import Path

from scripts.tools.rollup_aggregated_arena_front_band import build_front_band_rollup


def _write_csv(path: Path, rows) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        if fieldnames:
            writer.writeheader()
            for row in rows:
                writer.writerow(row)


def test_front_band_rollup_groups_sources_and_decay(tmp_path: Path) -> None:
    review_csv = tmp_path / "review.csv"
    decay_csv = tmp_path / "decay.csv"
    out_rows = tmp_path / "rows.csv"
    out_sources = tmp_path / "sources.csv"
    out_mixes = tmp_path / "mixes.csv"
    out_md = tmp_path / "rollup.md"

    _write_csv(
        review_csv,
        [
            {
                "date": "2026-01-01",
                "state_key": "StateA",
                "outcome": "Midday",
                "winner": "366",
                "gap_detail": "lane_alive_literal_missing_front3",
                "arena_vtrac_rank": "2",
                "candidate_universe_box_present": "0",
                "candidate_universe_straight_present": "0",
                "play_card_box_present": "0",
                "play_card_straight_present": "0",
                "winner_canonical_profit_alert_present": "0",
                "winner_vtrac_profit_alert_present": "0",
                "winner_canonical_blackapple_present": "0",
                "winner_vtrac_blackapple_present": "0",
                "winner_canonical_due_doubles_present": "1",
                "winner_vtrac_due_doubles_present": "1",
                "winner_vtrac_repeat_watch_present": "0",
                "winner_vtrac_aux_overdue_present": "1",
                "winner_canonical_aux_badge_present": "0",
                "winner_vtrac_aux_badge_present": "1",
            },
            {
                "date": "2026-01-01",
                "state_key": "StateA",
                "outcome": "Evening",
                "winner": "663",
                "gap_detail": "lane_alive_literal_missing_front5",
                "arena_vtrac_rank": "4",
                "candidate_universe_box_present": "0",
                "candidate_universe_straight_present": "0",
                "play_card_box_present": "0",
                "play_card_straight_present": "0",
                "winner_canonical_profit_alert_present": "0",
                "winner_vtrac_profit_alert_present": "0",
                "winner_canonical_blackapple_present": "0",
                "winner_vtrac_blackapple_present": "0",
                "winner_canonical_due_doubles_present": "1",
                "winner_vtrac_due_doubles_present": "1",
                "winner_vtrac_repeat_watch_present": "0",
                "winner_vtrac_aux_overdue_present": "1",
                "winner_canonical_aux_badge_present": "0",
                "winner_vtrac_aux_badge_present": "1",
            },
            {
                "date": "2026-01-02",
                "state_key": "StateB",
                "outcome": "Midday",
                "winner": "455",
                "gap_detail": "family_alive_literal_missing_front5",
                "arena_vtrac_rank": "5",
                "candidate_universe_box_present": "0",
                "candidate_universe_straight_present": "0",
                "play_card_box_present": "0",
                "play_card_straight_present": "0",
                "winner_canonical_profit_alert_present": "0",
                "winner_vtrac_profit_alert_present": "0",
                "winner_canonical_blackapple_present": "0",
                "winner_vtrac_blackapple_present": "0",
                "winner_canonical_due_doubles_present": "0",
                "winner_vtrac_due_doubles_present": "0",
                "winner_vtrac_repeat_watch_present": "1",
                "winner_vtrac_aux_overdue_present": "1",
                "winner_canonical_aux_badge_present": "0",
                "winner_vtrac_aux_badge_present": "1",
            },
            {
                "date": "2026-01-03",
                "state_key": "StateC",
                "outcome": "Midday",
                "winner": "123",
                "gap_detail": "thin_conversion_gap",
                "arena_vtrac_rank": "9",
                "candidate_universe_box_present": "0",
                "candidate_universe_straight_present": "0",
                "play_card_box_present": "0",
                "play_card_straight_present": "0",
                "winner_canonical_profit_alert_present": "0",
                "winner_vtrac_profit_alert_present": "0",
                "winner_canonical_blackapple_present": "0",
                "winner_vtrac_blackapple_present": "0",
                "winner_canonical_due_doubles_present": "0",
                "winner_vtrac_due_doubles_present": "0",
                "winner_vtrac_repeat_watch_present": "0",
                "winner_vtrac_aux_overdue_present": "0",
                "winner_canonical_aux_badge_present": "0",
                "winner_vtrac_aux_badge_present": "0",
            },
        ],
    )
    _write_csv(
        decay_csv,
        [
            {
                "snapshot_date": "2026-01-01",
                "state_key": "StateA",
                "dominant_vtrac_same_day": "1",
                "dominant_vtrac_within_3d": "1",
                "watchlist_box_same_day": "0",
                "watchlist_box_within_3d": "1",
            },
            {
                "snapshot_date": "2026-01-02",
                "state_key": "StateB",
                "dominant_vtrac_same_day": "0",
                "dominant_vtrac_within_3d": "1",
                "watchlist_box_same_day": "0",
                "watchlist_box_within_3d": "0",
            },
        ],
    )

    summary = build_front_band_rollup(
        review_csv=review_csv,
        decay_csv=decay_csv,
        out_rows_csv=out_rows,
        out_source_csv=out_sources,
        out_mix_csv=out_mixes,
        out_md=out_md,
        min_mix_rows=1,
    )

    assert summary["total_rows"] == 3
    assert summary["gap_counts"]["lane_alive_literal_missing_front3"] == 1
    assert summary["gap_counts"]["lane_alive_literal_missing_front5"] == 1
    assert summary["gap_counts"]["family_alive_literal_missing_front5"] == 1

    source_rows = {row["source"]: row for row in summary["source_rows"]}
    assert source_rows["aux_overdue"]["rows"] == "3"
    assert source_rows["aux_badge"]["watchlist_box_within_3d"] == "2/3"
    assert source_rows["due_doubles"]["rows"] == "2"

    mix_rows = {row["source_mix"]: row for row in summary["mix_rows"]}
    assert mix_rows["due_doubles+aux_overdue+aux_badge"]["rows"] == "2"
    assert mix_rows["due_doubles+aux_overdue+aux_badge"]["watchlist_box_within_3d"] == "2/2"
    assert mix_rows["repeat_watch+aux_overdue+aux_badge"]["rows"] == "1"

    bridge_rows = {row["source_mix"]: row for row in summary["bridge_rows"]}
    assert "due_doubles+aux_overdue+aux_badge" in bridge_rows
    assert "repeat_watch+aux_overdue+aux_badge" not in bridge_rows

    assert out_rows.exists()
    assert out_sources.exists()
    assert out_mixes.exists()
    assert out_md.exists()
