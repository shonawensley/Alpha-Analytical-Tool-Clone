import csv
import json
from pathlib import Path
from typing import Dict

import pytest

from core.module_b_digit_reduction import run_digit_reduction
from alpha_analytical.digit_reduction.analyzer_v2 import io as analyzer_io
from alpha_analytical.digit_reduction.analyzer_v2 import run as run_analyzer
from alpha_analytical.digit_reduction.analyzer_v2.winners_overlay import run_winner_overlay_batch

pytestmark = [pytest.mark.acceptance]

STATE_CASES = ["Delaware4", "Florida4"]


def _fixture_tables(state: str) -> Path:
    path = (
        Path(__file__)
        .resolve()
        .parent
        .parent
        / "fixtures"
        / "acceptance"
        / "digit_reduction"
        / state
        / "tables"
    )
    if not path.exists():
        raise FileNotFoundError(f"Digit reduction fixtures missing for {state}: {path}")
    return path


def _run_reducer_and_analyzer(state: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Dict[str, object]:
    tables_path = _fixture_tables(state)

    analysis_root = tmp_path / "analysis"
    digit_root = analysis_root / "digit_reduction"
    out_path = digit_root / state

    df, html_path, csv_path = run_digit_reduction(
        state=state,
        tables_path=tables_path,
        out_path=out_path,
    )

    assert not df.empty, "Reducer should produce score dataframe"
    html_path = Path(html_path)
    csv_path = Path(csv_path)
    assert html_path.exists(), "HTML report should exist"
    assert csv_path.exists(), "Scores CSV should exist"

    monkeypatch.setattr(analyzer_io, "_prefer_path_handler", lambda: None)

    result = run_analyzer(state, analysis_root=digit_root)
    assert result.get("rows", 0) > 0, "Analyzer should emit per-item rows"

    analyzer_dir = digit_root / state / "analyzer_v2"
    top_csv = analyzer_dir / f"{state}_analyzer_v2_top_candidates.csv"
    per_item_csv = analyzer_dir / f"{state}_analyzer_v2_per_item.csv"
    assert top_csv.exists(), "Top candidates CSV should exist"
    assert per_item_csv.exists(), "Per-item CSV should exist"

    return {
        "state": state,
        "analysis_root": analysis_root,
        "digit_root": digit_root,
        "html_path": html_path,
        "scores_csv": csv_path,
        "top_csv": top_csv,
        "per_item_csv": per_item_csv,
        "result": result,
    }


@pytest.mark.parametrize("state", STATE_CASES)
def test_digit_reduction_pipeline(state: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    ctx = _run_reducer_and_analyzer(state, tmp_path, monkeypatch)
    assert ctx["result"].get("rows", 0) > 0
    assert ctx["top_csv"].exists()
    assert ctx["per_item_csv"].exists()


@pytest.mark.parametrize("state", STATE_CASES)
def test_digit_reduction_winner_overlay(state: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    ctx = _run_reducer_and_analyzer(state, tmp_path, monkeypatch)

    with ctx["top_csv"].open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        first_row = next(reader, None)

    assert first_row, "Analyzer top candidates should provide at least one entry"
    winner = first_row.get("final.canon3")
    assert winner, "Top candidate must include final.canon3"

    batch = run_winner_overlay_batch(
        state,
        {"Combined": winner},
        analysis_root=ctx["analysis_root"],
        when="TESTSTAMP",
        mirror_to_winners=False,
    )

    combined = batch["results"].get("Combined")
    assert combined, "Combined overlay result should be populated"

    artifacts = [
        Path(combined["overlay_html"]),
        Path(combined["map_json"]),
        Path(combined["hits_csv"]),
        Path(combined["flags_csv"]),
        Path(combined["stamp_json_analyzer"]),
    ]
    for artifact in artifacts:
        assert artifact.exists(), f"Expected artifact missing: {artifact}"

    stamp_payload = json.loads(Path(combined["stamp_json_analyzer"]).read_text(encoding="utf-8"))
    assert stamp_payload["winner"] == winner
    assert stamp_payload["variant"] == "Combined"
    assert stamp_payload["state"] == state
