import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd
import pytest

from alpha_analytical.control_center import batch_runner
from alpha_analytical.digit_reduction.analyzer_v2.types import Item, Key, Step


def _make_entry(state: str, midday: str = "123", evening: str = "456") -> batch_runner.ParsedWinnerEntry:
    return batch_runner.ParsedWinnerEntry(
        label=state,
        canonical=state,
        project_state=state,
        midday=midday,
        evening=evening,
        raw_digits=(midday, evening),
    )


def test_run_digit_reduction_workflow_happy(tmp_path, monkeypatch):
    tables_root = tmp_path / "tables"
    analysis_root = tmp_path / "analysis"
    state = "TestState"
    (tables_root / state).mkdir(parents=True)
    (analysis_root / "digit_reduction" / state).mkdir(parents=True)

    monkeypatch.setattr(batch_runner.ph, "get_tables_output_dir", lambda: str(tables_root))

    def fake_get_analysis_dir(kind: str, selected: str) -> str:
        target = analysis_root / kind / selected
        target.mkdir(parents=True, exist_ok=True)
        return str(target)

    monkeypatch.setattr(batch_runner.ph, "get_analysis_dir", fake_get_analysis_dir)
    monkeypatch.setattr(batch_runner.ph, "get_analysis_output_dir", lambda: str(analysis_root))

    from core import module_b_digit_reduction as reducer_mod

    def fake_reducer(run_state, tables_path, out_path):
        out_path.mkdir(parents=True, exist_ok=True)
        html_path = out_path / f"{run_state}_digit_reduction_report.html"
        csv_path = out_path / f"{run_state}_digit_reduction_scores.csv"
        html_path.write_text("html", encoding="utf-8")
        csv_path.write_text("csv", encoding="utf-8")
        df = pd.DataFrame({"state": [run_state]})
        return df, str(html_path), str(csv_path)

    monkeypatch.setattr(reducer_mod, "run_digit_reduction", fake_reducer)

    import alpha_analytical.digit_reduction.analyzer_v2 as analyzer_pkg

    def fake_analyzer(run_state, analysis_root):
        analyzer_dir = Path(analysis_root) / "digit_reduction" / run_state / "analyzer_v2"
        analyzer_dir.mkdir(parents=True, exist_ok=True)
        (analyzer_dir / f"{run_state}_analyzer_v2_per_item.csv").write_text("per", encoding="utf-8")
        (analyzer_dir / f"{run_state}_analyzer_v2_top_candidates.csv").write_text("top", encoding="utf-8")
        return {"rows": 2}

    monkeypatch.setattr(analyzer_pkg, "run", fake_analyzer)

    import alpha_analytical.digit_reduction.analyzer_v2.winners_overlay as overlay_mod

    def fake_overlay(run_state, winners, *, analysis_root, when=None, mirror_to_winners=True):
        winners_dir = Path(analysis_root) / "digit_reduction" / run_state / "analyzer_v2" / "winners"
        winners_dir.mkdir(parents=True, exist_ok=True)
        overlay_path = winners_dir / f"{when or 'STAMP'}_Combined_winner_overlay.html"
        flags_path = winners_dir / f"{when or 'STAMP'}_Combined_winner_flags.csv"
        overlay_path.write_text("overlay", encoding="utf-8")
        flags_path.write_text("flags", encoding="utf-8")
        return {
            "state": run_state,
            "stamp": when or "STAMP",
            "results": {
                "Combined": {
                    "winner": winners.get("Combined"),
                    "hits": 1,
                    "overlay_html": str(overlay_path),
                    "flags_csv": str(flags_path),
                }
            },
        }

    monkeypatch.setattr(overlay_mod, "run_winner_overlay_batch", fake_overlay)

    import alpha_analytical.digit_reduction.analyzer_v2.training_bundle as bundle_mod

    def fake_package(state_name, *, stamp=None, analysis_root, include_overlay=False, include_hits=True, make_zip=False):
        bundle_dir = Path(analysis_root) / "digit_reduction" / state_name / "training_sets" / (stamp or "LATEST")
        bundle_dir.mkdir(parents=True, exist_ok=True)
        return {"bundle_dir": str(bundle_dir), "zip_path": None, "stamp": stamp or "LATEST"}

    monkeypatch.setattr(bundle_mod, "package_training_bundle", fake_package)

    entry = _make_entry(state)
    results = batch_runner.run_digit_reduction_workflow(
        [entry],
        run_reducer=True,
        run_overlay=True,
        run_analyzer=True,
        run_bundle=True,
        bundle_stamp="20250101",
        mirror_to_winners=True,
        include_overlay_html=True,
        include_hits=True,
        make_zip=False,
    )

    assert len(results) == 1
    record = results[0]
    assert record["state"] == state
    assert record["winners"].get("Combined") == "123"
    assert record["reducer"].get("rows") == 1
    assert record["overlay"].get("stamp") == "20250101"
    assert record["analyzer"].get("rows") == 2
    assert record["bundle"].get("bundle_dir")


def test_run_digit_reduction_workflow_missing_tables(tmp_path, monkeypatch):
    tables_root = tmp_path / "tables"
    analysis_root = tmp_path / "analysis"

    monkeypatch.setattr(batch_runner.ph, "get_tables_output_dir", lambda: str(tables_root))
    monkeypatch.setattr(batch_runner.ph, "get_analysis_output_dir", lambda: str(analysis_root))
    monkeypatch.setattr(batch_runner.ph, "get_analysis_dir", lambda kind, state: str(analysis_root / kind / state))

    entry = _make_entry("MissingState")
    results = batch_runner.run_digit_reduction_workflow([entry], run_reducer=True, run_overlay=True, run_analyzer=True)
    record = results[0]
    assert "Missing tables" in record["reducer"].get("error", "")
    assert record["overlay"].get("skipped") == "reducer failed"
    assert record["analyzer"].get("skipped") == "reducer failed"


def test_own_vs_combined_handles_empty_core():
    from alpha_analytical.digit_reduction.analyzer_v2 import pivot

    key_base = Key(
        state="Test",
        area="LS1",
        section="Combined",
        set="Set1",
        draw="Draw1",
        col=7,
        method="A",
        mode="own",
    )
    steps = [Step(step=0, value="123456", length=6, unique_digits=6, is_3value=False)]
    item_own = Item(
        key=key_base,
        grid_position={},
        sequence_meta={},
        steps=steps,
        final={"value": ""},
    )
    key_combined = Key(**{**key_base.__dict__, "mode": "combined"})
    item_combined = Item(
        key=key_combined,
        grid_position={},
        sequence_meta={},
        steps=steps,
        final={"value": ""},
    )

    features, delta_rows = pivot.own_vs_combined([item_own, item_combined])
    assert delta_rows[0]["mode.agree_core"] == 0
    for payload in features.values():
        assert payload["mode.agree_core"] == 0
