from pathlib import Path

import pandas as pd
import pytest
import yaml

from alpha_analytical import stable
from alpha_analytical.stable.post_pass_families import build_family_summary
from alpha_analytical.stable.feature_config import CFG as STABLE_CFG  # type: ignore
from alpha_analytical.stable.training_bundle import write_training_bundle  # noqa: F401


REQUIRED_ROW_COLUMNS = {
    "score_cov",
    "score_hpr",
    "score_perm",
    "score_repeat",
    "score_straight",
    "score_single",
    "score_cons",
    "score_hot",
    "score_mirror",
    "score_dom",
    "score_len",
    "score_hidden",
    "score_vtrac_straight",
    "score_persistence_set",
    "score_persistence_draw",
    "score_double_mirror",
    "family_id",
    "hidden3v",
    "source_literals",
}

REQUIRED_FAMILY_COLUMNS = {
    "fam_cov",
    "fam_hpr",
    "fam_perm",
    "fam_repeat",
    "fam_cons",
    "fam_hot",
    "fam_straight2",
    "fam_straight3",
    "fam_doubles",
    "fam_vtrac",
    "fam_hidden",
    "fam_double_mirror",
    "fam_persistence",
    "fam_section_bonus",
    "fam_progression_bonus",
    "fam_last_remaining_bonus",
    "any_doubles_support",
    "any_vtrac_straight",
    "any_hidden3v",
    "max_persistence_set",
    "max_persistence_draw",
    "section_count",
    "progression_flag",
    "last_remaining_3v",
}

REQUIRED_YAML_KEYS = {
    "vertical_coverage_per_row",
    "horizontal_persistence_repeat_bonus",
    "baseline_straight_bonus",
    "baseline_boxed_bonus",
    "straight_2rows_bonus",
    "straight_3rows_bonus",
    "extra_digit_per_char",
    "single_left_bonus",
    "mirror_bonus",
    "consensus_full_bonus",
    "stub_consensus_score",
    "hot_level_1_bonus",
    "hot_level_2_bonus",
    "dominant_last_bonus",
    "dominant_pair_bonus",
    "dominant_double3_bonus",
    "min_score_to_highlight",
    "persistence_set_bonus",
    "persistence_draw_bonus",
    "vtrac_straight_bonus",
    "double_mirror_bonus",
    "consensus_tail_bonus",
    "perm_density_per_extra",
    "repeat_count_per_extra",
    "vtrac_family_presence",
    "cross_section_triple",
    "progression_across_sets",
    "last_remaining_3v_bonus",
    "consensus_family_bonus",
    "hotzone_family_bonus",
    "doubles_trigger_bonus",
    "hidden3v_bonus",
    "persistence_family_set_bonus",
    "persistence_family_draw_bonus",
    "compound.set_chain_bonus",
    "compound.draw_chain_bonus",
    "compound.col1_bonus",
    "compound.hot1_bonus",
    "compound.hot2_bonus",
    "compound.consensus_bonus",
    "compound.hidden_core_bonus",
    "compound.vtrac_straight_bonus",
    "compound.double_mirror_bonus",
    "compound.col2_funnel_bonus",
    "compound.vt_only_threshold",
    "compound.vt_only_bonus",
    "compound.hot2_cap",
    "compound.double_mirror_cap",
}


def _build_table(pattern_map, set_label="Set1", draw_label="Draw1"):
    rows = []
    for row_type in ["R2", "R4", "R6", "R8"]:
        row = {"RowType": row_type, "Set": set_label, "Draw": draw_label}
        for col in stable.COLS:
            row[col] = pattern_map.get(col, "")
        rows.append(row)
    return pd.DataFrame(rows)


def _build_scores(pattern_map, section="Combined"):
    df = _build_table(pattern_map)
    _, results = stable.analyse(df, section)
    return pd.DataFrame(results)


def test_output_schema():
    scores = _build_scores({"1": "227", "2": "277"})
    assert REQUIRED_ROW_COLUMNS.issubset(set(scores.columns))
    families = build_family_summary(scores, stable.CFG)
    assert REQUIRED_FAMILY_COLUMNS.issubset(set(families.columns))


def test_feature_config_schema():
    config_path = Path(stable.__file__).resolve().parent / "feature_config.yml"
    data = yaml.safe_load(config_path.read_text()) or {}
    assert REQUIRED_YAML_KEYS.issubset(set(data.keys()))


def test_api_surface():
    for attr in ("analyse", "build_html", "_eval_single_left"):
        assert hasattr(stable, attr)
    from alpha_analytical.stable import post_pass_families

    for attr in ("derive_vtrac_index_for_canonical", "build_family_summary"):
        assert hasattr(post_pass_families, attr)


def test_why_tokens_and_hidden():
    scores = _build_scores({"1": "9449"})
    row = scores.iloc[0]
    assert bool(row["hidden3v"]) is True
    assert "hidden3v" in row["why"].split("|")
    assert row["score_hidden"] == pytest.approx(stable.CFG.get("hidden3v_bonus", 0))
    assert "R2=9449" in str(row["source_literals"])
    if row["straight2"]:
        assert "vstr2" in row["why"]


def test_consensus_doubles_support():
    scores = _build_scores({"1": "227", "2": "277"})
    families = build_family_summary(scores, stable.CFG)
    fam_row = families[families["any_doubles_support"]].iloc[0]
    assert fam_row["fam_doubles"] == pytest.approx(stable.CFG.get("doubles_trigger_bonus", 0))


def test_golden_snapshot():
    scores = _build_scores({"1": "227", "2": "277"})
    best = scores.sort_values("score", ascending=False).iloc[0]
    assert best["score_cov"] > 0
    assert best["score_straight"] >= stable.CFG["baseline_straight_bonus"]
    assert best["score"] == pytest.approx(
        best["score_cov"]
        + best["score_hpr"]
        + best["score_perm"]
        + best["score_repeat"]
        + best["score_straight"]
        + best["score_single"]
        + best["score_cons"]
        + best["score_hot"]
        + best["score_mirror"]
        + best["score_dom"]
        + best["score_len"]
        + best["score_hidden"]
        + best["score_double_mirror"]
        + best["score_vtrac_straight"]
        + best["score_persistence_set"]
        + best["score_persistence_draw"]
    )


def test_family_score_parts_sum():
    scores = _build_scores({"1": "227", "2": "277"})
    families = build_family_summary(scores, stable.CFG)
    part_cols = [
        "fam_cov",
        "fam_hpr",
        "fam_perm",
        "fam_repeat",
        "fam_cons",
        "fam_hot",
        "fam_straight2",
        "fam_straight3",
        "fam_doubles",
        "fam_vtrac",
        "fam_hidden",
        "fam_double_mirror",
        "fam_persistence",
        "fam_section_bonus",
        "fam_progression_bonus",
        "fam_last_remaining_bonus",
    ]
    for _, row in families.iterrows():
        total = sum(float(row[col]) for col in part_cols)
        assert row["family_score"] == pytest.approx(total)


def test_last_remaining_bonus_respects_flag():
    scores = _build_scores({"1": "227", "2": "277"})
    families = build_family_summary(scores, stable.CFG)
    assert families.loc[~families["last_remaining_3v"], "fam_last_remaining_bonus"].eq(0).all()
