from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

FIXTURE_DIR = Path(__file__).resolve().parents[1] / "fixtures" / "stable_mini"


def test_stable_fixture_has_expected_winner_flags() -> None:
    metrics = json.loads((FIXTURE_DIR / "StableMini_metrics.json").read_text())
    compound = pd.read_csv(FIXTURE_DIR / "StableMini_stable_patterns_compound.csv")

    assert metrics["winners"] == ["733", "271"]
    assert metrics["best_compound_rank"]["733"] == 1
    assert metrics["best_compound_rank"]["271"] == 2

    hits = metrics["winner_hits"]
    assert hits["733"]["exact_straight"] is True
    assert hits["271"]["exact_straight"] is False
    assert hits["271"]["exact_boxed"] is True

    health = metrics["health"]
    assert health["compound_rows"] == len(compound)
    assert health["vt_only_lane"] == int(compound["vt_only_lane"].astype(bool).sum())
    assert health["funnel_precol1"] == int((compound["funnel_precol1"].astype(float) > 0).sum())

    row_337 = compound.loc[compound["Canonical"] == 337].iloc[0]
    assert row_337["funnel_precol1"] == 1
    row_127 = compound.loc[compound["Canonical"] == 127].iloc[0]
    assert bool(row_127["vt_only_lane"]) is True


def test_spotlight_fixture_captures_literal_winners() -> None:
    spotlight_raw = pd.read_csv(FIXTURE_DIR / "StableMini_winner_family_spotlight_raw.csv")
    spotlight_fam = pd.read_csv(FIXTURE_DIR / "StableMini_winner_family_spotlight_families.csv")

    for df in (spotlight_raw, spotlight_fam):
        assert "winner_literal_midday" in df
        assert "winner_literal_evening" in df
        assert str(df["winner_literal_midday"].iloc[0]) == "733"
        assert str(df["winner_literal_evening"].iloc[0]) == "271"
        assert df["is_exact_boxed"].astype(bool).all()
        assert df["is_vtrac_boxed"].astype(bool).all()
