from __future__ import annotations

import json
import sys
from pathlib import Path


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: object) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _seed_window(tmp_path: Path) -> Path:
    window_root = tmp_path / "runs2" / "WINDOW_2026-01-05_to_2026-01-05"
    analysis_dir = window_root / "ANALYSIS_ARENA"
    validation_dir = window_root / "VALIDATION"

    _write_text(
        tmp_path / "data" / "results" / "2026-01-05.txt",
        "State\tPick 3\nMidday\tEvening\nNew York\t080\t735\n",
    )

    _write_json(
        analysis_dir / "2026-01-05__BOARD_SCOREBOARD__analysis_arena_day_review.json",
        {
            "metadata": {
                "profile": "tool_only",
                "experiment_tag": "arena_v0",
            },
            "board_verdict": {
                "top_primary_target": "NewYork4",
                "secondary_target": "NewYork4",
                "best_clean_host": "NewYork4",
                "highest_context_support_state": "NewYork4",
            },
            "scoreboard_rows": [
                {
                    "state_key": "NewYork4",
                    "score_rank": 1,
                    "priority_score": 98.4,
                    "role": "shared_host",
                    "targeting_bucket": "tight_core",
                    "tracker_posture": "tracker-rich",
                    "top_canonicals": ["008", "357"],
                    "top_vtrac_indices": ["6", "24"],
                    "profit_alert_hint": "A05",
                    "compound_event_hint": "ENGINE_GOV",
                    "due_double_hint": "0/5-1/6",
                    "blackapple_reco_hint": "008",
                    "positional_hint": "008",
                    "r_consensus_hint": "tail 08",
                    "survivor_hint": "frontier 008",
                }
            ],
        },
    )
    _write_json(
        analysis_dir / "2026-01-05__SHADOW_DECISION_POLICY__analysis_arena_day_review.json",
        {
            "state_decisions": [
                {
                    "state_key": "NewYork4",
                    "posture": "PLAY",
                    "mode": "BOX_FIRST",
                    "cap_class": "B24",
                    "translator_route": "shadow_only",
                    "reason_codes": ["CONSENSUS_EVENT", "DUE_DOUBLE"],
                }
            ]
        },
    )

    seed_rel = Path("sharepacks/_predictive/2026-01-05/NewYork4/analysis/translation_sandbox_seed__tool_only__arena_v0.json")
    _write_json(
        analysis_dir / "2026-01-05__TRANSLATION_SANDBOX_SEED__analysis_arena_day_review.json",
        {
            "state_receipts": [
                {
                    "state_key": "NewYork4",
                    "score_rank": 1,
                    "priority_score": 98.4,
                    "role": "shared_host",
                    "posture": "PLAY",
                    "mode": "BOX_FIRST",
                    "seed_json": str(seed_rel),
                    "seed_md": str(seed_rel).replace(".json", ".md"),
                }
            ]
        },
    )

    _write_json(
        tmp_path / seed_rel,
        {
            "brain1_core": {
                "dominant_canonicals": ["008", "357"],
                "context_reinforced_canonicals": ["008", "357"],
                "dominant_vtrac_indices": ["6", "24"],
            },
            "control_arm": {
                "candidate_universe": {
                    "path": "sharepacks/_predictive/2026-01-05/NewYork4/candidate_universe__tool_only__arena_v0.json"
                },
                "play_card": {
                    "path": "sharepacks/_predictive/2026-01-05/NewYork4/play_card__tool_only__arena_v0.json"
                },
                "preserved_not_budgeted_canonicals_top": ["008", "357"],
            },
            "sandbox_hypotheses": {
                "diagnostic_boxed_seed": [{"value": "008"}, {"value": "357"}],
                "diagnostic_straight_seed": [{"value": "080"}, {"value": "735"}],
                "diagnostic_vt_box_seed": [{"value": "6"}, {"value": "24"}],
            },
        },
    )
    _write_json(
        tmp_path / "sharepacks/_predictive/2026-01-05/NewYork4/candidate_universe__tool_only__arena_v0.json",
        {"union_combos": ["080", "735", "357"], "packs": []},
    )
    _write_json(
        tmp_path / "sharepacks/_predictive/2026-01-05/NewYork4/play_card__tool_only__arena_v0.json",
        {
            "strategies": {
                "analysis_prefix": {
                    "B12": {"combos": ["080"], "boxed_canonicals": ["008"]},
                    "B24": {"combos": ["080", "735"], "boxed_canonicals": ["008", "357"]},
                    "B36": {"combos": ["080", "735"], "boxed_canonicals": ["008", "357"]},
                }
            }
        },
    )

    _write_text(
        validation_dir / "2026-01-05_to_2026-01-05__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv",
        "date,state,period,winner,type,has_mirror_pair,mirror_pairs\n"
        "2026-01-05,NewYork4,Midday,080,double,False,\n"
        "2026-01-05,NewYork4,Evening,735,mirror_double,True,2/7\n",
    )
    return window_root


def test_window_performance_gap_and_deep_analysis_reports(tmp_path, monkeypatch) -> None:
    from scripts.tools import analysis_arena_window_utils as util
    from scripts.tools import create_window_deep_analysis_report as deep
    from scripts.tools import create_window_performance_gap_report as gap

    window_root = _seed_window(tmp_path)

    monkeypatch.setattr(util, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(gap, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(gap, "UTILS_REPO_ROOT", tmp_path)
    monkeypatch.setattr(gap, "DEFAULT_RESULTS_ROOT", tmp_path / "data" / "results")
    monkeypatch.setattr(deep, "REPO_ROOT", tmp_path)

    perf_md = window_root / "gap.md"
    perf_json = window_root / "gap.json"
    perf_ledger = window_root / "gap.csv"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "create_window_performance_gap_report.py",
            "--window-root",
            str(window_root),
            "--results-root",
            str(tmp_path / "data" / "results"),
            "--out-md",
            str(perf_md),
            "--out-json",
            str(perf_json),
            "--out-ledger",
            str(perf_ledger),
            "--force",
        ],
    )
    gap.main()

    perf_payload = json.loads(perf_json.read_text(encoding="utf-8"))
    assert perf_payload["summary_counts"]["winner_events"] == 2
    assert perf_payload["summary_counts"]["winner_on_board"] == 2
    assert perf_payload["summary_counts"]["play_card_any_box"] == 2
    assert perf_payload["summary_counts"]["cu_exact"] == 2
    assert "Arena Intrinsic Quality" in perf_md.read_text(encoding="utf-8")

    deep_md = window_root / "deep.md"
    deep_json = window_root / "deep.json"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "create_window_deep_analysis_report.py",
            "--window-root",
            str(window_root),
            "--performance-gap-json",
            str(perf_json),
            "--out-md",
            str(deep_md),
            "--out-json",
            str(deep_json),
            "--force",
        ],
    )
    deep.main()

    deep_payload = json.loads(deep_json.read_text(encoding="utf-8"))
    assert deep_payload["window_overview"]["winner_events"] == 2
    assert deep_payload["tracker_families"]["doubles_result_types"]["double"] == 1
    assert "Shared Complexes / Carryover / Decay" in deep_md.read_text(encoding="utf-8")
