from __future__ import annotations

import copy
import csv
import json
from pathlib import Path

from scripts.tools.audit_positional_aux_core import (
    CohortSpec,
    ProfileSpec,
    _draws_since_last_double,
    _target_vtrac_indices,
    run,
)
from scripts.tools.positional_aux_core import (
    build_lossless_report,
    grade_winner,
)


def _write_draws(path: Path, *, offset: int = 0) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for index in range(420):
        value = (
            ((index + offset) % 10) * 100
            + ((index * 3 + offset) % 10) * 10
            + ((index * 7 + offset) % 10)
        )
        rows.append(f"{value:03d}")
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["Draw"])
        writer.writerows([[value] for value in rows])


def _write_state_draws(draws_dir: Path, state: str = "Test") -> None:
    _write_draws(draws_dir / f"{state}_draws.csv", offset=0)
    _write_draws(draws_dir / f"{state}_Midday_draws.csv", offset=1)
    _write_draws(draws_dir / f"{state}_Evening_draws.csv", offset=2)


def test_lossless_report_preserves_full_native_fields(tmp_path: Path) -> None:
    draws_dir = tmp_path / "draws"
    _write_state_draws(draws_dir)

    payload = build_lossless_report(
        state_key="Test4",
        results_date="2026-01-01",
        draws_dir=draws_dir,
    )

    assert payload["metadata"]["winner_fields_present"] is False
    assert payload["metadata"]["source_is_frozen_pre_result"] is True
    assert set(payload["variants"]) == {"combined", "midday", "evening"}
    for variant in payload["variants"].values():
        for position in variant["positions"].values():
            assert len(position["top_digits"]) == 3
            assert {
                "gap_percentile",
                "score_components",
                "hard_due",
                "tags",
            }.issubset(position["top_digits"][0])
    assert payload["candidates"]
    assert {
        "native_ranks",
        "digital_root",
        "vtrac_index",
        "evidence",
        "source",
    }.issubset(payload["candidates"][0])


def test_grade_winner_separates_exact_box_vtrac_and_does_not_mutate() -> None:
    positions = {
        "0": {"top_digits": [{"digit": 1, "rank": 1}, {"digit": 6, "rank": 2}]},
        "1": {"top_digits": [{"digit": 2, "rank": 1}, {"digit": 7, "rank": 2}]},
        "2": {"top_digits": [{"digit": 3, "rank": 1}, {"digit": 8, "rank": 2}]},
    }
    payload = {
        "metadata": {"winner_fields_present": False},
        "variants": {
            variant: {"positions": copy.deepcopy(positions)}
            for variant in ("combined", "midday", "evening")
        },
        "candidates": [
            {
                "rank": 1,
                "combo": "321",
                "canonical": "123",
                "vtrac_index": 21,
            },
            {
                "rank": 2,
                "combo": "123",
                "canonical": "123",
                "vtrac_index": 21,
            },
        ],
    }
    original = copy.deepcopy(payload)

    grade = grade_winner(payload, period="Midday", winner="123")

    assert grade["target_variant_exact_position_count"] == 3
    assert grade["all_variant_same_position_exact_count"] == 3
    assert grade["shortlist_exact_rank"] == 2
    assert grade["shortlist_canonical_rank"] == 1
    assert grade["shortlist_vtrac_rank"] == 1
    assert grade["width_receipts"]["3"] == {
        "exact": True,
        "canonical_box": True,
        "vtrac_box": True,
    }
    assert "DIRECT_ORDERED" in grade["role_labels"]
    assert payload == original


def test_context_helpers_are_explicit(tmp_path: Path) -> None:
    summary = tmp_path / "summary.json"
    summary.write_text(
        json.dumps(
            {
                "vtrac": {
                    "overlay_top": {
                        "midday": [
                            {"index": 17, "draws_since": 100},
                            {"index": "9", "draws_since": 90},
                        ]
                    }
                }
            }
        ),
        encoding="utf-8",
    )

    assert _target_vtrac_indices(summary, "Midday") == [17, 9]
    assert _draws_since_last_double(["123", "456", "778", "111"]) == 2
    assert _draws_since_last_double(["123", "456"]) == 2


