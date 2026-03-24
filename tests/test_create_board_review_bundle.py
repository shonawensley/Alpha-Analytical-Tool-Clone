from __future__ import annotations

import csv
import json
from pathlib import Path

from scripts.tools.create_board_review_bundle import (
    build_board_review_bundle_markdown,
    build_board_review_bundle_payload,
    write_board_review_bundle_files,
)
from scripts.tools.build_board_spillover_overlay import build_board_spillover_overlay_payload, write_board_spillover_overlay_files
from scripts.tools.create_board_scoreboard import build_board_scoreboard_payload, write_board_scoreboard_files
from scripts.tools.build_shadow_decision_policy import build_shadow_decision_policy_payload, write_shadow_decision_policy_files


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
            "state_regime": {
                "dominant_canonical": top_canonicals[0],
                "dominant_vtrac_index": top_indices[0],
                "dominant_family": top_canonicals[0],
                "double_heavy": True,
                "context_reinforced": True,
                "vtrac_alignment": "aligned",
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
                        "recommended_canonicals_top": [top_canonicals[0]],
                        "control_center_top": [
                            {
                                "variant": "Combined",
                                "status": "WATCH",
                                "ba_score": 2,
                                "candidate_count": 8,
                                "examples": [top_canonicals[0]],
                                "triggers": "Pairs 1",
                            }
                        ]
                    },
                    "aux_positional_pressure": {
                        "signal_notes_top": ["Mirror-Echo active"],
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
                        "top_example_canonicals": [top_canonicals[0]],
                        "by_variant": {
                            "Combined": {
                                "draws_since_double": 12,
                                "families": [
                                    {
                                        "family": "0/5-4/9",
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


def test_build_board_review_bundle_payload_and_files(tmp_path: Path) -> None:
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
                alert_canonical="055",
            )
        ),
        encoding="utf-8",
    )

    va_path = day_dir / "Virginia4" / "analysis" / "aggregated_analysis_arena__tool_only__arena_v0.json"
    va_path.parent.mkdir(parents=True, exist_ok=True)
    va_path.write_text(
        json.dumps(
            _arena_fixture(
                state_key="Virginia4",
                top_canonicals=["225", "049"],
                top_indices=["10", "15"],
                watchlist=[{"vtrac_index": "15", "candidate_canonicals": ["049"]}],
                alert_canonical="049",
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
                "ImpliedSet": '["049","055","500","550","559"]',
                "Evidence": "",
                "Winner Midday": "",
                "Winner Evening": "",
                "Midday Hits": "",
                "Evening Hits": "",
            }
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
    midday_path.write_text("Pick 3\nMidday\tEvening\nVirginia\t940\t\nNew Jersey\t992\t\n", encoding="utf-8")

    overlay_payload = build_board_spillover_overlay_payload(
        day_dir=day_dir,
        results_date="2026-03-21",
        states=["Virginia4", "NewJersey4"],
        profile="tool_only",
        experiment_tag="arena_v0",
        board_name="Competition 8",
        sharepacks_root=sharepacks_root,
        repo_root=repo_root,
        midday_results_path=midday_path,
        top_items=6,
    )
    overlay_json = repo_root / "runs" / "overlay.json"
    overlay_json_path, overlay_md_path = write_board_spillover_overlay_files(
        out_json_path=overlay_json,
        payload=overlay_payload,
        write_md=True,
    )

    scoreboard_payload = build_board_scoreboard_payload(overlay_payload)
    scoreboard_md = repo_root / "runs" / "scoreboard.md"
    scoreboard_md_path, scoreboard_csv_path, scoreboard_json_path = write_board_scoreboard_files(
        out_md_path=scoreboard_md,
        payload=scoreboard_payload,
        write_csv=True,
        write_json=True,
    )

    decision_payload = build_shadow_decision_policy_payload(
        overlay_payload=overlay_payload,
        scoreboard_payload=scoreboard_payload,
    )
    decision_md = repo_root / "runs" / "shadow_dpl.md"
    decision_md_path, decision_json_path = write_shadow_decision_policy_files(
        out_md_path=decision_md,
        payload=decision_payload,
        write_json=True,
    )

    bundle_payload = build_board_review_bundle_payload(
        results_date="2026-03-21",
        board_name="Competition 8",
        overlay_payload=overlay_payload,
        scoreboard_payload=scoreboard_payload,
        decision_policy_payload=decision_payload,
        overlay_json_path=overlay_json_path,
        overlay_md_path=overlay_md_path,
        scoreboard_md_path=scoreboard_md_path,
        scoreboard_csv_path=scoreboard_csv_path,
        scoreboard_json_path=scoreboard_json_path,
        decision_policy_md_path=decision_md_path,
        decision_policy_json_path=decision_json_path,
    )

    assert bundle_payload["schema_version"] == "board_review_bundle_v0"
    assert bundle_payload["board_verdict"]["top_primary_target"]
    assert bundle_payload["artifacts"]["overlay_json"].endswith("overlay.json")
    assert bundle_payload["artifacts"]["shadow_decision_policy_md"].endswith("shadow_dpl.md")
    assert bundle_payload["workflow_manifest"]["brain2_runtime_entrypoint"].endswith("create_board_review_bundle.py")
    assert bundle_payload["workflow_manifest"]["shadow_decision_policy_builder"].endswith("build_shadow_decision_policy.py")
    assert bundle_payload["shadow_decision_policy"]["top_play_state"] or bundle_payload["shadow_decision_policy"]["top_watch_state"]

    md = build_board_review_bundle_markdown(bundle_payload)
    assert "Board Review Bundle" in md
    assert "Board Verdict" in md
    assert "Shadow Decision Policy" in md
    assert "Workflow" in md
    assert "overlay_json" in md

    out_md = repo_root / "runs" / "bundle.md"
    md_path, json_path = write_board_review_bundle_files(out_md_path=out_md, payload=bundle_payload, write_json=True)
    assert md_path.exists()
    assert json_path is not None and json_path.exists()
