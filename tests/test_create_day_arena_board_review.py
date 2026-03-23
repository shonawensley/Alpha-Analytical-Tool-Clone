from __future__ import annotations

import csv
import json
from pathlib import Path

from scripts.tools.create_day_arena_board_review import run_day_arena_board_review


def _write_csv(path: Path, rows, fieldnames) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _arena_fixture(state_key: str, canonical: str, vtrac_index: str) -> dict:
    return {
        "schema_version": "aggregated_analysis_arena_v0",
        "metadata": {"state_key": state_key, "results_date": "2026-03-21"},
        "arena_synthesis": {
            "dominant_canonicals": [{"value": canonical}],
            "dominant_vtrac_indices": [{"value": vtrac_index}],
            "dominant_families": [{"value": canonical}],
            "vtrac_literal_watchlist": [{"vtrac_index": vtrac_index, "candidate_canonicals": [canonical]}],
            "context_reinforced_canonicals": [{"value": canonical}],
            "context_only_pressure": [],
            "state_regime": {
                "dominant_canonical": canonical,
                "dominant_vtrac_index": vtrac_index,
                "dominant_family": canonical,
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
                                "canonical": canonical,
                                "strength": 4,
                                "badges": ["PERSIST"],
                                "suggested": "BOX",
                                "implied_set_size": 6,
                                "decay_draws": 4,
                            }
                        ]
                    },
                    "aux_blackapple_context": {
                        "recommended_canonicals_top": [canonical],
                        "control_center_top": [
                            {
                                "variant": "Combined",
                                "status": "WATCH",
                                "ba_score": 2,
                                "candidate_count": 4,
                                "examples": [canonical],
                                "triggers": "Pairs 1",
                            }
                        ],
                    },
                    "aux_positional_pressure": {
                        "signal_notes_top": ["Mirror-Echo active"],
                        "shortlist_top": [
                            {
                                "combo": canonical,
                                "canonical": canonical,
                                "score": 44.2,
                                "tags": ["Mirror-Echo"],
                                "vtrac_index": vtrac_index,
                            }
                        ],
                    },
                    "aux_due_doubles_family_pressure": {
                        "available": True,
                        "top_example_canonicals": [canonical],
                        "by_variant": {
                            "Combined": {
                                "draws_since_double": 12,
                                "families": [{"family": "0/5-4/9", "slot": "Family 1", "examples": [canonical]}],
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


def test_run_day_arena_board_review_orchestrates_arenas_and_bundle(tmp_path: Path, monkeypatch) -> None:
    repo_root = tmp_path
    sharepacks_root = repo_root / "sharepacks" / "_predictive"
    day_dir = sharepacks_root / "2026-03-21"
    (day_dir / "NewJersey4").mkdir(parents=True, exist_ok=True)
    (day_dir / "Virginia4").mkdir(parents=True, exist_ok=True)

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

    def fake_build_aggregated_analysis_arena_payload(*, state_key: str, **_: object) -> dict:
        if state_key == "NewJersey4":
            return _arena_fixture(state_key, "055", "1")
        return _arena_fixture(state_key, "049", "15")

    def fake_write_aggregated_analysis_arena_files(*, out_json_path: Path, payload: dict, write_md: bool = True):
        out_json_path.parent.mkdir(parents=True, exist_ok=True)
        out_json_path.write_text(json.dumps(payload), encoding="utf-8")
        md_path = None
        if write_md:
            md_path = out_json_path.with_suffix(".md")
            md_path.write_text("# stub\n", encoding="utf-8")
        return out_json_path, md_path

    monkeypatch.setattr(
        "scripts.tools.create_day_arena_board_review.build_aggregated_analysis_arena_payload",
        fake_build_aggregated_analysis_arena_payload,
    )
    monkeypatch.setattr(
        "scripts.tools.create_day_arena_board_review.write_aggregated_analysis_arena_files",
        fake_write_aggregated_analysis_arena_files,
    )

    receipt = run_day_arena_board_review(
        sharepacks_root=sharepacks_root,
        results_date="2026-03-21",
        states=["NewJersey4", "Virginia4"],
        profile="tool_only",
        experiment_tag="arena_v0",
        history_date=None,
        board_name="Competition 8",
        midday_results_path=midday_path,
        arena_top_items=12,
        board_top_items=8,
        out_dir=repo_root / "runs",
        rebuild_arenas=True,
    )

    assert len(receipt["arena_paths"]) == 2
    assert (repo_root / receipt["bundle_md"]).exists()
    assert (repo_root / receipt["overlay_json"]).exists()
    assert (repo_root / receipt["scoreboard_md"]).exists()

    bundle_json = repo_root / str(receipt["bundle_json"])
    payload = json.loads(bundle_json.read_text(encoding="utf-8"))
    assert payload["workflow_manifest"]["brain1_runtime_entrypoint"].endswith("build_aggregated_analysis_arena.py")
    assert payload["board_verdict"]["top_primary_target"]
