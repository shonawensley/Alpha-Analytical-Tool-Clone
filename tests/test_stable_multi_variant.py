from pathlib import Path

import pandas as pd

from src.core.stable_pattern_extractor import run_stable_pattern_extraction


def _rows_for(set_name: str, draw_name: str, value: str) -> list[tuple[str, str, str, str]]:
    return [(set_name, draw_name, rowtype, value) for rowtype in ("R2", "R4", "R6", "R8")]


def _write_table(dest: Path, entries: list[tuple[str, str, str, str]]) -> None:
    columns = ["Set", "Draw", "RowType"] + [str(c) for c in range(7, 0, -1)]
    records = []
    for set_name, draw_name, rowtype, value in entries:
        record = {col: "" for col in columns}
        record.update({"Set": set_name, "Draw": draw_name, "RowType": rowtype, "7": value})
        records.append(record)
    df = pd.DataFrame(records)
    dest.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(dest, index=False)


def test_stable_extractor_reads_all_sections(tmp_path):
    state = "Connecticut4"
    tables_dir = tmp_path / "tables"

    combo_rows = _rows_for("Set1", "Draw1", "345")
    midday_rows = _rows_for("Set1", "Draw1", "**789")
    evening_rows = _rows_for("Set1", "Draw1", "112")

    _write_table(tables_dir / f"{state}_Combined_combined.csv", combo_rows)
    _write_table(tables_dir / f"{state}_Midday_combined.csv", midday_rows)
    _write_table(tables_dir / f"{state}_Evening_combined.csv", evening_rows)

    out_dir = tmp_path / "analysis"
    df, html_path, csv_path = run_stable_pattern_extraction(
        state=state,
        tables_path=tables_dir,
        out_path=out_dir,
        min_occ=1,
    )

    assert set(df["section"]) == {"Combined", "Midday", "Evening"}
    assert Path(html_path).exists()
    assert Path(csv_path).exists()

    combo = df[(df["section"] == "Combined") & (df["Canonical"] == "345")]
    assert not combo.empty and combo["cons_full"].iloc[0]

    midday = df[(df["section"] == "Midday") & (df["Canonical"] == "789")]
    assert not midday.empty and midday["hot"].iloc[0] == 2


def test_persistence_scores(tmp_path):
    state = "Delaware4"
    tables_dir = tmp_path / "tables"

    persistence_rows = []
    persistence_rows += _rows_for("Set3", "Draw1", "312")
    persistence_rows += _rows_for("Set2", "Draw1", "312")
    persistence_rows += _rows_for("Set1", "Draw1", "312")
    persistence_rows += _rows_for("Set1", "Draw2", "312")

    _write_table(tables_dir / f"{state}_Combined_combined.csv", persistence_rows)

    out_dir = tmp_path / "analysis"
    df, _, _ = run_stable_pattern_extraction(
        state=state,
        tables_path=tables_dir,
        out_path=out_dir,
        min_occ=1,
    )

    row = df[(df["section"] == "Combined") & (df["Canonical"] == "123")].iloc[0]
    assert row["persistence_set_count"] >= 3
    assert row["persistence_draw_run"] >= 2
    cfg_set_bonus = 2  # default in feature_config.yml
    cfg_draw_bonus = 1
    assert row["score_persistence_set"] == (row["persistence_set_count"] - 1) * cfg_set_bonus
    assert row["score_persistence_draw"] == (row["persistence_draw_run"] - 1) * cfg_draw_bonus


def test_double_mirror_bonus(tmp_path):
    state = "Georgia4"
    tables_dir = tmp_path / "tables"
    entries = _rows_for("Set1", "Draw1", "112")
    _write_table(tables_dir / f"{state}_Combined_combined.csv", entries)

    df, _, _ = run_stable_pattern_extraction(
        state=state,
        tables_path=tables_dir,
        out_path=tmp_path / "analysis",
        min_occ=1,
    )
    row = df[(df["section"] == "Combined") & (df["Canonical"] == "112")].iloc[0]
    assert row["double_mirror"]
    assert row["score_double_mirror"] > 0


def test_consensus_tail_bonus(tmp_path):
    state = "Virginia4"
    tables_dir = tmp_path / "tables"
    entries = _rows_for("Set1", "Draw1", "345")
    _write_table(tables_dir / f"{state}_Combined_combined.csv", entries)

    df, _, _ = run_stable_pattern_extraction(
        state=state,
        tables_path=tables_dir,
        out_path=tmp_path / "analysis",
        min_occ=1,
    )
    row = df[(df["section"] == "Combined") & (df["Canonical"] == "345")].iloc[0]
    assert "consensus_tail" in row["why"]
