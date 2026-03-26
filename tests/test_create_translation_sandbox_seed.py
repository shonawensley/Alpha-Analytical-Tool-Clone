from __future__ import annotations

import json
from pathlib import Path

from scripts.tools.create_translation_sandbox_seed import (
    build_translation_sandbox_state_markdown,
    run_translation_sandbox_seed,
)


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def test_run_translation_sandbox_seed_collects_state_learning_surfaces(tmp_path: Path) -> None:
    repo_root = tmp_path
    sharepacks_root = repo_root / "sharepacks" / "_predictive"
    day_dir = sharepacks_root / "2026-03-25"
    state_dir = day_dir / "NewJersey4"
    analysis_dir = state_dir / "analysis"
    analysis_dir.mkdir(parents=True, exist_ok=True)

    overlay_path = repo_root / "runs" / "overlay.json"
    scoreboard_path = repo_root / "runs" / "scoreboard.json"
    decision_path = repo_root / "runs" / "shadow_dpl.json"

    _write_json(
        overlay_path,
        {
            "metadata": {
                "board_name": "Analysis Arena Day Review",
                "results_date": "2026-03-25",
                "profile": "tool_only",
                "experiment_tag": "arena_v0",
            },
            "state_summaries": [
                {
                    "state_key": "NewJersey4",
                    "primary_canonicals": ["455", "055"],
                    "secondary_canonicals": ["049"],
                    "dominant_families": ["455"],
                    "primary_vtrac_indices": ["5", "1"],
                    "secondary_vtrac_indices": ["15"],
                    "watchlist_indices": ["5"],
                    "context_reinforced_canonicals": ["455"],
                    "survivor_frontier_canonicals": ["455"],
                    "survivor_last_remaining_canonicals": ["455"],
                    "survivor_frontier_vtrac_indices": ["5"],
                    "survivor_last_remaining_vtrac_indices": ["5"],
                    "survivor_terminal_profiles": ["multi_literal_mixed_family__winner_family_hidden"],
                    "r_consensus_context": {
                        "available": True,
                        "event_count": 2,
                        "trial_eligible": True,
                    },
                    "r_consensus_support_canonicals": ["455", "049"],
                    "r_consensus_support_vtrac_indices": ["5"],
                    "profit_alert_implied_canonicals": ["049", "055"],
                    "top_profit_alerts": [{"alert_id": "A04", "canonical": "049", "strength": 4, "suggested": "BOX"}],
                    "blackapple_statuses": [{"variant": "Combined", "status": "WATCH", "ba_score": 2}],
                    "blackapple_recommended_canonicals": ["455"],
                    "positional_signal_notes": ["Mirror-Echo active"],
                    "positional_shortlist_top": [
                        {"combo": "455", "canonical": "455", "vtrac_index": "5", "tags": ["Mirror-Echo"]},
                        {"combo": "049", "canonical": "049", "vtrac_index": "15", "tags": ["Bridge"]},
                    ],
                    "due_double_families": [{"variant": "Combined", "draws_since_double": 13, "families": [{"family": "0/5-4/9"}]}],
                    "due_double_example_canonicals": ["055"],
                    "compound_events_top": [{"variant": "Combined", "top_event": "profit_alert_cluster", "priority": 2}],
                    "state_regime": {
                        "dominant_canonical": "455",
                        "survivor_pressure": True,
                        "last_remaining": True,
                        "hidden_terminal_support": True,
                    },
                }
            ],
        },
    )

    _write_json(
        scoreboard_path,
        {
            "metadata": {"generated_from_overlay": "Analysis Arena Day Review", "results_date": "2026-03-25"},
            "scoreboard_rows": [
                {
                    "score_rank": 1,
                    "state_key": "NewJersey4",
                    "priority_score": 34,
                    "role": "shared_host",
                    "targeting_bucket": "tight_core",
                    "spent_status": "mostly_unspent",
                    "evening_bias": "still_live",
                    "tracker_posture": "tracker-strong",
                }
            ],
        },
    )

    _write_json(
        decision_path,
        {
            "metadata": {"results_date": "2026-03-25", "generated_from_overlay": "Analysis Arena Day Review"},
            "state_decisions": [
                {
                    "state_key": "NewJersey4",
                    "posture": "PLAY",
                    "mode": "boxed",
                    "cap_class": "medium",
                    "translator_route": "boxed",
                    "reason_codes": ["PLAY_STATE", "LAST_REMAINING", "R_CONSENSUS_PRESENT"],
                    "carryover_action": "new",
                }
            ],
        },
    )

    _write_json(
        state_dir / "candidate_universe__tool_only__arena_v0.json",
        {
            "union_combos_count": 18,
            "packs": [
                {
                    "pack_id": "stable_primary",
                    "method_id": "stable_primary",
                    "variant": "Combined",
                    "play_mode": "boxed",
                    "canonicals": ["455", "049"],
                    "combos_count": 12,
                    "cost_units": 12,
                    "why_tags": ["stable", "direct"],
                },
                {
                    "pack_id": "aux_due_double",
                    "method_id": "aux_due_double",
                    "variant": "Combined",
                    "play_mode": "boxed",
                    "canonicals": ["455"],
                    "combos_count": 6,
                    "cost_units": 6,
                    "why_tags": ["aux", "due_double"],
                },
            ],
        },
    )

    _write_json(
        state_dir / "play_card__tool_only__arena_v0.json",
        {
            "ranked_candidates": [
                {"combo": "455", "canonical": "455", "score": 9.1, "support_packs_count": 2, "support_methods": ["stable_primary"], "support_variants": ["Combined"]},
                {"combo": "554", "canonical": "455", "score": 8.5, "support_packs_count": 2, "support_methods": ["stable_primary"], "support_variants": ["Combined"]},
            ],
            "strategies": {
                "play_box_first": {
                    "B12": {
                        "boxed_canonicals": ["455"],
                        "combos_count": 12,
                    }
                }
            },
        },
    )

    receipt = run_translation_sandbox_seed(
        sharepacks_root=sharepacks_root,
        results_date="2026-03-25",
        profile="tool_only",
        experiment_tag="arena_v0",
        board_name="Analysis Arena Day Review",
        overlay_json_path=overlay_path,
        scoreboard_json_path=scoreboard_path,
        decision_policy_json_path=decision_path,
        runs_dir=repo_root / "runs",
        states=["NewJersey4"],
    )

    assert receipt["manifest_md"].endswith("__TRANSLATION_SANDBOX_SEED__analysis_arena_day_review.md")
    assert len(receipt["state_receipts"]) == 1

    seed_json = analysis_dir / "translation_sandbox_seed__tool_only__arena_v0.json"
    seed_md = analysis_dir / "translation_sandbox_seed__tool_only__arena_v0.md"
    assert seed_json.exists()
    assert seed_md.exists()

    payload = json.loads(seed_json.read_text(encoding="utf-8"))
    assert payload["brain1_core"]["dominant_canonicals"][0] == "455"
    assert payload["shadow_decision_policy"]["posture"] == "PLAY"
    assert payload["control_arm"]["candidate_universe"]["available"] is True
    assert payload["control_arm"]["play_card"]["available"] is True
    assert payload["control_arm"]["preserved_not_budgeted_canonicals_top"] == ["049"]

    boxed_seed = payload["sandbox_hypotheses"]["diagnostic_boxed_seed"]
    assert boxed_seed[0]["value"] == "455"
    assert "brain1.primary" in boxed_seed[0]["source_tags"]
    assert "control_arm.play_card" in boxed_seed[0]["source_tags"]

    markdown = build_translation_sandbox_state_markdown(payload)
    assert "Translation Sandbox Seed" in markdown
    assert "Diagnostic Boxed Seed" in markdown
    assert "Preserved-not-budgeted canonicals" in markdown
