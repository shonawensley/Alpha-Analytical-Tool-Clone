from __future__ import annotations

import json
from pathlib import Path

from scripts.tools.create_brain2_master_validation_run_report import (
    DayArtifacts,
    build_brain2_master_validation_report,
)


def test_build_brain2_master_validation_report_includes_board_and_tracker_anchors(tmp_path: Path) -> None:
    repo_root = tmp_path
    template_path = repo_root / "template.md"
    template_path.write_text("# Template\n", encoding="utf-8")

    runs_dir = repo_root / "runs"
    control_center_dir = repo_root / "sharepacks" / "2026-01-05" / "control_center"
    control_center_dir.mkdir(parents=True, exist_ok=True)

    sandbox_json = repo_root / "runs2" / "2026-01-05__TRANSLATION_SANDBOX_SEED__analysis_arena_day_review.json"
    sandbox_json.parent.mkdir(parents=True, exist_ok=True)
    seed_json = repo_root / "sharepacks" / "_predictive" / "2026-01-05" / "NewYork4" / "analysis" / "translation_sandbox_seed__tool_only__arena_v0.json"
    seed_json.parent.mkdir(parents=True, exist_ok=True)
    seed_json.write_text(
        json.dumps(
            {
                "brain2_context": {
                    "positional_shortlist_top": [{"canonical": "345"}],
                    "blackapple_recommended_canonicals": ["455"],
                    "profit_alert_implied_canonicals": ["178"],
                    "due_double_example_canonicals": ["055"],
                },
                "control_arm": {"preserved_not_budgeted_canonicals_top": ["178"]},
                "sandbox_hypotheses": {
                    "diagnostic_boxed_seed": [{"value": "455"}],
                    "diagnostic_straight_seed": [{"value": "178"}],
                    "diagnostic_vt_box_seed": [{"value": "05"}],
                },
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    sandbox_json.write_text(
        json.dumps(
            {
                "state_receipts": [
                    {
                        "state_key": "NewYork4",
                        "seed_json": "sharepacks/_predictive/2026-01-05/NewYork4/analysis/translation_sandbox_seed__tool_only__arena_v0.json",
                    }
                ]
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    artifacts = DayArtifacts(
        bundle_md=repo_root / "runs2" / "bundle.md",
        bundle_json=repo_root / "runs2" / "bundle.json",
        scoreboard_md=repo_root / "runs2" / "scoreboard.md",
        scoreboard_json=repo_root / "runs2" / "scoreboard.json",
        overlay_md=repo_root / "runs2" / "overlay.md",
        overlay_json=repo_root / "runs2" / "overlay.json",
        shadow_md=repo_root / "runs2" / "shadow.md",
        shadow_json=repo_root / "runs2" / "shadow.json",
        sandbox_md=repo_root / "runs2" / "sandbox.md",
        sandbox_json=sandbox_json,
    )

    report = build_brain2_master_validation_report(
        results_date="2026-01-05",
        history_date="2026-01-04",
        artifacts=artifacts,
        template_path=template_path,
        board_scope_states=["NewYork4", "Florida4"],
        scoreboard_rows=[
            {
                "score_rank": 1,
                "state_key": "NewYork4",
                "role": "shared_host",
                "targeting_bucket": "tight_core",
                "tracker_posture": "tracker-strong",
                "top_canonicals": ["455", "178"],
            },
            {
                "score_rank": 2,
                "state_key": "Florida4",
                "role": "echo",
                "targeting_bucket": "watch_only",
                "tracker_posture": "tracker-mixed",
                "top_canonicals": ["994"],
            },
        ],
        board_verdict={
            "top_primary_target": "NewYork4",
            "secondary_target": "Florida4",
            "best_clean_host": "NewYork4",
            "highest_context_support_state": "NewYork4",
            "tight_core_states": ["NewYork4"],
            "watch_only_states": ["Florida4"],
            "small_shoulder_states": [],
            "direct_cross_state_receipts": ["pair echo"],
            "best_relationship_source": "duplicate pair",
        },
        duplicate_pairs=[
            {"state_a": "NewYork4", "state_b": "Florida4", "pair_score": 4, "relationship_types": ["pair_echo"]}
        ],
        shadow_verdict={
            "play_states": ["NewYork4"],
            "watch_states": ["Florida4"],
            "skip_states": [],
            "top_play_state": "NewYork4",
            "top_watch_state": "Florida4",
        },
        state_decisions=[
            {"state_key": "NewYork4", "reason_codes": ["R_CONSENSUS_PRESENT", "LAST_REMAINING"]},
            {"state_key": "Florida4", "reason_codes": ["R_CONSENSUS_PRESENT"]},
        ],
        profit_alert_rows=[
            {"StateKey": "Florida4", "AlertId": "A03", "Strength": "3", "Suggested": "BOX"},
            {"StateKey": "Florida4", "AlertId": "A04", "Strength": "4", "Suggested": "BOX"},
        ],
        compound_rows=[
            {"state_key": "Florida4", "variant": "Combined", "top_event": "STRAIGHT_GATE", "priority": "80", "candidate_alert_ids": "A03,A04"}
        ],
        blackapple_rows=[
            {"StateKey": "NewYork4", "Variant": "Evening", "Status": "ALERT", "BA-Score": "3", "Examples": "016 025 349"},
            {"StateKey": "Florida4", "Variant": "Combined", "Status": "WATCH", "BA-Score": "2", "Examples": "014 023 149"},
        ],
        due_rows=[
            {
                "StateKey": "NewYork4",
                "Variant": "Combined",
                "Draws Since Double": "5",
                "Winner Midday": "080",
                "Winner Evening": "735",
                "Midday Winner In Family": "False",
                "Evening Winner In Family": "False",
            },
            {
                "StateKey": "Florida4",
                "Variant": "Combined",
                "Draws Since Double": "3",
                "Winner Midday": "080",
                "Winner Evening": "994",
                "Midday Winner In Family": "False",
                "Evening Winner In Family": "True",
            },
        ],
        tracker_rows=[
            {"StateKey": "Florida4", "Variant": "Evening", "Current Index": "24", "Current==WinnerVTRAC": "True"}
        ],
        translation_learning={
            "boxed": ["`455` x1"],
            "straight": ["`178` x1"],
            "vt_box": ["`05` x1"],
            "positional": ["`345` x1"],
            "blackapple": ["`455` x1"],
            "profit": ["`178` x1"],
            "due": ["`055` x1"],
            "preserved": ["`178` x1"],
        },
        control_center_dir=control_center_dir,
        control_arm_runs_dir=runs_dir,
        doubles_inventory_md=repo_root / "runs2" / "doubles.md",
        doubles_inventory_csv=repo_root / "runs2" / "doubles.csv",
    )

    assert "Brain 2 Master Validation Run Report" in report
    assert "`NewYork4`" in report
    assert "daily doubles / mirror doubles on the day" in report
    assert "Florida4" in report
    assert "strongest boxed themes" in report
    assert "Candidate Universe" not in report  # report is section-driven, not raw template dump
    assert "candidate-universe grade" in report
