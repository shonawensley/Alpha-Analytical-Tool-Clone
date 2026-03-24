from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from alpha_analytical import stable
from alpha_analytical.stable.compound import compute_compound_scores
from alpha_analytical.stable.post_pass_families import build_family_summary
from scripts.tools.stable_arena import (
    _build_hidden_family_reveal,
    _build_order_transform_hints,
    build_stable_arena_markdown,
    build_stable_arena_payload,
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


def _write_stable_bundle(base_dir: Path, state_key: str = "TestState") -> Path:
    state_dir = base_dir / state_key
    state_dir.mkdir(parents=True, exist_ok=True)

    scores = pd.concat(
        [
            _build_scores({"1": "9449"}, set_label="Set1", draw_label="Draw1"),
            _build_scores({"1": "227", "2": "277"}, set_label="Set1", draw_label="Draw1"),
            _build_scores({"1": "2245"}, set_label="Set2", draw_label="Draw1"),
            _build_scores({"1": "81100324*"}, set_label="Set1", draw_label="Draw2"),
            _build_scores({"1": "8847*"}, set_label="Set1", draw_label="Draw3"),
        ],
        ignore_index=True,
    )
    compound = compute_compound_scores(scores, stable.CFG)
    families = build_family_summary(scores, stable.CFG, compound)

    scores.to_csv(state_dir / f"{state_key}_stable_patterns_scores.csv", index=False)
    compound.to_csv(state_dir / f"{state_key}_stable_patterns_compound.csv", index=False)
    families.to_csv(state_dir / f"{state_key}_stable_patterns_families.csv", index=False)

    metrics = {
        "state": state_key,
        "generated_at": "2026-03-06T00:00:00+00:00",
        "total_patterns": int(len(scores)),
        "total_families": int(len(families)),
        "compression_ratio": 0.5,
        "avg_top_hot_density": 0.0,
        "winners": [],
        "winner_hits": [],
        "health": {"compound_rows": int(len(compound)), "vt_only_lane": 0, "funnel_precol1": 0},
        "evidence_schema_version": 1,
        "stable_contract_version": 1,
        "compound_schema_version": 1,
        "signals": {"hot2_bias": True, "consensus_of_consensus": True},
    }
    (state_dir / f"{state_key}_metrics.json").write_text(json.dumps(metrics), encoding="utf-8")
    return state_dir


def _build_payload(tmp_path: Path):
    results_date = "2026-03-06"
    sharepacks_root = tmp_path / "sharepacks" / "_predictive"
    state_dir = sharepacks_root / results_date / "TestState"
    stable_dir = state_dir / "stable"
    _write_stable_bundle(stable_dir, state_key="TestState")
    payload = build_stable_arena_payload(
        state_dir=state_dir,
        state_key="TestState",
        results_date=results_date,
        history_date="2026-03-05",
        profile="tool_only",
        experiment_tag="stable_arena_v1",
        sharepacks_root=sharepacks_root,
        contains_winners_artifacts=False,
        repo_root=tmp_path,
        top_rows=25,
        top_pattern_ledgers=25,
        top_compound=25,
        top_families=10,
    )
    assert payload is not None
    return payload


def test_stable_arena_preserves_detailed_scores_and_long_patterns(tmp_path: Path):
    payload = _build_payload(tmp_path)
    combined = payload["sections"]["Combined"]

    assert combined["summary"]["long_canonical_rows"] > 0
    assert combined["top_row_patterns"]
    assert any(item["long_canonical"] for item in combined["top_row_patterns"])
    assert "score_perm" in combined["top_row_patterns"][0]["score_breakdown"]
    assert "score_hidden" in combined["top_row_patterns"][0]["score_breakdown"]

    ledger_4499 = next(item for item in combined["pattern_ledgers_top"] if item["canonical"] == "4499")
    assert ledger_4499["long_canonical"] is True
    assert ledger_4499["score_breakdown_sums"]["score_hidden"] > 0
    assert ledger_4499["row_hits"] >= 1
    assert ledger_4499["top_box_contributions"]
    assert ledger_4499["top_box_contributions"][0]["box_label"].startswith("Set")
    assert ledger_4499["score_breakdown_peaks"]["score_hidden"]["locator"]
    assert ledger_4499["score_breakdown_peaks"]["score_hidden"]["value"] > 0
    assert ledger_4499["compound_context"] is not None
    assert ledger_4499["compound_context"]["compound_score"] >= ledger_4499["compound_context"]["base_max_score"]
    assert "columns" in ledger_4499["span"]
    top_row = combined["top_row_patterns"][0]
    assert "source_cells" in top_row


def test_stable_arena_builds_family_rollups_and_survivor_frontiers(tmp_path: Path):
    payload = _build_payload(tmp_path)
    combined = payload["sections"]["Combined"]

    assert combined["family_rollups_top"]
    assert "fam_perm" in combined["family_rollups_top"][0]["breakdown_sums"]

    frontiers = combined["survivor_frontiers"]
    assert frontiers
    frontier = next(item for item in frontiers if item["set"] == "Set1" and item["draw"] == "Draw1")
    assert frontier["frontier_column"] == 2
    assert frontier["progression_column_count"] == 2
    assert frontier["frontier_pattern_summary"]["exact3digit_patterns_top"]
    assert "hidden_terminal_patterns_top" in frontier["frontier_pattern_summary"]
    assert frontier["frontier_pattern_summary"]["top_patterns"]
    assert frontier["is_single_family"] is True
    assert frontier["entries"][0]["last_remaining_3v"] is True

    progressions = combined["survivor_progressions"]
    assert progressions
    progression = next(item for item in progressions if item["set"] == "Set1" and item["draw"] == "Draw1")
    assert progression["eligible_columns"] == [1, 2]
    assert progression["frontier_column"] == 2
    assert progression["column_summaries"][0]["pattern_summary"]["exact3digit_patterns_top"]


def test_stable_arena_ledgers_show_frontier_and_compounding_context(tmp_path: Path):
    payload = _build_payload(tmp_path)
    combined = payload["sections"]["Combined"]

    frontier_ledger = next(
        item for item in combined["pattern_ledgers_top"] if item["frontier_summary"]["frontier_row_hits"] > 0
    )
    assert frontier_ledger["frontier_summary"]["frontier_box_count"] >= 1
    assert frontier_ledger["top_modal_orders"]
    assert frontier_ledger["compound_context"] is not None
    assert "compound_lift_over_base_max" in frontier_ledger["compound_context"]
    assert frontier_ledger["top_box_contributions"][0]["example_locators"]


def test_stable_arena_builds_hidden_family_reveal_objects(tmp_path: Path):
    payload = _build_payload(tmp_path)
    combined = payload["sections"]["Combined"]

    row_234 = next(item for item in combined["top_row_patterns"] if item["canonical"] == "234")
    reveal = row_234["hidden_family_reveal"]
    assert reveal is not None
    assert reveal["target_family_id"] == 30
    assert reveal["top_fragments"]
    assert any(fragment["fragment"] == "324" for fragment in reveal["top_fragments"])
    assert reveal["digit_anchors"]
    assert row_234["source_cells"][0]["literal"].startswith("81100324")

    ledger_234 = next(item for item in combined["pattern_ledgers_top"] if item["canonical"] == "234")
    assert ledger_234["hidden_family_reveal_summary"]["row_hits"] >= 1
    assert ledger_234["hidden_family_reveal_summary"]["top_fragments"]

    family_30 = next(item for item in combined["family_rollups_top"] if item["family_id"] == 30)
    assert family_30["hidden_family_reveal_summary"]["row_hits"] >= 1
    assert family_30["hidden_family_reveal_summary"]["top_fragments"]


def test_order_transform_hints_surface_vt8_recipe_for_family_fragment():
    hints = _build_order_transform_hints(
        canonical="4788",
        family_id=30,
        modal_order="8847",
        modal_rows=4,
        hidden_family_reveal={
            "top_fragments": [
                {
                    "fragment": "8847",
                    "count": 12,
                    "modal_exact_hits": 2,
                    "modal_subsequence_hits": 0,
                    "digit_anchor_strength": 4,
                    "value_anchor_strength": 4,
                    "best_literal": "29688447",
                    "row_type": "R6",
                }
            ]
        },
    )
    assert hints is not None
    assert hints["top_seeds"][0]["seed"] == "847"
    vt8 = next(item for item in hints["top_transforms"] if item["method_id"] == "vt8_expand_ordered")
    assert "342" in vt8["combos"]


def test_stable_arena_surfaces_order_transform_summaries(tmp_path: Path):
    payload = _build_payload(tmp_path)
    combined = payload["sections"]["Combined"]

    row_478 = next(item for item in combined["top_row_patterns"] if item["canonical"] == "478")
    assert row_478["order_transform_hints"] is not None
    assert row_478["order_transform_hints"]["top_transforms"]
    assert any(
        item["seed"] == "847" and item["method_id"] == "vt8_expand_ordered" and "342" in item["combos"]
        for item in row_478["order_transform_hints"]["top_transforms"]
    )

    ledger_478 = next(item for item in combined["pattern_ledgers_top"] if item["canonical"] == "478")
    assert ledger_478["order_transform_summary"]["row_hits"] >= 1
    assert ledger_478["order_transform_summary"]["top_methods"]

    family_30 = next(item for item in combined["family_rollups_top"] if item["family_id"] == 30)
    assert family_30["order_transform_summary"]["row_hits"] >= 1
    assert any(item["value"] == "847" for item in family_30["order_transform_summary"]["top_seeds"])
    assert any(item["value"] == "vt8_expand_ordered" for item in family_30["order_transform_summary"]["top_methods"])


def test_hidden_family_reveal_skips_same_length_order_variants():
    reveal = _build_hidden_family_reveal(
        canonical="008",
        family_id=4,
        modal_order="008",
        column="1",
        source_cells=[
            {
                "row_type": "R6",
                "literal": "800**",
                "digits": "800",
                "hot_level": 0,
            }
        ],
    )
    assert reveal is None


def test_stable_arena_markdown_is_human_readable(tmp_path: Path):
    payload = _build_payload(tmp_path)
    md = build_stable_arena_markdown(payload)

    assert "Stable Arena" in md
    assert "Top pattern ledgers" in md
    assert "Compound" in md
    assert "Top Parts" in md
    assert "Reveal" in md
    assert "Transform" in md
    assert "Survivor frontiers recorded" in md
    assert "4499" in md
