from __future__ import annotations

import csv
import json
from pathlib import Path

from scripts.tools.build_board_spillover_overlay import (
    build_board_spillover_overlay_markdown,
    build_board_spillover_overlay_payload,
    write_board_spillover_overlay_files,
)


def _write_csv(path: Path, rows, fieldnames) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _arena_fixture(
    *,
    state_key: str,
    top_canonicals: list[str],
    top_indices: list[str],
    watchlist: list[dict[str, object]],
    blackapple_status: str,
    blackapple_score: int,
    due_family: str,
    alert_canonical: str,
) -> dict:
    return {
        "schema_version": "aggregated_analysis_arena_v0",
        "metadata": {"state_key": state_key, "results_date": "2026-03-21"},
        "arena_synthesis": {
            "dominant_canonicals": [{"value": value} for value in top_canonicals],
            "dominant_vtrac_indices": [{"value": value} for value in top_indices],
            "dominant_families": [{"value": top_canonicals[0]}],
            "vtrac_literal_watchlist": watchlist,
            "context_reinforced_canonicals": [{"value": top_canonicals[0]}],
            "context_only_pressure": [],
            "r_consensus_context": {
                "available": True,
                "event_count": 2,
                "single_digit_count": 0,
                "two_digit_count": 2,
                "col1_count": 1,
                "col2_count": 1,
                "top_tail_values": [alert_canonical[-2:]],
                "cross_variant_tail_values": [alert_canonical[-2:]],
                "top_support_canonicals": [top_canonicals[0], top_canonicals[-1]],
                "top_support_vtrac_indices": [top_indices[0]],
                "signal_strength_class": "strong",
                "trial_eligible": True,
            },
            "stable_survivor_context": {
                "available": True,
                "frontier_count": 3,
                "progression_count": 2,
                "last_remaining_rows": 1,
                "hidden_terminal_frontier_count": 1,
                "top_frontier_canonicals": [top_canonicals[0], top_canonicals[-1]],
                "top_last_remaining_canonicals": [top_canonicals[0]],
                "top_frontier_vtrac_indices": [top_indices[0]],
                "top_last_remaining_vtrac_indices": [top_indices[0]],
                "last_remaining_examples": [{"profile": "multi_literal_single_vtrac_family_with_hidden_support"}],
            },
            "state_regime": {
                "dominant_canonical": top_canonicals[0],
                "dominant_vtrac_index": top_indices[0],
                "dominant_family": top_canonicals[0],
                "double_heavy": True,
                "context_reinforced": True,
                "vtrac_alignment": "aligned",
                "tail_consensus_present": True,
                "tail_consensus_value": alert_canonical[-2:],
                "tail_consensus_column": "col1",
                "consensus_strength_class": "strong",
                "consensus_trial_eligible": True,
                "survivor_pressure": True,
                "survivor_progression": True,
                "last_remaining": True,
                "hidden_terminal_support": True,
                "survivor_frontier_count": 3,
                "survivor_progression_count": 2,
                "last_remaining_rows": 1,
                "r_consensus_event_count": 2,
                "r_consensus_cross_variant_tail_count": 1,
            },
        },
        "context_tools": {
            "aux_control_center": {
                "arena_objects": {
                    "cc_profit_alert_context": {
                        "top_alerts": [
                            {
                                "alert_id": "A04",
                                "variant": "Combined",
                                "canonical": alert_canonical,
                                "strength": 4,
                                "badges": ["PERSIST"],
                                "suggested": "BOX",
                                "implied_set_size": 6,
                            }
                        ]
                    },
                    "aux_blackapple_context": {
                        "recommended_canonicals_top": [top_canonicals[0], top_canonicals[-1]],
                        "control_center_top": [
                            {
                                "variant": "Combined",
                                "status": blackapple_status,
                                "ba_score": blackapple_score,
                                "candidate_count": 8,
                                "examples": [top_canonicals[0]],
                                "triggers": "Pairs 1",
                            }
                        ]
                    },
                    "aux_positional_pressure": {
                        "signal_notes_top": ["Mirror-Echo active", "Double-pressure cluster"],
                        "shortlist_top": [
                            {
                                "combo": top_canonicals[0],
                                "canonical": top_canonicals[0],
                                "score": 44.2,
                                "tags": ["Mirror-Echo"],
                                "vtrac_index": top_indices[0],
                            }
                        ]
                    },
                    "aux_due_doubles_family_pressure": {
                        "available": True,
                        "top_example_canonicals": [top_canonicals[0], top_canonicals[-1]],
                        "by_variant": {
                            "Combined": {
                                "draws_since_double": 12,
                                "families": [
                                    {
                                        "family": due_family,
                                        "slot": "Family 1",
                                        "examples": [top_canonicals[0]],
                                    }
                                ],
                            }
                        },
                    },
                    "cc_compound_event_context": {
                        "top_events": [
                            {
                                "variant": "Combined",
                                "top_event": "profit_alert_cluster",
                                "priority": 2,
                                "candidate_alert_ids": ["A04"],
                                "promoter_alert_ids": ["A12"],
                                "watchlist_tags": ["persist"],
                                "strength_max": 4,
                            }
                        ]
                    },
                }
            }
        },
    }


