from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from alpha_analytical import stable
from alpha_analytical.stable.compound import compute_compound_scores
from alpha_analytical.stable.post_pass_families import build_family_summary
from scripts.tools.create_candidate_universe import (
    _parse_stable_compound_top,
    _parse_stable_family_vote,
    _parse_stable_last_remaining,
)


def _build_table(pattern_map, set_label="Set1", draw_label="Draw1"):
    rows = []
    for row_type in ["R2", "R4", "R6", "R8"]:
        row = {"RowType": row_type, "Set": set_label, "Draw": draw_label}
        for col in stable.COLS:
            row[col] = pattern_map.get(col, "")
        rows.append(row)
    return pd.DataFrame(rows)


def _build_scores(pattern_map, section="Combined", set_label="Set1", draw_label="Draw1"):
    df = _build_table(pattern_map, set_label=set_label, draw_label=draw_label)
    _, results = stable.analyse(df, section)
    return pd.DataFrame(results)


def _write_state_bundle(state_dir: Path, state_key: str = "TestState", include_last_remaining: bool = True) -> None:
    stable_dir = state_dir / "stable" / state_key
    stable_dir.mkdir(parents=True, exist_ok=True)

    frames = [
        _build_scores({"1": "9449"}, set_label="Set1", draw_label="Draw1"),
        _build_scores({"1": "2245"}, set_label="Set2", draw_label="Draw1"),
    ]
    if include_last_remaining:
        frames.append(_build_scores({"1": "227", "2": "277"}, set_label="Set1", draw_label="Draw1"))

    scores = pd.concat(frames, ignore_index=True)
    compound = compute_compound_scores(scores, stable.CFG)
    families = build_family_summary(scores, stable.CFG, compound)
    if not include_last_remaining:
        families["last_remaining_3v"] = False
        families["fam_last_remaining_bonus"] = 0.0

    scores.to_csv(stable_dir / f"{state_key}_stable_patterns_scores.csv", index=False)
    compound.to_csv(stable_dir / f"{state_key}_stable_patterns_compound.csv", index=False)
    families.to_csv(stable_dir / f"{state_key}_stable_patterns_families.csv", index=False)

    metrics = {
        "state": state_key,
        "generated_at": "2026-03-06T00:00:00+00:00",
        "total_patterns": int(len(scores)),
        "total_families": int(len(families)),
        "compression_ratio": 0.5,
        "avg_top_hot_density": 0.0,
        "health": {"compound_rows": int(len(compound)), "vt_only_lane": 0, "funnel_precol1": 0},
        "evidence_schema_version": 1,
        "stable_contract_version": 1,
        "compound_schema_version": 1,
        "signals": {"hot2_bias": True, "consensus_of_consensus": True},
    }
    (stable_dir / f"{state_key}_metrics.json").write_text(json.dumps(metrics), encoding="utf-8")


def test_stable_compound_top_emits_direct_three_digit_packs(tmp_path: Path):
    state_dir = tmp_path / "2026-03-06" / "TestState"
    _write_state_bundle(state_dir, include_last_remaining=True)

    packs, inputs = _parse_stable_compound_top(state_dir=state_dir, state_key="TestState", top_n=4)

    assert inputs
    assert packs
    assert all(pack["method_id"] == "stable_compound_top" for pack in packs)
    assert all(len(pack["canonicals"]) == 1 for pack in packs)
    assert all(len(pack["canonicals"][0]) == 3 for pack in packs)
    emitted = {pack["canonicals"][0] for pack in packs}
    assert "4499" not in emitted
    assert any(canon in emitted for canon in {"449", "227", "245"})


def test_stable_family_vote_emits_bounded_lane_closure_packs(tmp_path: Path):
    state_dir = tmp_path / "2026-03-06" / "TestState"
    _write_state_bundle(state_dir, include_last_remaining=True)

    packs, _ = _parse_stable_family_vote(
        state_dir=state_dir,
        state_key="TestState",
        top_n=2,
        max_cost_units=12,
    )

    assert packs
    pack = next(pack for pack in packs if pack["family_id"] == 26)
    assert pack["method_id"] == "stable_family_vote"
    assert pack["cost_units"] <= 12
    assert {"227", "277"}.issubset(set(pack["canonicals"]))
    assert pack["source_top_canonicals"]


def test_stable_last_remaining_emits_survivor_lane_pack_when_present(tmp_path: Path):
    state_dir = tmp_path / "2026-03-06" / "TestState"
    _write_state_bundle(state_dir, include_last_remaining=True)

    packs, _ = _parse_stable_last_remaining(
        state_dir=state_dir,
        state_key="TestState",
        top_n=3,
        max_cost_units=12,
    )

    assert packs
    pack = next(pack for pack in packs if pack["family_id"] == 26)
    assert pack["method_id"] == "stable_last_remaining"
    assert pack["last_remaining_rows"] >= 1
    assert pack["cost_units"] <= 12


def test_stable_last_remaining_is_zero_safe_when_no_survivor_rows(tmp_path: Path):
    state_dir = tmp_path / "2026-03-06" / "TestState"
    _write_state_bundle(state_dir, include_last_remaining=False)

    packs, inputs = _parse_stable_last_remaining(
        state_dir=state_dir,
        state_key="TestState",
        top_n=3,
        max_cost_units=12,
    )

    assert inputs
    assert packs == []
