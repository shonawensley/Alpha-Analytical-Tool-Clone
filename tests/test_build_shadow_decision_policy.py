from __future__ import annotations

import json
from pathlib import Path

from scripts.tools.build_shadow_decision_policy import (
    build_shadow_decision_policy_markdown,
    build_shadow_decision_policy_payload,
    write_shadow_decision_policy_files,
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
                "dominant_families": ["225"],
                "primary_canonicals": ["225", "022", "255"],
                "secondary_canonicals": ["049"],
                "primary_vtrac_indices": ["10", "3", "28"],
                "secondary_vtrac_indices": ["15"],
                "survivor_frontier_canonicals": ["225", "255"],
                "survivor_last_remaining_canonicals": ["225"],
                "survivor_last_remaining_vtrac_indices": ["10"],
                "survivor_terminal_profiles": ["multi_literal_single_vtrac_family_with_hidden_support"],
                "context_reinforced_canonicals": ["225"],
                "context_only_pressure": [],
                "profit_alert_implied_canonicals": ["049"],
                "top_profit_alerts": [{"alert_id": "A02", "canonical": "022", "strength": 4, "badges": ["CONS", "DBL"], "suggested": "BOX"}],
                "blackapple_statuses": [{"variant": "Combined", "status": "OFF", "ba_score": 1}],
                "compound_events_top": [{"variant": "Combined", "top_event": "profit_alert_cluster", "priority": 2, "strength_max": 4}],
                "positional_signal_notes": ["Mirror-Echo active"],
                "positional_shortlist_top": [{"combo": "225", "canonical": "225", "tags": ["Mirror-Echo"], "vtrac_index": "10"}],
                "due_double_families": [{"variant": "Combined", "draws_since_double": 12, "families": [{"family": "0/5-2/7"}]}],
                "state_regime": {
                    "dominant_canonical": "225",
                    "dominant_vtrac_index": "10",
                    "double_heavy": True,
                    "context_reinforced": True,
                    "vtrac_alignment": "aligned",
                    "survivor_pressure": True,
                    "survivor_progression": True,
                    "last_remaining": True,
                    "hidden_terminal_support": True,
                    "survivor_frontier_count": 3,
                    "survivor_progression_count": 2,
                    "last_remaining_rows": 1,
                },
            },
            {
                "state_key": "NewJersey4",
                "dominant_families": ["455"],
                "primary_canonicals": ["455", "559", "003"],
                "secondary_canonicals": ["049"],
                "primary_vtrac_indices": ["5", "4", "1"],
                "secondary_vtrac_indices": ["15"],
                "survivor_frontier_canonicals": ["455"],
                "survivor_last_remaining_canonicals": ["455"],
                "survivor_last_remaining_vtrac_indices": ["5"],
                "survivor_terminal_profiles": ["multi_literal_single_vtrac_family_with_hidden_support"],
                "context_reinforced_canonicals": ["455"],
                "context_only_pressure": [],
                "profit_alert_implied_canonicals": ["049", "055"],
                "top_profit_alerts": [{"alert_id": "A04", "canonical": "049", "strength": 3, "badges": ["PERSIST"], "suggested": "BOX"}],
                "blackapple_statuses": [{"variant": "Combined", "status": "WATCH", "ba_score": 2}],
                "compound_events_top": [],
                "positional_signal_notes": [],
                "positional_shortlist_top": [],
                "due_double_families": [{"variant": "Combined", "draws_since_double": 15, "families": [{"family": "0/5-4/9"}]}],
                "state_regime": {
                    "dominant_canonical": "455",
                    "dominant_vtrac_index": "5",
                    "double_heavy": True,
                    "context_reinforced": True,
                    "vtrac_alignment": "aligned",
                    "survivor_pressure": True,
                    "survivor_progression": True,
                    "last_remaining": True,
                    "hidden_terminal_support": True,
                    "survivor_frontier_count": 4,
                    "survivor_progression_count": 3,
                    "last_remaining_rows": 1,
                },
            },
        ],
    }