def test_build_board_spillover_overlay_payload_and_markdown(tmp_path: Path) -> None:
    repo_root = tmp_path
    sharepacks_root = repo_root / "sharepacks" / "_predictive"
    day_dir = sharepacks_root / "2026-03-21"

    nj_path = day_dir / "NewJersey4" / "analysis" / "aggregated_analysis_arena__tool_only__arena_v0.json"
    nj_path.parent.mkdir(parents=True, exist_ok=True)
    nj_path.write_text(
        json.dumps(
            _arena_fixture(
                state_key="NewJersey4",
                top_canonicals=["455", "055"],
                top_indices=["5", "1"],
                watchlist=[{"vtrac_index": "1", "candidate_canonicals": ["055"]}],
                blackapple_status="WATCH",
                blackapple_score=3,
                due_family="0/5-4/9",
                alert_canonical="055",
            )
        ),
        encoding="utf-8",
    )

    nc_path = day_dir / "NorthCarolina4" / "analysis" / "aggregated_analysis_arena__tool_only__arena_v0.json"
    nc_path.parent.mkdir(parents=True, exist_ok=True)
    nc_path.write_text(
        json.dumps(
            _arena_fixture(
                state_key="NorthCarolina4",
                top_canonicals=["299", "499"],
                top_indices=["31", "35"],
                watchlist=[{"vtrac_index": "31", "candidate_canonicals": ["299"]}],
                blackapple_status="ALERT",
                blackapple_score=5,
                due_family="2/7-4/9",
                alert_canonical="299",
            )
        ),
        encoding="utf-8",
    )

    _write_csv(
        day_dir / "control_center" / "profit_alerts.csv",
        [
            {
                "State": "New Jersey",
                "StateKey": "NewJersey4",
                "Variant": "Combined",
                "AlertId": "A04",
                "Strength": "4",
                "Suggested": "BOX",
                "CapLines": "6",
                "DecayDraws": "4",
                "Badges": "PERSIST",
                "Canonical": "055",
                "ImpliedSet": '["005","055","500","550"]',
                "Evidence": "",
                "Winner Midday": "",
                "Winner Evening": "",
                "Midday Hits": "",
                "Evening Hits": "",
            },
            {
                "State": "North Carolina",
                "StateKey": "NorthCarolina4",
                "Variant": "Combined",
                "AlertId": "A01",
                "Strength": "4",
                "Suggested": "BOX",
                "CapLines": "6",
                "DecayDraws": "4",
                "Badges": "CONS",
                "Canonical": "299",
                "ImpliedSet": '["299","992","924","249"]',
                "Evidence": "",
                "Winner Midday": "",
                "Winner Evening": "",
                "Midday Hits": "",
                "Evening Hits": "",
            },
        ],
        [
            "State",
            "StateKey",
            "Variant",
            "AlertId",
            "Strength",
            "Suggested",
            "CapLines",
            "DecayDraws",
            "Badges",
            "Canonical",
            "ImpliedSet",
            "Evidence",
            "Winner Midday",
            "Winner Evening",
            "Midday Hits",
            "Evening Hits",
        ],
    )

    midday_path = repo_root / "midday.txt"
    midday_path.write_text(
        "Pick 3\nMidday\tEvening\nNew Jersey\t992\t\nNorth Carolina\t550\t\n",
        encoding="utf-8",
    )

    payload = build_board_spillover_overlay_payload(
        day_dir=day_dir,
        results_date="2026-03-21",
        states=["NewJersey4", "NorthCarolina4"],
        profile="tool_only",
        experiment_tag="arena_v0",
        board_name="Competition 8",
        sharepacks_root=sharepacks_root,
        repo_root=repo_root,
        midday_results_path=midday_path,
        top_items=6,
    )

    assert payload["schema_version"] == "board_spillover_overlay_v0"
    assert payload["board_context"]["midday_results_available"] is True

    state_summaries = {row["state_key"]: row for row in payload["state_summaries"]}
    assert state_summaries["NewJersey4"]["midday_status"]["spent_status"] == "cross_state_spent"
    assert state_summaries["NorthCarolina4"]["midday_status"]["spent_status"] == "cross_state_spent"
    assert "055" in state_summaries["NewJersey4"]["primary_canonicals"]
    assert "299" in state_summaries["NorthCarolina4"]["primary_canonicals"]
    assert "455" in state_summaries["NewJersey4"]["blackapple_recommended_canonicals"]
    assert "455" in state_summaries["NewJersey4"]["survivor_frontier_canonicals"]
    assert "455" in state_summaries["NewJersey4"]["survivor_last_remaining_canonicals"]
    assert state_summaries["NewJersey4"]["survivor_terminal_profiles"][0] == "multi_literal_single_vtrac_family_with_hidden_support"
    assert state_summaries["NewJersey4"]["positional_signal_notes"][0] == "Mirror-Echo active"
    assert state_summaries["NewJersey4"]["compound_events_top"][0]["top_event"] == "profit_alert_cluster"
    assert "055" in state_summaries["NewJersey4"]["due_double_example_canonicals"]
    assert "055" in state_summaries["NewJersey4"]["secondary_canonicals"]
    assert state_summaries["NewJersey4"]["state_regime"]["last_remaining"] is True
    assert state_summaries["NewJersey4"]["r_consensus_context"]["available"] is True
    assert state_summaries["NewJersey4"]["r_consensus_top_tail_values"]
    assert state_summaries["NewJersey4"]["r_consensus_support_canonicals"][0] == "455"
    assert state_summaries["NewJersey4"]["state_regime"]["tail_consensus_present"] is True

    relationships = payload["relationships"]
    assert any(
        row["relationship_type"] == "alert_implied_echo"
        and row["state_a"] == "NewJersey4"
        and row["state_b"] == "NorthCarolina4"
        and row["directness"] == "direct-cross-state"
        for row in relationships
    )
    assert any(
        row["relationship_type"] == "alert_implied_echo"
        and row["state_a"] == "NorthCarolina4"
        and row["state_b"] == "NewJersey4"
        and row["directness"] == "direct-cross-state"
        for row in relationships
    )
    scoreboard = payload["board_summary"]["board_scoreboard"]
    assert scoreboard
    assert scoreboard[0]["state_key"] in {"NewJersey4", "NorthCarolina4"}
    assert scoreboard[0]["priority_score"] >= scoreboard[-1]["priority_score"]

    md = build_board_spillover_overlay_markdown(payload)
    assert "Board Spillover Overlay" in md
    assert "Board Scoreboard" in md
    assert "Relationships" in md
    assert "NewJersey4" in md
    assert "NorthCarolina4" in md

    out_json = repo_root / "docs" / "overlay.json"
    json_path, md_path = write_board_spillover_overlay_files(out_json_path=out_json, payload=payload, write_md=True)
    assert json_path.exists()
    assert md_path is not None and md_path.exists()