def test_harness_keeps_generation_and_winner_join_separate(tmp_path: Path) -> None:
    day_root = tmp_path / "replay"
    day_dir = day_root / "2026-01-01"
    draws_dir = day_dir / "Test4" / "aux" / "draws"
    _write_state_draws(draws_dir)
    summary_path = day_dir / "Test4" / "aux" / "Test4" / "summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(
        json.dumps({"vtrac": {"overlay_top": {"midday": []}}}),
        encoding="utf-8",
    )
    meta_path = day_dir / "control_center" / "meta.json"
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.write_text(
        json.dumps(
            {
                "results_date": "2026-01-01",
                "history_date": "2025-12-31",
            }
        ),
        encoding="utf-8",
    )
    winner_ledger = tmp_path / "winners.csv"
    with winner_ledger.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "event_id",
                "date",
                "state_key",
                "period",
                "winner",
                "pre_draw_available",
            ],
        )
        writer.writeheader()
        writer.writerow(
            {
                "event_id": "2026-01-01|Test4|Midday|123",
                "date": "2026-01-01",
                "state_key": "Test4",
                "period": "Midday",
                "winner": "123",
                "pre_draw_available": "True",
            }
        )
        writer.writerow(
            {
                "event_id": "2026-01-01|Test4|Midday|123",
                "date": "2026-01-01",
                "state_key": "Test4",
                "period": "Midday",
                "winner": "123",
                "pre_draw_available": "False",
            }
        )

    output_dir = tmp_path / "output"
    counts = run(
        cohorts=(
            CohortSpec(
                name="test",
                role="holdout",
                day_root=day_root,
                winner_ledger=winner_ledger,
            ),
        ),
        profiles=(
            ProfileSpec("native_all_variant", "static"),
            ProfileSpec(
                "forced_due_double_sensitivity",
                "forced_due_double",
            ),
        ),
        output_dir=output_dir,
    )

    assert counts["baseline_events"] == 1
    assert counts["profile_event_rows"] == 2
    feature_rows = list(
        csv.DictReader(
            (output_dir / "POSITIONAL_FEATURE_LEDGER.csv").open(
                encoding="utf-8",
                newline="",
            )
        )
    )
    assert feature_rows[0]["winner_join_phase"] == "post_result_grading"
    assert feature_rows[0]["source_is_frozen_pre_result"] == "True"
    assert feature_rows[0]["winner_ledger_row_count"] == "2"
    assert feature_rows[0]["winner_ledger_pre_draw_row_count"] == "1"
    assert feature_rows[0]["winner_ledger_post_result_row_count"] == "1"
    ablation_rows = list(
        csv.DictReader(
            (output_dir / "POSITIONAL_ABLATION_LEDGER.csv").open(
                encoding="utf-8",
                newline="",
            )
        )
    )
    forced_row = next(
        row
        for row in ablation_rows
        if row["profile"] == "forced_due_double_sensitivity"
    )
    assert forced_row["context_due_doubles_active"] == "True"
    manifest = json.loads((output_dir / "MANIFEST.json").read_text(encoding="utf-8"))
    assert manifest["runtime_mutation"] is False

    human_notes = output_dir / "HUMAN_NOTES.md"
    human_notes.write_text("preserve me\n", encoding="utf-8")
    rerun_counts = run(
        cohorts=(
            CohortSpec(
                name="test",
                role="holdout",
                day_root=day_root,
                winner_ledger=winner_ledger,
            ),
        ),
        profiles=(ProfileSpec("native_all_variant", "static"),),
        output_dir=output_dir,
        force=True,
    )
    assert rerun_counts["baseline_events"] == 1
    assert human_notes.read_text(encoding="utf-8") == "preserve me\n"
