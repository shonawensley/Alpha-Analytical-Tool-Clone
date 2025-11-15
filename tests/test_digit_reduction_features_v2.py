from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import pytest

from alpha_analytical.digit_reduction.analyzer_v2.features import ItemFeature, build_item_feature
from alpha_analytical.digit_reduction.analyzer_v2.pipeline import (
    FLAG_KIND_ORDER,
    _aggregate_metrics,
    _load_config,
)
from alpha_analytical.digit_reduction.analyzer_v2.score import score_row
from alpha_analytical.digit_reduction.analyzer_v2.types import Item, Key, Step


def _make_item(
    section: str,
    set_name: str,
    col: int,
    method: str,
    steps: List[Step],
    *,
    mode: str = "combined",
) -> Item:
    key = Key(
        state="TestState",
        area="LS1",
        section=section,
        set=set_name,
        draw="D1",
        col=col,
        method=method,
        mode=mode,
    )
    return Item(key=key, grid_position={}, sequence_meta={}, steps=steps, final={})


def _drop_family_steps() -> List[Step]:
    return [
        Step(step=0, value="992200", length=6, unique_digits=3, is_3value=False),
        Step(step=1, value="59900", length=5, unique_digits=3, is_3value=False),
        Step(step=2, value="590", length=3, unique_digits=3, is_3value=True),
    ]


def _dense_family_steps() -> List[Step]:
    return [
        Step(step=0, value="661188", length=6, unique_digits=3, is_3value=False),
        Step(step=1, value="6188", length=4, unique_digits=3, is_3value=False),
        Step(step=2, value="618", length=3, unique_digits=3, is_3value=True),
    ]


def test_build_item_feature_extracts_drop_metadata():
    config = _load_config()
    steps = _drop_family_steps()
    item = _make_item("Combined", "Set1", 7, "A", steps)
    feature = build_item_feature(item, config)
    row = feature.row
    assert row["drop_digit"] == "2"
    assert row["drop_run_len"] == 2
    assert row["earliest_exact_step"] == 1
    assert row["earliest_vtrac_step"] == 1
    assert row["box_family_density"] > 0.5
    assert row["dup_bonus"] >= 1.0


def test_aggregate_metrics_counts_columns_variants_methods():
    config = _load_config()
    items = [
        _make_item("Combined", "Set1", 7, "A", _drop_family_steps()),
        _make_item("Combined", "Set1", 6, "A", _drop_family_steps()),
        _make_item("Combined", "Set2", 7, "A", _drop_family_steps()),
        _make_item("Combined", "Set1", 7, "T", _drop_family_steps()),
        _make_item("Midday", "Set1", 7, "A", _drop_family_steps()),
    ]
    features = [build_item_feature(item, config) for item in items]
    _aggregate_metrics(features, config)

    lookup: Dict[tuple, Dict[str, any]] = {
        (
            f.row["section"],
            f.row["set"],
            f.row["col"],
            f.row["method"],
        ): f.row
        for f in features
    }

    set1 = lookup[("Combined", "Set1", 7, "A")]
    assert set1["cols_hit"] == 2
    assert set1["variants_hit"] == 2
    assert set1["method_consensus"] >= 2
    assert set1["recency_carryover"] == 1
    assert set1["box_pair_agree"] == 1

    set2 = lookup[("Combined", "Set2", 7, "A")]
    assert set2["recency_carryover"] == 0


def test_score_row_rewards_drop_quality_and_density():
    config = _load_config()
    base_row = {
        "earliest_exact_step": 1,
        "earliest_vtrac_step": 1,
        "earliest_drop_exact_step": 1,
        "earliest_drop_vtrac_step": 1,
        "earliest_family_exact_step": 1,
        "earliest_family_vtrac_step": 1,
        "box_family_density": 0.9,
        "dup_bonus": 2.0,
        "residual_purity": 0,
        "cols_hit": 3,
        "variants_hit": 2,
        "method_consensus": 2,
        "cluster_echo_count": 2,
        "variant_echo_count": 2,
        "set_echo_count": 2,
        "box_pair_agree": 1,
        "drop_run_len": 2,
        "drop_digit_mode_stability": 3,
        "recency_carryover": 1,
    }
    good = score_row(base_row.copy(), config)["score"]
    weaker_row = base_row.copy()
    weaker_row["drop_run_len"] = 5
    weaker_row["box_family_density"] = 0.2
    weaker = score_row(weaker_row, config)["score"]
    assert good > weaker

    baseline_row = base_row.copy()
    baseline_row["funnel_precol1"] = 0
    baseline_row["ls_col_42"] = 0
    baseline = score_row(baseline_row, config)["score_raw"]

    boosted_row = baseline_row.copy()
    boosted_row["funnel_precol1"] = 1
    boosted_row["ls_col_42"] = 1
    boosted = score_row(boosted_row, config)["score_raw"]
    assert boosted > baseline


def test_aggregate_metrics_sets_vt_only_and_funnel_flags():
    config = _load_config()

    def _base_row(col: int) -> Dict[str, any]:
        row: Dict[str, any] = {
            "state": "TestState",
            "area": "LS1",
            "section": "Combined",
            "set": "Set1",
            "draw": "Draw1",
            "col": col,
            "method": "A",
            "mode": "own",
            "family_id": "555",
        }
        for kind in FLAG_KIND_ORDER:
            row[f"earliest_{kind}_step"] = -1
            row[f"persistence_{kind}"] = 0
            row[f"final_{kind}_match"] = 0
        return row

    vt_row = _base_row(col=1)
    vt_row["earliest_vtrac_step"] = 1
    vt_row["final_vtrac_match"] = 1

    col4_row = _base_row(col=4)
    col4_row["earliest_vtrac_step"] = 2

    entries = [
        ItemFeature(row=vt_row, detail={}),
        ItemFeature(row=col4_row, detail={}),
    ]

    _aggregate_metrics(entries, config)

    assert entries[0].row["vt_only_lane"] == 1
    assert entries[0].row["funnel_precol1"] == 1
    assert entries[1].row["funnel_precol1"] == 1
    assert entries[1].row["ls_col_42"] == 1