def _scoreboard_fixture() -> dict:
    return {
        "metadata": {
            "generated_from_overlay": "Competition8 Evening Rerank After Midday",
            "results_date": "2026-03-21",
            "profile": "tool_only",
            "experiment_tag": "arena_v0",
        },
        "scoreboard_rows": [
            {
                "score_rank": 1,
                "state_key": "NewJersey4",
                "priority_score": 32,
                "role": "shared_host",
                "spent_status": "mostly_unspent",
                "evening_bias": "still_live",
                "targeting_bucket": "tight_core",
                "tracker_posture": "tracker-support",
                "best_blackapple": "Combined:WATCH/2",
                "profit_alert_hint": "A04:049:PERSIST",
                "compound_event_hint": "-",
                "positional_hint": "-",
                "due_double_hint": "Combined:0/5-4/9",
                "overlap_score": 28,
                "primary_overlap_hits": 4,
                "direct_cross_hits": 0,
            },
            {
                "score_rank": 2,
                "state_key": "Virginia4",
                "priority_score": 42,
                "role": "echo",
                "spent_status": "cross_state_spent",
                "evening_bias": "still_live",
                "targeting_bucket": "watch_only",
                "tracker_posture": "tracker-strong",
                "best_blackapple": "Combined:OFF/1",
                "profit_alert_hint": "A02:022:CONS,DBL",
                "compound_event_hint": "Combined:profit_alert_cluster:P2",
                "positional_hint": "Mirror-Echo active",
                "due_double_hint": "Combined:0/5-2/7",
                "overlap_score": 69,
                "primary_overlap_hits": 9,
                "direct_cross_hits": 1,
            },
        ],
    }


def test_build_shadow_decision_policy_payload_and_files(tmp_path: Path) -> None:
    payload = build_shadow_decision_policy_payload(
        overlay_payload=_overlay_fixture(),
        scoreboard_payload=_scoreboard_fixture(),
    )

    assert payload["schema_version"] == "shadow_decision_policy_v0"
    assert payload["shadow_verdict"]["top_play_state"] == "NewJersey4"
    assert payload["shadow_verdict"]["top_watch_state"] == "Virginia4"

    decisions = {row["state_key"]: row for row in payload["state_decisions"]}
    assert decisions["NewJersey4"]["posture"] == "PLAY"
    assert decisions["NewJersey4"]["mode"] in {"boxed", "vt_box"}
    assert decisions["NewJersey4"]["translator_route"] in {"boxed", "vt_box"}
    assert "PLAY_STATE" in decisions["NewJersey4"]["reason_codes"]
    assert "LAST_REMAINING" in decisions["NewJersey4"]["reason_codes"]
    assert "HIDDEN_TERMINAL_SUPPORT" in decisions["NewJersey4"]["reason_codes"]
    assert decisions["Virginia4"]["posture"] == "WATCH"
    assert "CONSENSUS_EVENT" in decisions["Virginia4"]["reason_codes"]
    assert "SURVIVOR_PROGRESSION" in decisions["Virginia4"]["reason_codes"]
    assert "WATCH_RELATIONSHIP" in decisions["Virginia4"]["blockers"]

    md = build_shadow_decision_policy_markdown(payload)
    assert "Shadow Decision Policy" in md
    assert "NewJersey4" in md and "Virginia4" in md
    assert "Shadow Verdict" in md

    out_md = tmp_path / "shadow_dpl.md"
    md_path, json_path = write_shadow_decision_policy_files(out_md_path=out_md, payload=payload, write_json=True)
    assert md_path.exists()
    assert json_path is not None and json_path.exists()

    reloaded = json.loads(json_path.read_text(encoding="utf-8"))
    assert reloaded["shadow_verdict"]["top_play_state"] == "NewJersey4"
