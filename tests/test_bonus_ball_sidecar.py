from __future__ import annotations

import json
import sys
import textwrap
from pathlib import Path

from alpha_analytical.control_center.bonus_ball_sidecar import (
    apply_bonus_ball_parity,
    build_bonus_ball_truth_payload,
    parse_bonus_ball_source,
)


CORE_RESULTS = textwrap.dedent(
    """\
    State\tPick 3
    Midday\tEvening
    Connecticut\t073\t922
    Florida\t700\t194
    Puerto Rico\t907\t321
    """
)


BONUS_RESULTS = textwrap.dedent(
    """\
    :
    Both Midday and Evening Results
    Game\tDraw Date\tResults
    Connecticut
    Play 3 Day\tWed, Mar 11, 2026\t0-7-3, Wild Ball: 1
    Play 3 Night\tWed, Mar 11, 2026\t9-2-2
    Delaware
    Play 3 Day\tWed, Mar 11, 2026\t5-2-6
    Florida
    Pick 3 Midday\tWed, Mar 11, 2026\t7-0-1, Fireball: 2
    Pick 3 Evening\tWed, Mar 11, 2026\t1-9-4, Fireball: 2
    Puerto Rico
    Pega 3 Tarde\tWed, Mar 11, 2026\t9-0-7, Wild Ball: 4
    Pega 3 Noche\tWed, Mar 11, 2026\t3-2-1, Wild Ball: 1
    """
)


def test_parse_bonus_ball_source_filters_to_supported_bonus_states() -> None:
    rows = parse_bonus_ball_source(BONUS_RESULTS)

    assert [(row.canonical, row.slot, row.sidecar_draw, row.bonus_digit) for row in rows] == [
        ("Connecticut", "Midday", "073", "1"),
        ("Connecticut", "Evening", "922", None),
        ("Florida", "Midday", "701", "2"),
        ("Florida", "Evening", "194", "2"),
        ("Puerto Rico", None, "907", "4"),
        ("Puerto Rico", "Evening", "321", "1"),
    ]


def test_apply_bonus_ball_parity_uses_parity_gate_and_reason_codes() -> None:
    rows = apply_bonus_ball_parity(
        results_date="2026-03-11",
        core_results_text=CORE_RESULTS,
        bonus_results_text=BONUS_RESULTS,
    )

    by_key = {(row.project_state, row.game_label_raw): row for row in rows}

    assert by_key[("Connecticut4", "Play 3 Day")].status == "accepted"
    assert by_key[("Connecticut4", "Play 3 Day")].reason == "parity_match"

    assert by_key[("Connecticut4", "Play 3 Night")].status == "skipped"
    assert by_key[("Connecticut4", "Play 3 Night")].reason == "no_bonus_ball"

    assert by_key[("Florida4", "Pick 3 Midday")].status == "rejected"
    assert by_key[("Florida4", "Pick 3 Midday")].reason == "draw_mismatch"

    assert by_key[("Florida4", "Pick 3 Evening")].status == "accepted"
    assert by_key[("Florida4", "Pick 3 Evening")].bonus_label_raw == "Fireball"

    assert by_key[("PuertoRico4", "Pega 3 Tarde")].status == "rejected"
    assert by_key[("PuertoRico4", "Pega 3 Tarde")].reason == "unsupported_game_label"

    assert by_key[("PuertoRico4", "Pega 3 Noche")].status == "accepted"
    assert by_key[("PuertoRico4", "Pega 3 Noche")].bonus_label_raw == "Wild Ball"


def test_build_bonus_ball_truth_payload_summarizes_rows() -> None:
    payload = build_bonus_ball_truth_payload(
        results_date="2026-03-11",
        core_results_text=CORE_RESULTS,
        bonus_results_text=BONUS_RESULTS,
        core_results_path="data/results/2026-03-11.txt",
        bonus_results_path="data/results_bonus/2026-03-11.txt",
    )

    summary = payload["summary"]
    assert summary["rows_total"] == 6
    assert summary["accepted_rows"] == 3
    assert summary["rejected_rows"] == 2
    assert summary["skipped_rows"] == 1
    assert summary["accepted_by_bonus_label"] == {"Fireball": 1, "Wild Ball": 2}


def test_create_bonus_ball_truth_report_cli(tmp_path: Path, monkeypatch) -> None:
    from scripts.tools import create_bonus_ball_truth_report as report

    results_root = tmp_path / "data" / "results"
    bonus_root = tmp_path / "data" / "results_bonus"
    out_dir = tmp_path / "reports" / "stable" / "bonus_ball_by_date" / "2026-03-11"
    results_root.mkdir(parents=True)
    bonus_root.mkdir(parents=True)
    (results_root / "2026-03-11.txt").write_text(CORE_RESULTS, encoding="utf-8")
    (bonus_root / "2026-03-11.txt").write_text(BONUS_RESULTS, encoding="utf-8")

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "create_bonus_ball_truth_report.py",
            "--date",
            "2026-03-11",
            "--results-root",
            str(results_root),
            "--bonus-results-root",
            str(bonus_root),
            "--out-dir",
            str(out_dir),
            "--force",
        ],
    )

    report.main()

    out_json = out_dir / "bonus_ball_truth.json"
    out_csv = out_dir / "bonus_ball_truth.csv"
    out_md = out_dir / "bonus_ball_parity_audit.md"

    assert out_json.exists()
    assert out_csv.exists()
    assert out_md.exists()

    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert payload["summary"]["accepted_rows"] == 3
    assert "Bonus-Ball Parity Audit" in out_md.read_text(encoding="utf-8")
