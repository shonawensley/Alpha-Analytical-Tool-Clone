from __future__ import annotations

import sys
from pathlib import Path


def test_inventory_uses_results_and_active_sharepacks_only(tmp_path, monkeypatch) -> None:
    from scripts.tools import create_doubles_mirror_doubles_inventory as mod

    monkeypatch.setattr(mod, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(mod, "RUNS_DIR", tmp_path / "runs")
    monkeypatch.setattr(mod, "RESULTS_DIR", tmp_path / "data" / "results")

    results_root = tmp_path / "data" / "results"
    results_root.mkdir(parents=True, exist_ok=True)
    (results_root / "2026-01-05.txt").write_text(
        "State\tPick 3\n"
        "Midday\tEvening\n"
        "New York\t080\t735\n"
        "Texas\t958\t572\n",
        encoding="utf-8",
    )

    predictive_root = tmp_path / "sharepacks" / "_predictive" / "2026-01-05" / "NewYork4"
    predictive_root.mkdir(parents=True, exist_ok=True)
    truth_root = tmp_path / "sharepacks" / "2026-01-05" / "NewYork4"
    (truth_root / "winners" / "NewYork4").mkdir(parents=True, exist_ok=True)
    (truth_root / "aux" / "draws").mkdir(parents=True, exist_ok=True)
    (truth_root / "control_center").mkdir(parents=True, exist_ok=True)
    (tmp_path / "sharepacks" / "2026-01-05" / "control_center").mkdir(parents=True, exist_ok=True)
    (tmp_path / "sharepacks" / "2026-01-05" / "control_center" / "due_doubles.csv").write_text(
        "StateKey,Variant,Draws Since Double,Family 1,Midday Winner In Family,Evening Winner In Family\n"
        "NewYork4,Midday,5,0/5:demo,1,\n"
        "NewYork4,Evening,2,1/6:demo,,0\n",
        encoding="utf-8",
    )

    runs_dir = tmp_path / "runs"
    runs_dir.mkdir(parents=True, exist_ok=True)
    (runs_dir / "2026-01-05__CANDIDATE_UNIVERSE_GRADE.csv").write_text(
        "state_key,winner_label,hit_any,box_hit,vtrac_index_hit,method_id,cost_units,combos_count,pack_id\n"
        "NewYork4,Midday,1,1,1,union,1,12,packA\n",
        encoding="utf-8",
    )
    (runs_dir / "2026-01-05__PLAY_CARD_GRADE.csv").write_text(
        "state_key,winner_label,hit_any,box_hit,vtrac_index_hit\n"
        "NewYork4,Midday,1,1,0\n",
        encoding="utf-8",
    )

    report_dir = tmp_path / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / "2026-01-05__NewYork4.md").write_text("# report\n", encoding="utf-8")

    out_md = tmp_path / "out" / "inventory.md"
    out_csv = tmp_path / "out" / "inventory.csv"
    out_deep = tmp_path / "out" / "deep.md"
    out_queue = tmp_path / "out" / "queue.md"

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "create_doubles_mirror_doubles_inventory.py",
            "--from-date",
            "2026-01-05",
            "--to-date",
            "2026-01-05",
            "--runs-dir",
            str(runs_dir),
            "--grades-runs-dir",
            str(runs_dir),
            "--results-root",
            str(results_root),
            "--predictive-sharepacks-root",
            str(tmp_path / "sharepacks" / "_predictive"),
            "--truth-sharepacks-root",
            str(tmp_path / "sharepacks"),
            "--run-report-dir",
            str(report_dir),
            "--out-md",
            str(out_md),
            "--out-csv",
            str(out_csv),
            "--out-deep-dive",
            str(out_deep),
            "--out-study-queue",
            str(out_queue),
        ],
    )

    mod.main()

    text = out_md.read_text(encoding="utf-8")
    assert "Event source: `data/results`" in text
    assert "corpus_summary.csv" not in text
    assert "2026-01-05__NewYork4.md" in text
    assert "Texas4" not in text
    assert "NewYork4" in text
