from __future__ import annotations

import json
from pathlib import Path

from scripts.tools.create_board_scoreboard import (
    build_board_scoreboard_markdown,
    build_board_scoreboard_payload,
    write_board_scoreboard_files,
)


def _overlay_fixture() -> dict:
    return {
        "metadata": {
            "board_name": "Competition8 Evening Rerank After Midday",
            "results_date": "2026-03-21",
            "profile": "tool_only",
            "experiment_tag": "arena_v0",
        },
        "state_summaries": [
            {
                "state_key": "Virginia4",
                "blackapple_statuses": [{"variant": "Combined", "status": "OFF", "ba_score": 1}],
                "blackapple_recommended_canonicals": ["022", "225"],
                "top_profit_alerts": [{"alert_id": "A02", "canonical": "022", "strength": 4, "badges": ["CONS", "DBL"]}],
                "compound_events_top": [{"variant": "Combined", "top_event": "profit_alert_cluster", "priority": 2, "strength_max": 4}],
                "positional_signal_notes": ["Mirror-Echo active"],
                "due_double_families": [{"variant": "Combined", "draws_since_double": 12, "families": [{"family": "0/5-2/7"}]}],
                "dominant_canonicals": ["225", "022", "255"],
                "dominant_vtrac_indices": ["10", "3", "28"],
                "survivor_terminal_profiles": ["multi_literal_single_vtrac_family_with_hidden_support"],
                "state_regime": {
                    "survivor_pressure": True,
                    "survivor_progression": True,
                    "last_remaining": True,
                    "hidden_terminal_support": True,
                    "survivor_progression_count": 2,
                    "last_remaining_rows": 1,
                },
            },
            {
                "state_key": "NewJersey4",
                "blackapple_statuses": [{"variant": "Combined", "status": "WATCH", "ba_score": 2}],
                "blackapple_recommended_canonicals": ["455", "559"],
                "top_profit_alerts": [{"alert_id": "A04", "canonical": "049", "strength": 3, "badges": ["PERSIST"]}],
                "compound_events_top": [],
                "positional_signal_notes": [],
                "due_double_families": [{"variant": "Combined", "draws_since_double": 15, "families": [{"family": "0/5-4/9"}]}],
                "dominant_canonicals": ["455", "559", "003"],
                "dominant_vtrac_indices": ["5", "4", "1"],
                "state_regime": {},
            },
        ],
        "board_summary": {
            "board_scoreboard": [
                {
                    "state_key": "Virginia4",
                    "input_rank": 1,
                    "priority_score": 42,
                    "role": "echo",
                    "spent_status": "cross_state_spent",
                    "evening_bias": "still_live",
                    "overlap_score": 69,
                    "primary_overlap_hits": 9,
                    "direct_cross_hits": 1,
                },
                {
                    "state_key": "NewJersey4",
                    "input_rank": 2,
                    "priority_score": 32,
                    "role": "shared_host",
                    "spent_status": "mostly_unspent",
                    "evening_bias": "still_live",
                    "overlap_score": 28,
                    "primary_overlap_hits": 4,
                    "direct_cross_hits": 0,
                },
            ],
            "likely_duplicated_pairs": [
                {
                    "state_a": "Virginia4",
                    "state_b": "NewJersey4",
                    "pair_score": 26,
                    "relationship_types": ["alert_implied_echo", "shared_lane"],
                }
            ],
            "strongest_overlap_pairs": [
                {
                    "state_a": "Virginia4",
                    "state_b": "NewJersey4",
                    "pair_score": 26,
                    "relationship_types": ["alert_implied_echo", "shared_lane"],
                }
            ],
        },
        "relationships": [
            {
                "state_a": "NewJersey4",
                "state_b": "Virginia4",
                "relationship_type": "alert_implied_echo",
                "directness": "direct-cross-state",
                "canonical_families": ["049", "559"],
                "explanation": "NewJersey4 profit-alert implied set directly captured Virginia4's Midday family: 049.",
            }
        ],
    }


def test_build_board_scoreboard_payload_and_files(tmp_path: Path) -> None:
    overlay = _overlay_fixture()
    payload = build_board_scoreboard_payload(overlay)

    assert payload["schema_version"] == "board_scoreboard_v0"
    rows = payload["scoreboard_rows"]
    assert rows[0]["state_key"] == "Virginia4"
    assert rows[0]["profit_alert_hint"].startswith("A02")
    assert rows[0]["compound_event_hint"].startswith("Combined:profit_alert_cluster")
    assert rows[0]["blackapple_reco_hint"] == "022,225"
    assert rows[0]["survivor_hint"].startswith("LR:1|Prog:2|Hidden|")
    assert rows[0]["positional_hint"] == "Mirror-Echo active"
    assert rows[1]["targeting_bucket"] == "tight_core"

    verdict = payload["board_verdict"]
    assert verdict["top_primary_target"] == "Virginia4"
    assert verdict["best_clean_host"] == "NewJersey4"
    assert verdict["highest_context_support_state"] == "Virginia4"
    assert verdict["direct_cross_state_receipts"][0]["state_a"] == "NewJersey4"

    md = build_board_scoreboard_markdown(payload)
    assert "Board Scoreboard" in md
    assert "Direct Cross-State Receipts" in md
    assert "Virginia4" in md and "NewJersey4" in md

    out_md = tmp_path / "scoreboard.md"
    md_path, csv_path, json_path = write_board_scoreboard_files(out_md_path=out_md, payload=payload, write_csv=True, write_json=True)
    assert md_path.exists()
    assert csv_path is not None and csv_path.exists()
    assert json_path is not None and json_path.exists()

    reloaded = json.loads(json_path.read_text(encoding="utf-8"))
    assert reloaded["board_verdict"]["top_primary_target"] == "Virginia4"
